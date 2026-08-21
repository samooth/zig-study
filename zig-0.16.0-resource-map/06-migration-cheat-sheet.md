# Zig 0.16.0 — Migration Cheat Sheet

Quick-reference for migrating from 0.15.x to 0.16.0.

## Entry Point

```zig
// OLD
pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator{};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();
    // ...
}

// NEW
pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;
    const io = init.io;
    const arena = init.arena;
    // ...
}
```

## Allocator Renames

| Old | New |
|-----|-----|
| `std.heap.GeneralPurposeAllocator` | `std.heap.DebugAllocator` |
| `GeneralPurposeAllocatorConfig` | `DebugAllocatorConfig` |

## I/O Module

| Old | New |
|-----|-----|
| `std.io` | `std.Io` |
| `std.io.GenericReader` | `std.Io.Reader` |
| `std.io.AnyReader` | `std.Io.Reader` |
| `std.io.fixedBufferStream(data)` (read) | `std.Io.Reader.fixed(data)` |
| `std.io.fixedBufferStream(buf)` (write) | `std.Io.Writer.fixed(buf)` |
| `std.io.getStdIn()` | `Io.File.stdin()` |
| `std.io.getStdOut()` | `Io.File.stdout()` |
| `std.io.getStdErr()` | `Io.File.stderr()` |

## File System

| Old | New |
|-----|-----|
| `std.fs.cwd()` | `std.Io.Dir.cwd()` |
| `std.fs.openFile(path, flags)` | `Io.Dir.openFile(io, path, flags)` |
| `file.reader()` | `file.reader(io, &.{})` |
| `file.writer()` | `file.writer(io, &.{})` |
| `std.fs.path` | `std.Io.Dir.path` (or keep using `std.fs.path` — deprecated alias) |
| `std.fs.max_path_bytes` | `std.Io.Dir.max_path_bytes` |
| `fs.Dir.readFileAlloc(alloc, path, max)` | `Io.Dir.cwd().readFileAlloc(io, path, alloc, .limited(max))` |
| `file.readToEndAlloc(alloc, max)` | `file_reader.interface.allocRemaining(alloc, .limited(max))` |
| `std.fs.getAppDataDir` | Removed (use `known-folders` package) |

## String Operations

| Old | New |
|-----|-----|
| `std.mem.trimLeft` | `std.mem.trimStart` |
| `std.mem.trimRight` | `std.mem.trimEnd` |

## Process

| Old | New |
|-----|-----|
| `std.process.argsAlloc(alloc)` | `init.minimal.args.toSlice(arena)` |
| `std.process.getCwd(buf)` | `std.process.currentPath(io, buf)` |
| `std.process.getCwdAlloc(alloc)` | `std.process.currentPathAlloc(io, alloc)` |
| `std.process.Child` stdin/stdout/stderr | Now `?Io.File` instead of raw handles |

## Time

| Old | New |
|-----|-----|
| `std.time.Instant` | `std.Io.Timestamp` |
| `std.time.Timer` | `std.Io.Timestamp` |
| `std.time.timestamp()` | `Io.Timestamp.now(io)` |
| `std.time.sleep(ns)` | `io.sleep(timeout)` |
| `{D}` format specifier | `std.Io.Duration{ .nanoseconds = ns }` with `{f}` |

## Random

| Old | New |
|-----|-----|
| `std.crypto.random.bytes(buf)` | `io.random(buf)` |
| `std.crypto.random.int(T)` | `io.random.int(T)` |
| CSPRNG | `Io.randomSecure(io, buf)` |

## Threading

| Old | New |
|-----|-----|
| `std.Thread.Pool` | Removed — use `std.Io.Group` + `Io.async` |
| `thread_pool.spawnWg(wg, func, args)` | `io.async(func, args)` or `group.spawn(io, func, args)` |

## Containers

| Old | New |
|-----|-----|
| `ArrayList(T){}` | `ArrayList(T).empty` |
| `HashMap(K,V,.{})` | `HashMap(K,V,.{}).empty` |
| `ArrayListUnmanaged(T){}` | `ArrayListUnmanaged(T).empty` |

## C Interop

| Old | New |
|-----|-----|
| `@cImport({ @cInclude("x.h"); })` | `b.addTranslateC` in build.zig, then `@import("c")` |
| `exe.linkLibC()` | `link_libc = true` in module options |

## Memory

| Old | New |
|-----|-----|
| `std.posix.mlock()` | `std.process.lockMemory(slice, .{})` |
| `std.posix.mlock2(slice, flags)` | `std.process.lockMemory(slice, .{.on_fault = true})` |
| `std.posix.mlockall(flags)` | `std.process.lockMemoryAll(.{ .current = true, .future = true })` |

## Build System

| Old | New |
|-----|-----|
| `.name = "x"` in build.zig.zon | `.name = .x` (enum literal) |
| `.fingerprint` field | Required in build.zig.zig.zon |
| `root_source_file = b.path(...)` | `root_module = b.createModule(.{ .root_source_file = ... })` |
| `b.makeTempPath()` | `b.addTempFiles(...)` |

## Quick Grep Safety Net

After migration, search for these patterns:

```bash
# Deprecated patterns that should be gone
rg "GeneralPurposeAllocator" --include "*.zig"
rg "@cImport" --include "*.zig"
rg "std\.io\." --include "*.zig"
rg "std\.fs\.openFile" --include "*.zig"
rg "trimLeft|trimRight" --include "*.zig"
rg "getCwd" --include "*.zig"
rg "argsAlloc" --include "*.zig"
rg "Thread\.Pool" --include "*.zig"
rg "fixedBufferStream" --include "*.zig"
rg "root_source_file" --include "*.zig"
rg "\.name = \"" --include "build.zig.zon"
```

## Performance Warning

`std.heap.DebugAllocator` can be **up to 1400x slower** than the old GPA for allocator-heavy workloads in Debug mode. Always time a representative workload after migration:

```bash
time ./your-tool <real-input>
```

If you see >10x regression vs 0.15, this is almost certainly the cause. Use `SmpAllocator` or `ArenaAllocator` for hot paths.
