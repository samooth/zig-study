# Zig 0.16.0 & 0.17.0 — Known Bugs and Issues

> Last updated: 2026-08-21
> Sources: Codeberg issue tracker, GitHub milestones, Ziggit community, Zig devlog

---

## Zig 0.16.0

### Compiler

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#31888](https://codeberg.org/ziglang/zig/issues/31888) | Miscompilation regarding C pointers | High | Modify C code to avoid affected patterns (see [termbox2 workaround](https://github.com/AnErrupTion/termbox2/commit/c7f241e8888ce243e1748b05c26a42fcfaaad936)) |
| [zig#30709](https://github.com/ziglang/zig/issues/30709) | DebugAllocator up to 1400x slower than GPA in Debug mode | Medium | Use `smp_allocator` for benchmarks; DebugAllocator is still correct but very slow for small allocations |
| [zig#25997](https://github.com/ziglang/zig/issues/25997) | Segfault when building with self-hosted x86_64 backend | High | Use LLVM backend (`-fllvm`) |
| — | Self-hosted aarch64 backend crashes on behavior tests | High | Use LLVM backend |

### Linker

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#31272](https://codeberg.org/ziglang/zig/issues/31272) | ELF linker assertion failure / linking issues in Debug mode | High | Use LLVM backend in Debug mode |
| [zig#31808](https://codeberg.org/ziglang/zig/issues/31808) | ELF linker assertion failure in `updateSymtabSize` | High | Use LLVM backend |

### Build System

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [translate-c#31863](https://codeberg.org/ziglang/zig/pulls/31863) | `zig build test --fuzz` fails without `-Doptimize=ReleaseSafe` | Medium | Pass `-Doptimize=ReleaseSafe` when fuzz testing |

### translate-c

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [translate-c#319](https://codeberg.org/ziglang/translate-c/issues/319) | Missing POSIX defines (`_XOPEN_SOURCE`) | Medium | Add `-D_XOPEN_SOURCE=700` to translate-c cflags |
| [translate-c#339](https://codeberg.org/ziglang/translate-c/issues/339) | Missing `_FORTIFY_SOURCE` and `__BSD_VISIBLE` | Medium | Add `-D_FORTIFY_SOURCE=0` (Linux), `-D__BSD_VISIBLE=1` (FreeBSD) to cflags |
| — | translate-c failures after upgrade from 0.15 (community reports on Ziggit) | Medium | Review C headers for missing platform defines; use `b.addTranslateC` with explicit cflags |

### Standard Library

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| — | LLVM loop vectorization disabled in self-hosted backend | Low | No user-facing impact for most code; use `-fllvm` for maximum optimization |

---

## Zig 0.17.0

### Compiler

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#36452](https://codeberg.org/ziglang/zig/issues/36452) | Manually-constructed `@Struct` has wrongly-typed field | Medium | Avoid manually constructing `@Struct` values; use normal struct literals |
| [zig#36574](https://codeberg.org/ziglang/zig/issues/36574) | Byte-aligned pointer to `packed struct` field is no longer a normal pointer | High | Use explicit `@ptrCast` or rework packed struct access patterns |
| [zig#36521](https://codeberg.org/ziglang/zig/issues/36521) | AIR uses `.splat` tag for arrays, causing bad codegen | Medium | Avoid splatting arrays in comptime |
| [zig#36569](https://codeberg.org/ziglang/zig/issues/36569) | x86_64 codegen crash when generating call from `.text` section bytes | High | Avoid calling function pointers derived from raw `.text` bytes |
| [zig#36567](https://codeberg.org/ziglang/zig/issues/36567) | `DebugAllocator` does not catch use-after-realloc | Medium | Use explicit bounds checking or `SafeAllocator` for testing |
| [zig#36565](https://codeberg.org/ziglang/zig/issues/36565) | `Io.Writer.printAddress` and `{*}` formatting ignore pointer bit offset | Low | Avoid formatting pointers with bit offsets directly |

### Linker

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#31823](https://codeberg.org/ziglang/zig/issues/31823) | Regression: linking `.so` by filename fails ("unable to find library") | High | Use full path or `-l` flag instead of filename |
| [zig#36551](https://codeberg.org/ziglang/zig/issues/36551) | SPIR-V linker emits duplicate entry points when linking incrementally | Medium | Avoid incremental linking for SPIR-V targets |
| [zig#36560](https://codeberg.org/ziglang/zig/issues/36560) | Old ELF linker still active (elimination planned for 0.18) | Low | No user-facing impact yet |

### Build System

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#36408](https://codeberg.org/ziglang/zig/issues/36408) | Old dependency used after `zig fetch --save <path>` (regression) | Medium | Run `zig build` twice or manually edit `build.zig.zon` |
| [zig#35371](https://codeberg.org/ziglang/zig/issues/35371) | `zig build` fails with SIGSEGV when fetching dependencies | High | Ensure stable network; retry; check `.zig-cache` permissions |
| [zig#35500](https://codeberg.org/ziglang/zig/issues/35500) | `cwd` causes build scripts to be recompiled unnecessarily | Medium | Avoid changing `cwd` in build scripts |
| [zig#32097](https://codeberg.org/ziglang/zig/issues/32097) | Absolute and cwd-relative paths in build cache behave inconsistently | Low | Use relative paths in build.zig |
| [zig#31876](https://codeberg.org/ziglang/zig/issues/31876) | AccessDenied when linking temporary options.zig to .zig-cache (regression) | Medium | Ensure `.zig-cache` directory permissions are correct |
| [zig#35568](https://codeberg.org/ziglang/zig/issues/35568) | Cannot add arbitrary C compiler flags with `std.Build.Step.TranslateC` (regression) | Medium | Use the `translate-c` package directly instead of `b.addTranslateC` |

### Standard Library

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#36576](https://codeberg.org/ziglang/zig/issues/36576) | `Io.Reader.writableVector` does ill-advised makeshift rebase | High | Avoid using `writableVector` directly; use higher-level Io APIs |
| [zig#36578](https://codeberg.org/ziglang/zig/issues/36578) | `Io.Reader.rebase` implies pointer stability it cannot uphold | Medium | Do not hold pointers across `rebase` calls |
| [zig#36570](https://codeberg.org/ziglang/zig/issues/36570) | `std.crypto.tls.Client` uses invalidated buffer | High (Urgent) | Avoid TLS client in affected configurations; await fix |
| [zig#36533](https://codeberg.org/ziglang/zig/issues/36533) | Severe memory leak on macOS (Urgent) | High | Monitor memory usage; avoid long-running processes on macOS |
| [zig#36539](https://codeberg.org/ziglang/zig/issues/36539) | `std.http.Client` DNS fails with systemd-resolved + search domain | Medium | Configure systemd-resolved without search domains, or use custom DNS resolver |
| [zig#36541](https://codeberg.org/ziglang/zig/issues/36541) | Unexpected side effect due to `NO_COLOR` environment variable | Low | Unset `NO_COLOR` if color output is expected |

### Cross-Compilation

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#36522](https://codeberg.org/ziglang/zig/issues/36522) | WASM: segfault when using variadic functions with complex C types | High | Avoid variadic C functions in WASM targets |
| [zig#36536](https://codeberg.org/ziglang/zig/issues/36536) | SPIR-V: tuple indexing doesn't account for comptime fields | Medium | Avoid tuple indexing with comptime fields on SPIR-V |
| [zig#31658](https://codeberg.org/ziglang/zig/issues/31658) | macOS builds fail with Xcode 26.4 | High | Use Xcode 26.3 or set `DEVELOPER_DIR` to an older Xcode |

### Debug Info

| Issue | Description | Severity | Workaround |
|-------|-------------|----------|------------|
| [zig#36561](https://codeberg.org/ziglang/zig/issues/36561) | `llvm-dwarfdump --verify` reports DW_TAG errors | Low | Ignore DWARF verification warnings; debug info is still functional |

---

## General Advice

- **Use LLVM backend** (`-fllvm`) if you hit self-hosted backend crashes or miscompilations
- **Use `smp_allocator`** instead of `DebugAllocator` for performance-sensitive code
- **Pin dependencies** in `build.zig.zon` with exact hashes to avoid fetch issues
- **Test with both Debug and ReleaseSafe** modes — some bugs are mode-specific
- **Check Codeberg issues** before upgrading: [0.16.0 milestone](https://codeberg.org/ziglang/zig/milestone/32343) | [0.17.0 milestone](https://codeberg.org/ziglang/zig/milestone/69474)

---

## Reporting Bugs

- **Primary tracker**: [codeberg.org/ziglang/zig/issues](https://codeberg.org/ziglang/zig/issues)
- **translate-c**: [codeberg.org/ziglang/translate-c/issues](https://codeberg.org/ziglang/translate-c/issues)
- **Community discussion**: [ziggit.dev](https://ziggit.dev)
- **Legacy GitHub issues**: [github.com/ziglang/zig/issues](https://github.com/ziglang/zig/issues) (read-only, migrated to Codeberg)
