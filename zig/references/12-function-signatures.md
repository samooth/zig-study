# Key Function Signatures

Condensed reference of the most important APIs. Full signatures in resource maps.

## std.Io (core)

```zig
pub fn operate(io: Io, operation: Operation) Cancelable!Operation.Result
pub fn operateTimeout(io: Io, operation: Operation, timeout: Timeout) OperateTimeoutError!Operation.Result

// Batch
pub fn init(storage: []Operation.Storage) Batch
pub fn add(batch: *Batch, operation: Operation) u32
pub fn awaitAsync(batch: *Batch, io: Io) Cancelable!void
pub fn awaitConcurrent(batch: *Batch, io: Io, timeout: Timeout) AwaitConcurrentError!void
pub fn cancel(batch: *Batch, io: Io) void

// Limit
pub fn limited(n: usize) Limit
pub fn limited64(n: u64) Limit

// Clock
pub fn now(clock: Clock, io: Io) Io.Timestamp
pub fn resolution(clock: Clock, io: Io) ResolutionError!Io.Duration

// Timestamp
pub fn fromNanoseconds(x: i96) Timestamp
pub fn toMilliseconds(t: Timestamp) i64
pub fn durationTo(from: Timestamp, to: Timestamp) Duration

// Duration
pub fn fromSeconds(x: i64) Duration
pub fn fromMilliseconds(x: i64) Duration
pub fn format(duration: Duration, w: *Writer) Writer.Error!void

// Timeout
pub fn toTimestamp(t: Timeout, io: Io) ?Clock.Timestamp
pub fn sleep(timeout: Timeout, io: Io) Cancelable!void

// Future
pub fn Future(Result: type) type
pub fn await(f: *Future(R), io: Io) Result
pub fn cancel(f: *Future(R), io: Io) ?Result

// Group
pub fn async(g: *Group, io: Io, function: anytype, args: ...) void
pub fn concurrent(g: *Group, io: Io, function: anytype, args: ...) ConcurrentError!void
pub fn await(g: *Group, io: Io) Cancelable!void
pub fn cancel(g: *Group, io: Io) void

// Concurrency
pub fn recancel(io: Io) void
pub fn swapCancelProtection(io: Io, new: CancelProtection) CancelProtection
pub fn checkCancel(io: Io) Cancelable!void
```

## std.Io.Dir

```zig
pub fn cwd() Dir
pub fn openFile(dir: Dir, io: Io, sub_path: []const u8, options: OpenFileOptions) File.OpenError!File
pub fn createFile(dir: Dir, io: Io, sub_path: []const u8, flags: CreateFileOptions) File.OpenError!File
pub fn openDir(dir: Dir, io: Io, sub_path: []const u8, options: OpenOptions) OpenError!Dir
pub fn createDir(dir: Dir, io: Io, sub_path: []const u8, permissions: Permissions) CreateDirError!void
pub fn deleteFile(dir: Dir, io: Io, sub_path: []const u8) DeleteFileError!void
pub fn deleteDir(dir: Dir, io: Io, sub_path: []const u8) DeleteDirError!void
pub fn statFile(dir: Dir, io: Io, sub_path: []const u8, options: StatFileOptions) StatFileError!File.Stat
pub fn rename(dir: Dir, io: Io, old: []const u8, new: []const u8) RenameError!void
pub fn symLink(dir: Dir, io: Io, target: []const u8, link: []const u8, flags: SymLinkFlags) SymLinkError!void
pub fn readLink(dir: Dir, io: Io, sub_path: []const u8, buffer: []u8) ReadLinkError!usize
pub fn walk(dir: Dir, allocator: Allocator) WalkError!Walker
pub fn iterate(dir: Dir, io: Io) IterateError!Iterator
pub fn readFileAlloc(dir: Dir, io: Io, path: []const u8, allocator: Allocator, limit: Limit) ReadFileAllocError![]u8
```

## std.Io.File

```zig
pub fn close(file: File, io: Io) void
pub fn read(file: File, io: Io, buffer: []u8) ReadError!usize
pub fn writeAll(file: File, io: Io, bytes: []const u8) WriteError!void
pub fn seekTo(file: File, io: Io, offset: u64) SeekError!void
pub fn seekBy(file: File, io: Io, offset: i64) SeekError!void
pub fn stat(file: File, io: Io) StatError!Stat
pub fn lock(file: File, io: Io, lock_type: Lock) LockError!void
pub fn tryLock(file: File, io: Io, lock_type: Lock) LockError!bool
pub fn unlock(file: File, io: Io) void
pub fn reader(file: File, io: Io, buffer: []u8) Reader
pub fn writer(file: File, io: Io, buffer: []u8) Writer
pub fn memoryMap(file: File, io: Io, options: MemoryMap.CreateOptions) MemoryMap.CreateError!MemoryMap
pub fn setLength(file: File, io: Io, length: u64) SetLengthError!void
pub fn sync(file: File, io: Io) SyncError!void
```

