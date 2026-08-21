# Allocator Reference

Memory allocators and patterns in Zig 0.16+/0.17+.

## Allocator Types

| Allocator | Use Case | Thread-safe | Notes |
|-----------|----------|-------------|-------|
| `SafeAllocator` (0.17) | General purpose, debug | Yes | Was `DebugAllocator` (0.16), `GeneralPurposeAllocator` (0.15) |
| `DebugAllocator` (0.16) | General purpose, debug | Yes | Renamed from GPA |
| `ArenaAllocator` | Batch allocation, process lifetime | No | One `deinit` frees everything |
| `SmpAllocator` | High-throughput allocation | Yes | SMP-optimized |
| `FixedBufferAllocator` | Stack/buffer allocation | No | No heap allocation |
| `PageAllocator` | OS page allocation | Yes | Low-level |
| `BufferFirstAllocator` | Try buffer first, fallback | No | Optimization |
| `MemoryPool(T)` | Single-type pool | No | Faster than general purpose |

## Juicy Main Allocators

```zig
pub fn main(init: std.process.Init) !void {
    // Debug-safe allocator (leak checking in debug mode)
    const gpa = init.gpa;

    // Process-lifetime arena (all freed on exit)
    const arena = init.arena;
    const alloc = arena.allocator();

    // Environment and args (already initialized)
    const env = init.environ_map;
    const args = try init.minimal.args.toSlice(alloc);
}
```

## Common Patterns

### Arena for Temporary Work

```zig
fn processFile(gpa: std.mem.Allocator, path: []const u8) !void {
    var arena = std.heap.ArenaAllocator.init(gpa);
    defer arena.deinit();
    const alloc = arena.allocator();

    // All these allocations freed at once
    const data = try alloc.dupe(u8, path);
    const lines = try alloc.split(u8, data, "\n");
    _ = lines;
}
```

### Fixed Buffer

```zig
var buf: [1024]u8 = undefined;
var fba = std.heap.FixedBufferAllocator.init(&buf);
const alloc = fba.allocator();
const s = try alloc.dupe(u8, "hello");
```

### ArrayList with Allocator

```zig
var list = std.ArrayList(u32).empty;
defer list.deinit(allocator);

try list.append(allocator, 42);
try list.appendSlice(allocator, &.{ 1, 2, 3 });
const owned = try list.toOwnedSlice(allocator);
defer allocator.free(owned);
```

### HashMap with Allocator

```zig
var map = std.StringHashMap(u32).empty;
defer map.deinit(allocator);

try map.put(allocator, "key", 42);
if (map.get("key")) |val| {
    // use val
}
```

## Error Handling

```zig
// Allocation failure is an error
const buf = try alloc.alloc(u8, 1024);
defer alloc.free(buf);

// Or catch
const buf = alloc.alloc(u8, 1024) catch |err| switch (err) {
    error.OutOfMemory => return err,
};
```

## Thread Safety

- `gpa` from `Init` is thread-safe
- `ArenaAllocator` is NOT thread-safe
- `FixedBufferAllocator` is NOT thread-safe
- Use `ThreadSafeAllocator` wrapper if needed

## DebugAllocator / SafeAllocator Config

```zig
// 0.16
var gpa = std.heap.DebugAllocator{
    .never_unmap = true,
    .retain_metadata = true,
};

// 0.17
var gpa = std.heap.SafeAllocator{
    // options...
};
```

## Memory Ownership Rules

1. Functions that allocate memory have an `Alloc` suffix or take an explicit `Allocator`
2. The caller owns memory and must free it
3. Use `defer` or `errdefer` for cleanup
4. Arena allocators simplify ownership: one `deinit` frees all

## Performance Warning

`DebugAllocator` / `SafeAllocator` can be **up to 1400x slower** than page_allocator for allocator-heavy workloads in Debug mode. Always profile:

```bash
time ./your-tool <real-input>
```
