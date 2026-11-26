use std::collections::{BTreeMap, BTreeSet};
use std::path::Path;

use anyhow::{Context, Result};
use victory_pe::implib::{ImportLibrary, LibImport, LibImportKind};
use victory_pe::{ImageInfo, ImportSymbol, layout};

pub fn run(file: &Path, list_imports: bool, list_exports: bool) -> Result<()> {
    let data = std::fs::read(file).with_context(|| format!("reading {}", file.display()))?;
    let info = ImageInfo::parse(&data).with_context(|| format!("parsing {}", file.display()))?;

    println!("file           {}", file.display());
    println!("file size      {} bytes", data.len());
    println!("blake3         {}", blake3::hash(&data).to_hex());
    if let Some(cv) = &info.codeview {
        println!("pdb            {}  (key {})", cv.pdb_path, cv.symbol_key());
    }
    println!(
        "kind           {}",
        if info.is_dll() { "dll" } else { "exe" }
    );
    println!(
        "subsystem      {} ({})",
        info.subsystem,
        info.subsystem_name()
    );
    println!(
        "image base     {:#x}  size {:#x}",
        info.image_base, info.size_of_image
    );
    println!("entry rva      {:#x}", info.entry_rva);
    println!(
        "stack          reserve {:#x} commit {:#x}",
        info.stack_reserve, info.stack_commit
    );
    println!(
        "dll flags      {:#06x}{}",
        info.dll_characteristics,
        dll_flags(info.dll_characteristics)
    );
    println!(
        "relocations    {}   exception table {}   load config {}",
        yes(info.has_relocations),
        yes(info.has_exception_table),
        yes(info.has_load_config)
    );
    if let Some(tls) = &info.tls {
        println!("tls            {} callback(s)", tls.callback_rvas.len());
    }

    println!("\nsections");
    for s in &info.sections {
        println!(
            "  {:<8} rva {:#010x} vsize {:#010x} raw {:#010x} flags {:#010x}{}",
            s.name.trim_end_matches('\0'),
            s.rva,
            s.virtual_size,
            s.file_size,
            s.characteristics,
            section_flags(s.characteristics)
        );
    }

    println!(
        "\nimports        {} functions from {} DLLs",
        info.import_count(),
        info.imports.len()
    );
    for m in &info.imports {
        println!("  {:<48} {:>5}", m.dll, m.entries.len());
        if list_imports {
            for e in &m.entries {
                println!("      {}", e.symbol);
            }
        }
    }
    if !info.delay_imports.is_empty() {
        println!("\ndelay-load imports");
        for m in &info.delay_imports {
            println!("  {:<48} {:>5}", m.dll, m.entries.len());
            if list_imports {
                for e in &m.entries {
                    println!("      {}", e.symbol);
                }
            }
        }
    }

    println!("\nexports        {}", info.exports.len());
    if list_exports {
        for e in &info.exports {
            let name = e.name.as_deref().unwrap_or("(by ordinal)");
            match (&e.rva, &e.forward) {
                (_, Some(fwd)) => println!("  {:>5}  {name} -> {fwd}", e.ordinal),
                (Some(rva), _) => println!("  {:>5}  {name}  {rva:#x}", e.ordinal),
                _ => println!("  {:>5}  {name}", e.ordinal),
            }
        }
    }
    Ok(())
}

pub fn lib_exports(lib: &Path, list: bool) -> Result<()> {
    let data = std::fs::read(lib).with_context(|| format!("reading {}", lib.display()))?;
    let parsed =
        ImportLibrary::parse(&data).with_context(|| format!("parsing {}", lib.display()))?;
    let by_dll = group_lib_exports(&parsed.imports);
    let export_count: usize = by_dll.values().map(BTreeSet::len).sum();
    println!(
        "{export_count} exports from {} DLLs ({} other members)",
        by_dll.len(),
        parsed.other_members
    );
    for (dll, exports) in &by_dll {
        println!("{dll:<60} {:>5}", exports.len());
        if list {
            for (export, _) in exports {
                println!("    {export}");
            }
        }
    }
    Ok(())
}