## std.Io.Reader / Writer

```zig
// Reader
pub fn takeByte(r: *Reader, io: Io) Error!u8
pub fn take(r: *Reader, io: Io, n: usize) Error![]u8
pub fn readAtLeast(r: *Reader, io: Io, buffer: []u8, min: usize) Error!usize
pub fn allocRemaining(r: *Reader, io: Io, allocator: Allocator, limit: Limit) Allocator.Error![]u8
pub fn fixed(data: []const u8) Reader

// Writer
pub fn writeAll(w: *Writer, io: Io, bytes: []const u8) Error!void
pub fn print(w: *Writer, io: Io, comptime fmt: []const u8, args: anytype) Error!void
pub fn fixed(buffer: []u8) Writer
pub fn writeInt(w: *Writer, comptime T: type, value: T, endian: std.lang.Endian) Error!void
```

## std.process

```zig
pub fn currentPath(io: Io, buffer: []u8) CurrentPathError!usize
pub fn currentPathAlloc(io: Io, allocator: Allocator) CurrentPathAllocError![:0]u8
pub fn executablePath(io: Io, buffer: []u8) ExecutablePathError!usize
pub fn spawn(io: Io, options: SpawnOptions) SpawnError!Child
pub fn run(allocator: Allocator, io: Io, argv: []const []const u8) RunError!RunResult
pub fn exit(status: u32) noreturn
pub fn abort() noreturn
pub fn getUserInfo(io: Io, name: []const u8) !UserInfo
pub fn lockMemory(slice: []u8, options: LockMemoryOptions) LockMemoryError!void
pub fn lockMemoryAll(options: LockMemoryAllOptions) LockMemoryAllError!void
```

## std.mem

```zig
pub fn indexOf(comptime T: type, haystack: []const T, needle: []const T) ?usize
pub fn indexOfScalar(comptime T: type, haystack: []const T, needle: T) ?usize
pub fn lastIndexOf(comptime T: type, haystack: []const T, needle: []const T) ?usize  // 0.16
pub fn findLast(comptime T: type, haystack: []const T, needle: []const T) ?usize     // 0.17
pub fn eql(comptime T: type, a: []const T, b: []const T) bool
pub fn order(comptime T: type, a: []const T, b: []const T) math.Order
pub fn trim(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
pub fn trimStart(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
pub fn trimEnd(comptime T: type, slice: []const T, values_to_strip: []const T) []const T
pub fn split(comptime T: type, slice: []const T, delimiter: []const T) SplitIterator(T, .forward)
pub fn join(allocator: Allocator, separator: []const u8, slices: []const []const u8) ![]u8
pub fn dupe(allocator: Allocator, comptime T: type, slice: []const T) ![]T
pub fn containsAtLeastScalar(comptime T: type, list: []const T, element: T, minimum: usize) bool
```

## std.meta

```zig
pub fn stringToEnum(comptime T: type, tag_name: []const u8) ?T
pub fn fieldNames(comptime T: type) []const [:0]const u8
pub fn fieldTypes(comptime T: type) []const type
pub fn declarations(comptime T: type) []const [:0]const u8
pub fn tags(comptime T: type) *const [fieldNames(T).len]T
pub fn ArgsTuple(comptime Function: type) type
```

## std.heap

```zig
pub const SafeAllocator = struct { /* 0.17 */ };
pub const DebugAllocator = struct { /* 0.16, alias for SafeAllocator in 0.17 */ };
pub const ArenaAllocator = struct {
    pub fn init(child_allocator: Allocator) ArenaAllocator
    pub fn deinit(self: *ArenaAllocator) void
    pub fn allocator(self: *ArenaAllocator) Allocator
};
pub const SmpAllocator = struct {};
pub const FixedBufferAllocator = struct {
    pub fn init(buffer: []u8) FixedBufferAllocator
    pub fn deinit(self: *FixedBufferAllocator) void
    pub fn allocator(self: *FixedBufferAllocator) Allocator
};
```

## std.fmt

```zig
pub fn bufPrint(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![]u8
pub fn allocPrint(allocator: Allocator, comptime fmt: []const u8, args: anytype) ![]u8
pub fn hex(x: anytype) [@typeInfo(@TypeOf(x)).int.bits / 4]u8
```

## std.testing

```zig
pub fn expectEqual(expected: anytype, actual: @TypeOf(expected)) !void
pub fn expectError(expected_error: anyerror, actual: anytype) !void
pub fn expect(a: bool) !void
pub fn expectFmt(expected: []const u8, comptime fmt: []const u8, args: anytype) !void
```
