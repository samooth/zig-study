# Process Reference

Process management in Zig 0.16+/0.17+.

## Juicy Main (std.process.Init)

The recommended entry point:

```zig
pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;           // DebugAllocator / SafeAllocator
    const io = init.io;             // Default Io implementation
    const arena = init.arena;       // ArenaAllocator (process-lifetime)
    const environ = init.environ_map;
    const preopens = init.preopens;

    // Minimal init (just environ + args)
    const minimal = init.minimal;
    const args = try minimal.args.toSlice(arena.allocator());
    _ = args;
}
```

### Init Fields

| Field | Type | Description |
|-------|------|-------------|
| `minimal` | `Init.Minimal` | Just environ + args |
| `arena` | `*ArenaAllocator` | Process-lifetime allocator |
| `gpa` | `Allocator` | Debug-safe allocator |
| `io` | `Io` | Default I/O implementation |
| `environ_map` | `*Environ.Map` | Environment variables |
| `preopens` | `Preopens` | Pre-opened file descriptors |

## Spawning Child Processes

```zig
// Simple spawn
const child = try std.process.spawn(io, .{
    .argv = &.{ "ls", "-la" },
    .cwd = "/tmp",
});
const term = try child.wait(io);
switch (term) {
    .exited => |code| {
        if (code != 0) return error.ProcessFailed;
    },
    .signal => |sig| {
        return error.ProcessSignaled;
    },
    else => return error.ProcessAbnormal,
}

// Spawn with captured output
const child = try std.process.spawn(io, .{
    .argv = &.{ "echo", "hello" },
    .stdout_behavior = .pipe,
});
defer child.kill(io);
const stdout = child.stdout.?.reader(io, &.{});
const output = try stdout.interface.allocRemaining(allocator, .limited(1024));
defer allocator.free(output);
```

## Child Process Handle

```zig
pub const Child = struct {
    stdin: ?Io.File,
    stdout: ?Io.File,
    stderr: ?Io.File,

    pub fn wait(self: *Child, io: Io) WaitError!Term { ... }
    pub fn kill(self: *Child, io: Io) void { ... }
    pub fnTERM(self: *Child, io: Io) void { ... }
};
```

## Environment Variables

```zig
// Via Init
const env = init.environ_map;

// Check if key exists
if (env.contains(arena, "HOME")) |exists| {
    _ = exists;
}

// Get value
if (env.get("PATH")) |path| {
    // path is []const u8
}

// Iterate
var iter = env.iterator();
while (iter.next()) |entry| {
    // entry.key, entry.value
}
```

## Command Line Arguments

```zig
// Via Init
const args = try init.minimal.args.toSlice(arena.allocator());

// args is a slice of [:0]const u8
for (args) |arg| {
    // arg is null-terminated
}
```

## Current Directory

```zig
// Get
var buf: [std.Io.Dir.max_path_bytes]u8 = undefined;
const len = try std.process.currentPath(io, &buf);
const cwd = buf[0..len];

// Set
try std.process.setCurrentPath(io, "/tmp");
```

## Executable Path

```zig
var buf: [std.Io.Dir.max_path_bytes]u8 = undefined;
const len = try std.process.executablePath(io, &buf);
const path = buf[0..len];
```

## Replace Process

```zig
// Replace current process image
try std.process.replace(io, .{
    .argv = &.{ "/bin/sh", "-c", "echo hello" },
});
// Does not return on success
```

## Exit / Abort

```zig
std.process.exit(0);    // exit with code
std.process.abort();    // abort with core dump
```

## WASI Preopens

```zig
const preopens = try std.process.Preopens.init(arena);
// preopens provides access to pre-opened directories
```

## User Info (POSIX)

```zig
const info = try std.process.getUserInfo(io, "username");
// info.uid, info.gid
```

## Memory Locking (0.16+)

```zig
// Lock memory
try std.process.lockMemory(slice, .{});
try std.process.lockMemory(slice, .{ .on_fault = true });

// Lock all
try std.process.lockMemoryAll(.{ .current = true, .future = true });
```