fn group_lib_exports(
    imports: &[LibImport],
) -> BTreeMap<String, BTreeSet<(&ImportSymbol, LibImportKind)>> {
    let mut by_dll: BTreeMap<_, BTreeSet<_>> = BTreeMap::new();
    for import in imports {
        by_dll
            .entry(import.dll.to_ascii_lowercase())
            .or_default()
            .insert((&import.export, import.kind));
    }
    by_dll
}

fn yes(b: bool) -> &'static str {
    if b { "yes" } else { "no" }
}

fn dll_flags(v: u16) -> String {
    use layout::dll_flags::*;
    let names = [
        (HIGH_ENTROPY_VA, "high-entropy-va"),
        (DYNAMIC_BASE, "dynamic-base"),
        (FORCE_INTEGRITY, "force-integrity"),
        (NX_COMPAT, "nx"),
        (NO_ISOLATION, "no-isolation"),
        (NO_SEH, "no-seh"),
        (NO_BIND, "no-bind"),
        (APPCONTAINER, "appcontainer"),
        (WDM_DRIVER, "wdm-driver"),
        (GUARD_CF, "cfg"),
        (TERMINAL_SERVER_AWARE, "terminal-server-aware"),
    ];
    let mut set: Vec<String> = names
        .iter()
        .filter(|(f, _)| v & f != 0)
        .map(|(_, n)| (*n).to_string())
        .collect();
    // Bits without a name (the reserved ones) are shown rather than dropped.
    let unnamed = names.iter().fold(v, |rest, (f, _)| rest & !f);
    if unnamed != 0 {
        set.push(format!("{unnamed:#06x}"));
    }
    if set.is_empty() {
        String::new()
    } else {
        format!("  ({})", set.join(", "))
    }
}

/// The section's access as `rwx`, then its other named flags; bits without a
/// name here (alignment, linker-only ones) are shown in hex.
fn section_flags(v: u32) -> String {
    use layout::section_flags::*;
    let access = [(MEM_READ, 'r'), (MEM_WRITE, 'w'), (MEM_EXECUTE, 'x')];
    let names = [
        (CNT_CODE, "code"),
        (CNT_INITIALIZED_DATA, "initialized-data"),
        (CNT_UNINITIALIZED_DATA, "uninitialized-data"),
        (MEM_DISCARDABLE, "discardable"),
        (MEM_NOT_CACHED, "not-cached"),
        (MEM_NOT_PAGED, "not-paged"),
        (MEM_SHARED, "shared"),
    ];
    let mut set = vec![
        access
            .iter()
            .map(|&(f, c)| if v & f != 0 { c } else { '-' })
            .collect::<String>(),
    ];
    set.extend(
        names
            .iter()
            .filter(|(f, _)| v & f != 0)
            .map(|(_, n)| (*n).to_string()),
    );
    let unnamed = access
        .iter()
        .map(|&(f, _)| f)
        .chain(names.iter().map(|&(f, _)| f))
        .fold(v, |rest, f| rest & !f);
    if unnamed != 0 {
        set.push(format!("{unnamed:#010x}"));
    }
    format!("  ({})", set.join(", "))
}

#[cfg(test)]
mod tests {
    use super::*;

