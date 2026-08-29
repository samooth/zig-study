# std.Io Reference

The central I/O abstraction in Zig 0.16+/0.17+. All I/O goes through `std.Io`.

## Architecture

```zig
pub const Io = struct {
    userdata: ?*anyopaque,
    vtable: *const VTable,
};
```

All operations dispatch through `io.vtable.xxx(io.userdata, ...)`.

## Key Types

| Type | Purpose |
|------|---------|
| `Io` | Central I/O interface |
| `Io.File` | File handle |
| `Io.Dir` | Directory handle |
| `Io.Reader` | Generic byte reader |
| `Io.Writer` | Generic byte writer |
| `Io.Terminal` | Terminal/ANSI handling |
| `Io.net` | TCP/UDP/Unix networking |
| `Io.Timestamp` | Point in time (was `std.time.Instant`) |
| `Io.Duration` | Time duration |
| `Io.Timeout` | Union of none/duration/deadline |
| `Io.Clock` | Clock type (real/awake/boot/cpu) |
| `Io.Future(R)` | Async operation handle |
| `Io.Batch` | Batched I/O operations |
| `Io.Group` | Task group with shared lifetime |
| `Io.Select(U)` | Select on multiple futures |
| `Io.Mutex` | Mutex |
| `Io.Condition` | Condition variable |
| `Io.RwLock` | Reader-writer lock |
| `Io.Semaphore` | Semaphore |

## File Operations

```zig
// Open
const file = try std.Io.Dir.cwd().openFile(io, "path", .{});
defer file.close(io);

// Create
const file = try std.Io.Dir.cwd().createFile(io, "path", .{});
defer file.close(io);

// Read into buffer
var buf: [1024]u8 = undefined;
const n = try file.read(io, &buf);

// Write
try file.writeAll(io, "hello world");

// Seek
try file.seekTo(io, 0);
try file.seekBy(io, -5);

// Stat
const stat = try file.stat(io);

// Lock
try file.lock(io, .shared);
defer file.unlock(io);

// Memory map
const mm = try file.memoryMap(io, .{});
defer mm.destroy(io);
```

## Reader / Writer

```zig
// Reader from fixed buffer
var reader: std.Io.Reader = .fixed("hello world");
const byte = try reader.takeByte(io);

// Reader from file
var file_reader = file.reader(io, &.{});
const contents = try file_reader.interface.allocRemaining(allocator, .limited(1024));

// Writer to fixed buffer
var writer: std.Io.Writer = .fixed(buffer);
try writer.writeAll(io, "hello");
try writer.print(io, "value: {}", .{42});

// Writer to file
var file_writer = file.writer(io, &.{});
try file_writer.interface.writeAll(io, "data");
```

## Directory Operations

```zig
const dir = std.Io.Dir.cwd();

// Open subdirectory
const sub = try dir.openDir(io, "subdir", .{});
defer sub.close(io);

// Create directory
try dir.createDir(io, "new_dir", .{});

// Delete
try dir.deleteFile(io, "file.txt");
try dir.deleteDir(io, "empty_dir");

// Walk
var walker = try dir.walk(allocator);
defer walker.deinit();
while (try walker.next(io)) |entry| {
    // entry.path, entry.kind, entry.dir
}

// Read directory entries
var iter = try dir.iterate(io);
while (try iter.next()) |entry| {
    // entry.name, entry.kind
}

// Stat
const stat = try dir.statFile(io, "file.txt");

// Rename
try dir.rename(io, "old.txt", "new.txt");

// Symlink
try dir.symLink(io, "target", "link", .{});

// Read link
var buf: [std.Io.Dir.max_path_bytes]u8 = undefined;
const len = try dir.readLink(io, "link", &buf);
```

## Networking

```zig
// TCP connect
const stream = try std.Io.net.connect(&address, io, .{});
defer stream.close(io);

// TCP listen
const server = try std.Io.net.listen(&address, io, .{});
const conn = try server.accept(io);

// UDP
const socket = try std.Io.net.bind(&address, io, .{});

// DNS resolution (takes a port, no allocator)
const result = try std.Io.net.resolve(io, hostname, 0);
```

## Time

```zig
// Get current time
const now = io.now(.real);

// Sleep — takes a Timeout (union of .none/.duration/.deadline)
try io.sleep(.{ .duration = std.Io.Duration.fromSeconds(1) });
try io.sleep(.{ .duration = std.Io.Duration.fromMilliseconds(500) });

// Clock resolution
const res = try io.resolution(.real);

// Duration arithmetic
const later = std.Io.Timestamp.addDuration(now, duration);
const diff = std.Io.Timestamp.durationTo(now, later);
```

## Random

```zig
// Fill buffer with random bytes
var buf: [32]u8 = undefined;
io.random(&buf);

// Secure random (CSPRNG)
var secure_buf: [32]u8 = undefined;
try io.randomSecure(&secure_buf);
```

## Async / Concurrency

```zig
// Async operation
var future = io.async(myFunction, .{arg1, arg2});
const result = future.await(io);

// Cancel
if (future.cancel(io)) |resource| resource.deinit() else |_| {};

// Group (shared lifetime)
var group = io.group();
defer group.deinit(io);
try group.spawn(io, taskA, .{});
try group.spawn(io, taskB, .{});
try group.wait(io);

// Select
const idx = try io.select(&.{ future_a, future_b });
```

## Backends

| Backend | Platform | Notes |
|---------|----------|-------|
| `Io.Uring` | Linux x86_64/aarch64 | io_uring-based |
| `Io.Kqueue` | BSD x86_64/aarch64 | kqueue-based |
| `Io.Dispatch` | macOS/iOS (0.17) | Grand Central Dispatch |
| `Io.Threaded` | All platforms | Thread-pool fallback |

## Testing

```zig
test "io operations" {
    const io = std.testing.io;
    // Use io for all I/O in tests
    var reader: std.Io.Reader = .fixed("test data");
    _ = reader;
}
```
