# VIctory Forge status

Generated 2026-11-26 06:48 UTC. Base: upstream `main` at `63bcca43c6`. Branch `forge/main` at `16b5bd14a2`: **361 of 1320 open pull requests** merged, building (`cargo check --workspace --all-targets`) and passing the asset policy (`cargo xtask policy`). Rules: [RULES.md](RULES.md).

| Result | Pull requests |
|---|---:|
| in forge | 361 |
| conflicts with pull requests | 457 |
| conflicts with main | 397 |
| breaks the build | 63 |
| changes CI workflows | 8 |
| draft | 34 |

## Tests on the branch

`cargo test --workspace --no-fail-fast`: **1322 passed, 125 failed, 30 ignored** (on the machine that ran the Forge; GPU tests skip where it has no GPU). Test failures do not keep a pull request out; they are listed for the authors.

- `bounded_execution_and_compiler_refusal`
- `dirty_pages_test::warp_dirty_pages`
- `emit::bvh_tests::intersections_on_nodes_in_title_memory_equal_the_reference`
- `emit::bvh_tests::intersections_on_the_gpu_equal_the_reference`
- `emit::bvh_tests::intersections_with_64_bit_pointers_on_the_gpu_equal_the_reference`
- `emit::bvh_tests::intersections_with_a16_on_the_gpu_equal_the_reference`
- `emit::bvh_tests::unsorted_box_intersections_on_the_gpu_equal_the_reference`
- `emit::memory_tests::heap_direct_texture_reads_mark_their_heap_index`
- `emit::memory_tests::root_views_read_their_copy_and_zeros_past_it`
- `emit::memory_tests::straddling_writes_across_256mib_and_4gib_boundaries_mark_exact_pages`
- `emit::memory_tests::title_memory_is_read_and_written_at_computed_addresses`
- `emit::memory_tests::writes_through_views_mark_their_pages`
- `emit::semantics_tests::arithmetic_matches_the_hardware`
- `emit::semantics_tests::byte_dot_products_match_the_hardware`
- `emit::semantics_tests::byte_packing_matches_the_hardware`
- `emit::semantics_tests::carries_match_the_hardware`
- `emit::semantics_tests::class_compares_match_the_hardware`
- `emit::semantics_tests::compares_match_the_hardware`
- `emit::semantics_tests::compares_of_denormals_agree_across_adapters`
- `emit::semantics_tests::constant_compares_run`
- `emit::semantics_tests::constant_results_run`
- `emit::semantics_tests::conversions_match_the_hardware`
- `emit::semantics_tests::cube_faces_match_the_hardware`
- `emit::semantics_tests::else_lanes_keep_their_registers`
- `emit::semantics_tests::f16_add_sub_round_to_zero_once`
- `emit::semantics_tests::f16_arithmetic_rounds_once`
- `emit::semantics_tests::f16_results_round_as_the_mode_says`
- `emit::semantics_tests::f16_results_round_to_nearest_even`
- `emit::semantics_tests::floor_conversions_match_the_hardware`
- `emit::semantics_tests::integers_match_the_hardware`
- `emit::semantics_tests::lds_bytes_and_halves_match_the_hardware`
- `emit::semantics_tests::lds_out_of_bounds_reads_zero_and_drops_writes`
- `emit::semantics_tests::masked_lanes_keep_their_registers`
- `emit::semantics_tests::med3_orders_signed_zeros`
- `emit::semantics_tests::min_max_and_clamp_match_the_hardware`
- `emit::semantics_tests::min_max_and_selects_take_denormals_on_the_bits`
- `emit::semantics_tests::mixed_precision_matches_the_hardware`
- `emit::semantics_tests::output_multipliers_give_positive_zero`
- `emit::semantics_tests::rounding_matches_the_hardware`
- `emit::semantics_tests::scalar_alu_matches_the_hardware`
- `emit::semantics_tests::scalar_min_max_set_scc_from_the_compare`
- `emit::semantics_tests::selects_match_the_hardware`
- `emit::semantics_tests::sixteen_bit_floats_match_the_hardware`
- `emit::semantics_tests::source_modifiers_set_the_sign_of_a_nan`
- `emit::semantics_tests::sub_dword_operands_match_the_hardware`
- `emit::semantics_tests::transcendental_specials_match_the_hardware`
- `emit::semantics_tests::whole_wave_sections_keep_rounding_mode_changes`
- `emit::semantics_tests::wide_shifts_match_the_hardware`
- `emit::stride_tests::a_constant_buffer_through_the_heap_reads_as_a_raw_buffer`
- `emit::stride_tests::a_half_buffer_load_reads_the_half_at_its_address`
- `emit::stride_tests::a_heap_buffer_read_by_element_takes_the_views_stride`
- `emit::stride_tests::a_heap_buffer_read_where_no_buffer_view_is_reads_zeros`
- `emit::stride_tests::a_sampler_chosen_by_a_uniform_branch_samples_as_chosen`
- `emit::stride_tests::d16_typed_buffer_accesses_pass_bits_through_integer_views`
- `emit::stride_tests::d16_x_loads_read_r16_uint_and_r16_float_views`
- `emit::stride_tests::half_buffer_stores_leave_the_other_half_alone`
- `emit::synthetic_tests::empty_root_constants_bind_zero_in_draw_and_dispatch`
- `emit::synthetic_tests::gathers_at_a_level_match_the_hardware`
- `emit::synthetic_tests::global_stores_keep_each_lanes_offset_after_exec_is_restored`
- `emit::synthetic_tests::pops_wait_loop_exits_immediately_for_inactive_lanes`
- `emit::tests::edge_flagged_triangles_draw_as_unflagged_ones`
- `emit::tests::v_interp_p2_f16_modifiers_narrow_once_in_mode16`
- `emit::valu_tests::a_branch_to_fallthrough_keeps_both_values_at_a_join`
- `emit::valu_tests::bcpack_bc6_index_width_for_every_mode`
- `emit::valu_tests::bcpack_nibble_split_matches_the_formats_function`
- `emit::valu_tests::bfe_signed_and_unsigned_match_rdna2`
- `emit::valu_tests::cvt_f32_f64_applies_e64_source_and_output_modifiers`
- `emit::valu_tests::cvt_f32_f64_decodes_double_inline_constants`
- `emit::valu_tests::cvt_f32_f64_matches_rdna2`
- `emit::valu_tests::cvt_f32_f64_uses_literal_as_the_high_word`
- `emit::valu_tests::f16_max_and_min_order_negative_zero_below_positive_zero`
- `emit::valu_tests::f64_add_mul_and_fma_are_ieee`
- `emit::valu_tests::f64_arithmetic_reads_sgpr_pairs`
- `emit::valu_tests::f64_conversions_match_rdna2`
- `emit::valu_tests::f64_max_and_min_order_zeros_and_skip_nan`
- `emit::valu_tests::f64_reads_uniform_pairs_at_odd_dwords`
- `emit::valu_tests::f64_sources_apply_abs_and_neg`
- `emit::valu_tests::fspx_programs_run_with_the_hardwares_dot_products`
- `emit::valu_tests::mad_i64_i32_sign_extends_literal_addend`
- `emit::valu_tests::max_and_min_order_negative_zero_below_positive_zero`
- `emit::valu_tests::med3_orders_negative_zero_below_positive_zero`
- `emit::valu_tests::normalized_buffer_formats_load_correctly_rounded_quotients`
- `emit::valu_tests::normalized_buffer_formats_load_their_ends_exactly`
- `emit::valu_tests::normalized_codes_truncate_back_to_themselves`
- `emit::valu_tests::packed_add_selects_halves_of_inline_constants`
- `emit::valu_tests::packed_fmac_accumulates_each_half`
- `emit::valu_tests::relative_moves_reach_only_what_their_clamped_index_can`
- `emit::valu_tests::s_cmpk_compares_against_the_extended_immediate`
- `emit::valu_tests::s_lshl_add_shifts_the_first_operand_then_adds`
- `emit::valu_tests::scalar_quad_masks_pack_nibbles_and_set_scc`
- `emit::valu_tests::signed_64_bit_operands_sign_extend_their_literal`
- `emit::valu_tests::src_scc_reads_as_zero_or_one`
- `emit::valu_tests::tbuffer_d16_loads_pack_two_channels_per_dword`
- `emit::valu_tests::v_cmp_class_f16_matches_rdna2`
- `emit::valu_tests::v_cmp_f64_matches_ieee`
- `emit::valu_tests::v_cmp_lg_is_false_for_nan`
- `emit::valu_tests::v_cmp_u64_and_i64_order_by_the_high_dword`
- `emit::valu_tests::v_cvt_f16_u16_and_i16_widen_the_integer_first`
- `emit::valu_tests::v_cvt_norm_i16_and_u16_f16_round_the_exact_product`
- `emit::valu_tests::v_cvt_off_f32_i4_uses_the_signed_low_nibble`
- `emit::valu_tests::v_cvt_u16_and_i16_f16_saturate`
- `emit::valu_tests::v_fract_f16_never_returns_one`
- `emit::valu_tests::v_fract_f32_never_returns_one`
- `emit::valu_tests::v_med3_f16_matches_rdna2_with_nan`
- `emit::valu_tests::v_med3_f32_matches_rdna2_with_nan`
- `emit::valu_tests::v_min3_max3_med3_integer_forms_match_rdna2`
- `emit::valu_tests::v_mul_legacy_f32_treats_denormals_as_zero`
- `emit::valu_tests::v_perm_b32_matches_rdna2`
- `emit::valu_tests::v_sin_and_v_cos_f16_reduce_large_turns`
- `emit::valu_tests::v_sin_and_v_cos_f32_reduce_large_turns`
- `emit::valu_tests::xma_integer_log2_handles_both_words`
- `emit::valu_tests::xma_sample_to_i16_handles_ties_and_saturation`
- `emit::waterfall_tests::lanes_load_from_the_buffer_their_nested_arms_chose`
- `emit::waterfall_tests::lanes_sample_the_entry_their_offset_names_in_the_console_waterfall`
- `emit::waterfall_tests::lanes_sample_the_texture_their_arm_loaded_or_picked`
- `emit::waterfall_tests::lanes_sample_the_texture_their_if_else_arm_chose`
- `emit::waterfall_tests::lanes_sample_their_own_texture_in_a_waterfall_narrowed_by_v_cmpx`
- `modules::gameinput::tests::query_interface_answers_identity_and_the_objects_own_iid`
- `modules::gameinput::tests::reading_callbacks_filter_changes_and_stop`
- `modules::storage::tests::the_path_is_the_drive_root_and_its_nul`
- `root::tests::host_serialized_blobs_create_root_signatures`
- `root::tests::malformed_blobs_are_rejected_by_the_host`
- `root::tests::our_blobs_deserialize_on_the_host`
- `root::tests::versioned_descriptions_serialize_on_the_host`
- `the_conformance_title_runs_through_victory`

## Since the last run

Joined the branch: #189, #457, #485, #583, #1013, #1262, #1264, #1361, #1362, #1653, #1703, #1772, #1811, #1824, #1859, #1879, #1922, #1942, #1963, #1991, #2012, #2039, #2075, #2111, #2115, #2118, #2150, #2173, #2187, #2219, #2223, #2238, #2269, #2273, #2276, #2278, #2282, #2295, #2298, #2332, #2452, #2486, #2512, #2524, #2528, #2554, #2557, #2587, #2607, #2629, #2639, #2659, #2678, #2706, #2727, #2761, #2766, #2769, #2794, #2798, #2800, #2804, #2805, #2806, #2808, #2809, #2812, #2814, #2816, #2818, #2820, #2823, #2828, #2838, #2839, #2845, #2850, #2855, #2858, #2859, #2869, #2873, #2878, #2882, #2886, #2887, #2889, #2896, #2897, #2901, #2902, #2904, #2906, #2909, #2910, #2912, #2917, #2919, #2921, #2922, #2923, #2931, #2935, #2944, #2947, #2950, #2952, #2955, #2961, #2962, #2964, #2966, #2979, #2980, #2981, #2989, #2990, #2991, #2998, #3001, #3002, #3006, #3014, #3015, #3019, #3020, #3024, #3030, #3034, #3038, #3049, #3052, #3054.

Left the branch (closed, merged upstream, or now conflicting or failing): #114, #139, #158, #166, #259, #284, #328, #379, #385, #395, #415, #421, #506, #535, #613, #684, #983, #1009, #1033, #1046, #1152, #1155, #1195, #1203, #1205, #1207, #1209, #1259, #1324, #1329, #1364, #1365, #1383, #1424, #1492, #1537, #1614, #1628, #1657, #1700, #1720, #1728, #1766, #1778, #1790, #1798, #1806, #1807, #1821, #1833, #1839, #1852, #1863, #1865, #1887, #1894, #1895, #1897, #1913, #1914, #1916, #1927, #1931, #1988, #2007, #2008, #2015, #2021, #2031, #2036, #2043, #2044, #2052, #2067, #2073, #2081, #2088, #2098, #2109, #2110, #2114, #2147, #2154, #2155, #2159, #2162, #2164, #2168, #2172, #2198, #2200, #2218, #2225, #2234, #2239, #2241, #2243, #2262, #2286, #2299, #2301, #2304, #2306, #2340, #2344, #2377, #2386, #2387, #2388, #2403, #2416, #2455, #2462, #2464, #2471, #2493, #2507, #2510, #2515, #2530, #2531, #2534, #2546, #2556, #2577, #2580, #2596, #2611, #2640, #2654, #2674, #2681, #2684, #2703, #2717, #2796.

