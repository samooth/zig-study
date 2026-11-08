# Language Reference

Zig language fundamentals for 0.16.x / 0.17.x.

## Builtins

### Type Construction (0.17 changes)

| Builtin | Purpose | Example |
|---------|---------|---------|
| `@typeInfo(T)` | Get type metadata | `@typeInfo(u32).int.signedness` |
| `@typeName(T)` | Type as string | `@typeName(u32)` → `"u32"` |
| `@as(T, value)` | Type coercion | `@as(u64, x)` |
| `@intCast(x)` | Integer cast | `@intCast(big_num)` |
| `@floatCast(x)` | Float cast | `@floatCast(f)` |
| `@bitCast(x)` | Bit reinterpret | `@bitCast(bytes)` |
| `@truncate(x)` | Truncate integer | `@truncate(big)` |
| `@alignCast(x)` | Align pointer | `@alignCast(ptr)` |
| `@ptrCast(x)` | Pointer cast | `@ptrCast(raw)` |
| `@volatileCast(x)` | Volatile cast | `@volatileCast(ptr)` |
| `@enumFromInt(x)` | Int to enum (all versions) | `@enumFromInt(raw)` |
| `@fromBackingInt(x)` | Int to enum (added 0.17) | `@fromBackingInt(@intCast(raw))` |
| `@intFromEnum(e)` | Enum to int (all versions) | `@intFromEnum(tag)` |
| `@backingInt(e)` | Enum to int (added 0.17) | `@backingInt(tag)` |
| `@intFromPtr(p)` | Pointer to int | `@intFromPtr(ptr)` |
| `@ptrFromInt(i)` | Int to pointer | `@ptrFromInt(addr)` |
| `@fieldParentPtr(name, ptr)` | Container field parent | `@fieldParentPtr("field", ptr)` |
| `@embedFile(path)` | Embed file at comptime | `@embedFile("data.txt")` |
| `@import(name)` | Import module | `@import("std")` |
| `@compileError(msg)` | Compile-time error | `@compileError("unsupported")` |
| `@compileLog(vals...)` | Compile-time debug | `@compileLog(x)` |
| `@panic(msg)` | Runtime panic | `@panic("unreachable")` |
| `@breakpoint()` | Debug breakpoint | `@breakpoint()` |
| `@returnAddress()` | Return address | `@returnAddress()` |
| `@src()` | Source location | `@src()` |
| `@tagName(e)` | Enum tag name | `@tagName(tag)` |
| `@errorName(e)` | Error name | `@errorName(err)` |
| `@unionInit(U, tag, val)` | Init tagged union | `@unionInit(MyUnion, .tag, val)` |
| `@call(.auto, fn, args)` | Call function | `@call(.auto, func, .{a, b})` |
| `@hasField(T, name)` | Check field exists | `@hasField(MyStruct, "x")` |
| `@hasDecl(T, name)` | Check decl exists | `@hasDecl(MyModule, "foo")` |
| `@sizeOf(T)` | Type size in bytes | `@sizeOf(u32)` → `4` |
| `@alignOf(T)` | Type alignment | `@alignOf(u32)` |
| `@offsetOf(T, field)` | Field offset | `@offsetOf(MyStruct, "x")` |
| `@bitSizeOf(T)` | Bit size | `@bitSizeOf(u32)` → `32` |
| `@minValue(T)` | Min value | `@minValue(i8)` → `-128` |
| `@maxValue(T)` | Max value | `@maxValue(u8)` → `255` |
| `@splat(x)` | Scalar to vector | `@splat(@as(@Vector(4, f32), 1.0))` |
| `@reduce(op, vec)` | Vector reduce | `@reduce(.Add, vec)` |
| `@shuffle(vec, a, b, mask)` | Vector shuffle | `@shuffle(f32, a, b, [4]i32{0,1,2,3})` |
| `@select(T, pred, a, b)` | Vector select | `@select(f32, mask, a, b)` |
| `@Vector(len, T)` | SIMD vector type | `@Vector(4, f32)` |
| `@Tuple(types)` | Tuple type (0.16+) | `@Tuple(&.{ u32, bool })` |
| `@inComptime()` | Check comptime ctx | `if (@inComptime()) ...` |
| `@typeInfo(T).@"union"` | Access union info | Pattern: `@"enum"`, `@"struct"`, etc. |

### @typeInfo Structures (0.17 restructured)

```zig
// Pointer — attrs nested
info.Pointer.attrs.@"const"
info.Pointer.attrs.@"volatile"
info.Pointer.attrs.@"align"
info.Pointer.attrs.@"addrspace"
info.Pointer.attrs.@"allowzero"

// Struct — flat field arrays
info.Struct.field_names    // []const [:0]const u8
info.Struct.field_types    // []const type
info.Struct.field_attrs    // []const FieldAttributes
info.Struct.decl_names     // []const [:0]const u8

// Enum — mode replaces is_exhaustive
info.Enum.field_names
info.Enum.field_values
info.Enum.mode             // .exhaustive | .nonexhaustive

// Fn — attrs nested
info.Fn.attrs.@"callconv"
info.Fn.attrs.varargs
info.Fn.param_types        // []const ?type
info.Fn.param_attrs        // []const ParamAttributes

// Union
info.Union.field_names
info.Union.field_types
info.Union.field_attrs
info.Union.decl_names

// Opaque
info.Opaque.decl_names     // []const [:0]const u8

// ErrorSet
info.ErrorSet.error_names  // ?[]const [:0]const u8
```

## Syntax

### Labeled Blocks

```zig
const result = result: {
    const x = try compute();
    break :result x;
};
```

### Labeled Switch

```zig
const x: enum { a, b, c } = .a;
const val = switch (x) {
    inline .a, .b, .c => |tag| @intFromEnum(tag),
};
```

### Packed Structs

```zig
const Flags = packed struct {
    read: bool = false,
    write: bool = false,
    execute: bool = false,
    _: u5 = 0,
};
// Pointers forbidden inside packed structs (0.16+)
```

### Error Sets

```zig
const MyError = error{ NotFound, PermissionDenied, OutOfMemory };
// Cannot reify error sets with @Type (0.16+)
```

### Sentinel-Terminated Types

```zig
const slice: [:0]const u8 = "hello";  // null-terminated
const arr: [5:0]u8 = "hello";         // sentinel-terminated array
```

## Control Flow

### errdefer

```zig
fn create() !Resource {
    var r = try alloc(Resource);
    errdefer r.deinit(); // only runs if function returns error
    try r.init();
    return r;
}
```

### defer with capture

```zig
var file = try open(path);
defer file.close(); // always runs
```

### Inline for

```zig
inline for (.{ u8, u16, u32 }) |T| {
    // unrolled at comptime
}
```

## Comptime

```zig
// Comptime function
fn fibonacci(comptime n: comptime_int) comptime_int {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
const result = fibonacci(10); // computed at compile time

// Comptime block
comptime {
    // code that runs at compile time
    _ = @import("some_file.zig"); // force discovery
}
```

## Memory Model

- All allocations take an explicit `Allocator` parameter
- `defer` for unconditional cleanup, `errdefer` for error-only cleanup
- No garbage collection, no reference counting
- Arena allocators for batch allocation patterns

## Error Handling

```zig
// Propagate
try riskyOperation();

// Catch and handle
const val = riskyOperation() catch |err| switch (err) {
    error.OutOfMemory => return err,
    error.NotFound => null,
};

// Catch and replace
const val = riskyOperation() catch 0;
```
