# Zig 0.16.0 — Release Overview

## Release Facts

| Field | Value |
|-------|-------|
| Version | 0.16.0 |
| Release Date | April 14, 2026 |
| Development Cycle | 8 months |
| Contributors | 244 |
| Commits | 1183 |
| Mascot | Carmen the Allocgator |
| Official Theme | I/O as an Interface |

## Headline Features

### 1. I/O as an Interface (`std.Io`)

The largest architectural change in Zig's history. Every I/O-capable function now takes an `Io` instance as an argument. This unifies:

- File system operations
- Networking (TCP/UDP/Unix)
- Process management
- Time and sleeping
- Randomness
- Async/concurrent execution
- Synchronization primitives

The `Io` struct is a vtable: `{ userdata: ?*anyopaque, vtable: *const VTable }`. Backends include `Uring` (Linux), `Kqueue` (BSD/macOS), and `Threaded` (thread-pool fallback).

### 2. Juicy Main (`std.process.Init`)

New entry point pattern that eliminates allocator/env boilerplate:

```zig
pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;           // DebugAllocator
    const io = init.io;             // Default Io implementation
    const arena = init.arena;       // ArenaAllocator (process-lifetime)
    const environ = init.environ_map;
    const args = try init.minimal.args.toSlice(arena.allocator());
}
```

### 3. @cImport Deprecated

C translation moves to the build system via `b.addTranslateC`. The `@cImport` builtin still works in 0.16.0 but will be removed in 0.17.0.

### 4. @Type Removed

Replaced by focused builtins: `@typeInfo`, `@typeName`, `@as`, `@Tuple`, etc.

### 5. New ELF Linker

Enabled with `-fnew-linker` or `exe.use_new_linker = true`. Default for `-fincremental` + ELF targets. 66% faster incremental link times.

### 6. Self-hosted Backend Progress

Faster debug builds (~15% improvement) without LLVM dependency. Smaller binary output.

## Compiler Changes

- **C Translation** now based on Aro + translate-c instead of libclang
- **Reworked Type Resolution** — acyclic dependency graph, better incremental compilation
- **Incremental Compilation** — major improvements; one-line changes recompile in milliseconds
- **New ELF Linker** — 66% faster for incremental builds

## Target Support

| Platform | Version |
|----------|---------|
| musl libc | Updated (1206 functions remaining) |
| glibc | 2.43 |
| Linux Headers | 6.19 |
| macOS Headers | 26.4 |
| MinGW-w64 | commit `38c8142f` (99 fewer C source files) |

## Standard Library Highlights

- `std.Io` — unified I/O abstraction
- `std.process.Init` — Juicy Main
- `std.heap.DebugAllocator` — renamed from `GeneralPurposeAllocator`
- `std.compress.zstd` — Zstandard support added
- `std.crypto.aes_siv`, `aes_gcm_siv` — nonce-reuse-resistant AEADs
- `std.crypto.ascon` — NIST lightweight crypto (SP 800-232)
- `std.Io.Dir.walkSelectively` — selective directory tree walking
- `std.process.lockMemory` / `lockMemoryAll` — replaces `mlock`/`mlockall`

## Known Issues

- `zig build test --fuzz` fails without `-Doptimize=ReleaseSafe` (fix in progress)
- DebugAllocator can be up to 1400x slower than GPA for allocator-heavy workloads in Debug mode
- Self-hosted aarch64 backend crashes on behavior tests

## Links

- [Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)
- [Download](https://ziglang.org/download/)
- [Source](https://codeberg.org/ziglang/zig)
- [Language Reference](https://ziglang.org/documentation/0.16.0/)
- [Standard Library Docs](https://ziglang.org/documentation/0.16.0/std/)
- [Milestone #30](https://github.com/ziglang/zig/milestone/30)
