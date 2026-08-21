# Zig 0.16.0 vs 0.17.0 — Function Signature Differences

Public API changes only (internal test/mock functions filtered out).

## Io (core)

### + Added in 0.17.0 (50)

| Function | Signature |
|----------|-----------|
| `add` | `pub fn add(batch: *Batch, operation: Operation) u32` |
| `addAt` | `pub fn addAt(batch: *Batch, index: u32, operation: Operation) void` |
| `awaitAsync` | `pub fn awaitAsync(batch: *Batch, io: Io) Cancelable!void` |
| `awaitConcurrent` | `pub fn awaitConcurrent(batch: *Batch, io: Io, timeout: Timeout) AwaitConcurrentError!void` |
| `awaitMany` | `pub fn awaitMany(s: *S, buffer: []U, min: usize) Cancelable!usize` |
| `cancel` | `pub fn cancel(s: *S) ?U` |
| `cancel` | `pub fn cancel(batch: *Batch, io: Io) void` |
| `cancelDiscard` | `pub fn cancelDiscard(s: *S) void` |
| `concurrent` | `pub fn concurrent(s: *S, comptime field: Field, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) ), ) ConcurrentError!void` |
| `format` | `pub fn format(duration: Duration, w: *Writer) Writer.Error!void` |
| `fromMicroseconds` | `pub fn fromMicroseconds(x: i64) Duration` |
| `get` | `pub fn get(q: *@This() , io: Io, buffer: []Elem, min: usize) (QueueClosedError || Cancelable)!usize` |
| `next` | `pub fn next(batch: *Batch) ?Completion` |
| `noGroupAsync` | `pub fn noGroupAsync(userdata: ?*anyopaque, group: *Group, context: []const u8, context_alignment: std.mem.Alignment, start: *const fn (context: *const anyopaque) void, ) void` |
| `noNow` | `pub fn noNow(userdata: ?*anyopaque, clock: Clock) Timestamp` |
| `noSleep` | `pub fn noSleep(userdata: ?*anyopaque, clock: Timeout) Cancelable!void` |
| `noTryLockStderr` | `pub fn noTryLockStderr(userdata: ?*anyopaque, terminal_mode: ?Terminal.Mode) Cancelable!?LockedStderr` |
| `operateTimeout` | `pub fn operateTimeout(io: Io, operation: Operation, timeout: Timeout) OperateTimeoutError!Operation.Result` |
| `put` | `pub fn put(q: *@This() , io: Io, elements: []const Elem, min: usize) (QueueClosedError || Cancelable)!usize` |
| `toInt64` | `pub fn toInt64(l: Limit) ?u64` |
| `toMicroseconds` | `pub fn toMicroseconds(d: Duration) i64` |
| `toMicroseconds` | `pub fn toMicroseconds(t: Timestamp) i64` |
| `unreachableAwait` | `pub fn unreachableAwait(userdata: ?*anyopaque, any_future: *AnyFuture, result: []u8, result_alignment: std.mem.Alignment,) void` |
| `unreachableBatchAwaitAsync` | `pub fn unreachableBatchAwaitAsync(userdata: ?*anyopaque, b: *Batch) Cancelable!void` |
| `unreachableBatchAwaitConcurrent` | `pub fn unreachableBatchAwaitConcurrent(userdata: ?*anyopaque, b: *Batch, timeout: Timeout) Batch.AwaitConcurrentError!void` |
| `unreachableBatchCancel` | `pub fn unreachableBatchCancel(userdata: ?*anyopaque, b: *Batch) void` |
| `unreachableCancel` | `pub fn unreachableCancel(userdata: ?*anyopaque, any_future: *AnyFuture, result: []u8, result_alignment: std.mem.Alignment,) void` |
| `unreachableCheckCancel` | `pub fn unreachableCheckCancel(userdata: ?*anyopaque) Cancelable!void` |
| `unreachableChildKill` | `pub fn unreachableChildKill(userdata: ?*anyopaque, child: *std.process.Child) void` |
| `unreachableChildWait` | `pub fn unreachableChildWait(userdata: ?*anyopaque, child: *std.process.Child) std.process.Child.WaitError!std.process.Child.Term` |
| `unreachableDirClose` | `pub fn unreachableDirClose(userdata: ?*anyopaque, dirs: []const Dir) void` |
| `unreachableFileClose` | `pub fn unreachableFileClose(userdata: ?*anyopaque, files: []const File) void` |
| `unreachableFileEnableAnsiEscapeCodes` | `pub fn unreachableFileEnableAnsiEscapeCodes(userdata: ?*anyopaque, file: File) File.EnableAnsiEscapeCodesError!void` |
| `unreachableFileIsTty` | `pub fn unreachableFileIsTty(userdata: ?*anyopaque, file: File) Cancelable!bool` |
| `unreachableFileMemoryMapDestroy` | `pub fn unreachableFileMemoryMapDestroy(userdata: ?*anyopaque, mm: *File.MemoryMap) void` |
| `unreachableFileMemoryMapRead` | `pub fn unreachableFileMemoryMapRead(userdata: ?*anyopaque, mm: *File.MemoryMap) File.ReadPositionalError!void` |
| `unreachableFileMemoryMapSetLength` | `pub fn unreachableFileMemoryMapSetLength(userdata: ?*anyopaque, mm: *File.MemoryMap, new_len: usize) File.MemoryMap.SetLengthError!void` |
| `unreachableFileMemoryMapWrite` | `pub fn unreachableFileMemoryMapWrite(userdata: ?*anyopaque, mm: *File.MemoryMap) File.WritePositionalError!void` |
| `unreachableFileSupportsAnsiEscapeCodes` | `pub fn unreachableFileSupportsAnsiEscapeCodes(userdata: ?*anyopaque, file: File) Cancelable!bool` |
| `unreachableFileUnlock` | `pub fn unreachableFileUnlock(userdata: ?*anyopaque, file: File) void` |
| `unreachableGroupAwait` | `pub fn unreachableGroupAwait(userdata: ?*anyopaque, group: *Group, token: *anyopaque) Cancelable!void` |
| `unreachableGroupCancel` | `pub fn unreachableGroupCancel(userdata: ?*anyopaque, group: *Group, token: *anyopaque) void` |
| `unreachableLockStderr` | `pub fn unreachableLockStderr(userdata: ?*anyopaque, terminal_mode: ?Terminal.Mode) Cancelable!LockedStderr` |
| `unreachableNetClose` | `pub fn unreachableNetClose(userdata: ?*anyopaque, handle: []const net.Socket.Handle) void` |
| `unreachableNetInterfaceName` | `pub fn unreachableNetInterfaceName(userdata: ?*anyopaque, interface: net.Interface) net.Interface.NameError!net.Interface.Name` |
| `unreachableRecancel` | `pub fn unreachableRecancel(userdata: ?*anyopaque) void` |
| `unreachableSwapCancelProtection` | `pub fn unreachableSwapCancelProtection(userdata: ?*anyopaque, new: CancelProtection) CancelProtection` |
| `unreachableUnlockStderr` | `pub fn unreachableUnlockStderr(userdata: ?*anyopaque) void` |
| `wait` | `pub fn wait(event: *Event, io: Io) Cancelable!void` |
| `waitTimeout` | `pub fn waitTimeout(cond: *Condition, io: Io, mutex: *Mutex, timeout: Timeout) WaitTimeoutError!void` |

