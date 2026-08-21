# Zig 0.17.0 — Standard Library Changes

What's new, removed, and renamed in the 0.17.0 standard library compared to 0.16.0.

## New Modules

### `std.lang` (replaces `std.builtin`)

The language-provided types and constants have a new home:

```zig
// 0.17.0
pub const lang = @import("lang.zig");
pub const builtin = lang; // deprecated alias
```

Contains: `StackTrace`, `GlobalLinkage`, `SymbolVisibility`, `AtomicOrder`, `ReduceOp`, `AtomicRmwOp`, `Optimize` (was `OptimizeMode`), `Type` (restructured), `CallingConvention`, `LinkMode`, `SubSystem`, etc.

### `std.spirv` (replaces `std.gpu`)

Expanded SPIR-V GPU intrinsics module:

```zig
// Built-in variables
pub const position_in: *addrspace(.input) @Vector(4, f32)
pub const frag_coord: @Vector(4, f32) addrspace(.input)
pub const global_invocation_id: @Vector(3, u32) addrspace(.input)
// ... more builtins

// Synchronization
pub const Scope = enum(u32) { cross_device, device, workgroup, subgroup, invocation, ... };
pub const MemorySemantics = packed struct(u32) { acquire, release, ... };
pub fn controlBarrier(execution, memory, semantics) void
pub fn memoryBarrier(memory, semantics) void
pub fn workgroupBarrier() void

// Specialization constants
pub fn specConst(comptime T: type, comptime id: u32, comptime default: T) T

// Image operations
pub fn imageSampleImplicitLod(...)
pub fn imageQuerySize(...)
pub fn imageWrite(...)
```

### `std.Io.Dispatch` (new macOS backend)

Grand Central Dispatch backend for macOS/iOS:

```zig
pub const Dispatch = @import("Io/Dispatch.zig");
// Used automatically on macOS/iOS instead of Kqueue
```

### `std.Io.fiber` (new fiber support)

Low-level fiber/context switching primitives:

```zig
pub const supported = switch (builtin.cpu.arch) {
    .aarch64, .riscv64, .x86_64 => true,
    else => false,
};
pub const Context = extern struct { sp, fp, pc: u64 };
pub const Switch = extern struct { old: *Context, new: *Context };
pub inline fn contextSwitch(s: *const Switch) *const Switch
```

### `std.ascii` (new module)

Dedicated ASCII character handling:

```zig
pub const lowercase = "abcdefghijklmnopqrstuvwxyz";
pub const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
pub const letters = lowercase ++ uppercase;
pub const control_code = struct { pub const nul = 0x00; pub const bel = 0x07; ... };

pub fn isAlphanumeric(c: u8) bool
pub fn isControl(c: u8) bool
pub fn isWhitespace(c: u8) bool
pub fn toLowercase(c: u8) u8
pub fn toUppercase(c: u8) u8
// ... more classification and conversion functions
```

### `std.Io.Uring` (renamed from `IoUring`)

```zig
// 0.16.0
pub const IoUring = @import("Io/IoUring.zig");

// 0.17.0
pub const Uring = @import("Io/Uring.zig");
```

### `std.heap.SafeAllocator` (new, replaces `DebugAllocator`)

```zig
// 0.16.0
pub const DebugAllocator = @import("heap/debug_allocator.zig").DebugAllocator;

// 0.17.0
pub const SafeAllocator = @import("heap/SafeAllocator.zig");
pub const DebugAllocator = SafeAllocator; // deprecated alias
```

### `std.heap.BrkAllocator` (new)

New allocator based on `brk` syscall:

```zig
pub const BrkAllocator = @import("heap/BrkAllocator.zig");
pub const WasmAllocator = if (builtin.single_threaded) BrkAllocator else @compileError("unimplemented");
```

### `std.heap.BufferFirstAllocator` (new)

```zig
pub const BufferFirstAllocator = @import("heap/BufferFirstAllocator.zig");
```

## Removed Modules

| Module | Replacement |
|--------|-------------|
| `std.builtin` (as primary) | `std.lang` (builtin kept as deprecated alias) |
| `std.gpu` | `std.spirv` |
| `std.heap.StackFallbackAllocator` | Use `SmpAllocator` or manual approach |
| `std.heap.SbrkAllocator` | `std.heap.BrkAllocator` (renamed) |
| `std.heap.WasmAllocator` (standalone) | Now conditionally `BrkAllocator` on single-threaded |
| `std.heap.ThreadSafeAllocator` | Use `SafeAllocator` |

## Renamed Files

| Old Path | New Path |
|----------|----------|
| `builtin.zig` | `lang.zig` |
| `builtin/` | `lang/` |
| `builtin/assembly.zig` | `lang/assembly.zig` |
| `gpu.zig` | `spirv.zig` |
| `Io/IoUring.zig` | `Io/Uring.zig` |
| `heap/SmpAllocator.zig` | `heap/SmpAllocator.zig` (unchanged) |
| `heap/arena_allocator.zig` | `heap/ArenaAllocator.zig` (capitalized) |

## Io VTable Changes

New entry in the VTable:

```zig
pub const VTable = struct {
    crashHandler: *const fn (?*anyopaque) void,  // NEW
    async: ...,
    concurrent: ...,
    // ... rest unchanged
};
```

## Io Evented Backend Changes

```zig
// 0.16.0
pub const Evented = switch (builtin.os.tag) {
    .linux => IoUring,
    .dragonfly, .freebsd, .netbsd, .openbsd, .driverkit, .ios, .macos, ... => Kqueue,
    else => void,
};

// 0.17.0
pub const Evented = if (fiber.supported) switch (builtin.os.tag) {
    .linux => Uring,
    .dragonfly, .freebsd, .netbsd, .openbsd => Kqueue,
    .driverkit, .ios, .macos, .tvos, .visionos, .watchos => Dispatch,
    else => void,
} else void;
```

Key changes:
- macOS/iOS now use `Dispatch` (Grand Central Dispatch) instead of `Kqueue`
- `fiber.supported` gate (aarch64, riscv64, x86_64 only)
- BSD systems still use `Kqueue`

## Options Changes

New options in `std.Options`:

```zig
pub const Options = struct {
    // ... existing options ...
    networking: bool = true,  // NEW: disable networking in Io
    // ... 
};
```

## Deprecated Names (kept as aliases)

| Old Name | New Name |
|----------|----------|
| `std.builtin` | `std.lang` |
| `std.builtin.OptimizeMode` | `std.lang.Optimize` |
| `std.heap.DebugAllocator` | `std.heap.SafeAllocator` |
| `std.heap.DebugAllocatorConfig` | `std.heap.SafeAllocator.Options` |
| `std.Io.IoUring` | `std.Io.Uring` |
| `std.ArrayListUnmanaged` | `std.ArrayList` |
| `std.bit_set.StaticBitSet` | `std.bit_set.Static` |
| `std.bit_set.DynamicBitSet` | `std.bit_set.DynamicManaged` |
| `std.bit_set.DynamicBitSetUnmanaged` | `std.bit_set.Dynamic` |
| `std.ArrayHashMapUnmanaged` | `std.array_hash_map.Custom` |
| `std.AutoArrayHashMapUnmanaged` | `std.array_hash_map.Auto` |
| `std.StringArrayHashMapUnmanaged` | `std.array_hash_map.String` |
