//! What the host GPU's memory is like (decision 0005's unified-memory item,
//! #880): unified with the CPU's (an APU, an integrated GPU, Apple silicon
//! under a translation layer) or its own, and whether the CPU maps part of
//! it.
//!
//! The console's GPU reads title memory where it is. Here host copies of it
//! are kept current at each submission (`crate::shadow`), which on a unified
//! host buys nothing: there the GPU reaches every placement at the same
//! speed, so the copies cost their CPU time and give no GPU time back. On a
//! discrete GPU video memory is much faster than system memory, and memory
//! the CPU maps there (GPU upload heaps, through Resizable BAR) changes how
//! copies in it are filled.
//!
//! [`detect`] asks the device: two feature queries and the memory budgets
//! (about 0.3 ms), logged once at host creation and named in the GPU
//! failure text. Nothing changes behaviour on it yet.

use windows::Win32::Graphics::Direct3D12::*;
use windows::Win32::Graphics::Dxgi::{
    CreateDXGIFactory2, DXGI_CREATE_FACTORY_FLAGS, DXGI_MEMORY_SEGMENT_GROUP,
    DXGI_MEMORY_SEGMENT_GROUP_LOCAL, DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL,
    DXGI_QUERY_VIDEO_MEMORY_INFO, IDXGIAdapter3, IDXGIFactory4,
};

/// What the host GPU's memory is like.
#[derive(Clone, Debug)]
pub(crate) struct Memory {
    /// The device says it shares memory with the CPU
    /// (`D3D12_FEATURE_DATA_ARCHITECTURE1::UMA`).
    pub(crate) uma: bool,
    /// And that the CPU's caches are coherent with it for every kind of
    /// memory (`CacheCoherentUMA`). AMD APUs say not, yet write-back system
    /// memory is coherent both ways there too.
    pub(crate) cache_coherent: bool,
    /// Video memory the CPU maps (`D3D12_HEAP_TYPE_GPU_UPLOAD`: Resizable
    /// BAR on a discrete GPU).
    pub(crate) gpu_upload_heaps: bool,
    /// The memory manager's budgets for this process, in MiB: local (video
    /// memory; all of it on a unified host) and non-local (system memory
    /// the GPU reaches; none on a unified host).
    pub(crate) budgets: Option<(u64, u64)>,
}

impl std::fmt::Display for Memory {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let kind = match (self.uma, self.gpu_upload_heaps) {
            (true, _) => "unified with the CPU's",
            (false, true) => "its own, the CPU maps part of it (Resizable BAR)",
            (false, false) => "its own",
        };
        write!(f, "{kind}")?;
        if self.uma {
            write!(f, ", cache-coherent {}", self.cache_coherent)?;
        }
        if let Some((local, non_local)) = self.budgets {
            write!(f, "; budgets {local} MiB local, {non_local} MiB non-local")?;
        }
        Ok(())
    }
}

/// What `device` reports about its memory.
pub(crate) fn detect(device: &ID3D12Device) -> Memory {
    let mut architecture = D3D12_FEATURE_DATA_ARCHITECTURE1::default();
    let mut options = D3D12_FEATURE_DATA_D3D12_OPTIONS16::default();
    // SAFETY: each query writes its own structure, of the given size.
    let (known, upload) = unsafe {
        let known = device
            .CheckFeatureSupport(
                D3D12_FEATURE_ARCHITECTURE1,
                (&raw mut architecture).cast(),
                size_of_val(&architecture) as u32,
            )
            .is_ok();
        let upload = device
            .CheckFeatureSupport(
                D3D12_FEATURE_D3D12_OPTIONS16,
                (&raw mut options).cast(),
                size_of_val(&options) as u32,
            )
            .is_ok()
            && options.GPUUploadHeapSupported.as_bool();
        (known, upload)
    };
    Memory {
        uma: known && architecture.UMA.as_bool(),
        cache_coherent: known && architecture.CacheCoherentUMA.as_bool(),
        gpu_upload_heaps: upload,
        budgets: budgets(device),
    }
}

/// The local and non-local budgets of `device`'s adapter, in MiB.
fn budgets(device: &ID3D12Device) -> Option<(u64, u64)> {
    // SAFETY: plain device and DXGI queries with valid out pointers.
    unsafe {
        let luid = device.GetAdapterLuid();
        let factory: IDXGIFactory4 = CreateDXGIFactory2(DXGI_CREATE_FACTORY_FLAGS(0)).ok()?;
        let adapter: IDXGIAdapter3 = factory.EnumAdapterByLuid(luid).ok()?;
        let budget = |group: DXGI_MEMORY_SEGMENT_GROUP| {
            let mut info = DXGI_QUERY_VIDEO_MEMORY_INFO::default();
            adapter.QueryVideoMemoryInfo(0, group, &mut info).ok()?;
            Some(info.Budget >> 20)
        };
        Some((
            budget(DXGI_MEMORY_SEGMENT_GROUP_LOCAL)?,
            budget(DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL)?,
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    /// WARP is a unified host.
    #[test]
    fn warp_is_unified() {
        // SAFETY: plain DXGI and device creation.
        let device = unsafe {
            let Ok(factory) = CreateDXGIFactory2::<IDXGIFactory4>(DXGI_CREATE_FACTORY_FLAGS(0))
            else {
                return;
            };
            let Ok(adapter) =
                factory.EnumWarpAdapter::<windows::Win32::Graphics::Dxgi::IDXGIAdapter>()
            else {
                return;
            };
            let mut device: Option<ID3D12Device> = None;
            let level = windows::Win32::Graphics::Direct3D::D3D_FEATURE_LEVEL_11_0;
            if D3D12CreateDevice(&adapter, level, &mut device).is_err() {
                return;
            }
            device.unwrap()
        };
        let memory = detect(&device);
        assert!(memory.uma, "{memory}");
        assert!(memory.to_string().starts_with("unified with the CPU's"), "{memory}");
    }

    /// The host device's answer (whatever it is), as the host logs it.
    #[test]
    fn the_host_device_is_described() {
        let Some(host) = crate::host::host() else {
            return;
        };
        let memory = &host.memory;
        assert!(memory.uma || !memory.cache_coherent, "{memory}");
        assert!(!memory.to_string().is_empty());
    }
}