### - Removed from 0.16.0 (12)

| Function | Signature |
|----------|-----------|
| `SelectUnion` | `pub fn SelectUnion(S: type) type` |
| `add` | `pub fn add(b: *Batch, operation: Operation) u32` |
| `addAt` | `pub fn addAt(b: *Batch, index: u32, operation: Operation) void` |
| `awaitAsync` | `pub fn awaitAsync(b: *Batch, io: Io) Cancelable!void` |
| `awaitConcurrent` | `pub fn awaitConcurrent(b: *Batch, io: Io, timeout: Timeout) AwaitConcurrentError!void` |
| `cancel` | `pub fn cancel(b: *Batch, io: Io) void` |
| `cancel` | `pub fn cancel(s: *S) void` |
| `get` | `pub fn get(q: *@This() , io: Io, buffer: []Elem, target: usize) (QueueClosedError || Cancelable)!usize` |
| `next` | `pub fn next(b: *Batch) ?Completion` |
| `put` | `pub fn put(q: *@This() , io: Io, elements: []const Elem, target: usize) (QueueClosedError || Cancelable)!usize` |
| `select` | `pub fn select(io: Io, s: anytype) Cancelable!SelectUnion(@TypeOf(s))` |
| `wait` | `pub fn wait(event: *Event, io: Io) Io.Cancelable!void` |

