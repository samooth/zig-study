# Zig 0.16.0 — I/O as an Interface (`std.Io`)

## Overview

`std.Io` is a vtable-based abstraction that unifies ALL I/O operations behind a single interface. This is the biggest architectural change in Zig 0.16.0.

**Source:** `<zig-install-dir>/lib/std/Io.zig` (3461 lines)

## Architecture

```
std.Io
├── VTable (manual dispatch)
│   ├── async / concurrent / await / cancel
│   ├── groupAsync / groupConcurrent / groupAwait / groupCancel
│   ├── select / recancel / swapCancelProtection / checkCancel
│   ├── File operations (open, read, write, seek, stat, lock)
│   ├── Dir operations (open, create, delete, walk, read)
│   ├── Net operations (tcp, udp, dns, listen, connect)
│   ├── Process (spawn, currentPath, kill, wait)
│   ├── Time (now, sleep, resolution)
│   ├── Random (random, randomSecure)
│   └── Synchronization (futex, event, condition, semaphore)
│
├── Backends
│   ├── Uring (Linux x86_64/aarch64)
│   ├── Kqueue (BSD/macOS x86_64/aarch64)
│   └── Threaded (thread-pool fallback, ~19K lines)
│
└── Sub-types
    ├── Reader / Writer
    ├── Dir / File
    ├── net (TCP/UDP/Unix/DNS)
    ├── Terminal
    ├── RwLock / Semaphore
    ├── Future(R) / Batch / Group / Select
    ├── Mutex / Condition / Event
    ├── Clock / Timestamp / Duration / Timeout
    └── Io.File.MemoryMap
```

## Core Type

```zig
pub const Io = struct {
    userdata: ?*anyopaque,
    vtable: *const VTable,
};
```

All operations go through `io.vtable.xxx(io.userdata, ...)`.

## Key Concepts

### Future(R)

Represents an in-progress async operation:

```zig
pub fn Future(comptime R: type) type {
    return struct {
        // ...
        pub fn await(self: *Future(R), io: Io) R { ... }
        pub fn cancel(self: *Future(R), io: Io) R { ... }
    };
}
```

### Cancellation

Most I/O operations include `error.Canceled` in their error sets. Pattern:

```zig
var file_task = io.async(Io.Dir.openFile, .{ .cwd(), io, "hello.txt", .{} });
defer file_task.await(io).close(io);
```

### Groups

O(1) overhead for spawning N tasks with shared lifetime:

```zig
var group: Io.Group = .init;

group.async(io, taskA, .{arg1});
try group.concurrent(io, taskB, .{arg2});
try group.await(io);
```

### Batch

For operations that don't need shared lifetime — lighter than Group.

### Select

Block until one of multiple futures completes:

```zig
const Union = union(enum) { a: FutureA, b: FutureB };
var buffer: [2]Union = undefined;
var sel = Io.Select(Union).init(io, &buffer);
sel.async(.a, futureA, .{});
sel.async(.b, futureB, .{});
const result = try sel.await();
```

## Subsystems

### File System

| Old (0.15.x) | New (0.16.0) |
|---------------|--------------|
| `std.fs.cwd()` | `std.Io.Dir.cwd()` |
| `std.fs.openFile(path, flags)` | `Io.Dir.openFile(io, path, flags)` |
| `file.reader()` | `file.reader(io, &.{})` |
| `file.writer()` | `file.writer(io, &.{})` |
| `std.fsDir.readFileAlloc(...)` | `Io.Dir.cwd().readFileAlloc(io, path, alloc, Io.Limit.limited(n))` |
| `std.fs.path` | `std.Io.Dir.path` |

### Networking

| Old | New |
|-----|-----|
| `std.net.tcpConnect(...)` | `Io.net.tcpConnect(io, addr)` |
| `std.net.Address.resolveIp(...)` | `Io.net.Address.resolveIp(...)` |
| `std.net.Server` | `Io.net.Server` |

### Time

| Old | New |
|-----|-----|
| `std.time.Instant` | `std.Io.Timestamp` |
| `std.time.Timer` | `std.Io.Timestamp` |
| `std.time.timestamp()` | `Io.Timestamp.now(io, .real)` |
| `std.time.sleep(ns)` | `io.sleep(timeout, .real)` |

### Randomness

| Old | New |
|-----|-----|
| `std.crypto.random.bytes(buf)` | `io.random(buf)` |
| `std.crypto.random.int(u64)` | `io.random.int(u64)` |
| CSPRNG via Io | `Io.randomSecure(io, buf)` |

### Process

| Old | New |
|-----|-----|
| `std.process.Child` | `std.process.Child` (now Io-based) |
| `child.stdin` | `child.stdin` is now `?Io.File` |
| `std.process.getCwd(buf)` | `std.process.currentPath(io, buf)` |

## Io Backends

### Uring (Linux)

- Available on x86_64 and aarch64 Linux
- True io_uring-based async I/O
- Lowest latency for Linux

### Kqueue (BSD/macOS)

- Available on x86_64 and aarch64 for: DragonFly, FreeBSD, NetBSD, OpenBSD, macOS, iOS, tvOS, watchOS, visionOS
- Uses kqueue for event notification

### Threaded (Fallback)

- Thread-pool based implementation
- Available on all platforms
- ~19,000 lines of code
- Uses `Io.async` / `Io.concurrent` for concurrency

## Testing

```zig
const std = @import("std");

test "io operations" {
    const io = std.testing.io;
    // Use io for all I/O operations in tests
    var reader: std.Io.Reader = .fixed("hello");
    _ = reader;
}
```

`std.testing.io` provides a global `Io` instance for test code.

## Migration Notes

1. Functions that previously used global state now take `Io` as first parameter
2. `std.io` (lowercase) → `std.Io` (uppercase)
3. `std.Io.GenericReader` → `std.Io.Reader`
4. `std.Io.AnyReader` → `std.Io.Reader`
5. `std.io.fixedBufferStream(data)` → `std.Io.Reader.fixed(data)` or `std.Io.Writer.fixed(buffer)`
6. `{D}` format specifier → `std.Io.Duration{ .nanoseconds = ns }` with `{f}`
