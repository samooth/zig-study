# Critical Patterns: WRONG → CORRECT

The top gotchas that cause compilation errors or wrong behavior in Zig 0.16+/0.17+.

## 1. Entry Point

```zig
// WRONG
pub fn main() !void { ... }

// CORRECT (0.16+)
pub fn main(init: std.process.Init) !void {
    const gpa = init.gpa;
    const io = init.io;
    const arena = init.arena;
}
```

## 2. Allocator Names

```zig
// WRONG (0.16+)
var gpa = std.heap.GeneralPurposeAllocator{};
// WRONG (0.17+)
var gpa = std.heap.DebugAllocator{};

// CORRECT (0.17+)
var gpa = std.heap.SafeAllocator{};
// CORRECT (0.16)
var gpa = std.heap.DebugAllocator{};
```

## 3. Container Initialization

```zig
// WRONG
var list = std.ArrayList(u8){};
var map = std.StringHashMap(u32){};
var queue = std.PriorityQueue(u32, void, lessThan){};

// CORRECT
var list = std.ArrayList(u8).empty;
var map = std.StringHashMap(u32).empty;
var queue = std.PriorityQueue(u32, void, lessThan).empty;
```

## 4. File Operations

```zig
// WRONG
const file = try std.fs.cwd().openFile(path, .{});
const file = try std.fs.openFileAbsolute(path, .{});

// CORRECT
const file = try std.Io.Dir.cwd().openFile(io, path, .{});
const file = try std.Io.Dir.openFileAbsolute(io, path, .{});
```

## 5. Reader/Writer Creation

```zig
// WRONG
var fbs = std.io.fixedBufferStream(data);
const reader = fbs.reader();

// CORRECT
var reader: std.Io.Reader = .fixed(data);

// WRONG (writing)
var fbs = std.io.fixedBufferStream(buffer);
const writer = fbs.writer();

// CORRECT
var writer: std.Io.Writer = .fixed(buffer);
```

## 6. String Trimming

```zig
// WRONG
std.mem.trimLeft(u8, s, " ");
std.mem.trimRight(u8, s, " ");

// CORRECT
std.mem.trimStart(u8, s, " ");
std.mem.trimEnd(u8, s, " ");
```

## 7. Current Directory

```zig
// WRONG
var buf: [std.fs.max_path_bytes]u8 = undefined;
const n = try std.process.getCwd(&buf);

// CORRECT
var buf: [std.Io.Dir.max_path_bytes]u8 = undefined;
const n = try std.process.currentPath(io, &buf);
```

## 8. Command Line Arguments

```zig
// WRONG
const args = try std.process.argsAlloc(allocator);

// CORRECT (via Juicy Main)
const args = try init.minimal.args.toSlice(init.arena.allocator());
```

## 9. Random Number Generation

```zig
// WRONG
var buf: [32]u8 = undefined;
std.crypto.random.bytes(&buf);

// CORRECT
var buf: [32]u8 = undefined;
io.random(&buf);
```

## 10. Sleep / Time

```zig
// WRONG
std.time.sleep(1_000_000_000); // 1 second in ns

// CORRECT
io.sleep(.{ .nanoseconds = 1_000_000_000 });
// or
io.sleep(std.Io.Duration.fromSeconds(1));
```

## 11. @cImport (removed in 0.17)

```zig
// WRONG
const c = @cImport({
    @cInclude("stdio.h");
});

// CORRECT — build.zig:
const translate_c = b.addTranslateC(.{
    .root_source_file = b.path("src/c.h"),
    .target = target,
});
// main.zig:
const c = @import("c");
```

## 12. @enumFromInt / @intFromEnum (0.17 rename)

```zig
// WRONG (0.17)
const tag: MyEnum = @enumFromInt(raw);
const raw: u32 = @intFromEnum(tag);

// CORRECT (0.17)
const tag: MyEnum = @fromBackingInt(@intCast(raw));
const raw: u32 = @backingInt(tag);
```

## 13. OptimizeMode Variants (0.17)

```zig
// WRONG (0.17)
if (mode == .Debug) { ... }
if (mode == .ReleaseSafe) { ... }

// CORRECT (0.17)
if (mode == .debug) { ... }
if (mode == .safe) { ... }
```

## 14. @typeInfo Access (0.17)

```zig
// WRONG (0.17)
for (@typeInfo(T).Struct.fields) |f| { _ = f.name; }
if (@typeInfo(T).Enum.is_exhaustive) { ... }
for (@typeInfo(T).Fn.params) |p| { _ = p.type; }

// CORRECT (0.17)
for (@typeInfo(T).Struct.field_names) |name| { ... }
if (@typeInfo(T).Enum.mode == .exhaustive) { ... }
for (@typeInfo(T).Fn.param_types) |T_opt| { ... }
```

## 15. std.builtin → std.lang (0.17)

```zig
// WRONG (0.17)
const mode = std.builtin.OptimizeMode.Debug;

// CORRECT (0.17)
const mode = std.lang.Optimize.debug;
// or (deprecated alias still works):
const mode = std.builtin.Optimize.debug;
```

## 16. build.zig.zon Name (0.16+)

```zig
// WRONG
.{
    .name = "myproject",
    .version = "0.1.0",
}

// CORRECT
.{
    .name = .myproject,
    .fingerprint = 0xa1b2c3d4,
    .version = "0.1.0",
}
```

## 17. Build Executable (0.16+)

```zig
// WRONG
const exe = b.addExecutable(.{
    .name = "myapp",
    .root_source_file = b.path("src/main.zig"),
});

// CORRECT
const exe = b.addExecutable(.{
    .name = "myapp",
    .root_module = b.createModule(.{
        .root_source_file = b.path("src/main.zig"),
    }),
});
```

## 18. Thread.Pool → Io.Group

```zig
// WRONG
var pool: std.Thread.Pool = undefined;
try pool.init(.{ .n_jobs = 4 });
pool.spawnWg(&wg, myFunc, .{arg});

// CORRECT
const io = init.io;
var group = io.group();
defer group.deinit(io);
try group.spawn(io, myFunc, .{arg});
try group.wait(io);
```

## 19. mlock / mlockall

```zig
// WRONG
try std.posix.mlock();
try std.posix.mlockall(std.posix.MCL_CURRENT | std.posix.MCL_FUTURE);

// CORRECT
try std.process.lockMemory(slice, .{});
try std.process.lockMemoryAll(.{ .current = true, .future = true });
```

## 20. fs.Dir.readFileAlloc

```zig
// WRONG
const contents = try std.fs.cwd().readFileAlloc(allocator, path, 1024);

// CORRECT
const contents = try std.Io.Dir.cwd().readFileAlloc(io, path, allocator, .limited(1024));
```
