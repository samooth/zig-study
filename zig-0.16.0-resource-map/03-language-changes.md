# Zig 0.16.0 — Language Changes

## Builtin Changes

### @Type Removed

`@Type` has been removed. Use focused builtins instead:

| Old | New |
|-----|-----|
| `@Type(.{ .@"enum" = ... })` | `@Type(.{ .@"enum" = ... })` — still works for enums |
| `@Type(.{ .@"struct" = ... })` | Construct struct types via `@Type` or comptime |
| `@Type(.{ .@"union" = ... })` | Construct union types via `@Type` or comptime |
| `@TypeInfo(T)` | `@typeInfo(T)` (lowercase `t`) |
| `@typeName(T)` | `@typeName(T)` (unchanged) |

**Note:** You can no longer reify tuple types with `comptime` fields, or reify error sets.

### @cImport Deprecated

Still compiles in 0.16.0, but will be removed in 0.17.0. Migration:

```zig
// OLD
const c = @cImport({
    @cInclude("stdio.h");
});

// NEW — build.zig
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
    .optimize = optimize,
});

// NEW — src/main.zig
const c = @import("c");
```

### @Tuple

New builtin for constructing tuple types:

```zig
const MyTuple = @Tuple(&.{ u32, []const u8, bool });
```

## Syntax Changes

### Packed Struct/Union Changes

- Pointers are now **forbidden** inside packed structs and unions
- Equality comparisons on packed unions are now directly supported (no need to wrap in packed struct)

### Runtime Vector Indexing Forbidden

Runtime vector indexing is no longer allowed. Use `@as` or explicit element access instead.

### Switch Statement Changes

- Lazy values are properly resolved before comparisons with prong items
- Evaluation order is now the same for all switch types (with or without label)

### Equality Comparisons on Packed Unions

```zig
const PackedUnion = packed union {
    a: u32,
    b: u32,
};
// Now you can compare directly:
if (x == y) { ... } // Previously required wrapping in packed struct
```

## Type System Changes

### Reworked Type Resolution

- Internal dependency graph is now acyclic (except for actual dependency loops)
- Eliminates "over-analysis" — rebuilding more code than necessary
- Fixes the biggest inconsistency between incremental and non-incremental builds
- Some code that previously compiled may now hit a dependency loop error

### Pointer Changes

- Pointers inside packed structs/unions: **forbidden**
- `[*c]` pointers: behavior unchanged

## Removed Features

### `std.builtin.subsystem`

Removed — subsystem detection was flaky and not needed at compile time. The actual subsystem is only known at link time.

**Alternative:** Determine at runtime if needed.

### `std.Target.SubSystem`

Moved to `std.zig.SubSystem`. Old location kept as deprecated alias.

### `ucontext_t` and Related

Removed from standard library. Deprecated in POSIX, not available in musl.

## Renamed APIs

| Old | New |
|-----|-----|
| `std.mem.trimLeft` | `std.mem.trimStart` |
| `std.mem.trimRight` | `std.mem.trimEnd` |
| `std.process.getCwd` | `std.process.currentPath` |
| `std.process.getCwdAlloc` | `std.process.currentPathAlloc` |
| `std.Thread.Pool` | Removed (use `std.Io.Group` + `Io.async`) |

## New Standard Library APIs

### Debug Information

```zig
// Capture stack trace
pub fn captureCurrentStackTrace(options: StackUnwindOptions) StackTrace

// Write stack trace
pub fn writeStackTrace(st: *const StackTrace, t: Io.Terminal) !void

// Dump to stderr
pub fn dumpStackTrace(st: *const StackTrace) void
```

### Memory Locking

```zig
// Old
try std.posix.mlock();
try std.posix.mlock2(slice, std.posix.MLOCK_ONFAULT);
try std.posix.mlockall(slice, std.posix.MCL_CURRENT | std.posix.MCL_FUTURE);

// New
try std.process.lockMemory(slice, .{});
try std.process.lockMemory(slice, .{ .on_fault = true });
try std.process.lockMemoryAll(.{ .current = true, .future = true });
```

### Cryptography Additions

- `std.crypto.aes_siv` — AES-SIV (nonce-reuse resistant)
- `std.crypto.aes_gcm_siv` — AES-GCM-SIV (nonce-reuse resistant, good for embedded)
- `std.crypto.ascon` — Ascon-AEAD, Ascon-Hash, Ascon-CHash (NIST SP 800-232)

### Compression

- `std.compress.zstd` — Zstandard support added alongside gzip/zlib/deflate

### Windows

- Networking via direct AFD access (no ws2_32.dll)
- Inter-process progress reporting
- All stdlib functionality now based on NtDll syscalls

## Format Specifiers

| Old | New |
|-----|-----|
| `{D}` (duration) | `{f}` with `std.Io.Duration{ .nanoseconds = ns }` |

## Allocator Changes

| Old | New |
|-----|-----|
| `std.heap.GeneralPurposeAllocator` | `std.heap.DebugAllocator` |
| `GeneralPurposeAllocatorConfig` | `DebugAllocatorConfig` |

Old names kept as deprecated aliases.

## Thread Changes

`std.Thread.Pool` removed entirely. Use:

```zig
// Old
thread_pool.spawnWg(wg, func, .{args});

// New
var future = io.async(func, .{args});
defer if (future.cancel(io)) |r| r.deinit() else |_| {};
```

## Environment Variables & Args

No longer global. Access through `std.process.Init`:

```zig
pub fn main(init: std.process.Init) !void {
    const env = init.environ_map;
    const args = try init.minimal.args.toSlice(init.arena.allocator());
}
```