    fn import_archive(members: &[(&str, &str, u16)]) -> Vec<u8> {
        let mut archive = b"!<arch>\n".to_vec();
        for &(dll, name, kind) in members {
            let strings = format!("{name}\0{dll}\0");
            let size = 20 + strings.len();
            let header = format!("{:<16}{:<32}{size:<10}`\n", "import.obj/", "");
            archive.extend_from_slice(header.as_bytes());
            archive.extend_from_slice(b"\0\0\xff\xff\0\0"); // Signatures and version
            archive.extend_from_slice(&victory_pe::MACHINE_AMD64.to_le_bytes());
            archive.extend_from_slice(&0u32.to_le_bytes()); // Timestamp
            archive.extend_from_slice(&(strings.len() as u32).to_le_bytes());
            archive.extend_from_slice(&0u16.to_le_bytes()); // Hint
            archive.extend_from_slice(&(kind | (1 << 2)).to_le_bytes()); // Import by name
            archive.extend_from_slice(strings.as_bytes());
            if size % 2 == 1 {
                archive.push(b'\n');
            }
        }
        archive
    }

    #[test]
    fn lib_exports_deduplicates_dll_names_with_different_case() {
        let archive = import_archive(&[("Example.dll", "Foo", 0), ("example.dll", "Foo", 0)]);
        let parsed = ImportLibrary::parse(&archive).unwrap();
        assert_eq!(parsed.imports.len(), 2);

        let by_dll = group_lib_exports(&parsed.imports);
        assert_eq!(by_dll.len(), 1);
        let exports = &by_dll["example.dll"];
        assert_eq!(exports.len(), 1);
        assert_eq!(exports.first().unwrap().0.to_string(), "Foo");
    }

    #[test]
    fn lib_exports_preserves_distinct_symbols_kinds_and_dlls() {
        use LibImportKind::{Code, Data};

        let archive = import_archive(&[
            ("Example.dll", "Foo", 0),
            ("example.dll", "Bar", 0),
            ("example.dll", "Foo", 1),
            ("Other.dll", "Foo", 0),
        ]);
        let parsed = ImportLibrary::parse(&archive).unwrap();
        let by_dll = group_lib_exports(&parsed.imports);
        let exports: Vec<_> = by_dll["example.dll"]
            .iter()
            .map(|(export, kind)| (export.to_string(), *kind))
            .collect();
        assert_eq!(
            exports,
            [
                ("Bar".to_owned(), Code),
                ("Foo".to_owned(), Code),
                ("Foo".to_owned(), Data),
            ]
        );
        assert_eq!(by_dll.len(), 2);
        assert_eq!(by_dll["other.dll"].len(), 1);
    }

    #[test]
    fn section_flags_names_the_title_sections() {
        // Sections of the title executable of Series 1.0.2.1.
        assert_eq!(section_flags(0x6000_0020), "  (r-x, code)"); // .text
        assert_eq!(section_flags(0x4000_0040), "  (r--, initialized-data)"); // .rdata
        assert_eq!(section_flags(0xc000_0040), "  (rw-, initialized-data)"); // .data
        assert_eq!(
            section_flags(0x4200_0040),
            "  (r--, initialized-data, discardable)"
        ); // .reloc
        assert_eq!(section_flags(0), "  (---)"); // .retplne
    }

    #[test]
    fn section_flags_shows_bits_without_a_name() {
        // An alignment field (object files only) and a linker flag.
        assert_eq!(section_flags(0x6050_0820), "  (r-x, code, 0x00500800)");
        assert_eq!(
            section_flags(0xf000_0080),
            "  (rwx, uninitialized-data, shared)"
        );
    }

    #[test]
    fn dll_flags_names_every_bit_the_title_sets() {
        // The title executable of Series 1.0.2.1 carries 0x8160.
        assert_eq!(
            dll_flags(0x8160),
            "  (high-entropy-va, dynamic-base, nx, terminal-server-aware)"
        );
        assert_eq!(
            dll_flags(0x4160),
            "  (high-entropy-va, dynamic-base, nx, cfg)"
        );
    }

    #[test]
    fn dll_flags_shows_bits_without_a_name() {
        assert_eq!(dll_flags(0), "");
        assert_eq!(dll_flags(0x0001), "  (0x0001)");
        assert_eq!(
            dll_flags(0x0e41),
            "  (dynamic-base, no-isolation, no-seh, no-bind, 0x0001)"
        );
    }
}