## in forge (361)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#24](https://github.com/Marvisak/VIctory/pull/24) | GPU: run indirect mesh dispatches (DispatchMeshX) through indirect execution | artor410 |  |
| [#76](https://github.com/Marvisak/VIctory/pull/76) | xmem: map a run of physical pages over several placeholders | SuryaK5125 |  |
| [#105](https://github.com/Marvisak/VIctory/pull/105) | Shaders: a loop that branches back to the entry instruction translates | tedin7 |  |
| [#151](https://github.com/Marvisak/VIctory/pull/151) | Link victory.exe with a 16 MiB default thread stack | ItsYusei99 |  |
| [#188](https://github.com/Marvisak/VIctory/pull/188) | Loader: find TLS-array load candidates sixteen offsets at a time (8-9x faster scan) | TG0000 |  |
| [#189](https://github.com/Marvisak/VIctory/pull/189) | Shaders: emulate Wave64 compute shaders on Wave32 and narrower hosts | alfycs |  |
| [#212](https://github.com/Marvisak/VIctory/pull/212) | GPU, HLE: report host display HDR luminance and configure swap chain color space | n-romanovich |  |
| [#228](https://github.com/Marvisak/VIctory/pull/228) | XGameSave: a failed create leaves a null handle, as documented | Dufftwt |  |
| [#240](https://github.com/Marvisak/VIctory/pull/240) | DSP: convolve reverb streams on the host | Quat3rnion |  |
| [#280](https://github.com/Marvisak/VIctory/pull/280) | README: a hard drive keeps the first screen black for ~90 s | curnpoo |  |
| [#324](https://github.com/Marvisak/VIctory/pull/324) | fix(pe): detect incomplete TLS callback arrays | pedrofort |  |
| [#343](https://github.com/Marvisak/VIctory/pull/343) | Shaders: reject overlapping DXBC container parts | pedrofort |  |
| [#364](https://github.com/Marvisak/VIctory/pull/364) | XMA: accelerate VLC decoding with an eight-bit prefix lookup | pedrofort |  |
| [#369](https://github.com/Marvisak/VIctory/pull/369) | Shaders: eliminate heap allocations during CFG traversal | pedrofort |  |
| [#378](https://github.com/Marvisak/VIctory/pull/378) | CLI: include runtime shader hashes in the translation listing | Mesrine67 |  |
| [#398](https://github.com/Marvisak/VIctory/pull/398) | HLE: report the single supported offline user | ToxicmaggotRP |  |
| [#446](https://github.com/Marvisak/VIctory/pull/446) | HLE: report required size on string getter buffer errors | enzoduarte1 |  |
| [#450](https://github.com/Marvisak/VIctory/pull/450) | GPU: preserve typed null render target slots | fuzeofficlal |  |
| [#454](https://github.com/Marvisak/VIctory/pull/454) | Loader: opt-in VICTORY_NO_WATCHDOG hook for the title's watchdog (build 1.0.2.1) | ruvenesh |  |
| [#457](https://github.com/Marvisak/VIctory/pull/457) | fix(shader): accept overwritten VGPR inputs in counted indexed writes | jeremygold02 |  |
| [#477](https://github.com/Marvisak/VIctory/pull/477) | Shaders: fix DXIL validator UB on null error blobs, unchecked GetStatus, and COM/DLL handle leaks | nathanbzrr |  |
| [#478](https://github.com/Marvisak/VIctory/pull/478) | Audio capture: guard WASAPI timestamp underflow and stream silence writes | nathanbzrr |  |
| [#485](https://github.com/Marvisak/VIctory/pull/485) | GPU: preserve compatible read states for read-only depth targets | fuzeofficlal |  |
| [#486](https://github.com/Marvisak/VIctory/pull/486) | shader: opt the test binaries into an app-local Agility SDK runtime | naixue2233 |  |
| [#491](https://github.com/Marvisak/VIctory/pull/491) | GPU: remember pipelines whose creation crashed the process (VICTORY_PIPELINE_JOURNAL) | desplmfao |  |
| [#505](https://github.com/Marvisak/VIctory/pull/505) | Tests: add synthetic Xbox runtime conformance under Wine | pedrofort |  |
| [#512](https://github.com/Marvisak/VIctory/pull/512) | HLE: resolve ordinals on pseudo-module handles | Quat3rnion |  |
| [#517](https://github.com/Marvisak/VIctory/pull/517) | CLI: report incomplete shader directory scans | Dathinel |  |
| [#522](https://github.com/Marvisak/VIctory/pull/522) | HLE: validate null package identifier in XPackage methods | pushkarreddyy |  |
| [#541](https://github.com/Marvisak/VIctory/pull/541) | GPU: retain D3D12 object names in private data | broccolize |  |
| [#545](https://github.com/Marvisak/VIctory/pull/545) | xtask: add qa command to run policy, rustfmt, and clippy checks | pushkarreddyy |  |
| [#580](https://github.com/Marvisak/VIctory/pull/580) | Docs: add a contributor onboarding guide | lucaseddd |  |
| [#583](https://github.com/Marvisak/VIctory/pull/583) | fix(gpu): respect indirect count buffer and bind null root views | matheusfrta |  |
| [#590](https://github.com/Marvisak/VIctory/pull/590) | HLE: reject duplicate blob changes in one save update | Quat3rnion |  |
| [#601](https://github.com/Marvisak/VIctory/pull/601) | GPU: bound texture upload and capture slices to the allocated buffer | AwsAli05 |  |
| [#602](https://github.com/Marvisak/VIctory/pull/602) | GPU: report retained snapshot, texture scratch and upload memory | lucaseddd |  |
| [#660](https://github.com/Marvisak/VIctory/pull/660) | Shaders: drop a wave64 mask whose low dword is seen with two high dwords | coderanonymus |  |
| [#673](https://github.com/Marvisak/VIctory/pull/673) | Make translate failure examples stable across workers | timorjay |  |
| [#677](https://github.com/Marvisak/VIctory/pull/677) | Build: thin LTO for release and diag builds | wbkepler |  |
| [#686](https://github.com/Marvisak/VIctory/pull/686) | docs: check archive integrity after an early boot breakpoint | TomEageer |  |
| [#703](https://github.com/Marvisak/VIctory/pull/703) | Formats: eliminate BCPack per-call allocations and optimize streaming decode | wbkepler |  |
| [#708](https://github.com/Marvisak/VIctory/pull/708) | fix(config): keep the data directory out of the cache root | Loggerten |  |
| [#927](https://github.com/Marvisak/VIctory/pull/927) | GameInput: held keys are reported in the order they were pressed, as documented | BastienRodz |  |
| [#933](https://github.com/Marvisak/VIctory/pull/933) | GPU: report allocated mips from GetDesc | enzoduarte1 |  |
| [#939](https://github.com/Marvisak/VIctory/pull/939) | HLE: XSystemGetXboxLiveSandboxId refuses a buffer under 16 bytes | LouisRiverstone |  |
| [#997](https://github.com/Marvisak/VIctory/pull/997) | HLE: prevent automatic WinHTTP redirects | Hiiva |  |
| [#1010](https://github.com/Marvisak/VIctory/pull/1010) | GPU: copy title memory into host memory without a system call | TG0000 |  |
| [#1013](https://github.com/Marvisak/VIctory/pull/1013) | perf(shader): speed up control-flow structurisation | matheusfrta |  |
| [#1065](https://github.com/Marvisak/VIctory/pull/1065) | Shaders: use validator 1.8 for compute derivatives | Halfect |  |
| [#1110](https://github.com/Marvisak/VIctory/pull/1110) | fix(hle): account for save replacements before clamping quota | divyeshganta |  |
| [#1111](https://github.com/Marvisak/VIctory/pull/1111) | fix(loader): preserve protection regions when binding unaligned imports | divyeshganta |  |
| [#1113](https://github.com/Marvisak/VIctory/pull/1113) | Formats: lay out packed RGB textures as horizontal texel pairs | Razdva122 |  |
| [#1123](https://github.com/Marvisak/VIctory/pull/1123) | Validate XGameSave blob count before reading | EatCodeSleep2 |  |
| [#1174](https://github.com/Marvisak/VIctory/pull/1174) | HLE: implement IUnknown::QueryInterface and unit tests for xgame objects | geiyiliyabumo |  |
| [#1193](https://github.com/Marvisak/VIctory/pull/1193) | HLE: add synthetic unit tests for storage.rs and host.rs | geiyiliyabumo |  |
| [#1194](https://github.com/Marvisak/VIctory/pull/1194) | HLE: extract installed_package and add focused xstore license/package tests | geiyiliyabumo |  |
| [#1196](https://github.com/Marvisak/VIctory/pull/1196) | HLE: fix self-closing XML element body parsing in runtime.rs and add unit tests | geiyiliyabumo |  |
| [#1199](https://github.com/Marvisak/VIctory/pull/1199) | HLE: return NOT_SUPPORTED early for null out in QueryApiImpl without marking area missing | geiyiliyabumo |  |
| [#1212](https://github.com/Marvisak/VIctory/pull/1212) | HLE: expand synthetic unit tests for apu.rs (1 -> 19 tests) | geiyiliyabumo |  |
| [#1218](https://github.com/Marvisak/VIctory/pull/1218) | xtask: wine-test runs the Windows tests on a Linux host under Wine | neonbyte1 |  |
| [#1253](https://github.com/Marvisak/VIctory/pull/1253) | Shaders: ignore pre-loop table loads when proving waterfall offsets | mgunes1311-lab |  |
| [#1262](https://github.com/Marvisak/VIctory/pull/1262) | Shaders: double-precision add, mul, fma, min, max, compares and conversions (stacked on #416) | MamaLeVrai |  |
| [#1263](https://github.com/Marvisak/VIctory/pull/1263) | Shader: the loop limit switch works in every build | pablogonz12 |  |
| [#1264](https://github.com/Marvisak/VIctory/pull/1264) | HLE: map a page scatter in runs, not one page at a time | pablogonz12 |  |
| [#1278](https://github.com/Marvisak/VIctory/pull/1278) | Docs: add testing.md | DrummingBird1 |  |
| [#1283](https://github.com/Marvisak/VIctory/pull/1283) | Clarify DRED reports when GPU progress is unknown | DoubleD17 |  |
| [#1303](https://github.com/Marvisak/VIctory/pull/1303) | Shaders: bounds-check DXIL header offsets and recognize dword zero padding | geiyiliyabumo |  |
| [#1304](https://github.com/Marvisak/VIctory/pull/1304) | Loader: fix thread shutdown targeting, registry lifetime, and CRT detach ordering | geiyiliyabumo |  |
| [#1306](https://github.com/Marvisak/VIctory/pull/1306) | Loader: fix thunk block overflow, capacity enforcement, flush errors, and leaks | geiyiliyabumo |  |
| [#1335](https://github.com/Marvisak/VIctory/pull/1335) | test(shader): translate random GFX10 programs on every test run | Levichu51 |  |
| [#1361](https://github.com/Marvisak/VIctory/pull/1361) | Shaders: hardware probe for s_flbit_i32 | LouisRiverstone |  |
| [#1362](https://github.com/Marvisak/VIctory/pull/1362) | Shaders: hardware test for s_lshl1..4_add_u32 | LouisRiverstone |  |
| [#1406](https://github.com/Marvisak/VIctory/pull/1406) | GPU: fix NULL/UNKNOWN SRV/UAVs on promoted-typeless textures and MSAA/array/3D NULL RTV/DSVs | ESAT586 |  |
| [#1414](https://github.com/Marvisak/VIctory/pull/1414) | GPU: avoid clobbering HostList prelude allocator when a list executes twice in one submission | ESAT586 |  |
| [#1418](https://github.com/Marvisak/VIctory/pull/1418) | [BUNDLE] GPU fixes (write watch, textures, device, DXGI, objects, primitives, capture): 9 PRs, #553 #153 #270 #1158 #1204 #1220 #488 #1146 #631 (rebuilt on main 70564ae) | MamaLeVrai |  |
| [#1428](https://github.com/Marvisak/VIctory/pull/1428) | GPU: guard OMSetRenderTargets handle expansion on empty, null, or oversized calls | fuzeofficlal |  |
| [#1445](https://github.com/Marvisak/VIctory/pull/1445) | HLE reuses freed physical page numbers | BaggyALPHA |  |
| [#1457](https://github.com/Marvisak/VIctory/pull/1457) | DirectStorage: keep raw reads running while staging drains | Luizbc2 |  |
| [#1505](https://github.com/Marvisak/VIctory/pull/1505) | GPU: pipeline workers at the title's priority, not below it | KevinPratap |  |
| [#1547](https://github.com/Marvisak/VIctory/pull/1547) | GPU: invalidate HOST_WRITTEN textures when title memory is written | n-romanovich |  |
| [#1548](https://github.com/Marvisak/VIctory/pull/1548) | GPU: preserve full DYNAMIC descriptor range when host view heap is capped at PORTABLE_VIEWS | n-romanovich |  |
| [#1555](https://github.com/Marvisak/VIctory/pull/1555) | GPU: coalesce nearby shadow-buffer refreshes without spanning huge heap gaps | Texbirds |  |
| [#1557](https://github.com/Marvisak/VIctory/pull/1557) | Validate BC7 control-word subset counts | oddmaniv |  |
| [#1564](https://github.com/Marvisak/VIctory/pull/1564) | GPU: MakeResident succeeds, as the console's memory is always resident | LouisRiverstone |  |
| [#1571](https://github.com/Marvisak/VIctory/pull/1571) | GPU: add diagnostics for shader dependency wait times | srijann07 |  |
| [#1584](https://github.com/Marvisak/VIctory/pull/1584) | GPU: add opt-in idle shader cache trimming | srijann07 |  |
| [#1593](https://github.com/Marvisak/VIctory/pull/1593) | [BUNDLE] Shader translation speed: 4 PRs, #288 #369 #1033 #1180 (rebuilt on main 70564ae) | MamaLeVrai |  |
| [#1621](https://github.com/Marvisak/VIctory/pull/1621) | bound the bytes one part's native blobs unpack to and hand out | imjustprism |  |
| [#1653](https://github.com/Marvisak/VIctory/pull/1653) | victory-gpu: split the pipeline library into shards so a save writes only what changed (was 600 MB per save) | pes7 |  |
| [#1676](https://github.com/Marvisak/VIctory/pull/1676) | Shaders, CLI: name a host without mesh shaders in the pipeline census | fiestorra |  |
| [#1681](https://github.com/Marvisak/VIctory/pull/1681) | GPU: verify exact dirty-page masks on D3D12 | avt0m4t48 |  |
| [#1701](https://github.com/Marvisak/VIctory/pull/1701) | GPU: VICTORY_MODE overrides the reported console display mode | Calvix2k |  |
| [#1703](https://github.com/Marvisak/VIctory/pull/1703) | README: the GPU timing switch needs DRED for the per-command notes | fiestorra |  |
| [#1716](https://github.com/Marvisak/VIctory/pull/1716) | victory-shader: fold constants and eliminate dead pure ops in bitcode | bartikele |  |
| [#1719](https://github.com/Marvisak/VIctory/pull/1719) | DirectStorage: clear the factory out pointer on failure | davutsimsekk |  |
| [#1722](https://github.com/Marvisak/VIctory/pull/1722) | GPU: the host pipeline library works under Wine (null blob for an empty library) | Impre-visible |  |
| [#1741](https://github.com/Marvisak/VIctory/pull/1741) | Docs: AGENTS.md for AI agents working on VIctory | ThiagoAlexsander |  |
| [#1765](https://github.com/Marvisak/VIctory/pull/1765) | GPU tests: the castable pair is two host textures where the host refuses castable formats | AgneyaK |  |
| [#1770](https://github.com/Marvisak/VIctory/pull/1770) | Descriptor tests: take the capped heap's design into account | kais7654 |  |
| [#1772](https://github.com/Marvisak/VIctory/pull/1772) | HLE: handle verbatim/drive-root mounts and UNC/verbatim GetDiskFreeSpaceW roots | n-romanovich |  |
| [#1776](https://github.com/Marvisak/VIctory/pull/1776) | GPU: exclude 4:2:2 packed formats 68/69 from castable texture formats | 0xKaji |  |
| [#1784](https://github.com/Marvisak/VIctory/pull/1784) | Test Wave32 spilled lane masks at control-flow joins | rezioliver-collab |  |
| [#1787](https://github.com/Marvisak/VIctory/pull/1787) | GPU: textures drop unordered access in formats the host cannot write (NVIDIA B5G5R5A1) | Danigamer05 |  |
| [#1792](https://github.com/Marvisak/VIctory/pull/1792) | Formats: reject texture mip counts beyond the full chain | VlREX |  |
| [#1794](https://github.com/Marvisak/VIctory/pull/1794) | Shaders: support BVH a16 ray directions and unsorted box nodes | ESAT586 |  |
| [#1797](https://github.com/Marvisak/VIctory/pull/1797) | XMA: reject frame starts in packet headers | VlREX |  |
| [#1802](https://github.com/Marvisak/VIctory/pull/1802) | Perf/shader relative shift bounds | VlREX |  |
| [#1805](https://github.com/Marvisak/VIctory/pull/1805) | CLI: write pipeline key listings in stable pack order | EatCodeSleep2 |  |
| [#1809](https://github.com/Marvisak/VIctory/pull/1809) | CLI: list pipeline keys without initializing caches | EatCodeSleep2 |  |
| [#1811](https://github.com/Marvisak/VIctory/pull/1811) | Shader tests: run v_perm_b32 on the GPU | n-romanovich |  |
| [#1814](https://github.com/Marvisak/VIctory/pull/1814) | PE tests: cover ImportLibrary::parse short imports and archive errors | n-romanovich |  |
| [#1816](https://github.com/Marvisak/VIctory/pull/1816) | GPU: account for delivered bytes in bulk copyback | aycow |  |
| [#1822](https://github.com/Marvisak/VIctory/pull/1822) | Speech: the title's narration plays through the host's SAPI voice | kais7654 |  |
| [#1823](https://github.com/Marvisak/VIctory/pull/1823) | Shaders: bound a signature part's register rows and its allocation | slatefield |  |
| [#1824](https://github.com/Marvisak/VIctory/pull/1824) | Shaders: declare each dx.op call once | slatefield |  |
| [#1825](https://github.com/Marvisak/VIctory/pull/1825) | GPU: keep the view-stride table once per list, not per draw stage | slatefield |  |
| [#1827](https://github.com/Marvisak/VIctory/pull/1827) | HLE: enumerate the current installation for XPackageKind::Game | n-romanovich |  |
| [#1834](https://github.com/Marvisak/VIctory/pull/1834) | Shaders: read a VALU opcode's name without a heap vector | slatefield |  |
| [#1849](https://github.com/Marvisak/VIctory/pull/1849) | GPU: free memory is not the runtime's to watch (fixes a world-load deadlock under Wine) | crashbashash |  |
| [#1857](https://github.com/Marvisak/VIctory/pull/1857) | Shader tests: 64-bit image atomics skip devices without typed 64-bit heap atomics | Ingenioeren |  |
| [#1859](https://github.com/Marvisak/VIctory/pull/1859) | GPU: reject overflowing and non-buffer descriptor spans before shadow… | VlREX |  |
| [#1862](https://github.com/Marvisak/VIctory/pull/1862) | GPU: index bindless texture slots for targeted release and preserve u… | VlREX |  |
| [#1866](https://github.com/Marvisak/VIctory/pull/1866) | Game: preserve sample masks in prebuilt graphics pipelines | necrobytes |  |
| [#1879](https://github.com/Marvisak/VIctory/pull/1879) | Shader tests: keep dot4 test operands runtime for RDNA1 | n-romanovich |  |
| [#1880](https://github.com/Marvisak/VIctory/pull/1880) | Audio: refill XMA rings from a decoded reserve on the title's thread | beamdotdev |  |
| [#1884](https://github.com/Marvisak/VIctory/pull/1884) | Perf/memory guard batching | VlREX |  |
| [#1892](https://github.com/Marvisak/VIctory/pull/1892) | Tests: every GPU test module takes the shared lock, which diff_tests did not | fiestorra |  |
| [#1903](https://github.com/Marvisak/VIctory/pull/1903) | Shader: the ray test's triangle multiplies stay apart from their adds | kais7654 |  |
| [#1907](https://github.com/Marvisak/VIctory/pull/1907) | victory-shader: honor unwritten OSG1 channels and output modes in rectangle_gs | mgunes1311-lab |  |
| [#1922](https://github.com/Marvisak/VIctory/pull/1922) | GPU: refuse wave64 mesh and compute programs on hosts without 64-lane waves (rebase of #578) | slatefield |  |
| [#1933](https://github.com/Marvisak/VIctory/pull/1933) | victory-gpu: keep depth-twin UAVs in concrete UAV formats and support default views | mgunes1311-lab |  |
| [#1942](https://github.com/Marvisak/VIctory/pull/1942) | GameInput: answer IUnknown and own-IID queries on the COM objects (re-lands #1641) | Calvix2k |  |
| [#1944](https://github.com/Marvisak/VIctory/pull/1944) | reject a dxbc part inside the header or part table | imjustprism |  |
| [#1946](https://github.com/Marvisak/VIctory/pull/1946) | Descriptors: null UAV for packed 16-bit formats D3D12 refuses | Biewlhenrique |  |
| [#1947](https://github.com/Marvisak/VIctory/pull/1947) | HLE: a live range takes a guard page, and a mapped range is not a placeholder | fiestorra |  |
| [#1963](https://github.com/Marvisak/VIctory/pull/1963) | GPU: what shaders write beside a root UAV in its pages goes back to title memory | oVolkra |  |
| [#1966](https://github.com/Marvisak/VIctory/pull/1966) | keep crash reports when stderr is closed | imjustprism |  |
| [#1975](https://github.com/Marvisak/VIctory/pull/1975) | HLE: match rpcrt4 UuidFromString nil-UUID and canonical string rules | mgunes1311-lab |  |
| [#1978](https://github.com/Marvisak/VIctory/pull/1978) | GPU: no texture layouts or name copies per draw for unchanged answers | 0xkn0wh3r3 |  |
| [#1981](https://github.com/Marvisak/VIctory/pull/1981) | Preserve the last complete save when a newer version is missing a blob | WerG0D |  |
| [#1984](https://github.com/Marvisak/VIctory/pull/1984) | GPU: return NV12 and P010 luma and chroma copy footprints | yuniskh |  |
| [#1991](https://github.com/Marvisak/VIctory/pull/1991) | Shader tests: skip the GPU suites a device cannot run | Calvix2k |  |
| [#1992](https://github.com/Marvisak/VIctory/pull/1992) | docs: update architecture scheme | IWillFall1337 |  |
| [#1995](https://github.com/Marvisak/VIctory/pull/1995) | CLI: recommend a DXIL validator in translate --help | AlanQiang0418 |  |
| [#2001](https://github.com/Marvisak/VIctory/pull/2001) | HLE: resolve the local machine name to loopback | necrobytes |  |
| [#2005](https://github.com/Marvisak/VIctory/pull/2005) | GPU: log the missing D3D12 1.7 (no castable texture formats) | Calvix2k |  |
| [#2012](https://github.com/Marvisak/VIctory/pull/2012) | Shaders: decode finds instructions in a table by dword, not a tree | 0xkn0wh3r3 |  |
| [#2018](https://github.com/Marvisak/VIctory/pull/2018) | Docs: rustdoc builds the GPU crate again (shader_cache's private link) | Gruzzberry |  |
| [#2022](https://github.com/Marvisak/VIctory/pull/2022) | xmem: an aligned XMemAllocDefault block is padded once, not twice | 0xkn0wh3r3 |  |
| [#2026](https://github.com/Marvisak/VIctory/pull/2026) | Formats: bounds-check a detiled row once, not each run in it | 0xkn0wh3r3 |  |
| [#2039](https://github.com/Marvisak/VIctory/pull/2039) | CLI: resolve same-directory title DLL exports in census | fuzeofficlal |  |
| [#2041](https://github.com/Marvisak/VIctory/pull/2041) | Shaders: the fused multiply-add probe binds a sampler heap | 0xkn0wh3r3 |  |
| [#2053](https://github.com/Marvisak/VIctory/pull/2053) | GPU: log the host GPU, and warn when it is not the one to run on | rminzao |  |
| [#2057](https://github.com/Marvisak/VIctory/pull/2057) | Tests: a conformance title checks the runtime against the public platform documentation | 0xkn0wh3r3 |  |
| [#2066](https://github.com/Marvisak/VIctory/pull/2066) | Net: forward zero-address datagram disconnects | fuzeofficlal |  |
| [#2074](https://github.com/Marvisak/VIctory/pull/2074) | DirectStorage: a queue submits itself past half its capacity, not at half | 0xkn0wh3r3 |  |
| [#2075](https://github.com/Marvisak/VIctory/pull/2075) | HLE: with no process task queue, a call given no queue fails with E_NO_TASK_QUEUE | 0xkn0wh3r3 |  |
| [#2079](https://github.com/Marvisak/VIctory/pull/2079) | Shaders: a relative move's program is built at its full range only if no bound is proven | 0xkn0wh3r3 |  |
| [#2082](https://github.com/Marvisak/VIctory/pull/2082) | Docs: running under Wine/Proton on Linux (short notes) | desplmfao |  |
| [#2090](https://github.com/Marvisak/VIctory/pull/2090) | Add CPU-only execution-equivalence tests for Wave32 shader SSA and structured EXEC | chaseb64 |  |
| [#2101](https://github.com/Marvisak/VIctory/pull/2101) | GPU: castable formats the host has | Deilach |  |
| [#2111](https://github.com/Marvisak/VIctory/pull/2111) | GPU: the frame's wait for pipelines is one budget for all recording threads | r4tedx |  |
| [#2115](https://github.com/Marvisak/VIctory/pull/2115) | CLI: translate --count counts the instructions of the emitted shaders | r4tedx |  |
| [#2118](https://github.com/Marvisak/VIctory/pull/2118) | GPU: the BVH builder runs whole or not at all | 0xkn0wh3r3 |  |
| [#2139](https://github.com/Marvisak/VIctory/pull/2139) | HLE: implement synchronous XGameSave slots and unfiltered blob enumeration | fuzeofficlal |  |
| [#2141](https://github.com/Marvisak/VIctory/pull/2141) | HLE: registry lookups through kernelbase.dll reach the device-type overrides | BastienRodz |  |
| [#2150](https://github.com/Marvisak/VIctory/pull/2150) | Shaders: one instruction for one value (13.5 % fewer emitted instructions, no program lost) | r4tedx |  |
| [#2153](https://github.com/Marvisak/VIctory/pull/2153) | GPU: a snapshot that fails to allocate frees the idle pool and tries once more | desplmfao |  |
| [#2165](https://github.com/Marvisak/VIctory/pull/2165) | Loader: rebase of #1156 (continue past a title's int3 asserts) onto current main | Key-rs |  |
| [#2173](https://github.com/Marvisak/VIctory/pull/2173) | GPU: handle typed D16/D32 and multisample depth twins | fuzeofficlal |  |
| [#2184](https://github.com/Marvisak/VIctory/pull/2184) | xmem: 32-bit XMemAllocDefault blocks get the alignment they ask for | BastienRodz |  |
| [#2187](https://github.com/Marvisak/VIctory/pull/2187) | GPU: a readable texture does not share a host texture denied to shaders | fuzeofficlal |  |
| [#2195](https://github.com/Marvisak/VIctory/pull/2195) | GPU tests: the library test's shaders compile with Wine's compiler too | winne42 |  |
| [#2196](https://github.com/Marvisak/VIctory/pull/2196) | GPU tests: root signatures made from each shader's RS string | winne42 |  |
| [#2197](https://github.com/Marvisak/VIctory/pull/2197) | config: flag fidelityfx_dir in `victory config` policy check; fix example comment | romeawayfromhome-rgb |  |
| [#2199](https://github.com/Marvisak/VIctory/pull/2199) | XMem: preserve overlapping source pages during GPU mapping copies | Razdva122 |  |
| [#2205](https://github.com/Marvisak/VIctory/pull/2205) | Diagnostics: VICTORY_KEYS can hold a key longer than 0.2 s | fiestorra |  |
| [#2219](https://github.com/Marvisak/VIctory/pull/2219) | docs: mention VICTORY_CONFIG in README | romeawayfromhome-rgb |  |
| [#2223](https://github.com/Marvisak/VIctory/pull/2223) | GPU: account for pending pipelines before promotion | andrewpozdnakov7-jpg |  |
| [#2229](https://github.com/Marvisak/VIctory/pull/2229) | Shaders: v_pk_fmac_f16 with DPP reads src0 from the selected lane | BastienRodz |  |
| [#2235](https://github.com/Marvisak/VIctory/pull/2235) | GPU: a title memory copy left out of a page table is named when slots come back | denkencar-sketch |  |
| [#2238](https://github.com/Marvisak/VIctory/pull/2238) | Watch: dropping a tracker keeps a mapping guarded while a tracker holds its alias | denkencar-sketch |  |
| [#2246](https://github.com/Marvisak/VIctory/pull/2246) | xtask: reject decimal byte arrays in the asset policy | xiaotu030202 |  |
| [#2254](https://github.com/Marvisak/VIctory/pull/2254) | Shaders: v_mad_i64_i32 sign-extends a 32-bit literal addend | BastienRodz |  |
| [#2265](https://github.com/Marvisak/VIctory/pull/2265) | Tests: allow the frame clock to skip ticks after a late frame | andrewpozdnakov7-jpg |  |
| [#2269](https://github.com/Marvisak/VIctory/pull/2269) | GPU: marks in the last dword of the written-pages bitmap are not discarded | denkencar-sketch |  |
| [#2273](https://github.com/Marvisak/VIctory/pull/2273) | GPU diagnostics: VICTORY_SKIP_PIPELINES says what it took and when it skips | BaggyALPHA |  |
| [#2274](https://github.com/Marvisak/VIctory/pull/2274) | GPU: aliased textures copy only the subresources that have the same bytes per row | denkencar-sketch |  |
| [#2276](https://github.com/Marvisak/VIctory/pull/2276) | GPU: a depth texture used before it got a twin is copied to the twin in the list | denkencar-sketch |  |
| [#2278](https://github.com/Marvisak/VIctory/pull/2278) | GPU: a plain heap description is not read past its 16 bytes without checking they are mapped | denkencar-sketch |  |
| [#2282](https://github.com/Marvisak/VIctory/pull/2282) | Shaders: apply v_interp_p2_f16 modifiers in f32 before narrow16 | BlueCatsz |  |
| [#2284](https://github.com/Marvisak/VIctory/pull/2284) | Shader tests: cover the merged geometry user-data layout | Halfect |  |
| [#2288](https://github.com/Marvisak/VIctory/pull/2288) | docs: mention VICTORY_SKIP_CPU_CHECK in README | romeawayfromhome-rgb |  |
| [#2295](https://github.com/Marvisak/VIctory/pull/2295) | GPU: the fifth dword of a root constants parameter is read as a constant | denkencar-sketch |  |
| [#2298](https://github.com/Marvisak/VIctory/pull/2298) | GPU: aliasing and UAV barriers keep the host resources they name until the list is reset | denkencar-sketch |  |
| [#2303](https://github.com/Marvisak/VIctory/pull/2303) | GPU: page mapping copies wait for the submission that is running | denkencar-sketch |  |
| [#2320](https://github.com/Marvisak/VIctory/pull/2320) | Preserve signed R16 contrast in PNG captures | DoubleD17 |  |
| [#2323](https://github.com/Marvisak/VIctory/pull/2323) | Shader tests: the gather-at-a-level test reads its records through a raw view (false failure on NVIDIA) | Bullet18x |  |
| [#2332](https://github.com/Marvisak/VIctory/pull/2332) | GPU: the console's packed 4-bit colour target stands in as B5G5R5A1 | fiestorra |  |
| [#2339](https://github.com/Marvisak/VIctory/pull/2339) | docs: mention path override env vars in README | romeawayfromhome-rgb |  |
| [#2379](https://github.com/Marvisak/VIctory/pull/2379) | docs: document VICTORY_TRAP_LOG and VICTORY_AUDIO_CAPTURE_OF in the Debugging table | cloph-dsp |  |
| [#2392](https://github.com/Marvisak/VIctory/pull/2392) | HLE: a null or empty subkey opens the emulated OEM key itself (#765) | KainanP |  |
| [#2404](https://github.com/Marvisak/VIctory/pull/2404) | XG: preserve packed mip swizzle/positions and fix array subresource tiling (fixes #2400) | pushkarreddyy |  |
| [#2406](https://github.com/Marvisak/VIctory/pull/2406) | Shaders: s_cbranch_vccz/vccnz tests raw VCC, not VCC & EXEC | makmatvey |  |
| [#2418](https://github.com/Marvisak/VIctory/pull/2418) | Loader: guard dir64_relocations against BASERELOC size and page+offset overflow (fixes #2411) | pushkarreddyy |  |
| [#2420](https://github.com/Marvisak/VIctory/pull/2420) | PE: reject out-of-range export addresses in parse_exports (fixes #2412) | pushkarreddyy |  |
| [#2422](https://github.com/Marvisak/VIctory/pull/2422) | Shaders: visit resource::track blocks in reverse postorder | makmatvey |  |
| [#2426](https://github.com/Marvisak/VIctory/pull/2426) | Build: a ship profile with fat LTO and one codegen unit | Halfect |  |
| [#2430](https://github.com/Marvisak/VIctory/pull/2430) | GPU tests: a device removal fails the test that found it, later tests skip (#2317 item 1) | KainanP |  |
| [#2443](https://github.com/Marvisak/VIctory/pull/2443) | GPU: expose IDXGIObject on emulated DXGI interfaces | Damokles2 |  |
| [#2445](https://github.com/Marvisak/VIctory/pull/2445) | Loader: clamp VEH instruction reads to the faulting page in emulate_amd_only and sse4a | Texbirds |  |
| [#2447](https://github.com/Marvisak/VIctory/pull/2447) | GPU: probe 4 KiB OS pages in descriptor sync_heaps | Texbirds |  |
| [#2450](https://github.com/Marvisak/VIctory/pull/2450) | Shader: check device removal before FMad readback | Damokles2 |  |
| [#2452](https://github.com/Marvisak/VIctory/pull/2452) | HLE: DirectStorage open_file shares write/delete and keeps LastError | makmatvey |  |
| [#2466](https://github.com/Marvisak/VIctory/pull/2466) | docs: add contributor workflow | The-Star-World |  |
| [#2467](https://github.com/Marvisak/VIctory/pull/2467) | victory-shader: preserve high bits in root-derived BVH node addresses (#2368) | cloph-dsp |  |
| [#2478](https://github.com/Marvisak/VIctory/pull/2478) | GPU: an option to refresh a texture once every N frames | HoLa-Lee |  |
| [#2486](https://github.com/Marvisak/VIctory/pull/2486) | GPU: keep constant nonzero targets visible in captures | andrewpozdnakov7-jpg |  |
| [#2491](https://github.com/Marvisak/VIctory/pull/2491) | Shaders: intersect compare bounds with existing range bounds in Ranges::edge_hi | reeledMarek |  |
| [#2506](https://github.com/Marvisak/VIctory/pull/2506) | HLE: GetModuleHandleEx finds the title's modules, not the host's | cryst4lpepsi |  |
| [#2508](https://github.com/Marvisak/VIctory/pull/2508) | tools: add bounded Windows benchmark script | The-Star-World |  |
| [#2511](https://github.com/Marvisak/VIctory/pull/2511) | XGameSave: refuse an update when no version number is above the highest (#2497) | Creaa |  |
| [#2512](https://github.com/Marvisak/VIctory/pull/2512) | GameInput: look up only devices already seen by the process | andrewpozdnakov7-jpg |  |
| [#2520](https://github.com/Marvisak/VIctory/pull/2520) | Shaders: walk a predecessor's live-out registers once instead of searching it per register | liandraraiane |  |
| [#2524](https://github.com/Marvisak/VIctory/pull/2524) | HLE: bounds-check all four bytes of ACP notification writes in audio::submit | reeledMarek |  |
| [#2528](https://github.com/Marvisak/VIctory/pull/2528) | GPU diagnostics: count texture data without row padding | andrewpozdnakov7-jpg |  |
| [#2553](https://github.com/Marvisak/VIctory/pull/2553) | HLE: snapshot DirectStorage physical page lists with relaxed atomic loads | reeledMarek |  |
| [#2554](https://github.com/Marvisak/VIctory/pull/2554) | Loader: guard null C++ exception pointers in crash::thrown and Rsp overflow/alignment in unwind_into | reeledMarek |  |
| [#2557](https://github.com/Marvisak/VIctory/pull/2557) | GameInput: deliver registered reading callbacks | andrewpozdnakov7-jpg |  |
| [#2564](https://github.com/Marvisak/VIctory/pull/2564) | Shaders: hardware probes for the remaining s_cmp_* integer compares | LouisRiverstone |  |
| [#2565](https://github.com/Marvisak/VIctory/pull/2565) | Shaders: hardware probes for s_bitcmp0_b32 and s_bitcmp1_b32 | LouisRiverstone |  |
| [#2570](https://github.com/Marvisak/VIctory/pull/2570) | Shaders: hardware probes for the 64-bit scalar logic and shift ops | LouisRiverstone |  |
| [#2575](https://github.com/Marvisak/VIctory/pull/2575) | Game: skip redundant pipeline state enumeration and eliminate inner-loop blend Vec allocations | reeledMarek |  |
| [#2578](https://github.com/Marvisak/VIctory/pull/2578) | Core: ignore empty VICTORY_LOG and RUST_LOG values instead of overriding default log level | reeledMarek |  |
| [#2581](https://github.com/Marvisak/VIctory/pull/2581) | xtask: preserve filenames during asset-policy checks | XeNS1 |  |
| [#2585](https://github.com/Marvisak/VIctory/pull/2585) | GPU tests: each test's prepare hook runs on its own thread | fyernald |  |
| [#2587](https://github.com/Marvisak/VIctory/pull/2587) | Shaders: bind a zero dword for empty root-constant slices | fuzeofficlal |  |
| [#2588](https://github.com/Marvisak/VIctory/pull/2588) | Decode RGB9E5 in diagnostic PNG captures | DoubleD17 |  |
| [#2589](https://github.com/Marvisak/VIctory/pull/2589) | Diagnostics: preserve the world capture draw count | andrewpozdnakov7-jpg |  |
| [#2591](https://github.com/Marvisak/VIctory/pull/2591) | Formats: add a runnable BC5 record reconstruction shader example | Dathinel |  |
| [#2592](https://github.com/Marvisak/VIctory/pull/2592) | CLI: reject VS+GS graphics pipelines in prebuild | fuzeofficlal |  |
| [#2599](https://github.com/Marvisak/VIctory/pull/2599) | GPU: read UAV MipSlice from offset 8 in image_words | fuzeofficlal |  |
| [#2605](https://github.com/Marvisak/VIctory/pull/2605) | GPU: waits on memory that cannot be read are counted apart (#2604) | BastienRodz |  |
| [#2607](https://github.com/Marvisak/VIctory/pull/2607) | Diagnostics: decode signed 32-bit color captures | andrewpozdnakov7-jpg |  |
| [#2618](https://github.com/Marvisak/VIctory/pull/2618) | XAsync: a result size of 0 when there is no result to take | F1reworks10 |  |
| [#2622](https://github.com/Marvisak/VIctory/pull/2622) | Shaders: a constant branch through a folded block drops its untaken phi entry | BastienRodz |  |
| [#2625](https://github.com/Marvisak/VIctory/pull/2625) | HLE: encode async results without reading struct padding | XeNS1 |  |
| [#2629](https://github.com/Marvisak/VIctory/pull/2629) | GPU diagnostics: sample pages the watch calls unchanged against title memory | r4tedx |  |
| [#2630](https://github.com/Marvisak/VIctory/pull/2630) | refuse a tls directory that runs outside the image | imjustprism |  |
| [#2634](https://github.com/Marvisak/VIctory/pull/2634) | victory-gpu: say once, not per slot, that the title's heap outgrew the host's (first frame 21 s -> 33 ms) | pes7 |  |
| [#2635](https://github.com/Marvisak/VIctory/pull/2635) | docs: mention VICTORY_DIFF_ONLY in README | romeawayfromhome-rgb |  |
| [#2639](https://github.com/Marvisak/VIctory/pull/2639) | GPU: texture bytes off the runtime's memory are read at each refresh, as buffer copies' are (#2638) | BastienRodz |  |
| [#2641](https://github.com/Marvisak/VIctory/pull/2641) | Document how to run the pull request checks locally | maxence468 |  |
| [#2642](https://github.com/Marvisak/VIctory/pull/2642) | Check staged file type changes in the asset policy hook | maxence468 |  |
| [#2656](https://github.com/Marvisak/VIctory/pull/2656) | Shader tests: translate BCPack's signed nibble split and check every input | Dathinel |  |
| [#2658](https://github.com/Marvisak/VIctory/pull/2658) | Game tests: cover CityHash64 length and block boundaries | XeNS1 |  |
| [#2659](https://github.com/Marvisak/VIctory/pull/2659) | Loader (diagnostics): VICTORY_POKE writes through the page's protection | kotekompotek |  |
| [#2666](https://github.com/Marvisak/VIctory/pull/2666) | GPU diagnostics: end draw traces at every present | andrewpozdnakov7-jpg |  |
| [#2678](https://github.com/Marvisak/VIctory/pull/2678) | victory doctor: a run's failures, each linked to the issues that report it | shawshanker18 |  |
| [#2685](https://github.com/Marvisak/VIctory/pull/2685) | Shader tests: translate XMA integer log2 across both input words | Dathinel |  |
| [#2687](https://github.com/Marvisak/VIctory/pull/2687) | Shader tests: translate the BC6H index width lookup | Dathinel |  |
| [#2700](https://github.com/Marvisak/VIctory/pull/2700) | Shader tests: translate XMA float samples to signed PCM16 | Dathinel |  |
| [#2702](https://github.com/Marvisak/VIctory/pull/2702) | GPU: resolve multisampled color targets before diagnostic readback | andrewpozdnakov7-jpg |  |
| [#2706](https://github.com/Marvisak/VIctory/pull/2706) | victory-gpu: keep a pipeline library per translation, not one shared one (a translator edit destroyed a 926 MB / 7.5 min cache) | pes7 |  |
| [#2708](https://github.com/Marvisak/VIctory/pull/2708) | Find the first XMA frame when a buffer starts with continuation data | VlREX |  |
| [#2714](https://github.com/Marvisak/VIctory/pull/2714) | Keep XMA input valid when looping back to the start of a buffer | VlREX |  |
| [#2715](https://github.com/Marvisak/VIctory/pull/2715) | Clear stale button and key state in GameInput output buffers | VlREX |  |
| [#2720](https://github.com/Marvisak/VIctory/pull/2720) | Preserve ambiguous legacy XGameSave migrations (FIND-23) | leftmove |  |
| [#2727](https://github.com/Marvisak/VIctory/pull/2727) | GPU: reject overflowing rectangle vertex ranges | fuzeofficlal |  |
| [#2732](https://github.com/Marvisak/VIctory/pull/2732) | GPU: capture render and depth targets written by clears | andrewpozdnakov7-jpg |  |
| [#2738](https://github.com/Marvisak/VIctory/pull/2738) | Tests: wait for the late page list instead of sleeping | Therecalloftheonion |  |
| [#2739](https://github.com/Marvisak/VIctory/pull/2739) | Tests: bind a constant where a shader has no user data | Therecalloftheonion |  |
| [#2741](https://github.com/Marvisak/VIctory/pull/2741) | PE: reject null IAT RVAs in non-empty import descriptors | fuzeofficlal |  |
| [#2742](https://github.com/Marvisak/VIctory/pull/2742) | HLE: validate XMemMapPhysicalPages inputs before unmapping and roll back partial runs | fuzeofficlal |  |
| [#2745](https://github.com/Marvisak/VIctory/pull/2745) | HLE: succeed DisableThreadLibraryCalls for pseudo-module handles | fuzeofficlal |  |
| [#2749](https://github.com/Marvisak/VIctory/pull/2749) | XTaskQueue: every queue using a port hears of a task submitted to it | F1reworks10 |  |
| [#2761](https://github.com/Marvisak/VIctory/pull/2761) | Shaders: the operand of a GWS instruction is read from the address field | Moon0755 |  |
| [#2763](https://github.com/Marvisak/VIctory/pull/2763) | GPU: inherit typed formats in explicit RTV and DSV descriptions | andrewpozdnakov7-jpg |  |
| [#2765](https://github.com/Marvisak/VIctory/pull/2765) | Shaders: scratch with neither address names no register (GFX10.3 ST mode) | Moon0755 |  |
| [#2766](https://github.com/Marvisak/VIctory/pull/2766) | Shader tests: the descriptor-join tests build off Windows | lcg007xd-c |  |
| [#2769](https://github.com/Marvisak/VIctory/pull/2769) | GPU: keep PresentX statistics monotonic across concurrent reports | andrewpozdnakov7-jpg |  |
| [#2771](https://github.com/Marvisak/VIctory/pull/2771) | Shaders: a global or scratch load into LDS has no result register | Moon0755 |  |
| [#2784](https://github.com/Marvisak/VIctory/pull/2784) | Shaders: build Halves def/phi table lazily as a compact Vec<Def> in io::raise | RVZO6 |  |
| [#2793](https://github.com/Marvisak/VIctory/pull/2793) | Shaders: signature rows of one register follow their name offsets | Moon0755 |  |
| [#2794](https://github.com/Marvisak/VIctory/pull/2794) | Game: truncate oversized inflated stream to pack size in shaderpack::find | GuckstduWeitaaa |  |
| [#2795](https://github.com/Marvisak/VIctory/pull/2795) | Formats: speed up XMA2 inverse MDCT by 24-29% | brainbudt |  |
| [#2797](https://github.com/Marvisak/VIctory/pull/2797) | Loader: accept identical destination when concurrent publish rename fails | fuzeofficlal |  |
| [#2798](https://github.com/Marvisak/VIctory/pull/2798) | Shaders: a mesh program's PSV0 counts shared memory only when it has some | Moon0755 |  |
| [#2800](https://github.com/Marvisak/VIctory/pull/2800) | Shaders: SP3 text names a discard's address and position target four | Moon0755 |  |
| [#2804](https://github.com/Marvisak/VIctory/pull/2804) | GPU tests: what marking written title pages costs, per way of marking (benchmark for #2167, #2175, #2465, #2755) | 0xkn0wh3r3 |  |
| [#2805](https://github.com/Marvisak/VIctory/pull/2805) | GPU tests: assert a missed submission through readback | andrewpozdnakov7-jpg |  |
| [#2806](https://github.com/Marvisak/VIctory/pull/2806) | GPU tests: what translated 16-bit float math costs against the host's (34x on an RTX 5070 Ti; for #2384) | 0xkn0wh3r3 |  |
| [#2808](https://github.com/Marvisak/VIctory/pull/2808) | Shaders: speed up DXBC container MD5 hashing by 16-43% | brainbudt |  |
| [#2809](https://github.com/Marvisak/VIctory/pull/2809) | Run: the title's warm-up starts itself, at load | kais7654 |  |
| [#2812](https://github.com/Marvisak/VIctory/pull/2812) | shader: a comparison sampler replaces the reduction instead of OR-ing into it | spy0eye-beep |  |
| [#2814](https://github.com/Marvisak/VIctory/pull/2814) | docs: mention VICTORY_COPIES_IN_VIDEO_MEMORY in README Debugging table | romeawayfromhome-rgb |  |
| [#2816](https://github.com/Marvisak/VIctory/pull/2816) | Shaders: a wave64 mask restored from word-by-word scalar copies is the same mask | 0xkn0wh3r3 |  |
| [#2818](https://github.com/Marvisak/VIctory/pull/2818) | GPU: share readback chunks between a list's texture read backs | Therecalloftheonion |  |
| [#2820](https://github.com/Marvisak/VIctory/pull/2820) | GPU tests: a benchmark of what list calls cost on the title's threads | 0xkn0wh3r3 |  |
| [#2823](https://github.com/Marvisak/VIctory/pull/2823) | Shaders: the neg input modifier flips a NaN's sign too | xKineticK |  |
| [#2828](https://github.com/Marvisak/VIctory/pull/2828) | Pipeline cache: verify content when accepting a racing publication | andrewpozdnakov7-jpg |  |
| [#2838](https://github.com/Marvisak/VIctory/pull/2838) | CLI: reject conflicting shader-info output modes | 109User109 |  |
| [#2839](https://github.com/Marvisak/VIctory/pull/2839) | CLI: flag files configured as directories | 109User109 |  |
| [#2845](https://github.com/Marvisak/VIctory/pull/2845) | docs: list the variables the tests on outside files read | AurumCarlos |  |
| [#2850](https://github.com/Marvisak/VIctory/pull/2850) | GPU: refresh table CBVs on fresh_tables cache hits | fuzeofficlal |  |
| [#2855](https://github.com/Marvisak/VIctory/pull/2855) | xmem: a refused XMemVirtualAlloc leaves the host's reason in the last error | 0xkn0wh3r3 |  |
| [#2858](https://github.com/Marvisak/VIctory/pull/2858) | CLI: inspect names each section's flags | wilu222 |  |
| [#2859](https://github.com/Marvisak/VIctory/pull/2859) | Formats, GPU: a streamed texture's small mips are read before its large ones are there | 0xkn0wh3r3 |  |
| [#2869](https://github.com/Marvisak/VIctory/pull/2869) | Shaders: a buffer descriptor made raw from first-lane reads needs its waterfall (#2867) | BastienRodz |  |
| [#2873](https://github.com/Marvisak/VIctory/pull/2873) | GPU: a title buffer view takes a format the host takes, or stays null | 0xkn0wh3r3 |  |
| [#2878](https://github.com/Marvisak/VIctory/pull/2878) | Tests: the GPU tests load the D3D12 Agility SDK, as victory.exe does | lhnizdo |  |
| [#2882](https://github.com/Marvisak/VIctory/pull/2882) | GPU: heaps are bound again after a cut when ours stand in for both kinds (#2881) | BastienRodz |  |
| [#2886](https://github.com/Marvisak/VIctory/pull/2886) | Shaders: preserve round mode changes in whole-wave sections | yumaste |  |
| [#2887](https://github.com/Marvisak/VIctory/pull/2887) | HLE: a title's ExitProcess is logged as its exit is | 0xkn0wh3r3 |  |
| [#2889](https://github.com/Marvisak/VIctory/pull/2889) | GPU tests: read back cleared constant buffer descriptors | andrewpozdnakov7-jpg |  |
| [#2896](https://github.com/Marvisak/VIctory/pull/2896) | GPU: a list that binds no view heap gets ours before the root signature (#2894) | BastienRodz |  |
| [#2897](https://github.com/Marvisak/VIctory/pull/2897) | GPU: pipelines that write depth only go first among early starts | 0xkn0wh3r3 |  |
| [#2901](https://github.com/Marvisak/VIctory/pull/2901) | GPU: return S_FALSE when private data is already absent | andrewpozdnakov7-jpg |  |
| [#2902](https://github.com/Marvisak/VIctory/pull/2902) | HLE: a module name with a trailing dot gets no .dll appended | pawrenity |  |
| [#2904](https://github.com/Marvisak/VIctory/pull/2904) | DirectStorage: workers read a file through a handle each | 0xkn0wh3r3 |  |
| [#2906](https://github.com/Marvisak/VIctory/pull/2906) | HLE: oleaut32 is not in the host pass-through list, so the title's BSTR ordinals do not resolve | Jackster |  |
| [#2909](https://github.com/Marvisak/VIctory/pull/2909) | GPU: reject empty query heaps at creation | andrewpozdnakov7-jpg |  |
| [#2910](https://github.com/Marvisak/VIctory/pull/2910) | GPU: fit fallback host window to work area and honor VICTORY_WINDOW_MAX | alexandruiulian201-bot |  |
| [#2912](https://github.com/Marvisak/VIctory/pull/2912) | GPU: the host says whether its GPU shares memory with the CPU | 0xkn0wh3r3 |  |
| [#2917](https://github.com/Marvisak/VIctory/pull/2917) | Shaders: round half add and subtract toward zero once | andrewpozdnakov7-jpg |  |
| [#2919](https://github.com/Marvisak/VIctory/pull/2919) | GPU: the depth converter Wine's compiler builds too | arogan178 |  |
| [#2921](https://github.com/Marvisak/VIctory/pull/2921) | HLE, GPU: title memory held in place is let go before the title or the runtime changes it | 0xkn0wh3r3 |  |
| [#2922](https://github.com/Marvisak/VIctory/pull/2922) | Shaders: the fused multiply-add probe binds a sampler heap | 0xkn0wh3r3 |  |
| [#2923](https://github.com/Marvisak/VIctory/pull/2923) | Shaders: require EXEC coverage when tracing VALU address operands | fuzeofficlal |  |
| [#2931](https://github.com/Marvisak/VIctory/pull/2931) | GPU: match failed feature-level query results | andrewpozdnakov7-jpg |  |
| [#2935](https://github.com/Marvisak/VIctory/pull/2935) | GPU: count accepted presents while keeping title frames advancing | UwUCammie |  |
| [#2944](https://github.com/Marvisak/VIctory/pull/2944) | GPU: cap default pipeline worker count on <=24 GiB RAM hosts | alexandruiulian201-bot |  |
| [#2947](https://github.com/Marvisak/VIctory/pull/2947) | GPU: reject unknown shader model feature requests | andrewpozdnakov7-jpg |  |
| [#2950](https://github.com/Marvisak/VIctory/pull/2950) | Game: the shader pack in an archive inflates through zlib-rs | 0xkn0wh3r3 |  |
| [#2952](https://github.com/Marvisak/VIctory/pull/2952) | GPU: disable implicit stream depth test without a DSV format | fuzeofficlal |  |
| [#2955](https://github.com/Marvisak/VIctory/pull/2955) | GPU/Placement: defer free() reap, on-demand place() reap, O(1) heap metadata, and TLS fits->place alloc-info cache | RVZO6 |  |
| [#2961](https://github.com/Marvisak/VIctory/pull/2961) | GPU: reject shader-visible RTV and DSV heap creation | andrewpozdnakov7-jpg |  |
| [#2962](https://github.com/Marvisak/VIctory/pull/2962) | GPU: sample packed 10-bit frames for black-frame diagnostics | andrewpozdnakov7-jpg |  |
| [#2964](https://github.com/Marvisak/VIctory/pull/2964) | Shader tests: serialize remaining Host::new tests with ONE_AT_A_TIME (#1882) | Dukestar69 |  |
| [#2966](https://github.com/Marvisak/VIctory/pull/2966) | GPU watch: ignore zero-length writes and remaps on unaligned addresses (#2011) | Dukestar69 |  |
| [#2979](https://github.com/Marvisak/VIctory/pull/2979) | GPU: validate command list Close and Reset state | andrewpozdnakov7-jpg |  |
| [#2980](https://github.com/Marvisak/VIctory/pull/2980) | GPU: a panic while making a host pipeline refuses it instead of ending the worker | Ingenioeren |  |
| [#2981](https://github.com/Marvisak/VIctory/pull/2981) | HLE/DirectStorage: reuse per-worker DecompressorOxide and source/intermediate scratch buffers | RVZO6 |  |
| [#2989](https://github.com/Marvisak/VIctory/pull/2989) | Loader: verify OpenThread owner PID before reading thread stack | fuzeofficlal |  |
| [#2990](https://github.com/Marvisak/VIctory/pull/2990) | HLE: skip junctions in the persistent-storage quota count | Halfect |  |
| [#2991](https://github.com/Marvisak/VIctory/pull/2991) | Loader: clear XMM0 in ReturnZero thunk stubs for floating-point imports | fuzeofficlal |  |
| [#2998](https://github.com/Marvisak/VIctory/pull/2998) | HLE: deliver initial XNetworking registration callbacks and track unregister tokens | fuzeofficlal |  |
| [#3001](https://github.com/Marvisak/VIctory/pull/3001) | App: release LoaderLock on unwind via Drop guard | Dukestar69 |  |
| [#3002](https://github.com/Marvisak/VIctory/pull/3002) | GPU: an early list reset leaves a held host list it cannot replace | ZeOs360 |  |
| [#3006](https://github.com/Marvisak/VIctory/pull/3006) | GPU: read single-plane depth textures into guest buffers | andrewpozdnakov7-jpg |  |
| [#3014](https://github.com/Marvisak/VIctory/pull/3014) | CLI: deduplicate lib-exports entries per case-normalized DLL | fuzeofficlal |  |
| [#3015](https://github.com/Marvisak/VIctory/pull/3015) | App: check transitive static imports of mapped title DLLs for missing files | fuzeofficlal |  |
| [#3019](https://github.com/Marvisak/VIctory/pull/3019) | App: roll back re-entrant dependent DLLs on LateDlls attach failure | fuzeofficlal |  |
| [#3020](https://github.com/Marvisak/VIctory/pull/3020) | CLI: count all SGD5 hashes and stripped-bitcode XDAT/xbop markers in shader-info | fuzeofficlal |  |
| [#3024](https://github.com/Marvisak/VIctory/pull/3024) | PE: check SizeOfOptionalHeader and slice bounds in data_directory_offset | fuzeofficlal |  |
| [#3030](https://github.com/Marvisak/VIctory/pull/3030) | HLE/Media: translate \??\<drive>:\ NT object-manager paths through virtual drive mounts | RVZO6 |  |
| [#3034](https://github.com/Marvisak/VIctory/pull/3034) | GPU: require texture copy footprints to fit a complete row | andrewpozdnakov7-jpg |  |
| [#3038](https://github.com/Marvisak/VIctory/pull/3038) | Shaders: keep spilled compute root parameters from claiming s16+ system SGPRs | fuzeofficlal |  |
| [#3049](https://github.com/Marvisak/VIctory/pull/3049) | Game: recover SGD5 records from unparsed databases alongside intact ones | fuzeofficlal |  |
| [#3052](https://github.com/Marvisak/VIctory/pull/3052) | GPU: read-mark scans stop at the end of the view slots in use | 0xkn0wh3r3 |  |
| [#3054](https://github.com/Marvisak/VIctory/pull/3054) | Loader: unload already-mapped title DLLs when a dependency fails | Dukestar69 |  |

## conflicts with pull requests (457)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#159](https://github.com/Marvisak/VIctory/pull/159) | GPU: occlusion, statistics and timestamp queries run on the host | r4tedx | files: `crates/victory-gpu/src/list.rs`; with #24 |
| [#171](https://github.com/Marvisak/VIctory/pull/171) | Shaders: lower v_mad_u64_u32 and v_mad_i64_i32 | n-romanovich | files: `crates/victory-shader/src/emit/mod.rs`; with #166 |
| [#200](https://github.com/Marvisak/VIctory/pull/200) | Shaders: lower v_div_scale_f32, v_div_fmas_f32 and v_div_fixup_f32 | n-romanovich | files: `crates/victory-shader/src/emit/mod.rs`; with #166, #189 |
| [#223](https://github.com/Marvisak/VIctory/pull/223) | Shaders: translate for the host's wave sizes | r4tedx | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/crosslane_tests.rs`; with #166, #189 |
| [#233](https://github.com/Marvisak/VIctory/pull/233) | Shaders: wave64 compute on 32-lane hosts, in halves and in the console flow | r4tedx | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/crosslane_tests.rs`; with #166, #189 |
| [#286](https://github.com/Marvisak/VIctory/pull/286) | Shaders: accept known D3D_MIN_PRECISION signature elements | tarcisioads | files: `crates/victory-shader/src/emit/mod.rs`; with #166, #189 |
| [#320](https://github.com/Marvisak/VIctory/pull/320) | Shaders: lane reads and writes where lanes branch differently run in the console flow | r4tedx | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/crosslane_tests.rs`; with #166, #189 |
| [#385](https://github.com/Marvisak/VIctory/pull/385) | Shaders: track every incoming edge of a lane-mask phi | nathanbzrr | files: `crates/victory-shader/src/emit/lower.rs`; with #166, #189, #379 |
| [#387](https://github.com/Marvisak/VIctory/pull/387) | GPU: preserve execution ordering for buffer copies | aycow | files: `crates/victory-gpu/src/list.rs`; with #24 |
| [#439](https://github.com/Marvisak/VIctory/pull/439) | Shaders: one console wave sharing LDS runs in the console flow on 32-lane hosts | r4tedx | files: `apps/victory/src/main.rs`, `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #166, #189, #378, #379, #395 |
| [#465](https://github.com/Marvisak/VIctory/pull/465) | Shaders: lower v_dot2_f32_f16 and v_dot2c_f32_f16 | Baconzido | files: `crates/victory-shader/src/emit/lower.rs`; with #189 |
| [#551](https://github.com/Marvisak/VIctory/pull/551) | Shaders: lower compute thread-group info and s_get_waveid_in_workgroup | kilvynsilveira-tech | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #511 |
| [#559](https://github.com/Marvisak/VIctory/pull/559) | GPU: track mip states for 2D color targets | fuzeofficlal | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/list.rs`; with #24, #189, #450, #485 |
| [#594](https://github.com/Marvisak/VIctory/pull/594) | GPU: track texture subresource states | broccolize | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`; with #24, #189, #212, #450, #485, #583 |
| [#652](https://github.com/Marvisak/VIctory/pull/652) | GPU: use selected mip extents for MSAA resolves | fuzeofficlal | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #642 |
| [#662](https://github.com/Marvisak/VIctory/pull/662) | DSP: refuse XDspDisconnect with active streams; XDSP_E_NO_DEVICE_RESOURCES past the stream limit | coderanonymus | files: `crates/victory-hle/src/modules/dsp.rs`; with #240 |
| [#926](https://github.com/Marvisak/VIctory/pull/926) | Shaders: 16-bit compares read the low halves whatever op_sel says, as RDNA2 does | BastienRodz | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #606 |
| [#929](https://github.com/Marvisak/VIctory/pull/929) | Audio: a silent playback endpoint when the host has no render device | vladbondarenko97 | files: `crates/victory-hle/src/modules/audio.rs`; with #478 |
| [#1059](https://github.com/Marvisak/VIctory/pull/1059) | Loader: VICTORY_PATCH writes bytes into a loaded module after relocation | Halfect | files: `crates/victory-loader/src/lib.rs`; with #454 |
| [#1192](https://github.com/Marvisak/VIctory/pull/1192) | Loader: skip empty executable sections in tls::redirect and add tls.rs unit tests | geiyiliyabumo | files: `crates/victory-loader/src/tls.rs`; with #188 |
| [#1201](https://github.com/Marvisak/VIctory/pull/1201) | Loader: free mapped module on TLS redirect error and add windows.rs unit tests | geiyiliyabumo | files: `crates/victory-loader/src/windows.rs`; with #454, #1111 |
| [#1211](https://github.com/Marvisak/VIctory/pull/1211) | Shaders: lower v_mad_{u16,i16} and saturating clamp on 16-bit integer ops | ESAT586 | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142 |
| [#1213](https://github.com/Marvisak/VIctory/pull/1213) | HLE: reject null handle in WinHttpSetOption proxy path and expand net.rs tests (1 -> 17) | geiyiliyabumo | files: `crates/victory-hle/src/modules/net.rs`; with #997 |
| [#1217](https://github.com/Marvisak/VIctory/pull/1217) | GPU: the copies timing no longer counts the flush before a title copy twice | neonbyte1 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010 |
| [#1223](https://github.com/Marvisak/VIctory/pull/1223) | Shaders: lower v_ldexp_f16 (VOP2 0x3b and VOP3 0x13b) | ESAT586 | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142 |
| [#1224](https://github.com/Marvisak/VIctory/pull/1224) | fix(hle): coalesce split placeholders when mapping physical pages | matheusfrta | files: `crates/victory-hle/src/modules/xmem.rs`; with #76 |
| [#1244](https://github.com/Marvisak/VIctory/pull/1244) | Validate VICTORY_PAIRS before translating shaders | DoubleD17 | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673 |
| [#1256](https://github.com/Marvisak/VIctory/pull/1256) | Shaders: decode cube-array slice and face in image lowering | fuzeofficlal | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142 |
| [#1271](https://github.com/Marvisak/VIctory/pull/1271) | Shaders: propagate written heap UAVs and mark glc UAV handles globally coherent | fuzeofficlal | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142, #1262 |
| [#1281](https://github.com/Marvisak/VIctory/pull/1281) | GPU/Shader: declare wave64 wave size and strip unsupported video-texture flags | kss306 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1142, #1262 |
| [#1292](https://github.com/Marvisak/VIctory/pull/1292) | Shaders: lower v_dot2_{i32_i16,u32_u16}, v_dot4_u32_u8, v_dot8_u32_u4, and saturating dot4 clamp | ESAT586 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142, #1262 |
| [#1300](https://github.com/Marvisak/VIctory/pull/1300) | Shaders: lower v_{min3,max3,med3}_{i16,u16} and v_mad_{u32_u16,i32_i16} | ESAT586 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1142, #1262 |
| [#1312](https://github.com/Marvisak/VIctory/pull/1312) | Shaders: mask v_readlane/v_writelane lane index and bypass EXEC on writelane | ashrafsdrop | files: `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/emit/wave.rs`, `crates/victory-shader/src/resource.rs`, `crates/victory-shader/src/structure.rs`; with #189, #660, #1013, #1142, #1253, #1262 |
| [#1385](https://github.com/Marvisak/VIctory/pull/1385) | Shaders: narrow mesh output bounds from GS_ALLOC_REQ M0 analysis (#201) | Ctrl-Alt-Haze | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #1327 |
| [#1396](https://github.com/Marvisak/VIctory/pull/1396) | GPU: preserve sub-64 KiB alignments and check bounds in allocation_info | fuzeofficlal | files: `crates/victory-gpu/src/resource.rs`; with #450, #933 |
| [#1408](https://github.com/Marvisak/VIctory/pull/1408) | Shaders: lower float wave prefix sums via lane reads | fuzeofficlal | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1262, #1263, #1327, #1335, #1395 |
| [#1422](https://github.com/Marvisak/VIctory/pull/1422) | GPU: ignore clear values on non-target textures and avoid caching failed host textures in PLACED_TEXTURES | ESAT586 | files: `crates/victory-gpu/src/resource.rs`; with #450, #933 |
| [#1432](https://github.com/Marvisak/VIctory/pull/1432) | HLE: set ERROR_PROC_NOT_FOUND for missing pseudo-module exports | fuzeofficlal | files: `crates/victory-hle/src/modules/kernel.rs`; with #512 |
| [#1434](https://github.com/Marvisak/VIctory/pull/1434) | Loader: match title DLL filenames ignoring ASCII case | fuzeofficlal | files: `crates/victory-loader/src/windows.rs`; with #454, #1111, #1304 |
| [#1437](https://github.com/Marvisak/VIctory/pull/1437) | Shaders: preserve the unwritten high half of packed D16 image loads | EatCodeSleep2 | files: `crates/victory-shader/src/emit/waterfall_tests.rs`; with #189, #1253 |
| [#1449](https://github.com/Marvisak/VIctory/pull/1449) | GPU: report host resources held by descriptor heap slots in diagnostics | fuzeofficlal | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406 |
| [#1460](https://github.com/Marvisak/VIctory/pull/1460) | Shaders: collapse duplicate branch targets and dedup phi predecessors | piyonchu | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1327, #1362, #1395 |
| [#1462](https://github.com/Marvisak/VIctory/pull/1462) | CLI: report emitted shader wave sizes in translate | gurvancampion | files: `apps/victory/src/translate.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #378, #517, #660, #673, #1262, #1263, #1327 |
| [#1493](https://github.com/Marvisak/VIctory/pull/1493) | Shaders: declare SamplerComparisonState for immediate comparison samplers and add GPU test | piyonchu | files: `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1263, #1335, #1473 |
| [#1511](https://github.com/Marvisak/VIctory/pull/1511) | [BUNDLE] DXIL emission and container robustness: 3 PRs, #343 #1303 #477 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-shader/src/emit/validator.rs`; with #477 |
| [#1540](https://github.com/Marvisak/VIctory/pull/1540) | Shaders: guard both back edges when a conditional branch targets two … | Texbirds | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #1327, #1395, #1473 |
| [#1543](https://github.com/Marvisak/VIctory/pull/1543) | GPU: avoid shift and arithmetic overflow panics in subresource and copyable_footprints (victory-gpu) | Texbirds | files: `crates/victory-gpu/src/resource.rs`; with #450, #933 |
| [#1546](https://github.com/Marvisak/VIctory/pull/1546) | GPU: route indirect dispatch_mesh_x through State::execute_indirect | n-romanovich | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428 |
| [#1565](https://github.com/Marvisak/VIctory/pull/1565) | GPU: Evict succeeds, as the console's memory is never evicted | LouisRiverstone | files: `crates/victory-gpu/src/device.rs`; with #1564 |
| [#1566](https://github.com/Marvisak/VIctory/pull/1566) | GPU: SetStablePowerState is accepted and ignored | LouisRiverstone | files: `crates/victory-gpu/src/device.rs`; with #1564 |
| [#1569](https://github.com/Marvisak/VIctory/pull/1569) | Shaders: lower v_swaprel_b32 | piyonchu | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1327, #1362, #1395 |
| [#1630](https://github.com/Marvisak/VIctory/pull/1630) | GPU: adapter choice and logging, presenter backoff, a texture-description ladder, and a display-deferral test a headless session can pass | fiestorra | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547 |
| [#1631](https://github.com/Marvisak/VIctory/pull/1631) | Tests: allow prebuilt HLE probe DLL via VICTORY_HLE_PROBE_DLL | fuzeofficlal | files: `crates/victory-loader/tests/load_probe.rs`; with #1218 |
| [#1639](https://github.com/Marvisak/VIctory/pull/1639) | PE: map header RVAs and read TLS data from the headers | sandivd | files: `crates/victory-pe/src/image.rs`; with #324 |
| [#1693](https://github.com/Marvisak/VIctory/pull/1693) | victory-shader: lower TFE image loads/samples/gathers via CheckAccessFullyMapped | tjthebigbearcat-hub | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`; with #189, #1065, #1262, #1623 |
| [#1700](https://github.com/Marvisak/VIctory/pull/1700) | GPU: say when a draw's render target has no host copy or lost its permission | fiestorra | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583 |
| [#1717](https://github.com/Marvisak/VIctory/pull/1717) | HLE: the retail console ID has the documented dotted form | davutsimsekk | files: `crates/victory-hle/src/modules/xsystem.rs`; with #939 |
| [#1731](https://github.com/Marvisak/VIctory/pull/1731) | GPU: occlusion queries measure on the host instead of reporting every draw visible | fiestorra | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1704, #1715 |
| [#1732](https://github.com/Marvisak/VIctory/pull/1732) | GPU: f32_to_half keeps NaN and rounds normals to nearest even (#843) | moe-miau | files: `crates/victory-gpu/src/primitive.rs`; with #1418 |
| [#1738](https://github.com/Marvisak/VIctory/pull/1738) | Shaders: preserve live interpolation values (on #453) | jaschinski97-ops | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #1623, #1712 |
| [#1749](https://github.com/Marvisak/VIctory/pull/1749) | GPU: indirect mesh dispatches run as an indirect execution of one record | bemalinho | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #1704, #1715 |
| [#1751](https://github.com/Marvisak/VIctory/pull/1751) | GPU: capped view heaps keep the full dynamic range (NVIDIA) | JurajSimicevic | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548 |
| [#1759](https://github.com/Marvisak/VIctory/pull/1759) | Shaders: lower numerical Wave32 mesh masks at uniform entry | aycow | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1262, #1263, #1335, #1614, #1623, #1712 |
| [#1763](https://github.com/Marvisak/VIctory/pull/1763) | GPU: refuse typed UAVs in unsupported formats regardless of family or castability | n-romanovich | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548 |
| [#1767](https://github.com/Marvisak/VIctory/pull/1767) | translate: report the validator's own reason, not the line that hides it | fiestorra | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676 |
| [#1777](https://github.com/Marvisak/VIctory/pull/1777) | GPU: size the view heap clamp from what the host takes (NVIDIA 1,000,000 cap) | antoinerz1 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #212, #450, #583, #1010, #1263, #1283, #1406 |
| [#1793](https://github.com/Marvisak/VIctory/pull/1793) | FidelityFX: Series X switches to the host upscaler and its render scale (rework of #1284) | AwkGrep256 | files: `crates/victory-loader/src/lib.rs`; with #454 |
| [#1796](https://github.com/Marvisak/VIctory/pull/1796) | Core: report unreadable implicit configuration files | VlREX | files: `crates/victory-core/src/config.rs`; with #708 |
| [#1803](https://github.com/Marvisak/VIctory/pull/1803) | GPU: route UAV barriers on depth textures to their twin planes | mgunes1311-lab | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428 |
| [#1807](https://github.com/Marvisak/VIctory/pull/1807) | Refactor/iterative shader bdd | VlREX | files: `crates/victory-shader/src/structure.rs`; with #660, #1013, #1593 |
| [#1818](https://github.com/Marvisak/VIctory/pull/1818) | GPU: preserve disjoint shadow refresh ranges | aycow | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#1819](https://github.com/Marvisak/VIctory/pull/1819) | Shaders: translated loops are left after 2^14 iterations (was 2^20) | Exopus-0x65f7ad0 | files: `README.md`, `crates/victory-shader/src/emit/mod.rs`; with #189, #280, #491, #660, #686, #1218, #1263, #1335 |
| [#1821](https://github.com/Marvisak/VIctory/pull/1821) | CLI: add offline shader and GPU regression comparison report with syn… | VlREX | files: `crates/victory-gpu/src/copystat.rs`; with #602, #1264 |
| [#1832](https://github.com/Marvisak/VIctory/pull/1832) | GPU: drop the unordered-access permission a format cannot carry, before any call names it | fiestorra | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1817 |
| [#1840](https://github.com/Marvisak/VIctory/pull/1840) | Shaders: discover irreducible loops with iterative SCC decomposition | VlREX | files: `crates/victory-shader/src/ir.rs`; with #105, #369, #1593 |
| [#1846](https://github.com/Marvisak/VIctory/pull/1846) | Shaders: worklist register liveness with 96 independent synthetic CFG… | VlREX | files: `crates/victory-shader/src/ir.rs`; with #105, #369, #1593 |
| [#1856](https://github.com/Marvisak/VIctory/pull/1856) | Shaders: programs without FMad disable math refactoring | rminzao | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`; with #189, #1065, #1262, #1716, #1824 |
| [#1877](https://github.com/Marvisak/VIctory/pull/1877) | Shaders: hardware test for the 16-bit integer ops | LouisRiverstone | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857 |
| [#1888](https://github.com/Marvisak/VIctory/pull/1888) | GPU: cache alias-copy footprint plans and pool temporary copy buffers | nathanbzrr | files: `crates/victory-gpu/src/texture.rs`; with #601, #602, #1547 |
| [#1894](https://github.com/Marvisak/VIctory/pull/1894) | GPU: pool mapped upload buffers across command list resets | n-romanovich | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#1898](https://github.com/Marvisak/VIctory/pull/1898) | GPU: dependency-aware two-stage shader translation and pipeline scheduling (#1509) | nathanbzrr | files: `crates/victory-gpu/src/pipeline/make.rs`; with #1505, #1571 |
| [#1904](https://github.com/Marvisak/VIctory/pull/1904) | GPU: VICTORY_LIBRARY_TIMING measures the host FidelityFX upscaler's GPU and CPU cost | AwkGrep256 | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#1908](https://github.com/Marvisak/VIctory/pull/1908) | Keep the shader cache warm across emitter test edits | necrobytes | files: `crates/victory-shader/build.rs`; with #486 |
| [#1917](https://github.com/Marvisak/VIctory/pull/1917) | FidelityFX: add opt-in AMD frame generation to host upscaling | AwkGrep256 | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-hle/src/modules/fidelityfx.rs`; with #189, #212, #280, #450, #491, #583, #686, #1010 |
| [#1935](https://github.com/Marvisak/VIctory/pull/1935) | XMem: recycle freed physical page numbers on allocation | ashrafsdrop | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445 |
| [#1936](https://github.com/Marvisak/VIctory/pull/1936) | GPU: an opt-in gate refuses a translated shader the DXIL validator rejects | Luislariosss | files: `crates/victory-gpu/src/pipeline/library.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #1263, #1653, #1722 |
| [#1937](https://github.com/Marvisak/VIctory/pull/1937) | Codex/fix gpu castable test 2026 11 25 | lollo1977 | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1868 |
| [#1939](https://github.com/Marvisak/VIctory/pull/1939) | Shaders: truncate s_buffer_load terms to dword alignment independently | ashrafsdrop | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#1940](https://github.com/Marvisak/VIctory/pull/1940) | Shaders: d16 buffer format loads of UNORM / SNORM data round once to nearest | upipibi | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1871, #1879 |
| [#1943](https://github.com/Marvisak/VIctory/pull/1943) | Shaders: the null-buffer reads of the heap skip a host that caps its heaps | kais7654 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/memory.rs`; with #1406, #1548, #1770, #1859 |
| [#1958](https://github.com/Marvisak/VIctory/pull/1958) | Input: QueryInterface, a dispatcher, device methods, trigger rumble | RaghavVijayanand | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942 |
| [#1964](https://github.com/Marvisak/VIctory/pull/1964) | GPU: support 24-bit depth twins and per-plane active UAV tracking | nathanbzrr | files: `crates/victory-gpu/src/twin.rs`; with #1933 |
| [#1974](https://github.com/Marvisak/VIctory/pull/1974) | translate: say which validator engine produced the numbers, and warn before 1.8 | fiestorra | files: `crates/victory-shader/src/emit/validator.rs`; with #477 |
| [#1985](https://github.com/Marvisak/VIctory/pull/1985) | Shaders: compute exact dx.viewIdState and PSV0 input-output dependencies | nathanbzrr | files: `crates/victory-shader/src/emit/container.rs`, `crates/victory-shader/src/emit/shader.rs`; with #1065, #1262, #1716, #1824 |
| [#1986](https://github.com/Marvisak/VIctory/pull/1986) | GPU: a withheld range on a marked page does not hold back valid writes there | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#1993](https://github.com/Marvisak/VIctory/pull/1993) | GPU: hash DXIL shader slices zero-copy in HostPipeline::new | nathanbzrr | files: `crates/victory-gpu/src/pipeline/host.rs`; with #491, #1571, #1922 |
| [#1998](https://github.com/Marvisak/VIctory/pull/1998) | GPU: keep valid marked writes beside withheld ranges | Halfect | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816 |
| [#2002](https://github.com/Marvisak/VIctory/pull/2002) | translate: name VICTORY_DXIL in --validate's help, with why the version matters | fiestorra | files: `apps/victory/src/main.rs`; with #378, #1995 |
| [#2014](https://github.com/Marvisak/VIctory/pull/2014) | GPU: a mesh dispatch with an empty dimension runs nothing | artor410 | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428 |
| [#2034](https://github.com/Marvisak/VIctory/pull/2034) | Formats: BCPack block histories without per-call allocation or zeroing | StExpeditus | files: `crates/victory-formats/src/bcpack.rs`; with #703, #1557 |
| [#2051](https://github.com/Marvisak/VIctory/pull/2051) | GPU: a submission's refreshes copy on several threads | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2065](https://github.com/Marvisak/VIctory/pull/2065) | HLE: allow oleaut32.dll in default host policy | fuzeofficlal | files: `crates/victory-hle/src/host.rs`; with #1193 |
| [#2072](https://github.com/Marvisak/VIctory/pull/2072) | HLE: an unknown gamertag component is an invalid argument | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/xuser.rs`; with #398 |
| [#2076](https://github.com/Marvisak/VIctory/pull/2076) | HLE: implement remaining XAccessibility closed-caption, high-contrast, and speech-to-text slots | fuzeofficlal | files: `crates/victory-hle/src/modules/speech.rs`; with #1822 |
| [#2081](https://github.com/Marvisak/VIctory/pull/2081) | Shaders: cover v_cmp_class_f32 VOPC SGPR/literal, mask bits, and v_cmpx_class_* EXEC narrowing | fuzeofficlal | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2084](https://github.com/Marvisak/VIctory/pull/2084) | Shaders: buffer loads of a table in the program's code | rminzao | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2063, #2070, #2077, #2083 |
| [#2085](https://github.com/Marvisak/VIctory/pull/2085) | Shaders: pixel programs the console tests depth before keep early depth | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`; with #189, #1065, #1262, #1716, #1824, #2063, #2070, #2077 |
| [#2088](https://github.com/Marvisak/VIctory/pull/2088) | GPU: copy loose title memory in 256 KiB windows instead of 4 MiB (stacked on #402) | desplmfao | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816 |
| [#2089](https://github.com/Marvisak/VIctory/pull/2089) | hle: translate \??\ object-manager paths onto virtual drives | Pradhyumna51 | files: `crates/victory-hle/src/modules/files.rs`; with #1772 |
| [#2091](https://github.com/Marvisak/VIctory/pull/2091) | Shaders: lower Wave32 compute branches that reuse lane masks as scalar data | rezioliver-collab | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #1406, #1548, #1770, #1859, #1946, #2063 |
| [#2092](https://github.com/Marvisak/VIctory/pull/2092) | Shaders: lower v_dot4_u32_u8 and v_dot8_u32_u4 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2095](https://github.com/Marvisak/VIctory/pull/2095) | Input: trigger rumble through Windows.Gaming.Input | fylzzz | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942 |
| [#2096](https://github.com/Marvisak/VIctory/pull/2096) | GPU: bound shadow buffer lookup by maximum registered size instead of 64 entries | fuzeofficlal | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816 |
| [#2097](https://github.com/Marvisak/VIctory/pull/2097) | Shaders: lower v_qsad_pk_u16_u8, v_mqsad_pk_u16_u8, and v_mqsad_u32_u8 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2098](https://github.com/Marvisak/VIctory/pull/2098) | GPU: an acceleration structure's view address is its location | moe-miau | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946 |
| [#2099](https://github.com/Marvisak/VIctory/pull/2099) | GPU: stop the descriptor view table growing without bound | 0xkn0wh3r3 | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946 |
| [#2102](https://github.com/Marvisak/VIctory/pull/2102) | GPU: per-list and per-submission sets hash with FxHash, not SipHash | 0xkn0wh3r3 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #485, #583, #1010, #1283, #1414 |
| [#2104](https://github.com/Marvisak/VIctory/pull/2104) | Shaders: lower s_wqm_b32 and s_wqm_b64 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2106](https://github.com/Marvisak/VIctory/pull/2106) | GPU: reject non-power-of-two alignments in allocate_upload | fuzeofficlal | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428 |
| [#2117](https://github.com/Marvisak/VIctory/pull/2117) | Shaders: compute reading lanes only within aligned groups declares no wave size | rminzao | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #212, #450, #491, #583, #1010, #1262, #1283 |
| [#2121](https://github.com/Marvisak/VIctory/pull/2121) | GPU: page view heaps a host caps below the slots shaders index | 0xkn0wh3r3 | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2126](https://github.com/Marvisak/VIctory/pull/2126) | Shaders: compute threads that read other lanes keep unique ids in 2-D groups (NVIDIA) | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #1676, #1857, #1991, #2041, #2063, #2070 |
| [#2128](https://github.com/Marvisak/VIctory/pull/2128) | GPU: populate unbound table slots with typed null descriptors | fuzeofficlal | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #450, #485, #583, #660, #1262, #1263, #1335 |
| [#2129](https://github.com/Marvisak/VIctory/pull/2129) | GPU: map the pipeline library's file instead of reading it into memory | 0xkn0wh3r3 | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722 |
| [#2134](https://github.com/Marvisak/VIctory/pull/2134) | GPU tests: a world frame's preparing at the published volumes (benchmark) | r4tedx | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2142](https://github.com/Marvisak/VIctory/pull/2142) | GPU: read small buffer diagnostics via read_into instead of VirtualQuery | fuzeofficlal | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2146](https://github.com/Marvisak/VIctory/pull/2146) | GPU: add opt-in VICTORY_TEXTURE_MIP_DROP quality switch (fixes #737) | antikohza | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #24, #450, #601, #602, #933, #1406, #1428, #1547 |
| [#2148](https://github.com/Marvisak/VIctory/pull/2148) | Shaders: lower mul_hi without INT64 | scoresby13 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262 |
| [#2149](https://github.com/Marvisak/VIctory/pull/2149) | GPU: textures viewed only from a smaller level are uploaded from it on | 0xkn0wh3r3 | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2160](https://github.com/Marvisak/VIctory/pull/2160) | shader: improve v_log_f32 accuracy near unity (NEW-58) | TheGrayOrange | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2166](https://github.com/Marvisak/VIctory/pull/2166) | xtask: add CPU-only source verification report | yefan911 | files: `xtask/src/main.rs`; with #545, #1218 |
| [#2167](https://github.com/Marvisak/VIctory/pull/2167) | Shaders: guard memory_dirty atomics with test-before-or and coalesce page-table loads (FIND-12) | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2152 |
| [#2168](https://github.com/Marvisak/VIctory/pull/2168) | GPU: scope indirect clamp UAV barriers and skip zero-record clamps | RVZO6 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2176](https://github.com/Marvisak/VIctory/pull/2176) | GPU+shader: translate wave64 programs for 32-lane host waves when WaveLaneCountMax < 64 | n-romanovich | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/crosslane_tests.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2177](https://github.com/Marvisak/VIctory/pull/2177) | GPU+shader: clamp and place null buffer views within capped host descriptor heaps | n-romanovich | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2178](https://github.com/Marvisak/VIctory/pull/2178) | GPU+shader: back structured buffer views with raw descriptors for NVIDIA rawBufferLoad | n-romanovich | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1263, #1335, #1406, #1548, #1716, #1770 |
| [#2182](https://github.com/Marvisak/VIctory/pull/2182) | Input: opt-in mouse look on the stand-in pad's right stick | denkencar-sketch | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942 |
| [#2193](https://github.com/Marvisak/VIctory/pull/2193) | GPU: report allocated mip levels for auto-sized textures in GetDesc (fixes #773) | Xvania7 | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2198](https://github.com/Marvisak/VIctory/pull/2198) | docs: note translate --cache conflicts with --validate/--list | romeawayfromhome-rgb | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2201](https://github.com/Marvisak/VIctory/pull/2201) | gpu: compact non-empty indirect draw and dispatch arguments | UnkwnDev | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2207](https://github.com/Marvisak/VIctory/pull/2207) | Shaders: cache USER_DATA CBV rows and extracted dwords in Lower::user_at | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2152 |
| [#2208](https://github.com/Marvisak/VIctory/pull/2208) | Shaders: use atomicCompareExchange CAS loop for buffer_store_byte and buffer_store_short | RVZO6 | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #1065, #1262, #1716, #2115, #2150, #2152 |
| [#2210](https://github.com/Marvisak/VIctory/pull/2210) | Shaders: replace HashMap/linear scans in Lower with O(1) dense Vec tables | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2152 |
| [#2211](https://github.com/Marvisak/VIctory/pull/2211) | GPU: hash shaders once in pipeline::shader() and cache SFI0 atomics64 on Translated | RVZO6 | files: `crates/victory-gpu/src/pipeline.rs`; with #491, #1571, #1584, #1922, #2111, #2118 |
| [#2224](https://github.com/Marvisak/VIctory/pull/2224) | GPU: validate execute_indirect buffer offsets against buffer bounds and u64 overflow | Xvania7 | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428 |
| [#2225](https://github.com/Marvisak/VIctory/pull/2225) | Shaders: honor WARP-only mode in paired tests | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/semantics_tests.rs`; with #189, #1361, #1991 |
| [#2226](https://github.com/Marvisak/VIctory/pull/2226) | GPU: title textures the GPU writes share their heap's memory on the host | 0xkn0wh3r3 | files: `crates/victory-gpu/src/lib.rs`, `crates/victory-gpu/src/resource.rs`; with #212, #450, #933, #1010, #1264, #1547, #1681, #1776 |
| [#2227](https://github.com/Marvisak/VIctory/pull/2227) | core: add VICTORY_LOG_FILE and terminal-only stderr colour | Sidlik900 | files: `crates/victory-hle/src/modules/audio/capture.rs`; with #478 |
| [#2230](https://github.com/Marvisak/VIctory/pull/2230) | GameInput: a tap between two current-state reads is not lost (input at low frame rates) | desplmfao | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942, #2205 |
| [#2240](https://github.com/Marvisak/VIctory/pull/2240) | GPU: title memory copies are brought up to date again after a title write | denkencar-sketch | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2247](https://github.com/Marvisak/VIctory/pull/2247) | HLE files: wrap missing SetCurrentDirectoryW and Win32/UCRT path twins | Sidlik900 | files: `crates/victory-hle/src/modules/files.rs`; with #1772 |
| [#2249](https://github.com/Marvisak/VIctory/pull/2249) | HLE: WSAConnectByList and GetAddrInfoExA fail where the host lacks them, not abort (Wine) | desplmfao | files: `crates/victory-hle/src/modules/net.rs`; with #997, #2001, #2066 |
| [#2250](https://github.com/Marvisak/VIctory/pull/2250) | GPU: pipeline workers take their count from VICTORY_PIPELINE_THREADS | kotekompotek | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676, #1809, #2115 |
| [#2251](https://github.com/Marvisak/VIctory/pull/2251) | Tests: heap-capped and barrier-less hosts run the GPU tests | kotekompotek | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/memory.rs`; with #189, #450, #485, #583, #1406, #1548, #1765, #1770 |
| [#2272](https://github.com/Marvisak/VIctory/pull/2272) | GPU: a page a copy holds in part is taken after its marked copy-back | denkencar-sketch | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269 |
| [#2279](https://github.com/Marvisak/VIctory/pull/2279) | GPU: a render or depth view description with an unknown format names the resource's on a typeless host copy | denkencar-sketch | files: `crates/victory-gpu/src/descriptor.rs`; with #1406, #2278 |
| [#2292](https://github.com/Marvisak/VIctory/pull/2292) | GPU diagnostics: a pipeline whose creation faults is refused and the title goes on (opt-in, on #491) | desplmfao | files: `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/pipeline/make.rs`; with #491, #1505, #1571, #1922, #2111, #2118, #2223 |
| [#2293](https://github.com/Marvisak/VIctory/pull/2293) | GPU: a slot rewritten during a run keeps its view's copy of title memory until the run is over | denkencar-sketch | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946 |
| [#2294](https://github.com/Marvisak/VIctory/pull/2294) | GPU: a typed depth format in a shader resource view is made in the readable colour format | denkencar-sketch | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946 |
| [#2296](https://github.com/Marvisak/VIctory/pull/2296) | GPU: rectangle vertices are read from title memory through the kernel at submission | denkencar-sketch | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2297](https://github.com/Marvisak/VIctory/pull/2297) | GPU: a texture sampled before an in-list title memory copy is uploaded again after it | denkencar-sketch | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2299](https://github.com/Marvisak/VIctory/pull/2299) | GPU: harden CopyMemoryToMemoryX against unmapped or read-only pages | denkencar-sketch | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #2298 |
| [#2305](https://github.com/Marvisak/VIctory/pull/2305) | GPU: no render target view of a format the driver refuses while reporting support | fiestorra | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2309](https://github.com/Marvisak/VIctory/pull/2309) | Shaders: one back edge per block, so vkd3d-proton converts #439's loops (stacked on #439) | desplmfao | files: `apps/victory/src/main.rs`, `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2310](https://github.com/Marvisak/VIctory/pull/2310) | GPU diagnostics: breadcrumbs name the command a hung submission is stuck in (VICTORY_GPU_BREADCRUMBS) | desplmfao | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2319](https://github.com/Marvisak/VIctory/pull/2319) | GPU: create a texture without a host UAV format without the flag | Calvix2k | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2321](https://github.com/Marvisak/VIctory/pull/2321) | Report effect databases in shader-info effects mode | DoubleD17 | files: `apps/victory/src/shader.rs`; with #517 |
| [#2325](https://github.com/Marvisak/VIctory/pull/2325) | GPU: a resolve names the format of the host texture, not the console's id | denkencar-sketch | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #2298 |
| [#2327](https://github.com/Marvisak/VIctory/pull/2327) | GPU: a save that fails gives its changes back for the next one | denkencar-sketch | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195 |
| [#2328](https://github.com/Marvisak/VIctory/pull/2328) | GPU: pipeline library saves run one at a time | denkencar-sketch | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195 |
| [#2329](https://github.com/Marvisak/VIctory/pull/2329) | GPU: a list that binds a heap's view-address table keeps it until reset | denkencar-sketch | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2331](https://github.com/Marvisak/VIctory/pull/2331) | GPU: page-table writes go back beside those through views in one page | oVolkra | files: `crates/victory-gpu/src/memory.rs`, `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1770, #1816, #1963, #1978, #2153, #2235 |
| [#2334](https://github.com/Marvisak/VIctory/pull/2334) | Fix the Linux build and clippy gates (carries #1017) | ntgata1-dotcom | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-hle/src/modules/storage.rs`, `crates/victory-hle/src/runtime.rs`; with #189, #378, #450, #517, #673, #933, #1193, #1196 |
| [#2341](https://github.com/Marvisak/VIctory/pull/2341) | GPU: refresh a texture alias after its source is written again | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #450, #601, #602, #933, #1547, #1776, #1787, #1978 |
| [#2343](https://github.com/Marvisak/VIctory/pull/2343) | HLE: route kernelbase.dll registry exports through device_type | windfallscout | files: `crates/victory-hle/src/modules/xsystem.rs`; with #939, #2141 |
| [#2344](https://github.com/Marvisak/VIctory/pull/2344) | Shaders: name the operation kind a whole-wave section the simulation cannot follow | borosf | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/wave.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2350](https://github.com/Marvisak/VIctory/pull/2350) | Shaders: lower binary64 frexp exponent and significand | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2358](https://github.com/Marvisak/VIctory/pull/2358) | GPU: prepare and upload only dirty texture bands (opt-in) | nicolasveilleux | files: `crates/victory-formats/src/texture.rs`; with #1113, #1792, #2026 |
| [#2360](https://github.com/Marvisak/VIctory/pull/2360) | README: Windows 10 needs the D3D12 Agility SDK for shader model 6.6 | makmatvey | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2361](https://github.com/Marvisak/VIctory/pull/2361) | Shaders: lower SOP2 s_pack_{ll,lh,hh}_b32_b16 (#815) | fuzeofficlal | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2362](https://github.com/Marvisak/VIctory/pull/2362) | xtask: type-check the Windows target from any host | borosf | files: `xtask/src/main.rs`; with #545, #1218 |
| [#2371](https://github.com/Marvisak/VIctory/pull/2371) | GPU: prefer high-performance DXGI adapter supporting FL 12.0 (fixes #1226) | antikohza | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2372](https://github.com/Marvisak/VIctory/pull/2372) | Shaders: 16-bit gradient samples (_g16) and a16 independently, in decoding and lowering (#1116) | KainanP | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2385](https://github.com/Marvisak/VIctory/pull/2385) | Shaders: track s_add_u32 with src_scc in address high halves (#815) | fuzeofficlal | files: `crates/victory-shader/src/resource.rs`; with #189, #1253, #1794, #2284 |
| [#2386](https://github.com/Marvisak/VIctory/pull/2386) | Shaders: a DPP step over a lane set the section names stays followed | borosf | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/wave.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2389](https://github.com/Marvisak/VIctory/pull/2389) | GPU: streamed textures take video memory only for the levels the title holds (opt-in, ~5 GB less) | desplmfao | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #189, #212, #450, #583, #601, #602, #933, #1010 |
| [#2397](https://github.com/Marvisak/VIctory/pull/2397) | GPU: copystat counts its counters at compile time; range and drain tests (revives #1188) | KainanP | files: `crates/victory-gpu/src/copystat.rs`; with #602, #1264 |
| [#2398](https://github.com/Marvisak/VIctory/pull/2398) | Shaders, GPU: link over-budget mesh and pixel shaders under D3D12's 32 KiB output limit | Texbirds | files: `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`; with #189, #491, #660, #1262, #1263, #1335, #1571, #1716 |
| [#2405](https://github.com/Marvisak/VIctory/pull/2405) | Shaders: test raw VCC on s_cbranch_vccz and s_cbranch_vccnz without EXEC masking | ashrafsdrop | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/range.rs`; with #189, #1262, #1362, #1784, #1802, #1811, #1857, #1879 |
| [#2408](https://github.com/Marvisak/VIctory/pull/2408) | Shader: a dot product over a constant multiplicand is taken by hand | KainanP | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2415](https://github.com/Marvisak/VIctory/pull/2415) | GPU: remapping one mapping of aliased pages leaves the others guarded | BastienRodz | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269 |
| [#2421](https://github.com/Marvisak/VIctory/pull/2421) | xmem: use saturating_add for view end bounds in aliases (fixes #2413) | pushkarreddyy | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199 |
| [#2423](https://github.com/Marvisak/VIctory/pull/2423) | `victory-hle(apu)`: reuse Opus decode scratch buffer and pre-reserve result queue | faycalbaklouti | files: `crates/victory-hle/src/modules/apu.rs`; with #1212 |
| [#2425](https://github.com/Marvisak/VIctory/pull/2425) | `victory-hle(xmem)`: coalesce contiguous 64 KiB `MapViewOfFile3` runs and add lock-free VEH retry around split-and-remap | faycalbaklouti | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199 |
| [#2427](https://github.com/Marvisak/VIctory/pull/2427) | cut cold launch to the first screen from 49 s to 21 s | imjustprism | files: `crates/victory-gpu/src/host.rs`, `crates/victory-hle/Cargo.toml`, `crates/victory-hle/src/modules/dstorage.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1457 |
| [#2428](https://github.com/Marvisak/VIctory/pull/2428) | GPU: a submission refreshes a copy's ranges disjoint, not their span | borosf | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2429](https://github.com/Marvisak/VIctory/pull/2429) | GPU: use the DirectX Agility SDK when the system D3D12 runtime refuses the shaders' root signatures | wkdwilliams | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/lib.rs`; with #189, #212, #280, #450, #486, #491, #583, #686 |
| [#2437](https://github.com/Marvisak/VIctory/pull/2437) | GPU: a marked copy-back advances the snapshot of declared ranges over its page | BastienRodz | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269 |
| [#2442](https://github.com/Marvisak/VIctory/pull/2442) | GPU: a texture flags unordered access only where a view can take it | kotekompotek | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2444](https://github.com/Marvisak/VIctory/pull/2444) | HLE: keep refilling XMA PCM buffer across zero-sample decode steps | Texbirds | files: `crates/victory-hle/src/modules/audio.rs`; with #478, #1880 |
| [#2457](https://github.com/Marvisak/VIctory/pull/2457) | Shaders: return zero for unused image_get_resinfo extents | makmatvey | files: `crates/victory-shader/src/emit/waterfall_tests.rs`; with #189, #1253, #1991 |
| [#2459](https://github.com/Marvisak/VIctory/pull/2459) | GPU: drop ALLOW_UNORDERED_ACCESS when the format cannot be a UAV | roon9e | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2460](https://github.com/Marvisak/VIctory/pull/2460) | victory.exe: load the D3D12 Agility SDK from .\D3D12\ | lhnizdo | files: `README.md`, `apps/victory/build.rs`; with #151, #280, #491, #686, #1218, #1263, #1584, #1701 |
| [#2461](https://github.com/Marvisak/VIctory/pull/2461) | GPU and shaders: a host that caps its view heaps gets heaps at its ca… | lhnizdo | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #1263, #1406, #1548, #1770, #1859, #1946, #2018 |
| [#2464](https://github.com/Marvisak/VIctory/pull/2464) | GPU: on NVIDIA, structured buffer views are made raw | lhnizdo | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2472](https://github.com/Marvisak/VIctory/pull/2472) | GPU: hoist and batch indirect argument clamps into the list prelude | ESAT586 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2474](https://github.com/Marvisak/VIctory/pull/2474) | GPU: refreshes of two parts of one page do not make it current whole | BastienRodz | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2476](https://github.com/Marvisak/VIctory/pull/2476) | Discover shaders and pipeline packs through file symlinks | DoubleD17 | files: `apps/victory/src/shader.rs`, `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676, #1809, #2115 |
| [#2480](https://github.com/Marvisak/VIctory/pull/2480) | Shaders: BDD meet rejects a node held both ways and takes one condition as met | liandraraiane | files: `crates/victory-shader/src/structure.rs`; with #660, #1013, #1593, #2406 |
| [#2483](https://github.com/Marvisak/VIctory/pull/2483) | DSP: the reverb convolver passes the host checks (rebased #240) | kais7654 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/memory.rs`, `crates/victory-hle/src/modules/dsp.rs`, `crates/victory-hle/src/modules/dsp_convolve.rs`; with #240, #1406, #1548, #1770, #1859, #1946, #1963, #1978 |
| [#2492](https://github.com/Marvisak/VIctory/pull/2492) | Shaders: reject VALU float/clamp modifiers in I/O and resource analyses | reeledMarek | files: `crates/victory-shader/src/resource.rs`; with #189, #1253, #1794, #2284, #2422 |
| [#2501](https://github.com/Marvisak/VIctory/pull/2501) | Shaders: a BVH node offset from a root descriptor is computed in 64 bits | Calvix2k | files: `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/lower/bvh.rs`; with #189, #1794, #1903, #1991, #2467 |
| [#2504](https://github.com/Marvisak/VIctory/pull/2504) | HLE: physical-page writes open the title's views before they write | BastienRodz | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199 |
| [#2510](https://github.com/Marvisak/VIctory/pull/2510) | GPU: sweep cut pipeline-cache staging files | Ingenioeren | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195 |
| [#2516](https://github.com/Marvisak/VIctory/pull/2516) | GPU capture: decode XR-biased RGB before image scaling | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486 |
| [#2518](https://github.com/Marvisak/VIctory/pull/2518) | Preserve signed R8 contrast in PNG captures | DoubleD17 | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486 |
| [#2519](https://github.com/Marvisak/VIctory/pull/2519) | HLE: optionally back physical page pools with temporary sparse files | yyc160 | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199 |
| [#2527](https://github.com/Marvisak/VIctory/pull/2527) | GPU capture: decode R32G32_UINT targets | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486 |
| [#2529](https://github.com/Marvisak/VIctory/pull/2529) | Xmem: honour 32-bit allocation alignment | XratePirate | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199 |
| [#2532](https://github.com/Marvisak/VIctory/pull/2532) | PE: reject out-of-image TLS callback VAs in va_to_rva | reeledMarek | files: `crates/victory-pe/src/image.rs`; with #324, #2420 |
| [#2533](https://github.com/Marvisak/VIctory/pull/2533) | Game: guarantee 8-byte alignment for pipeline stream subobjects and input elements | reeledMarek | files: `crates/victory-game/src/pipelines.rs`; with #1866 |
| [#2540](https://github.com/Marvisak/VIctory/pull/2540) | GPU: a page a refresh took in part is not current | Calvix2k | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2548](https://github.com/Marvisak/VIctory/pull/2548) | Shaders: lower v_mov_b32 abs/neg modifiers bitwise | fuzeofficlal | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2559](https://github.com/Marvisak/VIctory/pull/2559) | GPU: a removal report without DRED names the switch, not "unsupported" | Ingenioeren | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2562](https://github.com/Marvisak/VIctory/pull/2562) | translate --pipelines: driver reasons for refusals, and --only <stages> (#2537) | oni-swr | files: `README.md`, `apps/victory/src/main.rs`, `apps/victory/src/translate.rs`, `crates/victory-shader/src/emit/host.rs`; with #189, #280, #378, #491, #517, #673, #686, #1218 |
| [#2567](https://github.com/Marvisak/VIctory/pull/2567) | Diagnostics: capture RGBA32 unsigned targets | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486 |
| [#2569](https://github.com/Marvisak/VIctory/pull/2569) | HLE: opt out of Windows 11 Efficiency Mode throttling in use_console_timers | Bebrik229 | files: `crates/victory-hle/src/runtime.rs`; with #1196 |
| [#2572](https://github.com/Marvisak/VIctory/pull/2572) | docs: mention shader-test DXC variables in README | romeawayfromhome-rgb | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2573](https://github.com/Marvisak/VIctory/pull/2573) | GPU: copy shader-written water/ocean textures back into title memory (VICTORY_TEXTURE_BACK) | Bebrik229 | files: `crates/victory-gpu/src/lib.rs`; with #212, #1010, #1264, #1681, #2053, #2196 |
| [#2576](https://github.com/Marvisak/VIctory/pull/2576) | GPU: read marks of slots forgotten before a submission are cleared before it runs | BastienRodz | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2579](https://github.com/Marvisak/VIctory/pull/2579) | Core: ignore empty LOCALAPPDATA, XDG_CACHE_HOME, and HOME in default directory resolution | reeledMarek | files: `crates/victory-core/src/config.rs`; with #708 |
| [#2594](https://github.com/Marvisak/VIctory/pull/2594) | Shader: lower f32 fused multiply-adds through f64 | JAEdotUK | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/host.rs`; with #189, #378, #517, #660, #673, #1065, #1253, #1262 |
| [#2595](https://github.com/Marvisak/VIctory/pull/2595) | pe: reject entry points outside the mapped image | XeNS1 | files: `crates/victory-pe/src/image.rs`; with #324, #2420 |
| [#2596](https://github.com/Marvisak/VIctory/pull/2596) | Shader tests: an empty root-constant list is set as the one constant it declares (#2571) | Creaa | files: `crates/victory-shader/src/emit/host.rs`; with #189, #1676, #1857, #1991, #2041, #2450, #2587 |
| [#2598](https://github.com/Marvisak/VIctory/pull/2598) | GPU: giving up a texture leaves the dynamic slots of recorded lists alone | BastienRodz | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585 |
| [#2600](https://github.com/Marvisak/VIctory/pull/2600) | Shaders: lower binary64 truncation | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2601](https://github.com/Marvisak/VIctory/pull/2601) | GPU: pin textures with pending host_writes against eviction | fuzeofficlal | files: `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #450, #601, #602, #933, #1547, #1776, #1787, #1978 |
| [#2603](https://github.com/Marvisak/VIctory/pull/2603) | Shaders: avoid f32 precision loss in thin rectangle right-angle check | fuzeofficlal | files: `crates/victory-shader/src/emit/rect.rs`; with #1907 |
| [#2606](https://github.com/Marvisak/VIctory/pull/2606) | HLE: decode numeric character references in manifests | XeNS1 | files: `crates/victory-hle/src/runtime.rs`; with #1196 |
| [#2608](https://github.com/Marvisak/VIctory/pull/2608) | GPU: split and flush command list segments after texture read-backs | fuzeofficlal | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #2298 |
| [#2610](https://github.com/Marvisak/VIctory/pull/2610) | Shaders: derive TYPED_UAV_LOADS and ROVs flags from surviving calls | fuzeofficlal | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/shader.rs`; with #1065, #1262, #1716, #1824, #2115, #2150 |
| [#2612](https://github.com/Marvisak/VIctory/pull/2612) | GPU: skip pending copy-backs and clear saved snapshots on remapped pages | ashrafsdrop | files: `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/watch.rs`, `crates/victory-hle/src/modules/xmem.rs`; with #76, #583, #602, #1264, #1445, #1816, #1849, #1884 |
| [#2614](https://github.com/Marvisak/VIctory/pull/2614) | GPU: cache parsed shader resource metadata across runs (shader-meta.bin) | Bebrik229 | files: `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/library.rs`; with #491, #1571, #1584, #1653, #1722, #1922, #2111, #2118 |
| [#2615](https://github.com/Marvisak/VIctory/pull/2615) | HLE: relaunch arguments split by the C runtime's rules | c4k3ss | files: `crates/victory-hle/src/modules/xgame.rs`; with #1174 |
| [#2617](https://github.com/Marvisak/VIctory/pull/2617) | HLE: hold DirectStorage reads behind held status entries and preserve sequence order | fuzeofficlal | files: `crates/victory-hle/src/modules/dstorage.rs`; with #1457, #1719, #2074, #2452, #2553 |
| [#2619](https://github.com/Marvisak/VIctory/pull/2619) | GPU: an opt-in constant stands in for one view a named program writes (VICTORY_AMBIENT) | r4tedx | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/lib.rs`; with #189, #212, #450, #485, #583, #1010, #1264, #1681 |
| [#2620](https://github.com/Marvisak/VIctory/pull/2620) | GPU: an opt-in constant takes the place of a named program that does not run (VICTORY_STAND_IN) | r4tedx | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/lib.rs`; with #189, #212, #450, #485, #583, #1010, #1264, #1681 |
| [#2626](https://github.com/Marvisak/VIctory/pull/2626) | GPU: packed 16-bit colour targets the host cannot write are RGBA8 there | moe-miau | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/resource.rs`; with #450, #933, #1406, #1547, #1776, #1787, #1978, #1984 |
| [#2627](https://github.com/Marvisak/VIctory/pull/2627) | Shaders: exclude masks widened past block reachability from Structured::active | VastyViz | files: `crates/victory-shader/src/emit/synthetic_tests.rs`, `crates/victory-shader/src/structure.rs`; with #189, #660, #1013, #1593, #1991, #2323, #2406, #2587 |
| [#2628](https://github.com/Marvisak/VIctory/pull/2628) | GPU, Shaders: a capped view heap clamps shader heap indices from the first shader | moe-miau | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/memory.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2631](https://github.com/Marvisak/VIctory/pull/2631) | Shaders: s_cbranch_vccz/vccnz tests raw VCC, not VCC & EXEC | dutch2005 | files: `crates/victory-shader/src/structure.rs`; with #660, #1013, #1593, #2406 |
| [#2632](https://github.com/Marvisak/VIctory/pull/2632) | GPU: port DirectStorage staging and indirect draw improvements | Lkxex | files: `apps/victory/src/translate.rs`, `crates/victory-formats/src/texture.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-hle/src/modules/dstorage.rs`; with #189, #378, #517, #583, #673, #1113, #1457, #1676 |
| [#2633](https://github.com/Marvisak/VIctory/pull/2633) | Shaders: wave64 compute programs run in 32-lane halves on hosts of 32-lane waves | chippy01 | files: `README.md`, `apps/victory/src/main.rs`, `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #280, #378, #450, #485, #491, #517, #583 |
| [#2636](https://github.com/Marvisak/VIctory/pull/2636) | GPU: decode packed 16-bit UNORM diagnostic targets | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486, #2588, #2589, #2607 |
| [#2644](https://github.com/Marvisak/VIctory/pull/2644) | Loader (diagnostics): VICTORY_STEP_OVER steps over listed title breakpoints (#698) | Pierrot1398 | files: `README.md`, `crates/victory-loader/src/crash.rs`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2646](https://github.com/Marvisak/VIctory/pull/2646) | GPU: a WARP host keeps its pipeline library in a file of its own (#2637) | Creaa | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195 |
| [#2647](https://github.com/Marvisak/VIctory/pull/2647) | Shaders: lower nearest-even binary64 rounding | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2648](https://github.com/Marvisak/VIctory/pull/2648) | BCPack: stop completed lanes from taking another lane’s bytes | chaseb64 | files: `crates/victory-formats/src/bcpack.rs`; with #703, #1557 |
| [#2649](https://github.com/Marvisak/VIctory/pull/2649) | BCPack: retain a partial rANS refill at a fragment boundary | chaseb64 | files: `crates/victory-formats/src/bcpack.rs`; with #703, #1557 |
| [#2655](https://github.com/Marvisak/VIctory/pull/2655) | GPU: preserve wide float contrast in diagnostic captures | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486, #2588, #2589, #2607 |
| [#2657](https://github.com/Marvisak/VIctory/pull/2657) | Shaders: scope DXIL bitcode liveness to reachable blocks and live phi edges | Moon0755 | files: `crates/victory-shader/src/emit/bitcode.rs`; with #1065, #1262, #1716, #2115, #2150, #2622 |
| [#2662](https://github.com/Marvisak/VIctory/pull/2662) | Shaders: O(\|known\|) BDD forced() sweep, read-only implies(), per-block reuse in finish(), and FxHash in meet_in() | RVZO6 | files: `crates/victory-shader/src/structure.rs`; with #660, #1013, #1593, #2406 |
| [#2663](https://github.com/Marvisak/VIctory/pull/2663) | Formats/XMA: add 10-bit VLC lookup table, u64 bit-peek, and quant-factor LUT | RVZO6 | files: `crates/victory-formats/src/xma.rs`; with #364, #1797 |
| [#2664](https://github.com/Marvisak/VIctory/pull/2664) | Shaders/IR: eliminate per-instruction/CFG Vec allocations and O(1) effects dedup | RVZO6 | files: `crates/victory-shader/src/gfx10/fields.rs`, `crates/victory-shader/src/ir.rs`; with #105, #369, #1593, #1834, #2079, #2520 |
| [#2665](https://github.com/Marvisak/VIctory/pull/2665) | Shaders/Bitcode: cache Shader::op declarations, primitive types, scalar constants, and zero-copy bitcode Writer | RVZO6 | files: `crates/victory-shader/src/emit/shader.rs`; with #1065, #1262, #1716, #1824, #2150 |
| [#2667](https://github.com/Marvisak/VIctory/pull/2667) | GPU/HLE: pipelined startup reads and pooled small buffers, rebased onto main | kais7654 | files: `crates/victory-gpu/src/host.rs`, `crates/victory-hle/Cargo.toml`, `crates/victory-hle/src/modules/dstorage.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1457 |
| [#2668](https://github.com/Marvisak/VIctory/pull/2668) | Shaders: guard heap-direct texture read marks with EXEC | fuzeofficlal | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/memory_tests.rs`; with #189, #1262, #1991, #2229, #2254, #2282 |
| [#2672](https://github.com/Marvisak/VIctory/pull/2672) | loader: keep mapped DLLs inside the title directory | Rickeal-Boss | files: `crates/victory-loader/src/windows.rs`; with #454, #1111, #1304 |
| [#2673](https://github.com/Marvisak/VIctory/pull/2673) | GPU: report the first differing captured render target | necrobytes | files: `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #601, #1418, #1765, #1825 |
| [#2675](https://github.com/Marvisak/VIctory/pull/2675) | HLE: retain unreadable legacy save display metadata (on #2525) | jaschinski97-ops | files: `crates/victory-hle/src/modules/xgamesave.rs`; with #228, #590, #1110, #1123, #1981, #2139, #2511 |
| [#2676](https://github.com/Marvisak/VIctory/pull/2676) | Shader tests: translate the signed BCPack index residual sum | Dathinel | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2679](https://github.com/Marvisak/VIctory/pull/2679) | GPU: make shared sRGB textures typeless for unordered access | fuzeofficlal | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2680](https://github.com/Marvisak/VIctory/pull/2680) | GPU: keep edge samples in odd-sized diagnostic PNGs | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486, #2588, #2589, #2607 |
| [#2681](https://github.com/Marvisak/VIctory/pull/2681) | Shader tests: translate BCPack pixel-pair residual lookup | Dathinel | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2683](https://github.com/Marvisak/VIctory/pull/2683) | victory-shader: clamp heap indices to the largest heap a host can make (no descriptor read past the heap) | pes7 | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585, #2599, #2634 |
| [#2686](https://github.com/Marvisak/VIctory/pull/2686) | Shaders: validate far-jump arithmetic and control-flow entries | XeNS1 | files: `crates/victory-shader/src/gfx10/mod.rs`, `crates/victory-shader/src/ir.rs`; with #105, #369, #1335, #1593, #2012, #2079, #2520 |
| [#2690](https://github.com/Marvisak/VIctory/pull/2690) | GPU: report default buffer alignment from GetDesc | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2694](https://github.com/Marvisak/VIctory/pull/2694) | Reject XMA frame starts outside the announcing packet | VlREX | files: `crates/victory-formats/src/xma.rs`; with #364, #1797 |
| [#2696](https://github.com/Marvisak/VIctory/pull/2696) | victory-gpu: VICTORY_SKIP_PIPELINES works in release builds, where the removals are | pes7 | files: `crates/victory-gpu/src/pipeline.rs`; with #491, #1571, #1584, #1922, #2111, #2118, #2273 |
| [#2698](https://github.com/Marvisak/VIctory/pull/2698) | Shaders: derive ATOMIC64_TYPED and ATOMIC64_HEAP from the atomics that are written | Moon0755 | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/shader.rs`; with #1065, #1262, #1716, #1824, #2115, #2150, #2622 |
| [#2703](https://github.com/Marvisak/VIctory/pull/2703) | GPU: a root constant's dword 4 is a value, not a view offset (#2699) | Calvix2k | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2704](https://github.com/Marvisak/VIctory/pull/2704) | Round rectangle half-float attributes to even and preserve NaNs | VlREX | files: `crates/victory-gpu/src/primitive.rs`; with #1418 |
| [#2705](https://github.com/Marvisak/VIctory/pull/2705) | GPU: opt-in video-memory side for host copies of title buffers | MrEjecutor | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/memory.rs`, `crates/victory-gpu/src/shadow.rs`; with #189, #212, #450, #583, #602, #1010, #1283, #1414 |
| [#2709](https://github.com/Marvisak/VIctory/pull/2709) | Avoid publishing a silent XMA output block after a whole-frame skip | VlREX | files: `crates/victory-hle/src/modules/audio.rs`; with #478, #1880, #2524, #2708 |
| [#2710](https://github.com/Marvisak/VIctory/pull/2710) | Apply outstanding XMA sample skips to the final overlap | VlREX | files: `crates/victory-hle/src/modules/audio.rs`; with #478, #1880, #2524, #2708 |
| [#2711](https://github.com/Marvisak/VIctory/pull/2711) | Shaders, GPU: on 32-lane hosts, wave64 halves act as waves; the BVH builder waits (stacked on #2176, #2118) | moe-miau | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #189, #212, #378, #450, #485, #517, #583, #660 |
| [#2713](https://github.com/Marvisak/VIctory/pull/2713) | Shaders: lower binary64 ceiling and floor | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2716](https://github.com/Marvisak/VIctory/pull/2716) | XGameSave: clear stray files at staged version paths | TaynanGT | files: `crates/victory-hle/src/modules/xgamesave.rs`; with #228, #590, #1110, #1123, #1981, #2139, #2511 |
| [#2718](https://github.com/Marvisak/VIctory/pull/2718) | Report overlapping VICTORY_KEYS holds as one active key | VlREX | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942, #2205, #2512, #2557, #2715 |
| [#2721](https://github.com/Marvisak/VIctory/pull/2721) | GPU: a slow-frame report that says what bound the frame and why (guard split out to #2911) | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/pipeline/make.rs`; with #189, #212, #450, #491, #583, #1010, #1283, #1414 |
| [#2723](https://github.com/Marvisak/VIctory/pull/2723) | Shader: key every heap handle cache by element type (#177 on main, fixes the NVIDIA compute-pipeline crash) | andyeox-systemd | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2726](https://github.com/Marvisak/VIctory/pull/2726) | victory-gpu: refresh and route external host textures through one copy | mgunes1311-lab | files: `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #450, #601, #602, #933, #1547, #1776, #1787, #1978 |
| [#2728](https://github.com/Marvisak/VIctory/pull/2728) | Shaders: lower binary64 fractional parts | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2724 |
| [#2730](https://github.com/Marvisak/VIctory/pull/2730) | docs: mention VICTORY_SEMANTICS_REPORT in README | romeawayfromhome-rgb | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2731](https://github.com/Marvisak/VIctory/pull/2731) | PE: tests for delay-import parsing (names, ordinals, IAT bounds) | Vedoxdev123 | files: `crates/victory-pe/src/image.rs`; with #324, #2420, #2630 |
| [#2735](https://github.com/Marvisak/VIctory/pull/2735) | Formats: speed up BC7 BCPack decoding by 27% (and BC1/BC4 by 14-15%) | brainbudt | files: `crates/victory-formats/src/bcpack.rs`; with #703, #1557 |
| [#2736](https://github.com/Marvisak/VIctory/pull/2736) | Formats: speed up GFX10 tiled texture copies up to 2.4x | brainbudt | files: `crates/victory-formats/src/texture.rs`; with #1113, #1792, #2026 |
| [#2740](https://github.com/Marvisak/VIctory/pull/2740) | PE tests: cover section RVA boundaries on every host | XeNS1 | files: `crates/victory-pe/src/image.rs`; with #324, #2420, #2630 |
| [#2743](https://github.com/Marvisak/VIctory/pull/2743) | Shaders: lower binary64 scaling with floating-point modes | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282 |
| [#2747](https://github.com/Marvisak/VIctory/pull/2747) | GPU tests: cover texture alias fallback on runtimes without Device10 | VlREX | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2756](https://github.com/Marvisak/VIctory/pull/2756) | GPU: capture the mip selected by 2D render-target views | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/resource.rs`; with #189, #212, #450, #485, #583, #601, #933, #1010 |
| [#2757](https://github.com/Marvisak/VIctory/pull/2757) | Report keyboard glyphs and dead keys using the focused window layout | maxence468 | files: `crates/victory-hle/src/modules/gameinput.rs`; with #927, #1942, #2205, #2512, #2557, #2715 |
| [#2767](https://github.com/Marvisak/VIctory/pull/2767) | gpu: widen unsupported 16-bit render targets and UAVs to R8G8B8A8_UNORM | narishaa | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/resource.rs`; with #450, #933, #1406, #1547, #1776, #1787, #1978, #1984 |
| [#2773](https://github.com/Marvisak/VIctory/pull/2773) | GPU: a texture is made in the uses its format takes | kais7654 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`; with #24, #189, #212, #450, #485, #583, #933, #1010 |
| [#2774](https://github.com/Marvisak/VIctory/pull/2774) | Shaders: validate raw fixtures and signed MAD64 with full-word regression | LogicGrove | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2776](https://github.com/Marvisak/VIctory/pull/2776) | shader: lower non-sum wave prefix operations to DXIL | JAEdotUK | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2755, #2766, #2768 |
| [#2785](https://github.com/Marvisak/VIctory/pull/2785) | Shaders: single-RPO sparse 1-pass propagate_copies, compact Def table, O(log S) scalar lookup, and stack scratch in resource::track | RVZO6 | files: `crates/victory-shader/src/resource.rs`; with #189, #1253, #1794, #2284, #2422 |
| [#2786](https://github.com/Marvisak/VIctory/pull/2786) | GPU: keep persistent workers in texture::in_parallel so thread_local SCRATCH survives across submissions, and coalesce subresource spans | RVZO6 | files: `crates/victory-gpu/src/texture.rs`; with #601, #602, #1547, #2274, #2478, #2639 |
| [#2787](https://github.com/Marvisak/VIctory/pull/2787) | CLI/GPU: avoid rescanning game_dir and re-inflating/re-hashing cached containers during warm prebuild, and stop Named::find early | RVZO6 | files: `apps/victory/src/prebuild.rs`, `apps/victory/src/translate.rs`, `crates/victory-game/src/pipelines.rs`; with #189, #378, #517, #673, #1676, #1805, #1809, #1866 |
| [#2788](https://github.com/Marvisak/VIctory/pull/2788) | Audio: XMA decoding keeps up while frames are slow (MMCSS thread, the mixer never waits for a decode) | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/audio.rs`; with #478, #1880, #2524, #2708, #2714 |
| [#2789](https://github.com/Marvisak/VIctory/pull/2789) | Shaders: ds_wrap_rtn_b32 reads both of its data operands | lcg007xd-c | files: `crates/victory-shader/src/gfx10/sp3.rs`; with #2761, #2765, #2771 |
| [#2791](https://github.com/Marvisak/VIctory/pull/2791) | Shaders: lower binary64 square root with 32-bit operations | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2755, #2766, #2768 |
| [#2792](https://github.com/Marvisak/VIctory/pull/2792) | fix(shader): allow untracked scalar lane masks in v_cndmask_b32 | legayclightning22 | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2796](https://github.com/Marvisak/VIctory/pull/2796) | Shaders: track GFX10 instruction starts with a bitmap (order-independent decode) | brainbudt | files: `crates/victory-shader/src/gfx10/mod.rs`; with #1335, #2012 |
| [#2799](https://github.com/Marvisak/VIctory/pull/2799) | Shaders: lower binary64 reciprocal with 32-bit operations | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766 |
| [#2801](https://github.com/Marvisak/VIctory/pull/2801) | GPU: integer render targets write unblended on the host (#2775) | miatson | files: `crates/victory-gpu/src/pipeline/host.rs`; with #491, #1571, #1922 |
| [#2803](https://github.com/Marvisak/VIctory/pull/2803) | GPU: keep host pipeline caches per adapter | yumaste | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195, #2706 |
| [#2810](https://github.com/Marvisak/VIctory/pull/2810) | GPU: a deferred copy of memory the submission's shaders write runs after the copy-backs | kotekompotek | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2811](https://github.com/Marvisak/VIctory/pull/2811) | Shaders: lower binary64 reciprocal square root with dwords | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2802 |
| [#2817](https://github.com/Marvisak/VIctory/pull/2817) | Shaders: pixel DPP8 within a quad reads through quad operations; common quad patterns take one | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2802 |
| [#2819](https://github.com/Marvisak/VIctory/pull/2819) | Capture: preserve short words in tiny target logs | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486, #2588, #2589, #2607, #2702 |
| [#2821](https://github.com/Marvisak/VIctory/pull/2821) | GPU: title threads recording lists no longer wait on descriptor and buffer-copy locks | 0xkn0wh3r3 | files: `crates/victory-gpu/src/descriptor.rs`; with #1406, #2278, #2447, #2763 |
| [#2825](https://github.com/Marvisak/VIctory/pull/2825) | Shaders: f16 arithmetic in native half on hosts with 16-bit operations (37x on an RTX 5070 Ti; for #2384) | 0xkn0wh3r3 | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #189, #378, #450, #485, #517, #583, #660, #673 |
| [#2827](https://github.com/Marvisak/VIctory/pull/2827) | Capture: save packed R10G10B10A2 presentation frames | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/capture.rs`; with #601, #1418, #2320, #2486, #2588, #2589, #2607, #2702 |
| [#2830](https://github.com/Marvisak/VIctory/pull/2830) | Shaders: select v_readfirstlane_b32 source lane from the EXEC guard | fuzeofficlal | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2831](https://github.com/Marvisak/VIctory/pull/2831) | Shaders: dwords read from the first lane outside a waterfall's own reads are one lane's (#2829) | BastienRodz | files: `crates/victory-shader/src/resource.rs`; with #189, #1253, #1794, #2284, #2422 |
| [#2832](https://github.com/Marvisak/VIctory/pull/2832) | fix(gpu): add RTV/UAV format fallbacks and restrict format 67 promotion for placed views | legayclightning22 | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2833](https://github.com/Marvisak/VIctory/pull/2833) | Net: a datagram socket that sends before it is bound is bound to loop… | miatson | files: `crates/victory-hle/src/modules/net.rs`; with #997, #2001, #2066 |
| [#2834](https://github.com/Marvisak/VIctory/pull/2834) | GPU: a texture loses the unordered use its format cannot take, as its render target's | kais7654 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`; with #24, #189, #212, #450, #485, #583, #933, #1010 |
| [#2836](https://github.com/Marvisak/VIctory/pull/2836) | Shaders: a lane mask's high dword is the pair's own, not a guess at the register next to the low one | kotekompotek | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2837](https://github.com/Marvisak/VIctory/pull/2837) | GPU diagnostics: name the first observed black frame accurately | 109User109 | files: `crates/victory-gpu/src/queue.rs`; with #450, #2303, #2605, #2666, #2769 |
| [#2840](https://github.com/Marvisak/VIctory/pull/2840) | GPU: validate committed resource probes without allocating | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2841](https://github.com/Marvisak/VIctory/pull/2841) | GPU, Shaders: honor thread dimensions in direct DispatchX (#2750) | brainbudt | files: `crates/victory-gpu/src/pipeline.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #491, #1262, #1571, #1584, #1922, #2111, #2118 |
| [#2843](https://github.com/Marvisak/VIctory/pull/2843) | Shaders: round scaled and normalized D16 buffer loads to nearest even | dooprazol | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2802, #2823 |
| [#2844](https://github.com/Marvisak/VIctory/pull/2844) | GPU: keep CPU descriptor slots until recording consumes them | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs`; with #24, #189, #212, #450, #485, #583, #1010, #1283 |
| [#2846](https://github.com/Marvisak/VIctory/pull/2846) | docs: fix the dangling HDR TODO reference | kyle7908 | files: `crates/victory-hle/src/modules/display.rs`; with #212 |
| [#2848](https://github.com/Marvisak/VIctory/pull/2848) | victory-gpu: take per-frame allocations, locks and system calls off the frame paths (7 places the profile points at) | pes7 | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/watch.rs`; with #1406, #1849, #1884, #2238, #2278, #2447, #2763 |
| [#2849](https://github.com/Marvisak/VIctory/pull/2849) | GPU: open guarded pages in runs, not one VirtualProtect at a time | Therecalloftheonion | files: `crates/victory-gpu/src/watch.rs`; with #1849, #1884, #2238 |
| [#2853](https://github.com/Marvisak/VIctory/pull/2853) | Preserve pipeline cache retries and reject unmapped BVH nodes | Lkxex | files: `crates/victory-gpu/src/pipeline/library.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/lower/bvh.rs`; with #189, #1262, #1653, #1722, #1794, #1903, #2195, #2229 |
| [#2856](https://github.com/Marvisak/VIctory/pull/2856) | GPU: a wider loose window covers a later smaller ask | Luislariosss | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269, #2629 |
| [#2857](https://github.com/Marvisak/VIctory/pull/2857) | Shaders: a mesh program's PSV0 counts shared memory only when it has some | kais7654 | files: `crates/victory-shader/src/emit/mod.rs`, `crates/victory-shader/src/emit/shader.rs`; with #189, #660, #1065, #1262, #1263, #1335, #1716, #1823 |
| [#2860](https://github.com/Marvisak/VIctory/pull/2860) | Net: the IP helper's echo requests and address resolution reach loopback only | miatson | files: `crates/victory-hle/src/modules/net.rs`; with #997, #2001, #2066 |
| [#2861](https://github.com/Marvisak/VIctory/pull/2861) | GPU tests: two tests CI runners failed hold on a loaded host | 0xkn0wh3r3 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/frame.rs`; with #1406, #1548, #1770, #1859, #1946, #2265, #2585, #2599 |
| [#2864](https://github.com/Marvisak/VIctory/pull/2864) | Shaders: live phi edges look up the earlier condition sets they cover | Anzymanz | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823 |
| [#2865](https://github.com/Marvisak/VIctory/pull/2865) | GPU: guard alias_source against null resources, unmapped heaps, and empty planes | danielibabet | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#2866](https://github.com/Marvisak/VIctory/pull/2866) | Translate: count the instructions on 16-bit floats (for #2384, #2825) | xndbogdan | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676, #1809, #2115, #2809 |
| [#2868](https://github.com/Marvisak/VIctory/pull/2868) | Shaders, GPU: a rectangle list's pixel shader can read SV_PrimitiveID | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/rect.rs`; with #1907 |
| [#2871](https://github.com/Marvisak/VIctory/pull/2871) | GPU: clears of one view in a list share one dynamic slot | r4tedx | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#2872](https://github.com/Marvisak/VIctory/pull/2872) | GPU: committed host textures past the budget are evicted and kept, no… | mitaka1959 | files: `README.md`, `crates/victory-gpu/src/host.rs`; with #189, #212, #280, #450, #491, #583, #686, #1010 |
| [#2874](https://github.com/Marvisak/VIctory/pull/2874) | Shaders: refuse side effects in whole-wave sections | yumaste | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823 |
| [#2875](https://github.com/Marvisak/VIctory/pull/2875) | GPU: loose windows can sit in video memory the CPU writes | Luislariosss | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269, #2629 |
| [#2877](https://github.com/Marvisak/VIctory/pull/2877) | GPU: make frame pacing tests deterministic with a virtual clock | alexandruiulian201-bot | files: `crates/victory-gpu/src/frame.rs`; with #2265 |
| [#2879](https://github.com/Marvisak/VIctory/pull/2879) | Formats: render-target XOR layouts (SW_64KB_R_X) have addresses on both consoles | 0xkn0wh3r3 | files: `crates/victory-formats/src/texture.rs`, `crates/victory-gpu/src/console.rs`, `crates/victory-gpu/src/texture.rs`; with #601, #602, #1113, #1418, #1547, #1792, #2026, #2274 |
| [#2883](https://github.com/Marvisak/VIctory/pull/2883) | DirectStorage: physical pages the host refused a view of are written on a retry | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/dstorage.rs`; with #1457, #1719, #2074, #2452, #2553, #2738 |
| [#2885](https://github.com/Marvisak/VIctory/pull/2885) | GPU, Shaders: view structured buffers raw on host for NVIDIA heap reads (FIND-11) | jujumoneylol | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/host.rs`; with #189, #1406, #1548, #1676, #1770, #1857, #1859, #1946 |
| [#2888](https://github.com/Marvisak/VIctory/pull/2888) | GPU tests: one page-table test lock for every test that binds a list | Jackster | files: `crates/victory-gpu/src/memory.rs`; with #1770, #1963, #1978, #2235, #2629, #2805 |
| [#2891](https://github.com/Marvisak/VIctory/pull/2891) | Shaders: track rounding modes set from constant SGPRs | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/semantics_tests.rs`; with #189, #1361, #1991, #2564, #2565, #2570, #2823, #2884 |
| [#2892](https://github.com/Marvisak/VIctory/pull/2892) | tools: cargo xtask refusals <log> says what a run lost, and why | HoLa-Lee | files: `xtask/src/main.rs`; with #545, #1218 |
| [#2895](https://github.com/Marvisak/VIctory/pull/2895) | GPU: a buffer view slot follows the title buffer that holds its bytes | 0xkn0wh3r3 | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585, #2599, #2634 |
| [#2898](https://github.com/Marvisak/VIctory/pull/2898) | GPU: rate-limit capped heap slot warning to once per 64K band | alexandruiulian201-bot | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585, #2599, #2634 |
| [#2899](https://github.com/Marvisak/VIctory/pull/2899) | GPU: confirm the host fence before copying results back | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2900](https://github.com/Marvisak/VIctory/pull/2900) | GPU: a list's upload fills can be shared among threads (VICTORY_FILL_WORKERS) | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2903](https://github.com/Marvisak/VIctory/pull/2903) | HLE: the title's idle and lowest threads run below normal | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/kernel.rs`; with #512, #2506, #2745, #2887, #2902 |
| [#2905](https://github.com/Marvisak/VIctory/pull/2905) | GPU: no copy of a host texture onto itself | 0xkn0wh3r3 | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #2298, #2732, #2818 |
| [#2907](https://github.com/Marvisak/VIctory/pull/2907) | victory: run makes the title's shaders and pipelines before it starts, with a progress window (once; kept on disk) | 0xkn0wh3r3 | files: `README.md`, `apps/victory/Cargo.toml`, `crates/victory-gpu/src/host.rs`; with #189, #212, #280, #450, #491, #583, #686, #1010 |
| [#2908](https://github.com/Marvisak/VIctory/pull/2908) | GPU: a submission's preludes of barriers can be recorded on several threads | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2911](https://github.com/Marvisak/VIctory/pull/2911) | GPU: an opt-in slow-pipeline guard, VICTORY_SLOW_PIPELINES=1 (stacked on #2721) | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/pipeline/make.rs`; with #189, #212, #450, #491, #583, #1010, #1283, #1414 |
| [#2913](https://github.com/Marvisak/VIctory/pull/2913) | GPU: an argument clamp Wine's compiler builds too (carries #1279) | arogan178 | files: `crates/victory-gpu/src/indirect.rs`; with #583 |
| [#2914](https://github.com/Marvisak/VIctory/pull/2914) | GPU: marked pages go back to title memory on several threads (#2826) | kotekompotek | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269, #2629 |
| [#2915](https://github.com/Marvisak/VIctory/pull/2915) | Shaders: an f16 result takes its output modifier | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2916](https://github.com/Marvisak/VIctory/pull/2916) | xmem: mapping pages asks the host only for what it needs | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199, #2742 |
| [#2918](https://github.com/Marvisak/VIctory/pull/2918) | GPU: a marked page's copy-back writes only the bytes the shaders changed, with plain stores | ZeOs360 | files: `crates/victory-gpu/src/copystat.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shadow.rs`; with #189, #212, #450, #583, #602, #1010, #1264, #1283 |
| [#2920](https://github.com/Marvisak/VIctory/pull/2920) | Shaders: lanes of a wave reach group barriers together, as on the console | lhnizdo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/structure.rs`; with #189, #660, #1013, #1262, #1593, #2229, #2254, #2282 |
| [#2924](https://github.com/Marvisak/VIctory/pull/2924) | Shaders: reuse source-lane activity ballots | Ingenioeren | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2925](https://github.com/Marvisak/VIctory/pull/2925) | Shaders: one console wave run as two host waves meets at barriers between its LDS phases (stacked on #2176) | moe-miau | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`; with #189, #212, #378, #450, #485, #517, #583, #660 |
| [#2926](https://github.com/Marvisak/VIctory/pull/2926) | Shaders: saturate clamped 24-bit multiply and multiply-add | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2927](https://github.com/Marvisak/VIctory/pull/2927) | docs: explain GPU timing overhead | FR4NC7S | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2928](https://github.com/Marvisak/VIctory/pull/2928) | Shaders: a mesh primitive naming a vertex no lane writes is culled | 0xkn0wh3r3 | files: `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1263, #1335, #1716, #1823, #1991, #2115 |
| [#2929](https://github.com/Marvisak/VIctory/pull/2929) | GPU (diagnostics): the frame-rate line ranks host copies by what video memory would save | 0xkn0wh3r3 | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#2934](https://github.com/Marvisak/VIctory/pull/2934) | README: say VICTORY_GPU_TIMING's times are the mode's, not a normal frame's (FIND-29) | Jackster | files: `README.md`; with #280, #491, #686, #1218, #1263, #1584, #1701, #1703 |
| [#2936](https://github.com/Marvisak/VIctory/pull/2936) | victory-gpu: 16-bit packed colour widens for the host (the second crash between the account screen and gameplay), and the two tools it took | pes7 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #485, #583, #1010, #1283, #1414 |
| [#2937](https://github.com/Marvisak/VIctory/pull/2937) | GPU tests: the two view-heap tests say when a host caps the heap | HoLa-Lee | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585, #2599, #2634 |
| [#2938](https://github.com/Marvisak/VIctory/pull/2938) | Shaders: lower RDNA2 lighting multiply in DXIL | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2940](https://github.com/Marvisak/VIctory/pull/2940) | GPU/Bindless: O(1) texture forget reverse index, FxHash maps, and identical-rewrite fast-path | RVZO6 | files: `crates/victory-gpu/src/bindless.rs`; with #1547, #1862, #2196 |
| [#2941](https://github.com/Marvisak/VIctory/pull/2941) | Shaders: encoding-gated fast scans, zero-alloc wave::simulate, and dense range::relative_bounds | RVZO6 | files: `crates/victory-shader/src/emit/wave.rs`, `crates/victory-shader/src/range.rs`; with #189, #1802, #2079, #2491 |
| [#2942](https://github.com/Marvisak/VIctory/pull/2942) | Shaders/Lower: dense Value tables, FxHash maps, lazy get() mask checks, O(1) valu16 reject, and zero-alloc buffer/mask helpers | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2948](https://github.com/Marvisak/VIctory/pull/2948) | Shaders, GPU: a root UAV a shader only reads is not written back | 0xkn0wh3r3 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-shader/src/emit/shader.rs`; with #189, #450, #485, #583, #1065, #1262, #1716, #1765 |
| [#2951](https://github.com/Marvisak/VIctory/pull/2951) | victory: translate --cache and the pre-build say where their time went (slowest shaders and pipelines, library saves) | 0xkn0wh3r3 | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195, #2706 |
| [#2953](https://github.com/Marvisak/VIctory/pull/2953) | Shaders: lower binary64 division fixup in DXIL | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2954](https://github.com/Marvisak/VIctory/pull/2954) | Shaders: lower v_bfe_u32/v_bfe_i32 to one Ubfe/Ibfe | Ingenioeren | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #1065, #1262, #1716, #2115, #2150, #2229, #2254 |
| [#2956](https://github.com/Marvisak/VIctory/pull/2956) | Loader/TLS: use memchr::memmem SIMD scan in tls::patch | RVZO6 | files: `crates/victory-loader/src/tls.rs`; with #188 |
| [#2957](https://github.com/Marvisak/VIctory/pull/2957) | Shaders/IR: pruned SSA via bitset IDF + dominator-tree renaming, linear CFG scan, and early dropped-inst skip | RVZO6 | files: `crates/victory-shader/src/ir.rs`; with #105, #369, #1593, #2079, #2520 |
| [#2958](https://github.com/Marvisak/VIctory/pull/2958) | Shaders: one lane of a wave sets a mark its wave shares (frames 411 -> 283 ms on an RTX 4070 SUPER) | moe-miau | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2959](https://github.com/Marvisak/VIctory/pull/2959) | GPU: report pipeline creation and loads after they succeed | necrobytes | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195, #2706 |
| [#2960](https://github.com/Marvisak/VIctory/pull/2960) | Cut the 17 s world frames with asynchronous submission and a copy queue | ynnmuraii | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/pipeline/make.rs`, `crates/victory-gpu/src/queue.rs`; with #24, #189, #212, #450, #583, #1010, #1264, #1283 |
| [#2963](https://github.com/Marvisak/VIctory/pull/2963) | Shaders: allow abs/neg source modifiers on v_cvt_{u16,i16}_f16 | Dukestar69 | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#2965](https://github.com/Marvisak/VIctory/pull/2965) | GPU: reject mismatched command list allocators | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/list.rs`; with #24, #450, #1428, #2298, #2732, #2818 |
| [#2967](https://github.com/Marvisak/VIctory/pull/2967) | Shaders: track spilled lane masks, Atom::Phi back-edges, and carry masks | Dukestar69 | files: `crates/victory-shader/src/structure.rs`; with #660, #1013, #1593, #2406, #2816 |
| [#2969](https://github.com/Marvisak/VIctory/pull/2969) | GPU: shaders of our own that Wine's compiler builds too | neonbyte1 | files: `crates/victory-gpu/src/bindless.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/pipeline/library.rs`, `crates/victory-gpu/src/twin.rs`; with #189, #450, #485, #583, #1547, #1653, #1722, #1765 |
| [#2970](https://github.com/Marvisak/VIctory/pull/2970) | Shaders: keep v0 as the leading vertex of both rectangle triangles | fuzeofficlal | files: `crates/victory-shader/src/emit/rect.rs`; with #1907, #2964 |
| [#2971](https://github.com/Marvisak/VIctory/pull/2971) | GPU: store HostHeap kept/made sparsely and allocate strides/marks lazily | 0xKaji | files: `crates/victory-gpu/src/descriptor/host.rs`; with #1406, #1548, #1770, #1859, #1946, #2585, #2599, #2634 |
| [#2972](https://github.com/Marvisak/VIctory/pull/2972) | GPU: reclaim idle staging, scratch, and arena buffers and evict on system memory pressure | 0xKaji | files: `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs`; with #450, #601, #602, #933, #1547, #1776, #1787, #1978 |
| [#2973](https://github.com/Marvisak/VIctory/pull/2973) | Tests and fixes so the suite runs under Wine | neonbyte1 | files: `crates/victory-gpu/src/bindless.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/pipeline/library.rs`; with #189, #450, #485, #583, #997, #1361, #1406, #1547 |
| [#2974](https://github.com/Marvisak/VIctory/pull/2974) | GPU: reduce shader and pipeline RAM usage (Weak cache, deflate containers, 32 MiB DXIL cache) | 0xKaji | files: `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/make.rs`; with #491, #1505, #1571, #1584, #1922, #2111, #2118, #2223 |
| [#2975](https://github.com/Marvisak/VIctory/pull/2975) | Shaders: lower v_div_scale_f64 and its lane mask | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2977](https://github.com/Marvisak/VIctory/pull/2977) | Shaders: one back edge per block, for the dxil-spirv in Proton | neonbyte1 | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs`; with #189, #1065, #1262, #1716, #2115, #2150, #2229, #2254 |
| [#2978](https://github.com/Marvisak/VIctory/pull/2978) | Shaders: whole-wave sections follow binary64 sums (WaveActiveSum of a double) | Anzymanz | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1065, #1262, #1362, #1716, #1784, #1811, #1857 |
| [#2982](https://github.com/Marvisak/VIctory/pull/2982) | Loader/Prepare: zero-alloc block-filtered DIR64 relocation clearing for TLS callbacks | RVZO6 | files: `crates/victory-loader/src/prepare.rs`; with #2418 |
| [#2983](https://github.com/Marvisak/VIctory/pull/2983) | Shaders/Emit: clear D3D12 filter reduction bits (0x180) before setting comparison bit (0x80) | RVZO6 | files: `crates/victory-shader/src/emit/mod.rs`; with #189, #660, #1263, #1335, #1716, #1823, #1991, #2115 |
| [#2984](https://github.com/Marvisak/VIctory/pull/2984) | GPU: implement ClearState on command lists | fuzeofficlal | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/list.rs`; with #24, #189, #450, #485, #583, #1428, #1765, #1825 |
| [#2985](https://github.com/Marvisak/VIctory/pull/2985) | GPU: a tracked texture write detiles and copies only the rows it touches (#1135) | wwwwwwww3333333 | files: `crates/victory-formats/src/texture.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/texture.rs`; with #189, #450, #485, #583, #601, #602, #1113, #1547 |
| [#2986](https://github.com/Marvisak/VIctory/pull/2986) | GPU: use one warm-up key for reordered graphics shader stages | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/pipeline.rs`; with #491, #1571, #1584, #1922, #2111, #2118, #2273, #2952 |
| [#2987](https://github.com/Marvisak/VIctory/pull/2987) | HLE: retain DirectStorage file references across queued reads | fuzeofficlal | files: `crates/victory-hle/src/modules/dstorage.rs`; with #1457, #1719, #2074, #2452, #2553, #2738, #2904, #2981 |
| [#2988](https://github.com/Marvisak/VIctory/pull/2988) | Shaders: lower v_trig_preop_f64 argument reduction | andrewpozdnakov7-jpg | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#2992](https://github.com/Marvisak/VIctory/pull/2992) | Build and test the portable crates on non-Windows hosts | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/kernel.rs`; with #512, #2506, #2745, #2887, #2902 |
| [#2993](https://github.com/Marvisak/VIctory/pull/2993) | GPU: host copies of title buffers in video memory, under a DXGI budget (opt-in) | r4tedx | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs`, `crates/victory-gpu/src/shadow.rs`; with #189, #212, #450, #485, #583, #602, #1010, #1264 |
| [#2994](https://github.com/Marvisak/VIctory/pull/2994) | GPU: keep v0 as the leading vertex in CPU-expanded rectangles | steven-seagull27 | files: `crates/victory-gpu/src/pipeline/host.rs`; with #491, #1571, #1922, #2897, #2952 |
| [#2995](https://github.com/Marvisak/VIctory/pull/2995) | HLE: return Winsock sockaddr errors from getnameinfo on invalid input | fuzeofficlal | files: `crates/victory-hle/src/modules/net.rs`; with #997, #2001, #2066 |
| [#2997](https://github.com/Marvisak/VIctory/pull/2997) | Shaders: fix compute lane permutations on WARP | andrewpozdnakov7-jpg | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/shader_cache.rs`; with #189, #212, #378, #450, #485, #491, #517, #583 |
| [#2999](https://github.com/Marvisak/VIctory/pull/2999) | Shaders: implicit-level samples in compute follow the console's lane quads (#2027, on #1237) | wwwwwwww3333333 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs`; with #189, #1262, #1991, #2229, #2254, #2282, #2323, #2587 |
| [#3000](https://github.com/Marvisak/VIctory/pull/3000) | emit host: an empty root-constant list is not passed to the runtime | HoLa-Lee | files: `crates/victory-shader/src/emit/host.rs`; with #189, #1676, #1857, #1991, #2041, #2450, #2587, #2878 |
| [#3003](https://github.com/Marvisak/VIctory/pull/3003) | CLI: deduplicate translate containers by declared container bytes instead of DXIL payload alone | fuzeofficlal | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676, #1809, #2115, #2809 |
| [#3004](https://github.com/Marvisak/VIctory/pull/3004) | CLI: discover compressed shader packs in archives without SGD5 or header magic | fuzeofficlal | files: `apps/victory/src/prebuild.rs`; with #1805, #1809, #2592 |
| [#3008](https://github.com/Marvisak/VIctory/pull/3008) | Shaders/Lower: align and extract sub-dword buffer_load_{ubyte,sbyte,ushort,sshort} on CBVs | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#3009](https://github.com/Marvisak/VIctory/pull/3009) | Shaders/Lower: reject non-zero soffset/built_offset on typed buffer_store_format_xyzw | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#3010](https://github.com/Marvisak/VIctory/pull/3010) | Shaders/Lower: return 6 faces for channel 2 of image_get_resinfo on SQ_RSRC_IMG_CUBE | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#3011](https://github.com/Marvisak/VIctory/pull/3011) | Build: thin LTO, x86-64-v3 on Windows, xxh3 for texture change detection | 0xkn0wh3r3 | files: `Cargo.lock`, `Cargo.toml`; with #677, #2426, #2581, #2809, #2950 |
| [#3013](https://github.com/Marvisak/VIctory/pull/3013) | GPU: keep untracked pages writable in Tracked::taken | fuzeofficlal | files: `crates/victory-gpu/src/watch.rs`; with #1849, #1884, #2238, #2966 |
| [#3016](https://github.com/Marvisak/VIctory/pull/3016) | Shaders: the SCC a waterfall loop's s_andn2_wrexec leaves is false after the loop | Anzymanz | files: `crates/victory-shader/src/emit/valu_tests.rs`; with #189, #1262, #1362, #1784, #1811, #1857, #1879, #1892 |
| [#3017](https://github.com/Marvisak/VIctory/pull/3017) | Fix #2413: use saturating_add for view end bounds in aliases | tharun-37 | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199, #2742 |
| [#3018](https://github.com/Marvisak/VIctory/pull/3018) | HLE: share DirectStorage file opens and keep the host's error code | Halfect | files: `crates/victory-hle/src/modules/dstorage.rs`; with #1457, #1719, #2074, #2452, #2553, #2738, #2904, #2981 |
| [#3021](https://github.com/Marvisak/VIctory/pull/3021) | Tests: the conformance title's GPU frame, cargo conformance and cargo demo (with a stress scale), on Windows and macOS | 0xkn0wh3r3 | files: `README.md`, `crates/victory-hle/Cargo.toml`, `xtask/src/main.rs`; with #280, #491, #545, #686, #1218, #1263, #1584, #1701 |
| [#3022](https://github.com/Marvisak/VIctory/pull/3022) | GPU: read D24S8 and D32S8 planes into guest buffers | andrewpozdnakov7-jpg | files: `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`; with #24, #450, #933, #1428, #1547, #1776, #1787, #1978 |
| [#3023](https://github.com/Marvisak/VIctory/pull/3023) | Shaders: s_cbranch_vccz/vccnz on a scalar VCC decide once for the wave (#2780, on #2836) | wwwwwwww3333333 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs`, `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/structure.rs`; with #189, #660, #1013, #1262, #1362, #1593, #1784, #1811 |
| [#3025](https://github.com/Marvisak/VIctory/pull/3025) | GPU: graphics pipelines are made before compute ones, and compute never takes every worker | Luislariosss | files: `crates/victory-gpu/src/pipeline/make.rs`; with #1505, #1571, #2111, #2118, #2223, #2897, #2944, #2980 |
| [#3026](https://github.com/Marvisak/VIctory/pull/3026) | xtask: bound policy file reads and report read errors | fuzeofficlal | files: `xtask/src/policy.rs`; with #2246, #2581, #2642 |
| [#3029](https://github.com/Marvisak/VIctory/pull/3029) | CLI: keep distinct DXIL dumps when shader labels collide | passerbyyhx | files: `apps/victory/src/translate.rs`; with #189, #378, #517, #673, #1676, #1809, #2115, #2809 |
| [#3031](https://github.com/Marvisak/VIctory/pull/3031) | GPU/Shadow: advance saved before snapshot after merge_writeback in copy_back_or_not | RVZO6 | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269, #2629 |
| [#3032](https://github.com/Marvisak/VIctory/pull/3032) | Shaders/Lower: reject unmodeled non-VOP3P modifiers in Lower::packed16 | RVZO6 | files: `crates/victory-shader/src/emit/lower.rs`; with #189, #1262, #2229, #2254, #2282, #2766, #2823, #2886 |
| [#3033](https://github.com/Marvisak/VIctory/pull/3033) | GPU: load an optional D3D12 Agility SDK | Auroraooy | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-shader/Cargo.toml`; with #189, #212, #280, #450, #477, #491, #583, #686 |
| [#3035](https://github.com/Marvisak/VIctory/pull/3035) | GPU: write faults read the bytes they save without the guard lock | liandraraiane | files: `crates/victory-gpu/src/watch.rs`; with #1849, #1884, #2238, #2966 |
| [#3036](https://github.com/Marvisak/VIctory/pull/3036) | GPU: a copy-back still pending when the title takes the range back writes nothing | HoLa-Lee | files: `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1816, #2153, #2269, #2629 |
| [#3039](https://github.com/Marvisak/VIctory/pull/3039) | GPU: a lost host list's heaps are not a wanted pair | kotekompotek | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#3040](https://github.com/Marvisak/VIctory/pull/3040) | Game: recover depth-bounds-enabled states in pipeline prebuild | fuzeofficlal | files: `crates/victory-game/src/pipelines.rs`; with #1866, #2575 |
| [#3041](https://github.com/Marvisak/VIctory/pull/3041) | GPU: refresh heap textures with untracked pages (FIND-17) | leftmove | files: `crates/victory-gpu/src/texture.rs`; with #601, #602, #1547, #2274, #2478, #2639, #2859 |
| [#3042](https://github.com/Marvisak/VIctory/pull/3042) | Loader: extrq/insertq with the field in the instruction jump to SSE2 code after their first fault | 101Leafy | files: `crates/victory-loader/src/crash.rs`; with #1966, #2165, #2445, #2554, #2659 |
| [#3043](https://github.com/Marvisak/VIctory/pull/3043) | Shaders, GPU: clamp immediate static sampler MipLODBias to D3D12 bounds | fuzeofficlal | files: `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-shader/src/emit/sampler.rs`; with #491, #1571, #1922, #2812, #2897, #2952 |
| [#3044](https://github.com/Marvisak/VIctory/pull/3044) | CLI: refuse VICTORY_PREBUILD_KEYS paths inside the repository | fuzeofficlal | files: `apps/victory/src/prebuild.rs`; with #1805, #1809, #2592 |
| [#3046](https://github.com/Marvisak/VIctory/pull/3046) | Run, GPU: save the pipeline cache on normal title exit | fuzeofficlal | files: `crates/victory-gpu/src/pipeline/library.rs`; with #1653, #1722, #2195, #2706 |
| [#3047](https://github.com/Marvisak/VIctory/pull/3047) | Game: name rasterisers from the pack's register images | zed6000 | files: `crates/victory-game/src/pipelines.rs`; with #1866, #2575 |
| [#3048](https://github.com/Marvisak/VIctory/pull/3048) | Game: try what depth-stencil registers do not keep (stacked on #3047) | zed6000 | files: `crates/victory-game/src/pipelines.rs`; with #1866, #2575 |
| [#3050](https://github.com/Marvisak/VIctory/pull/3050) | GPU: our view heap is bound for a list that binds none | kotekompotek | files: `crates/victory-gpu/src/draw.rs`; with #189, #450, #485, #583, #1765, #1825, #1963, #2118 |
| [#3051](https://github.com/Marvisak/VIctory/pull/3051) | GPU: mesh pipelines without a pixel shader get an empty one on WARP | redNSF | files: `crates/victory-gpu/src/host.rs`; with #189, #212, #450, #583, #1010, #1283, #1414, #1555 |
| [#3053](https://github.com/Marvisak/VIctory/pull/3053) | xmem: large graphics blocks get write-watched memory of their own | 0xkn0wh3r3 | files: `crates/victory-hle/src/modules/xmem.rs`; with #76, #1264, #1445, #1947, #2022, #2184, #2199, #2742 |
| [#3055](https://github.com/Marvisak/VIctory/pull/3055) | GPU: batch and parallelize descriptor heap syncs | MeMako | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/shadow.rs`; with #583, #602, #1406, #1548, #1770, #1816, #1859, #1946 |
| [#3057](https://github.com/Marvisak/VIctory/pull/3057) | GPU/Resource: support 2-plane D16_UNORM_S8_UINT formats (118..=120) in GetCopyableFootprints | RVZO6 | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |
| [#3058](https://github.com/Marvisak/VIctory/pull/3058) | GPU/COM: return hidden sret out pointer in RAX from Heap/Resource/DescriptorHeap/Queue GetDesc | RVZO6 | files: `crates/victory-gpu/src/resource.rs`; with #450, #933, #1547, #1776, #1787, #1978, #1984, #2005 |

## conflicts with main (397)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#32](https://github.com/Marvisak/VIctory/pull/32) | GPU: fence waits, direct memory-write wakes, queue timeline and host list pool | AndyLatimer | files: `crates/victory-gpu/src/fence.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs` |
| [#55](https://github.com/Marvisak/VIctory/pull/55) | GPU: create host textures without the uses the host refuses | a55uka | files: `crates/victory-gpu/src/resource.rs` |
| [#72](https://github.com/Marvisak/VIctory/pull/72) | GPU: retry pipeline cache saves after write failures | FIocker | files: `crates/victory-gpu/src/pipeline/library.rs` |
| [#78](https://github.com/Marvisak/VIctory/pull/78) | Shaders: inline float constants as f16 in v_fma_mix and v_pack_b32_f16 | tedin7 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#82](https://github.com/Marvisak/VIctory/pull/82) | HLE: speak the title's narration with the host's speech synthesizer | permadiego | files: `crates/victory-hle/Cargo.toml` |
| [#83](https://github.com/Marvisak/VIctory/pull/83) | GPU: bound the null sampler staging heap | FIocker | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#89](https://github.com/Marvisak/VIctory/pull/89) | gpu: packed 16-bit render targets are R8G8B8A8 where the GPU cannot render to them | HenriqueSBueno | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/texture.rs` |
| [#91](https://github.com/Marvisak/VIctory/pull/91) | Shaders: lower s_cmov_b32, s_cmov_b64 and s_cmovk_i32 | tedin7 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#92](https://github.com/Marvisak/VIctory/pull/92) | Shaders: lower v_add_nc_i32, v_sub_nc_i32, v_mul_lo_i32 and the signed 16-bit add and sub | tedin7 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#98](https://github.com/Marvisak/VIctory/pull/98) | Shaders: model v_permlane16_b32 in whole-wave sections | tedin7 | files: `crates/victory-shader/src/emit/wave.rs` |
| [#112](https://github.com/Marvisak/VIctory/pull/112) | Build: Linux workspace, contributor setup and CI | Quat3rnion | files: `apps/victory/src/translate.rs`, `crates/victory-hle/src/modules/xgameui.rs` |
| [#120](https://github.com/Marvisak/VIctory/pull/120) | Shaders: lower s_absdiff_i32, s_sext_i32_i8/i16 and s_pack_ll/lh/hh_b32_b16 | tedin7 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#123](https://github.com/Marvisak/VIctory/pull/123) | GPU: refuse raw buffer views that do not start on 16 bytes | 9hvn9yt2vk-netizen | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#130](https://github.com/Marvisak/VIctory/pull/130) | Profile: opt-in VICTORY_PROFILE (frame times, memory, caches, loads; frames.csv, a Perfetto trace and an on-screen overlay) | Sunkiller-qc | files: `apps/victory/src/run.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-gpu/src/texture.rs` |
| [#145](https://github.com/Marvisak/VIctory/pull/145) | Shaders: read both ballot halves for wave32 host-wave mask ops | 7ROBE | files: `crates/victory-shader/src/emit/lower.rs` |
| [#148](https://github.com/Marvisak/VIctory/pull/148) | Shaders: lower s_bcnt0_i32_b32/_b64, s_ff0_i32_b32/_b64 and s_flbit_i32_b64/_i64 | Rareuncommon | files: `crates/victory-shader/src/emit/lower.rs` |
| [#150](https://github.com/Marvisak/VIctory/pull/150) | Input: read DualSense pads over HID when XInput has none | Kam471 | files: `README.md`, `crates/victory-hle/src/modules/mod.rs` |
| [#157](https://github.com/Marvisak/VIctory/pull/157) | Shaders: lower 24-bit mul_hi, saturating 16-bit packs, integer dot pr… | 9hvn9yt2vk-netizen | files: `crates/victory-shader/src/emit/lower.rs` |
| [#168](https://github.com/Marvisak/VIctory/pull/168) | Shaders: SCC of s_min, s_max and s_lshl1-4_add_u32 as the ISA sets it | Dufftwt | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#177](https://github.com/Marvisak/VIctory/pull/177) | Shaders: key heap handles by element type (atomic on a float-read UAV) | Ortomanic | files: `crates/victory-shader/src/emit/lower.rs` |
| [#182](https://github.com/Marvisak/VIctory/pull/182) | Files: `..` in a title path stops at the virtual drive's root | Maraco91 | files: `crates/victory-hle/src/modules/files.rs` |
| [#192](https://github.com/Marvisak/VIctory/pull/192) | Shaders: replace single-wave Wave64 LDS lockstep with barriers and lower 32-lane swizzle/DPP at WaveSize(32) | kxiserino | files: `crates/victory-shader/src/emit/lower.rs` |
| [#202](https://github.com/Marvisak/VIctory/pull/202) | GPU: skip unmapped regions after a failed bulk read into host memory | ifBars | files: `crates/victory-gpu/src/host.rs` |
| [#216](https://github.com/Marvisak/VIctory/pull/216) | Loader & HLE: harden VEH crash handler, PE prep/exports/TLS, and allow oleaut32 | wbkepler | files: `crates/victory-loader/src/crash.rs` |
| [#222](https://github.com/Marvisak/VIctory/pull/222) | apu: warn when the host has no audio output device | a55uka | files: `README.md` |
| [#224](https://github.com/Marvisak/VIctory/pull/224) | HLE: report the host's commit headroom before the title starts | WallasSCRIPTS | files: `README.md`, `crates/victory-hle/src/modules/xmem.rs` |
| [#230](https://github.com/Marvisak/VIctory/pull/230) | GPU: skip unchanged texture uploads via prelude copy recording | wbkepler | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs` |
| [#234](https://github.com/Marvisak/VIctory/pull/234) | HLE: overlapped DirectStorage I/O and persistent xmem section views | wbkepler | files: `crates/victory-hle/src/modules/dstorage.rs` |
| [#236](https://github.com/Marvisak/VIctory/pull/236) | XAsync: a canceled pending call's work touches neither freed state nor the next call | Dufftwt | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#237](https://github.com/Marvisak/VIctory/pull/237) | HLE: offload async saves, reuse audio buffers, pin APU heap, and decouple input rumble/dialogs | wbkepler | files: `crates/victory-hle/src/modules/apu.rs`, `crates/victory-hle/src/modules/audio.rs`, `crates/victory-hle/src/modules/gameinput.rs`, `crates/victory-hle/src/modules/xasync.rs`, `crates/victory-hle/src/modules/xgamesave.rs` |
| [#242](https://github.com/Marvisak/VIctory/pull/242) | GPU: make ExecuteIndirect clamping countBuffer-aware and non-destructive | wbkepler | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs` |
| [#250](https://github.com/Marvisak/VIctory/pull/250) | GPU & CLI: configurable/uncapped FPS limit, high-res pacing, high-refresh modes, and tearing swapchain | wbkepler | files: `crates/victory-gpu/src/frame.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs` |
| [#261](https://github.com/Marvisak/VIctory/pull/261) | GPU: copy-back puts back only what shaders wrote, in two more cases | Maraco91 | files: `crates/victory-gpu/src/shadow.rs` |
| [#269](https://github.com/Marvisak/VIctory/pull/269) | Shaders: scalars leave divergent loops and branches as the wave's last path left them | TheHoracio | files: `crates/victory-shader/src/emit/lower.rs` |
| [#275](https://github.com/Marvisak/VIctory/pull/275) | GPU: atomic adaptive PSO wait budget and non-blocking pipeline library saves | wbkepler | files: `crates/victory-gpu/src/pipeline/library.rs`, `crates/victory-gpu/src/pipeline/make.rs` |
| [#278](https://github.com/Marvisak/VIctory/pull/278) | GPU: answer format-info and virtual-address feature queries | Quat3rnion | files: `crates/victory-gpu/src/device.rs` |
| [#279](https://github.com/Marvisak/VIctory/pull/279) | GPU: name the commands at a DRED stop, and dump translated shaders | ALFREDOHDEZ | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline.rs` |
| [#284](https://github.com/Marvisak/VIctory/pull/284) | Shaders: RDNA2's legacy multiply-adds are the fused ones | Dufftwt | files: `crates/victory-shader/src/gfx10/opcodes.rs` |
| [#290](https://github.com/Marvisak/VIctory/pull/290) | HLE tests: cover Windows path rules on every host | Quat3rnion | files: `crates/victory-hle/src/modules/mod.rs` |
| [#292](https://github.com/Marvisak/VIctory/pull/292) | Shader: lower WQM QuadAny, clamp LDS accesses, and guard loop budgets & barriers | wbkepler | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/structure.rs` |
| [#301](https://github.com/Marvisak/VIctory/pull/301) | GPU: non-stream graphics PSOs, stream subobjects 25..=28, texture-to-buffer readbacks, and sRGB view preservation | wbkepler | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/host.rs` |
| [#310](https://github.com/Marvisak/VIctory/pull/310) | Policy: resolve cache paths inside Windows AppContainer | melon0918 | files: `crates/victory-core/src/policy.rs` |
| [#312](https://github.com/Marvisak/VIctory/pull/312) | HLE: SDL3 gamepad backend for the gameinput shim | DaviTostes | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#317](https://github.com/Marvisak/VIctory/pull/317) | Shaders: support cube dimension in descriptor_data | tarcisioads | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#319](https://github.com/Marvisak/VIctory/pull/319) | GPU: end a late flip wait on the tick it missed, not the next | xmvo | files: `crates/victory-gpu/src/frame.rs` |
| [#321](https://github.com/Marvisak/VIctory/pull/321) | GPU: honour scheduled frame-event offsets | Quat3rnion | files: `crates/victory-gpu/src/frame.rs` |
| [#328](https://github.com/Marvisak/VIctory/pull/328) | Shaders: lower MSAA image_load and image_get_resinfo | tarcisioads | files: `crates/victory-shader/src/emit/lower.rs` |
| [#329](https://github.com/Marvisak/VIctory/pull/329) | Shaders: recover record counts for descriptor-only structured buffers | Raxstreams | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#332](https://github.com/Marvisak/VIctory/pull/332) | Shaders: lower partial-channel image_store | tarcisioads | files: `crates/victory-shader/src/emit/lower.rs` |
| [#342](https://github.com/Marvisak/VIctory/pull/342) | Shaders: lower partial-channel typed buffer stores | tarcisioads | files: `crates/victory-shader/src/emit/lower.rs` |
| [#347](https://github.com/Marvisak/VIctory/pull/347) | GPU: ask for an empty pipeline library with a null blob | AugustoZFJ | files: `crates/victory-gpu/src/pipeline/library.rs` |
| [#374](https://github.com/Marvisak/VIctory/pull/374) | XAsync: a wait on a failed call during its cleanup waits for the status | marquezinii | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#388](https://github.com/Marvisak/VIctory/pull/388) | GPU: refresh unwatched textures without a region query; detile into cached memory | ItsYusei99 | files: `crates/victory-gpu/src/texture.rs` |
| [#402](https://github.com/Marvisak/VIctory/pull/402) | GPU: find a buffer holding an address past many smaller ones; reuse loose windows that hold a range | kxiserino | files: `crates/victory-gpu/src/shadow.rs` |
| [#411](https://github.com/Marvisak/VIctory/pull/411) | GPU: require only the descriptor heaps used by the pipeline | FIocker | files: `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-shader/src/emit/shader.rs` |
| [#412](https://github.com/Marvisak/VIctory/pull/412) | HLE: validate XPackage chunk selectors | enzoduarte1 | files: `crates/victory-hle/src/modules/xpackage.rs` |
| [#416](https://github.com/Marvisak/VIctory/pull/416) | shader: implement v_cvt_f32_f64 instruction lowering | bitzin-dev | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#420](https://github.com/Marvisak/VIctory/pull/420) | GPU: include root-selected entries in rebuilt descriptor tables | FIocker | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#425](https://github.com/Marvisak/VIctory/pull/425) | Game: validate DXBC containers in SGD5 records | enzoduarte1 | files: `crates/victory-game/src/sgd5.rs` |
| [#427](https://github.com/Marvisak/VIctory/pull/427) | GPU: say in device-removed reports which user data is a table | GamingRipperDoc | files: `crates/victory-gpu/src/draw.rs` |
| [#428](https://github.com/Marvisak/VIctory/pull/428) | GameInput: next and previous readings of a disconnected device fail | marquezinii | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#430](https://github.com/Marvisak/VIctory/pull/430) | DirectStorage: Close completes what was submitted | marquezinii | files: `crates/victory-hle/src/modules/dstorage.rs` |
| [#434](https://github.com/Marvisak/VIctory/pull/434) | Shaders: a wave32 program's mask read picks its half of a 64-lane ballot | NolanCotter | files: `crates/victory-shader/src/emit/lower.rs` |
| [#435](https://github.com/Marvisak/VIctory/pull/435) | GPU: coalesce identical write declarations within a submission | melon0918 | files: `crates/victory-gpu/src/host.rs` |
| [#443](https://github.com/Marvisak/VIctory/pull/443) | Audio: keep XMA frames split across rolling inputs | Quat3rnion | files: `crates/victory-formats/src/xma.rs`, `crates/victory-hle/src/modules/audio.rs` |
| [#458](https://github.com/Marvisak/VIctory/pull/458) | Fix GPU hangs, memory leak, and mesh shader exports; render intro cre… | techselect | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/resource.rs` |
| [#463](https://github.com/Marvisak/VIctory/pull/463) | GPU: load an app-local D3D12 Agility SDK runtime when present | Shaun-Fong | files: `README.md`, `apps/victory/src/main.rs` |
| [#470](https://github.com/Marvisak/VIctory/pull/470) | shader: lower wave prefixes of min and max | Loggerten | files: `crates/victory-shader/src/emit/lower.rs` |
| [#472](https://github.com/Marvisak/VIctory/pull/472) | GPU: grow the write snapshot in place, and cap idle pool memory | SaymonMaster14 | files: `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/texture.rs` |
| [#482](https://github.com/Marvisak/VIctory/pull/482) | App: reject wrapping RVAs in VICTORY_WATCH | enzoduarte1 | files: `apps/victory/src/run.rs` |
| [#492](https://github.com/Marvisak/VIctory/pull/492) | GPU: substitute R9G9B9E5_SHAREDEXP render targets and UAVs with R16G16B16A16_FLOAT | Yaekai | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs` |
| [#498](https://github.com/Marvisak/VIctory/pull/498) | shader: lower v_movrelsd_2_b32 and v_swaprel_b32 | NolanCotter | files: `crates/victory-shader/src/emit/lower.rs` |
| [#499](https://github.com/Marvisak/VIctory/pull/499) | shader: lower v_sat_pk_u8_i16 | NolanCotter | files: `crates/victory-shader/src/emit/lower.rs` |
| [#500](https://github.com/Marvisak/VIctory/pull/500) | GPU diagnostics: pick capture frames by draw count | itsRevela | files: `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/queue.rs` |
| [#503](https://github.com/Marvisak/VIctory/pull/503) | HLE: pin a call's task queue at XAsyncBegin | Quat3rnion | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#521](https://github.com/Marvisak/VIctory/pull/521) | Shaders: model the compute thread-group info SGPR's wave count | AnoHunted | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#523](https://github.com/Marvisak/VIctory/pull/523) | Build: compile and test the workspace on Linux again | spidercraft | files: `apps/victory/src/translate.rs`, `crates/victory-hle/src/modules/xgame.rs`, `crates/victory-hle/src/modules/xgameui.rs` |
| [#530](https://github.com/Marvisak/VIctory/pull/530) | GPU diagnostics: show one of the title's render targets in the window | AKA0GHOST | files: `README.md`, `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/host.rs` |
| [#535](https://github.com/Marvisak/VIctory/pull/535) | App: enforce asset policy check in default_paths | pushkarreddyy | files: `apps/victory/src/main.rs` |
| [#537](https://github.com/Marvisak/VIctory/pull/537) | GPU: name the switch when a removal has no device-removed data | coderanonymus | files: `README.md` |
| [#542](https://github.com/Marvisak/VIctory/pull/542) | Shaders: keep buffer offsets below 2 GiB (NVIDIA + vkd3d-proton world device loss) | gingertonik | files: `crates/victory-shader/src/emit/lower.rs` |
| [#544](https://github.com/Marvisak/VIctory/pull/544) | HLE: report queue termination after running callbacks | Quat3rnion | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#561](https://github.com/Marvisak/VIctory/pull/561) | xmem: commit physical pages in pieces, and report the real count | JoshRob297 | files: `crates/victory-hle/src/modules/xmem.rs` |
| [#574](https://github.com/Marvisak/VIctory/pull/574) | HLE: write at-rest gamepad state for non-pad readings | Quat3rnion | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#575](https://github.com/Marvisak/VIctory/pull/575) | GPU: release resources the CPU is done with behind the queue | Len1k | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/shadow.rs` |
| [#578](https://github.com/Marvisak/VIctory/pull/578) | GPU: refuse wave64 mesh and compute programs on hosts without 64-lane waves | wbkepler | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/host.rs` |
| [#579](https://github.com/Marvisak/VIctory/pull/579) | GPU: VICTORY_SKIP_WAVE64 diagnostics switch for wave64 programs | wbkepler | files: `README.md`, `crates/victory-gpu/src/pipeline.rs` |
| [#586](https://github.com/Marvisak/VIctory/pull/586) | Shaders: honor the mesh allocation request counts | Kam471 | files: `README.md`, `apps/victory/src/translate.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs` |
| [#587](https://github.com/Marvisak/VIctory/pull/587) | Shaders: guard mesh output bounds, init all primitives, and omit sync on divergent s_barrier | FibbS6 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#595](https://github.com/Marvisak/VIctory/pull/595) | GPU: run submissions asynchronously on a host fence timeline | wbkepler | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/fence.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs` |
| [#596](https://github.com/Marvisak/VIctory/pull/596) | Shaders: lower v_cvt_pknorm_{i16,u16}_{f32,f16} with exact rounding | mercuryVM | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#599](https://github.com/Marvisak/VIctory/pull/599) | Shaders: lane-indexed ops on a wide host wave use the own console wave | NolanCotter | files: `crates/victory-shader/src/emit/lower.rs` |
| [#609](https://github.com/Marvisak/VIctory/pull/609) | GPU: retain and retire released host textures, staging, shadow buffers, and descriptor resources across submissions | LAKSHYA-cmd-tech | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs` |
| [#616](https://github.com/Marvisak/VIctory/pull/616) | GPU: rectangle draws check their bounds without 32-bit overflow | itzzArshad | files: `crates/victory-gpu/src/draw.rs` |
| [#628](https://github.com/Marvisak/VIctory/pull/628) | Shaders: lower ds_min_f32 / ds_max_f32 (and _rtn) with RDNA2's NaN rules | mercuryVM | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#633](https://github.com/Marvisak/VIctory/pull/633) | HLE: GetModuleFileNameA answers in the ANSI code page | JFIREonFIRE | files: `crates/victory-hle/src/modules/kernel.rs` |
| [#651](https://github.com/Marvisak/VIctory/pull/651) | GPU: select the readable format and plane for depth/stencil shader views | Raxstreams | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#656](https://github.com/Marvisak/VIctory/pull/656) | Input: report the character each held key types | lameloball2813-ui | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#659](https://github.com/Marvisak/VIctory/pull/659) | Shaders: refuse per-lane reads of mesh v5 in v5 writes and after joins | coderanonymus | files: `crates/victory-shader/src/ir.rs` |
| [#663](https://github.com/Marvisak/VIctory/pull/663) | media: apply the local-file rule to the source reader, sink writer and MFCreateFile | coderanonymus | files: `crates/victory-hle/src/modules/media.rs` |
| [#679](https://github.com/Marvisak/VIctory/pull/679) | run: refuse capture and dump paths inside the repo | binarycleric | files: `apps/victory/src/run.rs` |
| [#687](https://github.com/Marvisak/VIctory/pull/687) | hle: track title working-set memory, bound xasync threads, and map XUser devices | wbkepler | files: `crates/victory-hle/src/modules/xasync.rs`, `crates/victory-hle/src/modules/xmem.rs` |
| [#688](https://github.com/Marvisak/VIctory/pull/688) | GPU: take back the dynamic descriptor slots of lists that ran when a heap runs short | iurysf | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs` |
| [#690](https://github.com/Marvisak/VIctory/pull/690) | gpu: expand console primitive topologies into host list index buffers | wbkepler | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/primitive.rs` |
| [#693](https://github.com/Marvisak/VIctory/pull/693) | gpu: move shadow buffers to DEFAULT VRAM with pooled staging transfers | wbkepler | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/watch.rs` |
| [#695](https://github.com/Marvisak/VIctory/pull/695) | gpu: VICTORY_D3D12_WARP=0 opts out of the software adapter | arthercz | files: `README.md`, `crates/victory-formats/src/xma.rs`, `crates/victory-formats/src/xma/tables.rs`, `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/descriptor/host.rs` |
| [#697](https://github.com/Marvisak/VIctory/pull/697) | Shader: backward dead-code elimination in DXIL bitcode emission | wbkepler | files: `crates/victory-shader/src/emit/bitcode.rs` |
| [#707](https://github.com/Marvisak/VIctory/pull/707) | Shaders: lower tbuffer_store_format_* that need no conversion | mercuryVM | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#943](https://github.com/Marvisak/VIctory/pull/943) | GPU: use VirtualQuery region fallback in copy_mapped and write_mapped | MartinIndra02 | files: `crates/victory-gpu/src/host.rs` |
| [#946](https://github.com/Marvisak/VIctory/pull/946) | victory-shader: preserve helper-lane values on pixel waveReadLaneFirst | Sakura-Byte | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#952](https://github.com/Marvisak/VIctory/pull/952) | GPU: log the host's video-memory use and its budget | EgoraWyn | files: `crates/victory-gpu/src/host.rs` |
| [#956](https://github.com/Marvisak/VIctory/pull/956) | GPU: support multi-argument ExecuteIndirect signatures with root constants | MartinIndra02 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/pipeline/host.rs` |
| [#959](https://github.com/Marvisak/VIctory/pull/959) | victory: a menu when opened from Explorer, instead of help that closes at once | EduBertozzi | files: `Cargo.lock`, `apps/victory/src/main.rs` |
| [#960](https://github.com/Marvisak/VIctory/pull/960) | Game picker | killar4eto | files: `Cargo.lock`, `README.md`, `apps/victory/src/main.rs` |
| [#961](https://github.com/Marvisak/VIctory/pull/961) | Shaders, GPU: draw mesh pipelines without mesh shaders through a compute fallback (#3) | EduBertozzi | files: `apps/victory/src/main.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/host.rs` |
| [#967](https://github.com/Marvisak/VIctory/pull/967) | GPU: choose an adapter that can run the title, and name the ones that cannot | zzm1234560621-prog | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs` |
| [#969](https://github.com/Marvisak/VIctory/pull/969) | GPU: load the Agility SDK through ID3D12SDKConfiguration1 (#749) | mgunes1311-lab | files: `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/host.rs` |
| [#970](https://github.com/Marvisak/VIctory/pull/970) | GPU: aspect-aware concrete format resolution for typeless views (fixes #882, #876) | pushkarreddyy | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#982](https://github.com/Marvisak/VIctory/pull/982) | GPU: pool upload buffers across command list resets | chemokita13 | files: `crates/victory-gpu/src/host.rs` |
| [#984](https://github.com/Marvisak/VIctory/pull/984) | Shaders: split flat byte-offset accesses to structured buffers | CitizenCinema | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#988](https://github.com/Marvisak/VIctory/pull/988) | GPU: say when a fault lies past the end of its title memory copy | h0useadv | files: `crates/victory-gpu/src/shadow.rs` |
| [#999](https://github.com/Marvisak/VIctory/pull/999) | Shaders: search lane conditions once and redo a lowering once | TG0000 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/structure.rs` |
| [#1004](https://github.com/Marvisak/VIctory/pull/1004) | Shaders: lower image_get_lod on cube textures | tarcisioads | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1005](https://github.com/Marvisak/VIctory/pull/1005) | Fix 12 verified regressions in shader translation, runtime, caching and texture handling | THE-PRO-GAME | files: `apps/victory/src/translate.rs`, `crates/victory-formats/src/texture.rs`, `crates/victory-hle/src/modules/display.rs`, `crates/victory-hle/src/modules/xgamesave.rs`, `crates/victory-pipeline/src/cache.rs` |
| [#1012](https://github.com/Marvisak/VIctory/pull/1012) | Shaders: descriptors joined by nested control flow | ThiagoAlexsander | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1023](https://github.com/Marvisak/VIctory/pull/1023) | gpu: implement ordered 32-bit and 64-bit command-list memory waits | KLeek5 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/fence.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs` |
| [#1024](https://github.com/Marvisak/VIctory/pull/1024) | GPU: copy-back writes only the GPU's bytes and marks only unchanged pages current | Dufftwt | files: `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/watch.rs` |
| [#1032](https://github.com/Marvisak/VIctory/pull/1032) | GPU: cap oversized sampler heaps | divyeshganta | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1055](https://github.com/Marvisak/VIctory/pull/1055) | Shaders: scalar buffer loads from a UAV read it raw | adamdotpy | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1056](https://github.com/Marvisak/VIctory/pull/1056) | Shaders: scalar loads from a root view's address read its memory | adamdotpy | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1076](https://github.com/Marvisak/VIctory/pull/1076) | Fix NVIDIA Ada Lovelace (`RTX 4060`) D3D12 compatibility, 2s TDR submissions, and 16 GB host OOM | legayclightning22 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1083](https://github.com/Marvisak/VIctory/pull/1083) | Shaders: name what a scalar memory read is, and which descriptor dword it reads | adamdotpy | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1084](https://github.com/Marvisak/VIctory/pull/1084) | Shaders: a select or carry-in on an untracked mask tests this lane's bit | undeadhuman37 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1088](https://github.com/Marvisak/VIctory/pull/1088) | Fix compute shader signed overflow and paired LDS writes | THE-PRO-GAME | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1090](https://github.com/Marvisak/VIctory/pull/1090) | Shaders: lower constant 64-bit integer compares without INT64 | tarcisioads | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1095](https://github.com/Marvisak/VIctory/pull/1095) | Shaders: compute signed overflow SCC for s_add_i32, s_addk_i32, and s_sub_i32 | ESAT586 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1106](https://github.com/Marvisak/VIctory/pull/1106) | test(shader): report forced WARP runs as software only | divyeshganta | files: `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/emit/waterfall_tests.rs` |
| [#1112](https://github.com/Marvisak/VIctory/pull/1112) | Shaders: round normalized MTBUF loads without Int64ShaderOps | Razdva122 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1114](https://github.com/Marvisak/VIctory/pull/1114) | CLI: replay selected runtime shader hashes in offline translation | Razdva122 | files: `README.md`, `apps/victory/src/main.rs` |
| [#1124](https://github.com/Marvisak/VIctory/pull/1124) | Shadows: batch GPU copy-back writes safely | divyeshganta | files: `crates/victory-gpu/src/shadow.rs` |
| [#1126](https://github.com/Marvisak/VIctory/pull/1126) | GPU: release descriptor tables after a rejected bind | EatCodeSleep2 | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/pipeline.rs` |
| [#1129](https://github.com/Marvisak/VIctory/pull/1129) | GPU: give pipeline workers room for NVIDIA's shader compiler | divyeshganta | files: `crates/victory-gpu/src/pipeline/make.rs` |
| [#1133](https://github.com/Marvisak/VIctory/pull/1133) | Descriptors: clamp view indices past a capped host heap to a null slot | rivaldodev | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/host.rs` |
| [#1135](https://github.com/Marvisak/VIctory/pull/1135) | GPU: detile only texture subresources affected by writes | divyeshganta | files: `crates/victory-gpu/src/texture.rs` |
| [#1138](https://github.com/Marvisak/VIctory/pull/1138) | Shader tests: failures name the adapter that ran them | ayanbarosan | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/waterfall_tests.rs` |
| [#1143](https://github.com/Marvisak/VIctory/pull/1143) | GPU tests: verify a synthetic frame through PresentX | Doffi4 | files: `crates/victory-gpu/src/host.rs` |
| [#1144](https://github.com/Marvisak/VIctory/pull/1144) | Tests: show when shader differential checks are skipped | EatCodeSleep2 | files: `crates/victory-shader/src/emit/diff_tests.rs` |
| [#1145](https://github.com/Marvisak/VIctory/pull/1145) | Shaders: fix duplicate latch folding, unreachable phi edges, and replace_const caching in DXIL bitcode | hamdog0203 | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/shader.rs` |
| [#1156](https://github.com/Marvisak/VIctory/pull/1156) | Loader: continue past a title's int3 asserts, for finding the next blocker | adamdotpy | files: `crates/victory-loader/src/crash.rs` |
| [#1157](https://github.com/Marvisak/VIctory/pull/1157) | Input: the mouse as the stand-in pad's camera (VICTORY_MOUSE) | h0useadv | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#1178](https://github.com/Marvisak/VIctory/pull/1178) | Diagnostics: trace a DirectStorage request from submission to decoder outcome | Razdva122 | files: `crates/victory-hle/src/modules/dstorage.rs` |
| [#1190](https://github.com/Marvisak/VIctory/pull/1190) | Shaders: lower v_frexp_mant_{f32,f16} and v_frexp_exp_i{32_f32,16_f16} | ESAT586 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1203](https://github.com/Marvisak/VIctory/pull/1203) | GPU: expand synthetic unit tests for pipeline/make.rs (1 -> 9/12 tests) | geiyiliyabumo | files: `crates/victory-gpu/src/pipeline/make.rs` |
| [#1210](https://github.com/Marvisak/VIctory/pull/1210) | GPU: upload a host-copied texture again once the title writes its memory | powplusplus | files: `crates/victory-gpu/src/texture.rs` |
| [#1215](https://github.com/Marvisak/VIctory/pull/1215) | GPU: copy back with NtWriteVirtualMemory, no VirtualQuery before a copy into the title (copy back 1.5 s -> 0.13 s) | LooperSalty | files: `crates/victory-gpu/Cargo.toml`, `crates/victory-gpu/src/host.rs` |
| [#1227](https://github.com/Marvisak/VIctory/pull/1227) | Improve shader mask handling and GPU diagnostics | chiragmadhuprasad | files: `crates/victory-gpu/src/copystat.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/resource.rs` |
| [#1228](https://github.com/Marvisak/VIctory/pull/1228) | GPU: order shader writes on command list pipeline syncs (#732) | Ctrl-Alt-Haze | files: `crates/victory-gpu/src/list.rs` |
| [#1237](https://github.com/Marvisak/VIctory/pull/1237) | Shaders: implicit-level samples in compute take their gradients from the quad | felicienradio | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1243](https://github.com/Marvisak/VIctory/pull/1243) | HLE: the module tree gates for a host that is not Windows | MIchiel1234 | files: `crates/victory-hle/src/modules/xgame.rs`, `crates/victory-hle/src/modules/xgameui.rs` |
| [#1254](https://github.com/Marvisak/VIctory/pull/1254) | GPU diagnostics: a black frame's trace keeps the draws that end the frame | EduAzevedo | files: `README.md`, `crates/victory-gpu/src/draw.rs` |
| [#1261](https://github.com/Marvisak/VIctory/pull/1261) | Shaders: an SGPR no instruction writes stays refused above the initialized ones | Proudnoob4 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1267](https://github.com/Marvisak/VIctory/pull/1267) | GPU: keep only the bytes shaders may write, each once per submission | TG0000 | files: `crates/victory-gpu/src/shadow.rs` |
| [#1272](https://github.com/Marvisak/VIctory/pull/1272) | GPU: automatic texture mip-drop on E_OUTOFMEMORY and VICTORY_TEXTURE_MIP_DROP | ESAT586 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1275](https://github.com/Marvisak/VIctory/pull/1275) | Shaders: apply v_mov_b32 and v_cndmask_b32 abs/neg modifiers bitwise | Sakura-Byte | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1279](https://github.com/Marvisak/VIctory/pull/1279) | GPU: an argument clamp Wine's compiler builds too | Mumogg | files: `crates/victory-gpu/src/indirect.rs` |
| [#1285](https://github.com/Marvisak/VIctory/pull/1285) | Shaders: fix 16-bit VALU SDWA placement/sext and inline float constants | hamdog0203 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1289](https://github.com/Marvisak/VIctory/pull/1289) | Shader tests: v_pk_mul_lo_u16 keeps each half to 16 bits | bvtterbroot | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1295](https://github.com/Marvisak/VIctory/pull/1295) | Shaders: decode 16-bit integer inline float constants as f32 bits | WALID1618Y | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1298](https://github.com/Marvisak/VIctory/pull/1298) | GPU: replace stale descriptors on null CBV writes | EatCodeSleep2 | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/draw.rs` |
| [#1313](https://github.com/Marvisak/VIctory/pull/1313) | Shaders: return zero for unused image query extents | EatCodeSleep2 | files: `crates/victory-shader/src/emit/waterfall_tests.rs` |
| [#1314](https://github.com/Marvisak/VIctory/pull/1314) | Shaders: lower v_{fmaak,fmamk}_f16 and v_cvt_pk_{i16_i32,u16_u32} | ESAT586 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1331](https://github.com/Marvisak/VIctory/pull/1331) | GPU: rebind replaced descriptor heaps by host identity | EatCodeSleep2 | files: `crates/victory-gpu/src/draw.rs` |
| [#1336](https://github.com/Marvisak/VIctory/pull/1336) | Shaders: fix RPO resource tracking, SMEM alignment, raw VCC branch, and readlane/writelane semantics (#1249) | wbkepler | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/wave.rs`, `crates/victory-shader/src/structure.rs` |
| [#1338](https://github.com/Marvisak/VIctory/pull/1338) | Shaders: honor op_sel[3], clamp, and omod on v_interp_p2_f16 | AscilCH | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1339](https://github.com/Marvisak/VIctory/pull/1339) | Shaders: support clamp output modifier on v_cvt_pkrtz_f16_f32 | AscilCH | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1340](https://github.com/Marvisak/VIctory/pull/1340) | Shaders: mask M0[7:0] on v_movrel* and allow scalar/const src0 on v_movreld_b32 | AscilCH | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1341](https://github.com/Marvisak/VIctory/pull/1341) | Shaders: lower v_ldexp_f32 (VOP3 0x362) | AscilCH | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1342](https://github.com/Marvisak/VIctory/pull/1342) | Shaders: lower buffer_atomic_{sub,csub,inc,dec,fcmpswap,fmin,fmax} | AscilCH | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1349](https://github.com/Marvisak/VIctory/pull/1349) | GPU: reserve 2^18 dynamic slots on capped view heaps and trim fresh tables (#747) | wbkepler | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1355](https://github.com/Marvisak/VIctory/pull/1355) | HLE & Formats: replace miniz_oxide with SIMD-accelerated zlib-rs | wbkepler | files: `crates/victory-game/src/sgd5.rs`, `crates/victory-shader/src/native.rs` |
| [#1356](https://github.com/Marvisak/VIctory/pull/1356) | GPU: use RwLock for read-mostly tables and add per-HostList VA/view caches | wbkepler | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/pipeline.rs` |
| [#1357](https://github.com/Marvisak/VIctory/pull/1357) | HLE: native 4-motor Xbox impulse trigger haptics via Windows.Gaming.Input with XInput fallback | wbkepler | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#1363](https://github.com/Marvisak/VIctory/pull/1363) | [BUNDLE] XAsync, kernel, lifecycle and DirectStorage HLE: #114 #122 #247 #1098 #186 #373 #512 #451 #1080 #430 #577 #1238 | MamaLeVrai | files: `crates/victory-hle/src/modules/dstorage.rs`, `crates/victory-hle/src/modules/xasync.rs` |
| [#1372](https://github.com/Marvisak/VIctory/pull/1372) | Loader: lazily NOP-patch clwb/monitorx on #UD, emulate rdpid, batch IAT protection, and content-hash cached DLLs | wbkepler | files: `crates/victory-loader/src/crash.rs`, `crates/victory-loader/src/windows.rs` |
| [#1382](https://github.com/Marvisak/VIctory/pull/1382) | GPU: batch resource barriers, reuse draw scratch buffers, range-lock copy_simple, and pool list uploads | wbkepler | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1388](https://github.com/Marvisak/VIctory/pull/1388) | GPU: honor command-list 64-bit memory waits without blocking submissions (#700) | wbkepler | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs` |
| [#1393](https://github.com/Marvisak/VIctory/pull/1393) | Shaders: vectorize wide s_buffer_load and global_load rawBufferLoad calls | wbkepler | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1397](https://github.com/Marvisak/VIctory/pull/1397) | Shader: propagate float values across selects/phis and cache bools across dominators | wbkepler | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1398](https://github.com/Marvisak/VIctory/pull/1398) | Shaders: honor clamp on unsigned VOP3 add and subtract | EatCodeSleep2 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1399](https://github.com/Marvisak/VIctory/pull/1399) | Shader & GPU: support merged ES+GS geometry stages (vs_6_6 / gs_6_6) | wbkepler | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`, `crates/victory-shader/src/emit/rect.rs` |
| [#1403](https://github.com/Marvisak/VIctory/pull/1403) | CLI: report shader worker initialization failures | Luizbc2 | files: `apps/victory/src/translate.rs` |
| [#1405](https://github.com/Marvisak/VIctory/pull/1405) | GPU: a view's own copy that shaders feed reads its buffer's copy on the GPU (stacked on #334 and #1019) | SantannaCarlos | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/shadow.rs` |
| [#1407](https://github.com/Marvisak/VIctory/pull/1407) | Shaders: a lane-mask join of masks and numbers, read as a number | marquezinii | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1412](https://github.com/Marvisak/VIctory/pull/1412) | Shaders: keep scalar comparisons between lane masks uniform | EatCodeSleep2 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1416](https://github.com/Marvisak/VIctory/pull/1416) | Shaders: return zero for inactive compute swizzle sources | EatCodeSleep2 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1420](https://github.com/Marvisak/VIctory/pull/1420) | Shaders: a mask built up in a loop every lane runs the same way (stacked on #1407) | marquezinii | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1425](https://github.com/Marvisak/VIctory/pull/1425) | Shaders: a refusal names the instruction that made its missing value | ThomasSAMP | files: `apps/victory/src/translate.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1426](https://github.com/Marvisak/VIctory/pull/1426) | [BUNDLE] GPU host copies, descriptors, sampler heaps and footprints: 5 PRs, #322 #982 #409 #474 #1206 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/resource.rs` |
| [#1439](https://github.com/Marvisak/VIctory/pull/1439) | [BUNDLE] GPU pipeline library, shader cache, draw state and frame wait: 5 PRs, #1000 #626 #642 #174 #1279 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/list.rs` |
| [#1441](https://github.com/Marvisak/VIctory/pull/1441) | Shaders: preserve the unwritten high half of packed D16 buffer loads | EatCodeSleep2 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1448](https://github.com/Marvisak/VIctory/pull/1448) | GPU: invalidate root bindings when a root signature changes | Luizbc2 | files: `crates/victory-gpu/src/list.rs` |
| [#1463](https://github.com/Marvisak/VIctory/pull/1463) | GPU: cap command lists per submission (VICTORY_SUBMIT_MAX_RUNS) | Bebrik229 | files: `crates/victory-gpu/src/host.rs` |
| [#1466](https://github.com/Marvisak/VIctory/pull/1466) | GPU: avoid faulting when zero-filling protected title memory | fluffyflattershy-afk | files: `crates/victory-gpu/src/host.rs` |
| [#1469](https://github.com/Marvisak/VIctory/pull/1469) | Shaders: lower binary64 class comparisons | Luizbc2 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1472](https://github.com/Marvisak/VIctory/pull/1472) | GPU: flush only overlapping shadow refreshes before Step::GpuWrite | Sakura-Byte | files: `crates/victory-gpu/src/host.rs` |
| [#1483](https://github.com/Marvisak/VIctory/pull/1483) | Pick the discrete GPU on laptops; fix driver-dependent and wrong shader lowering | spy0eye-beep | files: `crates/victory-gpu/src/host.rs`, `crates/victory-hle/src/modules/xasync.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/sampler.rs` |
| [#1486](https://github.com/Marvisak/VIctory/pull/1486) | Shaders: track source lane in whole-wave Sym::Own to prevent miscompiled shuffles | AscilCH | files: `crates/victory-shader/src/emit/wave.rs` |
| [#1487](https://github.com/Marvisak/VIctory/pull/1487) | Shader tests: prefer high-performance hardware adapter in emit::host::Host::new | AscilCH | files: `crates/victory-shader/src/emit/host.rs` |
| [#1488](https://github.com/Marvisak/VIctory/pull/1488) | Shaders: lower ds_add{_rtn}_f32 and ds_cmpst{_rtn}_f32 LDS atomics | AscilCH | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1489](https://github.com/Marvisak/VIctory/pull/1489) | Shaders: lower image_gather4_c_lz and image_gather4_c_lz_o (MIMG 0x4f, 0x5f) | AscilCH | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1492](https://github.com/Marvisak/VIctory/pull/1492) | [BUNDLE] Shader instruction lowering: 10 PRs, #156 #162 #169 #368 #379 #990 #1021 #1048 #1052 #1053 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1514](https://github.com/Marvisak/VIctory/pull/1514) | Add opt-in GPU memory synchronization tracing | draggygaggy-maker | files: `README.md`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs` |
| [#1516](https://github.com/Marvisak/VIctory/pull/1516) | Shaders: zero missing typed-buffer components | venglov | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1519](https://github.com/Marvisak/VIctory/pull/1519) | Shaders: unpack 16-bit vertex inputs into the low half | Bloh09 | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#1541](https://github.com/Marvisak/VIctory/pull/1541) | CLI: list-diff compares two translate listings program by program | sinan-cmyk | files: `README.md`, `apps/victory/src/main.rs` |
| [#1542](https://github.com/Marvisak/VIctory/pull/1542) | [BUNDLE] GPU fixes 4: 3 PRs, #1082 #1173 #1265 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/list.rs` |
| [#1554](https://github.com/Marvisak/VIctory/pull/1554) | Shaders: the legacy MAD/MAC encodings are one fused multiply-add with flushed sources | Calvix2k | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/gfx10/opcodes.rs` |
| [#1560](https://github.com/Marvisak/VIctory/pull/1560) | PE: refuse an import address table inside the headers | default-cybe | files: `crates/victory-pe/src/image.rs` |
| [#1568](https://github.com/Marvisak/VIctory/pull/1568) | Shaders: model 64-bit carry sums and f16 reductions in whole-wave sections | MartinIndra02 | files: `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/emit/wave.rs` |
| [#1570](https://github.com/Marvisak/VIctory/pull/1570) | Shaders: govern pixel discard by last exp VM (Valid Mask) and guard pixel MRT exports | ESAT586 | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#1575](https://github.com/Marvisak/VIctory/pull/1575) | Shaders: sweep typed buffer formats and f16 ALU against exact references | DovisLe | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1577](https://github.com/Marvisak/VIctory/pull/1577) | Shaders: expand 64-bit inline constants as signed ints and binary64 floats | mgunes1311-lab | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1578](https://github.com/Marvisak/VIctory/pull/1578) | GPU: the "shader does not translate" warning names where its value was made | ThomasSAMP | files: `apps/victory/src/translate.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1587](https://github.com/Marvisak/VIctory/pull/1587) | Shaders: ballot divergent-loop masks at reconverged reads (#1498) | Ctrl-Alt-Haze | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1588](https://github.com/Marvisak/VIctory/pull/1588) | Shaders: single-round v_fma_mixlo_f16 and v_fma_mixhi_f16 | Ctrl-Alt-Haze | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1590](https://github.com/Marvisak/VIctory/pull/1590) | XMA tests: count frames only in the selected stream | zhaibingye | files: `crates/victory-formats/src/xma.rs` |
| [#1598](https://github.com/Marvisak/VIctory/pull/1598) | Shaders: lower v_mad_f16 and v_mac_f16 with unfused binary16 product rounding | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1602](https://github.com/Marvisak/VIctory/pull/1602) | Shader tests: f32/int conversions saturate, take NaN as 0, round to even | vladbondarenko97 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1606](https://github.com/Marvisak/VIctory/pull/1606) | Shaders: lower remaining 32-bit integer and bitwise LDS atomics | HumanlyDev | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1608](https://github.com/Marvisak/VIctory/pull/1608) | Shaders: single-round v_fma_mixlo_f16 and v_fma_mixhi_f16 to binary16 | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1609](https://github.com/Marvisak/VIctory/pull/1609) | victory doctor: name the known problems a run shows, in plain words (stacked on #959) | EduBertozzi | files: `Cargo.lock`, `apps/victory/src/main.rs` |
| [#1613](https://github.com/Marvisak/VIctory/pull/1613) | GPU: render targets keep their slots (null views for targets the host cannot bind), and no RTV or clear without the render-target use | AgneyaK | files: `crates/victory-gpu/src/list.rs` |
| [#1618](https://github.com/Marvisak/VIctory/pull/1618) | victory menu: speak Portuguese where Windows does (stacked on #1609) | EduBertozzi | files: `Cargo.lock`, `apps/victory/src/main.rs` |
| [#1619](https://github.com/Marvisak/VIctory/pull/1619) | Shader tests: pin IR reachability and PHI invariants | ArnabSaga | files: `crates/victory-shader/src/ir.rs` |
| [#1625](https://github.com/Marvisak/VIctory/pull/1625) | CLI: compare runtime shader failures with offline coverage | srijann07 | files: `apps/victory/src/main.rs` |
| [#1642](https://github.com/Marvisak/VIctory/pull/1642) | Shaders: preserve signaling NaNs in typed buffer loads | zhaibingye | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1646](https://github.com/Marvisak/VIctory/pull/1646) | Shaders: fold constant bin/cmp/select/cast ops and identity ops at emit time | adamdotpy | files: `crates/victory-shader/src/emit/bitcode.rs` |
| [#1648](https://github.com/Marvisak/VIctory/pull/1648) | GPU: mesh shaders emulated as compute + unpack vertex on SM 6.6 cards without a mesh tier | yoraudev | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/host.rs` |
| [#1649](https://github.com/Marvisak/VIctory/pull/1649) | shader: lower s_cmov_b32, s_cmov_b64, and s_cmovk_i32 | geiyiliyabumo | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1659](https://github.com/Marvisak/VIctory/pull/1659) | shader: lower v_frexp_{exp,mant}_{f32,f16} in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1661](https://github.com/Marvisak/VIctory/pull/1661) | GPU: route non-overlapping CopyMemoryToMemoryX through Step::Copy and scope invalidation to written ranges | anlnimus | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1662](https://github.com/Marvisak/VIctory/pull/1662) | Shaders: lower RDNA 2 quad-byte SAD instructions to DXIL | THE-PRO-GAME | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1663](https://github.com/Marvisak/VIctory/pull/1663) | Shaders: lower RDNA 2 ADDTID memory instructions to DXIL | THE-PRO-GAME | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1666](https://github.com/Marvisak/VIctory/pull/1666) | GPU: small first scratch chunk per list; log host memory against budget | cyudev | files: `crates/victory-gpu/src/host.rs` |
| [#1668](https://github.com/Marvisak/VIctory/pull/1668) | Shaders: read inline floats as f32 bits in 16-bit integer ops | Calvix2k | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1669](https://github.com/Marvisak/VIctory/pull/1669) | shader: handle dword-straddling 16-bit typed buffer loads at byte offset 3 | geiyiliyabumo | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1673](https://github.com/Marvisak/VIctory/pull/1673) | HLE: XTaskQueueTerminate cancels only its own tasks on shared ports | Calvix2k | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#1685](https://github.com/Marvisak/VIctory/pull/1685) | Shaders: lower v_cmp_{f,t}_{i64,u64} constant 64-bit compares | Calvix2k | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1686](https://github.com/Marvisak/VIctory/pull/1686) | Shaders: lower pixel shader SV_Coverage input via dx.op.coverage | Calvix2k | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1687](https://github.com/Marvisak/VIctory/pull/1687) | Shaders: lower image_gather4_c_lz(_o) and offset sample variants | Calvix2k | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1688](https://github.com/Marvisak/VIctory/pull/1688) | Shaders: lower v_mad_u32_u16, v_mad_i32_i16, and v_lerp_u8 | Calvix2k | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1691](https://github.com/Marvisak/VIctory/pull/1691) | GPU: track D3D12 shadow-buffer states (#1670) | Elensito | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/shadow.rs` |
| [#1692](https://github.com/Marvisak/VIctory/pull/1692) | [BUNDLE] GPU diagnostics: 3 PRs, #669 #1251 #602 (rebuilt on main 70564ae) | MamaLeVrai | files: `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/queue.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1702](https://github.com/Marvisak/VIctory/pull/1702) | HLE: add VICTORY_NO_HOST_PAD to hide host gamepads | Calvix2k | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#1710](https://github.com/Marvisak/VIctory/pull/1710) | GPU: keep dropped draws in the full frame reporting interval | zhaibingye | files: `crates/victory-gpu/src/host.rs` |
| [#1723](https://github.com/Marvisak/VIctory/pull/1723) | GPU diagnostics: pipeline statistics per noted command with VICTORY_GPU_TIMING | LarryBebou | files: `README.md` |
| [#1727](https://github.com/Marvisak/VIctory/pull/1727) | GPU: 1D textures are 2D on the host, one texel high (GBV id=940) | Bullet18x | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1735](https://github.com/Marvisak/VIctory/pull/1735) | GPU: time commands by pipeline in VICTORY_GPU_TIMING | Nixitov | files: `README.md`, `apps/victory/src/translate.rs`, `crates/victory-gpu/src/host.rs` |
| [#1737](https://github.com/Marvisak/VIctory/pull/1737) | Shaders: honor permlane EXEC and FI/BC flags (on #1014) | jaschinski97-ops | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1739](https://github.com/Marvisak/VIctory/pull/1739) | GPU: clear final mesh pipeline-stream padding after typed moves | jaschinski97-ops | files: `crates/victory-gpu/src/pipeline/host.rs` |
| [#1747](https://github.com/Marvisak/VIctory/pull/1747) | Shaders: lower v_div_scale_f32 and v_div_fmas_f32 | ESAT586 | files: `crates/victory-shader/src/emit/valu_tests.rs`, `crates/victory-shader/src/structure.rs` |
| [#1750](https://github.com/Marvisak/VIctory/pull/1750) | GPU: a wait for a submission ends when the device is lost or the GPU stalls | x3ero0 | files: `crates/victory-gpu/src/host.rs` |
| [#1756](https://github.com/Marvisak/VIctory/pull/1756) | Shaders: image atomics on a handle of their own element type | paulomatias97-create | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1757](https://github.com/Marvisak/VIctory/pull/1757) | Shaders: one arena per program for instruction operands and effects | Luislariosss | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/ir.rs`, `crates/victory-shader/src/structure.rs` |
| [#1761](https://github.com/Marvisak/VIctory/pull/1761) | Input: trigger rumble through Windows.Gaming.Input with one pad conne… | bemalinho | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#1769](https://github.com/Marvisak/VIctory/pull/1769) | Shaders: LDS accesses outside the program's allocation read 0 and drop their writes | Impre-visible | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1774](https://github.com/Marvisak/VIctory/pull/1774) | victory: meshdump surveys mesh and compute programs for group shape, LDS and divergent barriers | ryosen0 | files: `README.md`, `apps/victory/src/main.rs` |
| [#1779](https://github.com/Marvisak/VIctory/pull/1779) | GPU: view heaps on hosts capped below 2^21 descriptors | wbkepler | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1780](https://github.com/Marvisak/VIctory/pull/1780) | GPU: check every unordered texture view against the host's typed-store support (#1754) | LarryBebou | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1786](https://github.com/Marvisak/VIctory/pull/1786) | Input: support DualShock 4 over HID and preserve keyboard controls | delacor | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#1791](https://github.com/Marvisak/VIctory/pull/1791) | Shader tests: keep the FSPX dot4 test off folded constants | Calvix2k | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1795](https://github.com/Marvisak/VIctory/pull/1795) | Shaders: LDS halfwords straddling two dwords, and hardware tests of byte and halfword LDS accesses | dragoso | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1798](https://github.com/Marvisak/VIctory/pull/1798) | run: boot a separated exe/dump layout from the dump | Calvix2k | files: `crates/victory-loader/tests/load_probe.rs` |
| [#1799](https://github.com/Marvisak/VIctory/pull/1799) | fix(shader,gpu): eliminate 22s s_barrier world TDRs, zero invalid indirect mesh args, and reach Vice City opening credits & world frames | legayclightning22 | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#1800](https://github.com/Marvisak/VIctory/pull/1800) | GPU: log title slots past a capped heap once per 64 Ki, not each | AgneyaK | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1837](https://github.com/Marvisak/VIctory/pull/1837) | Display: the title's screenshots save the last presented frame | kais7654 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs` |
| [#1838](https://github.com/Marvisak/VIctory/pull/1838) | XGameSave: an old version another process holds open no longer fails the save | adamMasMusic | files: `crates/victory-hle/src/modules/xgamesave.rs` |
| [#1841](https://github.com/Marvisak/VIctory/pull/1841) | Shaders: honor FP32 rounding when packing a byte | AlanQiang0418 | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1843](https://github.com/Marvisak/VIctory/pull/1843) | GPU: unordered views only in formats the host stores to (NVIDIA device removal on B5G5R5A1) | KevinPratap | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1845](https://github.com/Marvisak/VIctory/pull/1845) | NVIDIA D3D12 fixes & shader translation improvements (dynamic descriptors, Wave32 compute, untracked masks) | mrsqarvc-byte | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1847](https://github.com/Marvisak/VIctory/pull/1847) | Shaders: reconstruct image descriptor dword 0 as a heap-slot proxy | AdamRchd | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1852](https://github.com/Marvisak/VIctory/pull/1852) | GPU: publish descriptor address snapshots before releasing writer lock | VlREX | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#1853](https://github.com/Marvisak/VIctory/pull/1853) | Shaders: extend image_gather4_l(_o) to all address modes, borders, a16, d16, unorm, and 2D arrays | ESAT586 | files: `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#1855](https://github.com/Marvisak/VIctory/pull/1855) | victory-gpu: clamp constant buffer views to their registered buffer | mgunes1311-lab | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs` |
| [#1858](https://github.com/Marvisak/VIctory/pull/1858) | Shader tests: the permute test skips a device with shorter waves | kais7654 | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#1861](https://github.com/Marvisak/VIctory/pull/1861) | fix | Yeetbot159 | files: `README.md`, `apps/victory/src/main.rs`, `apps/victory/src/run.rs`, `apps/victory/src/shader.rs`, `apps/victory/src/translate.rs` |
| [#1864](https://github.com/Marvisak/VIctory/pull/1864) | Shaders: global byte and half stores keep the rest of their dword | TinkerBell-90 | files: `crates/victory-shader/src/emit/memory_tests.rs` |
| [#1867](https://github.com/Marvisak/VIctory/pull/1867) | GPU: merge shadow write-back bytes in AVX2 vectors with scalar fallback | VlREX | files: `crates/victory-gpu/src/shadow.rs` |
| [#1869](https://github.com/Marvisak/VIctory/pull/1869) | Perf/indexed copyback ranges | VlREX | files: `crates/victory-gpu/src/memory.rs` |
| [#1883](https://github.com/Marvisak/VIctory/pull/1883) | Shaders: lane masks a traversal keeps as numbers | powplusplus | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1885](https://github.com/Marvisak/VIctory/pull/1885) | Shaders, GPU: one back edge per loop header, and a large stack for pipeline threads | powplusplus | files: `crates/victory-shader/src/emit/bitcode.rs` |
| [#1889](https://github.com/Marvisak/VIctory/pull/1889) | Shader tests: VICTORY_ADAPTER picks the GPU the hardware checks run on | alexdeliu | files: `crates/victory-shader/src/emit/host.rs` |
| [#1890](https://github.com/Marvisak/VIctory/pull/1890) | Shaders: console wave64 compute on 32-lane hosts (split waves) | beamdotdev | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#1897](https://github.com/Marvisak/VIctory/pull/1897) | end the stack walk where rtlvirtualunwind faults | imjustprism | files: `crates/victory-loader/src/crash.rs` |
| [#1899](https://github.com/Marvisak/VIctory/pull/1899) | Shaders: lower 64-bit texture atomics to DXIL i64 atomics | TansuoTro | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs`, `crates/victory-shader/src/emit/shader.rs` |
| [#1915](https://github.com/Marvisak/VIctory/pull/1915) | Shaders: lower 32-bit and 64-bit integer global atomics (cmpswap, csub, inc, dec, _x2) | ESAT586 | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/memory_tests.rs` |
| [#1923](https://github.com/Marvisak/VIctory/pull/1923) | GPU: run submissions asynchronously on a host fence timeline (rebase of #595) | slatefield | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/fence.rs`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/indirect.rs` |
| [#1924](https://github.com/Marvisak/VIctory/pull/1924) | Shader &amp; GPU: merged geometry stages (rebase of #1399, with the batched GSVS write fix) | slatefield | files: `crates/victory-shader/src/emit/bvh_tests.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/memory_tests.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1926](https://github.com/Marvisak/VIctory/pull/1926) | GPU: boot on NVIDIA when a format cannot be a typed UAV | QuentinDanblon | files: `README.md`, `crates/victory-gpu/src/descriptor/host.rs` |
| [#1934](https://github.com/Marvisak/VIctory/pull/1934) | GPU: resolve initial texture uploads and host_written at submission (#1891) | zondy1i | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs`, `crates/victory-gpu/src/texture.rs` |
| [#1953](https://github.com/Marvisak/VIctory/pull/1953) | Shaders: heap handles are reused only for the same resource properties | RaghavVijayanand | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1954](https://github.com/Marvisak/VIctory/pull/1954) | GPU: texture to buffer copies (read back) | RaghavVijayanand | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-gpu/src/resource.rs` |
| [#1955](https://github.com/Marvisak/VIctory/pull/1955) | Shaders: image stores of some channels, to mip 0, and to integer views | RaghavVijayanand | files: `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#1956](https://github.com/Marvisak/VIctory/pull/1956) | Shaders: cube face and multisampled image loads | RaghavVijayanand | files: `crates/victory-shader/src/emit/host.rs` |
| [#1957](https://github.com/Marvisak/VIctory/pull/1957) | GPU: blocking fence waits, feature queries, device methods, private interfaces | RaghavVijayanand | files: `crates/victory-gpu/src/fence.rs` |
| [#1959](https://github.com/Marvisak/VIctory/pull/1959) | Shaders: LDS sub-dword writes, typed buffers at offsets and of some channels, typed loads by index | RaghavVijayanand | files: `crates/victory-shader/src/emit/lower.rs` |
| [#1960](https://github.com/Marvisak/VIctory/pull/1960) | Shaders: wave64 compute programs on hosts of 32-lane waves | RaghavVijayanand | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#1962](https://github.com/Marvisak/VIctory/pull/1962) | GPU: make placed-texture heap slots that shaders actually read | antocorvo3000 | files: `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#1969](https://github.com/Marvisak/VIctory/pull/1969) | GPU: a title texture's host texture is made on its first use (the first-use half of #431) | AgneyaK | files: `crates/victory-gpu/src/resource.rs` |
| [#1971](https://github.com/Marvisak/VIctory/pull/1971) | GPU and shaders: publish bounded descriptor size metadata | thatirishguyyy | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/memory_tests.rs` |
| [#1972](https://github.com/Marvisak/VIctory/pull/1972) | Diagnostics: find, reproduce and skip pipelines the host's compiler c… | J-DB0 | files: `README.md`, `crates/victory-gpu/src/pipeline.rs` |
| [#2003](https://github.com/Marvisak/VIctory/pull/2003) | Shaders: MUBUF sub-dword `_d16` and `_d16_hi` loads | iurysf | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2015](https://github.com/Marvisak/VIctory/pull/2015) | Shader tests: check 125 more instructions on the hardware | astrosteveo | files: `crates/victory-shader/src/emit/semantics_tests.rs` |
| [#2017](https://github.com/Marvisak/VIctory/pull/2017) | GPU: pool HostList upload buffers across resets | lizapropanol | files: `crates/victory-gpu/src/host.rs` |
| [#2030](https://github.com/Marvisak/VIctory/pull/2030) | Shaders: round D16 image reads according to the bound texture format | AlanQiang0418 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`, `crates/victory-shader/src/emit/stride_tests.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#2035](https://github.com/Marvisak/VIctory/pull/2035) | Shaders: drop group sync for race-free divergent single-wave barriers on narrow-wave hosts | rivaldodev | files: `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#2042](https://github.com/Marvisak/VIctory/pull/2042) | GPU: no blending on integer render targets in host pipelines | Deilach | files: `crates/victory-gpu/src/pipeline/host.rs` |
| [#2064](https://github.com/Marvisak/VIctory/pull/2064) | Shaders: d16 buffer loads of floats truncate on every host | astrosteveo | files: `crates/victory-shader/src/emit/lower.rs` |
| [#2093](https://github.com/Marvisak/VIctory/pull/2093) | GPU: our compute shaders compiled by the build on Windows | Deilach | files: `crates/victory-gpu/src/indirect.rs`, `crates/victory-gpu/src/twin.rs` |
| [#2100](https://github.com/Marvisak/VIctory/pull/2100) | Shaders: lower v_cvt_pknorm_{i16,u16}_{f32,f16} in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs` |
| [#2113](https://github.com/Marvisak/VIctory/pull/2113) | Shaders: lower ds_inc_u32, ds_inc_rtn_u32, ds_dec_u32, and ds_dec_rtn_u32 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/semantics_tests.rs` |
| [#2116](https://github.com/Marvisak/VIctory/pull/2116) | Shaders: lower ds_rsub_u32 and ds_rsub_rtn_u32 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/semantics_tests.rs` |
| [#2119](https://github.com/Marvisak/VIctory/pull/2119) | Shaders: lower ds_wrxchg2_rtn_b32 and ds_wrxchg2st64_rtn_b32 in pure 32-bit DXIL | geiyiliyabumo | files: `crates/victory-shader/src/emit/semantics_tests.rs` |
| [#2125](https://github.com/Marvisak/VIctory/pull/2125) | Shaders: load D16 integer textures with their bound component type | AlanQiang0418 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/shader.rs`, `crates/victory-shader/src/emit/stride_tests.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#2136](https://github.com/Marvisak/VIctory/pull/2136) | GPU: a host copy nothing wrote is not asked for at submission | r4tedx | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shadow.rs`, `crates/victory-gpu/src/watch.rs` |
| [#2175](https://github.com/Marvisak/VIctory/pull/2175) | GPU: title memory page bitmaps live in video memory | wbkepler | files: `crates/victory-gpu/src/memory.rs` |
| [#2185](https://github.com/Marvisak/VIctory/pull/2185) | fix: clamp shader heap indices to the host's view-heap cap (NVIDIA) | thedanmaor | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2189](https://github.com/Marvisak/VIctory/pull/2189) | GPU: Graceful degradation and dynamic recycling for descriptor heaps exceeding 1,000,000 slots | Xvania7 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs` |
| [#2190](https://github.com/Marvisak/VIctory/pull/2190) | GPU: Map typeless texture views to concrete formats (fixes #850) | Xvania7 | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2192](https://github.com/Marvisak/VIctory/pull/2192) | GPU: schedule shader translation and pipeline creation as a dependency DAG (#1509) | Xvania7 | files: `crates/victory-gpu/src/pipeline/host.rs`, `crates/victory-gpu/src/pipeline/make.rs` |
| [#2194](https://github.com/Marvisak/VIctory/pull/2194) | GPU: Pre-check wave lane constraints for compute pipelines (fixes #817) | Xvania7 | files: `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/host.rs` |
| [#2202](https://github.com/Marvisak/VIctory/pull/2202) | shader: lower remaining packed dot products and clamped integer forms | UnkwnDev | files: `crates/victory-shader/src/emit/bitcode.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2242](https://github.com/Marvisak/VIctory/pull/2242) | \ GPU: copy-backs put back only the bytes the GPU changed\ | wbkepler | files: `crates/victory-gpu/src/shadow.rs` |
| [#2259](https://github.com/Marvisak/VIctory/pull/2259) | Keep the local launcher offline and policy compliant | namitahlawat | files: `crates/victory-formats/src/xma/tables.rs`, `crates/victory-gpu/src/capture.rs`, `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs` |
| [#2260](https://github.com/Marvisak/VIctory/pull/2260) | GPU: queries answer from the host GPU | FoxxoOwO | files: `README.md`, `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/list.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#2277](https://github.com/Marvisak/VIctory/pull/2277) | HLE xmem: support MEM_COMMIT inside 64 KiB placeholder reservations | Sidlik900 | files: `crates/victory-hle/src/modules/xmem.rs` |
| [#2280](https://github.com/Marvisak/VIctory/pull/2280) | GPU: copy-backs compare a block at a time (stacked on #2242) | wbkepler | files: `crates/victory-gpu/src/shadow.rs` |
| [#2311](https://github.com/Marvisak/VIctory/pull/2311) | GPU: programs that walk the BVH wait until the builder has run whole (NVIDIA device hang at world entry) | Bullet18x | files: `crates/victory-gpu/src/pipeline.rs` |
| [#2312](https://github.com/Marvisak/VIctory/pull/2312) | GPU, Shaders: spread compute dispatches past 65,535 groups in x across z (fixes #2256) | Xvania7 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#2316](https://github.com/Marvisak/VIctory/pull/2316) | GPU: VICTORY_FRAMETIME_DUMP writes the frame summary to a CSV | ruvenesh | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/lib.rs` |
| [#2335](https://github.com/Marvisak/VIctory/pull/2335) | docs: mention VICTORY_COPY_MODE in README Debugging table | romeawayfromhome-rgb | files: `README.md` |
| [#2337](https://github.com/Marvisak/VIctory/pull/2337) | Input: add Windows DualSense / DualSense Edge support | Asem912 | files: `apps/victory/src/main.rs`, `crates/victory-hle/src/modules/gameinput/mod.rs` |
| [#2342](https://github.com/Marvisak/VIctory/pull/2342) | Shaders: descriptors chosen by uniform trees of joins and selects | RomainKH | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#2345](https://github.com/Marvisak/VIctory/pull/2345) | GPU: every region of a tracked range must be the runtime's | crashbashash | files: `crates/victory-gpu/src/watch.rs` |
| [#2348](https://github.com/Marvisak/VIctory/pull/2348) | Shaders: lower v_cvt_f32_f64 | Calvix2k | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2354](https://github.com/Marvisak/VIctory/pull/2354) | GPU: queries run on the host GPU | FoxxoOwO | files: `README.md`, `crates/victory-gpu/src/host.rs` |
| [#2363](https://github.com/Marvisak/VIctory/pull/2363) | GPU: descriptor dwords read as data — the record count and the format | Calvix2k | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2367](https://github.com/Marvisak/VIctory/pull/2367) | GPU: select host DXGI adapter via VICTORY_ADAPTER and log GPU | PanS4ge | files: `README.md`, `crates/victory-gpu/src/host.rs` |
| [#2373](https://github.com/Marvisak/VIctory/pull/2373) | Run pixel shader wave operations over helper lanes, as the console does | Vyto-Line | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/shader_cache.rs`, `crates/victory-shader/src/emit/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#2382](https://github.com/Marvisak/VIctory/pull/2382) | Shaders: follow EXEC set from a scalar the section made constant | Calvix2k | files: `crates/victory-shader/src/emit/wave.rs` |
| [#2383](https://github.com/Marvisak/VIctory/pull/2383) | GPU: opt-in Agility SDK runtime for victory.exe | makmatvey | files: `apps/victory/src/main.rs` |
| [#2390](https://github.com/Marvisak/VIctory/pull/2390) | victory-shader: read pixel quad helper lanes without discard | bartikele | files: `crates/victory-shader/src/emit/lower.rs` |
| [#2394](https://github.com/Marvisak/VIctory/pull/2394) | victory-gpu: skip repeated dynamic descriptor slot searches after failure | bartikele | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2399](https://github.com/Marvisak/VIctory/pull/2399) | Shaders: hash the translator's hot maps with the multiply-rotate hasher | borosf | files: `crates/victory-shader/src/emit/lower.rs`, `crates/victory-shader/src/emit/mod.rs` |
| [#2401](https://github.com/Marvisak/VIctory/pull/2401) | GPU: under Wine, a host driver compiler crash costs its pipeline, not the run | Mumogg | files: `crates/victory-gpu/src/pipeline.rs`, `crates/victory-gpu/src/pipeline/library.rs`, `crates/victory-gpu/src/pipeline/make.rs` |
| [#2409](https://github.com/Marvisak/VIctory/pull/2409) | GPU: marked-page copy-backs skip work that changes nothing (stacked on #2280) | wbkepler | files: `crates/victory-gpu/src/shadow.rs` |
| [#2424](https://github.com/Marvisak/VIctory/pull/2424) | `apps/victory`: use dedicated Win32 `HeapCreate` global allocator and add `VICTORY_NO_WATCH_GUARDS` toggle | faycalbaklouti | files: `apps/victory/src/main.rs`, `crates/victory-gpu/src/watch.rs` |
| [#2435](https://github.com/Marvisak/VIctory/pull/2435) | GPU: give screen passes dedicated pipeline workers and wait budget (fixes #2433) | pushkarreddyy | files: `crates/victory-gpu/src/pipeline/make.rs` |
| [#2439](https://github.com/Marvisak/VIctory/pull/2439) | GPU: zero blend and depth-stencil padding the pipeline library compares | makmatvey | files: `crates/victory-gpu/src/pipeline/host.rs` |
| [#2441](https://github.com/Marvisak/VIctory/pull/2441) | GPU: live 1440p present fallback when 4K primaries stay unwritten (fixes #841) | Xvania7 | files: `crates/victory-gpu/src/queue.rs` |
| [#2451](https://github.com/Marvisak/VIctory/pull/2451) | GPU: cap oversized sampler heaps at 2,048 with dynamic slots | makmatvey | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2456](https://github.com/Marvisak/VIctory/pull/2456) | Shaders: name the adapter on translate --pipelines verdicts (FIND-3) | makmatvey | files: `crates/victory-gpu/src/host.rs`, `crates/victory-shader/src/emit/host.rs` |
| [#2475](https://github.com/Marvisak/VIctory/pull/2475) | GPU: reserve 2^18 dynamic slots on capped view heaps and trim fresh tables | kais7654 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs` |
| [#2490](https://github.com/Marvisak/VIctory/pull/2490) | Shaders: lower root UAV accesses as ROVs in POPS pixel shaders | reeledMarek | files: `crates/victory-shader/src/emit/lower.rs` |
| [#2515](https://github.com/Marvisak/VIctory/pull/2515) | Shaders: VOP3 f16 interpolation attr63.w is not a 32-bit literal | mgunes1311-lab | files: `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#2522](https://github.com/Marvisak/VIctory/pull/2522) | HLE: retain pending_with state across cancellation and prevent stale block completions | reeledMarek | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#2536](https://github.com/Marvisak/VIctory/pull/2536) | shader: expand constant dot4 multiplicands to avoid Arc IGC miscompilation | UnkwnDev | files: `crates/victory-shader/src/emit/bitcode.rs` |
| [#2539](https://github.com/Marvisak/VIctory/pull/2539) | Shaders: a select or carry-in on an untracked mask tests this lane's bit | kais7654 | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2542](https://github.com/Marvisak/VIctory/pull/2542) | GPU: use non-zero NumElements for null raw pairs in HostHeap::raw_pair_at | reeledMarek | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2543](https://github.com/Marvisak/VIctory/pull/2543) | GPU: keep view_addresses upload buffer alive on command lists and size it to HEAP_VIEWS | reeledMarek | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2545](https://github.com/Marvisak/VIctory/pull/2545) | GPU: avoid illegal COPY_SOURCE self-transition in Host::present | reeledMarek | files: `crates/victory-gpu/src/host.rs`, `crates/victory-gpu/src/queue.rs` |
| [#2558](https://github.com/Marvisak/VIctory/pull/2558) | Shaders: heap indices from data clamped before the root views they index | RomainKH | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-shader/src/emit/lower.rs` |
| [#2561](https://github.com/Marvisak/VIctory/pull/2561) | GPU: a page whose other mapping cannot be guarded stays changed | Calvix2k | files: `crates/victory-gpu/src/watch.rs` |
| [#2566](https://github.com/Marvisak/VIctory/pull/2566) | HLE: DirectStorage page writes are opened before the bytes land | Calvix2k | files: `crates/victory-gpu/src/watch.rs` |
| [#2582](https://github.com/Marvisak/VIctory/pull/2582) | GPU: a screen pass's own pool never waits longer than the frame budget (fixes #2433) | kais7654 | files: `crates/victory-gpu/src/pipeline/make.rs` |
| [#2593](https://github.com/Marvisak/VIctory/pull/2593) | Shader tests: BCPack's zigzag decode as console code matches the formats function | Dathinel | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2616](https://github.com/Marvisak/VIctory/pull/2616) | XTaskQueue: a dispatch serves every port, not only manual ones | F1reworks10 | files: `crates/victory-hle/src/modules/xasync.rs` |
| [#2643](https://github.com/Marvisak/VIctory/pull/2643) | Launcher: add lightweight world-frame capture. | anrq0 | files: `README.md`, `apps/victory/src/census.rs`, `apps/victory/src/main.rs`, `apps/victory/src/run.rs`, `crates/victory-gpu/src/bindless.rs` |
| [#2645](https://github.com/Marvisak/VIctory/pull/2645) | Measure release-build present intervals to diagnose menu frame pacing | maxence468 | files: `crates/victory-gpu/src/host.rs` |
| [#2650](https://github.com/Marvisak/VIctory/pull/2650) | GPU: #1779 (view heaps on hosts capped below 2^21) on current main, with lazy placed-texture views | Pierrot1398 | files: `crates/victory-gpu/src/descriptor/host.rs`, `crates/victory-gpu/src/draw.rs`, `crates/victory-gpu/src/host.rs` |
| [#2651](https://github.com/Marvisak/VIctory/pull/2651) | GPU: wave64 compute the translator sized runs on 32-lane hosts (stacked on #1922 and #233) | Pierrot1398 | files: `apps/victory/src/main.rs`, `crates/victory-shader/src/emit/host.rs` |
| [#2670](https://github.com/Marvisak/VIctory/pull/2670) | Build and test on Linux; a CI job keeps it so; VICTORY_LOG_FILE | nullexxx | files: `apps/victory/src/main.rs`, `crates/victory-hle/src/modules/xgameui.rs` |
| [#2677](https://github.com/Marvisak/VIctory/pull/2677) | App: keep run paths stable when the title changes directory | jaschinski97-ops | files: `apps/victory/src/run.rs` |
| [#2701](https://github.com/Marvisak/VIctory/pull/2701) | Decode signed and integer render targets correctly in diagnostic captures | VlREX | files: `crates/victory-gpu/src/capture.rs` |
| [#2707](https://github.com/Marvisak/VIctory/pull/2707) | GPU: preserve taken dynamic descriptor slots across texture eviction | Batushn | files: `crates/victory-gpu/src/descriptor/host.rs` |
| [#2717](https://github.com/Marvisak/VIctory/pull/2717) | Preserve held-key order in GameInput keyboard readings | VlREX | files: `crates/victory-hle/src/modules/gameinput.rs` |
| [#2733](https://github.com/Marvisak/VIctory/pull/2733) | Shaders, GPU: VICTORY_LOOP_CUTS=1 counts the lanes translated loops leave at the loop limit | Exopus-0x65f7ad0 | files: `crates/victory-gpu/src/draw.rs`, `crates/victory-shader/src/emit/synthetic_tests.rs` |
| [#2737](https://github.com/Marvisak/VIctory/pull/2737) | GPU: copy depth twins directly instead of through a scratch | Therecalloftheonion | files: `crates/victory-gpu/src/twin.rs` |
| [#2746](https://github.com/Marvisak/VIctory/pull/2746) | GPU: with VICTORY_FPS set, a present waits for the next frame's deadline | kais7654 | files: `crates/victory-gpu/src/host.rs` |
| [#2758](https://github.com/Marvisak/VIctory/pull/2758) | Windows compatibility work from TaynanGT/VIctory, merged with main | TaynanGT | files: `README.md`, `apps/victory/src/main.rs`, `crates/victory-gpu/src/bindless.rs`, `crates/victory-gpu/src/descriptor.rs`, `crates/victory-gpu/src/descriptor/host.rs` |
| [#2772](https://github.com/Marvisak/VIctory/pull/2772) | Pass XGameUi text entry scope hints to Windows text services | maxence468 | files: `crates/victory-hle/src/modules/xgameui.rs` |
| [#2807](https://github.com/Marvisak/VIctory/pull/2807) | Teste/series s 32gb | gabztoo | files: `README.md`, `apps/victory/src/run.rs`, `crates/victory-gpu/Cargo.toml`, `crates/victory-gpu/src/bindless.rs`, `crates/victory-gpu/src/capture.rs` |
| [#2813](https://github.com/Marvisak/VIctory/pull/2813) | shader: refuse reads of the carry s_lshlN_add_u32 leaves in SCC | spy0eye-beep | files: `crates/victory-shader/src/emit/valu_tests.rs` |
| [#2815](https://github.com/Marvisak/VIctory/pull/2815) | Experiment/pr2121 | theDVNVS | files: `README.md`, `apps/victory/src/main.rs`, `apps/victory/src/run.rs`, `apps/victory/src/translate.rs`, `crates/victory-formats/src/texture.rs` |
| [#2822](https://github.com/Marvisak/VIctory/pull/2822) | Shader: table reads the code computes mark their heap slots | kais7654 | files: `crates/victory-shader/src/emit/memory_tests.rs` |
| [#2933](https://github.com/Marvisak/VIctory/pull/2933) | victory-gpu: a view of no resource is not looked up as an alias (null dereference that ends every run after the account screen) | pes7 | files: `crates/victory-gpu/src/resource.rs` |
| [#3037](https://github.com/Marvisak/VIctory/pull/3037) | Fix #2503: tell GPU write watch before DirectStorage page writes | tharun-37 | files: `crates/victory-hle/src/modules/xmem.rs` |

## breaks the build (63)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#166](https://github.com/Marvisak/VIctory/pull/166) | Shaders: lower s_bitset{0,1}_b64, s_brev_b64 and s_bitreplicate_b64_b32 | n-romanovich | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524562 bytes exceeds the 524288-byte limit |
| [#379](https://github.com/Marvisak/VIctory/pull/379) | Shaders: lower v_div_fixup_f16 | LouisRiverstone | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 526079 bytes exceeds the 524288-byte limit |
| [#395](https://github.com/Marvisak/VIctory/pull/395) | shader: unpack compressed f16 pixel exports | Loggerten | crates\victory-shader\src\emit\lower.rs:11234:13: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#511](https://github.com/Marvisak/VIctory/pull/511) | Shaders: coalesce aligned constant-buffer loads | aycow | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524407 bytes exceeds the 524288-byte limit |
| [#529](https://github.com/Marvisak/VIctory/pull/529) | PE: preallocate symbol_key in CodeViewInfo | pushkarreddyy | crates\victory-pe\src\image.rs:879:1: error: unexpected closing delimiter: `}`: unexpected closing delimiter / error: could not compile `victory-pe` (lib test) due to 1 previous error / error: could not compile `victory-pe` (lib) due to 1 previous error |
| [#589](https://github.com/Marvisak/VIctory/pull/589) | fix(shader): skip unused image atomic descriptor reconstruction | jeremygold02 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525358 bytes exceeds the 524288-byte limit |
| [#606](https://github.com/Marvisak/VIctory/pull/606) | Shaders: ds_swizzle_b32 offsets from 0xC000 are the rotate and FFT modes | upipibi | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525382 bytes exceeds the 524288-byte limit |
| [#626](https://github.com/Marvisak/VIctory/pull/626) | GPU: fall back to standard root signature flags when host runtime rejects 0xC01/0xC00 | LAKSHYA-cmd-tech | crates\victory-gpu\src\pipeline\host.rs:998:1: error[E0428]: the name `tests` is defined multiple times: `tests` redefined here / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#642](https://github.com/Marvisak/VIctory/pull/642) | GPU: translate enhanced texture barriers in ID3D12GraphicsCommandList7::Barrier | nathanbzrr | crates\victory-gpu\src\list.rs:2872:30: error[E0308]: mismatched types: expected `Option<&ID3D12Resource>`, found `&ID3D12Resource` / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#1142](https://github.com/Marvisak/VIctory/pull/1142) | Shaders: support saturating clamp on packed 16-bit integer ops (v_pk_{add,sub,mad}_{u16,i16}) | ESAT586 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524956 bytes exceeds the 524288-byte limit |
| [#1315](https://github.com/Marvisak/VIctory/pull/1315) | Shaders, GPU: translate single-stream triangle geometry programs | r4tedx | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 530094 bytes exceeds the 524288-byte limit |
| [#1327](https://github.com/Marvisak/VIctory/pull/1327) | Shaders: apply bitwise modifiers to v_cmp_class_f32 source operands | fuzeofficlal | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524361 bytes exceeds the 524288-byte limit |
| [#1395](https://github.com/Marvisak/VIctory/pull/1395) | Shaders: lower s_bfe_u64, s_bfe_i64 and s_bfm_b64 | AnoHunted | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 529841 bytes exceeds the 524288-byte limit |
| [#1473](https://github.com/Marvisak/VIctory/pull/1473) | Shaders: track per-lane export state across mixed pixel-shader joins | Texbirds | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 527457 bytes exceeds the 524288-byte limit |
| [#1614](https://github.com/Marvisak/VIctory/pull/1614) | Shader tests: a cross-device VALU fuzzer (hardware adapters vs WARP) | alexdeliu | crates\victory-shader\src\emit\fuzz_tests.rs:214:9: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / crates\victory-shader\src\emit\fuzz_tests.rs:716:12: error: cannot construct `host::Host` with struct literal syntax due to private fields / error: could not compile `victory-shader` (lib test) due to 2 previous errors |
| [#1623](https://github.com/Marvisak/VIctory/pull/1623) | gfx10: keep an instruction's words inline instead of in a heap vector (decode -18..-45%, translation -1..-5%) | pes7 | crates\victory-shader\src\emit\random_tests.rs:505:39: error[E0616]: field `words` of struct `Instruction` is private: private field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#1704](https://github.com/Marvisak/VIctory/pull/1704) | FidelityFX: answer the upscale calls with DLSS through Streamline (stacked on #1868) | marquezinii | crates\victory-gpu\src\draw.rs:457:42: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / crates\victory-gpu\src\list.rs:1026:38: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / error: could not compile `victory-gpu` (lib) due to 2 previous errors |
| [#1712](https://github.com/Marvisak/VIctory/pull/1712) | victory-shader: support line-topology mesh shaders | tjthebigbearcat-hub | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525160 bytes exceeds the 524288-byte limit |
| [#1715](https://github.com/Marvisak/VIctory/pull/1715) | FidelityFX: DLSS frame generation on frames the title upscales (stacked on #1704) | marquezinii | crates\victory-gpu\src\draw.rs:457:42: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / crates\victory-gpu\src\list.rs:1026:38: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / error: could not compile `victory-gpu` (lib) due to 2 previous errors |
| [#1734](https://github.com/Marvisak/VIctory/pull/1734) | victory-shader: make the test dispatches cheap - an event wait and reused command objects (emit suite -33% wall, -48% CPU) | pes7 | crates\victory-shader\src\emit\wave64_tests.rs:1113:23: error[E0277]: `*mut c_void` cannot be sent between threads safely: `*mut c_void` cannot be sent between threads safely / crates\victory-shader\src\emit\host.rs:378:45: error[E0063]: missing field `reused` in initializer of `host::Host`: missing `reused` / error: could not compile `victory-shader` (lib test) due to 2 previous errors |
| [#1817](https://github.com/Marvisak/VIctory/pull/1817) | GPU: enforce logical indirect buffer spans | aycow | crates\victory-gpu\src\list.rs:1574:63: error[E0308]: mismatched types: expected `(u64, u64)`, found `u64` / error: could not compile `victory-gpu` (lib) due to 1 previous error / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#1868](https://github.com/Marvisak/VIctory/pull/1868) | FidelityFX: write an RGB9E5 output NVIDIA cannot store to through an FP16 texture (fixes a device removal) | marquezinii | crates\victory-gpu\src\draw.rs:460:42: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / crates\victory-gpu\src\list.rs:1026:38: error[E0308]: mismatched types: expected `&ID3D12Resource`, found `ID3D12Resource` / error: could not compile `victory-gpu` (lib) due to 2 previous errors |
| [#1871](https://github.com/Marvisak/VIctory/pull/1871) | Shaders: lower indexed tbuffer_load_format_* and indexed buffer_store_{byte,short} | ESAT586 | crates\victory-shader\src\emit\stride_tests.rs:871:9: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#1920](https://github.com/Marvisak/VIctory/pull/1920) | Shaders: v_mad_f32 and v_mac_f32 multiply apart from their add | kais7654 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524906 bytes exceeds the 524288-byte limit |
| [#1927](https://github.com/Marvisak/VIctory/pull/1927) | Shaders: d16 format loads saturate 32-bit integer channels | upipibi | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524686 bytes exceeds the 524288-byte limit |
| [#1994](https://github.com/Marvisak/VIctory/pull/1994) | Shaders: floor, ceil and fract read denormals as zeros | astrosteveo | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524376 bytes exceeds the 524288-byte limit |
| [#2020](https://github.com/Marvisak/VIctory/pull/2020) | Shaders: abs / neg on the shift-add and align ops act on the sign bit | upipibi | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524854 bytes exceeds the 524288-byte limit |
| [#2027](https://github.com/Marvisak/VIctory/pull/2027) | Shaders: a compute shader samples at level 0, not with derivatives (735 programs) | fiestorra | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525157 bytes exceeds the 524288-byte limit |
| [#2037](https://github.com/Marvisak/VIctory/pull/2037) | Shaders: byte and half format loads at a constant offset load the aligned dword directly (NVIDIA) | desplmfao | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524754 bytes exceeds the 524288-byte limit |
| [#2063](https://github.com/Marvisak/VIctory/pull/2063) | Shaders: lower s_ff0_i32_b32 and s_ff0_i32_b64 in pure 32-bit DXIL | geiyiliyabumo | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524603 bytes exceeds the 524288-byte limit |
| [#2070](https://github.com/Marvisak/VIctory/pull/2070) | Shaders: refuse the image instructions DXIL has no form of | 0xkn0wh3r3 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524961 bytes exceeds the 524288-byte limit |
| [#2077](https://github.com/Marvisak/VIctory/pull/2077) | Shaders: lower s_sext_i32_i8 and s_sext_i32_i16 in pure 32-bit DXIL | geiyiliyabumo | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524428 bytes exceeds the 524288-byte limit |
| [#2083](https://github.com/Marvisak/VIctory/pull/2083) | Shaders: lower s_bitreplicate_b64_b32 in pure 32-bit DXIL | geiyiliyabumo | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525528 bytes exceeds the 524288-byte limit |
| [#2094](https://github.com/Marvisak/VIctory/pull/2094) | Shaders: lower v_add_nc_i32, v_sub_nc_i32, v_add_nc_i16, and v_sub_nc_i16 in pure 32-bit DXIL | geiyiliyabumo | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 526926 bytes exceeds the 524288-byte limit |
| [#2122](https://github.com/Marvisak/VIctory/pull/2122) | query a buffer's size through a handle of its own | imjustprism | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 531588 bytes exceeds the 524288-byte limit |
| [#2152](https://github.com/Marvisak/VIctory/pull/2152) | Shaders: lower ds_permute_b32 and ds_nop | fuzeofficlal | crates\victory-shader\src\emit\ds_permute_tests.rs:187:9: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#2241](https://github.com/Marvisak/VIctory/pull/2241) | Shaders: 64-bit texture atomics as one i64 atomic | FoxxoOwO | crates\victory-shader\src\emit\valu_tests.rs:1940:9: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#2283](https://github.com/Marvisak/VIctory/pull/2283) | GPU: a fast content digest for untracked textures, and their commit check kept per remap epoch | alessiodeia | crates\victory-gpu\src\texture.rs:249:38: error[E0308]: mismatched types: expected `[u64; 2]`, found `Hash` / crates\victory-gpu\src\texture.rs:273:31: error[E0308]: mismatched types: expected `[u64; 2]`, found `Hash` / error: could not compile `victory-gpu` (lib) due to 2 previous errors |
| [#2314](https://github.com/Marvisak/VIctory/pull/2314) | GPU: copy compatible multisampled texture aliases directly | andrewpozdnakov7-jpg | crates\victory-gpu\src\resource.rs:2641:28: error[E0308]: mismatched types: expected `Option<&ID3D12Resource>`, found `&ID3D12Resource` / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#2333](https://github.com/Marvisak/VIctory/pull/2333) | Shaders: buffer byte and half stores of a VGPR's high half (_d16_hi) | TinkerBell-90 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524315 bytes exceeds the 524288-byte limit |
| [#2336](https://github.com/Marvisak/VIctory/pull/2336) | GPU: list only pipelines retained by the host library as prebuilt | andrewpozdnakov7-jpg | crates\victory-gpu\src\pipeline\library.rs:414:19: error[E0308]: mismatched types: expected `PipelineState`, found `ID3D12PipelineState` / error: could not compile `victory-gpu` (lib) due to 1 previous error / crates\victory-gpu\src\pipeline\host.rs:1209:17: error[E0594]: cannot assign to `cache`, as it is a captured variable in a `Fn` closure: cannot assign |
| [#2387](https://github.com/Marvisak/VIctory/pull/2387) | Shaders: track SGPR origins across cancelling s_xor_b32/b64 swaps (#815) | fuzeofficlal | crates\victory-shader\src\emit\valu_tests.rs:1005:9: error[E0560]: struct `Parts<'_>` has no field named `view_marks`: `Parts<'_>` does not have this field / error: could not compile `victory-shader` (lib test) due to 1 previous error |
| [#2396](https://github.com/Marvisak/VIctory/pull/2396) | GPU: wire DeserializeComputePipelineStateX to assemble ACCC | makmatvey | crates\victory-gpu\src\pipeline.rs:806:5: error[E0061]: this function takes 5 arguments but 4 arguments were supplied / error: could not compile `victory-gpu` (lib) due to 1 previous error / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#2509](https://github.com/Marvisak/VIctory/pull/2509) | GPU: upload the stencil plane with guest textures | andrewpozdnakov7-jpg | crates\victory-gpu\src\texture.rs:1164:13: error[E0308]: mismatched types: expected `Texture`, found `Layout` / crates\victory-gpu\src\texture.rs:1160:32: error[E0063]: missing field `subresources_per_plane` in initializer of `texture::Staging`: missing `subresources_per_plane` / error: could not compile `victory-gpu` (lib test) due to 2 previous errors |
| [#2549](https://github.com/Marvisak/VIctory/pull/2549) | GPU: a remapped mapping does not mark the mappings that still show it | Calvix2k | crates\victory-gpu\src\watch.rs:842:5: error[E0425]: cannot find function `changed_here` in this scope: not found in this scope / error: could not compile `victory-gpu` (lib) due to 1 previous error / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#2556](https://github.com/Marvisak/VIctory/pull/2556) | GPU: skip pipeline demand for empty compute dispatches | andrewpozdnakov7-jpg | crates\victory-gpu\src\pipeline\make.rs:677:13: error[E0061]: this function takes 5 arguments but 4 arguments were supplied / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#2623](https://github.com/Marvisak/VIctory/pull/2623) | Shaders: round half-precision fused multiply-add once | andrewpozdnakov7-jpg | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524748 bytes exceeds the 524288-byte limit |
| [#2654](https://github.com/Marvisak/VIctory/pull/2654) | GPU: skip pipeline demand for empty direct draws | andrewpozdnakov7-jpg | crates\victory-gpu\src\pipeline\make.rs:512:17: error[E0061]: this function takes 5 arguments but 4 arguments were supplied / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#2724](https://github.com/Marvisak/VIctory/pull/2724) | Shaders: texture reads at a computed table entry keep their read mark (#2722) | BastienRodz | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524630 bytes exceeds the 524288-byte limit |
| [#2729](https://github.com/Marvisak/VIctory/pull/2729) | GPU: keep rectangle corners consistent across vertex streams | andrewpozdnakov7-jpg | crates\victory-gpu\src\pipeline\host.rs:1186:13: error[E0061]: this function takes 5 arguments but 4 arguments were supplied / crates\victory-gpu\src\pipeline\host.rs:1349:28: error[E0308]: mismatched types: expected `Option<&ID3D12Resource>`, found `&ID3D12Resource` / error: could not compile `victory-gpu` (lib test) due to 2 previous errors |
| [#2755](https://github.com/Marvisak/VIctory/pull/2755) | Shaders: coalesce title-memory dirty marks within a wave | brainbudt | crates\victory-shader\src\emit\mod.rs:2191:21: error[E0433]: cannot find type `Shader` in this scope: use of undeclared type `Shader` / crates\victory-shader\src\emit\mod.rs:2198:50: error[E0433]: cannot find type `Attr` in this scope: use of undeclared type `Attr` / crates\victory-shader\src\emit\mod.rs:2200:44: error[E0433]: cannot find type `Attr` in this scope: use of undeclared type `Attr` |
| [#2768](https://github.com/Marvisak/VIctory/pull/2768) | Shaders: decode and lower v_dot8_i32_i4 | lcg007xd-c | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525737 bytes exceeds the 524288-byte limit |
| [#2782](https://github.com/Marvisak/VIctory/pull/2782) | Shaders: read known FP16/FP64 rounding mode bits | andrewpozdnakov7-jpg | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524783 bytes exceeds the 524288-byte limit |
| [#2802](https://github.com/Marvisak/VIctory/pull/2802) | Shaders: emit UAV barrier fence for global flat stores and atomics | fuzeofficlal | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525504 bytes exceeds the 524288-byte limit |
| [#2884](https://github.com/Marvisak/VIctory/pull/2884) | Shaders: round packed half-precision fused multiply-add once | andrewpozdnakov7-jpg | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524362 bytes exceeds the 524288-byte limit |
| [#2893](https://github.com/Marvisak/VIctory/pull/2893) | Shaders: find the normalized load rounding shift with one bit scan | Ingenioeren | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524916 bytes exceeds the 524288-byte limit |
| [#2943](https://github.com/Marvisak/VIctory/pull/2943) | Shaders: pack half FMA NaNs directly | Ingenioeren | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524789 bytes exceeds the 524288-byte limit |
| [#2968](https://github.com/Marvisak/VIctory/pull/2968) | Shaders: f32 floor, ceil and fract flush denormal operands | neonbyte1 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524572 bytes exceeds the 524288-byte limit |
| [#2996](https://github.com/Marvisak/VIctory/pull/2996) | GPU: number bounded indirect mesh groups consecutively | andrewpozdnakov7-jpg | crates\victory-gpu\src\pipeline\host.rs:1319:13: error[E0061]: this function takes 5 arguments but 4 arguments were supplied / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#3005](https://github.com/Marvisak/VIctory/pull/3005) | GPU: make already-used pipeline lookups read-only | AwsAli05 | crates\victory-gpu\src\pipeline\make.rs:779:31: error[E0599]: no method named `load` found for struct `std::sync::Once` in the current scope: method not found in `std::sync::Once` / error: could not compile `victory-gpu` (lib test) due to 1 previous error |
| [#3007](https://github.com/Marvisak/VIctory/pull/3007) | Shaders: lower the 32-bit mul_hi forms to one UMul/IMul | Ingenioeren | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 525583 bytes exceeds the 524288-byte limit |
| [#3027](https://github.com/Marvisak/VIctory/pull/3027) | Shaders: lower v_min3/v_max3/v_med3 to DXIL integer min/max | Ingenioeren | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524853 bytes exceeds the 524288-byte limit |
| [#3056](https://github.com/Marvisak/VIctory/pull/3056) | Shaders/Lower: guard global_atomic_fmin and global_atomic_fmax against NaN operands | RVZO6 | asset policy: POLICY: crates/victory-shader/src/emit/lower.rs: 524522 bytes exceeds the 524288-byte limit |

## changes CI workflows (8)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#113](https://github.com/Marvisak/VIctory/pull/113) | GitHub: rebase issue forms and PR template on main | Quat3rnion | files: `.github/workflows/pr-description.yml` |
| [#509](https://github.com/Marvisak/VIctory/pull/509) | GPU: add an opt-in execution performance census | aycow | files: `.github/workflows/ci.yml` |
| [#1058](https://github.com/Marvisak/VIctory/pull/1058) | CI: serialize Windows workspace tests | divyeshganta | files: `.github/workflows/ci.yml` |
| [#1241](https://github.com/Marvisak/VIctory/pull/1241) | CI: build and test the host-independent crates on Linux | MIchiel1234 | files: `.github/workflows/ci.yml` |
| [#2135](https://github.com/Marvisak/VIctory/pull/2135) | ci: Automated GitHub Actions Build Workflow | 7d4d9e33 | files: `.github/workflows/build-windows.yml` |
| [#2188](https://github.com/Marvisak/VIctory/pull/2188) | Testing: compare Windows benchmark runs with memory and time limits | Razdva122 | files: `.github/workflows/ci.yml` |
| [#2854](https://github.com/Marvisak/VIctory/pull/2854) | xtask: fail the test run when it executed nothing | HailLucifer666 | files: `.github/workflows/ci.yml` |
| [#2890](https://github.com/Marvisak/VIctory/pull/2890) | Linux build: main builds, lints and tests off Windows again (carries #2334, fixes #90) | arogan178 | files: `.github/workflows/ci.yml` |

## draft (34)

| PR | Title | Author | Detail |
|---|---|---|---|
| [#390](https://github.com/Marvisak/VIctory/pull/390) | Crash log: a panic carries our Rust stack | Kaairim |  |
| [#391](https://github.com/Marvisak/VIctory/pull/391) | Shaders: refuse LDS past the host's group limit by name | Kaairim |  |
| [#562](https://github.com/Marvisak/VIctory/pull/562) | GPU: reuse immutable descriptor tables across command lists | aycow |  |
| [#1179](https://github.com/Marvisak/VIctory/pull/1179) | Input: choose the loose controls diagram by active gamepad (stacked on #312) | Razdva122 |  |
| [#1789](https://github.com/Marvisak/VIctory/pull/1789) | fix(core): keep persistent data outside the cache | dereoalex |  |
| [#1965](https://github.com/Marvisak/VIctory/pull/1965) | GTA VI: all local work to reach the lit world, on current main (draft) | antocorvo3000 |  |
| [#1970](https://github.com/Marvisak/VIctory/pull/1970) | GTA VI: first approach with the title memory mirror (draft, for reference) | antocorvo3000 |  |
| [#2112](https://github.com/Marvisak/VIctory/pull/2112) | GPU: title memory in place instead of copied, opt-in (VICTORY_IN_PLACE=1; stacked on #2088, towards #880) | desplmfao |  |
| [#2120](https://github.com/Marvisak/VIctory/pull/2120) | GPU: copies of read-only title buffers in GPU upload heaps (opt-in) | 0xkn0wh3r3 |  |
| [#2130](https://github.com/Marvisak/VIctory/pull/2130) | GPU: copies of written title buffers in video memory with a mirror (opt-in) | 0xkn0wh3r3 |  |
| [#2171](https://github.com/Marvisak/VIctory/pull/2171) | GPU: a debug overlay, Alt+Z, drawn into the presented frame | 0xkn0wh3r3 |  |
| [#2203](https://github.com/Marvisak/VIctory/pull/2203) | Shaders/GPU: port experimental GTX compute and vertex fallback to current main | ElSeba0811 |  |
| [#2214](https://github.com/Marvisak/VIctory/pull/2214) | Shaders: console flow for groups of several console waves on 32-lane hosts | shawshanker18 |  |
| [#2222](https://github.com/Marvisak/VIctory/pull/2222) | GPU: render targets are demoted last, and upload-heap copies take a share of the VRAM budget | 0xkn0wh3r3 |  |
| [#2349](https://github.com/Marvisak/VIctory/pull/2349) | GPU: cheaper title memory copies, refresh batches and copy-back | denkencar-sketch |  |
| [#2465](https://github.com/Marvisak/VIctory/pull/2465) | GPU: the views' written-pages bitmap lives in video memory | wbkepler |  |
| [#2479](https://github.com/Marvisak/VIctory/pull/2479) | GPU: synchronize frame interval resets with tick reservations | VlREX |  |
| [#2482](https://github.com/Marvisak/VIctory/pull/2482) | GPU tests: close section handles after mapping watch test views | VlREX |  |
| [#2485](https://github.com/Marvisak/VIctory/pull/2485) | GPU tests: unmap the write-watch alias fixture views | VlREX |  |
| [#2487](https://github.com/Marvisak/VIctory/pull/2487) | GPU tests: release the bindless fixture descriptor heap | VlREX |  |
| [#2489](https://github.com/Marvisak/VIctory/pull/2489) | GPU tests: release buffers and textures in bindless fixtures | VlREX |  |
| [#2494](https://github.com/Marvisak/VIctory/pull/2494) | GPU/HLE: zero-reimport in-place memory remap prototype over SEC_COMMIT sections (#1905) | nathanbzrr |  |
| [#2495](https://github.com/Marvisak/VIctory/pull/2495) | GPU tests: release root signatures through their COM vtable | VlREX |  |
| [#2498](https://github.com/Marvisak/VIctory/pull/2498) | GPU tests: release the owned descriptor heap fixture | VlREX |  |
| [#2500](https://github.com/Marvisak/VIctory/pull/2500) | CLI: report completed shader translation jobs | VlREX |  |
| [#2502](https://github.com/Marvisak/VIctory/pull/2502) | CLI: distinguish named and ordinal missing imports in census | VlREX |  |
| [#2624](https://github.com/Marvisak/VIctory/pull/2624) | GPU: forward all direct mesh dispatch group counts | andrewpozdnakov7-jpg |  |
| [#2734](https://github.com/Marvisak/VIctory/pull/2734) | GPU: less copying back and forth: hot title buffers kept in video memory (opt-in, stacked on #2112) | sirrus98 |  |
| [#2751](https://github.com/Marvisak/VIctory/pull/2751) | FidelityFX: add experimental AMD Frame Generation 4.0.2 camera inputs | AwkGrep256 |  |
| [#2770](https://github.com/Marvisak/VIctory/pull/2770) | HLE: list the host's voices to the title and speak in the one it picks | kilolimaVI |  |
| [#2824](https://github.com/Marvisak/VIctory/pull/2824) | HLE/GPU: invalidate write trackers on 32-bit XMem allocation release and reuse | VlREX |  |
| [#2863](https://github.com/Marvisak/VIctory/pull/2863) | Diagnostics: opt-in native Graphics settings tab and menu traces | AwkGrep256 |  |
| [#2870](https://github.com/Marvisak/VIctory/pull/2870) | GPU: host copies of title buffers are in video memory by default where the host has GPU upload heaps | 0xkn0wh3r3 |  |
| [#2945](https://github.com/Marvisak/VIctory/pull/2945) | GPU: title memory in place by default where the host GPU shares memory with the CPU (stacked on #2112, #2912, #2921) | 0xkn0wh3r3 |  |