## Io/Dir

### + Added in 0.17.0 (7)

| Function | Signature |
|----------|-----------|
| `createFile` | `pub fn createFile(dir: Dir, io: Io, sub_path: []const u8, flags: CreateFileOptions) File.OpenError!File` |
| `createFileAbsolute` | `pub fn createFileAbsolute(io: Io, absolute_path: []const u8, flags: CreateFileOptions) File.OpenError!File` |
| `isRead` | `pub fn isRead(self: OpenFileOptions) bool` |
| `isWrite` | `pub fn isWrite(self: OpenFileOptions) bool` |
| `openFile` | `pub fn openFile(dir: Dir, io: Io, sub_path: []const u8, options: OpenFileOptions) File.OpenError!File` |
| `openFileAbsolute` | `pub fn openFileAbsolute(io: Io, absolute_path: []const u8, options: OpenFileOptions) File.OpenError!File` |
| `setFileOwner` | `pub fn setFileOwner(dir: Dir, io: Io, sub_path: []const u8, owner: ?File.Uid, group: ?File.Gid, options: SetFileOwnerOptions,) SetFileOwnerError!void` |

### - Removed from 0.16.0 (5)

| Function | Signature |
|----------|-----------|
| `createFile` | `pub fn createFile(dir: Dir, io: Io, sub_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileAbsolute` | `pub fn createFileAbsolute(io: Io, absolute_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `openFile` | `pub fn openFile(dir: Dir, io: Io, sub_path: []const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileAbsolute` | `pub fn openFileAbsolute(io: Io, absolute_path: []const u8, flags: File.OpenFlags) File.OpenError!File` |
| `setFileOwner` | `pub fn setFileOwner(dir: Dir, io: Io, sub_path: []const u8, owner: ?File.Uid, group: ?File.Gid, options: SetFileOwnerOptions,) SetOwnerError!void` |

## Io/File

### - Removed from 0.16.0 (2)

| Function | Signature |
|----------|-----------|
| `isRead` | `pub fn isRead(self: OpenFlags) bool` |
| `isWrite` | `pub fn isWrite(self: OpenFlags) bool` |

## Io/Reader

### + Added in 0.17.0 (1)

| Function | Signature |
|----------|-----------|
| `writableVectorWsa` | `pub fn writableVectorWsa(r: *Reader, buffer: []std.os.windows.AFD.WSABUF(.@"var") , data: []const []u8, ) Error!struct` |

### - Removed from 0.16.0 (1)

| Function | Signature |
|----------|-----------|
| `writableVectorWsa` | `pub fn writableVectorWsa(r: *Reader, buffer: []std.os.windows.ws2_32.WSABUF, data: []const []u8,) Error!struct` |

## Io/Writer

### + Added in 0.17.0 (4)

| Function | Signature |
|----------|-----------|
| `printStringEscaped` | `pub fn printStringEscaped(w: *Writer, bytes: []const u8) Error!void` |
| `writeInt` | `pub fn writeInt(w: *Writer, comptime T: type, value: T, endian: std.lang.Endian) Error!void` |
| `writeSliceEndian` | `pub fn writeSliceEndian(w: *Writer, Elem: type, slice: []const Elem, endian: std.lang.Endian,) Error!void` |
| `writeStruct` | `pub fn writeStruct(w: *Writer, value: anytype, endian: std.lang.Endian) Error!void` |

### - Removed from 0.16.0 (6)

| Function | Signature |
|----------|-----------|
| `printDuration` | `pub fn printDuration(w: *Writer, nanoseconds: anytype, options: std.fmt.Options) Error!void` |
| `printDurationSigned` | `pub fn printDurationSigned(w: *Writer, ns: i64) Error!void` |
| `printDurationUnsigned` | `pub fn printDurationUnsigned(w: *Writer, ns: u64) Error!void` |
| `writeInt` | `pub fn writeInt(w: *Writer, comptime T: type, value: T, endian: std.builtin.Endian) Error!void` |
| `writeSliceEndian` | `pub fn writeSliceEndian(w: *Writer, Elem: type, slice: []const Elem, endian: std.builtin.Endian,) Error!void` |
| `writeStruct` | `pub fn writeStruct(w: *Writer, value: anytype, endian: std.builtin.Endian) Error!void` |

## Io/net

### + Added in 0.17.0 (9)

| Function | Signature |
|----------|-----------|
| `connect` | `pub fn connect(address: *const IpAddress, io: Io, options: ConnectOptions) ConnectError!Stream` |
| `format` | `pub fn format(a: *const Ip6Address, w: *Io.Writer) Io.Writer.Error!void` |
| `formatResolved` | `pub fn formatResolved(a: *const Ip6Address, io: Io, w: *Io.Writer) FormatError!void` |
| `fromAny` | `pub fn fromAny(addr: IpAddress) ?Ip6Address` |
| `fromIp6` | `pub fn fromIp6(ip6: Ip6Address) IpAddress` |
| `fromIp6` | `pub fn fromIp6(ip6: Ip6Address) ?Ip4Address` |
| `isAbstract` | `pub fn isAbstract(ua: *const UnixAddress) bool` |
| `listen` | `pub fn listen(address: *const IpAddress, io: Io, options: ListenOptions) ListenError!Server` |
| `read` | `pub fn read(s: *const Stream, io: Io, data: [][]u8) Reader.Error!usize` |

### - Removed from 0.16.0 (5)

| Function | Signature |
|----------|-----------|
| `connect` | `pub fn connect(address: IpAddress, io: Io, options: ConnectOptions) ConnectError!Stream` |
| `format` | `pub fn format(a: Ip6Address, w: *Io.Writer) Io.Writer.Error!void` |
| `formatResolved` | `pub fn formatResolved(a: Ip6Address, io: Io, w: *Io.Writer) FormatError!void` |
| `fromAddress` | `pub fn fromAddress(a: *const Ip6Address, io: Io) FromAddressError!Unresolved` |
| `listen` | `pub fn listen(address: IpAddress, io: Io, options: ListenOptions) ListenError!Server` |

## process

### + Added in 0.17.0 (3)

| Function | Signature |
|----------|-----------|
| `getUserInfo` | `pub fn getUserInfo(io: Io, name: []const u8) !UserInfo` |
| `openExecutable` | `pub fn openExecutable(io: Io, flags: Dir.OpenFileOptions) OpenExecutableError!File` |
| `setCurrentPath` | `pub fn setCurrentPath(io: Io, path: []const u8) !void` |

### - Removed from 0.16.0 (2)

| Function | Signature |
|----------|-----------|
| `getUserInfo` | `pub fn getUserInfo(name: []const u8) !UserInfo` |
| `openExecutable` | `pub fn openExecutable(io: Io, flags: File.OpenFlags) OpenExecutableError!File` |

## process/Child

### + Added in 0.17.0 (2)

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format(t: Term, w: *Io.Writer) Io.Writer.Error!void` |
| `success` | `pub fn success(t: Term) bool` |

## heap

### - Removed from 0.16.0 (3)

| Function | Signature |
|----------|-----------|
| `StackFallbackAllocator` | `pub fn StackFallbackAllocator(comptime size: usize) type` |
| `get` | `pub fn get(self: *Self) Allocator` |
| `stackFallback` | `pub fn stackFallback(comptime size: usize, fallback_allocator: Allocator) StackFallbackAllocator(size)` |

## mem

### + Added in 0.17.0 (9)

| Function | Signature |
|----------|-----------|
| `ReverseIterator` | `pub fn ReverseIterator(comptime T: type) type` |
| `absorbSentinel` | `pub fn absorbSentinel(slice: anytype) AbsorbSentinel(@TypeOf(slice))` |
| `byteSwap` | `pub fn byteSwap(comptime S: type, ptr: *S) void` |
| `byteSwapAligned` | `pub fn byteSwapAligned(comptime S: type, comptime a: Alignment, ptr: *align(a.toByteUnits() ) S, ) void` |
| `containsAtLeastScalar` | `pub fn containsAtLeastScalar(comptime T: type, list: []const T, element: T, minimum: usize) bool` |
| `fromByteUnitsOptional` | `pub fn fromByteUnitsOptional(maybe_n: ?usize) ?Alignment` |
| `peek` | `pub fn peek(self: *const Self) ?[]const T` |
| `print` | `pub fn print(buffer: []u8, comptime format: []const u8, args: anytype) PrintError![]u8` |
| `printSentinel` | `pub fn printSentinel(buffer: []u8, comptime format: []const u8, args: anytype, comptime sentinel: u8,) PrintError![:sentinel]u8` |

### - Removed from 0.16.0 (4)

| Function | Signature |
|----------|-----------|
| `byteSwapAllFields` | `pub fn byteSwapAllFields(comptime S: type, ptr: *S) void` |
| `byteSwapAllFieldsAligned` | `pub fn byteSwapAllFieldsAligned(comptime S: type, comptime a: Alignment, ptr: *align(a.toByteUnits() ) S) void` |
| `containsAtLeastScalar` | `pub fn containsAtLeastScalar(comptime T: type, list: []const T, minimum: usize, element: T) bool` |
| `containsAtLeastScalar2` | `pub fn containsAtLeastScalar2(comptime T: type, list: []const T, element: T, minimum: usize) bool` |

## meta

### + Added in 0.17.0 (9)

| Function | Signature |
|----------|-----------|
| `AbsorbSentinel` | `pub fn AbsorbSentinel(comptime Pointer: type) type` |
| `BackingInt` | `pub fn BackingInt(comptime T: type) type` |
| `BareUnion` | `pub fn BareUnion(comptime T: type) type` |
| `Slice` | `pub fn Slice(comptime Pointer: type) type` |
| `declarations` | `pub fn declarations(comptime T: type) []const [:0]const u8` |
| `fieldNames` | `pub fn fieldNames(comptime T: type) []const [:0]const u8` |
| `fieldTypes` | `pub fn fieldTypes(comptime T: type) []const type` |
| `stringToEnum` | `pub fn stringToEnum(comptime T: type, tag_name: []const u8) ?T` |
| `tags` | `pub fn tags(comptime T: type) *const [fieldNames(T).len]T` |

### - Removed from 0.16.0 (8)

| Function | Signature |
|----------|-----------|
| `Int` | `pub fn Int(comptime signedness: std.builtin.Signedness, comptime bit_count: u16) type` |
| `Tuple` | `pub fn Tuple(comptime types: []const type) type` |
| `declarationInfo` | `pub fn declarationInfo(comptime T: type, comptime decl_name: []const u8) Type.Declaration` |
| `declarations` | `pub fn declarations(comptime T: type) []const Type.Declaration` |
| `fieldNames` | `pub fn fieldNames(comptime T: type) *const [fields(T).len][:0]const u8` |
| `fields` | `pub fn fields(comptime T: type) switch (@typeInfo(T))` |
| `stringToEnum` | `pub fn stringToEnum(comptime T: type, str: []const u8) ?T` |
| `tags` | `pub fn tags(comptime T: type) *const [fields(T).len]T` |

## fmt

### + Added in 0.17.0 (1)

| Function | Signature |
|----------|-----------|
| `hex` | `pub fn hex(x: anytype) [@typeInfo(@TypeOf(x)).int.bits / 4]u8` |

### - Removed from 0.16.0 (2)

| Function | Signature |
|----------|-----------|
| `bufPrintZ` | `pub fn bufPrintZ(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![:0]u8` |
| `hex` | `pub fn hex(x: anytype) [@sizeOf(@TypeOf(x)) * 2]u8` |

## testing

### + Added in 0.17.0 (3)

| Function | Signature |
|----------|-----------|
| `checkAllAllocationFailures` | `pub fn checkAllAllocationFailures(backing_allocator: std.mem.Allocator, comptime test_fn: anytype, extra_args: CheckAllAllocationFailuresExtraArgs(@TypeOf(test_fn) ), ) !void` |
| `fuzz` | `pub fn fuzz(context: anytype, comptime testOne: fn (context: @TypeOf(context) , smith: *Smith) anyerror!void, options: FuzzInputOptions, ) anyerror!void` |
| `init` | `pub fn init(out: *Io.Writer, buffer: []u8) WriterIndirect` |

### - Removed from 0.16.0 (2)

| Function | Signature |
|----------|-----------|
| `checkAllAllocationFailures` | `pub fn checkAllAllocationFailures(backing_allocator: std.mem.Allocator, comptime test_fn: anytype, extra_args: anytype) !void` |
| `fuzz` | `pub fn fuzz(context: anytype, comptime testOne: fn (context: @TypeOf(context) , input: []const u8) anyerror!void, options: FuzzInputOptions, ) anyerror!void` |

## debug

### + Added in 0.17.0 (5)

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void; /// /// /// Appends the symbols for the instruction at `address` to `symbols`. /// pub fn getSymbols(si: *SelfInfo, io: Io, symbol_allocator: Allocator, text_arena: Allocator, address: usize, include_inli...` |
| `dumpErrorReturnTrace` | `pub fn dumpErrorReturnTrace(et: *const std.builtin.StackTrace) void` |
| `loadUninstantiableType` | `pub fn loadUninstantiableType() noreturn` |
| `unexpectedErrorCode` | `pub fn unexpectedErrorCode(err: anyerror) noreturn` |
| `writeErrorReturnTrace` | `pub fn writeErrorReturnTrace(et: *const std.builtin.StackTrace, t: Io.Terminal) Writer.Error!void` |

### - Removed from 0.16.0 (1)

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void; /// /// /// Returns the symbol and source location of the instruction at `address`. /// pub fn getSymbol(si: *SelfInfo, io: Io, address: usize) SelfInfoError!Symbol; /// /// Returns a name for the "module...` |

## spirv

### + Added in 0.17.0 (7)

| Function | Signature |
|----------|-----------|
| `controlBarrier` | `pub fn controlBarrier(comptime execution: Scope, comptime memory: Scope, comptime semantics: MemorySemantics,) void` |
| `imageQuerySize` | `pub fn imageQuerySize(image: anytype,) ImageCoordinate(std.meta.Child(@TypeOf(image)), u32)` |
| `imageSampleImplicitLod` | `pub fn imageSampleImplicitLod(sampled_image: anytype, coordinate: ImageCoordinate(std.meta.Child(@TypeOf(sampled_image) ), f32), ) @Vector(4, ImageSampledType(std.meta.Child(@TypeOf(sampled_image))))` |
| `imageWrite` | `pub fn imageWrite(image: anytype, T: type, coordinate: ImageCoordinate(std.meta.Child(@TypeOf(image) ), T), texel: @Vector(4, ImageSampledType(std.meta.Child(@TypeOf(image)))), ) void` |
| `memoryBarrier` | `pub fn memoryBarrier(comptime memory: Scope, comptime semantics: MemorySemantics) void` |
| `specConst` | `pub fn specConst(T: type, comptime default_value: T, comptime spec_id: u32) T` |
| `workgroupBarrier` | `pub fn workgroupBarrier() void` |

## ascii

### + Added in 0.17.0 (1)

| Function | Signature |
|----------|-----------|
| `hexEscape` | `pub fn hexEscape(bytes: []const u8, case: std.fmt.Case) HexEscape` |

### - Removed from 0.16.0 (1)

| Function | Signature |
|----------|-----------|
| `hexEscape` | `pub fn hexEscape(bytes: []const u8, case: std.fmt.Case) std.fmt.Alt(HexEscape, HexEscape.format)` |

