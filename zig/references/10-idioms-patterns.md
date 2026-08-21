# Idioms & Patterns

Common Zig patterns and best practices for 0.16+/0.17+.

## Error Handling

### errdefer Pattern

```zig
fn createResource(alloc: std.mem.Allocator) !Resource {
    var r = Resource{};
    r.data = try alloc.alloc(u8, 100);
    errdefer alloc.free(r.data);
    r.handle = try openHandle();
    errdefer closeHandle(r.handle);
    return r; // both cleanups skipped on success
}
```

### Error Return Trace

```zig
// Errors propagate with full traces
try riskyOperation(); // trace shows call chain on failure
```

## Deferred Cleanup

```zig
// Always runs
var file = try open(path);
defer file.close();

// Only on error
var resource = try create();
errdefer resource.deinit();
try use(resource); // if this fails, resource is cleaned up
```

## Comptime Patterns

### Comptime Table

```zig
const Table = comptime {
    var t: [256]u8 = undefined;
    for (&t, 0..) |*byte, i| {
        byte.* = @intCast((i * 7 + 3) % 256);
    }
    break :t t;
};
```

### Comptime String Map

```zig
const map = std.StaticStringMap(Opcode).initComptime(.{
    .{ "ADD", .add },
    .{ "SUB", .sub },
    .{ "MUL", .mul },
});
```

### Generic Function

```zig
fn max(comptime T: type, a: T, b: T) T {
    return if (a > b) a else b;
}
```

## ArrayList Pattern

```zig
var list = std.ArrayList(MyStruct).empty;
defer list.deinit(allocator);

for (input) |item| {
    try list.append(allocator, try transform(item));
}

const owned = try list.toOwnedSlice(allocator);
defer allocator.free(owned);
```

## HashMap Pattern

```zig
var map = std.StringHashMap(usize).empty;
defer map.deinit(allocator);

for (items, 0..) |item, idx| {
    try map.put(allocator, item.name, idx);
}

if (map.getPtr("key")) |ptr| {
    ptr.* += 1; // modify in place
}
```

## JSON Pattern

```zig
const Config = struct {
    name: []const u8,
    version: u32,
    enabled: bool,
};

const parsed = try std.json.parseFromSlice(Config, allocator, json_bytes, .{});
defer parsed.deinit();
const config = parsed.value;
```

## File I/O Pattern

```zig
fn readFile(io: std.Io, path: []const u8, alloc: std.mem.Allocator) ![]u8 {
    const file = try std.Io.Dir.cwd().openFile(io, path, .{});
    defer file.close(io);
    var reader = file.reader(io, &.{});
    return try reader.interface.allocRemaining(alloc, .limited(1_000_000));
}
```

## Testing Pattern

```zig
const std = @import("std");

test "feature X" {
    const io = std.testing.io;
    const alloc = std.testing.allocator;

    const result = try myFunction(io, alloc, 42);
    defer alloc.free(result);

    try std.testing.expectEqual(@as(usize, 10), result.len);
}

test "error case" {
    const io = std.testing.io;
    const result = myFunction(io, undefined, -1);
    try std.testing.expectError(error.InvalidInput, result);
}
```

## Switch Pattern

```zig
const value = switch (tag) {
    .a => 1,
    .b => 2,
    .c => |c| blk: {
        // complex computation
        break :blk compute(c);
    },
    else => unreachable,
};
```

## Optional Pattern

```zig
fn find(haystack: []const u8, needle: u8) ?usize {
    for (haystack, 0..) |byte, idx| {
        if (byte == needle) return idx;
    }
    return null;
}

// Usage
if (find(data, '\n')) |idx| {
    processLine(data[0..idx]);
}
```

## Pointer Safety

```zig
// Slices are fat pointers (ptr + len)
const slice: []const u8 = "hello";

// Single-item pointers
const ptr: *const u32 = &value;

// Many-item pointers
const many: [*]const u8 = slice.ptr;

// C pointers
const c_ptr: [*c]const u8 = @ptrCast(ptr);
```

## Format Strings

```zig
const std = @import("std");

// Basic
std.debug.print("value: {}\n", .{42});
std.debug.print("string: {s}\n", .{"hello"});
std.debug.print("float: {d:.2}\n", .{3.14});

// Writer
try writer.print(io, "item: {}\n", .{item});

// Duration (0.16+)
try writer.print(io, "took {f}\n", .{std.Io.Duration{ .nanoseconds = 1234567 }});
```

## Thread Pattern

```zig
const thread = try std.Thread.spawn(.{}, myFunc, .{arg});
defer thread.join();
```

## Build.zig Idioms

### Conditional Compilation

```zig
if (target.result.os.tag == .linux) {
    exe.root_module.linkSystemLibrary("epoll", .{});
}
```

### Feature Detection

```zig
const use_thing = b.option(bool, "use_thing", "Enable thing") orelse false;
if (use_thing) {
    exe.root_module.addCMacro("USE_THING", "1");
}
```
