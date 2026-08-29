# Zig 0.16.0 — Function Signatures

Source: `<zig-install-dir>/lib/std`

## Io

| Function | Signature |
|----------|-----------|
| `fromIndex` | `pub fn fromIndex(i: usize) OptionalIndex` |
| `toIndex` | `pub fn toIndex(oi: OptionalIndex) u32` |
| `operate` | `pub fn operate(io: Io, operation: Operation) Cancelable!Operation.Result` |
| `init` | `pub fn init(storage: []Operation.Storage) Batch` |
| `add` | `pub fn add(b: *Batch, operation: Operation) u32` |
| `addAt` | `pub fn addAt(b: *Batch, index: u32, operation: Operation) void` |
| `next` | `pub fn next(b: *Batch) ?Completion` |
| `awaitAsync` | `pub fn awaitAsync(b: *Batch, io: Io) Cancelable!void` |
| `awaitConcurrent` | `pub fn awaitConcurrent(b: *Batch, io: Io, timeout: Timeout) AwaitConcurrentError!void` |
| `cancel` | `pub fn cancel(b: *Batch, io: Io) void` |
| `limited` | `pub fn limited(n: usize) Limit` |
| `limited64` | `pub fn limited64(n: u64) Limit` |
| `countVec` | `pub fn countVec(data: []const []const u8) Limit` |
| `min` | `pub fn min(a: Limit, b: Limit) Limit` |
| `max` | `pub fn max(a: Limit, b: Limit) Limit` |
| `minInt` | `pub fn minInt(l: Limit, n: usize) usize` |
| `minInt64` | `pub fn minInt64(l: Limit, n: u64) usize` |
| `slice` | `pub fn slice(l: Limit, s: []u8) []u8` |
| `sliceConst` | `pub fn sliceConst(l: Limit, s: []const u8) []const u8` |
| `toInt` | `pub fn toInt(l: Limit) ?usize` |
| `slice1` | `pub fn slice1(l: Limit, non_empty_buffer: []u8) []u8` |
| `nonzero` | `pub fn nonzero(l: Limit) bool` |
| `subtract` | `pub fn subtract(l: Limit, amount: usize) ?Limit` |
| `now` | `pub fn now(clock: Clock, io: Io) Io.Timestamp` |
| `resolution` | `pub fn resolution(clock: Clock, io: Io) ResolutionError!Io.Duration` |
| `now` | `pub fn now(io: Io, clock: Clock) Clock.Timestamp` |
| `wait` | `pub fn wait(t: Clock.Timestamp, io: Io) Cancelable!void` |
| `durationTo` | `pub fn durationTo(from: Clock.Timestamp, to: Clock.Timestamp) Clock.Duration` |
| `addDuration` | `pub fn addDuration(from: Clock.Timestamp, duration: Clock.Duration) Clock.Timestamp` |
| `subDuration` | `pub fn subDuration(from: Clock.Timestamp, duration: Clock.Duration) Clock.Timestamp` |
| `fromNow` | `pub fn fromNow(io: Io, duration: Clock.Duration) Clock.Timestamp` |
| `untilNow` | `pub fn untilNow(timestamp: Clock.Timestamp, io: Io) Clock.Duration` |
| `durationFromNow` | `pub fn durationFromNow(timestamp: Clock.Timestamp, io: Io) Clock.Duration` |
| `toClock` | `pub fn toClock(t: Clock.Timestamp, io: Io, clock: Clock) Clock.Timestamp` |
| `compare` | `pub fn compare(lhs: Clock.Timestamp, op: math.CompareOperator, rhs: Clock.Timestamp) bool` |
| `sleep` | `pub fn sleep(duration: Clock.Duration, io: Io) Cancelable!void` |
| `now` | `pub fn now(io: Io, clock: Clock) Io.Timestamp` |
| `durationTo` | `pub fn durationTo(from: Timestamp, to: Timestamp) Duration` |
| `addDuration` | `pub fn addDuration(from: Timestamp, duration: Duration) Timestamp` |
| `subDuration` | `pub fn subDuration(from: Timestamp, duration: Duration) Timestamp` |
| `withClock` | `pub fn withClock(t: Timestamp, clock: Clock) Clock.Timestamp` |
| `fromNanoseconds` | `pub fn fromNanoseconds(x: i96) Timestamp` |
| `toMilliseconds` | `pub fn toMilliseconds(t: Timestamp) i64` |
| `toSeconds` | `pub fn toSeconds(t: Timestamp) i64` |
| `toNanoseconds` | `pub fn toNanoseconds(t: Timestamp) i96` |
| `formatNumber` | `pub fn formatNumber(t: Timestamp, w: *std.Io.Writer, n: std.fmt.Number) std.Io.Writer.Error!void` |
| `untilNow` | `pub fn untilNow(t: Timestamp, io: Io, clock: Clock) Duration` |
| `fromNanoseconds` | `pub fn fromNanoseconds(x: i96) Duration` |
| `fromMilliseconds` | `pub fn fromMilliseconds(x: i64) Duration` |
| `fromSeconds` | `pub fn fromSeconds(x: i64) Duration` |
| `toMilliseconds` | `pub fn toMilliseconds(d: Duration) i64` |
| `toSeconds` | `pub fn toSeconds(d: Duration) i64` |
| `toNanoseconds` | `pub fn toNanoseconds(d: Duration) i96` |
| `toTimestamp` | `pub fn toTimestamp(t: Timeout, io: Io) ?Clock.Timestamp` |
| `toDeadline` | `pub fn toDeadline(t: Timeout, io: Io) Timeout` |
| `toDurationFromNow` | `pub fn toDurationFromNow(t: Timeout, io: Io) ?Clock.Duration` |
| `sleep` | `pub fn sleep(timeout: Timeout, io: Io) Cancelable!void` |
| `Future` | `pub fn Future(Result: type) type` |
| `cancel` | `pub fn cancel(f: *@This() , io: Io) Result` |
| `await` | `pub fn await(f: *@This() , io: Io) Result` |
| `async` | `pub fn async(g: *Group, io: Io, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) )) void` |
| `concurrent` | `pub fn concurrent(g: *Group, io: Io, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) )) ConcurrentError!void` |
| `await` | `pub fn await(g: *Group, io: Io) Cancelable!void` |
| `cancel` | `pub fn cancel(g: *Group, io: Io) void` |
| `recancel` | `pub fn recancel(io: Io) void` |
| `swapCancelProtection` | `pub fn swapCancelProtection(io: Io, new: CancelProtection) CancelProtection` |
| `checkCancel` | `pub fn checkCancel(io: Io) Cancelable!void` |
| `Select` | `pub fn Select(comptime U: type) type` |
| `init` | `pub fn init(io: Io, buffer: []U) S` |
| `async` | `pub fn async(s: *S, comptime field: Field, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) ), ) void` |
| `await` | `pub fn await(s: *S) Cancelable!U` |
| `cancel` | `pub fn cancel(s: *S) void` |
| `futexWait` | `pub fn futexWait(io: Io, comptime T: type, ptr: *align(@alignOf(u32) ) const T, expected: T) Cancelable!void` |
| `futexWaitTimeout` | `pub fn futexWaitTimeout(io: Io, comptime T: type, ptr: *align(@alignOf(u32) ) const T, expected: T, timeout: Timeout) Cancelable!void` |
| `futexWaitUncancelable` | `pub fn futexWaitUncancelable(io: Io, comptime T: type, ptr: *align(@alignOf(u32) ) const T, expected: T) void` |
| `futexWake` | `pub fn futexWake(io: Io, comptime T: type, ptr: *align(@alignOf(u32) ) const T, max_waiters: u32) void` |
| `tryLock` | `pub fn tryLock(m: *Mutex) bool` |
| `lock` | `pub fn lock(m: *Mutex, io: Io) Cancelable!void` |
| `lockUncancelable` | `pub fn lockUncancelable(m: *Mutex, io: Io) void` |
| `unlock` | `pub fn unlock(m: *Mutex, io: Io) void` |
| `wait` | `pub fn wait(cond: *Condition, io: Io, mutex: *Mutex) Cancelable!void` |
| `waitUncancelable` | `pub fn waitUncancelable(cond: *Condition, io: Io, mutex: *Mutex) void` |
| `signal` | `pub fn signal(cond: *Condition, io: Io) void` |
| `broadcast` | `pub fn broadcast(cond: *Condition, io: Io) void` |
| `isSet` | `pub fn isSet(event: *const Event) bool` |
| `wait` | `pub fn wait(event: *Event, io: Io) Io.Cancelable!void` |
| `waitUncancelable` | `pub fn waitUncancelable(event: *Event, io: Io) void` |
| `waitTimeout` | `pub fn waitTimeout(event: *Event, io: Io, timeout: Timeout) WaitTimeoutError!void` |
| `set` | `pub fn set(e: *Event, io: Io) void` |
| `reset` | `pub fn reset(e: *Event) void` |
| `init` | `pub fn init(buffer: []u8) TypeErasedQueue` |
| `close` | `pub fn close(q: *TypeErasedQueue, io: Io) void` |
| `put` | `pub fn put(q: *TypeErasedQueue, io: Io, elements: []const u8, min: usize) (QueueClosedError || Cancelable)!usize` |
| `putUncancelable` | `pub fn putUncancelable(q: *TypeErasedQueue, io: Io, elements: []const u8, min: usize) QueueClosedError!usize` |
| `get` | `pub fn get(q: *TypeErasedQueue, io: Io, buffer: []u8, min: usize) (QueueClosedError || Cancelable)!usize` |
| `getUncancelable` | `pub fn getUncancelable(q: *TypeErasedQueue, io: Io, buffer: []u8, min: usize) QueueClosedError!usize` |
| `Queue` | `pub fn Queue(Elem: type) type` |
| `init` | `pub fn init(buffer: []Elem) @This()` |
| `close` | `pub fn close(q: *@This() , io: Io) void` |
| `put` | `pub fn put(q: *@This() , io: Io, elements: []const Elem, target: usize) (QueueClosedError || Cancelable)!usize` |
| `putAll` | `pub fn putAll(q: *@This() , io: Io, elements: []const Elem) (QueueClosedError || Cancelable)!void` |
| `putUncancelable` | `pub fn putUncancelable(q: *@This() , io: Io, elements: []const Elem, min: usize) QueueClosedError!usize` |
| `putOne` | `pub fn putOne(q: *@This() , io: Io, item: Elem) (QueueClosedError || Cancelable)!void` |
| `putOneUncancelable` | `pub fn putOneUncancelable(q: *@This() , io: Io, item: Elem) QueueClosedError!void` |
| `get` | `pub fn get(q: *@This() , io: Io, buffer: []Elem, target: usize) (QueueClosedError || Cancelable)!usize` |
| `getUncancelable` | `pub fn getUncancelable(q: *@This() , io: Io, buffer: []Elem, min: usize) QueueClosedError!usize` |
| `getOne` | `pub fn getOne(q: *@This() , io: Io) (QueueClosedError || Cancelable)!Elem` |
| `getOneUncancelable` | `pub fn getOneUncancelable(q: *@This() , io: Io) QueueClosedError!Elem` |
| `capacity` | `pub fn capacity(q: *const @This() ) usize` |
| `async` | `pub fn async(io: Io, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) ), ) Future(@typeInfo(@TypeOf(function)).@"fn".return_type.?)` |
| `concurrent` | `pub fn concurrent(io: Io, function: anytype, args: std.meta.ArgsTuple(@TypeOf(function) ), ) ConcurrentError!Future(@typeInfo(@TypeOf(function)).@"fn".return_type.?)` |
| `sleep` | `pub fn sleep(io: Io, duration: Duration, clock: Clock) Cancelable!void` |
| `select` | `pub fn select(io: Io, s: anytype) Cancelable!SelectUnion(@TypeOf(s))` |
| `terminal` | `pub fn terminal(ls: LockedStderr) Terminal` |
| `clear` | `pub fn clear(ls: LockedStderr, buffer: []u8) Cancelable!void` |
| `lockStderr` | `pub fn lockStderr(io: Io, buffer: []u8, terminal_mode: ?Terminal.Mode) Cancelable!LockedStderr` |
| `tryLockStderr` | `pub fn tryLockStderr(io: Io, buffer: []u8, terminal_mode: ?Terminal.Mode) Cancelable!?LockedStderr` |
| `unlockStderr` | `pub fn unlockStderr(io: Io) void` |
| `random` | `pub fn random(io: Io, buffer: []u8) void` |
| `randomSecure` | `pub fn randomSecure(io: Io, buffer: []u8) RandomSecureError!void` |

## Random

| Function | Signature |
|----------|-----------|
| `interface` | `pub fn interface(this: *const @This() ) std.Random` |
| `init` | `pub fn init(pointer: anytype, comptime fillFn: fn (ptr: @TypeOf(pointer) , buf: []u8) void) Random` |
| `bytes` | `pub fn bytes(r: Random, buf: []u8) void` |
| `array` | `pub fn array(r: Random, comptime E: type, comptime N: usize) [N]E` |
| `boolean` | `pub fn boolean(r: Random) bool` |
| `enumValue` | `pub fn enumValue(r: Random, comptime EnumType: type) EnumType` |
| `enumValueWithIndex` | `pub fn enumValueWithIndex(r: Random, comptime EnumType: type, comptime Index: type) EnumType` |
| `int` | `pub fn int(r: Random, comptime T: type) T` |
| `uintLessThanBiased` | `pub fn uintLessThanBiased(r: Random, comptime T: type, less_than: T) T` |
| `uintLessThan` | `pub fn uintLessThan(r: Random, comptime T: type, less_than: T) T` |
| `uintAtMostBiased` | `pub fn uintAtMostBiased(r: Random, comptime T: type, at_most: T) T` |
| `uintAtMost` | `pub fn uintAtMost(r: Random, comptime T: type, at_most: T) T` |
| `intRangeLessThanBiased` | `pub fn intRangeLessThanBiased(r: Random, comptime T: type, at_least: T, less_than: T) T` |
| `intRangeLessThan` | `pub fn intRangeLessThan(r: Random, comptime T: type, at_least: T, less_than: T) T` |
| `intRangeAtMostBiased` | `pub fn intRangeAtMostBiased(r: Random, comptime T: type, at_least: T, at_most: T) T` |
| `intRangeAtMost` | `pub fn intRangeAtMost(r: Random, comptime T: type, at_least: T, at_most: T) T` |
| `float` | `pub fn float(r: Random, comptime T: type) T` |
| `floatNorm` | `pub fn floatNorm(r: Random, comptime T: type) T` |
| `floatExp` | `pub fn floatExp(r: Random, comptime T: type) T` |
| `shuffle` | `pub fn shuffle(r: Random, comptime T: type, buf: []T) void` |
| `shuffleWithIndex` | `pub fn shuffleWithIndex(r: Random, comptime T: type, buf: []T, comptime Index: type) void` |
| `weightedIndex` | `pub fn weightedIndex(r: Random, comptime T: type, proportions: []const T) usize` |
| `limitRangeBiased` | `pub fn limitRangeBiased(comptime T: type, random_int: T, less_than: T) T` |

## Thread

| Function | Signature |
|----------|-----------|
| `setName` | `pub fn setName(self: Thread, io: Io, name: []const u8) SetNameError!void` |
| `getName` | `pub fn getName(self: Thread, buffer_ptr: *[max_name_len:0]u8) GetNameError!?[]const u8` |
| `getCurrentId` | `pub fn getCurrentId() Id` |
| `getCpuCount` | `pub fn getCpuCount() CpuCountError!usize` |
| `spawn` | `pub fn spawn(config: SpawnConfig, comptime function: anytype, args: anytype) SpawnError!Thread` |
| `getHandle` | `pub fn getHandle(self: Thread) Handle` |
| `detach` | `pub fn detach(self: Thread) void` |
| `join` | `pub fn join(self: Thread) void` |
| `yield` | `pub fn yield() YieldError!void` |
| `run` | `pub fn run(ctx: *@This() ) !void` |
| `maybeAttachSignalStack` | `pub fn maybeAttachSignalStack() void` |

## array_list

| Function | Signature |
|----------|-----------|
| `Managed` | `pub fn Managed(comptime T: type) type` |
| `AlignedManaged` | `pub fn AlignedManaged(comptime T: type, comptime alignment: ?mem.Alignment) type` |
| `SentinelSlice` | `pub fn SentinelSlice(comptime s: T) type` |
| `init` | `pub fn init(gpa: Allocator) Self` |
| `initCapacity` | `pub fn initCapacity(gpa: Allocator, num: usize) Allocator.Error!Self` |
| `deinit` | `pub fn deinit(self: Self) void` |
| `fromOwnedSlice` | `pub fn fromOwnedSlice(gpa: Allocator, slice: Slice) Self` |
| `fromOwnedSliceSentinel` | `pub fn fromOwnedSliceSentinel(gpa: Allocator, comptime sentinel: T, slice: [:sentinel]T) Self` |
| `moveToUnmanaged` | `pub fn moveToUnmanaged(self: *Self) Aligned(T, alignment)` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self) Allocator.Error!Slice` |
| `toOwnedSliceSentinel` | `pub fn toOwnedSliceSentinel(self: *Self, comptime sentinel: T) Allocator.Error!SentinelSlice(sentinel)` |
| `clone` | `pub fn clone(self: Self) Allocator.Error!Self` |
| `insert` | `pub fn insert(self: *Self, i: usize, item: T) Allocator.Error!void` |
| `insertAssumeCapacity` | `pub fn insertAssumeCapacity(self: *Self, i: usize, item: T) void` |
| `addManyAt` | `pub fn addManyAt(self: *Self, index: usize, count: usize) Allocator.Error![]T` |
| `addManyAtAssumeCapacity` | `pub fn addManyAtAssumeCapacity(self: *Self, index: usize, count: usize) []T` |
| `insertSlice` | `pub fn insertSlice(self: *Self, index: usize, items: []const T,) Allocator.Error!void` |
| `replaceRange` | `pub fn replaceRange(self: *Self, start: usize, len: usize, new_items: []const T) Allocator.Error!void` |
| `replaceRangeAssumeCapacity` | `pub fn replaceRangeAssumeCapacity(self: *Self, start: usize, len: usize, new_items: []const T) void` |
| `append` | `pub fn append(self: *Self, item: T) Allocator.Error!void` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, item: T) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, i: usize) T` |
| `swapRemove` | `pub fn swapRemove(self: *Self, i: usize) T` |
| `appendSlice` | `pub fn appendSlice(self: *Self, items: []const T) Allocator.Error!void` |
| `appendSliceAssumeCapacity` | `pub fn appendSliceAssumeCapacity(self: *Self, items: []const T) void` |
| `appendUnalignedSlice` | `pub fn appendUnalignedSlice(self: *Self, items: []align(1) const T) Allocator.Error!void` |
| `appendUnalignedSliceAssumeCapacity` | `pub fn appendUnalignedSliceAssumeCapacity(self: *Self, items: []align(1) const T) void` |
| `print` | `pub fn print(self: *Self, comptime fmt: []const u8, args: anytype) error` |
| `appendNTimes` | `pub fn appendNTimes(self: *Self, value: T, n: usize) Allocator.Error!void` |
| `appendNTimesAssumeCapacity` | `pub fn appendNTimesAssumeCapacity(self: *Self, value: T, n: usize) void` |
| `resize` | `pub fn resize(self: *Self, new_len: usize) Allocator.Error!void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, new_len: usize) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, new_capacity: usize) Allocator.Error!void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(self: *Self, new_capacity: usize) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: usize) Allocator.Error!void` |
| `expandToCapacity` | `pub fn expandToCapacity(self: *Self) void` |
| `addOne` | `pub fn addOne(self: *Self) Allocator.Error!*T` |
| `addOneAssumeCapacity` | `pub fn addOneAssumeCapacity(self: *Self) *T` |
| `addManyAsArray` | `pub fn addManyAsArray(self: *Self, comptime n: usize) Allocator.Error!*[n]T` |
| `addManyAsArrayAssumeCapacity` | `pub fn addManyAsArrayAssumeCapacity(self: *Self, comptime n: usize) *[n]T` |
| `addManyAsSlice` | `pub fn addManyAsSlice(self: *Self, n: usize) Allocator.Error![]T` |
| `addManyAsSliceAssumeCapacity` | `pub fn addManyAsSliceAssumeCapacity(self: *Self, n: usize) []T` |
| `pop` | `pub fn pop(self: *Self) ?T` |
| `allocatedSlice` | `pub fn allocatedSlice(self: Self) Slice` |
| `unusedCapacitySlice` | `pub fn unusedCapacitySlice(self: Self) []T` |
| `getLast` | `pub fn getLast(self: Self) T` |
| `getLastOrNull` | `pub fn getLastOrNull(self: Self) ?T` |
| `Aligned` | `pub fn Aligned(comptime T: type, comptime alignment: ?mem.Alignment) type` |
| `initBuffer` | `pub fn initBuffer(buffer: Slice) Self` |
| `deinit` | `pub fn deinit(self: *Self, gpa: Allocator) void` |
| `toManaged` | `pub fn toManaged(self: *Self, gpa: Allocator) AlignedManaged(T, alignment)` |
| `fromOwnedSlice` | `pub fn fromOwnedSlice(slice: Slice) Self` |
| `fromOwnedSliceSentinel` | `pub fn fromOwnedSliceSentinel(comptime sentinel: T, slice: [:sentinel]T) Self` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self, gpa: Allocator) Allocator.Error!Slice` |
| `toOwnedSliceSentinel` | `pub fn toOwnedSliceSentinel(self: *Self, gpa: Allocator, comptime sentinel: T) Allocator.Error!SentinelSlice(sentinel)` |
| `clone` | `pub fn clone(self: Self, gpa: Allocator) Allocator.Error!Self` |
| `insert` | `pub fn insert(self: *Self, gpa: Allocator, i: usize, item: T) Allocator.Error!void` |
| `insertBounded` | `pub fn insertBounded(self: *Self, i: usize, item: T) error` |
| `addManyAt` | `pub fn addManyAt(self: *Self, gpa: Allocator, index: usize, count: usize,) Allocator.Error![]T` |
| `addManyAtBounded` | `pub fn addManyAtBounded(self: *Self, index: usize, count: usize) error` |
| `insertSlice` | `pub fn insertSlice(self: *Self, gpa: Allocator, index: usize, items: []const T,) Allocator.Error!void` |
| `insertSliceAssumeCapacity` | `pub fn insertSliceAssumeCapacity(self: *Self, index: usize, items: []const T,) void` |
| `insertSliceBounded` | `pub fn insertSliceBounded(self: *Self, index: usize, items: []const T,) error` |
| `replaceRange` | `pub fn replaceRange(self: *Self, gpa: Allocator, start: usize, len: usize, new_items: []const T,) Allocator.Error!void` |
| `replaceRangeBounded` | `pub fn replaceRangeBounded(self: *Self, start: usize, len: usize, new_items: []const T) error` |
| `append` | `pub fn append(self: *Self, gpa: Allocator, item: T) Allocator.Error!void` |
| `appendBounded` | `pub fn appendBounded(self: *Self, item: T) error` |
| `orderedRemoveMany` | `pub fn orderedRemoveMany(self: *Self, sorted_indexes: []const usize) void` |
| `appendSlice` | `pub fn appendSlice(self: *Self, gpa: Allocator, items: []const T) Allocator.Error!void` |
| `appendSliceBounded` | `pub fn appendSliceBounded(self: *Self, items: []const T) error` |
| `appendUnalignedSlice` | `pub fn appendUnalignedSlice(self: *Self, gpa: Allocator, items: []align(1) const T) Allocator.Error!void` |
| `appendUnalignedSliceBounded` | `pub fn appendUnalignedSliceBounded(self: *Self, items: []align(1) const T) error` |
| `print` | `pub fn print(self: *Self, gpa: Allocator, comptime fmt: []const u8, args: anytype) error` |
| `printAssumeCapacity` | `pub fn printAssumeCapacity(self: *Self, comptime fmt: []const u8, args: anytype) void` |
| `printBounded` | `pub fn printBounded(self: *Self, comptime fmt: []const u8, args: anytype) error` |
| `appendNTimes` | `pub fn appendNTimes(self: *Self, gpa: Allocator, value: T, n: usize) Allocator.Error!void` |
| `appendNTimesBounded` | `pub fn appendNTimesBounded(self: *Self, value: T, n: usize) error` |
| `resize` | `pub fn resize(self: *Self, gpa: Allocator, new_len: usize) Allocator.Error!void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, gpa: Allocator, new_len: usize) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, gpa: Allocator) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(self: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, gpa: Allocator, additional_count: usize,) Allocator.Error!void` |
| `addOne` | `pub fn addOne(self: *Self, gpa: Allocator) Allocator.Error!*T` |
| `addOneBounded` | `pub fn addOneBounded(self: *Self) error` |
| `addManyAsArray` | `pub fn addManyAsArray(self: *Self, gpa: Allocator, comptime n: usize) Allocator.Error!*[n]T` |
| `addManyAsArrayBounded` | `pub fn addManyAsArrayBounded(self: *Self, comptime n: usize) error` |
| `addManyAsSlice` | `pub fn addManyAsSlice(self: *Self, gpa: Allocator, n: usize) Allocator.Error![]T` |
| `addManyAsSliceBounded` | `pub fn addManyAsSliceBounded(self: *Self, n: usize) error` |
| `growCapacity` | `pub fn growCapacity(minimum: usize) usize` |

## ascii

| Function | Signature |
|----------|-----------|
| `isAlphanumeric` | `pub fn isAlphanumeric(c: u8) bool` |
| `isAlphabetic` | `pub fn isAlphabetic(c: u8) bool` |
| `isControl` | `pub fn isControl(c: u8) bool` |
| `isDigit` | `pub fn isDigit(c: u8) bool` |
| `isLower` | `pub fn isLower(c: u8) bool` |
| `isPrint` | `pub fn isPrint(c: u8) bool` |
| `isGraphical` | `pub fn isGraphical(c: u8) bool` |
| `isPunctuation` | `pub fn isPunctuation(c: u8) bool` |
| `isWhitespace` | `pub fn isWhitespace(c: u8) bool` |
| `isUpper` | `pub fn isUpper(c: u8) bool` |
| `isHex` | `pub fn isHex(c: u8) bool` |
| `isAscii` | `pub fn isAscii(c: u8) bool` |
| `toUpper` | `pub fn toUpper(c: u8) u8` |
| `toLower` | `pub fn toLower(c: u8) u8` |
| `lowerString` | `pub fn lowerString(output: []u8, ascii_string: []const u8) []u8` |
| `allocLowerString` | `pub fn allocLowerString(allocator: std.mem.Allocator, ascii_string: []const u8) ![]u8` |
| `upperString` | `pub fn upperString(output: []u8, ascii_string: []const u8) []u8` |
| `allocUpperString` | `pub fn allocUpperString(allocator: std.mem.Allocator, ascii_string: []const u8) ![]u8` |
| `eqlIgnoreCase` | `pub fn eqlIgnoreCase(a: []const u8, b: []const u8) bool` |
| `startsWithIgnoreCase` | `pub fn startsWithIgnoreCase(haystack: []const u8, needle: []const u8) bool` |
| `endsWithIgnoreCase` | `pub fn endsWithIgnoreCase(haystack: []const u8, needle: []const u8) bool` |
| `findIgnoreCase` | `pub fn findIgnoreCase(haystack: []const u8, needle: []const u8) ?usize` |
| `findIgnoreCasePos` | `pub fn findIgnoreCasePos(haystack: []const u8, start_index: usize, needle: []const u8) ?usize` |
| `findIgnoreCasePosLinear` | `pub fn findIgnoreCasePosLinear(haystack: []const u8, start_index: usize, needle: []const u8) ?usize` |
| `orderIgnoreCase` | `pub fn orderIgnoreCase(lhs: []const u8, rhs: []const u8) std.math.Order` |
| `orderIgnoreCaseZ` | `pub fn orderIgnoreCaseZ(lhs: [*:0]const u8, rhs: [*:0]const u8) std.math.Order` |
| `boundedOrderIgnoreCaseZ` | `pub fn boundedOrderIgnoreCaseZ(lhs: [*:0]const u8, rhs: [*:0]const u8, bound: usize) std.math.Order` |
| `lessThanIgnoreCase` | `pub fn lessThanIgnoreCase(lhs: []const u8, rhs: []const u8) bool` |
| `format` | `pub fn format(se: HexEscape, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `hexEscape` | `pub fn hexEscape(bytes: []const u8, case: std.fmt.Case) std.fmt.Alt(HexEscape, HexEscape.format)` |

## crypto

| Function | Signature |
|----------|-----------|
| `secureZero` | `pub fn secureZero(comptime T: type, s: []volatile T) void` |

## debug

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void; /// /// /// Returns the symbol and source location of the instruction at `address`. /// pub fn getSymbol(si: *SelfInfo, io: Io, address: usize) SelfInfoError!Symbol; /// /// Returns a name for the "module...` |
| `init` | `pub fn init(ctx: *cpu_context.Native) Allocator.Error!UnwindContext; /// pub fn deinit(ctx: *UnwindContext) void; /// /// Returns the frame pointer associated with the last unwound stack frame. /// /// If the frame pointer is unknown, 0 may be ret...` |
| `FullPanic` | `pub fn FullPanic(comptime panicFn: fn ([]const u8, ?usize) noreturn) type` |
| `sentinelMismatch` | `pub fn sentinelMismatch(expected: anytype, found: @TypeOf(expected) ) noreturn` |
| `unwrapError` | `pub fn unwrapError(err: anyerror) noreturn` |
| `outOfBounds` | `pub fn outOfBounds(index: usize, len: usize) noreturn` |
| `startGreaterThanEnd` | `pub fn startGreaterThanEnd(start: usize, end: usize) noreturn` |
| `inactiveUnionField` | `pub fn inactiveUnionField(active: anytype, accessed: @TypeOf(active) ) noreturn` |
| `sliceCastLenRemainder` | `pub fn sliceCastLenRemainder(src_len: usize) noreturn` |
| `reachedUnreachable` | `pub fn reachedUnreachable() noreturn` |
| `unwrapNull` | `pub fn unwrapNull() noreturn` |
| `castToNull` | `pub fn castToNull() noreturn` |
| `incorrectAlignment` | `pub fn incorrectAlignment() noreturn` |
| `invalidErrorCode` | `pub fn invalidErrorCode() noreturn` |
| `integerOutOfBounds` | `pub fn integerOutOfBounds() noreturn` |
| `integerOverflow` | `pub fn integerOverflow() noreturn` |
| `shlOverflow` | `pub fn shlOverflow() noreturn` |
| `shrOverflow` | `pub fn shrOverflow() noreturn` |
| `divideByZero` | `pub fn divideByZero() noreturn` |
| `exactDivisionRemainder` | `pub fn exactDivisionRemainder() noreturn` |
| `integerPartOutOfBounds` | `pub fn integerPartOutOfBounds() noreturn` |
| `corruptSwitch` | `pub fn corruptSwitch() noreturn` |
| `shiftRhsTooBig` | `pub fn shiftRhsTooBig() noreturn` |
| `invalidEnumValue` | `pub fn invalidEnumValue() noreturn` |
| `forLenMismatch` | `pub fn forLenMismatch() noreturn` |
| `copyLenMismatch` | `pub fn copyLenMismatch() noreturn` |
| `memcpyAlias` | `pub fn memcpyAlias() noreturn` |
| `noreturnReturned` | `pub fn noreturnReturned() noreturn` |
| `lockStderr` | `pub fn lockStderr(buffer: []u8) Io.LockedStderr` |
| `unlockStderr` | `pub fn unlockStderr() void` |
| `print` | `pub fn print(comptime fmt: []const u8, args: anytype) void` |
| `getSelfDebugInfo` | `pub fn getSelfDebugInfo() !*SelfInfo` |
| `dumpHex` | `pub fn dumpHex(bytes: []const u8) void` |
| `dumpHexFallible` | `pub fn dumpHexFallible(t: Io.Terminal, bytes: []const u8) !void` |
| `assert` | `pub fn assert(ok: bool) void` |
| `assertReadable` | `pub fn assertReadable(slice: []const volatile u8) void` |
| `assertAligned` | `pub fn assertAligned(ptr: anytype, comptime alignment: std.mem.Alignment) void` |
| `panic` | `pub fn panic(comptime format: []const u8, args: anytype) noreturn` |
| `panicExtra` | `pub fn panicExtra(ret_addr: ?usize, comptime format: []const u8, args: anytype,) noreturn` |
| `defaultPanic` | `pub fn defaultPanic(msg: []const u8, first_trace_addr: ?usize) noreturn` |
| `dumpCurrentStackTrace` | `pub fn dumpCurrentStackTrace(options: StackUnwindOptions) void` |
| `format` | `pub fn format(fst: FormatStackTrace, writer: *Writer) Writer.Error!void` |
| `writeStackTrace` | `pub fn writeStackTrace(st: *const StackTrace, t: Io.Terminal) Writer.Error!void` |
| `dumpStackTrace` | `pub fn dumpStackTrace(st: *const StackTrace) void` |
| `stripInstructionPtrAuthCode` | `pub fn stripInstructionPtrAuthCode(ptr: usize) usize` |
| `getDebugInfoAllocator` | `pub fn getDebugInfoAllocator() Allocator` |
| `maybeEnableSegfaultHandler` | `pub fn maybeEnableSegfaultHandler() void` |
| `updateSegfaultHandler` | `pub fn updateSegfaultHandler(act: ?*const posix.Sigaction) void` |
| `attachSegfaultHandler` | `pub fn attachSegfaultHandler() void` |
| `defaultHandleSegfault` | `pub fn defaultHandleSegfault(addr: ?usize, name: []const u8, opt_ctx: ?CpuContextPtr) noreturn` |
| `dumpStackPointerAddr` | `pub fn dumpStackPointerAddr(prefix: []const u8) void` |
| `ConfigurableTrace` | `pub fn ConfigurableTrace(comptime size: usize, comptime stack_frame_count: usize, comptime is_enabled: bool) type` |
| `addNoOp` | `pub fn addNoOp(t: *@This() , note: []const u8) void` |
| `addAddr` | `pub fn addAddr(t: *@This() , addr: usize, note: []const u8) void` |
| `dump` | `pub fn dump(t: @This() ) void` |
| `format` | `pub fn format(t: @This() , comptime fmt: []const u8, options: std.fmt.Options, writer: *Writer, ) !void` |
| `lock` | `pub fn lock(l: *SafetyLock) void` |
| `unlock` | `pub fn unlock(l: *SafetyLock) void` |
| `assertUnlocked` | `pub fn assertUnlocked(l: SafetyLock) void` |
| `assertLocked` | `pub fn assertLocked(l: SafetyLock) void` |
| `inValgrind` | `pub fn inValgrind() bool` |

## fmt

| Function | Signature |
|----------|-----------|
| `toNumber` | `pub fn toNumber(o: Options, mode: Number.Mode, case: Case) Number` |
| `base` | `pub fn base(mode: Mode) ?u8` |
| `parse` | `pub fn parse(comptime bytes: []const u8) Placeholder` |
| `number` | `pub fn number(self: *@This() ) ?usize` |
| `until` | `pub fn until(self: *@This() , delimiter: u8) []const u8` |
| `char` | `pub fn char(self: *@This() ) ?u8` |
| `maybe` | `pub fn maybe(self: *@This() , byte: u8) bool` |
| `specifier` | `pub fn specifier(self: *@This() ) !Specifier` |
| `peek` | `pub fn peek(self: *@This() , i: usize) ?u8` |
| `hasUnusedArgs` | `pub fn hasUnusedArgs(self: *@This() ) bool` |
| `nextArg` | `pub fn nextArg(self: *@This() , arg_index: ?usize) ?usize` |
| `printInt` | `pub fn printInt(buffer: []u8, value: anytype, base: u8, case: Case, options: Options) usize` |
| `digits2` | `pub fn digits2(value: u8) [2]u8` |
| `Alt` | `pub fn Alt(comptime Data: type, comptime formatFn: fn (data: Data, writer: *Writer) Writer.Error!void, ) type` |
| `format` | `pub fn format(self: @This() , writer: *Writer) Writer.Error!void` |
| `alt` | `pub fn alt(context: anytype, comptime func_name: @EnumLiteral() , ) Alt(@TypeOf(context), @field(@TypeOf(context), @tagName(func_name)))` |
| `other` | `pub fn other(ex: @This() , w: *Writer) Writer.Error!void` |
| `parseInt` | `pub fn parseInt(comptime T: type, buf: []const u8, base: u8) ParseIntError!T` |
| `parseIntWithGenericCharacter` | `pub fn parseIntWithGenericCharacter(comptime Result: type, comptime Character: type, buf: []const Character, base: u8,) ParseIntError!Result` |
| `parseUnsigned` | `pub fn parseUnsigned(comptime T: type, buf: []const u8, base: u8) ParseIntError!T` |
| `parseIntSizeSuffix` | `pub fn parseIntSizeSuffix(buf: []const u8, digit_base: u8) ParseIntError!usize` |
| `charToDigit` | `pub fn charToDigit(c: u8, base: u8) (error` |
| `digitToChar` | `pub fn digitToChar(digit: u8, case: Case) u8` |
| `bufPrint` | `pub fn bufPrint(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![]u8` |
| `bufPrintZ` | `pub fn bufPrintZ(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![:0]u8` |
| `bufPrintSentinel` | `pub fn bufPrintSentinel(buf: []u8, comptime fmt: []const u8, args: anytype, comptime sentinel: u8,) BufPrintError![:sentinel]u8` |
| `count` | `pub fn count(comptime fmt: []const u8, args: anytype) usize` |
| `allocPrint` | `pub fn allocPrint(gpa: Allocator, comptime fmt: []const u8, args: anytype) Allocator.Error![]u8` |
| `allocPrintSentinel` | `pub fn allocPrintSentinel(gpa: Allocator, comptime fmt: []const u8, args: anytype, comptime sentinel: u8,) Allocator.Error![:sentinel]u8` |
| `comptimePrint` | `pub fn comptimePrint(comptime fmt: []const u8, args: anytype) *const [count(fmt, args):0]u8` |
| `format` | `pub fn format(s: @This() , writer: *Writer) Writer.Error!void` |
| `bytesToHex` | `pub fn bytesToHex(input: anytype, case: Case) [input.len * 2]u8` |
| `hexToBytes` | `pub fn hexToBytes(out: []u8, input: []const u8) ![]u8` |
| `format` | `pub fn format(self: R, writer: *Writer) Writer.Error!void` |
| `hex` | `pub fn hex(x: anytype) [@sizeOf(@TypeOf(x)) * 2]u8` |

## hash_map

| Function | Signature |
|----------|-----------|
| `getAutoHashFn` | `pub fn getAutoHashFn(comptime K: type, comptime Context: type) (fn (Context, K) u64)` |
| `getAutoEqlFn` | `pub fn getAutoEqlFn(comptime K: type, comptime Context: type) (fn (Context, K, K) bool)` |
| `AutoHashMap` | `pub fn AutoHashMap(comptime K: type, comptime V: type) type` |
| `AutoHashMapUnmanaged` | `pub fn AutoHashMapUnmanaged(comptime K: type, comptime V: type) type` |
| `AutoContext` | `pub fn AutoContext(comptime K: type) type` |
| `StringHashMap` | `pub fn StringHashMap(comptime V: type) type` |
| `StringHashMapUnmanaged` | `pub fn StringHashMapUnmanaged(comptime V: type) type` |
| `hash` | `pub fn hash(self: @This() , s: []const u8) u64` |
| `eql` | `pub fn eql(self: @This() , a: []const u8, b: []const u8) bool` |
| `eqlString` | `pub fn eqlString(a: []const u8, b: []const u8) bool` |
| `hashString` | `pub fn hashString(s: []const u8) u64` |
| `eql` | `pub fn eql(_: @This() , a: u32, b: u32) bool` |
| `hash` | `pub fn hash(ctx: @This() , key: u32) u64` |
| `eql` | `pub fn eql(ctx: @This() , a: []const u8, b: u32) bool` |
| `hash` | `pub fn hash(_: @This() , adapted_key: []const u8) u64` |
| `HashMap` | `pub fn HashMap(comptime K: type, comptime V: type, comptime Context: type, comptime max_load_percentage: u64,) type` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `initContext` | `pub fn initContext(allocator: Allocator, ctx: Context) Self` |
| `lockPointers` | `pub fn lockPointers(self: *Self) void` |
| `unlockPointers` | `pub fn unlockPointers(self: *Self) void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self) void` |
| `count` | `pub fn count(self: Self) Size` |
| `iterator` | `pub fn iterator(self: *const Self) Iterator` |
| `keyIterator` | `pub fn keyIterator(self: Self) KeyIterator` |
| `valueIterator` | `pub fn valueIterator(self: Self) ValueIterator` |
| `getOrPut` | `pub fn getOrPut(self: *Self, key: K) Allocator.Error!GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, key: anytype, ctx: anytype) Allocator.Error!GetOrPutResult` |
| `getOrPutAssumeCapacity` | `pub fn getOrPutAssumeCapacity(self: *Self, key: K) GetOrPutResult` |
| `getOrPutAssumeCapacityAdapted` | `pub fn getOrPutAssumeCapacityAdapted(self: *Self, key: anytype, ctx: anytype) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, key: K, value: V) Allocator.Error!Entry` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, expected_count: Size) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: Size) Allocator.Error!void` |
| `capacity` | `pub fn capacity(self: Self) Size` |
| `put` | `pub fn put(self: *Self, key: K, value: V) Allocator.Error!void` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, key: K, value: V) Allocator.Error!void` |
| `putAssumeCapacity` | `pub fn putAssumeCapacity(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityNoClobber` | `pub fn putAssumeCapacityNoClobber(self: *Self, key: K, value: V) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, key: K, value: V) Allocator.Error!?KV` |
| `fetchPutAssumeCapacity` | `pub fn fetchPutAssumeCapacity(self: *Self, key: K, value: V) ?KV` |
| `fetchRemove` | `pub fn fetchRemove(self: *Self, key: K) ?KV` |
| `fetchRemoveAdapted` | `pub fn fetchRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `get` | `pub fn get(self: Self, key: K) ?V` |
| `getAdapted` | `pub fn getAdapted(self: Self, key: anytype, ctx: anytype) ?V` |
| `getPtr` | `pub fn getPtr(self: Self, key: K) ?*V` |
| `getPtrAdapted` | `pub fn getPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*V` |
| `getKey` | `pub fn getKey(self: Self, key: K) ?K` |
| `getKeyAdapted` | `pub fn getKeyAdapted(self: Self, key: anytype, ctx: anytype) ?K` |
| `getKeyPtr` | `pub fn getKeyPtr(self: Self, key: K) ?*K` |
| `getKeyPtrAdapted` | `pub fn getKeyPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*K` |
| `getEntry` | `pub fn getEntry(self: Self, key: K) ?Entry` |
| `getEntryAdapted` | `pub fn getEntryAdapted(self: Self, key: anytype, ctx: anytype) ?Entry` |
| `contains` | `pub fn contains(self: Self, key: K) bool` |
| `containsAdapted` | `pub fn containsAdapted(self: Self, key: anytype, ctx: anytype) bool` |
| `remove` | `pub fn remove(self: *Self, key: K) bool` |
| `removeAdapted` | `pub fn removeAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `removeByPtr` | `pub fn removeByPtr(self: *Self, key_ptr: *K) void` |
| `clone` | `pub fn clone(self: Self) Allocator.Error!Self` |
| `cloneWithAllocator` | `pub fn cloneWithAllocator(self: Self, new_allocator: Allocator) Allocator.Error!Self` |
| `cloneWithContext` | `pub fn cloneWithContext(self: Self, new_ctx: anytype) Allocator.Error!HashMap(K, V, @TypeOf(new_ctx), max_load_percentage)` |
| `cloneWithAllocatorAndContext` | `pub fn cloneWithAllocatorAndContext(self: Self, new_allocator: Allocator, new_ctx: anytype,) Allocator.Error!HashMap(K, V, @TypeOf(new_ctx), max_load_percentage)` |
| `move` | `pub fn move(self: *Self) Self` |
| `rehash` | `pub fn rehash(self: *Self) void` |
| `HashMapUnmanaged` | `pub fn HashMapUnmanaged(comptime K: type, comptime V: type, comptime Context: type, comptime max_load_percentage: u64,) type` |
| `isUsed` | `pub fn isUsed(self: Metadata) bool` |
| `isTombstone` | `pub fn isTombstone(self: Metadata) bool` |
| `isFree` | `pub fn isFree(self: Metadata) bool` |
| `takeFingerprint` | `pub fn takeFingerprint(hash: Hash) FingerPrint` |
| `fill` | `pub fn fill(self: *Metadata, fp: FingerPrint) void` |
| `remove` | `pub fn remove(self: *Metadata) void` |
| `next` | `pub fn next(it: *Iterator) ?Entry` |
| `next` | `pub fn next(self: *@This() ) ?*T` |
| `promote` | `pub fn promote(self: Self, allocator: Allocator) Managed` |
| `promoteContext` | `pub fn promoteContext(self: Self, allocator: Allocator, ctx: Context) Managed` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, allocator: Allocator, new_size: Size) Allocator.Error!void` |
| `ensureTotalCapacityContext` | `pub fn ensureTotalCapacityContext(self: *Self, allocator: Allocator, new_size: Size, ctx: Context) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, allocator: Allocator, additional_size: Size) Allocator.Error!void` |
| `ensureUnusedCapacityContext` | `pub fn ensureUnusedCapacityContext(self: *Self, allocator: Allocator, additional_size: Size, ctx: Context) Allocator.Error!void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, allocator: Allocator) void` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!void` |
| `putNoClobberContext` | `pub fn putNoClobberContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!void` |
| `putAssumeCapacityContext` | `pub fn putAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `putAssumeCapacityNoClobberContext` | `pub fn putAssumeCapacityNoClobberContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!?KV` |
| `fetchPutContext` | `pub fn fetchPutContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!?KV` |
| `fetchPutAssumeCapacityContext` | `pub fn fetchPutAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) ?KV` |
| `fetchRemoveContext` | `pub fn fetchRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `getEntryContext` | `pub fn getEntryContext(self: Self, key: K, ctx: Context) ?Entry` |
| `put` | `pub fn put(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!void` |
| `putContext` | `pub fn putContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!void` |
| `getKeyPtrContext` | `pub fn getKeyPtrContext(self: Self, key: K, ctx: Context) ?*K` |
| `getKeyContext` | `pub fn getKeyContext(self: Self, key: K, ctx: Context) ?K` |
| `getPtrContext` | `pub fn getPtrContext(self: Self, key: K, ctx: Context) ?*V` |
| `getContext` | `pub fn getContext(self: Self, key: K, ctx: Context) ?V` |
| `getOrPut` | `pub fn getOrPut(self: *Self, allocator: Allocator, key: K) Allocator.Error!GetOrPutResult` |
| `getOrPutContext` | `pub fn getOrPutContext(self: *Self, allocator: Allocator, key: K, ctx: Context) Allocator.Error!GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype) Allocator.Error!GetOrPutResult` |
| `getOrPutContextAdapted` | `pub fn getOrPutContextAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype, ctx: Context) Allocator.Error!GetOrPutResult` |
| `getOrPutAssumeCapacityContext` | `pub fn getOrPutAssumeCapacityContext(self: *Self, key: K, ctx: Context) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!Entry` |
| `getOrPutValueContext` | `pub fn getOrPutValueContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!Entry` |
| `containsContext` | `pub fn containsContext(self: Self, key: K, ctx: Context) bool` |
| `removeContext` | `pub fn removeContext(self: *Self, key: K, ctx: Context) bool` |
| `clone` | `pub fn clone(self: Self, allocator: Allocator) Allocator.Error!Self` |
| `cloneContext` | `pub fn cloneContext(self: Self, allocator: Allocator, new_ctx: anytype) Allocator.Error!HashMapUnmanaged(K, V, @TypeOf(new_ctx), max_load_percentage)` |
| `rehash` | `pub fn rehash(self: *Self, ctx: anytype) void` |

## heap

| Function | Signature |
|----------|-----------|
| `MemoryPool` | `pub fn MemoryPool(comptime Item: type) type` |
| `pageSize` | `pub fn pageSize() usize` |
| `defaultQueryPageSize` | `pub fn defaultQueryPageSize() usize` |
| `stackFallback` | `pub fn stackFallback(comptime size: usize, fallback_allocator: Allocator) StackFallbackAllocator(size)` |
| `StackFallbackAllocator` | `pub fn StackFallbackAllocator(comptime size: usize) type` |
| `get` | `pub fn get(self: *Self) Allocator` |
| `testAllocator` | `pub fn testAllocator(base_allocator: mem.Allocator) !void` |
| `testAllocatorAligned` | `pub fn testAllocatorAligned(base_allocator: mem.Allocator) !void` |
| `testAllocatorLargeAlignment` | `pub fn testAllocatorLargeAlignment(base_allocator: mem.Allocator) !void` |
| `testAllocatorAlignedShrink` | `pub fn testAllocatorAlignedShrink(base_allocator: mem.Allocator) !void` |

## json

| Function | Signature |
|----------|-----------|
| `fmt` | `pub fn fmt(value: anytype, options: Stringify.Options) Formatter(@TypeOf(value))` |
| `Formatter` | `pub fn Formatter(comptime T: type) type` |
| `format` | `pub fn format(self: @This() , writer: *std.Io.Writer) std.Io.Writer.Error!void` |

## mem

| Function | Signature |
|----------|-----------|
| `toByteUnits` | `pub fn toByteUnits(a: Alignment) usize` |
| `fromByteUnits` | `pub fn fromByteUnits(n: usize) Alignment` |
| `of` | `pub fn of(comptime T: type) Alignment` |
| `order` | `pub fn order(lhs: Alignment, rhs: Alignment) std.math.Order` |
| `compare` | `pub fn compare(lhs: Alignment, op: std.math.CompareOperator, rhs: Alignment) bool` |
| `max` | `pub fn max(lhs: Alignment, rhs: Alignment) Alignment` |
| `min` | `pub fn min(lhs: Alignment, rhs: Alignment) Alignment` |
| `forward` | `pub fn forward(a: Alignment, address: usize) usize` |
| `backward` | `pub fn backward(a: Alignment, address: usize) usize` |
| `check` | `pub fn check(a: Alignment, address: usize) bool` |
| `ValidationAllocator` | `pub fn ValidationAllocator(comptime T: type) type` |
| `init` | `pub fn init(underlying_allocator: T) @This()` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `alloc` | `pub fn alloc(ctx: *anyopaque, n: usize, alignment: mem.Alignment, ret_addr: usize,) ?[*]u8` |
| `resize` | `pub fn resize(ctx: *anyopaque, buf: []u8, alignment: Alignment, new_len: usize, ret_addr: usize,) bool` |
| `remap` | `pub fn remap(ctx: *anyopaque, buf: []u8, alignment: Alignment, new_len: usize, ret_addr: usize,) ?[*]u8` |
| `free` | `pub fn free(ctx: *anyopaque, buf: []u8, alignment: Alignment, ret_addr: usize,) void` |
| `reset` | `pub fn reset(self: *Self) void` |
| `validationWrap` | `pub fn validationWrap(allocator: anytype) ValidationAllocator(@TypeOf(allocator))` |
| `copyForwards` | `pub fn copyForwards(comptime T: type, dest: []T, source: []const T) void` |
| `copyBackwards` | `pub fn copyBackwards(comptime T: type, dest: []T, source: []const T) void` |
| `zeroes` | `pub fn zeroes(comptime T: type) T` |
| `zeroInit` | `pub fn zeroInit(comptime T: type, init: anytype) T` |
| `sort` | `pub fn sort(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) void` |
| `sortUnstable` | `pub fn sortUnstable(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) void` |
| `sortContext` | `pub fn sortContext(a: usize, b: usize, context: anytype) void` |
| `sortUnstableContext` | `pub fn sortUnstableContext(a: usize, b: usize, context: anytype) void` |
| `order` | `pub fn order(comptime T: type, lhs: []const T, rhs: []const T) math.Order` |
| `orderZ` | `pub fn orderZ(comptime T: type, lhs: [*:0]const T, rhs: [*:0]const T) math.Order` |
| `boundedOrderZ` | `pub fn boundedOrderZ(comptime T: type, lhs: [*:0]const T, rhs: [*:0]const T, bound: usize) math.Order` |
| `lessThan` | `pub fn lessThan(comptime T: type, lhs: []const T, rhs: []const T) bool` |
| `eql` | `pub fn eql(comptime T: type, a: []const T, b: []const T) bool` |
| `isNotEqual` | `pub fn isNotEqual(chunk_a: Chunk, chunk_b: Chunk) bool` |
| `findDiff` | `pub fn findDiff(comptime T: type, a: []const T, b: []const T) ?usize` |
| `span` | `pub fn span(ptr: anytype) Span(@TypeOf(ptr))` |
| `sliceTo` | `pub fn sliceTo(ptr: anytype, comptime end: std.meta.Elem(@TypeOf(ptr) )) SliceTo(@TypeOf(ptr), end)` |
| `len` | `pub fn len(value: anytype) usize` |
| `findSentinel` | `pub fn findSentinel(comptime T: type, comptime sentinel: T, p: [*:sentinel]const T) usize` |
| `allEqual` | `pub fn allEqual(comptime T: type, slice: []const T, scalar: T) bool` |
| `trimStart` | `pub fn trimStart(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `trimEnd` | `pub fn trimEnd(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `trim` | `pub fn trim(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `findScalar` | `pub fn findScalar(comptime T: type, slice: []const T, value: T) ?usize` |
| `findScalarLast` | `pub fn findScalarLast(comptime T: type, slice: []const T, value: T) ?usize` |
| `findScalarPos` | `pub fn findScalarPos(comptime T: type, slice: []const T, start_index: usize, value: T) ?usize` |
| `findAny` | `pub fn findAny(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `findLastAny` | `pub fn findLastAny(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `findAnyPos` | `pub fn findAnyPos(comptime T: type, slice: []const T, start_index: usize, values: []const T) ?usize` |
| `findNone` | `pub fn findNone(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `findLastNone` | `pub fn findLastNone(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `findNonePos` | `pub fn findNonePos(comptime T: type, slice: []const T, start_index: usize, values: []const T) ?usize` |
| `find` | `pub fn find(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `findLastLinear` | `pub fn findLastLinear(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `findPosLinear` | `pub fn findPosLinear(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize` |
| `findLast` | `pub fn findLast(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `findPos` | `pub fn findPos(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize` |
| `count` | `pub fn count(comptime T: type, haystack: []const T, needle: []const T) usize` |
| `countScalar` | `pub fn countScalar(comptime T: type, list: []const T, element: T) usize` |
| `containsAtLeast` | `pub fn containsAtLeast(comptime T: type, haystack: []const T, expected_count: usize, needle: []const T) bool` |
| `containsAtLeastScalar` | `pub fn containsAtLeastScalar(comptime T: type, list: []const T, minimum: usize, element: T) bool` |
| `containsAtLeastScalar2` | `pub fn containsAtLeastScalar2(comptime T: type, list: []const T, element: T, minimum: usize) bool` |
| `readVarInt` | `pub fn readVarInt(comptime ReturnType: type, bytes: []const u8, endian: Endian) ReturnType` |
| `readVarPackedInt` | `pub fn readVarPackedInt(comptime T: type, bytes: []const u8, bit_offset: usize, bit_count: usize, endian: std.builtin.Endian, signedness: std.builtin.Signedness,) T` |
| `readInt` | `pub fn readInt(comptime T: type, buffer: *const [@divExact(@typeInfo(T) .int.bits, 8)]u8, endian: Endian) T` |
| `readPackedInt` | `pub fn readPackedInt(comptime T: type, bytes: []const u8, bit_offset: usize, endian: Endian) T` |
| `writeInt` | `pub fn writeInt(comptime T: type, buffer: *[@divExact(@typeInfo(T) .int.bits, 8)]u8, value: T, endian: Endian) void` |
| `writePackedInt` | `pub fn writePackedInt(comptime T: type, bytes: []u8, bit_offset: usize, value: T, endian: Endian) void` |
| `writeVarPackedInt` | `pub fn writeVarPackedInt(bytes: []u8, bit_offset: usize, bit_count: usize, value: anytype, endian: std.builtin.Endian) void` |
| `byteSwapAllFields` | `pub fn byteSwapAllFields(comptime S: type, ptr: *S) void` |
| `byteSwapAllFieldsAligned` | `pub fn byteSwapAllFieldsAligned(comptime S: type, comptime a: Alignment, ptr: *align(a.toByteUnits() ) S) void` |
| `byteSwapAllElements` | `pub fn byteSwapAllElements(comptime Elem: type, slice: []Elem) void` |
| `tokenizeAny` | `pub fn tokenizeAny(comptime T: type, buffer: []const T, delimiters: []const T) TokenIterator(T, .any)` |
| `tokenizeSequence` | `pub fn tokenizeSequence(comptime T: type, buffer: []const T, delimiter: []const T) TokenIterator(T, .sequence)` |
| `tokenizeScalar` | `pub fn tokenizeScalar(comptime T: type, buffer: []const T, delimiter: T) TokenIterator(T, .scalar)` |
| `splitSequence` | `pub fn splitSequence(comptime T: type, buffer: []const T, delimiter: []const T) SplitIterator(T, .sequence)` |
| `splitAny` | `pub fn splitAny(comptime T: type, buffer: []const T, delimiters: []const T) SplitIterator(T, .any)` |
| `splitScalar` | `pub fn splitScalar(comptime T: type, buffer: []const T, delimiter: T) SplitIterator(T, .scalar)` |
| `splitBackwardsSequence` | `pub fn splitBackwardsSequence(comptime T: type, buffer: []const T, delimiter: []const T) SplitBackwardsIterator(T, .sequence)` |
| `splitBackwardsAny` | `pub fn splitBackwardsAny(comptime T: type, buffer: []const T, delimiters: []const T) SplitBackwardsIterator(T, .any)` |
| `splitBackwardsScalar` | `pub fn splitBackwardsScalar(comptime T: type, buffer: []const T, delimiter: T) SplitBackwardsIterator(T, .scalar)` |
| `window` | `pub fn window(comptime T: type, buffer: []const T, size: usize, advance: usize) WindowIterator(T)` |
| `WindowIterator` | `pub fn WindowIterator(comptime T: type) type` |
| `next` | `pub fn next(self: *Self) ?[]const T` |
| `startsWith` | `pub fn startsWith(comptime T: type, haystack: []const T, needle: []const T) bool` |
| `endsWith` | `pub fn endsWith(comptime T: type, haystack: []const T, needle: []const T) bool` |
| `cutPrefix` | `pub fn cutPrefix(comptime T: type, slice: []const T, prefix: []const T) ?[]const T` |
| `cutSuffix` | `pub fn cutSuffix(comptime T: type, slice: []const T, suffix: []const T) ?[]const T` |
| `cut` | `pub fn cut(comptime T: type, haystack: []const T, needle: []const T) ?struct` |
| `cutLast` | `pub fn cutLast(comptime T: type, haystack: []const T, needle: []const T) ?struct` |
| `cutScalar` | `pub fn cutScalar(comptime T: type, haystack: []const T, needle: T) ?struct` |
| `cutScalarLast` | `pub fn cutScalarLast(comptime T: type, haystack: []const T, needle: T) ?struct` |
| `TokenIterator` | `pub fn TokenIterator(comptime T: type, comptime delimiter_type: DelimiterType) type` |
| `peek` | `pub fn peek(self: *Self) ?[]const T` |
| `rest` | `pub fn rest(self: Self) []const T` |
| `SplitIterator` | `pub fn SplitIterator(comptime T: type, comptime delimiter_type: DelimiterType) type` |
| `first` | `pub fn first(self: *Self) []const T` |
| `SplitBackwardsIterator` | `pub fn SplitBackwardsIterator(comptime T: type, comptime delimiter_type: DelimiterType) type` |
| `join` | `pub fn join(allocator: Allocator, separator: []const u8, slices: []const []const u8) Allocator.Error![]u8` |
| `joinZ` | `pub fn joinZ(allocator: Allocator, separator: []const u8, slices: []const []const u8) Allocator.Error![:0]u8` |
| `concat` | `pub fn concat(allocator: Allocator, comptime T: type, slices: []const []const T) Allocator.Error![]T` |
| `concatWithSentinel` | `pub fn concatWithSentinel(allocator: Allocator, comptime T: type, slices: []const []const T, comptime s: T) Allocator.Error![:s]T` |
| `concatMaybeSentinel` | `pub fn concatMaybeSentinel(allocator: Allocator, comptime T: type, slices: []const []const T, comptime s: ?T) Allocator.Error![]T` |
| `min` | `pub fn min(comptime T: type, slice: []const T) T` |
| `max` | `pub fn max(comptime T: type, slice: []const T) T` |
| `minMax` | `pub fn minMax(comptime T: type, slice: []const T) struct` |
| `findMin` | `pub fn findMin(comptime T: type, slice: []const T) usize` |
| `findMax` | `pub fn findMax(comptime T: type, slice: []const T) usize` |
| `findMinMax` | `pub fn findMinMax(comptime T: type, slice: []const T) struct` |
| `swap` | `pub fn swap(comptime T: type, noalias a: *T, noalias b: *T) void` |
| `reverse` | `pub fn reverse(comptime T: type, items: []T) void` |
| `next` | `pub fn next(self: *@This() ) ?Element` |
| `nextPtr` | `pub fn nextPtr(self: *@This() ) ?ElementPointer` |
| `reverseIterator` | `pub fn reverseIterator(slice: anytype) ReverseIterator(@TypeOf(slice))` |
| `rotate` | `pub fn rotate(comptime T: type, items: []T, amount: usize) void` |
| `replace` | `pub fn replace(comptime T: type, input: []const T, needle: []const T, replacement: []const T, output: []T) usize` |
| `replaceScalar` | `pub fn replaceScalar(comptime T: type, slice: []T, match: T, replacement: T) void` |
| `collapseRepeatsLen` | `pub fn collapseRepeatsLen(comptime T: type, slice: []T, elem: T) usize` |
| `collapseRepeats` | `pub fn collapseRepeats(comptime T: type, slice: []T, elem: T) []T` |
| `replacementSize` | `pub fn replacementSize(comptime T: type, input: []const T, needle: []const T, replacement: []const T) usize` |
| `replaceOwned` | `pub fn replaceOwned(comptime T: type, allocator: Allocator, input: []const T, needle: []const T, replacement: []const T) Allocator.Error![]T` |
| `littleToNative` | `pub fn littleToNative(comptime T: type, x: T) T` |
| `bigToNative` | `pub fn bigToNative(comptime T: type, x: T) T` |
| `toNative` | `pub fn toNative(comptime T: type, x: T, endianness_of_x: Endian) T` |
| `nativeTo` | `pub fn nativeTo(comptime T: type, x: T, desired_endianness: Endian) T` |
| `nativeToLittle` | `pub fn nativeToLittle(comptime T: type, x: T) T` |
| `nativeToBig` | `pub fn nativeToBig(comptime T: type, x: T) T` |
| `alignPointerOffset` | `pub fn alignPointerOffset(ptr: anytype, align_to: usize) ?usize` |
| `alignPointer` | `pub fn alignPointer(ptr: anytype, align_to: usize) ?@TypeOf(ptr)` |
| `asBytes` | `pub fn asBytes(ptr: anytype) AsBytesReturnType(@TypeOf(ptr))` |
| `toBytes` | `pub fn toBytes(value: anytype) [@sizeOf(@TypeOf(value))]u8` |
| `bytesAsValue` | `pub fn bytesAsValue(comptime T: type, bytes: anytype) BytesAsValueReturnType(T, @TypeOf(bytes))` |
| `bytesToValue` | `pub fn bytesToValue(comptime T: type, bytes: anytype) T` |
| `bytesAsSlice` | `pub fn bytesAsSlice(comptime T: type, bytes: anytype) BytesAsSliceReturnType(T, @TypeOf(bytes))` |
| `sliceAsBytes` | `pub fn sliceAsBytes(slice: anytype) SliceAsBytesReturnType(@TypeOf(slice))` |
| `alignForwardAnyAlign` | `pub fn alignForwardAnyAlign(comptime T: type, addr: T, alignment: T) T` |
| `alignForward` | `pub fn alignForward(comptime T: type, addr: T, alignment: T) T` |
| `alignForwardLog2` | `pub fn alignForwardLog2(addr: usize, log2_alignment: u8) usize` |
| `doNotOptimizeAway` | `pub fn doNotOptimizeAway(val: anytype) void` |
| `alignBackwardAnyAlign` | `pub fn alignBackwardAnyAlign(comptime T: type, addr: T, alignment: T) T` |
| `alignBackward` | `pub fn alignBackward(comptime T: type, addr: T, alignment: T) T` |
| `isValidAlign` | `pub fn isValidAlign(alignment: usize) bool` |
| `isValidAlignGeneric` | `pub fn isValidAlignGeneric(comptime T: type, alignment: T) bool` |
| `isAlignedAnyAlign` | `pub fn isAlignedAnyAlign(i: usize, alignment: usize) bool` |
| `isAlignedLog2` | `pub fn isAlignedLog2(addr: usize, log2_alignment: u8) bool` |
| `isAligned` | `pub fn isAligned(addr: usize, alignment: usize) bool` |
| `isAlignedGeneric` | `pub fn isAlignedGeneric(comptime T: type, addr: T, alignment: T) bool` |
| `alignInBytes` | `pub fn alignInBytes(bytes: []u8, comptime new_alignment: usize) ?[]align(new_alignment) u8` |
| `alignInSlice` | `pub fn alignInSlice(slice: anytype, comptime new_alignment: usize) ?AlignedSlice(@TypeOf(slice), new_alignment)` |

## meta

| Function | Signature |
|----------|-----------|
| `stringToEnum` | `pub fn stringToEnum(comptime T: type, str: []const u8) ?T` |
| `alignment` | `pub fn alignment(comptime T: type) comptime_int` |
| `Child` | `pub fn Child(comptime T: type) type` |
| `Elem` | `pub fn Elem(comptime T: type) type` |
| `sentinel` | `pub fn sentinel(comptime T: type) ?Elem(T)` |
| `Sentinel` | `pub fn Sentinel(comptime T: type, comptime sentinel_val: Elem(T) ) type` |
| `containerLayout` | `pub fn containerLayout(comptime T: type) Type.ContainerLayout` |
| `declarations` | `pub fn declarations(comptime T: type) []const Type.Declaration` |
| `a` | `pub fn a() void` |
| `declarationInfo` | `pub fn declarationInfo(comptime T: type, comptime decl_name: []const u8) Type.Declaration` |
| `fields` | `pub fn fields(comptime T: type) switch (@typeInfo(T))` |
| `fieldInfo` | `pub fn fieldInfo(comptime T: type, comptime field: FieldEnum(T) ) switch (@typeInfo(T))` |
| `fieldNames` | `pub fn fieldNames(comptime T: type) *const [fields(T).len][:0]const u8` |
| `tags` | `pub fn tags(comptime T: type) *const [fields(T).len]T` |
| `FieldEnum` | `pub fn FieldEnum(comptime T: type) type` |
| `DeclEnum` | `pub fn DeclEnum(comptime T: type) type` |
| `Tag` | `pub fn Tag(comptime T: type) type` |
| `activeTag` | `pub fn activeTag(u: anytype) Tag(@TypeOf(u))` |
| `eql` | `pub fn eql(a: anytype, b: @TypeOf(a) ) bool` |
| `fieldIndex` | `pub fn fieldIndex(comptime T: type, comptime name: []const u8) ?comptime_int` |
| `Int` | `pub fn Int(comptime signedness: std.builtin.Signedness, comptime bit_count: u16) type` |
| `Float` | `pub fn Float(comptime bit_count: u8) type` |
| `ArgsTuple` | `pub fn ArgsTuple(comptime Function: type) type` |
| `Tuple` | `pub fn Tuple(comptime types: []const type) type` |
| `isError` | `pub fn isError(error_union: anytype) bool` |
| `hasFn` | `pub fn hasFn(comptime T: type, comptime name: []const u8) bool` |
| `foo` | `pub fn foo() void` |
| `hasMethod` | `pub fn hasMethod(comptime T: type, comptime name: []const u8) bool` |
| `hasUniqueRepresentation` | `pub fn hasUniqueRepresentation(comptime T: type) bool` |

## posix

| Function | Signature |
|----------|-----------|
| `close` | `pub fn close(fd: fd_t) void` |
| `reboot` | `pub fn reboot(cmd: RebootCommand) RebootError!void` |
| `raise` | `pub fn raise(sig: SIG) RaiseError!void` |
| `kill` | `pub fn kill(pid: pid_t, sig: SIG) KillError!void` |
| `read` | `pub fn read(fd: fd_t, buf: []u8) ReadError!usize` |
| `openat` | `pub fn openat(dir_fd: fd_t, file_path: []const u8, flags: O, mode: mode_t) OpenError!fd_t` |
| `openatZ` | `pub fn openatZ(dir_fd: fd_t, file_path: [*:0]const u8, flags: O, mode: mode_t) OpenError!fd_t` |
| `getppid` | `pub fn getppid() pid_t` |
| `getpeername` | `pub fn getpeername(sock: socket_t, addr: *sockaddr, addrlen: *socklen_t) GetSockNameError!void` |
| `fanotify_init` | `pub fn fanotify_init(flags: std.os.linux.fanotify.InitFlags, event_f_flags: u32) FanotifyInitError!i32` |
| `fanotify_mark` | `pub fn fanotify_mark(fanotify_fd: fd_t, flags: std.os.linux.fanotify.MarkFlags, mask: std.os.linux.fanotify.MarkMask, dirfd: fd_t, pathname: ?[]const u8,) FanotifyMarkError!void` |
| `fanotify_markZ` | `pub fn fanotify_markZ(fanotify_fd: fd_t, flags: std.os.linux.fanotify.MarkFlags, mask: std.os.linux.fanotify.MarkMask, dirfd: fd_t, pathname: ?[*:0]const u8,) FanotifyMarkError!void` |
| `mmap` | `pub fn mmap(ptr: ?[*]align(page_size_min) u8, length: usize, prot: PROT, flags: MAP, fd: fd_t, offset: u64, ) MMapError![]align(page_size_min) u8` |
| `munmap` | `pub fn munmap(memory: []align(page_size_min) const u8) void` |
| `mremap` | `pub fn mremap(old_address: ?[*]align(page_size_min) u8, old_len: usize, new_len: usize, flags: system.MREMAP, new_address: ?[*]align(page_size_min) u8, ) MRemapError![]align(page_size_min) u8` |
| `msync` | `pub fn msync(memory: []align(page_size_min) u8, flags: i32) MSyncError!void` |
| `sysctl` | `pub fn sysctl(name: []const c_int, oldp: ?*anyopaque, oldlenp: ?*usize, newp: ?*anyopaque, newlen: usize,) SysCtlError!void` |
| `getSelfPhdrs` | `pub fn getSelfPhdrs() []std.elf.ElfN.Phdr` |
| `dl_iterate_phdr` | `pub fn dl_iterate_phdr(context: anytype, comptime Error: type, comptime callback: fn (info: *dl_phdr_info, size: usize, context: @TypeOf(context) ) Error!void, ) Error!void` |
| `sched_getaffinity` | `pub fn sched_getaffinity(pid: pid_t) SchedGetAffinityError!cpu_set_t` |
| `sigaltstack` | `pub fn sigaltstack(ss: ?*const stack_t, old_ss: ?*stack_t) SigaltstackError!void` |
| `sigfillset` | `pub fn sigfillset() sigset_t` |
| `sigemptyset` | `pub fn sigemptyset() sigset_t` |
| `sigaddset` | `pub fn sigaddset(set: *sigset_t, sig: SIG) void` |
| `sigdelset` | `pub fn sigdelset(set: *sigset_t, sig: SIG) void` |
| `sigismember` | `pub fn sigismember(set: *const sigset_t, sig: SIG) bool` |
| `sigaction` | `pub fn sigaction(sig: SIG, noalias act: ?*const Sigaction, noalias oact: ?*Sigaction) void` |
| `sigprocmask` | `pub fn sigprocmask(flags: u32, noalias set: ?*const sigset_t, noalias oldset: ?*sigset_t) void` |
| `gethostname` | `pub fn gethostname(name_buffer: *[HOST_NAME_MAX]u8) GetHostNameError![]u8` |
| `uname` | `pub fn uname() utsname` |
| `poll` | `pub fn poll(fds: []pollfd, timeout: i32) PollError!usize` |
| `ppoll` | `pub fn ppoll(fds: []pollfd, timeout: ?*const timespec, mask: ?*const sigset_t) PPollError!usize` |
| `setsockopt` | `pub fn setsockopt(fd: socket_t, level: i32, optname: u32, opt: []const u8) SetSockOptError!void` |
| `memfd_createZ` | `pub fn memfd_createZ(name: [*:0]const u8, flags: u32) MemFdCreateError!fd_t` |
| `memfd_create` | `pub fn memfd_create(name: []const u8, flags: u32) MemFdCreateError!fd_t` |
| `getrusage` | `pub fn getrusage(who: i32) rusage` |
| `tcgetattr` | `pub fn tcgetattr(handle: fd_t) TermiosGetError!termios` |
| `tcsetattr` | `pub fn tcsetattr(handle: fd_t, optional_action: TCSA, termios_p: termios) TermiosSetError!void` |
| `tcgetpgrp` | `pub fn tcgetpgrp(handle: fd_t) TermioGetPgrpError!pid_t` |
| `tcsetpgrp` | `pub fn tcsetpgrp(handle: fd_t, pgrp: pid_t) TermioSetPgrpError!void` |
| `signalfd` | `pub fn signalfd(fd: fd_t, mask: *const sigset_t, flags: u32) !fd_t` |
| `sync` | `pub fn sync() void` |
| `syncfs` | `pub fn syncfs(fd: fd_t) SyncError!void` |
| `fdatasync` | `pub fn fdatasync(fd: fd_t) SyncError!void` |
| `prctl` | `pub fn prctl(option: PR, args: anytype) PrctlError!u31` |
| `getrlimit` | `pub fn getrlimit(resource: rlimit_resource) GetrlimitError!rlimit` |
| `setrlimit` | `pub fn setrlimit(resource: rlimit_resource, limits: rlimit) SetrlimitError!void` |
| `mincore` | `pub fn mincore(ptr: [*]align(page_size_min) u8, length: usize, vec: [*]u8) MincoreError!void` |
| `madvise` | `pub fn madvise(ptr: [*]align(page_size_min) u8, length: usize, advice: u32) MadviseError!void` |
| `perf_event_open` | `pub fn perf_event_open(attr: *system.perf_event_attr, pid: pid_t, cpu: i32, group_fd: fd_t, flags: usize,) PerfEventOpenError!fd_t` |
| `timerfd_create` | `pub fn timerfd_create(clock_id: system.timerfd_clockid_t, flags: system.TFD) TimerFdCreateError!fd_t` |
| `timerfd_settime` | `pub fn timerfd_settime(fd: i32, flags: system.TFD.TIMER, new_value: *const system.itimerspec, old_value: ?*system.itimerspec,) TimerFdSetError!void` |
| `timerfd_gettime` | `pub fn timerfd_gettime(fd: i32) TimerFdGetError!system.itimerspec` |
| `ptrace` | `pub fn ptrace(request: u32, pid: pid_t, addr: usize, data: usize) PtraceError!void` |
| `name_to_handle_at` | `pub fn name_to_handle_at(dirfd: fd_t, pathname: []const u8, handle: *std.os.linux.file_handle, mount_id: *i32, flags: u32,) NameToFileHandleAtError!void` |
| `name_to_handle_atZ` | `pub fn name_to_handle_atZ(dirfd: fd_t, pathname_z: [*:0]const u8, handle: *std.os.linux.file_handle, mount_id: *i32, flags: u32,) NameToFileHandleAtError!void` |
| `unexpectedErrno` | `pub fn unexpectedErrno(err: E) UnexpectedError` |
| `toPosixPath` | `pub fn toPosixPath(file_path: []const u8) error` |

## process

| Function | Signature |
|----------|-----------|
| `currentPath` | `pub fn currentPath(io: Io, buffer: []u8) CurrentPathError!usize` |
| `currentPathAlloc` | `pub fn currentPathAlloc(io: Io, allocator: Allocator) CurrentPathAllocError![:0]u8` |
| `getUserInfo` | `pub fn getUserInfo(name: []const u8) !UserInfo` |
| `posixGetUserInfo` | `pub fn posixGetUserInfo(io: Io, name: []const u8) !UserInfo` |
| `getBaseAddress` | `pub fn getBaseAddress() usize` |
| `replace` | `pub fn replace(io: Io, options: ReplaceOptions) ReplaceError` |
| `replacePath` | `pub fn replacePath(io: Io, dir: Io.Dir, options: ReplaceOptions) ReplaceError` |
| `spawn` | `pub fn spawn(io: Io, options: SpawnOptions) SpawnError!Child` |
| `spawnPath` | `pub fn spawnPath(io: Io, dir: Io.Dir, options: SpawnOptions) SpawnError!Child` |
| `run` | `pub fn run(gpa: Allocator, io: Io, options: RunOptions) RunError!RunResult` |
| `totalSystemMemory` | `pub fn totalSystemMemory() TotalSystemMemoryError!u64` |
| `cleanExit` | `pub fn cleanExit(io: Io) void` |
| `raiseFileDescriptorLimit` | `pub fn raiseFileDescriptorLimit() void` |
| `fatal` | `pub fn fatal(comptime format: []const u8, format_arguments: anytype) noreturn` |
| `executablePathAlloc` | `pub fn executablePathAlloc(io: Io, allocator: Allocator) ExecutablePathAllocError![:0]u8` |
| `executablePath` | `pub fn executablePath(io: Io, out_buffer: []u8) ExecutablePathError!usize` |
| `executableDirPath` | `pub fn executableDirPath(io: Io, out_buffer: []u8) ExecutablePathError!usize` |
| `executableDirPathAlloc` | `pub fn executableDirPathAlloc(io: Io, allocator: Allocator) ExecutablePathAllocError![]u8` |
| `openExecutable` | `pub fn openExecutable(io: Io, options: OpenFileOptions) OpenExecutableError!File` |
| `abort` | `pub fn abort() noreturn` |
| `exit` | `pub fn exit(status: u8) noreturn` |
| `setCurrentDir` | `pub fn setCurrentDir(io: Io, dir: Io.Dir) !void` |
| `lockMemory` | `pub fn lockMemory(memory: []align(std.heap.page_size_min) const u8, options: LockMemoryOptions) LockMemoryError!void` |
| `unlockMemory` | `pub fn unlockMemory(memory: []align(std.heap.page_size_min) const u8) UnlockMemoryError!void` |
| `lockMemoryAll` | `pub fn lockMemoryAll(options: LockMemoryAllOptions) LockMemoryError!void` |
| `unlockMemoryAll` | `pub fn unlockMemoryAll() UnlockMemoryError!void` |
| `protectMemory` | `pub fn protectMemory(memory: []align(std.heap.page_size_min) u8, protection: MemoryProtection) ProtectMemoryError!void` |

## sort

| Function | Signature |
|----------|-----------|
| `insertion` | `pub fn insertion(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) void` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a: usize, b: usize) bool` |
| `swap` | `pub fn swap(ctx: @This() , a: usize, b: usize) void` |
| `insertionContext` | `pub fn insertionContext(a: usize, b: usize, context: anytype) void` |
| `heap` | `pub fn heap(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) void` |
| `heapContext` | `pub fn heapContext(a: usize, b: usize, context: anytype) void` |
| `asc` | `pub fn asc(comptime T: type) fn (void, T, T) bool` |
| `inner` | `pub fn inner(_: void, a: T, b: T) bool` |
| `desc` | `pub fn desc(comptime T: type) fn (void, T, T) bool` |
| `binarySearch` | `pub fn binarySearch(comptime T: type, items: []const T, context: anytype, comptime compareFn: fn (@TypeOf(context) , T) std.math.Order, ) ?usize` |
| `lowerBound` | `pub fn lowerBound(comptime T: type, items: []const T, context: anytype, comptime compareFn: fn (@TypeOf(context) , T) std.math.Order, ) usize` |
| `upperBound` | `pub fn upperBound(comptime T: type, items: []const T, context: anytype, comptime compareFn: fn (@TypeOf(context) , T) std.math.Order, ) usize` |
| `partitionPoint` | `pub fn partitionPoint(comptime T: type, items: []const T, context: anytype, comptime predicate: fn (@TypeOf(context) , T) bool, ) usize` |
| `equalRange` | `pub fn equalRange(comptime T: type, items: []const T, context: anytype, comptime compareFn: fn (@TypeOf(context) , T) std.math.Order, ) struct` |
| `argMin` | `pub fn argMin(comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) ?usize` |
| `min` | `pub fn min(comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context) , lhs: T, rhs: T) bool, ) ?T` |
| `argMax` | `pub fn argMax(comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context) , lhs: T, rhs: T) bool, ) ?usize` |
| `max` | `pub fn max(comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context) , lhs: T, rhs: T) bool, ) ?T` |
| `isSorted` | `pub fn isSorted(comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context) , lhs: T, rhs: T) bool, ) bool` |

## testing

| Function | Signature |
|----------|-----------|
| `expectError` | `pub fn expectError(expected_error: anyerror, actual_error_union: anytype) !void` |
| `expectEqual` | `pub fn expectEqual(expected: anytype, actual: anytype) !void` |
| `expectFmt` | `pub fn expectFmt(expected: []const u8, comptime template: []const u8, args: anytype) !void` |
| `expectApproxEqAbs` | `pub fn expectApproxEqAbs(expected: anytype, actual: anytype, tolerance: anytype) !void` |
| `expectApproxEqRel` | `pub fn expectApproxEqRel(expected: anytype, actual: anytype, tolerance: anytype) !void` |
| `expectEqualSlices` | `pub fn expectEqualSlices(comptime T: type, expected: []const T, actual: []const T) !void` |
| `write` | `pub fn write(self: Self, writer: *Io.Writer) !void` |
| `write` | `pub fn write(self: BytesDiffer, writer: *Io.Writer) !void` |
| `expectEqualSentinel` | `pub fn expectEqualSentinel(comptime T: type, comptime sentinel: T, expected: [:sentinel]const T, actual: [:sentinel]const T) !void` |
| `expect` | `pub fn expect(ok: bool) !void` |
| `cleanup` | `pub fn cleanup(self: *TmpDir) void` |
| `tmpDir` | `pub fn tmpDir(opts: Io.Dir.OpenOptions) TmpDir` |
| `expectEqualStrings` | `pub fn expectEqualStrings(expected: []const u8, actual: []const u8) !void` |
| `expectStringStartsWith` | `pub fn expectStringStartsWith(actual: []const u8, expected_starts_with: []const u8) !void` |
| `expectStringEndsWith` | `pub fn expectStringEndsWith(actual: []const u8, expected_ends_with: []const u8) !void` |
| `expectEqualDeep` | `pub fn expectEqualDeep(expected: anytype, actual: anytype) error` |
| `format` | `pub fn format(self: @This() , writer: *Io.Writer) !void` |
| `checkAllAllocationFailures` | `pub fn checkAllAllocationFailures(backing_allocator: std.mem.Allocator, comptime test_fn: anytype, extra_args: anytype) !void` |
| `refAllDecls` | `pub fn refAllDecls(comptime T: type) void` |
| `fuzz` | `pub fn fuzz(context: anytype, comptime testOne: fn (context: @TypeOf(context) , input: []const u8) anyerror!void, options: FuzzInputOptions, ) anyerror!void` |
| `init` | `pub fn init(buffer: []u8, calls: []const Call) Reader` |
| `init` | `pub fn init(in: *Io.Reader, buffer: []u8) ReaderIndirect` |

## process / Args

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(a: Args) Iterator` |
| `initAllocator` | `pub fn initAllocator(a: Args, gpa: Allocator) InitError!Iterator` |
| `next` | `pub fn next(it: *Iterator) ?[:0]const u8` |
| `skip` | `pub fn skip(it: *Iterator) bool` |
| `deinit` | `pub fn deinit(it: *Iterator) void` |
| `init` | `pub fn init(gpa: Allocator, cmd_line_w: []const u16) Windows.InitError!Windows` |
| `next` | `pub fn next(self: *Windows) ?[:0]const u8` |
| `skip` | `pub fn skip(self: *Windows) bool` |
| `deinit` | `pub fn deinit(self: *Windows) void` |
| `init` | `pub fn init(a: Args) Posix` |
| `next` | `pub fn next(it: *Posix) ?[:0]const u8` |
| `skip` | `pub fn skip(it: *Posix) bool` |
| `init` | `pub fn init(allocator: Allocator) Wasi.InitError!Wasi` |
| `next` | `pub fn next(self: *Wasi) ?[:0]const u8` |
| `skip` | `pub fn skip(self: *Wasi) bool` |
| `deinit` | `pub fn deinit(self: *Wasi) void` |
| `iterate` | `pub fn iterate(a: Args) Iterator` |
| `iterateAllocator` | `pub fn iterateAllocator(a: Args, gpa: Allocator) Iterator.InitError!Iterator` |
| `toSlice` | `pub fn toSlice(a: Args, arena: Allocator) ToSliceError![]const [:0]const u8` |
| `IteratorGeneral` | `pub fn IteratorGeneral(comptime options: IteratorGeneralOptions) type` |
| `init` | `pub fn init(allocator: Allocator, cmd_line_utf8: []const u8) InitError!Self` |
| `initTakeOwnership` | `pub fn initTakeOwnership(allocator: Allocator, cmd_line_utf8: []const u8) InitError!Self` |
| `skip` | `pub fn skip(self: *Self) bool` |
| `next` | `pub fn next(self: *Self) ?[:0]const u8` |
| `deinit` | `pub fn deinit(self: *Self) void` |

## process / Child

| Function | Signature |
|----------|-----------|
| `getMaxRss` | `pub fn getMaxRss(rus: ResourceUsageStatistics) ?usize` |
| `kill` | `pub fn kill(child: *Child, io: Io) void` |
| `wait` | `pub fn wait(child: *Child, io: Io) WaitError!Term` |

## process / Environ

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(_: GlobalBlock, _: Allocator) void` |
| `deinit` | `pub fn deinit(block: PosixBlock, gpa: Allocator) void` |
| `isEmpty` | `pub fn isEmpty(v: View) bool` |
| `view` | `pub fn view(block: PosixBlock) View` |
| `deinit` | `pub fn deinit(block: WindowsBlock, gpa: Allocator) void` |
| `view` | `pub fn view(block: WindowsBlock) View` |
| `hash` | `pub fn hash(self: @This() , s: []const u8) u32` |
| `eql` | `pub fn eql(self: @This() , a: []const u8, b: []const u8, b_index: usize) bool` |
| `validateKeyForPut` | `pub fn validateKeyForPut(key: []const u8) bool` |
| `validateKeyForFetch` | `pub fn validateKeyForFetch(key: []const u8) bool` |
| `init` | `pub fn init(allocator: Allocator) Map` |
| `deinit` | `pub fn deinit(self: *Map) void` |
| `keys` | `pub fn keys(map: *const Map) [][]const u8` |
| `values` | `pub fn values(map: *const Map) [][]const u8` |
| `putPosixBlock` | `pub fn putPosixBlock(map: *Map, view: PosixBlock.View) Allocator.Error!void` |
| `putWindowsBlock` | `pub fn putWindowsBlock(map: *Map, view: WindowsBlock.View) Allocator.Error!void` |
| `putMove` | `pub fn putMove(self: *Map, key: []u8, value: []u8) Allocator.Error!void` |
| `put` | `pub fn put(self: *Map, key: []const u8, value: []const u8) Allocator.Error!void` |
| `getPtr` | `pub fn getPtr(self: Map, key: []const u8) ?*[]const u8` |
| `get` | `pub fn get(self: Map, key: []const u8) ?[]const u8` |
| `contains` | `pub fn contains(m: *const Map, key: []const u8) bool` |
| `swapRemove` | `pub fn swapRemove(self: *Map, key: []const u8) bool` |
| `orderedRemove` | `pub fn orderedRemove(self: *Map, key: []const u8) bool` |
| `count` | `pub fn count(self: Map) Size` |
| `iterator` | `pub fn iterator(self: *const Map) ArrayHashMap.Iterator` |
| `clone` | `pub fn clone(m: *const Map, gpa: Allocator) Allocator.Error!Map` |
| `createPosixBlock` | `pub fn createPosixBlock(map: *const Map, gpa: Allocator, options: CreatePosixBlockOptions,) Allocator.Error!PosixBlock` |
| `createWindowsBlock` | `pub fn createWindowsBlock(map: *const Map, gpa: Allocator, options: CreateWindowsBlockOptions,) error` |
| `createMap` | `pub fn createMap(env: Environ, allocator: Allocator) CreateMapError!Map` |
| `contains` | `pub fn contains(environ: Environ, gpa: Allocator, key: []const u8) ContainsError!bool` |
| `containsUnempty` | `pub fn containsUnempty(environ: Environ, gpa: Allocator, key: []const u8) ContainsError!bool` |
| `containsConstant` | `pub fn containsConstant(environ: Environ, comptime key: []const u8) bool` |
| `containsUnemptyConstant` | `pub fn containsUnemptyConstant(environ: Environ, comptime key: []const u8) bool` |
| `getPosix` | `pub fn getPosix(environ: Environ, key: []const u8) ?[:0]const u8` |
| `getWindows` | `pub fn getWindows(environ: Environ, key: [*:0]const u16) ?[:0]const u16` |
| `getAlloc` | `pub fn getAlloc(environ: Environ, gpa: Allocator, key: []const u8) GetAllocError![]u8` |
| `createPosixBlock` | `pub fn createPosixBlock(existing: Environ, gpa: Allocator, options: CreatePosixBlockOptions,) Allocator.Error!PosixBlock` |
| `createWindowsBlock` | `pub fn createWindowsBlock(existing: Environ, gpa: Allocator, options: CreateWindowsBlockOptions,) Allocator.Error!WindowsBlock` |

## process / Preopens

| Function | Signature |
|----------|-----------|
| `get` | `pub fn get(p: *const Preopens, name: []const u8) ?Resource` |
| `init` | `pub fn init(arena: Allocator) InitError!Preopens` |

## heap / FixedBufferAllocator

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(buffer: []u8) FixedBufferAllocator` |
| `allocator` | `pub fn allocator(self: *FixedBufferAllocator) Allocator` |
| `threadSafeAllocator` | `pub fn threadSafeAllocator(self: *FixedBufferAllocator) Allocator` |
| `ownsPtr` | `pub fn ownsPtr(self: *FixedBufferAllocator, ptr: [*]u8) bool` |
| `ownsSlice` | `pub fn ownsSlice(self: *FixedBufferAllocator, slice: []u8) bool` |
| `isLastAllocation` | `pub fn isLastAllocation(self: *FixedBufferAllocator, buf: []u8) bool` |
| `alloc` | `pub fn alloc(ctx: *anyopaque, n: usize, alignment: mem.Alignment, ra: usize) ?[*]u8` |
| `resize` | `pub fn resize(ctx: *anyopaque, buf: []u8, alignment: mem.Alignment, new_size: usize, return_address: usize,) bool` |
| `remap` | `pub fn remap(context: *anyopaque, memory: []u8, alignment: mem.Alignment, new_len: usize, return_address: usize,) ?[*]u8` |
| `free` | `pub fn free(ctx: *anyopaque, buf: []u8, alignment: mem.Alignment, return_address: usize,) void` |
| `reset` | `pub fn reset(self: *FixedBufferAllocator) void` |

## heap / PageAllocator

| Function | Signature |
|----------|-----------|
| `map` | `pub fn map(n: usize, alignment: mem.Alignment) ?[*]u8` |
| `unmap` | `pub fn unmap(memory: []align(page_size_min) u8) void` |
| `realloc` | `pub fn realloc(uncasted_memory: []u8, new_len: usize, may_move: bool) ?[*]u8` |

## heap / arena_allocator

| Function | Signature |
|----------|-----------|
| `promote` | `pub fn promote(self: State, child_allocator: Allocator) ArenaAllocator` |
| `allocator` | `pub fn allocator(self: *ArenaAllocator) Allocator` |
| `init` | `pub fn init(child_allocator: Allocator) ArenaAllocator` |
| `deinit` | `pub fn deinit(self: ArenaAllocator) void` |
| `queryCapacity` | `pub fn queryCapacity(self: ArenaAllocator) usize` |
| `reset` | `pub fn reset(self: *ArenaAllocator, mode: ResetMode) bool` |

## heap / debug_allocator

| Function | Signature |
|----------|-----------|
| `DebugAllocator` | `pub fn DebugAllocator(comptime config: Config) type` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `detectLeaks` | `pub fn detectLeaks(self: *Self) usize` |
| `flushRetainedMetadata` | `pub fn flushRetainedMetadata(self: *Self) void` |
| `deinit` | `pub fn deinit(self: *Self) std.heap.Check` |
| `deinitWithoutLeakChecks` | `pub fn deinitWithoutLeakChecks(self: *Self) void` |

## heap / memory_pool

| Function | Signature |
|----------|-----------|
| `Managed` | `pub fn Managed(comptime Item: type) type` |
| `Aligned` | `pub fn Aligned(comptime Item: type, comptime alignment: Alignment) type` |
| `AlignedManaged` | `pub fn AlignedManaged(comptime Item: type, comptime alignment: Alignment) type` |
| `Extra` | `pub fn Extra(comptime Item: type, comptime pool_options: Options) type` |
| `initCapacity` | `pub fn initCapacity(allocator: Allocator, num: usize) Allocator.Error!Pool` |
| `deinit` | `pub fn deinit(pool: *Pool, allocator: Allocator) void` |
| `toManaged` | `pub fn toManaged(pool: Pool, allocator: Allocator) ExtraManaged(Item, pool_options)` |
| `addCapacity` | `pub fn addCapacity(pool: *Pool, allocator: Allocator, num: usize) Allocator.Error!void` |
| `reset` | `pub fn reset(pool: *Pool, allocator: Allocator, mode: ResetMode) bool` |
| `create` | `pub fn create(pool: *Pool, allocator: Allocator) Allocator.Error!ItemPtr` |
| `destroy` | `pub fn destroy(pool: *Pool, ptr: ItemPtr) void` |
| `ExtraManaged` | `pub fn ExtraManaged(comptime Item: type, comptime pool_options: Options) type` |
| `init` | `pub fn init(allocator: Allocator) Pool` |
| `deinit` | `pub fn deinit(pool: *Pool) void` |
| `addCapacity` | `pub fn addCapacity(pool: *Pool, num: usize) Allocator.Error!void` |
| `reset` | `pub fn reset(pool: *Pool, mode: ResetMode) bool` |
| `create` | `pub fn create(pool: *Pool) Allocator.Error!ItemPtr` |

## http / Client

| Function | Signature |
|----------|-----------|
| `findConnection` | `pub fn findConnection(pool: *ConnectionPool, io: Io, criteria: Criteria) ?*Connection` |
| `acquireUnsafe` | `pub fn acquireUnsafe(pool: *ConnectionPool, connection: *Connection) void` |
| `acquire` | `pub fn acquire(pool: *ConnectionPool, io: Io, connection: *Connection) void` |
| `release` | `pub fn release(pool: *ConnectionPool, connection: *Connection, io: Io) void` |
| `addUsed` | `pub fn addUsed(pool: *ConnectionPool, io: Io, connection: *Connection) void` |
| `resize` | `pub fn resize(pool: *ConnectionPool, io: Io, allocator: Allocator, new_size: usize) void` |
| `deinit` | `pub fn deinit(pool: *ConnectionPool, io: Io) void` |
| `fromScheme` | `pub fn fromScheme(scheme: []const u8) ?Protocol` |
| `fromUri` | `pub fn fromUri(uri: Uri) ?Protocol` |
| `getReadError` | `pub fn getReadError(c: *const Connection) ?ReadError` |
| `host` | `pub fn host(c: *Connection) HostName` |
| `destroy` | `pub fn destroy(c: *Connection, io: Io) void` |
| `writer` | `pub fn writer(c: *Connection) *Writer` |
| `reader` | `pub fn reader(c: *Connection) *Reader` |
| `flush` | `pub fn flush(c: *Connection) Writer.Error!void` |
| `end` | `pub fn end(c: *Connection) Writer.Error!void` |
| `parse` | `pub fn parse(bytes: []const u8) ParseError!Head` |
| `iterateHeaders` | `pub fn iterateHeaders(h: Head) http.HeaderIterator` |
| `reader` | `pub fn reader(response: *Response, transfer_buffer: []u8) *Reader` |
| `readerDecompressing` | `pub fn readerDecompressing(response: *Response, transfer_buffer: []u8, decompress: *http.Decompress, decompress_buffer: []u8,) *Reader` |
| `bodyErr` | `pub fn bodyErr(response: *const Response) ?http.Reader.BodyError` |
| `iterateTrailers` | `pub fn iterateTrailers(response: *const Response) http.HeaderIterator` |
| `init` | `pub fn init(n: u16) RedirectBehavior` |
| `subtractOne` | `pub fn subtractOne(rb: *RedirectBehavior) void` |
| `remaining` | `pub fn remaining(rb: RedirectBehavior) u16` |
| `deinit` | `pub fn deinit(r: *Request) void` |
| `sendBodiless` | `pub fn sendBodiless(r: *Request) Writer.Error!void` |
| `sendBodilessUnflushed` | `pub fn sendBodilessUnflushed(r: *Request) Writer.Error!void` |
| `sendBody` | `pub fn sendBody(r: *Request, buffer: []u8) Writer.Error!http.BodyWriter` |
| `sendBodyComplete` | `pub fn sendBodyComplete(r: *Request, body: []u8) Writer.Error!void` |
| `sendBodyUnflushed` | `pub fn sendBodyUnflushed(r: *Request, buffer: []u8) Writer.Error!http.BodyWriter` |
| `receiveHead` | `pub fn receiveHead(r: *Request, redirect_buffer: []u8) ReceiveHeadError!Response` |
| `deinit` | `pub fn deinit(client: *Client) void` |
| `initDefaultProxies` | `pub fn initDefaultProxies(client: *Client, arena: Allocator, environ_map: *std.process.Environ.Map) !void` |
| `valueLength` | `pub fn valueLength(user_len: usize, password_len: usize) usize` |
| `valueLengthFromUri` | `pub fn valueLengthFromUri(uri: Uri) usize` |
| `value` | `pub fn value(uri: Uri, out: []u8) []u8` |
| `write` | `pub fn write(uri: Uri, out: *Writer) Writer.Error!void` |
| `connectTcp` | `pub fn connectTcp(client: *Client, host: HostName, port: u16, protocol: Protocol,) ConnectTcpError!*Connection` |
| `connectTcpOptions` | `pub fn connectTcpOptions(client: *Client, options: ConnectTcpOptions) ConnectTcpError!*Connection` |
| `connectUnix` | `pub fn connectUnix(client: *Client, path: []const u8) ConnectUnixError!*Connection` |
| `connectProxied` | `pub fn connectProxied(client: *Client, proxy: *Proxy, proxied_host: HostName, proxied_port: u16,) !*Connection` |
| `connect` | `pub fn connect(client: *Client, host: HostName, port: u16, protocol: Protocol,) ConnectError!*Connection` |
| `request` | `pub fn request(client: *Client, method: http.Method, uri: Uri, options: RequestOptions,) RequestError!Request` |
| `fetch` | `pub fn fetch(client: *Client, options: FetchOptions) FetchError!FetchResult` |

## http / Server

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(in: *Reader, out: *Writer) Server` |
| `receiveHead` | `pub fn receiveHead(s: *Server) ReceiveHeadError!Request` |
| `parse` | `pub fn parse(bytes: []const u8) ParseError!Head` |
| `iterateHeaders` | `pub fn iterateHeaders(r: *const Request) http.HeaderIterator` |
| `respond` | `pub fn respond(request: *Request, content: []const u8, options: RespondOptions,) ExpectContinueError!void` |
| `respondUnflushed` | `pub fn respondUnflushed(request: *Request, content: []const u8, options: RespondOptions,) ExpectContinueError!void` |
| `respondStreaming` | `pub fn respondStreaming(request: *Request, buffer: []u8, options: RespondStreamingOptions,) ExpectContinueError!http.BodyWriter` |
| `upgradeRequested` | `pub fn upgradeRequested(request: *const Request) UpgradeRequest` |
| `respondWebSocket` | `pub fn respondWebSocket(request: *Request, options: WebSocketOptions) ExpectContinueError!WebSocket` |
| `readerExpectContinue` | `pub fn readerExpectContinue(request: *Request, buffer: []u8) ExpectContinueError!*Reader` |
| `readerExpectNone` | `pub fn readerExpectNone(request: *Request, buffer: []u8) *Reader` |
| `writeExpectContinue` | `pub fn writeExpectContinue(request: *Request) ExpectContinueError!void` |
| `readSmallMessage` | `pub fn readSmallMessage(ws: *WebSocket) ReadSmallTextMessageError!SmallMessage` |
| `writeMessage` | `pub fn writeMessage(ws: *WebSocket, data: []const u8, op: Opcode) Writer.Error!void` |
| `writeMessageUnflushed` | `pub fn writeMessageUnflushed(ws: *WebSocket, data: []const u8, op: Opcode) Writer.Error!void` |
| `writeMessageVec` | `pub fn writeMessageVec(ws: *WebSocket, data: [][]const u8, op: Opcode) Writer.Error!void` |
| `writeMessageVecUnflushed` | `pub fn writeMessageVecUnflushed(ws: *WebSocket, data: [][]const u8, op: Opcode) Writer.Error!void` |
| `flush` | `pub fn flush(ws: *WebSocket) Writer.Error!void` |

## Io / Dir

| Function | Signature |
|----------|-----------|
| `cwd` | `pub fn cwd() Dir` |
| `init` | `pub fn init(dir: Dir, buffer: []align(@alignOf(usize) ) u8) Reader` |
| `read` | `pub fn read(r: *Reader, io: Io, buffer: []Entry) Error!usize` |
| `next` | `pub fn next(r: *Reader, io: Io) Error!?Entry` |
| `reset` | `pub fn reset(r: *Reader) void` |
| `init` | `pub fn init(dir: Dir, reader_state: Reader.State) Iterator` |
| `next` | `pub fn next(it: *Iterator, io: Io) Error!?Entry` |
| `iterate` | `pub fn iterate(dir: Dir) Iterator` |
| `iterateAssumeFirstIteration` | `pub fn iterateAssumeFirstIteration(dir: Dir) Iterator` |
| `next` | `pub fn next(self: *SelectiveWalker, io: Io) Error!?Walker.Entry` |
| `enter` | `pub fn enter(self: *SelectiveWalker, io: Io, entry: Walker.Entry) !void` |
| `deinit` | `pub fn deinit(self: *SelectiveWalker) void` |
| `leave` | `pub fn leave(self: *SelectiveWalker, io: Io) void` |
| `walkSelectively` | `pub fn walkSelectively(dir: Dir, allocator: Allocator) !SelectiveWalker` |
| `depth` | `pub fn depth(self: Walker.Entry) usize` |
| `next` | `pub fn next(self: *Walker, io: Io) !?Walker.Entry` |
| `deinit` | `pub fn deinit(self: *Walker) void` |
| `leave` | `pub fn leave(self: *Walker, io: Io) void` |
| `walk` | `pub fn walk(dir: Dir, allocator: Allocator) Allocator.Error!Walker` |
| `access` | `pub fn access(dir: Dir, io: Io, sub_path: []const u8, options: AccessOptions) AccessError!void` |
| `accessAbsolute` | `pub fn accessAbsolute(io: Io, absolute_path: []const u8, options: AccessOptions) AccessError!void` |
| `openDir` | `pub fn openDir(dir: Dir, io: Io, sub_path: []const u8, options: OpenOptions) OpenError!Dir` |
| `openDirAbsolute` | `pub fn openDirAbsolute(io: Io, absolute_path: []const u8, options: OpenOptions) OpenError!Dir` |
| `close` | `pub fn close(dir: Dir, io: Io) void` |
| `closeMany` | `pub fn closeMany(io: Io, dirs: []const Dir) void` |
| `openFile` | `pub fn openFile(dir: Dir, io: Io, sub_path: []const u8, options: OpenFileOptions) File.OpenError!File` |
| `openFileAbsolute` | `pub fn openFileAbsolute(io: Io, absolute_path: []const u8, options: OpenFileOptions) File.OpenError!File` |
| `createFile` | `pub fn createFile(dir: Dir, io: Io, sub_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileAbsolute` | `pub fn createFileAbsolute(io: Io, absolute_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `writeFile` | `pub fn writeFile(dir: Dir, io: Io, options: WriteFileOptions) WriteFileError!void` |
| `updateFile` | `pub fn updateFile(source_dir: Dir, io: Io, source_path: []const u8, dest_dir: Dir, /// If directories in this path do not exist, they are created. dest_path: []const u8, options: CopyFileOptions,) !PrevStatus` |
| `readFile` | `pub fn readFile(dir: Dir, io: Io, file_path: []const u8, buffer: []u8) ReadFileError![]u8` |
| `createDir` | `pub fn createDir(dir: Dir, io: Io, sub_path: []const u8, permissions: Permissions) CreateDirError!void` |
| `createDirAbsolute` | `pub fn createDirAbsolute(io: Io, absolute_path: []const u8, permissions: Permissions) CreateDirError!void` |
| `createDirPath` | `pub fn createDirPath(dir: Dir, io: Io, sub_path: []const u8) CreateDirPathError!void` |
| `createDirPathStatus` | `pub fn createDirPathStatus(dir: Dir, io: Io, sub_path: []const u8, permissions: Permissions) CreateDirPathError!CreatePathStatus` |
| `createDirPathOpen` | `pub fn createDirPathOpen(dir: Dir, io: Io, sub_path: []const u8, options: CreateDirPathOpenOptions) CreateDirPathOpenError!Dir` |
| `stat` | `pub fn stat(dir: Dir, io: Io) StatError!Stat` |
| `statFile` | `pub fn statFile(dir: Dir, io: Io, sub_path: []const u8, options: StatFileOptions) StatFileError!Stat` |
| `realPath` | `pub fn realPath(dir: Dir, io: Io, out_buffer: []u8) RealPathError!usize` |
| `realPathFile` | `pub fn realPathFile(dir: Dir, io: Io, sub_path: []const u8, out_buffer: []u8) RealPathFileError!usize` |
| `realPathFileAlloc` | `pub fn realPathFileAlloc(dir: Dir, io: Io, sub_path: []const u8, allocator: Allocator) RealPathFileAllocError![:0]u8` |
| `realPathFileAbsolute` | `pub fn realPathFileAbsolute(io: Io, absolute_path: []const u8, out_buffer: []u8) RealPathFileError!usize` |
| `realPathFileAbsoluteAlloc` | `pub fn realPathFileAbsoluteAlloc(io: Io, absolute_path: []const u8, allocator: Allocator) RealPathFileAllocError![:0]u8` |
| `deleteFile` | `pub fn deleteFile(dir: Dir, io: Io, sub_path: []const u8) DeleteFileError!void` |
| `deleteFileAbsolute` | `pub fn deleteFileAbsolute(io: Io, absolute_path: []const u8) DeleteFileError!void` |
| `deleteDir` | `pub fn deleteDir(dir: Dir, io: Io, sub_path: []const u8) DeleteDirError!void` |
| `deleteDirAbsolute` | `pub fn deleteDirAbsolute(io: Io, absolute_path: []const u8) DeleteDirError!void` |
| `rename` | `pub fn rename(old_dir: Dir, old_sub_path: []const u8, new_dir: Dir, new_sub_path: []const u8, io: Io,) RenameError!void` |
| `renameAbsolute` | `pub fn renameAbsolute(old_path: []const u8, new_path: []const u8, io: Io) RenameError!void` |
| `renamePreserve` | `pub fn renamePreserve(old_dir: Dir, old_sub_path: []const u8, new_dir: Dir, new_sub_path: []const u8, io: Io,) RenamePreserveError!void` |
| `hardLink` | `pub fn hardLink(old_dir: Dir, old_sub_path: []const u8, new_dir: Dir, new_sub_path: []const u8, io: Io, options: HardLinkOptions,) HardLinkError!void` |
| `symLink` | `pub fn symLink(dir: Dir, io: Io, target_path: []const u8, sym_link_path: []const u8, flags: SymLinkFlags,) SymLinkError!void` |
| `symLinkAbsolute` | `pub fn symLinkAbsolute(io: Io, target_path: []const u8, sym_link_path: []const u8, flags: SymLinkFlags,) SymLinkError!void` |
| `symLinkAtomic` | `pub fn symLinkAtomic(dir: Dir, io: Io, target_path: []const u8, sym_link_path: []const u8, flags: SymLinkFlags,) !void` |
| `readLink` | `pub fn readLink(dir: Dir, io: Io, sub_path: []const u8, buffer: []u8) ReadLinkError!usize` |
| `readLinkAbsolute` | `pub fn readLinkAbsolute(io: Io, absolute_path: []const u8, buffer: []u8) ReadLinkError!usize` |
| `readFileAlloc` | `pub fn readFileAlloc(dir: Dir, io: Io, /// On Windows, should be encoded as [WTF-8](https://wtf-8.codeberg.page/) . /// On WASI, should be encoded as valid UTF-8. /// On other platforms, an opaque sequence of bytes with no particular encoding. sub...` |
| `readFileAllocOptions` | `pub fn readFileAllocOptions(dir: Dir, io: Io, /// On Windows, should be encoded as [WTF-8](https://wtf-8.codeberg.page/) . /// On WASI, should be encoded as valid UTF-8. /// On other platforms, an opaque sequence of bytes with no particular encodi...` |
| `deleteTree` | `pub fn deleteTree(dir: Dir, io: Io, sub_path: []const u8) DeleteTreeError!void` |
| `deleteTreeMinStackSize` | `pub fn deleteTreeMinStackSize(dir: Dir, io: Io, sub_path: []const u8) DeleteTreeError!void` |
| `copyFile` | `pub fn copyFile(source_dir: Dir, source_path: []const u8, dest_dir: Dir, dest_path: []const u8, io: Io, options: CopyFileOptions,) CopyFileError!void` |
| `copyFileAbsolute` | `pub fn copyFileAbsolute(source_path: []const u8, dest_path: []const u8, io: Io, options: CopyFileOptions,) !void` |
| `createFileAtomic` | `pub fn createFileAtomic(dir: Dir, io: Io, sub_path: []const u8, options: CreateFileAtomicOptions,) CreateFileAtomicError!File.Atomic` |
| `setPermissions` | `pub fn setPermissions(dir: Dir, io: Io, new_permissions: File.Permissions) SetPermissionsError!void` |
| `setFilePermissions` | `pub fn setFilePermissions(dir: Dir, io: Io, sub_path: []const u8, new_permissions: File.Permissions, options: SetFilePermissionsOptions,) SetFilePermissionsError!void` |
| `setOwner` | `pub fn setOwner(dir: Dir, io: Io, owner: ?File.Uid, group: ?File.Gid) SetOwnerError!void` |
| `setFileOwner` | `pub fn setFileOwner(dir: Dir, io: Io, sub_path: []const u8, owner: ?File.Uid, group: ?File.Gid, options: SetFileOwnerOptions,) SetOwnerError!void` |
| `setTimestamps` | `pub fn setTimestamps(dir: Dir, io: Io, sub_path: []const u8, options: SetTimestampsOptions,) SetTimestampsError!void` |
| `setTimestampsNow` | `pub fn setTimestampsNow(dir: Dir, io: Io, sub_path: []const u8, options: SetTimestampsNowOptions,) SetTimestampsError!void` |

## Io / File

| Function | Signature |
|----------|-----------|
| `stdout` | `pub fn stdout() File` |
| `stderr` | `pub fn stderr() File` |
| `stdin` | `pub fn stdin() File` |
| `stat` | `pub fn stat(file: File, io: Io) StatError!Stat` |
| `isRead` | `pub fn isRead(self: OpenFlags) bool` |
| `isWrite` | `pub fn isWrite(self: OpenFlags) bool` |
| `close` | `pub fn close(file: File, io: Io) void` |
| `closeMany` | `pub fn closeMany(io: Io, files: []const File) void` |
| `sync` | `pub fn sync(file: File, io: Io) SyncError!void` |
| `isTty` | `pub fn isTty(file: File, io: Io) Io.Cancelable!bool` |
| `enableAnsiEscapeCodes` | `pub fn enableAnsiEscapeCodes(file: File, io: Io) EnableAnsiEscapeCodesError!void` |
| `supportsAnsiEscapeCodes` | `pub fn supportsAnsiEscapeCodes(file: File, io: Io) Io.Cancelable!bool` |
| `setLength` | `pub fn setLength(file: File, io: Io, new_length: u64) SetLengthError!void` |
| `length` | `pub fn length(file: File, io: Io) LengthError!u64` |
| `setPermissions` | `pub fn setPermissions(file: File, io: Io, new_permissions: Permissions) SetPermissionsError!void` |
| `setOwner` | `pub fn setOwner(file: File, io: Io, owner: ?Uid, group: ?Gid) SetOwnerError!void` |
| `toAttributes` | `pub fn toAttributes(self: @This() ) windows.FILE.ATTRIBUTE` |
| `readOnly` | `pub fn readOnly(self: @This() ) bool` |
| `setReadOnly` | `pub fn setReadOnly(self: @This() , read_only: bool) @This()` |
| `toMode` | `pub fn toMode(self: @This() ) std.posix.mode_t` |
| `fromMode` | `pub fn fromMode(mode: std.posix.mode_t) @This()` |
| `init` | `pub fn init(optional: ?Io.Timestamp) SetTimestamp` |
| `setTimestamps` | `pub fn setTimestamps(file: File, io: Io, options: SetTimestampsOptions) SetTimestampsError!void` |
| `setTimestampsNow` | `pub fn setTimestampsNow(file: File, io: Io) SetTimestampsError!void` |
| `readStreaming` | `pub fn readStreaming(file: File, io: Io, buffer: []const []u8) ReadStreamingError!usize` |
| `readPositional` | `pub fn readPositional(file: File, io: Io, buffer: []const []u8, offset: u64) ReadPositionalError!usize` |
| `writePositional` | `pub fn writePositional(file: File, io: Io, buffer: []const []const u8, offset: u64) WritePositionalError!usize` |
| `writePositionalAll` | `pub fn writePositionalAll(file: File, io: Io, bytes: []const u8, offset: u64) WritePositionalError!void` |
| `reader` | `pub fn reader(file: File, io: Io, buffer: []u8) Reader` |
| `readPositionalAll` | `pub fn readPositionalAll(file: File, io: Io, buffer: []u8, offset: u64) ReadPositionalError!usize` |
| `readerStreaming` | `pub fn readerStreaming(file: File, io: Io, buffer: []u8) Reader` |
| `writer` | `pub fn writer(file: File, io: Io, buffer: []u8) Writer` |
| `writerStreaming` | `pub fn writerStreaming(file: File, io: Io, buffer: []u8) Writer` |
| `writeStreaming` | `pub fn writeStreaming(file: File, io: Io, header: []const u8, data: []const []const u8, splat: usize) Writer.Error!usize` |
| `writeStreamingAll` | `pub fn writeStreamingAll(file: File, io: Io, bytes: []const u8) Writer.Error!void` |
| `lock` | `pub fn lock(file: File, io: Io, l: Lock) LockError!void` |
| `unlock` | `pub fn unlock(file: File, io: Io) void` |
| `tryLock` | `pub fn tryLock(file: File, io: Io, l: Lock) LockError!bool` |
| `downgradeLock` | `pub fn downgradeLock(file: File, io: Io) LockError!void` |
| `realPath` | `pub fn realPath(file: File, io: Io, out_buffer: []u8) RealPathError!usize` |
| `hardLink` | `pub fn hardLink(file: File, io: Io, new_dir: Dir, new_sub_path: []const u8, options: HardLinkOptions,) HardLinkError!void` |
| `createMemoryMap` | `pub fn createMemoryMap(file: File, io: Io, options: MemoryMap.CreateOptions) MemoryMap.CreateError!MemoryMap` |

## Io / Uring

| Function | Signature |
|----------|-----------|
| `io` | `pub fn io(el: *EventLoop) Io` |
| `init` | `pub fn init(el: *EventLoop, gpa: Allocator) !void` |
| `deinit` | `pub fn deinit(el: *EventLoop) void` |

## Io / Kqueue

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(k: *Kqueue, gpa: Allocator, options: InitOptions) !void` |
| `deinit` | `pub fn deinit(k: *Kqueue) void` |
| `createFileDescriptor` | `pub fn createFileDescriptor() CreateFileDescriptorError!posix.fd_t` |
| `io` | `pub fn io(k: *Kqueue) Io` |
| `kevent` | `pub fn kevent(kq: i32, changelist: []const posix.Kevent, eventlist: []posix.Kevent, timeout: ?*const posix.timespec,) KEventError!usize` |

## Io / Reader

| Function | Signature |
|----------|-----------|
| `limited` | `pub fn limited(r: *Reader, limit: Limit, buffer: []u8) Limited` |
| `fixed` | `pub fn fixed(buffer: []const u8) Reader` |
| `stream` | `pub fn stream(r: *Reader, w: *Writer, limit: Limit) StreamError!usize` |
| `discard` | `pub fn discard(r: *Reader, limit: Limit) Error!usize` |
| `defaultDiscard` | `pub fn defaultDiscard(r: *Reader, limit: Limit) Error!usize` |
| `streamExact` | `pub fn streamExact(r: *Reader, w: *Writer, n: usize) StreamError!void` |
| `streamExact64` | `pub fn streamExact64(r: *Reader, w: *Writer, n: u64) StreamError!void` |
| `streamExactPreserve` | `pub fn streamExactPreserve(r: *Reader, w: *Writer, preserve_len: usize, n: usize) StreamError!void` |
| `streamRemaining` | `pub fn streamRemaining(r: *Reader, w: *Writer) StreamRemainingError!usize` |
| `discardRemaining` | `pub fn discardRemaining(r: *Reader) ShortError!usize` |
| `allocRemaining` | `pub fn allocRemaining(r: *Reader, gpa: Allocator, limit: Limit) LimitedAllocError![]u8` |
| `allocRemainingAlignedSentinel` | `pub fn allocRemainingAlignedSentinel(r: *Reader, gpa: Allocator, limit: Limit, comptime alignment: std.mem.Alignment, comptime sentinel: ?u8,) LimitedAllocError!(if (sentinel) |s| [:s]align(alignment.toByteUnits()) u8 else []align(alignment.toByte...` |
| `appendExact` | `pub fn appendExact(r: *Reader, gpa: Allocator, list: *ArrayList(u8) , n: usize, ) AppendExactError!void` |
| `appendRemaining` | `pub fn appendRemaining(r: *Reader, gpa: Allocator, list: *ArrayList(u8) , limit: Limit, ) LimitedAllocError!void` |
| `appendRemainingAligned` | `pub fn appendRemainingAligned(r: *Reader, gpa: Allocator, comptime alignment: std.mem.Alignment, list: *std.array_list.Aligned(u8, alignment) , limit: Limit, ) LimitedAllocError!void` |
| `appendRemainingUnlimited` | `pub fn appendRemainingUnlimited(r: *Reader, gpa: Allocator, list: *ArrayList(u8) ) UnlimitedAllocError!void` |
| `readVec` | `pub fn readVec(r: *Reader, data: [][]u8) Error!usize` |
| `defaultReadVec` | `pub fn defaultReadVec(r: *Reader, data: [][]u8) Error!usize` |
| `buffered` | `pub fn buffered(r: *Reader) []u8` |
| `bufferedLen` | `pub fn bufferedLen(r: *const Reader) usize` |
| `hashed` | `pub fn hashed(r: *Reader, hasher: anytype, buffer: []u8) Hashed(@TypeOf(hasher))` |
| `readVecAll` | `pub fn readVecAll(r: *Reader, data: [][]u8) Error!void` |
| `peek` | `pub fn peek(r: *Reader, n: usize) Error![]u8` |
| `peekGreedy` | `pub fn peekGreedy(r: *Reader, n: usize) Error![]u8` |
| `toss` | `pub fn toss(r: *Reader, n: usize) void` |
| `tossBuffered` | `pub fn tossBuffered(r: *Reader) void` |
| `take` | `pub fn take(r: *Reader, n: usize) Error![]u8` |
| `takeArray` | `pub fn takeArray(r: *Reader, comptime n: usize) Error!*[n]u8` |
| `peekArray` | `pub fn peekArray(r: *Reader, comptime n: usize) Error!*[n]u8` |
| `discardAll` | `pub fn discardAll(r: *Reader, n: usize) Error!void` |
| `discardAll64` | `pub fn discardAll64(r: *Reader, n: u64) Error!void` |
| `discardShort` | `pub fn discardShort(r: *Reader, n: usize) ShortError!usize` |
| `readSliceAll` | `pub fn readSliceAll(r: *Reader, buffer: []u8) Error!void` |
| `readSliceShort` | `pub fn readSliceShort(r: *Reader, buffer: []u8) ShortError!usize` |
| `readSliceEndian` | `pub fn readSliceEndian(r: *Reader, comptime Elem: type, buffer: []Elem, endian: std.builtin.Endian,) Error!void` |
| `readSliceEndianAlloc` | `pub fn readSliceEndianAlloc(r: *Reader, allocator: Allocator, comptime Elem: type, len: usize, endian: std.builtin.Endian,) ReadAllocError![]Elem` |
| `readAlloc` | `pub fn readAlloc(r: *Reader, allocator: Allocator, len: usize) ReadAllocError![]u8` |
| `takeSentinel` | `pub fn takeSentinel(r: *Reader, comptime sentinel: u8) DelimiterError![:sentinel]u8` |
| `peekSentinel` | `pub fn peekSentinel(r: *Reader, comptime sentinel: u8) DelimiterError![:sentinel]u8` |
| `takeDelimiterInclusive` | `pub fn takeDelimiterInclusive(r: *Reader, delimiter: u8) DelimiterError![]u8` |
| `peekDelimiterInclusive` | `pub fn peekDelimiterInclusive(r: *Reader, delimiter: u8) DelimiterError![]u8` |
| `takeDelimiterExclusive` | `pub fn takeDelimiterExclusive(r: *Reader, delimiter: u8) DelimiterError![]u8` |
| `takeDelimiter` | `pub fn takeDelimiter(r: *Reader, delimiter: u8) error` |
| `peekDelimiterExclusive` | `pub fn peekDelimiterExclusive(r: *Reader, delimiter: u8) DelimiterError![]u8` |
| `streamDelimiter` | `pub fn streamDelimiter(r: *Reader, w: *Writer, delimiter: u8) StreamError!usize` |
| `streamDelimiterEnding` | `pub fn streamDelimiterEnding(r: *Reader, w: *Writer, delimiter: u8,) StreamRemainingError!usize` |
| `streamDelimiterLimit` | `pub fn streamDelimiterLimit(r: *Reader, w: *Writer, delimiter: u8, limit: Limit,) StreamDelimiterLimitError!usize` |
| `discardDelimiterInclusive` | `pub fn discardDelimiterInclusive(r: *Reader, delimiter: u8) Error!usize` |
| `discardDelimiterExclusive` | `pub fn discardDelimiterExclusive(r: *Reader, delimiter: u8) ShortError!usize` |
| `discardDelimiterLimit` | `pub fn discardDelimiterLimit(r: *Reader, delimiter: u8, limit: Limit) DiscardDelimiterLimitError!usize` |
| `fill` | `pub fn fill(r: *Reader, n: usize) Error!void` |
| `fillMore` | `pub fn fillMore(r: *Reader) Error!void` |
| `peekByte` | `pub fn peekByte(r: *Reader) Error!u8` |
| `takeByte` | `pub fn takeByte(r: *Reader) Error!u8` |
| `takeByteSigned` | `pub fn takeByteSigned(r: *Reader) Error!i8` |
| `takeInt` | `pub fn takeInt(r: *Reader, comptime T: type, endian: std.builtin.Endian) Error!T` |
| `peekInt` | `pub fn peekInt(r: *Reader, comptime T: type, endian: std.builtin.Endian) Error!T` |
| `takeVarInt` | `pub fn takeVarInt(r: *Reader, comptime Int: type, endian: std.builtin.Endian, n: usize) Error!Int` |
| `takeStructPointer` | `pub fn takeStructPointer(r: *Reader, comptime T: type) Error!*align(1) T` |
| `peekStructPointer` | `pub fn peekStructPointer(r: *Reader, comptime T: type) Error!*align(1) T` |
| `takeStruct` | `pub fn takeStruct(r: *Reader, comptime T: type, endian: std.builtin.Endian) Error!T` |
| `peekStruct` | `pub fn peekStruct(r: *Reader, comptime T: type, endian: std.builtin.Endian) Error!T` |
| `takeEnum` | `pub fn takeEnum(r: *Reader, comptime Enum: type, endian: std.builtin.Endian) TakeEnumError!Enum` |
| `takeEnumNonexhaustive` | `pub fn takeEnumNonexhaustive(r: *Reader, comptime Enum: type, endian: std.builtin.Endian) Error!Enum` |
| `takeLeb128` | `pub fn takeLeb128(r: *Reader, comptime T: type) TakeLeb128Error!T` |
| `rebase` | `pub fn rebase(r: *Reader, capacity: usize) Error!void` |
| `defaultRebase` | `pub fn defaultRebase(r: *Reader, capacity: usize) Error!void` |
| `Hashed` | `pub fn Hashed(comptime Hasher: type) type` |
| `init` | `pub fn init(in: *Reader, hasher: Hasher, buffer: []u8) @This()` |
| `writableVectorPosix` | `pub fn writableVectorPosix(r: *Reader, buffer: []std.posix.iovec, data: []const []u8) Error!struct` |
| `writableVectorWsa` | `pub fn writableVectorWsa(r: *Reader, buffer: []std.os.windows.ws2_32.WSABUF, data: []const []u8,) Error!struct` |
| `writableVector` | `pub fn writableVector(r: *Reader, buffer: [][]u8, data: []const []u8) Error!struct` |

## Io / RwLock

| Function | Signature |
|----------|-----------|
| `tryLock` | `pub fn tryLock(rl: *RwLock, io: Io) bool` |
| `lockUncancelable` | `pub fn lockUncancelable(rl: *RwLock, io: Io) void` |
| `unlock` | `pub fn unlock(rl: *RwLock, io: Io) void` |
| `tryLockShared` | `pub fn tryLockShared(rl: *RwLock, io: Io) bool` |
| `lockSharedUncancelable` | `pub fn lockSharedUncancelable(rl: *RwLock, io: Io) void` |
| `unlockShared` | `pub fn unlockShared(rl: *RwLock, io: Io) void` |

## Io / Semaphore

| Function | Signature |
|----------|-----------|
| `wait` | `pub fn wait(s: *Semaphore, io: Io) Io.Cancelable!void` |
| `waitUncancelable` | `pub fn waitUncancelable(s: *Semaphore, io: Io) void` |
| `post` | `pub fn post(s: *Semaphore, io: Io) void` |

## Io / Terminal

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(io: Io, file: File, NO_COLOR: bool, CLICOLOR_FORCE: bool) Io.Cancelable!Mode` |
| `setColor` | `pub fn setColor(t: Terminal, color: Color) SetColorError!void` |

## Io / Threaded

| Function | Signature |
|----------|-----------|
| `isInitialized` | `pub fn isInitialized(c: *const Csprng) bool` |
| `init` | `pub fn init(args: process.Args) Argv0` |
| `waitForApcOrAlert` | `pub fn waitForApcOrAlert() void` |
| `init` | `pub fn init(/// Must be threadsafe. Only used for the following functions: /// * `Io.VTable.async` /// * `Io.VTable.concurrent` /// * `Io.VTable.groupAsync` /// * `Io.VTable.groupConcurrent` /// If these functions are avoided, then `Allocator.fail...` |
| `setAsyncLimit` | `pub fn setAsyncLimit(t: *Threaded, new_limit: Io.Limit) void` |
| `deinit` | `pub fn deinit(t: *Threaded) void` |
| `io` | `pub fn io(t: *Threaded) Io` |
| `dirOpenFileWtf16` | `pub fn dirOpenFileWtf16(dir_handle: ?windows.HANDLE, sub_path_w: []const u16, options: OpenFileOptions,) File.OpenError!File` |
| `dirOpenDirWindows` | `pub fn dirOpenDirWindows(dir: Dir, sub_path_w: []const u16, options: Dir.OpenOptions,) Dir.OpenError!Dir` |
| `GetFinalPathNameByHandle` | `pub fn GetFinalPathNameByHandle(hFile: windows.HANDLE, fmt: GetFinalPathNameByHandleFormat, out_buffer: []u16,) GetFinalPathNameByHandleError![]u16` |
| `QueryObjectName` | `pub fn QueryObjectName(handle: windows.HANDLE, out_buffer: []u16) QueryObjectNameError![]u16` |
| `wToPrefixedFileW` | `pub fn wToPrefixedFileW(dir: ?windows.HANDLE, path: [:0]const u16) Wtf16ToPrefixedFileWError!WindowsPathSpace` |
| `sliceToPrefixedFileW` | `pub fn sliceToPrefixedFileW(dir: ?windows.HANDLE, path: []const u8) Wtf8ToPrefixedFileWError!WindowsPathSpace` |
| `span` | `pub fn span(wps: *const WindowsPathSpace) [:0]const u16` |
| `string` | `pub fn string(wps: *const WindowsPathSpace) windows.UNICODE_STRING` |
| `posixAddressFamily` | `pub fn posixAddressFamily(a: *const IpAddress) posix.sa_family_t` |
| `addressFromPosix` | `pub fn addressFromPosix(posix_address: *const PosixAddress) IpAddress` |
| `addressToPosix` | `pub fn addressToPosix(a: *const IpAddress, storage: *PosixAddress) posix.socklen_t` |
| `errnoBug` | `pub fn errnoBug(err: posix.E) Io.UnexpectedError` |
| `posixExecvPath` | `pub fn posixExecvPath(path: [*:0]const u8, child_argv: [*:null]const ?[*:0]const u8, env_block: process.Environ.PosixBlock,) process.ReplaceError` |
| `windowsCreatePipe` | `pub fn windowsCreatePipe(t: *Threaded, options: CreatePipeOptions) ![2]windows.HANDLE` |
| `environString` | `pub fn environString(t: *Threaded, comptime name: []const u8) ?[:0]const u8` |
| `pipe2` | `pub fn pipe2(flags: posix.O) PipeError![2]posix.fd_t` |
| `dup2` | `pub fn dup2(old_fd: posix.fd_t, new_fd: posix.fd_t) DupError!void` |
| `fchdir` | `pub fn fchdir(fd: posix.fd_t) FchdirError!void` |
| `chdir` | `pub fn chdir(dir_path: []const u8) ChdirError!void` |
| `mutexLock` | `pub fn mutexLock(m: *Io.Mutex) void` |
| `mutexUnlock` | `pub fn mutexUnlock(m: *Io.Mutex) void` |

## Io / Writer

| Function | Signature |
|----------|-----------|
| `fixed` | `pub fn fixed(buffer: []u8) Writer` |
| `hashed` | `pub fn hashed(w: *Writer, hasher: anytype, buffer: []u8) Hashed(@TypeOf(hasher))` |
| `buffered` | `pub fn buffered(w: *const Writer) []u8` |
| `countSplat` | `pub fn countSplat(data: []const []const u8, splat: usize) usize` |
| `countSendFileLowerBound` | `pub fn countSendFileLowerBound(n: usize, file_reader: *File.Reader, limit: Limit) ?usize` |
| `writeVec` | `pub fn writeVec(w: *Writer, data: []const []const u8) Error!usize` |
| `writeSplat` | `pub fn writeSplat(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `writeSplatHeader` | `pub fn writeSplatHeader(w: *Writer, header: []const u8, data: []const []const u8, splat: usize,) Error!usize` |
| `writeSplatHeaderLimit` | `pub fn writeSplatHeaderLimit(w: *Writer, header: []const u8, data: []const []const u8, splat: usize, limit: Limit,) Error!usize` |
| `flush` | `pub fn flush(w: *Writer) Error!void` |
| `defaultFlush` | `pub fn defaultFlush(w: *Writer) Error!void` |
| `noopFlush` | `pub fn noopFlush(w: *Writer) Error!void` |
| `rebase` | `pub fn rebase(w: *Writer, preserve: usize, unused_capacity_len: usize) Error!void` |
| `defaultRebase` | `pub fn defaultRebase(w: *Writer, preserve: usize, minimum_len: usize) Error!void` |
| `unusedCapacitySlice` | `pub fn unusedCapacitySlice(w: *const Writer) []u8` |
| `unusedCapacityLen` | `pub fn unusedCapacityLen(w: *const Writer) usize` |
| `writableArray` | `pub fn writableArray(w: *Writer, comptime len: usize) Error!*[len]u8` |
| `writableSlice` | `pub fn writableSlice(w: *Writer, len: usize) Error![]u8` |
| `writableSliceGreedy` | `pub fn writableSliceGreedy(w: *Writer, minimum_len: usize) Error![]u8` |
| `writableSliceGreedyPreserve` | `pub fn writableSliceGreedyPreserve(w: *Writer, preserve: usize, minimum_len: usize) Error![]u8` |
| `writableSlicePreserve` | `pub fn writableSlicePreserve(w: *Writer, preserve: usize, len: usize) Error![]u8` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(w: *Writer, n: usize) Error!void` |
| `undo` | `pub fn undo(w: *Writer, n: usize) void` |
| `advance` | `pub fn advance(w: *Writer, n: usize) void` |
| `writeVecAll` | `pub fn writeVecAll(w: *Writer, data: [][]const u8) Error!void` |
| `writeSplatAll` | `pub fn writeSplatAll(w: *Writer, data: [][]const u8, splat: usize) Error!void` |
| `write` | `pub fn write(w: *Writer, bytes: []const u8) Error!usize` |
| `writeAll` | `pub fn writeAll(w: *Writer, bytes: []const u8) Error!void` |
| `print` | `pub fn print(w: *Writer, comptime fmt: []const u8, args: anytype) Error!void` |
| `writeByte` | `pub fn writeByte(w: *Writer, byte: u8) Error!void` |
| `writeBytePreserve` | `pub fn writeBytePreserve(w: *Writer, preserve: usize, byte: u8) Error!void` |
| `splatByteAll` | `pub fn splatByteAll(w: *Writer, byte: u8, n: usize) Error!void` |
| `splatBytePreserve` | `pub fn splatBytePreserve(w: *Writer, preserve: usize, byte: u8, n: usize) Error!void` |
| `splatByte` | `pub fn splatByte(w: *Writer, byte: u8, n: usize) Error!usize` |
| `splatBytesAll` | `pub fn splatBytesAll(w: *Writer, bytes: []const u8, splat: usize) Error!void` |
| `splatBytes` | `pub fn splatBytes(w: *Writer, bytes: []const u8, n: usize) Error!usize` |
| `writeInt` | `pub fn writeInt(w: *Writer, comptime T: type, value: T, endian: std.builtin.Endian) Error!void` |
| `writeStruct` | `pub fn writeStruct(w: *Writer, value: anytype, endian: std.builtin.Endian) Error!void` |
| `writeSliceEndian` | `pub fn writeSliceEndian(w: *Writer, Elem: type, slice: []const Elem, endian: std.builtin.Endian,) Error!void` |
| `writeSliceSwap` | `pub fn writeSliceSwap(w: *Writer, Elem: type, slice: []const Elem) Error!void` |
| `sendFile` | `pub fn sendFile(w: *Writer, file_reader: *File.Reader, limit: Limit) FileError!usize` |
| `sendFileHeader` | `pub fn sendFileHeader(w: *Writer, header: []const u8, file_reader: *File.Reader, limit: Limit,) FileError!usize` |
| `sendFileReading` | `pub fn sendFileReading(w: *Writer, file_reader: *File.Reader, limit: Limit) FileReadingError!usize` |
| `sendFileAll` | `pub fn sendFileAll(w: *Writer, file_reader: *File.Reader, limit: Limit) FileAllError!usize` |
| `sendFileReadingAll` | `pub fn sendFileReadingAll(w: *Writer, file_reader: *File.Reader, limit: Limit) FileAllError!usize` |
| `alignBuffer` | `pub fn alignBuffer(w: *Writer, buffer: []const u8, width: usize, alignment: std.fmt.Alignment, fill: u8,) Error!void` |
| `alignBufferOptions` | `pub fn alignBufferOptions(w: *Writer, buffer: []const u8, options: std.fmt.Options) Error!void` |
| `printAddress` | `pub fn printAddress(w: *Writer, value: anytype) Error!void` |
| `printValue` | `pub fn printValue(w: *Writer, comptime fmt: []const u8, options: std.fmt.Options, value: anytype, max_depth: usize,) Error!void` |
| `printVector` | `pub fn printVector(w: *Writer, comptime fmt: []const u8, options: std.fmt.Options, value: anytype, max_depth: usize,) Error!void` |
| `printArray` | `pub fn printArray(w: *Writer, comptime fmt: []const u8, options: std.fmt.Options, ptr_to_array: anytype, max_depth: usize,) Error!void` |
| `printInt` | `pub fn printInt(w: *Writer, value: anytype, base: u8, case: std.fmt.Case, options: std.fmt.Options,) Error!void` |
| `printIntAny` | `pub fn printIntAny(w: *Writer, value: anytype, base: u8, case: std.fmt.Case, options: std.fmt.Options,) Error!void` |
| `printAsciiChar` | `pub fn printAsciiChar(w: *Writer, c: u8, options: std.fmt.Options) Error!void` |
| `printAscii` | `pub fn printAscii(w: *Writer, bytes: []const u8, options: std.fmt.Options) Error!void` |
| `printUnicodeCodepoint` | `pub fn printUnicodeCodepoint(w: *Writer, c: u21) Error!void` |
| `printFloat` | `pub fn printFloat(w: *Writer, value: anytype, options: std.fmt.Number) Error!void` |
| `printFloatHexOptions` | `pub fn printFloatHexOptions(w: *Writer, value: anytype, options: std.fmt.Number) Error!void` |
| `printFloatHex` | `pub fn printFloatHex(w: *Writer, value: anytype, case: std.fmt.Case, opt_precision: ?usize) Error!void` |
| `printByteSize` | `pub fn printByteSize(w: *Writer, value: u64, comptime units: ByteSizeUnits, options: std.fmt.Options,) Error!void` |
| `invalidFmtError` | `pub fn invalidFmtError(comptime fmt: []const u8, value: anytype) noreturn` |
| `printHex` | `pub fn printHex(w: *Writer, bytes: []const u8, case: std.fmt.Case) Error!void` |
| `printBase64` | `pub fn printBase64(w: *Writer, bytes: []const u8) Error!void` |
| `writeUleb128` | `pub fn writeUleb128(w: *Writer, value: anytype) Error!void` |
| `writeSleb128` | `pub fn writeSleb128(w: *Writer, value: anytype) Error!void` |
| `writeLeb128` | `pub fn writeLeb128(w: *Writer, value: anytype) Error!void` |
| `format` | `pub fn format(self: SelfType, w: *Writer) Error!void` |
| `failingDrain` | `pub fn failingDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `failingSendFile` | `pub fn failingSendFile(w: *Writer, file_reader: *File.Reader, limit: Limit) FileError!usize` |
| `failingRebase` | `pub fn failingRebase(w: *Writer, preserve: usize, capacity: usize) Error!void` |
| `init` | `pub fn init(buffer: []u8) Discarding` |
| `fullCount` | `pub fn fullCount(d: *const Discarding) u64` |
| `drain` | `pub fn drain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `consume` | `pub fn consume(w: *Writer, n: usize) usize` |
| `consumeAll` | `pub fn consumeAll(w: *Writer) usize` |
| `unimplementedSendFile` | `pub fn unimplementedSendFile(w: *Writer, file_reader: *File.Reader, limit: Limit) FileError!usize` |
| `fixedDrain` | `pub fn fixedDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `unreachableDrain` | `pub fn unreachableDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `unreachableRebase` | `pub fn unreachableRebase(w: *Writer, preserve: usize, capacity: usize) Error!void` |
| `fromArrayList` | `pub fn fromArrayList(array_list: *ArrayList(u8) ) Writer` |
| `toArrayList` | `pub fn toArrayList(w: *Writer) ArrayList(u8)` |
| `Hashed` | `pub fn Hashed(comptime Hasher: type) type` |
| `init` | `pub fn init(out: *Writer, buffer: []u8) @This()` |
| `initHasher` | `pub fn initHasher(out: *Writer, hasher: Hasher, buffer: []u8) @This()` |
| `Hashing` | `pub fn Hashing(comptime Hasher: type) type` |
| `init` | `pub fn init(buffer: []u8) @This()` |
| `initHasher` | `pub fn initHasher(hasher: Hasher, buffer: []u8) @This()` |
| `init` | `pub fn init(allocator: Allocator) Allocating` |
| `initAligned` | `pub fn initAligned(allocator: Allocator, alignment: std.mem.Alignment) Allocating` |
| `initCapacity` | `pub fn initCapacity(allocator: Allocator, capacity: usize) error` |
| `initOwnedSlice` | `pub fn initOwnedSlice(allocator: Allocator, slice: []u8) Allocating` |
| `initOwnedSliceAligned` | `pub fn initOwnedSliceAligned(allocator: Allocator, comptime alignment: std.mem.Alignment, slice: []align(alignment.toByteUnits() ) u8, ) Allocating` |
| `fromArrayList` | `pub fn fromArrayList(allocator: Allocator, array_list: *ArrayList(u8) ) Allocating` |
| `fromArrayListAligned` | `pub fn fromArrayListAligned(allocator: Allocator, comptime alignment: std.mem.Alignment, array_list: *std.array_list.Aligned(u8, alignment) , ) Allocating` |
| `deinit` | `pub fn deinit(a: *Allocating) void` |
| `toArrayList` | `pub fn toArrayList(a: *Allocating) ArrayList(u8)` |
| `toArrayListAligned` | `pub fn toArrayListAligned(a: *Allocating, comptime alignment: std.mem.Alignment,) std.array_list.Aligned(u8, alignment)` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(a: *Allocating, additional_count: usize) Allocator.Error!void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(a: *Allocating, new_capacity: usize) Allocator.Error!void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(a: *Allocating, new_capacity: usize) Allocator.Error!void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(a: *Allocating) Allocator.Error![]u8` |
| `toOwnedSliceSentinel` | `pub fn toOwnedSliceSentinel(a: *Allocating, comptime sentinel: u8) Allocator.Error![:sentinel]u8` |
| `written` | `pub fn written(a: *Allocating) []u8` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(a: *Allocating, new_len: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(a: *Allocating) void` |

## Io / net

| Function | Signature |
|----------|-----------|
| `parseLiteral` | `pub fn parseLiteral(text: []const u8) ParseLiteralError!IpAddress` |
| `parse` | `pub fn parse(text: []const u8, port: u16) !IpAddress` |
| `parseIp4` | `pub fn parseIp4(text: []const u8, port: u16) Ip4Address.ParseError!IpAddress` |
| `parseIp6` | `pub fn parseIp6(text: []const u8, port: u16) Ip6Address.ParseError!IpAddress` |
| `resolve` | `pub fn resolve(io: Io, text: []const u8, port: u16) !IpAddress` |
| `resolveIp6` | `pub fn resolveIp6(io: Io, text: []const u8, port: u16) Ip6Address.ResolveError!IpAddress` |
| `getPort` | `pub fn getPort(a: IpAddress) u16` |
| `setPort` | `pub fn setPort(a: *IpAddress, port: u16) void` |
| `formatResolved` | `pub fn formatResolved(a: IpAddress, io: Io, w: *Io.Writer) Ip6Address.FormatError!void` |
| `format` | `pub fn format(a: IpAddress, w: *Io.Writer) Io.Writer.Error!void` |
| `eql` | `pub fn eql(a: *const IpAddress, b: *const IpAddress) bool` |
| `listen` | `pub fn listen(address: IpAddress, io: Io, options: ListenOptions) ListenError!Server` |
| `bind` | `pub fn bind(address: *const IpAddress, io: Io, options: BindOptions) BindError!Socket` |
| `connect` | `pub fn connect(address: IpAddress, io: Io, options: ConnectOptions) ConnectError!Stream` |
| `loopback` | `pub fn loopback(port: u16) Ip4Address` |
| `unspecified` | `pub fn unspecified(port: u16) Ip4Address` |
| `parse` | `pub fn parse(buffer: []const u8, port: u16) ParseError!Ip4Address` |
| `format` | `pub fn format(a: Ip4Address, w: *Io.Writer) Io.Writer.Error!void` |
| `eql` | `pub fn eql(a: Ip4Address, b: Ip4Address) bool` |
| `loopback` | `pub fn loopback(port: u16) Ip6Address` |
| `unspecified` | `pub fn unspecified(port: u16) Ip6Address` |
| `fromIp4` | `pub fn fromIp4(ip4: Ip4Address) Ip6Address` |
| `fromAny` | `pub fn fromAny(addr: IpAddress) Ip6Address` |
| `parse` | `pub fn parse(text: []const u8) Parsed` |
| `format` | `pub fn format(u: *const Unresolved, w: *Io.Writer) Io.Writer.Error!void` |
| `parse` | `pub fn parse(buffer: []const u8, port: u16) ParseError!Ip6Address` |
| `resolve` | `pub fn resolve(io: Io, buffer: []const u8, port: u16) ResolveError!Ip6Address` |
| `formatResolved` | `pub fn formatResolved(a: Ip6Address, io: Io, w: *Io.Writer) FormatError!void` |
| `format` | `pub fn format(a: Ip6Address, w: *Io.Writer) Io.Writer.Error!void` |
| `eql` | `pub fn eql(a: Ip6Address, b: Ip6Address) bool` |
| `isMultiCast` | `pub fn isMultiCast(a: Ip6Address) bool` |
| `isLinkLocal` | `pub fn isLinkLocal(a: Ip6Address) bool` |
| `isLoopBack` | `pub fn isLoopBack(a: Ip6Address) bool` |
| `isSiteLocal` | `pub fn isSiteLocal(a: Ip6Address) bool` |
| `policy` | `pub fn policy(a: Ip6Address) *const Policy` |
| `scope` | `pub fn scope(a: Ip6Address) u8` |
| `init` | `pub fn init(p: []const u8) InitError!UnixAddress` |
| `listen` | `pub fn listen(ua: *const UnixAddress, io: Io, options: ListenOptions) ListenError!Server` |
| `connect` | `pub fn connect(ua: *const UnixAddress, io: Io) ConnectError!Stream` |
| `toSlice` | `pub fn toSlice(n: *const Name) []const u8` |
| `fromSlice` | `pub fn fromSlice(bytes: []const u8) error` |
| `fromSliceUnchecked` | `pub fn fromSliceUnchecked(bytes: []const u8) Name` |
| `resolve` | `pub fn resolve(n: *const Name, io: Io) ResolveError!Interface` |
| `name` | `pub fn name(i: Interface, io: Io) NameError!Name` |
| `isNone` | `pub fn isNone(i: Interface) bool` |
| `close` | `pub fn close(s: *const Socket, io: Io) void` |
| `closeMany` | `pub fn closeMany(io: Io, sockets: []const Socket) void` |
| `send` | `pub fn send(s: *const Socket, io: Io, dest: *const IpAddress, data: []const u8) SendError!void` |
| `sendMany` | `pub fn sendMany(s: *const Socket, io: Io, messages: []OutgoingMessage, flags: SendFlags) SendError!void` |
| `receive` | `pub fn receive(s: *const Socket, io: Io, buffer: []u8) ReceiveError!IncomingMessage` |
| `receiveTimeout` | `pub fn receiveTimeout(s: *const Socket, io: Io, buffer: []u8, timeout: Io.Timeout,) ReceiveTimeoutError!IncomingMessage` |
| `receiveManyTimeout` | `pub fn receiveManyTimeout(s: *const Socket, io: Io, /// Function assumes each element has initialized `control` field. /// Initializing with `IncomingMessage.init` may be helpful. message_buffer: []IncomingMessage, data_buffer: []u8, flags: Receiv...` |
| `createPair` | `pub fn createPair(io: Io, options: CreatePairOptions) CreatePairError![2]Socket` |
| `close` | `pub fn close(s: *const Stream, io: Io) void` |
| `shutdown` | `pub fn shutdown(s: *const Stream, io: Io, how: ShutdownHow) ShutdownError!void` |
| `init` | `pub fn init(stream: Stream, io: Io, buffer: []u8) Reader` |
| `init` | `pub fn init(stream: Stream, io: Io, buffer: []u8) Writer` |
| `reader` | `pub fn reader(stream: Stream, io: Io, buffer: []u8) Reader` |
| `writer` | `pub fn writer(stream: Stream, io: Io, buffer: []u8) Writer` |
| `deinit` | `pub fn deinit(s: *Server, io: Io) void` |
| `accept` | `pub fn accept(s: *Server, io: Io) AcceptError!Stream` |

## Io / net / HostName

| Function | Signature |
|----------|-----------|
| `validate` | `pub fn validate(bytes: []const u8) ValidateError!void` |
| `init` | `pub fn init(bytes: []const u8) ValidateError!HostName` |
| `sameParentDomain` | `pub fn sameParentDomain(parent_host: HostName, child_host: HostName) bool` |
| `eql` | `pub fn eql(a: HostName, b: HostName) bool` |
| `lookup` | `pub fn lookup(host_name: HostName, io: Io, resolved: *Io.Queue(LookupResult) , options: LookupOptions, ) LookupError!void` |
| `expand` | `pub fn expand(noalias packet: []const u8, start_i: usize, noalias dest_buffer: []u8) ExpandError!struct` |
| `init` | `pub fn init(r: []const u8) Error!DnsResponse` |
| `next` | `pub fn next(dr: *DnsResponse) Error!?Answer` |
| `connect` | `pub fn connect(host_name: HostName, io: Io, port: u16, options: IpAddress.ConnectOptions,) ConnectError!Stream` |
| `connectMany` | `pub fn connectMany(host_name: HostName, io: Io, port: u16, results: *Io.Queue(IpAddress.ConnectError!Stream) , options: IpAddress.ConnectOptions, ) LookupError!void` |
| `init` | `pub fn init(io: Io) !ResolvConf` |
| `parse` | `pub fn parse(rc: *ResolvConf, io: Io, reader: *Io.Reader) !void` |
| `nameservers` | `pub fn nameservers(rc: *const ResolvConf) []const IpAddress` |

## Io / File / Atomic

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(af: *Atomic, io: Io) void` |
| `link` | `pub fn link(af: *Atomic, io: Io) LinkError!void` |
| `replace` | `pub fn replace(af: *Atomic, io: Io) ReplaceError!void` |

## Io / File / MemoryMap

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(io: Io, file: File, options: CreateOptions) CreateError!MemoryMap` |
| `destroy` | `pub fn destroy(mm: *MemoryMap, io: Io) void` |
| `setLength` | `pub fn setLength(mm: *MemoryMap, io: Io, new_len: usize) SetLengthError!void` |
| `read` | `pub fn read(mm: *MemoryMap, io: Io) File.ReadPositionalError!void` |
| `write` | `pub fn write(mm: *MemoryMap, io: Io) File.WritePositionalError!void` |

## Io / File / MultiReader

| Function | Signature |
|----------|-----------|
| `contexts` | `pub fn contexts(s: *Streams) []Context` |
| `storage` | `pub fn storage(s: *Streams) []Io.Operation.Storage` |
| `Buffer` | `pub fn Buffer(comptime n: usize) type` |
| `toStreams` | `pub fn toStreams(b: *@This() ) *Streams` |
| `init` | `pub fn init(mr: *MultiReader, gpa: Allocator, io: Io, streams: *Streams, files: []const File) void` |
| `deinit` | `pub fn deinit(mr: *MultiReader) void` |
| `fileReader` | `pub fn fileReader(mr: *MultiReader, index: usize) *File.Reader` |
| `reader` | `pub fn reader(mr: *MultiReader, index: usize) *Io.Reader` |
| `checkAnyError` | `pub fn checkAnyError(mr: *const MultiReader) UnendingError!void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(mr: *MultiReader, index: usize) Allocator.Error![]u8` |
| `fill` | `pub fn fill(mr: *MultiReader, unused_capacity: usize, timeout: Io.Timeout) FillError!void` |
| `fillRemaining` | `pub fn fillRemaining(mr: *MultiReader, timeout: Io.Timeout) Io.Batch.AwaitConcurrentError!void` |

## Io / File / Reader

| Function | Signature |
|----------|-----------|
| `toStreaming` | `pub fn toStreaming(m: @This() ) @This()` |
| `toSimple` | `pub fn toSimple(m: @This() ) @This()` |
| `initInterface` | `pub fn initInterface(buffer: []u8) Io.Reader` |
| `init` | `pub fn init(file: File, io: Io, buffer: []u8) Reader` |
| `initSize` | `pub fn initSize(file: File, io: Io, buffer: []u8, size: ?u64) Reader` |
| `initStreaming` | `pub fn initStreaming(file: File, io: Io, buffer: []u8) Reader` |
| `getSize` | `pub fn getSize(r: *Reader) SizeError!u64` |
| `seekBy` | `pub fn seekBy(r: *Reader, offset: i64) SeekError!void` |
| `seekTo` | `pub fn seekTo(r: *Reader, offset: u64) SeekError!void` |
| `logicalPos` | `pub fn logicalPos(r: *const Reader) u64` |
| `streamMode` | `pub fn streamMode(r: *Reader, w: *Io.Writer, limit: Io.Limit, mode: Mode) Io.Reader.StreamError!usize` |
| `atEnd` | `pub fn atEnd(r: *Reader) bool` |

## Io / File / Writer

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(file: File, io: Io, buffer: []u8) Writer` |
| `initStreaming` | `pub fn initStreaming(file: File, io: Io, buffer: []u8) Writer` |
| `initDetect` | `pub fn initDetect(file: File, io: Io, buffer: []u8) Io.Cancelable!Writer` |
| `initInterface` | `pub fn initInterface(buffer: []u8) Io.Writer` |
| `moveToReader` | `pub fn moveToReader(w: *Writer) File.Reader` |
| `drain` | `pub fn drain(io_w: *Io.Writer, data: []const []const u8, splat: usize) Io.Writer.Error!usize` |
| `sendFile` | `pub fn sendFile(io_w: *Io.Writer, file_reader: *Io.File.Reader, limit: Io.Limit) Io.Writer.FileError!usize` |
| `seekTo` | `pub fn seekTo(w: *Writer, offset: u64) (SeekError || Io.Writer.Error)!void` |
| `logicalPos` | `pub fn logicalPos(w: *const Writer) u64` |
| `seekToUnbuffered` | `pub fn seekToUnbuffered(w: *Writer, offset: u64) SeekError!void` |
| `end` | `pub fn end(w: *Writer) EndError!void` |
| `flush` | `pub fn flush(w: *Writer) Error!void` |

## Io / Reader / Limited

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(reader: *Reader, limit: Limit, buffer: []u8) Limited` |

## BitStack

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(allocator: Allocator) @This()` |
| `deinit` | `pub fn deinit(self: *@This() ) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *@This() , bit_capacity: usize) Allocator.Error!void` |
| `push` | `pub fn push(self: *@This() , b: u1) Allocator.Error!void` |
| `peek` | `pub fn peek(self: *const @This() ) u1` |
| `pop` | `pub fn pop(self: *@This() ) u1` |
| `pushWithStateAssumeCapacity` | `pub fn pushWithStateAssumeCapacity(buf: []u8, bit_len: *usize, b: u1) void` |
| `peekWithState` | `pub fn peekWithState(buf: []const u8, bit_len: usize) u1` |
| `popWithState` | `pub fn popWithState(buf: []const u8, bit_len: *usize) u1` |

## Build

| Function | Signature |
|----------|-----------|
| `hash` | `pub fn hash(ctx: @This() , k: InitializedDepKey) u64` |
| `eql` | `pub fn eql(_: @This() , lhs: InitializedDepKey, rhs: InitializedDepKey) bool` |
| `create` | `pub fn create(graph: *Graph, build_root: Cache.Directory, cache_root: Cache.Directory, available_deps: AvailableDeps,) error` |
| `resolveInstallPrefix` | `pub fn resolveInstallPrefix(b: *Build, install_prefix: ?[]const u8, dir_list: DirList) void` |
| `addOptions` | `pub fn addOptions(b: *Build) *Step.Options` |
| `addExecutable` | `pub fn addExecutable(b: *Build, options: ExecutableOptions) *Step.Compile` |
| `addObject` | `pub fn addObject(b: *Build, options: ObjectOptions) *Step.Compile` |
| `addLibrary` | `pub fn addLibrary(b: *Build, options: LibraryOptions) *Step.Compile` |
| `addTest` | `pub fn addTest(b: *Build, options: TestOptions) *Step.Compile` |
| `addModule` | `pub fn addModule(b: *Build, name: []const u8, options: Module.CreateOptions) *Module` |
| `createModule` | `pub fn createModule(b: *Build, options: Module.CreateOptions) *Module` |
| `addSystemCommand` | `pub fn addSystemCommand(b: *Build, argv: []const []const u8) *Step.Run` |
| `addRunArtifact` | `pub fn addRunArtifact(b: *Build, exe: *Step.Compile) *Step.Run` |
| `addConfigHeader` | `pub fn addConfigHeader(b: *Build, options: Step.ConfigHeader.Options, values: anytype,) *Step.ConfigHeader` |
| `dupe` | `pub fn dupe(b: *Build, bytes: []const u8) []u8` |
| `dupeInner` | `pub fn dupeInner(allocator: std.mem.Allocator, bytes: []const u8) []u8` |
| `dupeStrings` | `pub fn dupeStrings(b: *Build, strings: []const []const u8) [][]u8` |
| `dupePath` | `pub fn dupePath(b: *Build, bytes: []const u8) []u8` |
| `addWriteFile` | `pub fn addWriteFile(b: *Build, file_path: []const u8, data: []const u8) *Step.WriteFile` |
| `addNamedWriteFiles` | `pub fn addNamedWriteFiles(b: *Build, name: []const u8) *Step.WriteFile` |
| `addNamedLazyPath` | `pub fn addNamedLazyPath(b: *Build, name: []const u8, lp: LazyPath) void` |
| `addTempFiles` | `pub fn addTempFiles(b: *Build) *Step.WriteFile` |
| `addMutateFiles` | `pub fn addMutateFiles(b: *Build, tmp_path: LazyPath) *Step.WriteFile` |
| `addWriteFiles` | `pub fn addWriteFiles(b: *Build) *Step.WriteFile` |
| `addUpdateSourceFiles` | `pub fn addUpdateSourceFiles(b: *Build) *Step.UpdateSourceFiles` |
| `addFail` | `pub fn addFail(b: *Build, error_msg: []const u8) *Step.Fail` |
| `addFmt` | `pub fn addFmt(b: *Build, options: Step.Fmt.Options) *Step.Fmt` |
| `addTranslateC` | `pub fn addTranslateC(b: *Build, options: Step.TranslateC.Options) *Step.TranslateC` |
| `getInstallStep` | `pub fn getInstallStep(b: *Build) *Step` |
| `getUninstallStep` | `pub fn getUninstallStep(b: *Build) *Step` |
| `option` | `pub fn option(b: *Build, comptime T: type, name_raw: []const u8, description_raw: []const u8) ?T` |
| `step` | `pub fn step(b: *Build, name: []const u8, description: []const u8) *Step` |
| `standardOptimizeOption` | `pub fn standardOptimizeOption(b: *Build, options: StandardOptimizeOptionOptions) std.builtin.OptimizeMode` |
| `standardTargetOptions` | `pub fn standardTargetOptions(b: *Build, args: StandardTargetOptionsArgs) ResolvedTarget` |
| `parseTargetQuery` | `pub fn parseTargetQuery(options: std.Target.Query.ParseOptions) error` |
| `standardTargetOptionsQueryOnly` | `pub fn standardTargetOptionsQueryOnly(b: *Build, args: StandardTargetOptionsArgs) Target.Query` |
| `addUserInputOption` | `pub fn addUserInputOption(b: *Build, name_raw: []const u8, value_raw: []const u8) error` |
| `addUserInputFlag` | `pub fn addUserInputFlag(b: *Build, name_raw: []const u8) error` |
| `validateUserInputDidItFail` | `pub fn validateUserInputDidItFail(b: *Build) bool` |
| `installArtifact` | `pub fn installArtifact(b: *Build, artifact: *Step.Compile) void` |
| `addInstallArtifact` | `pub fn addInstallArtifact(b: *Build, artifact: *Step.Compile, options: Step.InstallArtifact.Options,) *Step.InstallArtifact` |
| `installFile` | `pub fn installFile(b: *Build, src_path: []const u8, dest_rel_path: []const u8) void` |
| `installDirectory` | `pub fn installDirectory(b: *Build, options: Step.InstallDir.Options) void` |
| `installBinFile` | `pub fn installBinFile(b: *Build, src_path: []const u8, dest_rel_path: []const u8) void` |
| `installLibFile` | `pub fn installLibFile(b: *Build, src_path: []const u8, dest_rel_path: []const u8) void` |
| `addObjCopy` | `pub fn addObjCopy(b: *Build, source: LazyPath, options: Step.ObjCopy.Options) *Step.ObjCopy` |
| `addInstallFile` | `pub fn addInstallFile(b: *Build, source: LazyPath, dest_rel_path: []const u8) *Step.InstallFile` |
| `addInstallBinFile` | `pub fn addInstallBinFile(b: *Build, source: LazyPath, dest_rel_path: []const u8) *Step.InstallFile` |
| `addInstallLibFile` | `pub fn addInstallLibFile(b: *Build, source: LazyPath, dest_rel_path: []const u8) *Step.InstallFile` |
| `addInstallHeaderFile` | `pub fn addInstallHeaderFile(b: *Build, source: LazyPath, dest_rel_path: []const u8) *Step.InstallFile` |
| `addInstallFileWithDir` | `pub fn addInstallFileWithDir(b: *Build, source: LazyPath, install_dir: InstallDir, dest_rel_path: []const u8,) *Step.InstallFile` |
| `addInstallDirectory` | `pub fn addInstallDirectory(b: *Build, options: Step.InstallDir.Options) *Step.InstallDir` |
| `addCheckFile` | `pub fn addCheckFile(b: *Build, file_source: LazyPath, options: Step.CheckFile.Options,) *Step.CheckFile` |
| `truncateFile` | `pub fn truncateFile(b: *Build, dest_path: []const u8) (Io.Dir.CreateDirError || Io.Dir.StatFileError)!void` |
| `path` | `pub fn path(b: *Build, sub_path: []const u8) LazyPath` |
| `pathFromRoot` | `pub fn pathFromRoot(b: *Build, sub_path: []const u8) []u8` |
| `pathJoin` | `pub fn pathJoin(b: *Build, paths: []const []const u8) []u8` |
| `pathResolve` | `pub fn pathResolve(b: *Build, paths: []const []const u8) []u8` |
| `fmt` | `pub fn fmt(b: *Build, comptime format: []const u8, args: anytype) []u8` |
| `findProgram` | `pub fn findProgram(b: *Build, names: []const []const u8, paths: []const []const u8) error` |
| `runAllowFail` | `pub fn runAllowFail(b: *Build, argv: []const []const u8, out_code: *u8, stderr_behavior: std.process.SpawnOptions.StdIo,) RunError![]u8` |
| `run` | `pub fn run(b: *Build, argv: []const []const u8) []u8` |
| `addSearchPrefix` | `pub fn addSearchPrefix(b: *Build, search_prefix: []const u8) void` |
| `getInstallPath` | `pub fn getInstallPath(b: *Build, dir: InstallDir, dest_rel_path: []const u8) []const u8` |
| `artifact` | `pub fn artifact(d: *Dependency, name: []const u8) *Step.Compile` |
| `module` | `pub fn module(d: *Dependency, name: []const u8) *Module` |
| `namedWriteFiles` | `pub fn namedWriteFiles(d: *Dependency, name: []const u8) *Step.WriteFile` |
| `namedLazyPath` | `pub fn namedLazyPath(d: *Dependency, name: []const u8) LazyPath` |
| `path` | `pub fn path(d: *Dependency, sub_path: []const u8) LazyPath` |
| `lazyDependency` | `pub fn lazyDependency(b: *Build, name: []const u8, args: anytype) ?*Dependency` |
| `dependency` | `pub fn dependency(b: *Build, name: []const u8, args: anytype) *Dependency` |
| `lazyImport` | `pub fn lazyImport(b: *Build, /// The build.zig struct of the package importing the dependency. /// When calling this function from the `build` function of a build.zig file's, you normally /// pass `@This() `. comptime asking_build_zig: type, compt...` |
| `dependencyFromBuildZig` | `pub fn dependencyFromBuildZig(b: *Build, /// The build.zig struct of the dependency, normally obtained by `@import` of the dependency. /// If called from the build.zig file itself, use `@This` to obtain a reference to the struct. comptime build_zi...` |
| `runBuild` | `pub fn runBuild(b: *Build, build_zig: anytype) anyerror!void` |
| `getPath` | `pub fn getPath(gen: GeneratedFile) []const u8` |
| `getPath2` | `pub fn getPath2(gen: GeneratedFile, src_builder: *Build, asking_step: ?*Step) []const u8` |
| `getPath3` | `pub fn getPath3(gen: GeneratedFile, src_builder: *Build, asking_step: ?*Step) Io.Cancelable![]const u8` |
| `dirname` | `pub fn dirname(lazy_path: LazyPath) LazyPath` |
| `path` | `pub fn path(lazy_path: LazyPath, b: *Build, sub_path: []const u8) LazyPath` |
| `join` | `pub fn join(lazy_path: LazyPath, arena: Allocator, sub_path: []const u8) Allocator.Error!LazyPath` |
| `getDisplayName` | `pub fn getDisplayName(lazy_path: LazyPath) []const u8` |
| `addStepDependencies` | `pub fn addStepDependencies(lazy_path: LazyPath, other_step: *Step) void` |
| `getPath` | `pub fn getPath(lazy_path: LazyPath, src_builder: *Build) []const u8` |
| `getPath2` | `pub fn getPath2(lazy_path: LazyPath, src_builder: *Build, asking_step: ?*Step) []const u8` |
| `getPath3` | `pub fn getPath3(lazy_path: LazyPath, src_builder: *Build, asking_step: ?*Step) Cache.Path` |
| `getPath4` | `pub fn getPath4(lazy_path: LazyPath, src_builder: *Build, asking_step: ?*Step) Io.Cancelable!Cache.Path` |
| `basename` | `pub fn basename(lazy_path: LazyPath, src_builder: *Build, asking_step: ?*Step) []const u8` |
| `dupe` | `pub fn dupe(lazy_path: LazyPath, b: *Build) LazyPath` |
| `dumpBadGetPathHelp` | `pub fn dumpBadGetPathHelp(s: *Step, t: Io.Terminal, src_builder: *Build, asking_step: ?*Step) anyerror!void` |
| `dupe` | `pub fn dupe(dir: InstallDir, builder: *Build) InstallDir` |
| `tmpPath` | `pub fn tmpPath(b: *Build) LazyPath` |
| `resolveTargetQuery` | `pub fn resolveTargetQuery(b: *Build, query: Target.Query) ResolvedTarget` |
| `wantSharedLibSymLinks` | `pub fn wantSharedLibSymLinks(target: Target) bool` |
| `systemIntegrationOption` | `pub fn systemIntegrationOption(b: *Build, name: []const u8, config: SystemIntegrationOptionConfig,) bool` |

## DoublyLinkedList

| Function | Signature |
|----------|-----------|
| `insertAfter` | `pub fn insertAfter(list: *DoublyLinkedList, existing_node: *Node, new_node: *Node) void` |
| `insertBefore` | `pub fn insertBefore(list: *DoublyLinkedList, existing_node: *Node, new_node: *Node) void` |
| `concatByMoving` | `pub fn concatByMoving(list1: *DoublyLinkedList, list2: *DoublyLinkedList) void` |
| `append` | `pub fn append(list: *DoublyLinkedList, new_node: *Node) void` |
| `prepend` | `pub fn prepend(list: *DoublyLinkedList, new_node: *Node) void` |
| `remove` | `pub fn remove(list: *DoublyLinkedList, node: *Node) void` |
| `pop` | `pub fn pop(list: *DoublyLinkedList) ?*Node` |
| `popFirst` | `pub fn popFirst(list: *DoublyLinkedList) ?*Node` |
| `len` | `pub fn len(list: DoublyLinkedList) usize` |

## Progress

| Function | Signature |
|----------|-----------|
| `unwrap` | `pub fn unwrap(i: @This() ) ?Index` |
| `toOptional` | `pub fn toOptional(i: @This() ) OptionalIndex` |
| `start` | `pub fn start(node: Node, name: []const u8, estimated_total_items: usize) Node` |
| `startFmt` | `pub fn startFmt(node: Node, estimated_total_items: usize, comptime format: []const u8, args: anytype) Node` |
| `completeOne` | `pub fn completeOne(n: Node) void` |
| `setName` | `pub fn setName(n: Node, new_name: []const u8) void` |
| `getName` | `pub fn getName(n: Node) [max_name_len]u8` |
| `setCompletedItems` | `pub fn setCompletedItems(n: Node, completed_items: usize) void` |
| `setEstimatedTotalItems` | `pub fn setEstimatedTotalItems(n: Node, count: usize) void` |
| `increaseEstimatedTotalItems` | `pub fn increaseEstimatedTotalItems(n: Node, count: usize) void` |
| `end` | `pub fn end(n: Node) void` |
| `setIpcFile` | `pub fn setIpcFile(node: Node, expected_io_userdata: ?*anyopaque, file: Io.File) void` |
| `setIpcIndex` | `pub fn setIpcIndex(node: Node, ipc_index: Ipc.Index) void` |
| `takeIpcIndex` | `pub fn takeIpcIndex(node: Node) ?Ipc.Index` |
| `start` | `pub fn start(io: Io, options: Options) Node` |
| `setStatus` | `pub fn setStatus(new_status: Status) void` |
| `clearWrittenWithEscapeCodes` | `pub fn clearWrittenWithEscapeCodes(file_writer: *Io.File.Writer) Io.Writer.Error!void` |

## SemanticVersion

| Function | Signature |
|----------|-----------|
| `includesVersion` | `pub fn includesVersion(self: Range, ver: Version) bool` |
| `isAtLeast` | `pub fn isAtLeast(self: Range, ver: Version) ?bool` |
| `order` | `pub fn order(lhs: Version, rhs: Version) std.math.Order` |
| `parse` | `pub fn parse(text: []const u8) !Version` |
| `format` | `pub fn format(self: Version, w: *std.Io.Writer) std.Io.Writer.Error!void` |

## SinglyLinkedList

| Function | Signature |
|----------|-----------|
| `insertAfter` | `pub fn insertAfter(node: *Node, new_node: *Node) void` |
| `removeNext` | `pub fn removeNext(node: *Node) ?*Node` |
| `findLast` | `pub fn findLast(node: *Node) *Node` |
| `countChildren` | `pub fn countChildren(node: *const Node) usize` |
| `reverse` | `pub fn reverse(indirect: *?*Node) void` |
| `prepend` | `pub fn prepend(list: *SinglyLinkedList, new_node: *Node) void` |
| `remove` | `pub fn remove(list: *SinglyLinkedList, node: *Node) void` |
| `popFirst` | `pub fn popFirst(list: *SinglyLinkedList) ?*Node` |
| `len` | `pub fn len(list: SinglyLinkedList) usize` |

## Target

| Function | Signature |
|----------|-----------|
| `isDarwin` | `pub fn isDarwin(tag: Tag) bool` |
| `isBSD` | `pub fn isBSD(tag: Tag) bool` |
| `exeFileExt` | `pub fn exeFileExt(tag: Tag, arch: Cpu.Arch) [:0]const u8` |
| `staticLibSuffix` | `pub fn staticLibSuffix(tag: Tag, abi: Abi) [:0]const u8` |
| `dynamicLibSuffix` | `pub fn dynamicLibSuffix(tag: Tag) [:0]const u8` |
| `libPrefix` | `pub fn libPrefix(tag: Os.Tag, abi: Abi) [:0]const u8` |
| `defaultVersionRange` | `pub fn defaultVersionRange(tag: Tag, arch: Cpu.Arch, abi: Abi) Os` |
| `versionRangeTag` | `pub fn versionRangeTag(tag: Tag) @typeInfo(TaggedVersionRange).@"union".tag_type.?` |
| `isAtLeast` | `pub fn isAtLeast(ver: WindowsVersion, min_ver: WindowsVersion) bool` |
| `includesVersion` | `pub fn includesVersion(range: Range, ver: WindowsVersion) bool` |
| `isAtLeast` | `pub fn isAtLeast(range: Range, min_ver: WindowsVersion) ?bool` |
| `parse` | `pub fn parse(str: []const u8) !WindowsVersion` |
| `format` | `pub fn format(wv: WindowsVersion, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `includesVersion` | `pub fn includesVersion(range: HurdVersionRange, ver: std.SemanticVersion) bool` |
| `isAtLeast` | `pub fn isAtLeast(range: HurdVersionRange, ver: std.SemanticVersion) ?bool` |
| `includesVersion` | `pub fn includesVersion(range: LinuxVersionRange, ver: std.SemanticVersion) bool` |
| `isAtLeast` | `pub fn isAtLeast(range: LinuxVersionRange, ver: std.SemanticVersion) ?bool` |
| `default` | `pub fn default(arch: Cpu.Arch, tag: Tag, abi: Abi) VersionRange` |
| `gnuLibCVersion` | `pub fn gnuLibCVersion(range: TaggedVersionRange) ?std.SemanticVersion` |
| `versionRange` | `pub fn versionRange(os: Os) TaggedVersionRange` |
| `isAtLeast` | `pub fn isAtLeast(os: Os, comptime tag: Tag, ver: switch (tag.versionRangeTag() )` |
| `default` | `pub fn default(arch: Cpu.Arch, os_tag: Os.Tag) Abi` |
| `isGnu` | `pub fn isGnu(abi: Abi) bool` |
| `isMusl` | `pub fn isMusl(abi: Abi) bool` |
| `isOpenHarmony` | `pub fn isOpenHarmony(abi: Abi) bool` |
| `isAndroid` | `pub fn isAndroid(abi: Abi) bool` |
| `float` | `pub fn float(abi: Abi) Float` |
| `fileExt` | `pub fn fileExt(of: ObjectFormat, arch: Cpu.Arch) [:0]const u8` |
| `default` | `pub fn default(os_tag: Os.Tag, arch: Cpu.Arch) ObjectFormat` |
| `toElfMachine` | `pub fn toElfMachine(target: *const Target) std.elf.EM` |
| `toCoffMachine` | `pub fn toCoffMachine(target: *const Target) std.coff.IMAGE.FILE.MACHINE` |
| `isEmpty` | `pub fn isEmpty(set: Set) bool` |
| `count` | `pub fn count(set: Set) std.math.IntFittingRange(0, needed_bit_count)` |
| `isEnabled` | `pub fn isEnabled(set: Set, arch_feature_index: Index) bool` |
| `addFeature` | `pub fn addFeature(set: *Set, arch_feature_index: Index) void` |
| `addFeatureSet` | `pub fn addFeatureSet(set: *Set, other_set: Set) void` |
| `removeFeature` | `pub fn removeFeature(set: *Set, arch_feature_index: Index) void` |
| `removeFeatureSet` | `pub fn removeFeatureSet(set: *Set, other_set: Set) void` |
| `populateDependencies` | `pub fn populateDependencies(set: *Set, all_features_list: []const Cpu.Feature) void` |
| `asBytes` | `pub fn asBytes(set: *const Set) *const [byte_count]u8` |
| `eql` | `pub fn eql(set: Set, other_set: Set) bool` |
| `isSuperSetOf` | `pub fn isSuperSetOf(set: Set, other_set: Set) bool` |
| `FeatureSetFns` | `pub fn FeatureSetFns(comptime F: type) type` |
| `featureSet` | `pub fn featureSet(features: []const F) Set` |
| `featureSetHas` | `pub fn featureSetHas(set: Set, feature: F) bool` |
| `featureSetHasAny` | `pub fn featureSetHasAny(set: Set, features: anytype) bool` |
| `featureSetHasAll` | `pub fn featureSetHasAll(set: Set, features: anytype) bool` |
| `family` | `pub fn family(arch: Arch) Family` |
| `isX86` | `pub fn isX86(arch: Arch) bool` |
| `isArm` | `pub fn isArm(arch: Arch) bool` |
| `isThumb` | `pub fn isThumb(arch: Arch) bool` |
| `isAARCH64` | `pub fn isAARCH64(arch: Arch) bool` |
| `isArc` | `pub fn isArc(arch: Arch) bool` |
| `isHppa` | `pub fn isHppa(arch: Arch) bool` |
| `isWasm` | `pub fn isWasm(arch: Arch) bool` |
| `isLoongArch` | `pub fn isLoongArch(arch: Arch) bool` |
| `isRISCV` | `pub fn isRISCV(arch: Arch) bool` |
| `isRiscv32` | `pub fn isRiscv32(arch: Arch) bool` |
| `isRiscv64` | `pub fn isRiscv64(arch: Arch) bool` |
| `isMicroblaze` | `pub fn isMicroblaze(arch: Arch) bool` |
| `isMIPS` | `pub fn isMIPS(arch: Arch) bool` |
| `isMIPS32` | `pub fn isMIPS32(arch: Arch) bool` |
| `isMIPS64` | `pub fn isMIPS64(arch: Arch) bool` |
| `isPowerPC` | `pub fn isPowerPC(arch: Arch) bool` |
| `isPowerPC32` | `pub fn isPowerPC32(arch: Arch) bool` |
| `isPowerPC64` | `pub fn isPowerPC64(arch: Arch) bool` |
| `isSPARC` | `pub fn isSPARC(arch: Arch) bool` |
| `isSpirV` | `pub fn isSpirV(arch: Arch) bool` |
| `isSh` | `pub fn isSh(arch: Arch) bool` |
| `isBpf` | `pub fn isBpf(arch: Arch) bool` |
| `isNvptx` | `pub fn isNvptx(arch: Arch) bool` |
| `isXtensa` | `pub fn isXtensa(arch: Arch) bool` |
| `parseCpuModel` | `pub fn parseCpuModel(arch: Arch, cpu_name: []const u8) !*const Cpu.Model` |
| `endian` | `pub fn endian(arch: Arch) std.builtin.Endian` |
| `allFeaturesList` | `pub fn allFeaturesList(arch: Arch) []const Cpu.Feature` |
| `allCpuModels` | `pub fn allCpuModels(arch: Arch) []const *const Cpu.Model` |
| `plan9Ext` | `pub fn plan9Ext(arch: Cpu.Arch) [:0]const u8` |
| `fromCallingConvention` | `pub fn fromCallingConvention(cc: std.builtin.CallingConvention.Tag) []const Arch` |
| `toCpu` | `pub fn toCpu(model: *const Model, arch: Arch) Cpu` |
| `generic` | `pub fn generic(arch: Arch) *const Model` |
| `baseline` | `pub fn baseline(arch: Arch, os: Os) *const Model` |
| `baseline` | `pub fn baseline(arch: Arch, os: Os) Cpu` |
| `has` | `pub fn has(cpu: Cpu, comptime family: Arch.Family, feature: @field(Target, @tagName(family) ).Feature) bool` |
| `hasAny` | `pub fn hasAny(cpu: Cpu, comptime family: Arch.Family, features: []const @field(Target, @tagName(family) ).Feature) bool` |
| `hasAll` | `pub fn hasAll(cpu: Cpu, comptime family: Arch.Family, features: []const @field(Target, @tagName(family) ).Feature) bool` |
| `zigTriple` | `pub fn zigTriple(target: *const Target, allocator: Allocator) Allocator.Error![]u8` |
| `hurdTupleSimple` | `pub fn hurdTupleSimple(allocator: Allocator, arch: Cpu.Arch, abi: Abi) ![]u8` |
| `hurdTuple` | `pub fn hurdTuple(target: *const Target, allocator: Allocator) ![]u8` |
| `linuxTripleSimple` | `pub fn linuxTripleSimple(allocator: Allocator, arch: Cpu.Arch, os_tag: Os.Tag, abi: Abi) ![]u8` |
| `linuxTriple` | `pub fn linuxTriple(target: *const Target, allocator: Allocator) ![]u8` |
| `exeFileExt` | `pub fn exeFileExt(target: *const Target) [:0]const u8` |
| `staticLibSuffix` | `pub fn staticLibSuffix(target: *const Target) [:0]const u8` |
| `dynamicLibSuffix` | `pub fn dynamicLibSuffix(target: *const Target) [:0]const u8` |
| `libPrefix` | `pub fn libPrefix(target: *const Target) [:0]const u8` |
| `isMinGW` | `pub fn isMinGW(target: *const Target) bool` |
| `isGnuLibC` | `pub fn isGnuLibC(target: *const Target) bool` |
| `isMuslLibC` | `pub fn isMuslLibC(target: *const Target) bool` |
| `isBionicLibC` | `pub fn isBionicLibC(target: *const Target) bool` |
| `isDarwinLibC` | `pub fn isDarwinLibC(target: *const Target) bool` |
| `isFreeBSDLibC` | `pub fn isFreeBSDLibC(target: *const Target) bool` |
| `isNetBSDLibC` | `pub fn isNetBSDLibC(target: *const Target) bool` |
| `isOpenBSDLibC` | `pub fn isOpenBSDLibC(target: *const Target) bool` |
| `isWasiLibC` | `pub fn isWasiLibC(target: *const Target) bool` |
| `requiresLibC` | `pub fn requiresLibC(target: *const Target) bool` |
| `supportsAddressSpace` | `pub fn supportsAddressSpace(target: Target, address_space: std.builtin.AddressSpace, context: ?AddressSpaceContext,) bool` |
| `init` | `pub fn init(maybe_path: ?[]const u8) DynamicLinker` |
| `initFmt` | `pub fn initFmt(comptime fmt_str: []const u8, args: anytype) !DynamicLinker` |
| `get` | `pub fn get(dl: *const DynamicLinker) ?[]const u8` |
| `set` | `pub fn set(dl: *DynamicLinker, maybe_path: ?[]const u8) void` |
| `setFmt` | `pub fn setFmt(dl: *DynamicLinker, comptime fmt_str: []const u8, args: anytype) !void` |
| `eql` | `pub fn eql(lhs: DynamicLinker, rhs: DynamicLinker) bool` |
| `kind` | `pub fn kind(os: Os.Tag) Kind` |
| `standard` | `pub fn standard(cpu: Cpu, os: Os, abi: Abi) DynamicLinker` |
| `standardDynamicLinkerPath` | `pub fn standardDynamicLinkerPath(target: *const Target) DynamicLinker` |
| `ptrBitWidth_cpu_abi` | `pub fn ptrBitWidth_cpu_abi(cpu: Cpu, abi: Abi) u16` |
| `ptrBitWidth_arch_abi` | `pub fn ptrBitWidth_arch_abi(cpu_arch: Cpu.Arch, abi: Abi) u16` |
| `ptrBitWidth` | `pub fn ptrBitWidth(target: *const Target) u16` |
| `stackAlignment` | `pub fn stackAlignment(target: *const Target) u16` |
| `stackGrowth` | `pub fn stackGrowth(target: *const Target) StackGrowth` |
| `cCharSignedness` | `pub fn cCharSignedness(target: *const Target) std.builtin.Signedness` |
| `cTypeByteSize` | `pub fn cTypeByteSize(t: *const Target, c_type: CType) u16` |
| `cTypeBitSize` | `pub fn cTypeBitSize(target: *const Target, c_type: CType) u16` |
| `cTypeAlignment` | `pub fn cTypeAlignment(target: *const Target, c_type: CType) u16` |
| `cTypePreferredAlignment` | `pub fn cTypePreferredAlignment(target: *const Target, c_type: CType) u16` |
| `cMaxIntAlignment` | `pub fn cMaxIntAlignment(target: *const Target) u16` |
| `cCallingConvention` | `pub fn cCallingConvention(target: *const Target) ?std.builtin.CallingConvention` |

## Uri

| Function | Signature |
|----------|-----------|
| `getHost` | `pub fn getHost(uri: Uri, buffer: *[HostName.max_len]u8) GetHostError!HostName` |
| `getHostAlloc` | `pub fn getHostAlloc(uri: Uri, arena: Allocator) GetHostAllocError!HostName` |
| `isEmpty` | `pub fn isEmpty(component: Component) bool` |
| `toRaw` | `pub fn toRaw(component: Component, buffer: []u8) error` |
| `toRawMaybeAlloc` | `pub fn toRawMaybeAlloc(component: Component, arena: Allocator) Allocator.Error![]const u8` |
| `formatRaw` | `pub fn formatRaw(component: Component, w: *Writer) Writer.Error!void` |
| `formatEscaped` | `pub fn formatEscaped(component: Component, w: *Writer) Writer.Error!void` |
| `formatUser` | `pub fn formatUser(component: Component, w: *Writer) Writer.Error!void` |
| `formatPassword` | `pub fn formatPassword(component: Component, w: *Writer) Writer.Error!void` |
| `formatHost` | `pub fn formatHost(component: Component, w: *Writer) Writer.Error!void` |
| `formatPath` | `pub fn formatPath(component: Component, w: *Writer) Writer.Error!void` |
| `formatQuery` | `pub fn formatQuery(component: Component, w: *Writer) Writer.Error!void` |
| `formatFragment` | `pub fn formatFragment(component: Component, w: *Writer) Writer.Error!void` |
| `percentEncode` | `pub fn percentEncode(w: *Writer, raw: []const u8, comptime isValidChar: fn (u8) bool) Writer.Error!void` |
| `percentDecodeBackwards` | `pub fn percentDecodeBackwards(output: []u8, input: []const u8) []u8` |
| `percentDecodeInPlace` | `pub fn percentDecodeInPlace(buffer: []u8) []u8` |
| `parseAfterScheme` | `pub fn parseAfterScheme(scheme: []const u8, text: []const u8) ParseError!Uri` |
| `format` | `pub fn format(uri: *const Uri, writer: *Writer) Writer.Error!void` |
| `writeToStream` | `pub fn writeToStream(uri: *const Uri, writer: *Writer, flags: Format.Flags) Writer.Error!void` |
| `default` | `pub fn default(f: Format, writer: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(uri: *const Uri, flags: Format.Flags) std.fmt.Alt(Format, Format.default)` |
| `parse` | `pub fn parse(text: []const u8) ParseError!Uri` |
| `resolveInPlace` | `pub fn resolveInPlace(base: Uri, new_len: usize, aux_buf: *[]u8) ResolveInPlaceError!Uri` |

## array_hash_map

| Function | Signature |
|----------|-----------|
| `StringArrayHashMap` | `pub fn StringArrayHashMap(comptime V: type) type` |
| `StringArrayHashMapUnmanaged` | `pub fn StringArrayHashMapUnmanaged(comptime V: type) type` |
| `hash` | `pub fn hash(self: @This() , s: []const u8) u32` |
| `eql` | `pub fn eql(self: @This() , a: []const u8, b: []const u8, b_index: usize) bool` |
| `eqlString` | `pub fn eqlString(a: []const u8, b: []const u8) bool` |
| `hashString` | `pub fn hashString(s: []const u8) u32` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `initContext` | `pub fn initContext(allocator: Allocator, ctx: Context) Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `lockPointers` | `pub fn lockPointers(self: *Self) void` |
| `unlockPointers` | `pub fn unlockPointers(self: *Self) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self) void` |
| `count` | `pub fn count(self: Self) usize` |
| `keys` | `pub fn keys(self: Self) []K` |
| `values` | `pub fn values(self: Self) []V` |
| `iterator` | `pub fn iterator(self: *const Self) Iterator` |
| `getOrPut` | `pub fn getOrPut(self: *Self, key: K) !GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, key: anytype, ctx: anytype) !GetOrPutResult` |
| `getOrPutAssumeCapacity` | `pub fn getOrPutAssumeCapacity(self: *Self, key: K) GetOrPutResult` |
| `getOrPutAssumeCapacityAdapted` | `pub fn getOrPutAssumeCapacityAdapted(self: *Self, key: anytype, ctx: anytype) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, key: K, value: V) !GetOrPutResult` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, new_capacity: usize) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: usize) !void` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `put` | `pub fn put(self: *Self, key: K, value: V) !void` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, key: K, value: V) !void` |
| `putAssumeCapacity` | `pub fn putAssumeCapacity(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityNoClobber` | `pub fn putAssumeCapacityNoClobber(self: *Self, key: K, value: V) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, key: K, value: V) !?KV` |
| `fetchPutAssumeCapacity` | `pub fn fetchPutAssumeCapacity(self: *Self, key: K, value: V) ?KV` |
| `getEntry` | `pub fn getEntry(self: Self, key: K) ?Entry` |
| `getEntryAdapted` | `pub fn getEntryAdapted(self: Self, key: anytype, ctx: anytype) ?Entry` |
| `getIndex` | `pub fn getIndex(self: Self, key: K) ?usize` |
| `getIndexAdapted` | `pub fn getIndexAdapted(self: Self, key: anytype, ctx: anytype) ?usize` |
| `get` | `pub fn get(self: Self, key: K) ?V` |
| `getAdapted` | `pub fn getAdapted(self: Self, key: anytype, ctx: anytype) ?V` |
| `getPtr` | `pub fn getPtr(self: Self, key: K) ?*V` |
| `getPtrAdapted` | `pub fn getPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*V` |
| `getKey` | `pub fn getKey(self: Self, key: K) ?K` |
| `getKeyAdapted` | `pub fn getKeyAdapted(self: Self, key: anytype, ctx: anytype) ?K` |
| `getKeyPtr` | `pub fn getKeyPtr(self: Self, key: K) ?*K` |
| `getKeyPtrAdapted` | `pub fn getKeyPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*K` |
| `contains` | `pub fn contains(self: Self, key: K) bool` |
| `containsAdapted` | `pub fn containsAdapted(self: Self, key: anytype, ctx: anytype) bool` |
| `fetchSwapRemove` | `pub fn fetchSwapRemove(self: *Self, key: K) ?KV` |
| `fetchSwapRemoveAdapted` | `pub fn fetchSwapRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `fetchOrderedRemove` | `pub fn fetchOrderedRemove(self: *Self, key: K) ?KV` |
| `fetchOrderedRemoveAdapted` | `pub fn fetchOrderedRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `swapRemove` | `pub fn swapRemove(self: *Self, key: K) bool` |
| `swapRemoveAdapted` | `pub fn swapRemoveAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, key: K) bool` |
| `orderedRemoveAdapted` | `pub fn orderedRemoveAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `swapRemoveAt` | `pub fn swapRemoveAt(self: *Self, index: usize) void` |
| `orderedRemoveAt` | `pub fn orderedRemoveAt(self: *Self, index: usize) void` |
| `clone` | `pub fn clone(self: Self) !Self` |
| `cloneWithAllocator` | `pub fn cloneWithAllocator(self: Self, allocator: Allocator) !Self` |
| `cloneWithContext` | `pub fn cloneWithContext(self: Self, ctx: anytype) !ArrayHashMap(K, V, @TypeOf(ctx), store_hash)` |
| `cloneWithAllocatorAndContext` | `pub fn cloneWithAllocatorAndContext(self: Self, allocator: Allocator, ctx: anytype) !ArrayHashMap(K, V, @TypeOf(ctx), store_hash)` |
| `move` | `pub fn move(self: *Self) Self` |
| `reIndex` | `pub fn reIndex(self: *Self) !void` |
| `sort` | `pub fn sort(self: *Self, sort_ctx: anytype) void` |
| `sortUnstable` | `pub fn sortUnstable(self: *Self, sort_ctx: anytype) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, new_len: usize) void` |
| `pop` | `pub fn pop(self: *Self) ?KV` |
| `promote` | `pub fn promote(self: Self, gpa: Allocator) Managed` |
| `promoteContext` | `pub fn promoteContext(self: Self, gpa: Allocator, ctx: Context) Managed` |
| `init` | `pub fn init(gpa: Allocator, key_list: []const K, value_list: []const V) Oom!Self` |
| `reinit` | `pub fn reinit(self: *Self, gpa: Allocator, key_list: []const K, value_list: []const V) Oom!void` |
| `deinit` | `pub fn deinit(self: *Self, gpa: Allocator) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, gpa: Allocator) void` |
| `iterator` | `pub fn iterator(self: Self) Iterator` |
| `next` | `pub fn next(it: *Iterator) ?Entry` |
| `reset` | `pub fn reset(it: *Iterator) void` |
| `getOrPut` | `pub fn getOrPut(self: *Self, gpa: Allocator, key: K) Oom!GetOrPutResult` |
| `getOrPutContext` | `pub fn getOrPutContext(self: *Self, gpa: Allocator, key: K, ctx: Context) Oom!GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, gpa: Allocator, key: anytype, key_ctx: anytype) Oom!GetOrPutResult` |
| `getOrPutContextAdapted` | `pub fn getOrPutContextAdapted(self: *Self, gpa: Allocator, key: anytype, key_ctx: anytype, ctx: Context) Oom!GetOrPutResult` |
| `getOrPutAssumeCapacityContext` | `pub fn getOrPutAssumeCapacityContext(self: *Self, key: K, ctx: Context) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, gpa: Allocator, key: K, value: V) Oom!GetOrPutResult` |
| `getOrPutValueContext` | `pub fn getOrPutValueContext(self: *Self, gpa: Allocator, key: K, value: V, ctx: Context) Oom!GetOrPutResult` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, gpa: Allocator, new_capacity: usize) Oom!void` |
| `ensureTotalCapacityContext` | `pub fn ensureTotalCapacityContext(self: *Self, gpa: Allocator, new_capacity: usize, ctx: Context) Oom!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, gpa: Allocator, additional_capacity: usize,) Oom!void` |
| `ensureUnusedCapacityContext` | `pub fn ensureUnusedCapacityContext(self: *Self, gpa: Allocator, additional_capacity: usize, ctx: Context,) Oom!void` |
| `put` | `pub fn put(self: *Self, gpa: Allocator, key: K, value: V) Oom!void` |
| `putContext` | `pub fn putContext(self: *Self, gpa: Allocator, key: K, value: V, ctx: Context) Oom!void` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, gpa: Allocator, key: K, value: V) Oom!void` |
| `putNoClobberContext` | `pub fn putNoClobberContext(self: *Self, gpa: Allocator, key: K, value: V, ctx: Context) Oom!void` |
| `putAssumeCapacityContext` | `pub fn putAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `putAssumeCapacityNoClobberContext` | `pub fn putAssumeCapacityNoClobberContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, gpa: Allocator, key: K, value: V) Oom!?KV` |
| `fetchPutContext` | `pub fn fetchPutContext(self: *Self, gpa: Allocator, key: K, value: V, ctx: Context) Oom!?KV` |
| `fetchPutAssumeCapacityContext` | `pub fn fetchPutAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) ?KV` |
| `getEntryContext` | `pub fn getEntryContext(self: Self, key: K, ctx: Context) ?Entry` |
| `getIndexContext` | `pub fn getIndexContext(self: Self, key: K, ctx: Context) ?usize` |
| `getContext` | `pub fn getContext(self: Self, key: K, ctx: Context) ?V` |
| `getPtrContext` | `pub fn getPtrContext(self: Self, key: K, ctx: Context) ?*V` |
| `getKeyContext` | `pub fn getKeyContext(self: Self, key: K, ctx: Context) ?K` |
| `getKeyPtrContext` | `pub fn getKeyPtrContext(self: Self, key: K, ctx: Context) ?*K` |
| `containsContext` | `pub fn containsContext(self: Self, key: K, ctx: Context) bool` |
| `fetchSwapRemoveContext` | `pub fn fetchSwapRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `fetchSwapRemoveContextAdapted` | `pub fn fetchSwapRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) ?KV` |
| `fetchOrderedRemoveContext` | `pub fn fetchOrderedRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `fetchOrderedRemoveContextAdapted` | `pub fn fetchOrderedRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) ?KV` |
| `swapRemoveContext` | `pub fn swapRemoveContext(self: *Self, key: K, ctx: Context) bool` |
| `swapRemoveContextAdapted` | `pub fn swapRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) bool` |
| `orderedRemoveContext` | `pub fn orderedRemoveContext(self: *Self, key: K, ctx: Context) bool` |
| `orderedRemoveContextAdapted` | `pub fn orderedRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) bool` |
| `swapRemoveAtContext` | `pub fn swapRemoveAtContext(self: *Self, index: usize, ctx: Context) void` |
| `orderedRemoveAtContext` | `pub fn orderedRemoveAtContext(self: *Self, index: usize, ctx: Context) void` |
| `orderedRemoveAtMany` | `pub fn orderedRemoveAtMany(self: *Self, gpa: Allocator, sorted_indexes: []const usize) Oom!void` |
| `orderedRemoveAtManyContext` | `pub fn orderedRemoveAtManyContext(self: *Self, gpa: Allocator, sorted_indexes: []const usize, ctx: Context,) Oom!void` |
| `clone` | `pub fn clone(self: Self, gpa: Allocator) Oom!Self` |
| `cloneContext` | `pub fn cloneContext(self: Self, gpa: Allocator, ctx: Context) Oom!Self` |
| `reIndex` | `pub fn reIndex(self: *Self, gpa: Allocator) Oom!void` |
| `reIndexContext` | `pub fn reIndexContext(self: *Self, gpa: Allocator, ctx: Context) Oom!void` |
| `setKey` | `pub fn setKey(self: *Self, gpa: Allocator, index: usize, new_key: K) Oom!void` |
| `setKeyContext` | `pub fn setKeyContext(self: *Self, gpa: Allocator, index: usize, new_key: K, ctx: Context) Oom!void` |
| `sortContext` | `pub fn sortContext(self: *Self, sort_ctx: anytype, ctx: Context) void` |
| `sortUnstableContext` | `pub fn sortUnstableContext(self: *Self, sort_ctx: anytype, ctx: Context) void` |
| `shrinkRetainingCapacityContext` | `pub fn shrinkRetainingCapacityContext(self: *Self, new_len: usize, ctx: Context) void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, gpa: Allocator, new_len: usize) void` |
| `shrinkAndFreeContext` | `pub fn shrinkAndFreeContext(self: *Self, gpa: Allocator, new_len: usize, ctx: Context) void` |
| `popContext` | `pub fn popContext(self: *Self, ctx: Context) ?KV` |
| `f` | `pub fn f(allocator: Allocator) !void` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a_index: usize, b_index: usize) bool` |
| `getHashPtrAddrFn` | `pub fn getHashPtrAddrFn(comptime K: type, comptime Context: type) (fn (Context, K) u32)` |
| `getTrivialEqlFn` | `pub fn getTrivialEqlFn(comptime K: type, comptime Context: type) (fn (Context, K, K) bool)` |
| `AutoContext` | `pub fn AutoContext(comptime K: type) type` |
| `getAutoHashFn` | `pub fn getAutoHashFn(comptime K: type, comptime Context: type) (fn (Context, K) u32)` |
| `getAutoEqlFn` | `pub fn getAutoEqlFn(comptime K: type, comptime Context: type) (fn (Context, K, K, usize) bool)` |
| `autoEqlIsCheap` | `pub fn autoEqlIsCheap(comptime K: type) bool` |
| `getAutoHashStratFn` | `pub fn getAutoHashStratFn(comptime K: type, comptime Context: type, comptime strategy: std.hash.Strategy) (fn (Context, K) u32)` |

## atomic

| Function | Signature |
|----------|-----------|
| `Value` | `pub fn Value(comptime T: type) type` |
| `init` | `pub fn init(value: T) Self` |
| `load` | `pub fn load(self: *const Self, comptime order: AtomicOrder) T` |
| `store` | `pub fn store(self: *Self, value: T, comptime order: AtomicOrder) void` |
| `swap` | `pub fn swap(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `cmpxchgWeak` | `pub fn cmpxchgWeak(self: *Self, expected_value: T, new_value: T, comptime success_order: AtomicOrder, comptime fail_order: AtomicOrder,) ?T` |
| `cmpxchgStrong` | `pub fn cmpxchgStrong(self: *Self, expected_value: T, new_value: T, comptime success_order: AtomicOrder, comptime fail_order: AtomicOrder,) ?T` |
| `fetchAdd` | `pub fn fetchAdd(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchSub` | `pub fn fetchSub(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchMin` | `pub fn fetchMin(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchMax` | `pub fn fetchMax(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchAnd` | `pub fn fetchAnd(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchNand` | `pub fn fetchNand(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchXor` | `pub fn fetchXor(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `fetchOr` | `pub fn fetchOr(self: *Self, operand: T, comptime order: AtomicOrder) T` |
| `rmw` | `pub fn rmw(self: *Self, comptime op: std.builtin.AtomicRmwOp, operand: T, comptime order: AtomicOrder,) T` |
| `bitSet` | `pub fn bitSet(self: *Self, bit: Bit, comptime order: AtomicOrder) u1` |
| `bitReset` | `pub fn bitReset(self: *Self, bit: Bit, comptime order: AtomicOrder) u1` |
| `bitToggle` | `pub fn bitToggle(self: *Self, bit: Bit, comptime order: AtomicOrder) u1` |
| `spinLoopHint` | `pub fn spinLoopHint() void` |
| `cacheLineForCpu` | `pub fn cacheLineForCpu(cpu: std.Target.Cpu) u16` |
| `tryLock` | `pub fn tryLock(m: *Mutex) bool` |
| `unlock` | `pub fn unlock(m: *Mutex) void` |

## base64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8) Base64Encoder` |
| `calcSize` | `pub fn calcSize(encoder: *const Base64Encoder, source_len: usize) usize` |
| `encodeWriter` | `pub fn encodeWriter(encoder: *const Base64Encoder, dest: *std.Io.Writer, source: []const u8) !void` |
| `encode` | `pub fn encode(encoder: *const Base64Encoder, dest: []u8, source: []const u8) []const u8` |
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8) Base64Decoder` |
| `calcSizeUpperBound` | `pub fn calcSizeUpperBound(decoder: *const Base64Decoder, source_len: usize) Error!usize` |
| `calcSizeForSlice` | `pub fn calcSizeForSlice(decoder: *const Base64Decoder, source: []const u8) Error!usize` |
| `decode` | `pub fn decode(decoder: *const Base64Decoder, dest: []u8, source: []const u8) Error!void` |
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8, ignore_chars: []const u8) Base64DecoderWithIgnore` |
| `calcSizeUpperBound` | `pub fn calcSizeUpperBound(decoder_with_ignore: *const Base64DecoderWithIgnore, source_len: usize) usize` |
| `decode` | `pub fn decode(decoder_with_ignore: *const Base64DecoderWithIgnore, dest: []u8, source: []const u8) Error!usize` |

## bit_set

| Function | Signature |
|----------|-----------|
| `StaticBitSet` | `pub fn StaticBitSet(comptime size: usize) type` |
| `IntegerBitSet` | `pub fn IntegerBitSet(comptime size: u16) type` |
| `initEmpty` | `pub fn initEmpty() Self` |
| `initFull` | `pub fn initFull() Self` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `isSet` | `pub fn isSet(self: Self, index: usize) bool` |
| `count` | `pub fn count(self: Self) usize` |
| `setValue` | `pub fn setValue(self: *Self, index: usize, value: bool) void` |
| `set` | `pub fn set(self: *Self, index: usize) void` |
| `setRangeValue` | `pub fn setRangeValue(self: *Self, range: Range, value: bool) void` |
| `unset` | `pub fn unset(self: *Self, index: usize) void` |
| `toggle` | `pub fn toggle(self: *Self, index: usize) void` |
| `toggleSet` | `pub fn toggleSet(self: *Self, toggles: Self) void` |
| `toggleAll` | `pub fn toggleAll(self: *Self) void` |
| `setUnion` | `pub fn setUnion(self: *Self, other: Self) void` |
| `setIntersection` | `pub fn setIntersection(self: *Self, other: Self) void` |
| `findFirstSet` | `pub fn findFirstSet(self: Self) ?usize` |
| `findLastSet` | `pub fn findLastSet(self: Self) ?usize` |
| `toggleFirstSet` | `pub fn toggleFirstSet(self: *Self) ?usize` |
| `eql` | `pub fn eql(self: Self, other: Self) bool` |
| `subsetOf` | `pub fn subsetOf(self: Self, other: Self) bool` |
| `supersetOf` | `pub fn supersetOf(self: Self, other: Self) bool` |
| `complement` | `pub fn complement(self: Self) Self` |
| `unionWith` | `pub fn unionWith(self: Self, other: Self) Self` |
| `intersectWith` | `pub fn intersectWith(self: Self, other: Self) Self` |
| `xorWith` | `pub fn xorWith(self: Self, other: Self) Self` |
| `differenceWith` | `pub fn differenceWith(self: Self, other: Self) Self` |
| `iterator` | `pub fn iterator(self: *const Self, comptime options: IteratorOptions) Iterator(options)` |
| `Iterator` | `pub fn Iterator(comptime options: IteratorOptions) type` |
| `next` | `pub fn next(self: *IterSelf) ?usize` |
| `ArrayBitSet` | `pub fn ArrayBitSet(comptime MaskIntType: type, comptime size: usize) type` |
| `initEmpty` | `pub fn initEmpty(allocator: Allocator, bit_length: usize) !Self` |
| `initFull` | `pub fn initFull(allocator: Allocator, bit_length: usize) !Self` |
| `resize` | `pub fn resize(self: *@This() , allocator: Allocator, new_len: usize, fill: bool) !void` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `clone` | `pub fn clone(self: *const Self, new_allocator: Allocator) !Self` |
| `unsetAll` | `pub fn unsetAll(self: *Self) void` |
| `setAll` | `pub fn setAll(self: *Self) void` |
| `resize` | `pub fn resize(self: *@This() , new_len: usize, fill: bool) !void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `next` | `pub fn next(self: *Self) ?usize` |

## buf_map

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(allocator: Allocator) BufMap` |
| `deinit` | `pub fn deinit(self: *BufMap) void` |
| `putMove` | `pub fn putMove(self: *BufMap, key: []u8, value: []u8) !void` |
| `put` | `pub fn put(self: *BufMap, key: []const u8, value: []const u8) !void` |
| `getPtr` | `pub fn getPtr(self: BufMap, key: []const u8) ?*[]const u8` |
| `get` | `pub fn get(self: BufMap, key: []const u8) ?[]const u8` |
| `remove` | `pub fn remove(self: *BufMap, key: []const u8) void` |
| `count` | `pub fn count(self: BufMap) BufMapHashMap.Size` |
| `iterator` | `pub fn iterator(self: *const BufMap) BufMapHashMap.Iterator` |

## buf_set

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(a: Allocator) BufSet` |
| `deinit` | `pub fn deinit(self: *BufSet) void` |
| `insert` | `pub fn insert(self: *BufSet, value: []const u8) !void` |
| `contains` | `pub fn contains(self: BufSet, value: []const u8) bool` |
| `remove` | `pub fn remove(self: *BufSet, value: []const u8) void` |
| `count` | `pub fn count(self: *const BufSet) usize` |
| `iterator` | `pub fn iterator(self: *const BufSet) Iterator` |
| `allocator` | `pub fn allocator(self: *const BufSet) Allocator` |
| `cloneWithAllocator` | `pub fn cloneWithAllocator(self: *const BufSet, new_allocator: Allocator,) Allocator.Error!BufSet` |
| `clone` | `pub fn clone(self: *const BufSet) Allocator.Error!BufSet` |

## builtin

| Function | Signature |
|----------|-----------|
| `archs` | `pub fn archs(cc: CallingConvention) []const std.Target.Cpu.Arch` |
| `eql` | `pub fn eql(a: CallingConvention, b: CallingConvention) bool` |
| `withStackAlign` | `pub fn withStackAlign(cc: CallingConvention, incoming_stack_alignment: u64) CallingConvention` |
| `sentinel` | `pub fn sentinel(comptime ptr: Pointer) ?ptr.child` |
| `sentinel` | `pub fn sentinel(comptime arr: Array) ?arr.child` |
| `defaultValue` | `pub fn defaultValue(comptime sf: StructField) ?sf.type` |

## c

| Function | Signature |
|----------|-----------|
| `versionCheck` | `pub fn versionCheck(comptime version: std.SemanticVersion) bool` |
| `errno` | `pub fn errno(rc: anytype) E` |
| `fromTimestamp` | `pub fn fromTimestamp(tm: wasi.timestamp_t) timespec` |
| `toTimestamp` | `pub fn toTimestamp(ts: timespec) wasi.timestamp_t` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `IWHT` | `pub fn IWHT(m: u32) bool` |
| `ISDOOR` | `pub fn ISDOOR(m: u32) bool` |
| `ISPORT` | `pub fn ISPORT(m: u32) bool` |
| `ISINDEX` | `pub fn ISINDEX(m: u32) bool` |
| `IDX` | `pub fn IDX(sig: usize) usize` |
| `WORD` | `pub fn WORD(sig: usize) usize` |
| `BIT` | `pub fn BIT(sig: usize) usize` |
| `VALID` | `pub fn VALID(sig: usize) usize` |
| `EXITSTATUS` | `pub fn EXITSTATUS(x: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(x: u32) SIG` |
| `STOPSIG` | `pub fn STOPSIG(x: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(x: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(x: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(x: u32) bool` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) SIG` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `IFCONTINUED` | `pub fn IFCONTINUED(s: u32) bool` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `atime` | `pub fn atime(self: @This() ) timespec` |
| `mtime` | `pub fn mtime(self: @This() ) timespec` |
| `ctime` | `pub fn ctime(self: @This() ) timespec` |
| `fromFilestat` | `pub fn fromFilestat(st: wasi.filestat_t) Stat` |
| `birthtime` | `pub fn birthtime(self: @This() ) timespec` |
| `sigrtmin` | `pub fn sigrtmin() u8` |
| `sigrtmax` | `pub fn sigrtmax() u8` |

## coff

| Function | Signature |
|----------|-----------|
| `getImportByName` | `pub fn getImportByName(raw: u32) ?ByName` |
| `getImportByOrdinal` | `pub fn getImportByOrdinal(raw: u32) ?ByOrdinal` |
| `getImportByName` | `pub fn getImportByName(raw: u64) ?ByName` |
| `getImportByOrdinal` | `pub fn getImportByOrdinal(raw: u64) ?ByOrdinal` |
| `getName` | `pub fn getName(self: *align(1) const SectionHeader) ?[]const u8` |
| `getNameOffset` | `pub fn getNameOffset(self: SectionHeader) ?u32` |
| `getAlignment` | `pub fn getAlignment(self: SectionHeader) ?u16` |
| `setAlignment` | `pub fn setAlignment(self: *SectionHeader, new_alignment: u16) void` |
| `isCode` | `pub fn isCode(self: SectionHeader) bool` |
| `isComdat` | `pub fn isComdat(self: SectionHeader) bool` |
| `toByteUnits` | `pub fn toByteUnits(a: Align) ?u16` |
| `fromByteUnits` | `pub fn fromByteUnits(n: u16) Align` |
| `sizeOf` | `pub fn sizeOf() usize` |
| `getName` | `pub fn getName(self: *const Symbol) ?[]const u8` |
| `getNameOffset` | `pub fn getNameOffset(self: Symbol) ?u32` |
| `getFileName` | `pub fn getFileName(self: *const FileDefinition) []const u8` |
| `init` | `pub fn init(data: []const u8, is_loaded: bool) error` |
| `getPdbPath` | `pub fn getPdbPath(self: *Coff) !?[]const u8` |
| `getHeader` | `pub fn getHeader(self: Coff) Header` |
| `getOptionalHeader` | `pub fn getOptionalHeader(self: Coff) OptionalHeader` |
| `getOptionalHeader32` | `pub fn getOptionalHeader32(self: Coff) OptionalHeader.PE32` |
| `getOptionalHeader64` | `pub fn getOptionalHeader64(self: Coff) OptionalHeader.@"PE32+"` |
| `getImageBase` | `pub fn getImageBase(self: Coff) u64` |
| `getNumberOfDataDirectories` | `pub fn getNumberOfDataDirectories(self: Coff) u32` |
| `getDataDirectories` | `pub fn getDataDirectories(self: *const Coff) []align(1) const ImageDataDirectory` |
| `getSymtab` | `pub fn getSymtab(self: *const Coff) ?Symtab` |
| `getStrtab` | `pub fn getStrtab(self: *const Coff) error` |
| `strtabRequired` | `pub fn strtabRequired(self: *const Coff) bool` |
| `getSectionHeaders` | `pub fn getSectionHeaders(self: *const Coff) []align(1) const SectionHeader` |
| `getSectionHeadersAlloc` | `pub fn getSectionHeadersAlloc(self: *const Coff, allocator: mem.Allocator) ![]SectionHeader` |
| `getSectionName` | `pub fn getSectionName(self: *const Coff, sect_hdr: *align(1) const SectionHeader) error` |
| `getSectionByName` | `pub fn getSectionByName(self: *const Coff, comptime name: []const u8) ?*align(1) const SectionHeader` |
| `getSectionData` | `pub fn getSectionData(self: *const Coff, sec: *align(1) const SectionHeader) []const u8` |
| `getSectionDataAlloc` | `pub fn getSectionDataAlloc(self: *const Coff, sec: *align(1) const SectionHeader, allocator: mem.Allocator) ![]u8` |
| `len` | `pub fn len(self: Symtab) usize` |
| `at` | `pub fn at(self: Symtab, index: usize, tag: Tag) Record` |
| `next` | `pub fn next(self: *Slice) ?Symbol` |
| `slice` | `pub fn slice(self: Symtab, start: usize, end: ?usize) Slice` |
| `get` | `pub fn get(self: Strtab, off: u32) []const u8` |

## deque

| Function | Signature |
|----------|-----------|
| `Deque` | `pub fn Deque(comptime T: type) type` |
| `initCapacity` | `pub fn initCapacity(gpa: Allocator, capacity: usize) Allocator.Error!Self` |
| `initBuffer` | `pub fn initBuffer(buffer: []T) Self` |
| `deinit` | `pub fn deinit(deque: *Self, gpa: Allocator) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(deque: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(deque: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(deque: *Self, gpa: Allocator, additional_count: usize,) Allocator.Error!void` |
| `pushFront` | `pub fn pushFront(deque: *Self, gpa: Allocator, item: T) error` |
| `pushFrontBounded` | `pub fn pushFrontBounded(deque: *Self, item: T) error` |
| `pushFrontAssumeCapacity` | `pub fn pushFrontAssumeCapacity(deque: *Self, item: T) void` |
| `pushBack` | `pub fn pushBack(deque: *Self, gpa: Allocator, item: T) error` |
| `pushBackBounded` | `pub fn pushBackBounded(deque: *Self, item: T) error` |
| `pushBackAssumeCapacity` | `pub fn pushBackAssumeCapacity(deque: *Self, item: T) void` |
| `front` | `pub fn front(deque: *const Self) ?T` |
| `back` | `pub fn back(deque: *const Self) ?T` |
| `at` | `pub fn at(deque: *const Self, index: usize) T` |
| `popFront` | `pub fn popFront(deque: *Self) ?T` |
| `popBack` | `pub fn popBack(deque: *Self) ?T` |
| `next` | `pub fn next(it: *Iterator) ?T` |
| `iterator` | `pub fn iterator(deque: *const Self) Iterator` |

## dynamic_library

| Function | Signature |
|----------|-----------|
| `open` | `pub fn open(path: []const u8) Error!DynLib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8) Error!DynLib` |
| `close` | `pub fn close(self: *DynLib) void` |
| `lookup` | `pub fn lookup(self: *DynLib, comptime T: type, name: [:0]const u8) ?T` |
| `end` | `pub fn end(self: *Iterator) bool` |
| `next` | `pub fn next(self: *Iterator) ?*LinkMap` |
| `get_DYNAMIC` | `pub fn get_DYNAMIC() ?[*]const elf.Dyn` |
| `linkmap_iterator` | `pub fn linkmap_iterator() error` |
| `open` | `pub fn open(path: []const u8, LD_LIBRARY_PATH: ?[]const u8) Error!ElfDynLib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8, LD_LIBRARY_PATH: ?[]const u8) Error!ElfDynLib` |
| `close` | `pub fn close(self: *ElfDynLib) void` |
| `lookup` | `pub fn lookup(self: *const ElfDynLib, comptime T: type, name: [:0]const u8) ?T` |
| `fromPtr` | `pub fn fromPtr(header: *elf.gnu_hash.Header) @This()` |
| `lookupAddress` | `pub fn lookupAddress(self: *const ElfDynLib, vername: []const u8, name: []const u8) ?usize` |
| `open` | `pub fn open(path: []const u8) Error!DlDynLib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8) Error!DlDynLib` |
| `close` | `pub fn close(self: *DlDynLib) void` |
| `lookup` | `pub fn lookup(self: *DlDynLib, comptime T: type, name: [:0]const u8) ?T` |
| `getError` | `pub fn getError() ?[:0]const u8` |

## elf

| Function | Signature |
|----------|-----------|
| `iterateProgramHeaders` | `pub fn iterateProgramHeaders(h: *const Header, file_reader: *Io.File.Reader) ProgramHeaderIterator` |
| `iterateProgramHeadersBuffer` | `pub fn iterateProgramHeadersBuffer(h: *const Header, buf: []const u8) ProgramHeaderBufferIterator` |
| `iterateSectionHeaders` | `pub fn iterateSectionHeaders(h: *const Header, file_reader: *Io.File.Reader) SectionHeaderIterator` |
| `iterateSectionHeadersBuffer` | `pub fn iterateSectionHeadersBuffer(h: *const Header, buf: []const u8) SectionHeaderBufferIterator` |
| `iterateDynamicSection` | `pub fn iterateDynamicSection(h: *const Header, file_reader: *Io.File.Reader, offset: u64, size: u64,) DynamicSectionIterator` |
| `iterateDynamicSectionBuffer` | `pub fn iterateDynamicSectionBuffer(h: *const Header, buf: []const u8, offset: u64, size: u64,) DynamicSectionBufferIterator` |
| `read` | `pub fn read(r: *Io.Reader) ReadError!Header` |
| `init` | `pub fn init(hdr: anytype, endian: Endian) Header` |
| `next` | `pub fn next(it: *ProgramHeaderIterator) !?Elf64_Phdr` |
| `next` | `pub fn next(it: *ProgramHeaderBufferIterator) !?Elf64_Phdr` |
| `takeProgramHeader` | `pub fn takeProgramHeader(reader: *Io.Reader, is_64: bool, endian: Endian) !Elf64_Phdr` |
| `next` | `pub fn next(it: *SectionHeaderIterator) !?Elf64_Shdr` |
| `next` | `pub fn next(it: *SectionHeaderBufferIterator) !?Elf64_Shdr` |
| `takeSectionHeader` | `pub fn takeSectionHeader(reader: *Io.Reader, is_64: bool, endian: Endian) !Elf64_Shdr` |
| `next` | `pub fn next(it: *DynamicSectionIterator) !?Elf64_Dyn` |
| `next` | `pub fn next(it: *DynamicSectionBufferIterator) !?Elf64_Dyn` |
| `takeDynamicSection` | `pub fn takeDynamicSection(reader: *Io.Reader, is_64: bool, endian: Endian) !Elf64_Dyn` |
| `st_type` | `pub fn st_type(self: @This() ) u4` |
| `st_bind` | `pub fn st_bind(self: @This() ) u4` |
| `r_sym` | `pub fn r_sym(self: @This() ) u24` |
| `r_type` | `pub fn r_type(self: @This() ) u8` |
| `r_sym` | `pub fn r_sym(self: @This() ) u32` |
| `r_type` | `pub fn r_type(self: @This() ) u32` |
| `ElfN` | `pub fn ElfN(comptime class: CLASS) type` |
| `date` | `pub fn date(self: ar_hdr) std.fmt.ParseIntError!u64` |
| `size` | `pub fn size(self: ar_hdr) std.fmt.ParseIntError!u32` |
| `isStrtab` | `pub fn isStrtab(self: ar_hdr) bool` |
| `isSymtab` | `pub fn isSymtab(self: ar_hdr) bool` |
| `isSymtab64` | `pub fn isSymtab64(self: ar_hdr) bool` |
| `isSymdef` | `pub fn isSymdef(self: ar_hdr) bool` |
| `isSymdefSorted` | `pub fn isSymdefSorted(self: ar_hdr) bool` |
| `name` | `pub fn name(self: *const ar_hdr) ?[]const u8` |
| `nameOffset` | `pub fn nameOffset(self: ar_hdr) std.fmt.ParseIntError!?u32` |
| `calculate` | `pub fn calculate(name: []const u8) u32` |

## enums

| Function | Signature |
|----------|-----------|
| `fromInt` | `pub fn fromInt(comptime E: type, integer: anytype) ?E` |
| `EnumFieldStruct` | `pub fn EnumFieldStruct(comptime E: type, comptime Data: type, comptime field_default: ?Data) type` |
| `valuesFromFields` | `pub fn valuesFromFields(comptime E: type, comptime fields: []const EnumField) []const E` |
| `values` | `pub fn values(comptime E: type) []const E` |
| `tagName` | `pub fn tagName(comptime E: type, e: E) ?[:0]const u8` |
| `directEnumArrayLen` | `pub fn directEnumArrayLen(comptime E: type, comptime max_unused_slots: comptime_int) comptime_int` |
| `directEnumArray` | `pub fn directEnumArray(comptime E: type, comptime Data: type, comptime max_unused_slots: comptime_int, init_values: EnumFieldStruct(E, Data, null) , ) [directEnumArrayLen(E, max_unused_slots)]Data` |
| `directEnumArrayDefault` | `pub fn directEnumArrayDefault(comptime E: type, comptime Data: type, comptime default: ?Data, comptime max_unused_slots: comptime_int, init_values: EnumFieldStruct(E, Data, default) , ) [directEnumArrayLen(E, max_unused_slots)]Data` |
| `EnumSet` | `pub fn EnumSet(comptime E: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, bool, false) ) Self` |
| `initEmpty` | `pub fn initEmpty() Self` |
| `initFull` | `pub fn initFull() Self` |
| `initMany` | `pub fn initMany(keys: []const Key) Self` |
| `initOne` | `pub fn initOne(key: Key) Self` |
| `count` | `pub fn count(self: Self) usize` |
| `contains` | `pub fn contains(self: Self, key: Key) bool` |
| `insert` | `pub fn insert(self: *Self, key: Key) void` |
| `remove` | `pub fn remove(self: *Self, key: Key) void` |
| `setPresent` | `pub fn setPresent(self: *Self, key: Key, present: bool) void` |
| `toggle` | `pub fn toggle(self: *Self, key: Key) void` |
| `toggleSet` | `pub fn toggleSet(self: *Self, other: Self) void` |
| `toggleAll` | `pub fn toggleAll(self: *Self) void` |
| `setUnion` | `pub fn setUnion(self: *Self, other: Self) void` |
| `setIntersection` | `pub fn setIntersection(self: *Self, other: Self) void` |
| `eql` | `pub fn eql(self: Self, other: Self) bool` |
| `subsetOf` | `pub fn subsetOf(self: Self, other: Self) bool` |
| `supersetOf` | `pub fn supersetOf(self: Self, other: Self) bool` |
| `complement` | `pub fn complement(self: Self) Self` |
| `unionWith` | `pub fn unionWith(self: Self, other: Self) Self` |
| `intersectWith` | `pub fn intersectWith(self: Self, other: Self) Self` |
| `xorWith` | `pub fn xorWith(self: Self, other: Self) Self` |
| `differenceWith` | `pub fn differenceWith(self: Self, other: Self) Self` |
| `iterator` | `pub fn iterator(self: *const Self) Iterator` |
| `next` | `pub fn next(self: *Iterator) ?Key` |
| `EnumMap` | `pub fn EnumMap(comptime E: type, comptime V: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, ?Value, @as(?Value, null) )) Self` |
| `initFull` | `pub fn initFull(value: Value) Self` |
| `initFullWith` | `pub fn initFullWith(init_values: EnumFieldStruct(E, Value, null) ) Self` |
| `initFullWithDefault` | `pub fn initFullWithDefault(comptime default: ?Value, init_values: EnumFieldStruct(E, Value, default) ) Self` |
| `count` | `pub fn count(self: *const Self) usize` |
| `contains` | `pub fn contains(self: *const Self, key: Key) bool` |
| `get` | `pub fn get(self: *const Self, key: Key) ?Value` |
| `getAssertContains` | `pub fn getAssertContains(self: *const Self, key: Key) Value` |
| `getPtr` | `pub fn getPtr(self: *Self, key: Key) ?*Value` |
| `getPtrConst` | `pub fn getPtrConst(self: *const Self, key: Key) ?*const Value` |
| `getPtrAssertContains` | `pub fn getPtrAssertContains(self: *Self, key: Key) *Value` |
| `getPtrConstAssertContains` | `pub fn getPtrConstAssertContains(self: *const Self, key: Key) *const Value` |
| `put` | `pub fn put(self: *Self, key: Key, value: Value) void` |
| `putUninitialized` | `pub fn putUninitialized(self: *Self, key: Key) *Value` |
| `fetchPut` | `pub fn fetchPut(self: *Self, key: Key, value: Value) ?Value` |
| `fetchRemove` | `pub fn fetchRemove(self: *Self, key: Key) ?Value` |
| `iterator` | `pub fn iterator(self: *Self) Iterator` |
| `next` | `pub fn next(self: *Iterator) ?Entry` |
| `EnumMultiset` | `pub fn EnumMultiset(comptime E: type) type` |
| `BoundedEnumMultiset` | `pub fn BoundedEnumMultiset(comptime E: type, comptime CountSize: type) type` |
| `init` | `pub fn init(init_counts: EnumFieldStruct(E, CountSize, 0) ) Self` |
| `initWithCount` | `pub fn initWithCount(comptime c: CountSize) Self` |
| `contains` | `pub fn contains(self: Self, key: E) bool` |
| `removeAll` | `pub fn removeAll(self: *Self, key: E) void` |
| `addAssertSafe` | `pub fn addAssertSafe(self: *Self, key: E, c: CountSize) void` |
| `add` | `pub fn add(self: *Self, key: E, c: CountSize) error` |
| `remove` | `pub fn remove(self: *Self, key: E, c: CountSize) void` |
| `getCount` | `pub fn getCount(self: Self, key: E) CountSize` |
| `setCount` | `pub fn setCount(self: *Self, key: E, c: CountSize) void` |
| `addSetAssertSafe` | `pub fn addSetAssertSafe(self: *Self, other: Self) void` |
| `addSet` | `pub fn addSet(self: *Self, other: Self) error` |
| `removeSet` | `pub fn removeSet(self: *Self, other: Self) void` |
| `plusAssertSafe` | `pub fn plusAssertSafe(self: Self, other: Self) Self` |
| `plus` | `pub fn plus(self: Self, other: Self) error` |
| `minus` | `pub fn minus(self: Self, other: Self) Self` |
| `EnumArray` | `pub fn EnumArray(comptime E: type, comptime V: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, Value, null) ) Self` |
| `initDefault` | `pub fn initDefault(comptime default: ?Value, init_values: EnumFieldStruct(E, Value, default) ) Self` |
| `initUndefined` | `pub fn initUndefined() Self` |
| `initFill` | `pub fn initFill(v: Value) Self` |
| `get` | `pub fn get(self: Self, key: Key) Value` |
| `getPtr` | `pub fn getPtr(self: *Self, key: Key) *Value` |
| `getPtrConst` | `pub fn getPtrConst(self: *const Self, key: Key) *const Value` |
| `set` | `pub fn set(self: *Self, key: Key, value: Value) void` |
| `EnumIndexer` | `pub fn EnumIndexer(comptime E: type) type` |
| `indexOf` | `pub fn indexOf(e: E) usize` |
| `keyForIndex` | `pub fn keyForIndex(i: usize) E` |

## gpu

| Function | Signature |
|----------|-----------|
| `executionMode` | `pub fn executionMode(comptime entry_point: anytype, comptime mode: ExecutionMode) void` |

## hash

| Function | Signature |
|----------|-----------|
| `int` | `pub fn int(input: anytype) @TypeOf(input)` |

## http

| Function | Signature |
|----------|-----------|
| `requestHasBody` | `pub fn requestHasBody(m: Method) bool` |
| `responseHasBody` | `pub fn responseHasBody(m: Method) bool` |
| `safe` | `pub fn safe(m: Method) bool` |
| `idempotent` | `pub fn idempotent(m: Method) bool` |
| `cacheable` | `pub fn cacheable(m: Method) bool` |
| `phrase` | `pub fn phrase(self: Status) ?[]const u8` |
| `class` | `pub fn class(self: Status) Class` |
| `fromString` | `pub fn fromString(s: []const u8) ?ContentEncoding` |
| `minBufferCapacity` | `pub fn minBufferCapacity(ce: ContentEncoding) usize` |
| `init` | `pub fn init(integer: u64) RemainingChunkLen` |
| `int` | `pub fn int(rcl: RemainingChunkLen) u64` |
| `receiveHead` | `pub fn receiveHead(reader: *Reader) HeadError![]const u8` |
| `bodyReader` | `pub fn bodyReader(reader: *Reader, transfer_buffer: []u8, transfer_encoding: TransferEncoding, content_length: ?u64,) *std.Io.Reader` |
| `bodyReaderDecompressing` | `pub fn bodyReaderDecompressing(reader: *Reader, transfer_buffer: []u8, transfer_encoding: TransferEncoding, content_length: ?u64, content_encoding: ContentEncoding, decompress: *Decompress, decompress_buffer: []u8,) *std.Io.Reader` |
| `init` | `pub fn init(decompress: *Decompress, transfer_reader: *std.Io.Reader, buffer: []u8, content_encoding: ContentEncoding,) *std.Io.Reader` |
| `isEliding` | `pub fn isEliding(w: *const BodyWriter) bool` |
| `flush` | `pub fn flush(w: *BodyWriter) Error!void` |
| `end` | `pub fn end(w: *BodyWriter) Error!void` |
| `endUnflushed` | `pub fn endUnflushed(w: *BodyWriter) Error!void` |
| `endChunked` | `pub fn endChunked(w: *BodyWriter, options: EndChunkedOptions) Error!void` |
| `endChunkedUnflushed` | `pub fn endChunkedUnflushed(w: *BodyWriter, options: EndChunkedOptions) Error!void` |
| `contentLengthDrain` | `pub fn contentLengthDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `noneDrain` | `pub fn noneDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `elidingDrain` | `pub fn elidingDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |
| `elidingSendFile` | `pub fn elidingSendFile(w: *Writer, file_reader: *File.Reader, limit: std.Io.Limit) Writer.FileError!usize` |
| `noneSendFile` | `pub fn noneSendFile(w: *Writer, file_reader: *File.Reader, limit: std.Io.Limit) Writer.FileError!usize` |
| `contentLengthSendFile` | `pub fn contentLengthSendFile(w: *Writer, file_reader: *File.Reader, limit: std.Io.Limit) Writer.FileError!usize` |
| `chunkedSendFile` | `pub fn chunkedSendFile(w: *Writer, file_reader: *File.Reader, limit: std.Io.Limit) Writer.FileError!usize` |
| `chunkedDrain` | `pub fn chunkedDrain(w: *Writer, data: []const []const u8, splat: usize) Error!usize` |

## leb128

| Function | Signature |
|----------|-----------|
| `writeUnsignedFixed` | `pub fn writeUnsignedFixed(comptime l: usize, ptr: *[l]u8, int: std.meta.Int(.unsigned, l * 7) ) void` |
| `writeUnsignedExtended` | `pub fn writeUnsignedExtended(slice: []u8, arg: anytype) void` |
| `writeSignedFixed` | `pub fn writeSignedFixed(comptime l: usize, ptr: *[l]u8, int: std.meta.Int(.signed, l * 7) ) void` |

## log

| Function | Signature |
|----------|-----------|
| `asText` | `pub fn asText(comptime self: Level) []const u8` |
| `logEnabled` | `pub fn logEnabled(comptime level: Level, comptime scope: @EnumLiteral() ) bool` |
| `defaultTerminalMode` | `pub fn defaultTerminalMode() std.Io.Terminal.Mode` |
| `defaultLog` | `pub fn defaultLog(comptime level: Level, comptime scope: @EnumLiteral() , comptime format: []const u8, args: anytype, ) void` |
| `defaultLogFileTerminal` | `pub fn defaultLogFileTerminal(comptime level: Level, comptime scope: @EnumLiteral() , comptime format: []const u8, args: anytype, t: std.Io.Terminal, ) std.Io.Writer.Error!void` |
| `scoped` | `pub fn scoped(comptime scope: @EnumLiteral() ) type` |
| `err` | `pub fn err(comptime format: []const u8, args: anytype,) void` |
| `warn` | `pub fn warn(comptime format: []const u8, args: anytype,) void` |
| `info` | `pub fn info(comptime format: []const u8, args: anytype,) void` |
| `debug` | `pub fn debug(comptime format: []const u8, args: anytype,) void` |

## macho

| Function | Signature |
|----------|-----------|
| `segName` | `pub fn segName(seg: *const segment_command_64) []const u8` |
| `isWriteable` | `pub fn isWriteable(seg: segment_command_64) bool` |
| `sectName` | `pub fn sectName(sect: *const section_64) []const u8` |
| `segName` | `pub fn segName(sect: *const section_64) []const u8` |
| `attrs` | `pub fn attrs(sect: section_64) u32` |
| `isCode` | `pub fn isCode(sect: section_64) bool` |
| `isZerofill` | `pub fn isZerofill(sect: section_64) bool` |
| `isSymbolStubs` | `pub fn isSymbolStubs(sect: section_64) bool` |
| `isDebug` | `pub fn isDebug(sect: section_64) bool` |
| `isDontDeadStrip` | `pub fn isDontDeadStrip(sect: section_64) bool` |
| `isDontDeadStripIfReferencesLive` | `pub fn isDontDeadStripIfReferencesLive(sect: section_64) bool` |
| `tentative` | `pub fn tentative(sym: nlist_64) bool` |
| `cast` | `pub fn cast(lc: LoadCommand, comptime Cmd: type) ?Cmd` |
| `getSections` | `pub fn getSections(lc: LoadCommand) []align(1) const section_64` |
| `getDylibPathName` | `pub fn getDylibPathName(lc: LoadCommand) []const u8` |
| `getRpathPathName` | `pub fn getRpathPathName(lc: LoadCommand) []const u8` |
| `getBuildVersionTools` | `pub fn getBuildVersionTools(lc: LoadCommand) []align(1) const build_tool_version` |
| `next` | `pub fn next(it: *LoadCommandIterator) error` |
| `init` | `pub fn init(hdr: *const mach_header_64, cmds_buf_overlong: []const u8) error` |

## math

| Function | Signature |
|----------|-----------|
| `approxEqAbs` | `pub fn approxEqAbs(comptime T: type, x: T, y: T, tolerance: T) bool` |
| `approxEqRel` | `pub fn approxEqRel(comptime T: type, x: T, y: T, tolerance: T) bool` |
| `raiseInvalid` | `pub fn raiseInvalid() void` |
| `raiseUnderflow` | `pub fn raiseUnderflow() void` |
| `raiseOverflow` | `pub fn raiseOverflow() void` |
| `raiseInexact` | `pub fn raiseInexact() void` |
| `raiseDivByZero` | `pub fn raiseDivByZero() void` |
| `sin` | `pub fn sin(value: anytype) @TypeOf(value)` |
| `cos` | `pub fn cos(value: anytype) @TypeOf(value)` |
| `tan` | `pub fn tan(value: anytype) @TypeOf(value)` |
| `radiansToDegrees` | `pub fn radiansToDegrees(ang: anytype) if (@TypeOf(ang) == comptime_int) comptime_float else @TypeOf(ang)` |
| `degreesToRadians` | `pub fn degreesToRadians(ang: anytype) if (@TypeOf(ang) == comptime_int) comptime_float else @TypeOf(ang)` |
| `exp` | `pub fn exp(value: anytype) @TypeOf(value)` |
| `exp2` | `pub fn exp2(value: anytype) @TypeOf(value)` |
| `Min` | `pub fn Min(comptime A: type, comptime B: type) type` |
| `wrap` | `pub fn wrap(x: anytype, r: anytype) @TypeOf(x)` |
| `clamp` | `pub fn clamp(val: anytype, lower: anytype, upper: anytype) @TypeOf(val, lower, upper)` |
| `mul` | `pub fn mul(comptime T: type, a: T, b: T) (error` |
| `add` | `pub fn add(comptime T: type, a: T, b: T) (error` |
| `sub` | `pub fn sub(comptime T: type, a: T, b: T) (error` |
| `negate` | `pub fn negate(x: anytype) !@TypeOf(x)` |
| `shlExact` | `pub fn shlExact(comptime T: type, a: T, shift_amt: Log2Int(T) ) !T` |
| `shl` | `pub fn shl(comptime T: type, a: T, shift_amt: anytype) T` |
| `shr` | `pub fn shr(comptime T: type, a: T, shift_amt: anytype) T` |
| `rotr` | `pub fn rotr(comptime T: type, x: T, r: anytype) T` |
| `rotl` | `pub fn rotl(comptime T: type, x: T, r: anytype) T` |
| `Log2Int` | `pub fn Log2Int(comptime T: type) type` |
| `Log2IntCeil` | `pub fn Log2IntCeil(comptime T: type) type` |
| `IntFittingRange` | `pub fn IntFittingRange(comptime from: comptime_int, comptime to: comptime_int) type` |
| `divTrunc` | `pub fn divTrunc(comptime T: type, numerator: T, denominator: T) !T` |
| `divFloor` | `pub fn divFloor(comptime T: type, numerator: T, denominator: T) !T` |
| `divCeil` | `pub fn divCeil(comptime T: type, numerator: T, denominator: T) !T` |
| `divExact` | `pub fn divExact(comptime T: type, numerator: T, denominator: T) !T` |
| `mod` | `pub fn mod(comptime T: type, numerator: T, denominator: T) !T` |
| `rem` | `pub fn rem(comptime T: type, numerator: T, denominator: T) !T` |
| `negateCast` | `pub fn negateCast(x: anytype) !std.meta.Int(.signed, @bitSizeOf(@TypeOf(x)))` |
| `cast` | `pub fn cast(comptime T: type, x: anytype) ?T` |
| `alignCast` | `pub fn alignCast(comptime alignment: Alignment, ptr: anytype) AlignCastError!AlignCastResult(alignment, @TypeOf(ptr))` |
| `isPowerOfTwo` | `pub fn isPowerOfTwo(int: anytype) bool` |
| `ByteAlignedInt` | `pub fn ByteAlignedInt(comptime T: type) type` |
| `round` | `pub fn round(value: anytype) @TypeOf(value)` |
| `trunc` | `pub fn trunc(value: anytype) @TypeOf(value)` |
| `floor` | `pub fn floor(value: anytype) @TypeOf(value)` |
| `floorPowerOfTwo` | `pub fn floorPowerOfTwo(comptime T: type, value: T) T` |
| `ceil` | `pub fn ceil(value: anytype) @TypeOf(value)` |
| `ceilPowerOfTwoPromote` | `pub fn ceilPowerOfTwoPromote(comptime T: type, value: T) std.meta.Int(@typeInfo(T).int.signedness, @typeInfo(T).int.bits + 1)` |
| `ceilPowerOfTwo` | `pub fn ceilPowerOfTwo(comptime T: type, value: T) (error` |
| `ceilPowerOfTwoAssert` | `pub fn ceilPowerOfTwoAssert(comptime T: type, value: T) T` |
| `log2_int` | `pub fn log2_int(comptime T: type, x: T) Log2Int(T)` |
| `log2_int_ceil` | `pub fn log2_int_ceil(comptime T: type, x: T) Log2IntCeil(T)` |
| `lossyCast` | `pub fn lossyCast(comptime T: type, value: anytype) T` |
| `lerp` | `pub fn lerp(a: anytype, b: anytype, t: anytype) @TypeOf(a, b, t)` |
| `maxInt` | `pub fn maxInt(comptime T: type) comptime_int` |
| `minInt` | `pub fn minInt(comptime T: type) comptime_int` |
| `mulWide` | `pub fn mulWide(comptime T: type, a: T, b: T) std.meta.Int( @typeInfo(T).int.signedness, @typeInfo(T).int.bits * 2, )` |
| `invert` | `pub fn invert(self: Order) Order` |
| `differ` | `pub fn differ(self: Order) ?Order` |
| `compare` | `pub fn compare(self: Order, op: CompareOperator) bool` |
| `order` | `pub fn order(a: anytype, b: anytype) Order` |
| `reverse` | `pub fn reverse(op: CompareOperator) CompareOperator` |
| `compare` | `pub fn compare(a: anytype, op: CompareOperator, b: anytype) bool` |
| `boolMask` | `pub fn boolMask(comptime MaskInt: type, value: bool) MaskInt` |
| `comptimeMod` | `pub fn comptimeMod(num: anytype, comptime denom: comptime_int) IntFittingRange(0, denom - 1)` |
| `toFloat` | `pub fn toFloat(self: F80) f80` |
| `fromFloat` | `pub fn fromFloat(x: f80) F80` |
| `sign` | `pub fn sign(i: anytype) @TypeOf(i)` |

## multi_array_list

| Function | Signature |
|----------|-----------|
| `MultiArrayList` | `pub fn MultiArrayList(comptime T: type) type` |
| `initCapacity` | `pub fn initCapacity(gpa: Allocator, num: usize) Allocator.Error!Self` |
| `fromT` | `pub fn fromT(outer: T) @This()` |
| `toT` | `pub fn toT(tag: Tag, bare: Bare) T` |
| `items` | `pub fn items(self: Slice, comptime field: Field) []FieldType(field)` |
| `set` | `pub fn set(self: *Slice, index: usize, elem: T) void` |
| `get` | `pub fn get(self: Slice, index: usize) T` |
| `toMultiArrayList` | `pub fn toMultiArrayList(self: Slice) Self` |
| `deinit` | `pub fn deinit(self: *Slice, gpa: Allocator) void` |
| `subslice` | `pub fn subslice(s: Slice, off: usize, len: usize) Slice` |
| `deinit` | `pub fn deinit(self: *Self, gpa: Allocator) void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self) Slice` |
| `slice` | `pub fn slice(self: Self) Slice` |
| `items` | `pub fn items(self: Self, comptime field: Field) []FieldType(field)` |
| `set` | `pub fn set(self: *Self, index: usize, elem: T) void` |
| `get` | `pub fn get(self: Self, index: usize) T` |
| `append` | `pub fn append(self: *Self, gpa: Allocator, elem: T) Allocator.Error!void` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, elem: T) void` |
| `appendBounded` | `pub fn appendBounded(self: *Self, elem: T) error` |
| `addOne` | `pub fn addOne(self: *Self, gpa: Allocator) Allocator.Error!usize` |
| `addOneAssumeCapacity` | `pub fn addOneAssumeCapacity(self: *Self) usize` |
| `addOneBounded` | `pub fn addOneBounded(self: *Self) error` |
| `pop` | `pub fn pop(self: *Self) ?T` |
| `insert` | `pub fn insert(self: *Self, gpa: Allocator, index: usize, elem: T) !void` |
| `insertAssumeCapacity` | `pub fn insertAssumeCapacity(self: *Self, index: usize, elem: T) void` |
| `insertBounded` | `pub fn insertBounded(self: *Self, index: usize, elem: T) error` |
| `swapRemove` | `pub fn swapRemove(self: *Self, index: usize) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, index: usize) void` |
| `orderedRemoveMany` | `pub fn orderedRemoveMany(self: *Self, sorted_indexes: []const usize) void` |
| `resize` | `pub fn resize(self: *Self, gpa: Allocator, new_len: usize) Allocator.Error!void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, gpa: Allocator, new_len: usize) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, gpa: Allocator) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `growCapacity` | `pub fn growCapacity(minimum: usize) usize` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, gpa: Allocator, additional_count: usize) Allocator.Error!void` |
| `setCapacity` | `pub fn setCapacity(self: *Self, gpa: Allocator, new_capacity: usize) Allocator.Error!void` |
| `clone` | `pub fn clone(self: Self, gpa: Allocator) Allocator.Error!Self` |
| `swap` | `pub fn swap(sc: @This() , a_index: usize, b_index: usize) void` |
| `lessThan` | `pub fn lessThan(sc: @This() , a_index: usize, b_index: usize) bool` |
| `sort` | `pub fn sort(self: Self, ctx: anytype) void` |
| `sortSpan` | `pub fn sortSpan(self: Self, a: usize, b: usize, ctx: anytype) void` |
| `sortUnstable` | `pub fn sortUnstable(self: Self, ctx: anytype) void` |
| `sortSpanUnstable` | `pub fn sortSpanUnstable(self: Self, a: usize, b: usize, ctx: anytype) void` |
| `capacityInBytes` | `pub fn capacityInBytes(capacity: usize) usize` |

## pie

| Function | Signature |
|----------|-----------|
| `relocate` | `pub fn relocate(phdrs: []const elf.Phdr) void` |

## priority_dequeue

| Function | Signature |
|----------|-----------|
| `PriorityDequeue` | `pub fn PriorityDequeue(comptime T: type, comptime Context: type, comptime compareFn: fn (context: Context, a: T, b: T) Order) type` |
| `init` | `pub fn init(allocator: Allocator, context: Context) Self` |
| `deinit` | `pub fn deinit(self: Self) void` |
| `add` | `pub fn add(self: *Self, elem: T) !void` |
| `addSlice` | `pub fn addSlice(self: *Self, items: []const T) !void` |
| `peekMin` | `pub fn peekMin(self: *Self) ?T` |
| `peekMax` | `pub fn peekMax(self: *Self) ?T` |
| `count` | `pub fn count(self: Self) usize` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `fromOwnedSlice` | `pub fn fromOwnedSlice(allocator: Allocator, items: []T, context: Context) Self` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, new_capacity: usize) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: usize) !void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, new_len: usize) void` |
| `update` | `pub fn update(self: *Self, elem: T, new_elem: T) !void` |
| `next` | `pub fn next(it: *Iterator) ?T` |
| `reset` | `pub fn reset(it: *Iterator) void` |
| `iterator` | `pub fn iterator(self: *Self) Iterator` |

## priority_queue

| Function | Signature |
|----------|-----------|
| `PriorityQueue` | `pub fn PriorityQueue(comptime T: type, comptime Context: type, comptime compareFn: fn (context: Context, a: T, b: T) Order) type` |
| `init` | `pub fn init(allocator: Allocator, context: Context) Self` |
| `deinit` | `pub fn deinit(self: Self) void` |
| `add` | `pub fn add(self: *Self, elem: T) !void` |
| `addSlice` | `pub fn addSlice(self: *Self, items: []const T) !void` |
| `peek` | `pub fn peek(self: *Self) ?T` |
| `remove` | `pub fn remove(self: *Self) T` |
| `count` | `pub fn count(self: Self) usize` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `fromOwnedSlice` | `pub fn fromOwnedSlice(allocator: Allocator, items: []T, context: Context) Self` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, new_capacity: usize) !void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(self: *Self, new_capacity: usize) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: usize) !void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, new_capacity: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self) void` |
| `update` | `pub fn update(self: *Self, elem: T, new_elem: T) !void` |
| `next` | `pub fn next(it: *Iterator) ?T` |
| `reset` | `pub fn reset(it: *Iterator) void` |
| `iterator` | `pub fn iterator(self: *Self) Iterator` |

## simd

| Function | Signature |
|----------|-----------|
| `suggestVectorLengthForCpu` | `pub fn suggestVectorLengthForCpu(comptime T: type, comptime cpu: std.Target.Cpu) ?comptime_int` |
| `suggestVectorLength` | `pub fn suggestVectorLength(comptime T: type) ?comptime_int` |
| `VectorIndex` | `pub fn VectorIndex(comptime VectorType: type) type` |
| `VectorCount` | `pub fn VectorCount(comptime VectorType: type) type` |
| `iota` | `pub fn iota(comptime T: type, comptime len: usize) @Vector(len, T)` |
| `repeat` | `pub fn repeat(comptime len: usize, vec: anytype) @Vector(len, std.meta.Child(@TypeOf(vec)))` |
| `join` | `pub fn join(a: anytype, b: anytype) @Vector(vectorLength(@TypeOf(a)) + vectorLength(@TypeOf(b)), std.meta.Child(@TypeOf(a)))` |
| `interlace` | `pub fn interlace(vecs: anytype) @Vector(vectorLength(@TypeOf(vecs[0])) * vecs.len, std.meta.Child(@TypeOf(vecs[0])))` |
| `deinterlace` | `pub fn deinterlace(comptime vec_count: usize, interlaced: anytype,) [vec_count]@Vector( vectorLength(@TypeOf(interlaced)) / vec_count, std.meta.Child(@TypeOf(interlaced)), )` |
| `extract` | `pub fn extract(vec: anytype, comptime first: VectorIndex(@TypeOf(vec) ), comptime count: VectorCount(@TypeOf(vec)), ) @Vector(count, std.meta.Child(@TypeOf(vec)))` |
| `mergeShift` | `pub fn mergeShift(a: anytype, b: anytype, comptime shift: VectorCount(@TypeOf(a, b) )) @TypeOf(a, b)` |
| `shiftElementsRight` | `pub fn shiftElementsRight(vec: anytype, comptime amount: VectorCount(@TypeOf(vec) ), shift_in: std.meta.Child(@TypeOf(vec))) @TypeOf(vec)` |
| `shiftElementsLeft` | `pub fn shiftElementsLeft(vec: anytype, comptime amount: VectorCount(@TypeOf(vec) ), shift_in: std.meta.Child(@TypeOf(vec))) @TypeOf(vec)` |
| `rotateElementsLeft` | `pub fn rotateElementsLeft(vec: anytype, comptime amount: VectorCount(@TypeOf(vec) )) @TypeOf(vec)` |
| `rotateElementsRight` | `pub fn rotateElementsRight(vec: anytype, comptime amount: VectorCount(@TypeOf(vec) )) @TypeOf(vec)` |
| `reverseOrder` | `pub fn reverseOrder(vec: anytype) @TypeOf(vec)` |
| `firstTrue` | `pub fn firstTrue(vec: anytype) ?VectorIndex(@TypeOf(vec))` |
| `lastTrue` | `pub fn lastTrue(vec: anytype) ?VectorIndex(@TypeOf(vec))` |
| `countTrues` | `pub fn countTrues(vec: anytype) VectorCount(@TypeOf(vec))` |
| `firstIndexOfValue` | `pub fn firstIndexOfValue(vec: anytype, value: std.meta.Child(@TypeOf(vec) )) ?VectorIndex(@TypeOf(vec))` |
| `lastIndexOfValue` | `pub fn lastIndexOfValue(vec: anytype, value: std.meta.Child(@TypeOf(vec) )) ?VectorIndex(@TypeOf(vec))` |
| `countElementsWithValue` | `pub fn countElementsWithValue(vec: anytype, value: std.meta.Child(@TypeOf(vec) )) VectorCount(@TypeOf(vec))` |
| `prefixScanWithFunc` | `pub fn prefixScanWithFunc(comptime hop: isize, vec: anytype, /// The error type that `func` might return. Set this to `void` if `func` doesn't return an error union. comptime ErrorType: type, comptime func: fn (@TypeOf(vec) , @TypeOf(vec)) if (Err...` |
| `prefixScan` | `pub fn prefixScan(comptime op: std.builtin.ReduceOp, comptime hop: isize, vec: anytype) @TypeOf(vec)` |

## static_string_map

| Function | Signature |
|----------|-----------|
| `StaticStringMap` | `pub fn StaticStringMap(comptime V: type) type` |
| `defaultEql` | `pub fn defaultEql(a: []const u8, b: []const u8) bool` |
| `eqlAsciiIgnoreCase` | `pub fn eqlAsciiIgnoreCase(a: []const u8, b: []const u8) bool` |
| `StaticStringMapWithEql` | `pub fn StaticStringMapWithEql(comptime V: type, comptime eql: fn (a: []const u8, b: []const u8) bool, ) type` |
| `initComptime` | `pub fn initComptime(comptime kvs_list: anytype) Self` |
| `init` | `pub fn init(kvs_list: anytype, allocator: mem.Allocator) !Self` |
| `deinit` | `pub fn deinit(self: Self, allocator: mem.Allocator) void` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a: usize, b: usize) bool` |
| `swap` | `pub fn swap(ctx: @This() , a: usize, b: usize) void` |
| `has` | `pub fn has(self: Self, str: []const u8) bool` |
| `get` | `pub fn get(self: Self, str: []const u8) ?V` |
| `getIndex` | `pub fn getIndex(self: Self, str: []const u8) ?usize` |
| `getLongestPrefix` | `pub fn getLongestPrefix(self: Self, str: []const u8) ?KV` |
| `getLongestPrefixIndex` | `pub fn getLongestPrefixIndex(self: Self, str: []const u8) ?usize` |
| `keys` | `pub fn keys(self: Self) []const []const u8` |
| `values` | `pub fn values(self: Self) []const V` |

## std

| Function | Signature |
|----------|-----------|
| `ArrayList` | `pub fn ArrayList(comptime T: type) type` |

## tar

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(d: *Diagnostics) void` |
| `fullName` | `pub fn fullName(header: Header, buffer: []u8) ![]const u8` |
| `linkName` | `pub fn linkName(header: Header, buffer: []u8) ![]const u8` |
| `name` | `pub fn name(header: Header) []const u8` |
| `mode` | `pub fn mode(header: Header) !u32` |
| `size` | `pub fn size(header: Header) !u64` |
| `chksum` | `pub fn chksum(header: Header) !u64` |
| `is_ustar` | `pub fn is_ustar(header: Header) bool` |
| `prefix` | `pub fn prefix(header: Header) []const u8` |
| `kind` | `pub fn kind(header: Header) Kind` |
| `checkChksum` | `pub fn checkChksum(header: Header) !u64` |
| `init` | `pub fn init(reader: *Io.Reader, options: Options) Iterator` |
| `next` | `pub fn next(self: *Iterator) !?File` |
| `streamRemaining` | `pub fn streamRemaining(it: *Iterator, file: File, w: *Io.Writer) Io.Reader.StreamError!void` |
| `value` | `pub fn value(self: Attribute, dst: []u8) ![]const u8` |
| `next` | `pub fn next(self: *Self) !?Attribute` |

## treap

| Function | Signature |
|----------|-----------|
| `Treap` | `pub fn Treap(comptime Key: type, comptime compareFn: anytype) type` |
| `next` | `pub fn next(node: *Node) ?*Node` |
| `prev` | `pub fn prev(node: *Node) ?*Node` |
| `getMin` | `pub fn getMin(self: Self) ?*Node` |
| `getMax` | `pub fn getMax(self: Self) ?*Node` |
| `getEntryFor` | `pub fn getEntryFor(self: *Self, key: Key) Entry` |
| `getEntryForExisting` | `pub fn getEntryForExisting(self: *Self, node: *Node) Entry` |
| `set` | `pub fn set(self: *Entry, new_node: ?*Node) void` |
| `next` | `pub fn next(it: *InorderIterator) ?*Node` |
| `inorderIterator` | `pub fn inorderIterator(self: *Self) InorderIterator` |
| `init` | `pub fn init(slice: []T, rng: std.Random) Self` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) ?*T` |

## tz

| Function | Signature |
|----------|-----------|
| `name` | `pub fn name(self: *const Timetype) [:0]const u8` |
| `isDst` | `pub fn isDst(self: Timetype) bool` |
| `standardTimeIndicator` | `pub fn standardTimeIndicator(self: Timetype) bool` |
| `utIndicator` | `pub fn utIndicator(self: Timetype) bool` |
| `parse` | `pub fn parse(allocator: Allocator, reader: *Reader) !Tz` |
| `deinit` | `pub fn deinit(self: *Tz) void` |

## unicode

| Function | Signature |
|----------|-----------|
| `utf8CodepointSequenceLength` | `pub fn utf8CodepointSequenceLength(c: u21) !u3` |
| `utf8ByteSequenceLength` | `pub fn utf8ByteSequenceLength(first_byte: u8) !u3` |
| `utf8Encode` | `pub fn utf8Encode(c: u21, out: []u8) error` |
| `utf8EncodeComptime` | `pub fn utf8EncodeComptime(comptime c: u21) [ utf8CodepointSequenceLength(c) catch |err| @compileError(@errorName(err)) ]u8` |
| `utf8Decode` | `pub fn utf8Decode(bytes: []const u8) Utf8DecodeError!u21` |
| `utf8Decode2` | `pub fn utf8Decode2(bytes: [2]u8) Utf8Decode2Error!u21` |
| `utf8Decode3` | `pub fn utf8Decode3(bytes: [3]u8) Utf8Decode3Error!u21` |
| `utf8Decode3AllowSurrogateHalf` | `pub fn utf8Decode3AllowSurrogateHalf(bytes: [3]u8) Utf8Decode3AllowSurrogateHalfError!u21` |
| `utf8Decode4` | `pub fn utf8Decode4(bytes: [4]u8) Utf8Decode4Error!u21` |
| `utf8ValidCodepoint` | `pub fn utf8ValidCodepoint(value: u21) bool` |
| `utf8CountCodepoints` | `pub fn utf8CountCodepoints(s: []const u8) !usize` |
| `utf8ValidateSlice` | `pub fn utf8ValidateSlice(input: []const u8) bool` |
| `init` | `pub fn init(s: []const u8) !Utf8View` |
| `initUnchecked` | `pub fn initUnchecked(s: []const u8) Utf8View` |
| `initComptime` | `pub fn initComptime(comptime s: []const u8) Utf8View` |
| `iterator` | `pub fn iterator(s: Utf8View) Utf8Iterator` |
| `nextCodepointSlice` | `pub fn nextCodepointSlice(it: *Utf8Iterator) ?[]const u8` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Utf8Iterator) ?u21` |
| `peek` | `pub fn peek(it: *Utf8Iterator, n: usize) []const u8` |
| `utf16IsHighSurrogate` | `pub fn utf16IsHighSurrogate(c: u16) bool` |
| `utf16IsLowSurrogate` | `pub fn utf16IsLowSurrogate(c: u16) bool` |
| `utf16CodepointSequenceLength` | `pub fn utf16CodepointSequenceLength(c: u21) !u2` |
| `utf16CodeUnitSequenceLength` | `pub fn utf16CodeUnitSequenceLength(first_code_unit: u16) !u2` |
| `utf16DecodeSurrogatePair` | `pub fn utf16DecodeSurrogatePair(surrogate_pair: []const u16) !u21` |
| `init` | `pub fn init(s: []const u16) Utf16LeIterator` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Utf16LeIterator) NextCodepointError!?u21` |
| `utf16CountCodepoints` | `pub fn utf16CountCodepoints(utf16le: []const u16) !usize` |
| `fmtUtf8` | `pub fn fmtUtf8(utf8: []const u8) std.fmt.Alt([]const u8, formatUtf8)` |
| `utf16LeToUtf8ArrayList` | `pub fn utf16LeToUtf8ArrayList(result: *std.array_list.Managed(u8) , utf16le: []const u16) Utf16LeToUtf8AllocError!void` |
| `utf16LeToUtf8Alloc` | `pub fn utf16LeToUtf8Alloc(allocator: Allocator, utf16le: []const u16) Utf16LeToUtf8AllocError![]u8` |
| `utf16LeToUtf8AllocZ` | `pub fn utf16LeToUtf8AllocZ(allocator: Allocator, utf16le: []const u16) Utf16LeToUtf8AllocError![:0]u8` |
| `utf16LeToUtf8` | `pub fn utf16LeToUtf8(utf8: []u8, utf16le: []const u16) Utf16LeToUtf8Error!usize` |
| `utf8ToUtf16LeArrayList` | `pub fn utf8ToUtf16LeArrayList(result: *std.array_list.Managed(u16) , utf8: []const u8) error` |
| `utf8ToUtf16LeAlloc` | `pub fn utf8ToUtf16LeAlloc(allocator: Allocator, utf8: []const u8) error` |
| `utf8ToUtf16LeAllocZ` | `pub fn utf8ToUtf16LeAllocZ(allocator: Allocator, utf8: []const u8) error` |
| `utf8ToUtf16Le` | `pub fn utf8ToUtf16Le(utf16le: []u16, utf8: []const u8) error` |
| `utf8ToUtf16LeImpl` | `pub fn utf8ToUtf16LeImpl(utf16le: []u16, utf8: []const u8, comptime surrogates: Surrogates) !usize` |
| `utf8ToUtf16LeStringLiteral` | `pub fn utf8ToUtf16LeStringLiteral(comptime utf8: []const u8) *const [calcUtf16LeLen(utf8) catch |err| @compileError(err):0]u16` |
| `wtf8ToWtf16LeStringLiteral` | `pub fn wtf8ToWtf16LeStringLiteral(comptime wtf8: []const u8) *const [calcWtf16LeLen(wtf8) catch |err| @compileError(err):0]u16` |
| `calcUtf16LeLenImpl` | `pub fn calcUtf16LeLenImpl(utf8: []const u8, comptime surrogates: Surrogates) !usize` |
| `calcUtf16LeLen` | `pub fn calcUtf16LeLen(utf8: []const u8) CalcUtf16LeLenError!usize` |
| `calcWtf16LeLen` | `pub fn calcWtf16LeLen(wtf8: []const u8) CalcWtf16LeLenError!usize` |
| `fmtUtf16Le` | `pub fn fmtUtf16Le(utf16le: []const u16) std.fmt.Alt([]const u16, formatUtf16Le)` |
| `isSurrogateCodepoint` | `pub fn isSurrogateCodepoint(c: u21) bool` |
| `wtf8Encode` | `pub fn wtf8Encode(c: u21, out: []u8) error` |
| `wtf8Decode` | `pub fn wtf8Decode(bytes: []const u8) Wtf8DecodeError!u21` |
| `wtf8ValidateSlice` | `pub fn wtf8ValidateSlice(input: []const u8) bool` |
| `init` | `pub fn init(s: []const u8) error` |
| `initUnchecked` | `pub fn initUnchecked(s: []const u8) Wtf8View` |
| `initComptime` | `pub fn initComptime(comptime s: []const u8) Wtf8View` |
| `iterator` | `pub fn iterator(s: Wtf8View) Wtf8Iterator` |
| `nextCodepointSlice` | `pub fn nextCodepointSlice(it: *Wtf8Iterator) ?[]const u8` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Wtf8Iterator) ?u21` |
| `peek` | `pub fn peek(it: *Wtf8Iterator, n: usize) []const u8` |
| `wtf16LeToWtf8ArrayList` | `pub fn wtf16LeToWtf8ArrayList(result: *std.array_list.Managed(u8) , utf16le: []const u16) Allocator.Error!void` |
| `wtf16LeToWtf8Alloc` | `pub fn wtf16LeToWtf8Alloc(allocator: Allocator, wtf16le: []const u16) Allocator.Error![]u8` |
| `wtf16LeToWtf8AllocZ` | `pub fn wtf16LeToWtf8AllocZ(allocator: Allocator, wtf16le: []const u16) Allocator.Error![:0]u8` |
| `wtf16LeToWtf8` | `pub fn wtf16LeToWtf8(wtf8: []u8, wtf16le: []const u16) usize` |
| `wtf8ToWtf16LeArrayList` | `pub fn wtf8ToWtf16LeArrayList(result: *std.array_list.Managed(u16) , wtf8: []const u8) error` |
| `wtf8ToWtf16LeAlloc` | `pub fn wtf8ToWtf16LeAlloc(allocator: Allocator, wtf8: []const u8) error` |
| `wtf8ToWtf16LeAllocZ` | `pub fn wtf8ToWtf16LeAllocZ(allocator: Allocator, wtf8: []const u8) error` |
| `wtf8ToWtf16Le` | `pub fn wtf8ToWtf16Le(wtf16le: []u16, wtf8: []const u8) error` |
| `wtf8ToUtf8Lossy` | `pub fn wtf8ToUtf8Lossy(utf8: []u8, wtf8: []const u8) error` |
| `wtf8ToUtf8LossyAlloc` | `pub fn wtf8ToUtf8LossyAlloc(allocator: Allocator, wtf8: []const u8) error` |
| `wtf8ToUtf8LossyAllocZ` | `pub fn wtf8ToUtf8LossyAllocZ(allocator: Allocator, wtf8: []const u8) error` |
| `init` | `pub fn init(s: []const u16) Wtf16LeIterator` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Wtf16LeIterator) ?u21` |
| `calcWtf8Len` | `pub fn calcWtf8Len(wtf16le: []const u16) usize` |

## valgrind

| Function | Signature |
|----------|-----------|
| `doClientRequest` | `pub fn doClientRequest(default: usize, request: usize, a1: usize, a2: usize, a3: usize, a4: usize, a5: usize) usize` |
| `ToolBase` | `pub fn ToolBase(base: [2]u8) u32` |
| `IsTool` | `pub fn IsTool(base: [2]u8, code: usize) bool` |
| `runningOnValgrind` | `pub fn runningOnValgrind() usize` |
| `discardTranslations` | `pub fn discardTranslations(qzz: []const u8) void` |
| `innerThreads` | `pub fn innerThreads(qzz: [*]u8) void` |
| `nonSimdCall0` | `pub fn nonSimdCall0(func: fn (usize) usize) usize` |
| `nonSimdCall1` | `pub fn nonSimdCall1(func: fn (usize, usize) usize, a1: usize) usize` |
| `nonSimdCall2` | `pub fn nonSimdCall2(func: fn (usize, usize, usize) usize, a1: usize, a2: usize) usize` |
| `nonSimdCall3` | `pub fn nonSimdCall3(func: fn (usize, usize, usize, usize) usize, a1: usize, a2: usize, a3: usize) usize` |
| `countErrors` | `pub fn countErrors() usize` |
| `mallocLikeBlock` | `pub fn mallocLikeBlock(mem: []u8, rzB: usize, is_zeroed: bool) void` |
| `resizeInPlaceBlock` | `pub fn resizeInPlaceBlock(oldmem: []u8, newsize: usize, rzB: usize) void` |
| `freeLikeBlock` | `pub fn freeLikeBlock(addr: [*]u8, rzB: usize) void` |
| `createMempool` | `pub fn createMempool(pool: [*]u8, rzB: usize, is_zeroed: bool, flags: usize) void` |
| `destroyMempool` | `pub fn destroyMempool(pool: [*]u8) void` |
| `mempoolAlloc` | `pub fn mempoolAlloc(pool: [*]u8, mem: []u8) void` |
| `mempoolFree` | `pub fn mempoolFree(pool: [*]u8, addr: [*]u8) void` |
| `mempoolTrim` | `pub fn mempoolTrim(pool: [*]u8, mem: []u8) void` |
| `moveMempool` | `pub fn moveMempool(poolA: [*]u8, poolB: [*]u8) void` |
| `mempoolChange` | `pub fn mempoolChange(pool: [*]u8, addrA: [*]u8, mem: []u8) void` |
| `mempoolExists` | `pub fn mempoolExists(pool: [*]u8) bool` |
| `stackRegister` | `pub fn stackRegister(stack: []u8) usize` |
| `stackDeregister` | `pub fn stackDeregister(id: usize) void` |
| `stackChange` | `pub fn stackChange(id: usize, newstack: []u8) void` |
| `loadPdbDebuginfo` | `pub fn loadPdbDebuginfo(fd, ptr, total_size, delta) void` |
| `mapIpToSrcloc` | `pub fn mapIpToSrcloc(addr: *const u8, buf64: [64]u8) usize` |
| `disableErrorReporting` | `pub fn disableErrorReporting() void` |
| `enableErrorReporting` | `pub fn enableErrorReporting() void` |
| `monitorCommand` | `pub fn monitorCommand(command: [*]u8) bool` |

## wasm

| Function | Signature |
|----------|-----------|
| `fromValtype` | `pub fn fromValtype(valtype: Valtype) BlockType` |

## zig

| Function | Signature |
|----------|-----------|
| `terminalMode` | `pub fn terminalMode(color: Color) ?Io.Terminal.Mode` |
| `hashSrc` | `pub fn hashSrc(src: []const u8) SrcHash` |
| `srcHashEql` | `pub fn srcHashEql(a: SrcHash, b: SrcHash) bool` |
| `hashName` | `pub fn hashName(parent_hash: SrcHash, sep: []const u8, name: []const u8) SrcHash` |
| `eql` | `pub fn eql(a: Loc, b: Loc) bool` |
| `findLineColumn` | `pub fn findLineColumn(source: []const u8, byte_offset: usize) Loc` |
| `lineDelta` | `pub fn lineDelta(source: []const u8, start: usize, end: usize) isize` |
| `binNameAlloc` | `pub fn binNameAlloc(allocator: Allocator, options: BinNameOptions) error` |
| `eql` | `pub fn eql(a: BuildId, b: BuildId) bool` |
| `toSlice` | `pub fn toSlice(hs: *const HexString) []const u8` |
| `initHexString` | `pub fn initHexString(bytes: []const u8) BuildId` |
| `parse` | `pub fn parse(text: []const u8) !BuildId` |
| `format` | `pub fn format(id: BuildId, writer: *Writer) Writer.Error!void` |
| `serializeCpu` | `pub fn serializeCpu(buffer: *std.array_list.Managed(u8) , cpu: std.Target.Cpu) Allocator.Error!void` |
| `serializeCpuAlloc` | `pub fn serializeCpuAlloc(ally: Allocator, cpu: std.Target.Cpu) Allocator.Error![]u8` |
| `fmtId` | `pub fn fmtId(bytes: []const u8) FormatId` |
| `fmtIdFlags` | `pub fn fmtIdFlags(bytes: []const u8, flags: FormatId.Flags) FormatId` |
| `fmtIdPU` | `pub fn fmtIdPU(bytes: []const u8) FormatId` |
| `fmtIdP` | `pub fn fmtIdP(bytes: []const u8) FormatId` |
| `format` | `pub fn format(ctx: FormatId, writer: *Writer) Writer.Error!void` |
| `fmtString` | `pub fn fmtString(bytes: []const u8) std.fmt.Alt([]const u8, stringEscape)` |
| `fmtChar` | `pub fn fmtChar(c: u21) std.fmt.Alt(u21, charEscape)` |
| `stringEscape` | `pub fn stringEscape(bytes: []const u8, w: *Writer) Writer.Error!void` |
| `charEscape` | `pub fn charEscape(codepoint: u21, w: *Writer) Writer.Error!void` |
| `isValidId` | `pub fn isValidId(bytes: []const u8) bool` |
| `isUnderscore` | `pub fn isUnderscore(bytes: []const u8) bool` |
| `readSourceFileToEndAlloc` | `pub fn readSourceFileToEndAlloc(gpa: Allocator, file_reader: *Io.File.Reader) ![:0]u8` |
| `printAstErrorsToStderr` | `pub fn printAstErrorsToStderr(gpa: Allocator, io: Io, tree: Ast, path: []const u8, color: Color) !void` |
| `putAstErrorsIntoBundle` | `pub fn putAstErrorsIntoBundle(gpa: Allocator, tree: Ast, path: []const u8, wip_errors: *std.zig.ErrorBundle.Wip,) Allocator.Error!void` |
| `resolveTargetQueryOrFatal` | `pub fn resolveTargetQueryOrFatal(io: Io, target_query: std.Target.Query) std.Target` |
| `parseTargetQueryOrReportFatalError` | `pub fn parseTargetQueryOrReportFatalError(allocator: Allocator, opts: std.Target.Query.ParseOptions,) std.Target.Query` |
| `isSet` | `pub fn isSet(ev: EnvVar, map: *const std.process.Environ.Map) bool` |
| `get` | `pub fn get(ev: EnvVar, map: *const std.process.Environ.Map) ?[]const u8` |
| `message` | `pub fn message(r: SimpleComptimeReason) []const u8` |
| `cacheName` | `pub fn cacheName(ea: EmitArtifact, gpa: Allocator, opts: BinNameOptions) Allocator.Error![]const u8` |

## zip

| Function | Signature |
|----------|-----------|
| `need_zip64` | `pub fn need_zip64(self: EndRecord) bool` |
| `findBuffer` | `pub fn findBuffer(buffer: []const u8) FindBufferError!EndRecord` |
| `findFile` | `pub fn findFile(fr: *File.Reader) FindFileError!EndRecord` |
| `init` | `pub fn init(reader: *Reader, method: CompressionMethod, buffer: []u8) Reader` |
| `init` | `pub fn init(input: *File.Reader) !Iterator` |
| `next` | `pub fn next(self: *Iterator) !?Entry` |
| `extract` | `pub fn extract(self: Entry, stream: *File.Reader, options: ExtractOptions, filename_buf: []u8, dest: Io.Dir,) !void` |
| `deinit` | `pub fn deinit(self: *Diagnostics) void` |
| `nextFilename` | `pub fn nextFilename(self: *Diagnostics, name: []const u8) error` |
| `extract` | `pub fn extract(dest: Io.Dir, fr: *File.Reader, options: ExtractOptions) !void` |

## sort / block

| Function | Signature |
|----------|-----------|
| `block` | `pub fn block(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (@TypeOf(context) , lhs: T, rhs: T) bool, ) void` |

## sort / pdq

| Function | Signature |
|----------|-----------|
| `pdq` | `pub fn pdq(comptime T: type, items: []T, context: anytype, comptime lessThanFn: fn (context: @TypeOf(context) , lhs: T, rhs: T) bool, ) void` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a: usize, b: usize) bool` |
| `swap` | `pub fn swap(ctx: @This() , a: usize, b: usize) void` |
| `pdqContext` | `pub fn pdqContext(a: usize, b: usize, context: anytype) void` |

## crypto / Certificate

| Function | Signature |
|----------|-----------|
| `Hash` | `pub fn Hash(comptime algorithm: Algorithm) type` |
| `Curve` | `pub fn Curve(comptime curve: NamedCurve) type` |
| `slice` | `pub fn slice(p: Parsed, s: Slice) []const u8` |
| `issuer` | `pub fn issuer(p: Parsed) []const u8` |
| `subject` | `pub fn subject(p: Parsed) []const u8` |
| `commonName` | `pub fn commonName(p: Parsed) []const u8` |
| `signature` | `pub fn signature(p: Parsed) []const u8` |
| `pubKey` | `pub fn pubKey(p: Parsed) []const u8` |
| `message` | `pub fn message(p: Parsed) []const u8` |
| `subjectAltName` | `pub fn subjectAltName(p: Parsed) []const u8` |
| `verify` | `pub fn verify(parsed_subject: Parsed, parsed_issuer: Parsed, now_sec: i64) VerifyError!void` |
| `verifyHostName` | `pub fn verifyHostName(parsed_subject: Parsed, host_name: []const u8) VerifyHostNameError!void` |
| `parse` | `pub fn parse(cert: Certificate) ParseError!Parsed` |
| `verify` | `pub fn verify(subject: Certificate, issuer: Certificate, now_sec: i64) !void` |
| `contents` | `pub fn contents(cert: Certificate, elem: der.Element) []const u8` |
| `parseBitString` | `pub fn parseBitString(cert: Certificate, elem: der.Element) !der.Element.Slice` |
| `parseTime` | `pub fn parseTime(cert: Certificate, elem: der.Element) ParseTimeError!u64` |
| `toSeconds` | `pub fn toSeconds(date: Date) u64` |
| `parseTimeDigits` | `pub fn parseTimeDigits(text: *const [2]u8, min: u8, max: u8) !u8` |
| `parseYear4` | `pub fn parseYear4(text: *const [4]u8) !u16` |
| `parseAlgorithm` | `pub fn parseAlgorithm(bytes: []const u8, element: der.Element) ParseEnumError!Algorithm` |
| `parseAlgorithmCategory` | `pub fn parseAlgorithmCategory(bytes: []const u8, element: der.Element) ParseEnumError!AlgorithmCategory` |
| `parseAttribute` | `pub fn parseAttribute(bytes: []const u8, element: der.Element) ParseEnumError!Attribute` |
| `parseNamedCurve` | `pub fn parseNamedCurve(bytes: []const u8, element: der.Element) ParseEnumError!NamedCurve` |
| `parseExtensionId` | `pub fn parseExtensionId(bytes: []const u8, element: der.Element) ParseEnumError!ExtensionId` |
| `parseVersion` | `pub fn parseVersion(bytes: []const u8, version_elem: der.Element) ParseVersionError!Version` |
| `parse` | `pub fn parse(bytes: []const u8, index: u32) Element.ParseError!Element` |
| `fromBytes` | `pub fn fromBytes(comptime modulus_len: usize, msg: []const u8) [modulus_len]u8` |
| `verify` | `pub fn verify(comptime modulus_len: usize, sig: [modulus_len]u8, msg: []const u8, public_key: PublicKey, comptime Hash: type,) VerifyError!void` |
| `concatVerify` | `pub fn concatVerify(comptime modulus_len: usize, sig: [modulus_len]u8, msg: []const []const u8, public_key: PublicKey, comptime Hash: type,) VerifyError!void` |
| `fromBytes` | `pub fn fromBytes(pub_bytes: []const u8, modulus_bytes: []const u8) FromBytesError!PublicKey` |
| `parseDer` | `pub fn parseDer(pub_key: []const u8) ParseDerError!struct` |

## crypto / Sha1

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Sha1` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Sha1, b: []const u8) void` |
| `peek` | `pub fn peek(d: Sha1) [digest_length]u8` |
| `final` | `pub fn final(d: *Sha1, out: *[digest_length]u8) void` |
| `finalResult` | `pub fn finalResult(d: *Sha1) [digest_length]u8` |

## crypto / aegis

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |
| `initWithNonce` | `pub fn initWithNonce(key: *const [key_length]u8, nonce: *const [nonce_length]u8) Mac` |
| `init` | `pub fn init(key: *const [key_length]u8) Mac` |
| `update` | `pub fn update(self: *Mac, b: []const u8) void` |
| `final` | `pub fn final(self: *Mac, out: *[mac_length]u8) void` |
| `createWithNonce` | `pub fn createWithNonce(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8, nonce: *const [nonce_length]u8) void` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |

## crypto / aes_ccm

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8,) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8,) AuthenticationError!void` |

## crypto / aes_gcm

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / aes_gcm_siv

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / aes_ocb

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / aes_siv

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: ?[]const u8, nonce: ?[]const u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: ?[]const u8, nonce: ?[]const u8, key: [key_length]u8) AuthenticationError!void` |
| `encryptWithAdVector` | `pub fn encryptWithAdVector(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const []const u8, key: [key_length]u8) void` |
| `decryptWithAdVector` | `pub fn decryptWithAdVector(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const []const u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / argon2

| Function | Signature |
|----------|-----------|
| `fromLimits` | `pub fn fromLimits(ops_limit: u32, mem_limit: usize) Self` |
| `kdf` | `pub fn kdf(allocator: mem.Allocator, derived_key: []u8, password: []const u8, salt: []const u8, params: Params, mode: Mode, io: Io,) KdfError!void` |
| `create` | `pub fn create(allocator: mem.Allocator, password: []const u8, params: Params, mode: Mode, buf: []u8, io: Io,) HasherError![]const u8` |
| `verify` | `pub fn verify(allocator: mem.Allocator, str: []const u8, password: []const u8, io: Io,) HasherError!void` |
| `strHash` | `pub fn strHash(password: []const u8, options: HashOptions, out: []u8, io: Io,) Error![]const u8` |
| `strVerify` | `pub fn strVerify(str: []const u8, password: []const u8, options: VerifyOptions, io: Io,) Error!void` |

## crypto / ascon

| Function | Signature |
|----------|-----------|
| `State` | `pub fn State(comptime endian: std.builtin.Endian) type` |
| `init` | `pub fn init(initial_state: [block_bytes]u8) Self` |
| `initFromWords` | `pub fn initFromWords(initial_state: [5]u64) Self` |
| `initXof` | `pub fn initXof() Self` |
| `initXofA` | `pub fn initXofA() Self` |
| `asBytes` | `pub fn asBytes(self: *Self) *[block_bytes]u8` |
| `endianSwap` | `pub fn endianSwap(self: *Self) void` |
| `setBytes` | `pub fn setBytes(self: *Self, bytes: []const u8) void` |
| `addByte` | `pub fn addByte(self: *Self, byte: u8, offset: usize) void` |
| `addBytes` | `pub fn addBytes(self: *Self, bytes: []const u8) void` |
| `extractBytes` | `pub fn extractBytes(self: *Self, out: []u8) void` |
| `xorBytes` | `pub fn xorBytes(self: *Self, out: []u8, in: []const u8) void` |
| `clear` | `pub fn clear(self: *Self, from: usize, to: usize) void` |
| `secureZero` | `pub fn secureZero(self: *Self) void` |
| `permuteR` | `pub fn permuteR(state: *Self, comptime rounds: u4) void` |
| `permute` | `pub fn permute(state: *Self) void` |
| `permuteRatchet` | `pub fn permuteRatchet(state: *Self, comptime rounds: u4, comptime rate: u6) void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `init` | `pub fn init(options: Options) AsconHash256` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(self: *AsconHash256, b: []const u8) void` |
| `final` | `pub fn final(self: *AsconHash256, out: *[digest_length]u8) void` |
| `init` | `pub fn init(options: Options) AsconXof128` |
| `hash` | `pub fn hash(bytes: []const u8, out: []u8, options: Options) void` |
| `update` | `pub fn update(self: *AsconXof128, b: []const u8) void` |
| `squeeze` | `pub fn squeeze(self: *AsconXof128, out: []u8) void` |
| `init` | `pub fn init(options: Options) AsconCxof128` |
| `update` | `pub fn update(self: *AsconCxof128, b: []const u8) void` |
| `squeeze` | `pub fn squeeze(self: *AsconCxof128, out: []u8) void` |

## crypto / bcrypt

| Function | Signature |
|----------|-----------|
| `bcrypt` | `pub fn bcrypt(password: []const u8, salt: *const [salt_length]u8, params: Params,) [dk_length]u8` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: []const u8) void` |
| `init` | `pub fn init(key: []const u8) Self` |
| `update` | `pub fn update(self: *Self, msg: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |
| `hash` | `pub fn hash(sha2pass: [Sha512.digest_length]u8, sha2salt: [Sha512.digest_length]u8) [32]u8` |
| `pbkdf` | `pub fn pbkdf(pass: []const u8, salt: []const u8, key: []u8, rounds: u32) !void` |
| `opensshKdf` | `pub fn opensshKdf(pass: []const u8, salt: []const u8, key: []u8, rounds: u32) !void` |
| `strHash` | `pub fn strHash(password: []const u8, options: HashOptions, out: []u8, io: std.Io,) Error![]const u8` |
| `strHashWithSalt` | `pub fn strHashWithSalt(password: []const u8, options: HashOptions, out: []u8, salt: [salt_length]u8,) Error![]const u8` |
| `strVerify` | `pub fn strVerify(str: []const u8, password: []const u8, options: VerifyOptions,) Error!void` |

## crypto / benchmark

| Function | Signature |
|----------|-----------|
| `benchmarkHash` | `pub fn benchmarkHash(comptime Hash: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkHashParallel` | `pub fn benchmarkHashParallel(comptime Hash: anytype, comptime bytes: comptime_int, allocator: mem.Allocator, io: std.Io) !u64` |
| `benchmarkMac` | `pub fn benchmarkMac(comptime Mac: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkKeyExchange` | `pub fn benchmarkKeyExchange(comptime DhKeyExchange: anytype, comptime exchange_count: comptime_int) !u64` |
| `benchmarkSignature` | `pub fn benchmarkSignature(comptime Signature: anytype, comptime signatures_count: comptime_int, io: std.Io) !u64` |
| `benchmarkSignatureVerification` | `pub fn benchmarkSignatureVerification(comptime Signature: anytype, comptime signatures_count: comptime_int, io: std.Io) !u64` |
| `benchmarkBatchSignatureVerification` | `pub fn benchmarkBatchSignatureVerification(comptime Signature: anytype, comptime signatures_count: comptime_int, io: std.Io) !u64` |
| `benchmarkKem` | `pub fn benchmarkKem(comptime Kem: anytype, comptime kems_count: comptime_int, io: std.Io) !u64` |
| `benchmarkKemDecaps` | `pub fn benchmarkKemDecaps(comptime Kem: anytype, comptime kems_count: comptime_int, io: std.Io) !u64` |
| `benchmarkKemKeyGen` | `pub fn benchmarkKemKeyGen(comptime Kem: anytype, comptime kems_count: comptime_int, io: std.Io) !u64` |
| `benchmarkAead` | `pub fn benchmarkAead(comptime Aead: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkAes` | `pub fn benchmarkAes(comptime Aes: anytype, comptime count: comptime_int) !u64` |
| `benchmarkAes8` | `pub fn benchmarkAes8(comptime Aes: anytype, comptime count: comptime_int) !u64` |
| `main` | `pub fn main(init: std.process.Init) !void` |

## crypto / blake2

| Function | Signature |
|----------|-----------|
| `Blake2s` | `pub fn Blake2s(comptime out_bits: usize) type` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `Blake2b` | `pub fn Blake2b(comptime out_bits: usize) type` |

## crypto / blake3

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Blake3` |
| `initKdf` | `pub fn initKdf(context: []const u8, options: KdfOptions) Blake3` |
| `hash` | `pub fn hash(b: []const u8, out: []u8, options: Options) void` |
| `hashParallel` | `pub fn hashParallel(b: []const u8, out: []u8, options: Options, allocator: Allocator, io: Io) error` |
| `update` | `pub fn update(self: *Blake3, input: []const u8) void` |
| `final` | `pub fn final(self: *const Blake3, out: []u8) void` |
| `finalizeSeek` | `pub fn finalizeSeek(self: *const Blake3, seek: u64, out: []u8) void` |
| `reset` | `pub fn reset(self: *Blake3) void` |

## crypto / cbc_mac

| Function | Signature |
|----------|-----------|
| `CbcMac` | `pub fn CbcMac(comptime BlockCipher: type) type` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(self: *Self, msg: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |

## crypto / chacha20

| Function | Signature |
|----------|-----------|
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u32, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `stream` | `pub fn stream(out: []u8, counter: u32, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u64, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `stream` | `pub fn stream(out: []u8, counter: u64, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |

## crypto / cmac

| Function | Signature |
|----------|-----------|
| `Cmac` | `pub fn Cmac(comptime BlockCipher: type) type` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(self: *Self, msg: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |

## crypto / ecdsa

| Function | Signature |
|----------|-----------|
| `Ecdsa` | `pub fn Ecdsa(comptime Curve: type, comptime Hash: type) type` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) !SecretKey` |
| `toBytes` | `pub fn toBytes(sk: SecretKey) [encoded_length]u8` |
| `fromSec1` | `pub fn fromSec1(sec1: []const u8) !PublicKey` |
| `toCompressedSec1` | `pub fn toCompressedSec1(pk: PublicKey) [compressed_sec1_encoded_length]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(pk: PublicKey) [uncompressed_sec1_encoded_length]u8` |
| `verifier` | `pub fn verifier(sig: Signature, public_key: PublicKey) Verifier.InitError!Verifier` |
| `verify` | `pub fn verify(sig: Signature, msg: []const u8, public_key: PublicKey) VerifyError!void` |
| `verifyPrehashed` | `pub fn verifyPrehashed(sig: Signature, msg_hash: [Hash.digest_length]u8, public_key: PublicKey) VerifyError!void` |
| `toBytes` | `pub fn toBytes(sig: Signature) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) Signature` |
| `toDer` | `pub fn toDer(sig: Signature, buf: *[der_encoded_length_max]u8) []u8` |
| `fromDer` | `pub fn fromDer(der: []const u8) EncodingError!Signature` |
| `update` | `pub fn update(self: *Signer, data: []const u8) void` |
| `finalize` | `pub fn finalize(self: *Signer) (IdentityElementError || NonCanonicalError)!Signature` |
| `update` | `pub fn update(self: *Verifier, data: []const u8) void` |
| `verify` | `pub fn verify(self: *Verifier) VerifyError!void` |
| `generateDeterministic` | `pub fn generateDeterministic(seed: [seed_length]u8) IdentityElementError!KeyPair` |
| `generate` | `pub fn generate(io: std.Io) KeyPair` |
| `fromSecretKey` | `pub fn fromSecretKey(secret_key: SecretKey) IdentityElementError!KeyPair` |
| `sign` | `pub fn sign(key_pair: KeyPair, msg: []const u8, noise: ?[noise_length]u8) (IdentityElementError || NonCanonicalError)!Signature` |
| `signPrehashed` | `pub fn signPrehashed(key_pair: KeyPair, msg_hash: [Hash.digest_length]u8, noise: ?[noise_length]u8) (IdentityElementError || NonCanonicalError)!Signature` |
| `signer` | `pub fn signer(key_pair: KeyPair, noise: ?[noise_length]u8) !Signer` |

## crypto / ff

| Function | Signature |
|----------|-----------|
| `Uint` | `pub fn Uint(comptime max_bits: comptime_int) type` |
| `fromPrimitive` | `pub fn fromPrimitive(comptime T: type, init_value: T) OverflowError!Self` |
| `toPrimitive` | `pub fn toPrimitive(self: Self, comptime T: type) OverflowError!T` |
| `toBytes` | `pub fn toBytes(self: Self, bytes: []u8, comptime endian: Endian) OverflowError!void` |
| `fromBytes` | `pub fn fromBytes(bytes: []const u8, comptime endian: Endian) OverflowError!Self` |
| `eql` | `pub fn eql(x: Self, y: Self) bool` |
| `compare` | `pub fn compare(x: Self, y: Self) math.Order` |
| `isZero` | `pub fn isZero(x: Self) bool` |
| `isOdd` | `pub fn isOdd(x: Self) bool` |
| `addWithOverflow` | `pub fn addWithOverflow(x: *Self, y: Self) u1` |
| `subWithOverflow` | `pub fn subWithOverflow(x: *Self, y: Self) u1` |
| `fromPrimitive` | `pub fn fromPrimitive(comptime T: type, m: Modulus(bits) , x: T) (OverflowError || FieldElementError)!Self` |
| `toPrimitive` | `pub fn toPrimitive(self: Self, comptime T: type) (OverflowError || RepresentationError)!T` |
| `fromBytes` | `pub fn fromBytes(m: Modulus(bits) , bytes: []const u8, comptime endian: Endian) (OverflowError || FieldElementError)!Self` |
| `toBytes` | `pub fn toBytes(self: Self, bytes: []u8, comptime endian: Endian) (OverflowError || RepresentationError)!void` |
| `isZero` | `pub fn isZero(self: Self) bool` |
| `isOdd` | `pub fn isOdd(self: Self) bool` |
| `Modulus` | `pub fn Modulus(comptime max_bits: comptime_int) type` |
| `bits` | `pub fn bits(self: Self) usize` |
| `one` | `pub fn one(self: Self) Fe` |
| `fromUint` | `pub fn fromUint(v_: FeUint) InvalidModulusError!Self` |
| `fromPrimitive` | `pub fn fromPrimitive(comptime T: type, x: T) (InvalidModulusError || OverflowError)!Self` |
| `fromBytes` | `pub fn fromBytes(bytes: []const u8, comptime endian: Endian) (InvalidModulusError || OverflowError)!Self` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(self: Self, fe: Fe) error` |
| `add` | `pub fn add(self: Self, x: Fe, y: Fe) Fe` |
| `sub` | `pub fn sub(self: Self, x: Fe, y: Fe) Fe` |
| `toMontgomery` | `pub fn toMontgomery(self: Self, x: *Fe) RepresentationError!void` |
| `fromMontgomery` | `pub fn fromMontgomery(self: Self, x: *Fe) RepresentationError!void` |
| `reduce` | `pub fn reduce(self: Self, x: anytype) Fe` |
| `mul` | `pub fn mul(self: Self, x: Fe, y: Fe) Fe` |
| `sq` | `pub fn sq(self: Self, x: Fe) Fe` |
| `pow` | `pub fn pow(self: Self, x: Fe, e: Fe) (NullExponentError || RepresentationError)!Fe` |
| `powPublic` | `pub fn powPublic(self: Self, x: Fe, e: Fe) (NullExponentError || RepresentationError)!Fe` |
| `powWithEncodedExponent` | `pub fn powWithEncodedExponent(self: Self, x: Fe, e: []const u8, endian: Endian) NullExponentError!Fe` |
| `powWithEncodedPublicExponent` | `pub fn powWithEncodedPublicExponent(self: Self, x: Fe, e: []const u8, endian: Endian) NullExponentError!Fe` |

## crypto / ghash_polyval

| Function | Signature |
|----------|-----------|
| `initForBlockCount` | `pub fn initForBlockCount(key: *const [key_length]u8, block_count: usize) Self` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(st: *Self, m: []const u8) void` |
| `pad` | `pub fn pad(st: *Self) void` |
| `final` | `pub fn final(st: *Self, out: *[mac_length]u8) void` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |

## crypto / hash_composition

| Function | Signature |
|----------|-----------|
| `Composition` | `pub fn Composition(comptime H1: type, comptime H2: type) type` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |

## crypto / hkdf

| Function | Signature |
|----------|-----------|
| `Hkdf` | `pub fn Hkdf(comptime Hmac: type) type` |
| `extract` | `pub fn extract(salt: []const u8, ikm: []const u8) [prk_length]u8` |
| `extractInit` | `pub fn extractInit(salt: []const u8) Hmac` |
| `expand` | `pub fn expand(out: []u8, ctx: []const u8, prk: [prk_length]u8) void` |

## crypto / hmac

| Function | Signature |
|----------|-----------|
| `Hmac` | `pub fn Hmac(comptime Hash: type) type` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: []const u8) void` |
| `init` | `pub fn init(key: []const u8) Self` |
| `update` | `pub fn update(ctx: *Self, msg: []const u8) void` |
| `final` | `pub fn final(ctx: *Self, out: *[mac_length]u8) void` |

## crypto / hybrid_kem

| Function | Signature |
|----------|-----------|
| `HybridKem` | `pub fn HybridKem(comptime params: Params) type` |
| `toBytes` | `pub fn toBytes(self: PublicKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(buf: *const [encoded_length]u8) PublicKey` |
| `encaps` | `pub fn encaps(pk: PublicKey, io: std.Io) !EncapsulatedSecret` |
| `encapsDeterministic` | `pub fn encapsDeterministic(pk: PublicKey, seed: []const u8) !EncapsulatedSecret` |
| `toBytes` | `pub fn toBytes(self: SecretKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(buf: *const [encoded_length]u8) SecretKey` |
| `decaps` | `pub fn decaps(self: SecretKey, ct: *const [params.Nct]u8) ![params.Nss]u8` |
| `generateDeterministic` | `pub fn generateDeterministic(seed: [params.Nseed]u8) !KeyPair` |
| `generate` | `pub fn generate(io: std.Io) !KeyPair` |
| `randomScalar` | `pub fn randomScalar(seed: []const u8) ![scalar_length]u8` |
| `mul` | `pub fn mul(p: Curve, scalar: [scalar_length]u8) !Curve` |
| `mulBase` | `pub fn mulBase(scalar: [scalar_length]u8) !Curve` |
| `elementToSharedSecret` | `pub fn elementToSharedSecret(p: Curve) [scalar_length]u8` |
| `encodePoint` | `pub fn encodePoint(p: Curve) [element_length]u8` |
| `decodePoint` | `pub fn decodePoint(bytes: *const [element_length]u8) !Curve` |
| `mulBase` | `pub fn mulBase(scalar: [scalar_length]u8) ![element_length]u8` |
| `mul` | `pub fn mul(point: [element_length]u8, scalar: [scalar_length]u8) ![scalar_length]u8` |
| `elementToSharedSecret` | `pub fn elementToSharedSecret(ss: [scalar_length]u8) [scalar_length]u8` |
| `encodePoint` | `pub fn encodePoint(p: [element_length]u8) [element_length]u8` |
| `decodePoint` | `pub fn decodePoint(bytes: *const [element_length]u8) [element_length]u8` |

## crypto / isap

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / kangarootwelve

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `update` | `pub fn update(self: *Self, data: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: []u8) void` |
| `hash` | `pub fn hash(message: []const u8, out: []u8, options: Options) !void` |
| `hashParallel` | `pub fn hashParallel(message: []const u8, out: []u8, options: Options, allocator: Allocator, io: Io) !void` |

## crypto / keccak_p

| Function | Signature |
|----------|-----------|
| `KeccakF` | `pub fn KeccakF(comptime f: u11) type` |
| `init` | `pub fn init(bytes: [block_bytes]u8) Self` |
| `asBytes` | `pub fn asBytes(self: *Self) *[block_bytes]u8` |
| `endianSwap` | `pub fn endianSwap(self: *Self) void` |
| `setBytes` | `pub fn setBytes(self: *Self, bytes: []const u8) void` |
| `addByte` | `pub fn addByte(self: *Self, byte: u8, offset: usize) void` |
| `addBytes` | `pub fn addBytes(self: *Self, bytes: []const u8) void` |
| `extractBytes` | `pub fn extractBytes(self: *Self, out: []u8) void` |
| `xorBytes` | `pub fn xorBytes(self: *Self, out: []u8, in: []const u8) void` |
| `clear` | `pub fn clear(self: *Self, from: usize, to: usize) void` |
| `secureZero` | `pub fn secureZero(self: *Self) void` |
| `permuteR` | `pub fn permuteR(self: *Self, comptime rounds: u5) void` |
| `permute` | `pub fn permute(self: *Self) void` |
| `State` | `pub fn State(comptime f: u11, comptime capacity: u11, comptime rounds: u5) type` |
| `absorb` | `pub fn absorb(self: *Self, bytes: []const u8) void` |
| `init` | `pub fn init(bytes: [f / 8]u8, delim: u8) Self` |
| `fillBlock` | `pub fn fillBlock(self: *Self) void` |
| `pad` | `pub fn pad(self: *Self) void` |
| `squeeze` | `pub fn squeeze(self: *Self, out: []u8) void` |

## crypto / md5

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(data: []const u8, out: *[digest_length]u8, options: Options) void` |
| `hashResult` | `pub fn hashResult(data: []const u8) [digest_length]u8` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |

## crypto / ml_dsa

| Function | Signature |
|----------|-----------|
| `toBytes` | `pub fn toBytes(self: PublicKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) !PublicKey` |
| `toBytes` | `pub fn toBytes(self: SecretKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) !SecretKey` |
| `public` | `pub fn public(self: *const SecretKey) PublicKey` |
| `signer` | `pub fn signer(self: *const SecretKey, noise: ?[noise_length]u8) !Signer` |
| `signerWithContext` | `pub fn signerWithContext(self: *const SecretKey, noise: ?[noise_length]u8, context: []const u8) ContextTooLongError!Signer` |
| `newKeyFromSeed` | `pub fn newKeyFromSeed(seed: *const [seed_length]u8) struct` |
| `toBytes` | `pub fn toBytes(self: Signature) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) EncodingError!Signature` |
| `verify` | `pub fn verify(sig: Signature, msg: []const u8, public_key: PublicKey,) VerifyError!void` |
| `verifyWithContext` | `pub fn verifyWithContext(sig: Signature, msg: []const u8, public_key: PublicKey, context: []const u8,) VerifyError!void` |
| `verifier` | `pub fn verifier(self: Signature, public_key: PublicKey) !Verifier` |
| `verifierWithContext` | `pub fn verifierWithContext(self: Signature, public_key: PublicKey, context: []const u8) ContextTooLongError!Verifier` |
| `init` | `pub fn init(secret_key: *const SecretKey, noise: ?[noise_length]u8, context: []const u8) ContextTooLongError!Signer` |
| `update` | `pub fn update(self: *Signer, data: []const u8) void` |
| `finalize` | `pub fn finalize(self: *Signer) Signature` |
| `init` | `pub fn init(signature: Signature, public_key: PublicKey, context: []const u8) ContextTooLongError!Verifier` |
| `update` | `pub fn update(self: *Verifier, data: []const u8) void` |
| `verify` | `pub fn verify(self: *Verifier) SignatureVerificationError!void` |
| `generate` | `pub fn generate(io: std.Io) KeyPair` |
| `generateDeterministic` | `pub fn generateDeterministic(seed: [32]u8) !KeyPair` |
| `fromSecretKey` | `pub fn fromSecretKey(sk: SecretKey) !KeyPair` |
| `signer` | `pub fn signer(self: *const KeyPair, noise: ?[noise_length]u8) !Signer` |
| `signerWithContext` | `pub fn signerWithContext(self: *const KeyPair, noise: ?[noise_length]u8, context: []const u8) ContextTooLongError!Signer` |
| `sign` | `pub fn sign(kp: KeyPair, msg: []const u8, noise: ?[noise_length]u8,) !Signature` |
| `signWithContext` | `pub fn signWithContext(kp: KeyPair, msg: []const u8, noise: ?[noise_length]u8, context: []const u8,) ContextTooLongError!Signature` |

## crypto / ml_kem

| Function | Signature |
|----------|-----------|
| `encaps` | `pub fn encaps(pk: PublicKey, io: std.Io) EncapsulatedSecret` |
| `encapsDeterministic` | `pub fn encapsDeterministic(pk: PublicKey, seed: *const [encaps_seed_length]u8) EncapsulatedSecret` |
| `toBytes` | `pub fn toBytes(pk: PublicKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(buf: *const [encoded_length]u8) errors.NonCanonicalError!PublicKey` |
| `decaps` | `pub fn decaps(sk: SecretKey, ct: *const [ciphertext_length]u8) ![shared_length]u8` |
| `toBytes` | `pub fn toBytes(sk: SecretKey) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(buf: *const [encoded_length]u8) errors.NonCanonicalError!SecretKey` |
| `generateDeterministic` | `pub fn generateDeterministic(seed: [seed_length]u8) !KeyPair` |
| `generate` | `pub fn generate(io: std.Io) KeyPair` |

## crypto / modes

| Function | Signature |
|----------|-----------|
| `ctr` | `pub fn ctr(comptime BlockCipher: anytype, block_cipher: BlockCipher, dst: []u8, src: []const u8, iv: [BlockCipher.block_length]u8, endian: std.builtin.Endian) void` |
| `ctrSlice` | `pub fn ctrSlice(comptime BlockCipher: anytype, block_cipher: BlockCipher, dst: []u8, src: []const u8, iv: [BlockCipher.block_length]u8, endian: std.builtin.Endian, comptime counter_offset: usize, comptime counter_size: usize,) void` |

## crypto / pbkdf2

| Function | Signature |
|----------|-----------|
| `pbkdf2` | `pub fn pbkdf2(dk: []u8, password: []const u8, salt: []const u8, rounds: u32, comptime Prf: type) (WeakParametersError || OutputTooLongError)!void` |

## crypto / phc_encoding

| Function | Signature |
|----------|-----------|
| `BinValue` | `pub fn BinValue(comptime max_len: usize) type` |
| `fromSlice` | `pub fn fromSlice(slice: []const u8) Error!Self` |
| `constSlice` | `pub fn constSlice(self: *const Self) []const u8` |
| `deserialize` | `pub fn deserialize(comptime HashResult: type, str: []const u8) Error!HashResult` |
| `serialize` | `pub fn serialize(params: anytype, str: []u8) Error![]const u8` |
| `calcSize` | `pub fn calcSize(params: anytype) usize` |

## crypto / poly1305

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(key: *const [key_length]u8) Poly1305` |
| `update` | `pub fn update(st: *Poly1305, m: []const u8) void` |
| `pad` | `pub fn pad(st: *Poly1305) void` |
| `final` | `pub fn final(st: *Poly1305, out: *[mac_length]u8) void` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |

## crypto / salsa20

| Function | Signature |
|----------|-----------|
| `Salsa` | `pub fn Salsa(comptime rounds: comptime_int) type` |
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u64, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `XSalsa` | `pub fn XSalsa(comptime rounds: comptime_int) type` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `seal` | `pub fn seal(c: []u8, m: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `open` | `pub fn open(m: []u8, c: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `createSharedSecret` | `pub fn createSharedSecret(public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError)![shared_length]u8` |
| `seal` | `pub fn seal(c: []u8, m: []const u8, npub: [nonce_length]u8, public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError)!void` |
| `open` | `pub fn open(m: []u8, c: []const u8, npub: [nonce_length]u8, public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError || AuthenticationError)!void` |
| `seal` | `pub fn seal(io: std.Io, c: []u8, m: []const u8, public_key: [public_length]u8) (WeakPublicKeyError || IdentityElementError)!void` |
| `open` | `pub fn open(m: []u8, c: []const u8, keypair: KeyPair) (IdentityElementError || WeakPublicKeyError || AuthenticationError)!void` |

## crypto / scrypt

| Function | Signature |
|----------|-----------|
| `fromLimits` | `pub fn fromLimits(ops_limit: u64, mem_limit: usize) Self` |
| `kdf` | `pub fn kdf(allocator: mem.Allocator, derived_key: []u8, password: []const u8, salt: []const u8, params: Params,) KdfError!void` |
| `HashResult` | `pub fn HashResult(comptime crypt_max_hash_len: usize) type` |
| `BinValue` | `pub fn BinValue(comptime max_len: usize) type` |
| `fromSlice` | `pub fn fromSlice(slice: []const u8) EncodingError!Self` |
| `constSlice` | `pub fn constSlice(self: *const Self) []const u8` |
| `saltFromBin` | `pub fn saltFromBin(comptime len: usize, salt: [len]u8) [Codec.encodedLen(len)]u8` |
| `deserialize` | `pub fn deserialize(comptime T: type, str: []const u8) EncodingError!T` |
| `serialize` | `pub fn serialize(params: anytype, str: []u8) EncodingError![]const u8` |
| `calcSize` | `pub fn calcSize(params: anytype) usize` |
| `create` | `pub fn create(allocator: mem.Allocator, password: []const u8, params: Params, buf: []u8, io: std.Io,) HasherError![]const u8` |
| `createWithSalt` | `pub fn createWithSalt(allocator: mem.Allocator, password: []const u8, params: Params, buf: []u8, salt: *const [default_salt_len]u8,) HasherError![]const u8` |
| `verify` | `pub fn verify(allocator: mem.Allocator, str: []const u8, password: []const u8,) HasherError!void` |
| `createWithSalt` | `pub fn createWithSalt(allocator: mem.Allocator, password: []const u8, params: Params, buf: []u8, salt_bin: *const [default_salt_len]u8,) HasherError![]const u8` |
| `strHash` | `pub fn strHash(password: []const u8, options: HashOptions, out: []u8, io: std.Io,) Error![]const u8` |
| `strHashWithSalt` | `pub fn strHashWithSalt(password: []const u8, options: HashOptions, out: []u8, salt: *const [default_salt_len]u8,) Error![]const u8` |
| `strVerify` | `pub fn strVerify(str: []const u8, password: []const u8, options: VerifyOptions,) Error!void` |

## crypto / sha2

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `peek` | `pub fn peek(d: Self) [digest_length]u8` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `finalResult` | `pub fn finalResult(d: *Self) [digest_length]u8` |

## crypto / sha3

| Function | Signature |
|----------|-----------|
| `TurboShake128` | `pub fn TurboShake128(delim: ?u7) type` |
| `TurboShake256` | `pub fn TurboShake256(comptime delim: ?u7) type` |
| `Keccak` | `pub fn Keccak(comptime f: u11, comptime output_bits: u11, comptime default_delim: u8, comptime rounds: u5) type` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(bytes: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(self: *Self, bytes: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[digest_length]u8) void` |
| `Shake` | `pub fn Shake(comptime security_level: u11) type` |
| `TurboShake` | `pub fn TurboShake(comptime security_level: u11, comptime delim: ?u7) type` |
| `hash` | `pub fn hash(bytes: []const u8, out: []u8, options: Options) void` |
| `squeeze` | `pub fn squeeze(self: *Self, out_: []u8) void` |
| `final` | `pub fn final(self: *Self, out: []u8) void` |
| `fillBlock` | `pub fn fillBlock(self: *Self) void` |
| `CShake` | `pub fn CShake(comptime security_level: u11, comptime fname: ?[]const u8) type` |
| `squeeze` | `pub fn squeeze(self: *Self, out: []u8) void` |
| `KMac` | `pub fn KMac(comptime security_level: u11) type` |
| `initWithOptions` | `pub fn initWithOptions(key: []const u8, options: Options) Self` |
| `init` | `pub fn init(key: []const u8) Self` |
| `update` | `pub fn update(self: *Self, b: []const u8) void` |
| `createWithOptions` | `pub fn createWithOptions(out: []u8, msg: []const u8, key: []const u8, options: Options) void` |
| `create` | `pub fn create(out: []u8, msg: []const u8, key: []const u8) void` |
| `TupleHash` | `pub fn TupleHash(comptime security_level: u11) type` |
| `initWithOptions` | `pub fn initWithOptions(options: Options) Self` |
| `init` | `pub fn init() Self` |
| `slice` | `pub fn slice(self: *const Length) []const u8` |
| `encode` | `pub fn encode(comptime encoding: NistLengthEncoding, len: usize) Length` |

## crypto / siphash

| Function | Signature |
|----------|-----------|
| `SipHash64` | `pub fn SipHash64(comptime c_rounds: usize, comptime d_rounds: usize) type` |
| `SipHash128` | `pub fn SipHash128(comptime c_rounds: usize, comptime d_rounds: usize) type` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(self: *Self, b: []const u8) void` |
| `peek` | `pub fn peek(self: Self) [mac_length]u8` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |
| `finalResult` | `pub fn finalResult(self: *Self) [mac_length]u8` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |
| `finalInt` | `pub fn finalInt(self: *Self) T` |
| `toInt` | `pub fn toInt(msg: []const u8, key: *const [key_length]u8) T` |

## crypto / timing_safe

| Function | Signature |
|----------|-----------|
| `eql` | `pub fn eql(comptime T: type, a: T, b: T) bool` |
| `compare` | `pub fn compare(comptime T: type, a: []const T, b: []const T, endian: Endian) Order` |
| `add` | `pub fn add(comptime T: type, a: []const T, b: []const T, result: []T, endian: Endian) bool` |
| `sub` | `pub fn sub(comptime T: type, a: []const T, b: []const T, result: []T, endian: Endian) bool` |
| `classify` | `pub fn classify(ptr: anytype) void` |
| `declassify` | `pub fn declassify(ptr: anytype) void` |

## crypto / tls

| Function | Signature |
|----------|-----------|
| `toError` | `pub fn toError(description: Description) Error!void` |
| `with` | `pub fn with(cipher_suite: CipherSuite) With` |
| `HandshakeCipherT` | `pub fn HandshakeCipherT(comptime AeadType: type, comptime HashType: type, comptime explicit_iv_length: comptime_int) type` |
| `ApplicationCipherT` | `pub fn ApplicationCipherT(comptime AeadType: type, comptime HashType: type, comptime explicit_iv_length: comptime_int) type` |
| `hmacExpandLabel` | `pub fn hmacExpandLabel(comptime Hmac: type, secret: []const u8, label_then_seed: []const []const u8, comptime len: usize,) [len]u8` |
| `hkdfExpandLabel` | `pub fn hkdfExpandLabel(comptime Hkdf: type, key: [Hkdf.prk_length]u8, label: []const u8, context: []const u8, comptime len: usize,) [len]u8` |
| `emptyHash` | `pub fn emptyHash(comptime Hash: type) [Hash.digest_length]u8` |
| `hmac` | `pub fn hmac(comptime Hmac: type, message: []const u8, key: [Hmac.key_length]u8) [Hmac.mac_length]u8` |
| `extension` | `pub fn extension(et: ExtensionType, bytes: anytype) [2 + 2 + bytes.len]u8` |
| `array` | `pub fn array(comptime Len: type, comptime Elem: type, elems: anytype,) [@divExact(@bitSizeOf(Len), 8) + @divExact(@bitSizeOf(Elem), 8) * elems.len]u8` |
| `int` | `pub fn int(comptime Int: type, val: Int) [@divExact(@bitSizeOf(Int), 8)]u8` |
| `fromTheirSlice` | `pub fn fromTheirSlice(buf: []u8) Decoder` |
| `readAtLeast` | `pub fn readAtLeast(d: *Decoder, stream: *std.Io.Reader, their_amt: usize) !void` |
| `readAtLeastOurAmt` | `pub fn readAtLeastOurAmt(d: *Decoder, stream: *std.Io.Reader, our_amt: usize) !void` |
| `ensure` | `pub fn ensure(d: *Decoder, amt: usize) !void` |
| `decode` | `pub fn decode(d: *Decoder, comptime T: type) T` |
| `array` | `pub fn array(d: *Decoder, comptime len: usize) *[len]u8` |
| `slice` | `pub fn slice(d: *Decoder, len: usize) []u8` |
| `skip` | `pub fn skip(d: *Decoder, amt: usize) void` |
| `eof` | `pub fn eof(d: Decoder) bool` |
| `sub` | `pub fn sub(d: *Decoder, their_len: usize) !Decoder` |
| `rest` | `pub fn rest(d: Decoder) []u8` |

## crypto / pcurves / common

| Function | Signature |
|----------|-----------|
| `Field` | `pub fn Field(comptime params: FieldParams) type` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s_: [encoded_length]u8, endian: std.builtin.Endian) NonCanonicalError!void` |
| `orderSwap` | `pub fn orderSwap(s: [encoded_length]u8) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(s_: [encoded_length]u8, endian: std.builtin.Endian) NonCanonicalError!Fe` |
| `toBytes` | `pub fn toBytes(fe: Fe, endian: std.builtin.Endian) [encoded_length]u8` |
| `fromInt` | `pub fn fromInt(comptime x: IntRepr) NonCanonicalError!Fe` |
| `toInt` | `pub fn toInt(fe: Fe) IntRepr` |
| `isZero` | `pub fn isZero(fe: Fe) bool` |
| `equivalent` | `pub fn equivalent(a: Fe, b: Fe) bool` |
| `isOdd` | `pub fn isOdd(fe: Fe) bool` |
| `cMov` | `pub fn cMov(fe: *Fe, a: Fe, c: u1) void` |
| `add` | `pub fn add(a: Fe, b: Fe) Fe` |
| `sub` | `pub fn sub(a: Fe, b: Fe) Fe` |
| `dbl` | `pub fn dbl(a: Fe) Fe` |
| `mul` | `pub fn mul(a: Fe, b: Fe) Fe` |
| `sq` | `pub fn sq(a: Fe) Fe` |
| `pow` | `pub fn pow(a: Fe, comptime T: type, comptime n: T) Fe` |
| `neg` | `pub fn neg(a: Fe) Fe` |
| `invert` | `pub fn invert(a: Fe) Fe` |
| `isSquare` | `pub fn isSquare(x2: Fe) bool` |
| `sqrt` | `pub fn sqrt(x2: Fe) NotSquareError!Fe` |

## crypto / pcurves / p256

| Function | Signature |
|----------|-----------|
| `rejectIdentity` | `pub fn rejectIdentity(p: P256) IdentityElementError!void` |
| `fromAffineCoordinates` | `pub fn fromAffineCoordinates(p: AffineCoordinates) EncodingError!P256` |
| `fromSerializedAffineCoordinates` | `pub fn fromSerializedAffineCoordinates(xs: [32]u8, ys: [32]u8, endian: std.builtin.Endian) (NonCanonicalError || EncodingError)!P256` |
| `recoverY` | `pub fn recoverY(x: Fe, is_odd: bool) NotSquareError!Fe` |
| `fromSec1` | `pub fn fromSec1(s: []const u8) (EncodingError || NotSquareError || NonCanonicalError)!P256` |
| `toCompressedSec1` | `pub fn toCompressedSec1(p: P256) [33]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(p: P256) [65]u8` |
| `random` | `pub fn random(io: std.Io) P256` |
| `neg` | `pub fn neg(p: P256) P256` |
| `dbl` | `pub fn dbl(p: P256) P256` |
| `addMixed` | `pub fn addMixed(p: P256, q: AffineCoordinates) P256` |
| `add` | `pub fn add(p: P256, q: P256) P256` |
| `sub` | `pub fn sub(p: P256, q: P256) P256` |
| `subMixed` | `pub fn subMixed(p: P256, q: AffineCoordinates) P256` |
| `affineCoordinates` | `pub fn affineCoordinates(p: P256) AffineCoordinates` |
| `equivalent` | `pub fn equivalent(a: P256, b: P256) bool` |
| `mul` | `pub fn mul(p: P256, s_: [32]u8, endian: std.builtin.Endian) IdentityElementError!P256` |
| `mulPublic` | `pub fn mulPublic(p: P256, s_: [32]u8, endian: std.builtin.Endian) IdentityElementError!P256` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: P256, s1_: [32]u8, p2: P256, s2_: [32]u8, endian: std.builtin.Endian) IdentityElementError!P256` |
| `neg` | `pub fn neg(p: AffineCoordinates) AffineCoordinates` |

## crypto / pcurves / p384

| Function | Signature |
|----------|-----------|
| `rejectIdentity` | `pub fn rejectIdentity(p: P384) IdentityElementError!void` |
| `fromAffineCoordinates` | `pub fn fromAffineCoordinates(p: AffineCoordinates) EncodingError!P384` |
| `fromSerializedAffineCoordinates` | `pub fn fromSerializedAffineCoordinates(xs: [48]u8, ys: [48]u8, endian: std.builtin.Endian) (NonCanonicalError || EncodingError)!P384` |
| `recoverY` | `pub fn recoverY(x: Fe, is_odd: bool) NotSquareError!Fe` |
| `fromSec1` | `pub fn fromSec1(s: []const u8) (EncodingError || NotSquareError || NonCanonicalError)!P384` |
| `toCompressedSec1` | `pub fn toCompressedSec1(p: P384) [49]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(p: P384) [97]u8` |
| `random` | `pub fn random(io: std.Io) P384` |
| `neg` | `pub fn neg(p: P384) P384` |
| `dbl` | `pub fn dbl(p: P384) P384` |
| `addMixed` | `pub fn addMixed(p: P384, q: AffineCoordinates) P384` |
| `add` | `pub fn add(p: P384, q: P384) P384` |
| `sub` | `pub fn sub(p: P384, q: P384) P384` |
| `subMixed` | `pub fn subMixed(p: P384, q: AffineCoordinates) P384` |
| `affineCoordinates` | `pub fn affineCoordinates(p: P384) AffineCoordinates` |
| `equivalent` | `pub fn equivalent(a: P384, b: P384) bool` |
| `mul` | `pub fn mul(p: P384, s_: [48]u8, endian: std.builtin.Endian) IdentityElementError!P384` |
| `mulPublic` | `pub fn mulPublic(p: P384, s_: [48]u8, endian: std.builtin.Endian) IdentityElementError!P384` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: P384, s1_: [48]u8, p2: P384, s2_: [48]u8, endian: std.builtin.Endian) IdentityElementError!P384` |
| `neg` | `pub fn neg(p: AffineCoordinates) AffineCoordinates` |

## crypto / pcurves / secp256k1

| Function | Signature |
|----------|-----------|
| `splitScalar` | `pub fn splitScalar(s: [32]u8, endian: std.builtin.Endian) NonCanonicalError!SplitScalar` |
| `rejectIdentity` | `pub fn rejectIdentity(p: Secp256k1) IdentityElementError!void` |
| `fromAffineCoordinates` | `pub fn fromAffineCoordinates(p: AffineCoordinates) EncodingError!Secp256k1` |
| `fromSerializedAffineCoordinates` | `pub fn fromSerializedAffineCoordinates(xs: [32]u8, ys: [32]u8, endian: std.builtin.Endian) (NonCanonicalError || EncodingError)!Secp256k1` |
| `recoverY` | `pub fn recoverY(x: Fe, is_odd: bool) NotSquareError!Fe` |
| `fromSec1` | `pub fn fromSec1(s: []const u8) (EncodingError || NotSquareError || NonCanonicalError)!Secp256k1` |
| `toCompressedSec1` | `pub fn toCompressedSec1(p: Secp256k1) [33]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(p: Secp256k1) [65]u8` |
| `random` | `pub fn random(io: std.Io) Secp256k1` |
| `neg` | `pub fn neg(p: Secp256k1) Secp256k1` |
| `dbl` | `pub fn dbl(p: Secp256k1) Secp256k1` |
| `addMixed` | `pub fn addMixed(p: Secp256k1, q: AffineCoordinates) Secp256k1` |
| `add` | `pub fn add(p: Secp256k1, q: Secp256k1) Secp256k1` |
| `sub` | `pub fn sub(p: Secp256k1, q: Secp256k1) Secp256k1` |
| `subMixed` | `pub fn subMixed(p: Secp256k1, q: AffineCoordinates) Secp256k1` |
| `affineCoordinates` | `pub fn affineCoordinates(p: Secp256k1) AffineCoordinates` |
| `equivalent` | `pub fn equivalent(a: Secp256k1, b: Secp256k1) bool` |
| `mul` | `pub fn mul(p: Secp256k1, s_: [32]u8, endian: std.builtin.Endian) IdentityElementError!Secp256k1` |
| `mulPublic` | `pub fn mulPublic(p: Secp256k1, s_: [32]u8, endian: std.builtin.Endian) (IdentityElementError || NonCanonicalError)!Secp256k1` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: Secp256k1, s1_: [32]u8, p2: Secp256k1, s2_: [32]u8, endian: std.builtin.Endian) IdentityElementError!Secp256k1` |
| `neg` | `pub fn neg(p: AffineCoordinates) AffineCoordinates` |

## crypto / pcurves / p384 / p384_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [6]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[6]u64, arg1: u1, arg2: [6]u64, arg3: [6]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[48]u8, arg1: [6]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[6]u64, arg1: [48]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[7]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[7]u64, out3: *[7]u64, out4: *[6]u64, out5: *[6]u64, arg1: u64, arg2: [7]u64, arg3: [7]u64, arg4: [6]u64, arg5: [6]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[6]u64) void` |

## crypto / pcurves / p384 / p384_scalar_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [6]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[6]u64, arg1: u1, arg2: [6]u64, arg3: [6]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[48]u8, arg1: [6]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[6]u64, arg1: [48]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[7]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[7]u64, out3: *[7]u64, out4: *[6]u64, out5: *[6]u64, arg1: u64, arg2: [7]u64, arg3: [7]u64, arg4: [6]u64, arg5: [6]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[6]u64) void` |

## crypto / pcurves / p384 / scalar

| Function | Signature |
|----------|-----------|
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!void` |
| `reduce64` | `pub fn reduce64(s: [64]u8, endian: std.builtin.Endian) CompressedScalar` |
| `mul` | `pub fn mul(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `mulAdd` | `pub fn mulAdd(a: CompressedScalar, b: CompressedScalar, c: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `add` | `pub fn add(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `neg` | `pub fn neg(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `sub` | `pub fn sub(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `random` | `pub fn random(io: std.Io, endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `isOdd` | `pub fn isOdd(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) bool` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random(io: std.Io) Scalar` |

## crypto / pcurves / secp256k1 / scalar

| Function | Signature |
|----------|-----------|
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!void` |
| `reduce48` | `pub fn reduce48(s: [48]u8, endian: std.builtin.Endian) CompressedScalar` |
| `reduce64` | `pub fn reduce64(s: [64]u8, endian: std.builtin.Endian) CompressedScalar` |
| `mul` | `pub fn mul(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `mulAdd` | `pub fn mulAdd(a: CompressedScalar, b: CompressedScalar, c: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `add` | `pub fn add(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `neg` | `pub fn neg(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `sub` | `pub fn sub(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `random` | `pub fn random(io: std.Io, endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes48` | `pub fn fromBytes48(s: [48]u8, endian: std.builtin.Endian) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `isOdd` | `pub fn isOdd(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) bool` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random(io: std.Io) Scalar` |

## crypto / pcurves / secp256k1 / secp256k1_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [4]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[4]u64, arg1: u1, arg2: [4]u64, arg3: [4]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[32]u8, arg1: [4]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[4]u64, arg1: [32]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[5]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[5]u64, out3: *[5]u64, out4: *[4]u64, out5: *[4]u64, arg1: u64, arg2: [5]u64, arg3: [5]u64, arg4: [4]u64, arg5: [4]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[4]u64) void` |

## crypto / pcurves / secp256k1 / secp256k1_scalar_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [4]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[4]u64, arg1: u1, arg2: [4]u64, arg3: [4]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[32]u8, arg1: [4]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[4]u64, arg1: [32]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[5]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[5]u64, out3: *[5]u64, out4: *[4]u64, out5: *[4]u64, arg1: u64, arg2: [5]u64, arg3: [5]u64, arg4: [4]u64, arg5: [4]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[4]u64) void` |

## crypto / pcurves / p256 / p256_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [4]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[4]u64, arg1: u1, arg2: [4]u64, arg3: [4]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[32]u8, arg1: [4]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[4]u64, arg1: [32]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[5]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[5]u64, out3: *[5]u64, out4: *[4]u64, out5: *[4]u64, arg1: u64, arg2: [5]u64, arg3: [5]u64, arg4: [4]u64, arg5: [4]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[4]u64) void` |

## crypto / pcurves / p256 / p256_scalar_64

| Function | Signature |
|----------|-----------|
| `mul` | `pub fn mul(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `square` | `pub fn square(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `add` | `pub fn add(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `sub` | `pub fn sub(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement, arg2: MontgomeryDomainFieldElement) void` |
| `opp` | `pub fn opp(out1: *MontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `fromMontgomery` | `pub fn fromMontgomery(out1: *NonMontgomeryDomainFieldElement, arg1: MontgomeryDomainFieldElement) void` |
| `toMontgomery` | `pub fn toMontgomery(out1: *MontgomeryDomainFieldElement, arg1: NonMontgomeryDomainFieldElement) void` |
| `nonzero` | `pub fn nonzero(out1: *u64, arg1: [4]u64) void` |
| `selectznz` | `pub fn selectznz(out1: *[4]u64, arg1: u1, arg2: [4]u64, arg3: [4]u64) void` |
| `toBytes` | `pub fn toBytes(out1: *[32]u8, arg1: [4]u64) void` |
| `fromBytes` | `pub fn fromBytes(out1: *[4]u64, arg1: [32]u8) void` |
| `setOne` | `pub fn setOne(out1: *MontgomeryDomainFieldElement) void` |
| `msat` | `pub fn msat(out1: *[5]u64) void` |
| `divstep` | `pub fn divstep(out1: *u64, out2: *[5]u64, out3: *[5]u64, out4: *[4]u64, out5: *[4]u64, arg1: u64, arg2: [5]u64, arg3: [5]u64, arg4: [4]u64, arg5: [4]u64) void` |
| `divstepPrecomp` | `pub fn divstepPrecomp(out1: *[4]u64) void` |

## crypto / pcurves / p256 / scalar

| Function | Signature |
|----------|-----------|
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!void` |
| `reduce48` | `pub fn reduce48(s: [48]u8, endian: std.builtin.Endian) CompressedScalar` |
| `reduce64` | `pub fn reduce64(s: [64]u8, endian: std.builtin.Endian) CompressedScalar` |
| `mul` | `pub fn mul(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `mulAdd` | `pub fn mulAdd(a: CompressedScalar, b: CompressedScalar, c: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `add` | `pub fn add(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `neg` | `pub fn neg(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `sub` | `pub fn sub(a: CompressedScalar, b: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!CompressedScalar` |
| `random` | `pub fn random(io: std.Io, endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes48` | `pub fn fromBytes48(s: [48]u8, endian: std.builtin.Endian) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `isOdd` | `pub fn isOdd(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) bool` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random(io: std.Io) Scalar` |

## crypto / Certificate / Bundle

| Function | Signature |
|----------|-----------|
| `verify` | `pub fn verify(cb: Bundle, subject: Certificate.Parsed, now_sec: i64) VerifyError!void` |
| `find` | `pub fn find(cb: Bundle, subject_name: []const u8) ?u32` |
| `hash` | `pub fn hash(ctx: @This() , k: []const u8) u64` |
| `eql` | `pub fn eql(ctx: @This() , a: []const u8, b_key: der.Element.Slice) bool` |
| `deinit` | `pub fn deinit(cb: *Bundle, gpa: Allocator) void` |
| `rescan` | `pub fn rescan(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp) RescanError!void` |
| `addCertsFromDirPath` | `pub fn addCertsFromDirPath(cb: *Bundle, gpa: Allocator, io: Io, dir: Io.Dir, sub_dir_path: []const u8,) AddCertsFromDirPathError!void` |
| `addCertsFromDirPathAbsolute` | `pub fn addCertsFromDirPathAbsolute(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp, abs_dir_path: []const u8,) AddCertsFromDirPathError!void` |
| `addCertsFromDir` | `pub fn addCertsFromDir(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp, iterable_dir: Io.Dir) AddCertsFromDirError!void` |
| `addCertsFromFilePathAbsolute` | `pub fn addCertsFromFilePathAbsolute(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp, abs_file_path: []const u8,) AddCertsFromFilePathError!void` |
| `addCertsFromFilePath` | `pub fn addCertsFromFilePath(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp, dir: Io.Dir, sub_file_path: []const u8,) AddCertsFromFilePathError!void` |
| `addCertsFromFile` | `pub fn addCertsFromFile(cb: *Bundle, gpa: Allocator, file_reader: *Io.File.Reader, now_sec: i64) AddCertsFromFileError!void` |
| `parseCert` | `pub fn parseCert(cb: *Bundle, gpa: Allocator, decoded_start: u32, now_sec: i64) ParseCertError!void` |
| `hash` | `pub fn hash(ctx: MapContext, k: der.Element.Slice) u64` |
| `eql` | `pub fn eql(ctx: MapContext, a: der.Element.Slice, b: der.Element.Slice) bool` |

## crypto / Certificate / Bundle / macos

| Function | Signature |
|----------|-----------|
| `rescanMac` | `pub fn rescanMac(cb: *Bundle, gpa: Allocator, io: Io, now: Io.Timestamp) RescanMacError!void` |

## crypto / codecs / asn1

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(number: Tag.Number, constructed: bool, class: Tag.Class) Tag` |
| `universal` | `pub fn universal(number: Tag.Number, constructed: bool) Tag` |
| `decode` | `pub fn decode(reader: *std.Io.Reader) !Tag` |
| `encode` | `pub fn encode(self: Tag, writer: *std.Io.Writer) @TypeOf(writer).Error!void` |
| `toExpected` | `pub fn toExpected(self: Tag) ExpectedTag` |
| `fromZig` | `pub fn fromZig(comptime T: type) Tag` |
| `len` | `pub fn len(self: Slice) Index` |
| `view` | `pub fn view(self: Slice, bytes: []const u8) []const u8` |
| `decode` | `pub fn decode(bytes: []const u8, index: Index) DecodeError!Element` |
| `init` | `pub fn init(number: ?Tag.Number, constructed: ?bool, class: ?Tag.Class) ExpectedTag` |
| `primitive` | `pub fn primitive(number: ?Tag.Number) ExpectedTag` |
| `match` | `pub fn match(self: ExpectedTag, tag: Tag) bool` |
| `initExplicit` | `pub fn initExplicit(number: std.meta.Tag(Tag.Number) , class: Tag.Class) FieldTag` |
| `initImplicit` | `pub fn initImplicit(number: std.meta.Tag(Tag.Number) , class: Tag.Class) FieldTag` |
| `fromContainer` | `pub fn fromContainer(comptime Container: type, comptime field_name: []const u8) ?FieldTag` |
| `toTag` | `pub fn toTag(self: FieldTag) Tag` |
| `bitLen` | `pub fn bitLen(self: BitString) usize` |
| `decodeDer` | `pub fn decodeDer(decoder: *der.Decoder) !BitString` |
| `encodeDer` | `pub fn encodeDer(self: BitString, encoder: *der.Encoder) !void` |
| `Opaque` | `pub fn Opaque(comptime tag: Tag) type` |
| `decodeDer` | `pub fn decodeDer(decoder: *der.Decoder) !@This()` |
| `encodeDer` | `pub fn encodeDer(self: @This() , encoder: *der.Encoder) !void` |

## crypto / codecs / base64_hex_ct

| Function | Signature |
|----------|-----------|
| `encode` | `pub fn encode(encoded: []u8, bin: []const u8, comptime case: std.fmt.Case) error` |
| `decode` | `pub fn decode(bin: []u8, encoded: []const u8) error` |
| `decode` | `pub fn decode(self: DecoderWithIgnore, bin: []u8, encoded: []const u8,) error` |
| `decodedLenForSlice` | `pub fn decodedLenForSlice(decoder: DecoderWithIgnore, encoded: []const u8) !usize` |
| `decodedLenUpperBound` | `pub fn decodedLenUpperBound(hex_len: usize) usize` |
| `decoderWithIgnore` | `pub fn decoderWithIgnore(ignore_chars: []const u8) error` |
| `encodedLen` | `pub fn encodedLen(bin_len: usize, variant: Variant) usize` |
| `decodedLen` | `pub fn decodedLen(b64_len: usize, variant: Variant) !usize` |
| `encode` | `pub fn encode(encoded: []u8, bin: []const u8, comptime variant: Variant) error` |
| `decode` | `pub fn decode(bin: []u8, encoded: []const u8, comptime variant: Variant) error` |
| `decode` | `pub fn decode(self: DecoderWithIgnore, bin: []u8, encoded: []const u8, comptime variant: Variant,) error` |
| `decodedLenForSlice` | `pub fn decodedLenForSlice(decoder: DecoderWithIgnore, encoded: []const u8, variant: Variant) !usize` |
| `decodedLenUpperBound` | `pub fn decodedLenUpperBound(b64_len: usize) usize` |

## crypto / codecs / asn1 / Oid

| Function | Signature |
|----------|-----------|
| `fromDot` | `pub fn fromDot(dot_notation: []const u8, out: []u8) InitError!Oid` |
| `toDot` | `pub fn toDot(self: Oid, writer: anytype) @TypeOf(writer).Error!void` |
| `init` | `pub fn init(comptime hex: []const u8, dot_notation: []const u8) TestCase` |
| `decodeDer` | `pub fn decodeDer(decoder: *der.Decoder) !Oid` |
| `encodeDer` | `pub fn encodeDer(self: Oid, encoder: *der.Encoder) !void` |
| `fromDotComptime` | `pub fn fromDotComptime(comptime dot_notation: []const u8) Oid` |
| `StaticMap` | `pub fn StaticMap(comptime Enum: type) type` |
| `oidToEnum` | `pub fn oidToEnum(self: @This() , encoded: []const u8) ?Enum` |
| `enumToOid` | `pub fn enumToOid(self: @This() , value: Enum) Oid` |
| `initComptime` | `pub fn initComptime(comptime key_pairs: anytype) ReturnType` |

## crypto / codecs / asn1 / der

| Function | Signature |
|----------|-----------|
| `decode` | `pub fn decode(comptime T: type, encoded: []const u8) !T` |
| `encode` | `pub fn encode(allocator: std.mem.Allocator, value: anytype) ![]u8` |

## crypto / codecs / asn1 / der / ArrayListReverse

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(allocator: Allocator) ArrayListReverse` |
| `deinit` | `pub fn deinit(self: *ArrayListReverse) void` |
| `ensureCapacity` | `pub fn ensureCapacity(self: *ArrayListReverse, new_capacity: usize) Error!void` |
| `prependSlice` | `pub fn prependSlice(self: *ArrayListReverse, data: []const u8) Error!void` |
| `clearAndFree` | `pub fn clearAndFree(self: *ArrayListReverse) void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *ArrayListReverse) Error![]u8` |

## crypto / codecs / asn1 / der / Decoder

| Function | Signature |
|----------|-----------|
| `any` | `pub fn any(self: *Decoder, comptime T: type) !T` |
| `sequence` | `pub fn sequence(self: *Decoder) !Element` |
| `element` | `pub fn element(self: *Decoder, expected: ExpectedTag,) (error` |
| `view` | `pub fn view(self: Decoder, elem: Element) []const u8` |

## crypto / codecs / asn1 / der / Encoder

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(allocator: std.mem.Allocator) Encoder` |
| `deinit` | `pub fn deinit(self: *Encoder) void` |
| `any` | `pub fn any(self: *Encoder, val: anytype) !void` |
| `tag` | `pub fn tag(self: *Encoder, tag_: Tag) !void` |
| `length` | `pub fn length(self: *Encoder, len: usize) !void` |
| `tagBytes` | `pub fn tagBytes(self: *Encoder, tag_: Tag, bytes: []const u8) !void` |
| `writer` | `pub fn writer(self: *Encoder) ArrayListReverse.Writer` |

## crypto / aes / aesni

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub fn encrypt(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub fn decrypt(block: Block, inv_round_key: Block) Block` |
| `decryptLast` | `pub fn decryptLast(block: Block, inv_round_key: Block) Block` |
| `xorBlocks` | `pub fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub fn orBlocks(block1: Block, block2: Block) Block` |
| `invMixColumns` | `pub fn invMixColumns(block: Block) Block` |
| `encryptParallel` | `pub fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `BlockVec` | `pub fn BlockVec(comptime blocks_count: comptime_int) type` |
| `fromBytes` | `pub fn fromBytes(bytes: *const [blocks_count * 16]u8) Self` |
| `toBytes` | `pub fn toBytes(block_vec: Self) [blocks_count * 16]u8` |
| `xorBytes` | `pub fn xorBytes(block_vec: Self, bytes: *const [blocks_count * 16]u8) [blocks_count * 16]u8` |
| `encrypt` | `pub fn encrypt(block_vec: Self, round_key_vec: Self) Self` |
| `encryptLast` | `pub fn encryptLast(block_vec: Self, round_key_vec: Self) Self` |
| `decrypt` | `pub fn decrypt(block_vec: Self, inv_round_key_vec: Self) Self` |
| `decryptLast` | `pub fn decryptLast(block_vec: Self, inv_round_key_vec: Self) Self` |
| `xorBlocks` | `pub fn xorBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `andBlocks` | `pub fn andBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `orBlocks` | `pub fn orBlocks(block_vec1: Self, block_vec2: Block) Self` |
| `invMixColumns` | `pub fn invMixColumns(block_vec: Self) Self` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes) ) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / aes / armcrypto

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub fn encrypt(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub fn decrypt(block: Block, inv_round_key: Block) Block` |
| `decryptLast` | `pub fn decryptLast(block: Block, inv_round_key: Block) Block` |
| `xorBlocks` | `pub fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub fn orBlocks(block1: Block, block2: Block) Block` |
| `invMixColumns` | `pub fn invMixColumns(block: Block) Block` |
| `encryptParallel` | `pub fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `BlockVec` | `pub fn BlockVec(comptime blocks_count: comptime_int) type` |
| `fromBytes` | `pub fn fromBytes(bytes: *const [blocks_count * 16]u8) Self` |
| `toBytes` | `pub fn toBytes(block_vec: Self) [blocks_count * 16]u8` |
| `xorBytes` | `pub fn xorBytes(block_vec: Self, bytes: *const [blocks_count * 16]u8) [32]u8` |
| `encrypt` | `pub fn encrypt(block_vec: Self, round_key_vec: Self) Self` |
| `encryptLast` | `pub fn encryptLast(block_vec: Self, round_key_vec: Self) Self` |
| `decrypt` | `pub fn decrypt(block_vec: Self, inv_round_key_vec: Self) Self` |
| `decryptLast` | `pub fn decryptLast(block_vec: Self, inv_round_key_vec: Self) Self` |
| `xorBlocks` | `pub fn xorBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `andBlocks` | `pub fn andBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `orBlocks` | `pub fn orBlocks(block_vec1: Self, block_vec2: Block) Self` |
| `invMixColumns` | `pub fn invMixColumns(block_vec: Self) Self` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes) ) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / aes / soft

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub fn encrypt(block: Block, round_key: Block) Block` |
| `encryptUnprotected` | `pub fn encryptUnprotected(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub fn decrypt(block: Block, round_key: Block) Block` |
| `decryptUnprotected` | `pub fn decryptUnprotected(block: Block, round_key: Block) Block` |
| `decryptLast` | `pub fn decryptLast(block: Block, round_key: Block) Block` |
| `xorBlocks` | `pub fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub fn orBlocks(block1: Block, block2: Block) Block` |
| `invMixColumns` | `pub fn invMixColumns(block: Block) Block` |
| `encryptParallel` | `pub fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `BlockVec` | `pub fn BlockVec(comptime blocks_count: comptime_int) type` |
| `fromBytes` | `pub fn fromBytes(bytes: *const [blocks_count * 16]u8) Self` |
| `toBytes` | `pub fn toBytes(block_vec: Self) [blocks_count * 16]u8` |
| `xorBytes` | `pub fn xorBytes(block_vec: Self, bytes: *const [blocks_count * 16]u8) [32]u8` |
| `encrypt` | `pub fn encrypt(block_vec: Self, round_key_vec: Self) Self` |
| `encryptLast` | `pub fn encryptLast(block_vec: Self, round_key_vec: Self) Self` |
| `decrypt` | `pub fn decrypt(block_vec: Self, inv_round_key_vec: Self) Self` |
| `decryptLast` | `pub fn decryptLast(block_vec: Self, inv_round_key_vec: Self) Self` |
| `xorBlocks` | `pub fn xorBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `andBlocks` | `pub fn andBlocks(block_vec1: Self, block_vec2: Self) Self` |
| `orBlocks` | `pub fn orBlocks(block_vec1: Self, block_vec2: Block) Self` |
| `invMixColumns` | `pub fn invMixColumns(block_vec: Self) Self` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes) ) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / tls / Client

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(input: *Reader, output: *Writer, options: Options) InitError!Client` |
| `end` | `pub fn end(c: *Client) Writer.Error!void` |
| `eof` | `pub fn eof(c: Client) bool` |

## crypto / 25519 / curve25519

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub fn fromBytes(s: [32]u8) Curve25519` |
| `toBytes` | `pub fn toBytes(p: Curve25519) [32]u8` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: [32]u8) NonCanonicalError!void` |
| `rejectIdentity` | `pub fn rejectIdentity(p: Curve25519) IdentityElementError!void` |
| `clearCofactor` | `pub fn clearCofactor(p: Curve25519) WeakPublicKeyError!Curve25519` |
| `clampedMul` | `pub fn clampedMul(p: Curve25519, s: [32]u8) IdentityElementError!Curve25519` |
| `mul` | `pub fn mul(p: Curve25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Curve25519` |
| `fromEdwards25519` | `pub fn fromEdwards25519(p: crypto.ecc.Edwards25519) IdentityElementError!Curve25519` |

## crypto / 25519 / ed25519

| Function | Signature |
|----------|-----------|
| `seed` | `pub fn seed(self: SecretKey) [KeyPair.seed_length]u8` |
| `publicKeyBytes` | `pub fn publicKeyBytes(self: SecretKey) [PublicKey.encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) !SecretKey` |
| `toBytes` | `pub fn toBytes(sk: SecretKey) [encoded_length]u8` |
| `update` | `pub fn update(self: *Signer, data: []const u8) void` |
| `finalize` | `pub fn finalize(self: *Signer) Signature` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) NonCanonicalError!PublicKey` |
| `toBytes` | `pub fn toBytes(pk: PublicKey) [encoded_length]u8` |
| `update` | `pub fn update(self: *Verifier, msg: []const u8) void` |
| `verify` | `pub fn verify(self: *Verifier) VerifyError!void` |
| `verifyStrict` | `pub fn verifyStrict(self: *Verifier) VerifyError!void` |
| `toBytes` | `pub fn toBytes(sig: Signature) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) Signature` |
| `verifier` | `pub fn verifier(sig: Signature, public_key: PublicKey) Verifier.InitError!Verifier` |
| `verify` | `pub fn verify(sig: Signature, msg: []const u8, public_key: PublicKey) VerifyError!void` |
| `verifyStrict` | `pub fn verifyStrict(sig: Signature, msg: []const u8, public_key: PublicKey) VerifyError!void` |
| `generateDeterministic` | `pub fn generateDeterministic(seed: [seed_length]u8) IdentityElementError!KeyPair` |
| `generate` | `pub fn generate(io: std.Io) KeyPair` |
| `fromSecretKey` | `pub fn fromSecretKey(secret_key: SecretKey) (NonCanonicalError || EncodingError || IdentityElementError)!KeyPair` |
| `sign` | `pub fn sign(key_pair: KeyPair, msg: []const u8, noise: ?[noise_length]u8) (IdentityElementError || NonCanonicalError || KeyMismatchError || WeakPublicKeyError)!Signature` |
| `signerWithBaseNonce` | `pub fn signerWithBaseNonce(key_pair: KeyPair, base_nonce: [32]u8, /// If set, should be something unique for each message, such as a counter. noise: ?[noise_length]u8,) (IdentityElementError || KeyMismatchError || NonCanonicalError || WeakPublicKe...` |
| `signer` | `pub fn signer(key_pair: KeyPair, /// If set, should be something unique for each message, such as a /// random nonce, or a counter. noise: ?[noise_length]u8, io: std.Io,) (IdentityElementError || KeyMismatchError || NonCanonicalError || WeakPublic...` |
| `verifyBatch` | `pub fn verifyBatch(io: std.Io, comptime count: usize, signature_batch: [count]BatchElement) (SignatureVerificationError || IdentityElementError || WeakPublicKeyError || EncodingError || NonCanonicalError)!void` |
| `unblind` | `pub fn unblind(blind_public_key: BlindPublicKey, blind_seed: [blind_seed_length]u8, ctx: []const u8) (IdentityElementError || NonCanonicalError || EncodingError || WeakPublicKeyError)!PublicKey` |
| `init` | `pub fn init(key_pair: Ed25519.KeyPair, blind_seed: [blind_seed_length]u8, ctx: []const u8) (NonCanonicalError || IdentityElementError)!BlindKeyPair` |
| `sign` | `pub fn sign(key_pair: BlindKeyPair, msg: []const u8, noise: ?[noise_length]u8) (IdentityElementError || KeyMismatchError || NonCanonicalError || WeakPublicKeyError)!Signature` |

## crypto / 25519 / edwards25519

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub fn fromBytes(s: [encoded_length]u8) EncodingError!Edwards25519` |
| `toBytes` | `pub fn toBytes(p: Edwards25519) [encoded_length]u8` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: [32]u8) NonCanonicalError!void` |
| `rejectIdentity` | `pub fn rejectIdentity(p: Edwards25519) IdentityElementError!void` |
| `rejectUnexpectedSubgroup` | `pub fn rejectUnexpectedSubgroup(p: Edwards25519) (WeakPublicKeyError || UnexpectedSubgroupError)!void` |
| `clearCofactor` | `pub fn clearCofactor(p: Edwards25519) Edwards25519` |
| `rejectLowOrder` | `pub fn rejectLowOrder(p: Edwards25519) WeakPublicKeyError!void` |
| `neg` | `pub fn neg(p: Edwards25519) Edwards25519` |
| `dbl` | `pub fn dbl(p: Edwards25519) Edwards25519` |
| `add` | `pub fn add(p: Edwards25519, q: Edwards25519) Edwards25519` |
| `sub` | `pub fn sub(p: Edwards25519, q: Edwards25519) Edwards25519` |
| `mul` | `pub fn mul(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `mulPublic` | `pub fn mulPublic(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: Edwards25519, s1: [32]u8, p2: Edwards25519, s2: [32]u8) WeakPublicKeyError!Edwards25519` |
| `mulMulti` | `pub fn mulMulti(comptime count: usize, ps: [count]Edwards25519, ss: [count][32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `clampedMul` | `pub fn clampedMul(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `elligator2` | `pub fn elligator2(r: Fe) struct` |
| `fromHash` | `pub fn fromHash(h: [64]u8) Edwards25519` |
| `fromString` | `pub fn fromString(comptime random_oracle: bool, ctx: []const u8, s: []const u8) Edwards25519` |
| `fromUniform` | `pub fn fromUniform(r: [32]u8) Edwards25519` |

## crypto / 25519 / field

| Function | Signature |
|----------|-----------|
| `isZero` | `pub fn isZero(fe: Fe) bool` |
| `equivalent` | `pub fn equivalent(a: Fe, b: Fe) bool` |
| `fromBytes` | `pub fn fromBytes(s: [32]u8) Fe` |
| `toBytes` | `pub fn toBytes(fe: Fe) [32]u8` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8) Fe` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: [32]u8, comptime ignore_extra_bit: bool) NonCanonicalError!void` |
| `add` | `pub fn add(a: Fe, b: Fe) Fe` |
| `sub` | `pub fn sub(a: Fe, b: Fe) Fe` |
| `neg` | `pub fn neg(a: Fe) Fe` |
| `isNegative` | `pub fn isNegative(a: Fe) bool` |
| `cMov` | `pub fn cMov(fe: *Fe, a: Fe, c: u64) void` |
| `cSwap2` | `pub fn cSwap2(a0: *Fe, b0: *Fe, a1: *Fe, b1: *Fe, c: u64) void` |
| `mul` | `pub fn mul(a: Fe, b: Fe) callconv(bloaty_inline) Fe` |
| `sq` | `pub fn sq(a: Fe) Fe` |
| `sq2` | `pub fn sq2(a: Fe) Fe` |
| `mul32` | `pub fn mul32(a: Fe, comptime n: u32) Fe` |
| `invert` | `pub fn invert(a: Fe) Fe` |
| `pow2523` | `pub fn pow2523(a: Fe) Fe` |
| `abs` | `pub fn abs(a: Fe) Fe` |
| `isSquare` | `pub fn isSquare(a: Fe) bool` |
| `sqrt` | `pub fn sqrt(x2: Fe) NotSquareError!Fe` |

## crypto / 25519 / ristretto255

| Function | Signature |
|----------|-----------|
| `rejectIdentity` | `pub fn rejectIdentity(p: Ristretto255) IdentityElementError!void` |
| `fromBytes` | `pub fn fromBytes(s: [encoded_length]u8) (NonCanonicalError || EncodingError)!Ristretto255` |
| `toBytes` | `pub fn toBytes(e: Ristretto255) [encoded_length]u8` |
| `fromUniform` | `pub fn fromUniform(h: [64]u8) Ristretto255` |
| `dbl` | `pub fn dbl(p: Ristretto255) Ristretto255` |
| `add` | `pub fn add(p: Ristretto255, q: Ristretto255) Ristretto255` |
| `sub` | `pub fn sub(p: Ristretto255, q: Ristretto255) Ristretto255` |
| `mul` | `pub fn mul(p: Ristretto255, s: [encoded_length]u8) (IdentityElementError || WeakPublicKeyError)!Ristretto255` |
| `equivalent` | `pub fn equivalent(p: Ristretto255, q: Ristretto255) bool` |

## crypto / 25519 / scalar

| Function | Signature |
|----------|-----------|
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: CompressedScalar) NonCanonicalError!void` |
| `reduce` | `pub fn reduce(s: CompressedScalar) CompressedScalar` |
| `reduce64` | `pub fn reduce64(s: [64]u8) CompressedScalar` |
| `clamp` | `pub fn clamp(s: *CompressedScalar) void` |
| `mul` | `pub fn mul(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `mulAdd` | `pub fn mulAdd(a: CompressedScalar, b: CompressedScalar, c: CompressedScalar) CompressedScalar` |
| `mul8` | `pub fn mul8(s: CompressedScalar) CompressedScalar` |
| `add` | `pub fn add(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `neg` | `pub fn neg(s: CompressedScalar) CompressedScalar` |
| `sub` | `pub fn sub(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `random` | `pub fn random(io: std.Io) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(bytes: CompressedScalar) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(bytes: [64]u8) Scalar` |
| `toBytes` | `pub fn toBytes(expanded: *const Scalar) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(x: Scalar) Scalar` |
| `invert` | `pub fn invert(x: Scalar) Scalar` |
| `random` | `pub fn random(io: std.Io) Scalar` |

## crypto / 25519 / x25519

| Function | Signature |
|----------|-----------|
| `generateDeterministic` | `pub fn generateDeterministic(seed: [seed_length]u8) IdentityElementError!KeyPair` |
| `generate` | `pub fn generate(io: std.Io) KeyPair` |
| `fromEd25519` | `pub fn fromEd25519(ed25519_key_pair: crypto.sign.Ed25519.KeyPair) (IdentityElementError || EncodingError)!KeyPair` |
| `recoverPublicKey` | `pub fn recoverPublicKey(secret_key: [secret_length]u8) IdentityElementError![public_length]u8` |
| `publicKeyFromEd25519` | `pub fn publicKeyFromEd25519(ed25519_public_key: crypto.sign.Ed25519.PublicKey) (IdentityElementError || EncodingError)![public_length]u8` |
| `scalarmult` | `pub fn scalarmult(secret_key: [secret_length]u8, public_key: [public_length]u8) IdentityElementError![shared_length]u8` |

## valgrind / cachegrind

| Function | Signature |
|----------|-----------|
| `startInstrumentation` | `pub fn startInstrumentation() void` |
| `stopInstrumentation` | `pub fn stopInstrumentation() void` |

## valgrind / callgrind

| Function | Signature |
|----------|-----------|
| `dumpStats` | `pub fn dumpStats() void` |
| `dumpStatsAt` | `pub fn dumpStatsAt(pos_str: [*:0]const u8) void` |
| `zeroStats` | `pub fn zeroStats() void` |
| `toggleCollect` | `pub fn toggleCollect() void` |
| `startInstrumentation` | `pub fn startInstrumentation() void` |
| `stopInstrumentation` | `pub fn stopInstrumentation() void` |

## valgrind / memcheck

| Function | Signature |
|----------|-----------|
| `makeMemNoAccess` | `pub fn makeMemNoAccess(qzz: []const u8) void` |
| `makeMemUndefined` | `pub fn makeMemUndefined(qzz: []const u8) void` |
| `makeMemDefined` | `pub fn makeMemDefined(qzz: []const u8) void` |
| `makeMemDefinedIfAddressable` | `pub fn makeMemDefinedIfAddressable(qzz: []const u8) void` |
| `createBlock` | `pub fn createBlock(qzz: []const u8, desc: [*:0]const u8) usize` |
| `discard` | `pub fn discard(blkindex: usize) bool` |
| `checkMemIsAddressable` | `pub fn checkMemIsAddressable(qzz: []const u8) usize` |
| `checkMemIsDefined` | `pub fn checkMemIsDefined(qzz: []const u8) usize` |
| `doLeakCheck` | `pub fn doLeakCheck() void` |
| `doAddedLeakCheck` | `pub fn doAddedLeakCheck() void` |
| `doChangedLeakCheck` | `pub fn doChangedLeakCheck() void` |
| `doQuickLeakCheck` | `pub fn doQuickLeakCheck() void` |
| `countLeaks` | `pub fn countLeaks() CountResult` |
| `countLeakBlocks` | `pub fn countLeakBlocks() CountResult` |
| `getVbits` | `pub fn getVbits(zza: []u8, zzvbits: []u8) u2` |
| `setVbits` | `pub fn setVbits(zzvbits: []u8, zza: []u8) u2` |
| `disableAddrErrorReportingInRange` | `pub fn disableAddrErrorReportingInRange(qzz: []u8) usize` |
| `enableAddrErrorReportingInRange` | `pub fn enableAddrErrorReportingInRange(qzz: []u8) usize` |

## math / acos

| Function | Signature |
|----------|-----------|
| `acos` | `pub fn acos(x: anytype) @TypeOf(x)` |

## math / acosh

| Function | Signature |
|----------|-----------|
| `acosh` | `pub fn acosh(x: anytype) @TypeOf(x)` |

## math / asin

| Function | Signature |
|----------|-----------|
| `asin` | `pub fn asin(x: anytype) @TypeOf(x)` |

## math / asinh

| Function | Signature |
|----------|-----------|
| `asinh` | `pub fn asinh(x: anytype) @TypeOf(x)` |

## math / atan

| Function | Signature |
|----------|-----------|
| `atan` | `pub fn atan(x: anytype) @TypeOf(x)` |

## math / atan2

| Function | Signature |
|----------|-----------|
| `atan2` | `pub fn atan2(y: anytype, x: anytype) @TypeOf(x, y)` |

## math / atanh

| Function | Signature |
|----------|-----------|
| `atanh` | `pub fn atanh(x: anytype) @TypeOf(x)` |

## math / cbrt

| Function | Signature |
|----------|-----------|
| `cbrt` | `pub fn cbrt(x: anytype) @TypeOf(x)` |

## math / complex

| Function | Signature |
|----------|-----------|
| `Complex` | `pub fn Complex(comptime T: type) type` |
| `init` | `pub fn init(re: T, im: T) Self` |
| `add` | `pub fn add(self: Self, other: Self) Self` |
| `sub` | `pub fn sub(self: Self, other: Self) Self` |
| `mul` | `pub fn mul(self: Self, other: Self) Self` |
| `div` | `pub fn div(self: Self, other: Self) Self` |
| `conjugate` | `pub fn conjugate(self: Self) Self` |
| `neg` | `pub fn neg(self: Self) Self` |
| `mulbyi` | `pub fn mulbyi(self: Self) Self` |
| `reciprocal` | `pub fn reciprocal(self: Self) Self` |
| `magnitude` | `pub fn magnitude(self: Self) T` |
| `squaredMagnitude` | `pub fn squaredMagnitude(self: Self) T` |

## math / copysign

| Function | Signature |
|----------|-----------|
| `copysign` | `pub fn copysign(magnitude: anytype, sign: @TypeOf(magnitude) ) @TypeOf(magnitude)` |

## math / cosh

| Function | Signature |
|----------|-----------|
| `cosh` | `pub fn cosh(x: anytype) @TypeOf(x)` |

## math / expm1

| Function | Signature |
|----------|-----------|
| `expm1` | `pub fn expm1(x: anytype) @TypeOf(x)` |

## math / expo2

| Function | Signature |
|----------|-----------|
| `expo2` | `pub fn expo2(x: anytype) @TypeOf(x)` |

## math / float

| Function | Signature |
|----------|-----------|
| `FloatRepr` | `pub fn FloatRepr(comptime Float: type) type` |
| `unbias` | `pub fn unbias(biased: BiasedExponent) Exponent` |
| `bias` | `pub fn bias(unbiased: Exponent) BiasedExponent` |
| `reconstruct` | `pub fn reconstruct(normalized: Normalized, sign: std.math.Sign) Float` |
| `floatExponentBits` | `pub fn floatExponentBits(comptime T: type) comptime_int` |
| `floatMantissaBits` | `pub fn floatMantissaBits(comptime T: type) comptime_int` |
| `floatFractionalBits` | `pub fn floatFractionalBits(comptime T: type) comptime_int` |
| `floatExponentMin` | `pub fn floatExponentMin(comptime T: type) comptime_int` |
| `floatExponentMax` | `pub fn floatExponentMax(comptime T: type) comptime_int` |
| `floatTrueMin` | `pub fn floatTrueMin(comptime T: type) T` |
| `floatMin` | `pub fn floatMin(comptime T: type) T` |
| `floatMax` | `pub fn floatMax(comptime T: type) T` |
| `floatEps` | `pub fn floatEps(comptime T: type) T` |
| `floatEpsAt` | `pub fn floatEpsAt(comptime T: type, x: T) T` |
| `inf` | `pub fn inf(comptime Type: type) Type` |
| `nan` | `pub fn nan(comptime Type: type) Type` |
| `snan` | `pub fn snan(comptime Type: type) Type` |

## math / frexp

| Function | Signature |
|----------|-----------|
| `Frexp` | `pub fn Frexp(comptime T: type) type` |
| `frexp` | `pub fn frexp(x: anytype) Frexp(@TypeOf(x))` |

## math / gamma

| Function | Signature |
|----------|-----------|
| `gamma` | `pub fn gamma(comptime T: type, x: T) T` |
| `lgamma` | `pub fn lgamma(comptime T: type, x: T) T` |

## math / gcd

| Function | Signature |
|----------|-----------|
| `gcd` | `pub fn gcd(a: anytype, b: anytype) @TypeOf(a, b)` |

## math / hypot

| Function | Signature |
|----------|-----------|
| `hypot` | `pub fn hypot(x: anytype, y: anytype) @TypeOf(x, y)` |

## math / ilogb

| Function | Signature |
|----------|-----------|
| `ilogb` | `pub fn ilogb(x: anytype) i32` |

## math / isfinite

| Function | Signature |
|----------|-----------|
| `isFinite` | `pub fn isFinite(x: anytype) bool` |

## math / isinf

| Function | Signature |
|----------|-----------|
| `isInf` | `pub fn isInf(x: anytype) bool` |
| `isPositiveInf` | `pub fn isPositiveInf(x: anytype) bool` |
| `isNegativeInf` | `pub fn isNegativeInf(x: anytype) bool` |

## math / isnan

| Function | Signature |
|----------|-----------|
| `isNan` | `pub fn isNan(x: anytype) bool` |
| `isSignalNan` | `pub fn isSignalNan(x: anytype) bool` |

## math / isnormal

| Function | Signature |
|----------|-----------|
| `isNormal` | `pub fn isNormal(x: anytype) bool` |

## math / iszero

| Function | Signature |
|----------|-----------|
| `isPositiveZero` | `pub fn isPositiveZero(x: anytype) bool` |
| `isNegativeZero` | `pub fn isNegativeZero(x: anytype) bool` |

## math / lcm

| Function | Signature |
|----------|-----------|
| `lcm` | `pub fn lcm(a: anytype, b: anytype) @TypeOf(a, b)` |

## math / ldexp

| Function | Signature |
|----------|-----------|
| `ldexp` | `pub fn ldexp(x: anytype, n: i32) @TypeOf(x)` |

## math / log

| Function | Signature |
|----------|-----------|
| `log` | `pub fn log(comptime T: type, base: T, x: T) T` |

## math / log10

| Function | Signature |
|----------|-----------|
| `log10` | `pub fn log10(x: anytype) @TypeOf(x)` |
| `log10_int` | `pub fn log10_int(x: anytype) std.math.Log2Int(@TypeOf(x))` |

## math / log1p

| Function | Signature |
|----------|-----------|
| `log1p` | `pub fn log1p(x: anytype) @TypeOf(x)` |

## math / log2

| Function | Signature |
|----------|-----------|
| `log2` | `pub fn log2(x: anytype) @TypeOf(x)` |

## math / log_int

| Function | Signature |
|----------|-----------|
| `log_int` | `pub fn log_int(comptime T: type, base: T, x: T) Log2Int(T)` |

## math / modf

| Function | Signature |
|----------|-----------|
| `Modf` | `pub fn Modf(comptime T: type) type` |
| `modf` | `pub fn modf(x: anytype) Modf(@TypeOf(x))` |

## math / nextafter

| Function | Signature |
|----------|-----------|
| `nextAfter` | `pub fn nextAfter(comptime T: type, x: T, y: T) T` |

## math / pow

| Function | Signature |
|----------|-----------|
| `pow` | `pub fn pow(comptime T: type, x: T, y: T) T` |

## math / powi

| Function | Signature |
|----------|-----------|
| `powi` | `pub fn powi(comptime T: type, x: T, y: T) (error` |

## math / signbit

| Function | Signature |
|----------|-----------|
| `signbit` | `pub fn signbit(x: anytype) bool` |

## math / sinh

| Function | Signature |
|----------|-----------|
| `sinh` | `pub fn sinh(x: anytype) @TypeOf(x)` |

## math / sqrt

| Function | Signature |
|----------|-----------|
| `sqrt` | `pub fn sqrt(x: anytype) Sqrt(@TypeOf(x))` |
| `Sqrt` | `pub fn Sqrt(comptime T: type) type` |

## math / tanh

| Function | Signature |
|----------|-----------|
| `tanh` | `pub fn tanh(x: anytype) @TypeOf(x)` |

## math / complex / abs

| Function | Signature |
|----------|-----------|
| `abs` | `pub fn abs(z: anytype) @TypeOf(z.re, z.im)` |

## math / complex / acos

| Function | Signature |
|----------|-----------|
| `acos` | `pub fn acos(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / acosh

| Function | Signature |
|----------|-----------|
| `acosh` | `pub fn acosh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / arg

| Function | Signature |
|----------|-----------|
| `arg` | `pub fn arg(z: anytype) @TypeOf(z.re, z.im)` |

## math / complex / asin

| Function | Signature |
|----------|-----------|
| `asin` | `pub fn asin(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / asinh

| Function | Signature |
|----------|-----------|
| `asinh` | `pub fn asinh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / atan

| Function | Signature |
|----------|-----------|
| `atan` | `pub fn atan(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / atanh

| Function | Signature |
|----------|-----------|
| `atanh` | `pub fn atanh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / conj

| Function | Signature |
|----------|-----------|
| `conj` | `pub fn conj(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / cos

| Function | Signature |
|----------|-----------|
| `cos` | `pub fn cos(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / cosh

| Function | Signature |
|----------|-----------|
| `cosh` | `pub fn cosh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / exp

| Function | Signature |
|----------|-----------|
| `exp` | `pub fn exp(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / ldexp

| Function | Signature |
|----------|-----------|
| `ldexp_cexp` | `pub fn ldexp_cexp(z: anytype, expt: i32) Complex(@TypeOf(z.re, z.im))` |

## math / complex / log

| Function | Signature |
|----------|-----------|
| `log` | `pub fn log(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / pow

| Function | Signature |
|----------|-----------|
| `pow` | `pub fn pow(z: anytype, s: anytype) Complex(@TypeOf(z.re, z.im, s.re, s.im))` |

## math / complex / proj

| Function | Signature |
|----------|-----------|
| `proj` | `pub fn proj(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / sin

| Function | Signature |
|----------|-----------|
| `sin` | `pub fn sin(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / sinh

| Function | Signature |
|----------|-----------|
| `sinh` | `pub fn sinh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / sqrt

| Function | Signature |
|----------|-----------|
| `sqrt` | `pub fn sqrt(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / tan

| Function | Signature |
|----------|-----------|
| `tan` | `pub fn tan(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / complex / tanh

| Function | Signature |
|----------|-----------|
| `tanh` | `pub fn tanh(z: anytype) Complex(@TypeOf(z.re, z.im))` |

## math / big / int

| Function | Signature |
|----------|-----------|
| `calcLimbLen` | `pub fn calcLimbLen(scalar: anytype) usize` |
| `calcToStringLimbsBufferLen` | `pub fn calcToStringLimbsBufferLen(a_len: usize, base: u8) usize` |
| `calcDivLimbsBufferLen` | `pub fn calcDivLimbsBufferLen(a_len: usize, b_len: usize) usize` |
| `calcMulLimbsBufferLen` | `pub fn calcMulLimbsBufferLen(a_len: usize, b_len: usize, aliases: usize) usize` |
| `calcMulWrapLimbsBufferLen` | `pub fn calcMulWrapLimbsBufferLen(bit_count: usize, a_len: usize, b_len: usize, aliases: usize) usize` |
| `calcSetStringLimbsBufferLen` | `pub fn calcSetStringLimbsBufferLen(base: u8, string_len: usize) usize` |
| `calcSetStringLimbCount` | `pub fn calcSetStringLimbCount(base: u8, string_len: usize) usize` |
| `calcPowLimbsBufferLen` | `pub fn calcPowLimbsBufferLen(a_bit_count: usize, y: usize) usize` |
| `calcSqrtLimbsBufferLen` | `pub fn calcSqrtLimbsBufferLen(a_bit_count: usize) usize` |
| `calcNonZeroTwosCompLimbCount` | `pub fn calcNonZeroTwosCompLimbCount(bit_count: usize) usize` |
| `calcTwosCompLimbCount` | `pub fn calcTwosCompLimbCount(bit_count: usize) usize` |
| `addMulLimbWithCarry` | `pub fn addMulLimbWithCarry(a: Limb, b: Limb, c: Limb, carry: *Limb) Limb` |
| `toConst` | `pub fn toConst(self: Mutable) Const` |
| `toInt` | `pub fn toInt(self: Mutable, comptime Int: type) ConvertError!Int` |
| `toFloat` | `pub fn toFloat(self: Mutable, comptime Float: type, round: Round) struct` |
| `eqlZero` | `pub fn eqlZero(self: Mutable) bool` |
| `toManaged` | `pub fn toManaged(self: Mutable, allocator: Allocator) Managed` |
| `init` | `pub fn init(limbs_buffer: []Limb, value: anytype) Mutable` |
| `copy` | `pub fn copy(self: *Mutable, other: Const) void` |
| `swap` | `pub fn swap(self: *Mutable, other: *Mutable) void` |
| `dump` | `pub fn dump(self: Mutable) void` |
| `clone` | `pub fn clone(other: Mutable, limbs: []Limb) Mutable` |
| `negate` | `pub fn negate(self: *Mutable) void` |
| `abs` | `pub fn abs(self: *Mutable) void` |
| `set` | `pub fn set(self: *Mutable, value: anytype) void` |
| `setString` | `pub fn setString(self: *Mutable, base: u8, value: []const u8,) error` |
| `setTwosCompIntLimit` | `pub fn setTwosCompIntLimit(r: *Mutable, limit: TwosCompIntLimit, signedness: Signedness, bit_count: usize,) void` |
| `setFloat` | `pub fn setFloat(self: *Mutable, value: anytype, round: Round) Exactness` |
| `addScalar` | `pub fn addScalar(r: *Mutable, a: Const, scalar: anytype) void` |
| `add` | `pub fn add(r: *Mutable, a: Const, b: Const) void` |
| `addWrap` | `pub fn addWrap(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) bool` |
| `addSat` | `pub fn addSat(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) void` |
| `sub` | `pub fn sub(r: *Mutable, a: Const, b: Const) void` |
| `subWrap` | `pub fn subWrap(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) bool` |
| `subSat` | `pub fn subSat(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) void` |
| `mul` | `pub fn mul(rma: *Mutable, a: Const, b: Const, limbs_buffer: []Limb, allocator: ?Allocator) void` |
| `mulNoAlias` | `pub fn mulNoAlias(rma: *Mutable, a: Const, b: Const, allocator: ?Allocator) void` |
| `mulWrap` | `pub fn mulWrap(rma: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize, limbs_buffer: []Limb, allocator: ?Allocator,) void` |
| `mulWrapNoAlias` | `pub fn mulWrapNoAlias(rma: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize, allocator: ?Allocator,) void` |
| `bitReverse` | `pub fn bitReverse(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `byteSwap` | `pub fn byteSwap(r: *Mutable, a: Const, signedness: Signedness, byte_count: usize) void` |
| `popCount` | `pub fn popCount(r: *Mutable, a: Const, bit_count: usize) void` |
| `sqrNoAlias` | `pub fn sqrNoAlias(rma: *Mutable, a: Const, opt_allocator: ?Allocator) void` |
| `divFloor` | `pub fn divFloor(q: *Mutable, r: *Mutable, a: Const, b: Const, limbs_buffer: []Limb,) void` |
| `divTrunc` | `pub fn divTrunc(q: *Mutable, r: *Mutable, a: Const, b: Const, limbs_buffer: []Limb,) void` |
| `shiftLeft` | `pub fn shiftLeft(r: *Mutable, a: Const, shift: usize) void` |
| `shiftLeftSat` | `pub fn shiftLeftSat(r: *Mutable, a: Const, shift: usize, signedness: Signedness, bit_count: usize) void` |
| `shiftRight` | `pub fn shiftRight(r: *Mutable, a: Const, shift: usize) void` |
| `bitNotWrap` | `pub fn bitNotWrap(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `bitOr` | `pub fn bitOr(r: *Mutable, a: Const, b: Const) void` |
| `bitAnd` | `pub fn bitAnd(r: *Mutable, a: Const, b: Const) void` |
| `bitXor` | `pub fn bitXor(r: *Mutable, a: Const, b: Const) void` |
| `gcd` | `pub fn gcd(rma: *Mutable, x: Const, y: Const, limbs_buffer: *std.array_list.Managed(Limb) ) !void` |
| `pow` | `pub fn pow(r: *Mutable, a: Const, b: u32, limbs_buffer: []Limb) void` |
| `sqrt` | `pub fn sqrt(r: *Mutable, a: Const, limbs_buffer: []Limb,) void` |
| `gcdNoAlias` | `pub fn gcdNoAlias(rma: *Mutable, x: Const, y: Const, limbs_buffer: *std.array_list.Managed(Limb) ) !void` |
| `truncate` | `pub fn truncate(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `saturate` | `pub fn saturate(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `readTwosComplement` | `pub fn readTwosComplement(x: *Mutable, buffer: []const u8, bit_count: usize, endian: Endian, signedness: Signedness,) void` |
| `readPackedTwosComplement` | `pub fn readPackedTwosComplement(x: *Mutable, buffer: []const u8, bit_offset: usize, bit_count: usize, endian: Endian, signedness: Signedness,) void` |
| `normalize` | `pub fn normalize(r: *Mutable, length: usize) void` |
| `format` | `pub fn format(self: Mutable, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `formatNumber` | `pub fn formatNumber(self: Mutable, w: *std.Io.Writer, n: std.fmt.Number) std.Io.Writer.Error!void` |
| `toManaged` | `pub fn toManaged(self: Const, allocator: Allocator) Allocator.Error!Managed` |
| `toMutable` | `pub fn toMutable(self: Const, limbs: []Limb) Mutable` |
| `dump` | `pub fn dump(self: Const) void` |
| `abs` | `pub fn abs(self: Const) Const` |
| `negate` | `pub fn negate(self: Const) Const` |
| `isOdd` | `pub fn isOdd(self: Const) bool` |
| `isEven` | `pub fn isEven(self: Const) bool` |
| `bitCountAbs` | `pub fn bitCountAbs(self: Const) usize` |
| `bitCountTwosComp` | `pub fn bitCountTwosComp(self: Const) usize` |
| `bitCountTwosCompForSignedness` | `pub fn bitCountTwosCompForSignedness(self: Const, signedness: std.builtin.Signedness) usize` |
| `popCount` | `pub fn popCount(self: Const, bit_count: usize) usize` |
| `fitsInTwosComp` | `pub fn fitsInTwosComp(self: Const, signedness: Signedness, bit_count: usize) bool` |
| `fits` | `pub fn fits(self: Const, comptime T: type) bool` |
| `sizeInBaseUpperBound` | `pub fn sizeInBaseUpperBound(self: Const, base: usize) usize` |
| `toInt` | `pub fn toInt(self: Const, comptime Int: type) ConvertError!Int` |
| `toFloat` | `pub fn toFloat(self: Const, comptime Float: type, round: Round) struct` |
| `format` | `pub fn format(self: Const, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `formatNumber` | `pub fn formatNumber(self: Const, w: *std.Io.Writer, number: std.fmt.Number) std.Io.Writer.Error!void` |
| `toStringAlloc` | `pub fn toStringAlloc(self: Const, allocator: Allocator, base: u8, case: std.fmt.Case) Allocator.Error![]u8` |
| `toString` | `pub fn toString(self: Const, string: []u8, base: u8, case: std.fmt.Case, limbs_buffer: []Limb) usize` |
| `writeTwosComplement` | `pub fn writeTwosComplement(x: Const, buffer: []u8, endian: Endian) void` |
| `writePackedTwosComplement` | `pub fn writePackedTwosComplement(x: Const, buffer: []u8, bit_offset: usize, bit_count: usize, endian: Endian) void` |
| `orderAbs` | `pub fn orderAbs(a: Const, b: Const) math.Order` |
| `order` | `pub fn order(a: Const, b: Const) math.Order` |
| `orderAgainstScalar` | `pub fn orderAgainstScalar(lhs: Const, scalar: anytype) math.Order` |
| `eqlZero` | `pub fn eqlZero(a: Const) bool` |
| `eqlAbs` | `pub fn eqlAbs(a: Const, b: Const) bool` |
| `eql` | `pub fn eql(a: Const, b: Const) bool` |
| `clz` | `pub fn clz(a: Const, bits: Limb) Limb` |
| `ctz` | `pub fn ctz(a: Const, bits: Limb) Limb` |
| `init` | `pub fn init(allocator: Allocator) !Managed` |
| `toMutable` | `pub fn toMutable(self: Managed) Mutable` |
| `toConst` | `pub fn toConst(self: Managed) Const` |
| `initSet` | `pub fn initSet(allocator: Allocator, value: anytype) !Managed` |
| `initCapacity` | `pub fn initCapacity(allocator: Allocator, capacity: usize) !Managed` |
| `len` | `pub fn len(self: Managed) usize` |
| `isPositive` | `pub fn isPositive(self: Managed) bool` |
| `setSign` | `pub fn setSign(self: *Managed, positive: bool) void` |
| `setLen` | `pub fn setLen(self: *Managed, new_len: usize) void` |
| `setMetadata` | `pub fn setMetadata(self: *Managed, positive: bool, length: usize) void` |
| `ensureCapacity` | `pub fn ensureCapacity(self: *Managed, capacity: usize) !void` |
| `deinit` | `pub fn deinit(self: *Managed) void` |
| `clone` | `pub fn clone(other: Managed) !Managed` |
| `cloneWithDifferentAllocator` | `pub fn cloneWithDifferentAllocator(other: Managed, allocator: Allocator) !Managed` |
| `copy` | `pub fn copy(self: *Managed, other: Const) !void` |
| `swap` | `pub fn swap(self: *Managed, other: *Managed) void` |
| `dump` | `pub fn dump(self: Managed) void` |
| `negate` | `pub fn negate(self: *Managed) void` |
| `abs` | `pub fn abs(self: *Managed) void` |
| `isOdd` | `pub fn isOdd(self: Managed) bool` |
| `isEven` | `pub fn isEven(self: Managed) bool` |
| `bitCountAbs` | `pub fn bitCountAbs(self: Managed) usize` |
| `bitCountTwosComp` | `pub fn bitCountTwosComp(self: Managed) usize` |
| `fitsInTwosComp` | `pub fn fitsInTwosComp(self: Managed, signedness: Signedness, bit_count: usize) bool` |
| `fits` | `pub fn fits(self: Managed, comptime T: type) bool` |
| `sizeInBaseUpperBound` | `pub fn sizeInBaseUpperBound(self: Managed, base: usize) usize` |
| `set` | `pub fn set(self: *Managed, value: anytype) Allocator.Error!void` |
| `toInt` | `pub fn toInt(self: Managed, comptime Int: type) ConvertError!Int` |
| `toFloat` | `pub fn toFloat(self: Managed, comptime Float: type, round: Round) struct` |
| `setString` | `pub fn setString(self: *Managed, base: u8, value: []const u8) !void` |
| `setTwosCompIntLimit` | `pub fn setTwosCompIntLimit(r: *Managed, limit: TwosCompIntLimit, signedness: Signedness, bit_count: usize,) !void` |
| `toString` | `pub fn toString(self: Managed, allocator: Allocator, base: u8, case: std.fmt.Case) ![]u8` |
| `format` | `pub fn format(self: Managed, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `formatNumber` | `pub fn formatNumber(self: Managed, w: *std.Io.Writer, n: std.fmt.Number) std.Io.Writer.Error!void` |
| `orderAbs` | `pub fn orderAbs(a: Managed, b: Managed) math.Order` |
| `order` | `pub fn order(a: Managed, b: Managed) math.Order` |
| `eqlZero` | `pub fn eqlZero(a: Managed) bool` |
| `eqlAbs` | `pub fn eqlAbs(a: Managed, b: Managed) bool` |
| `eql` | `pub fn eql(a: Managed, b: Managed) bool` |
| `normalize` | `pub fn normalize(r: *Managed, length: usize) void` |
| `addScalar` | `pub fn addScalar(r: *Managed, a: *const Managed, scalar: anytype) Allocator.Error!void` |
| `add` | `pub fn add(r: *Managed, a: *const Managed, b: *const Managed) Allocator.Error!void` |
| `addWrap` | `pub fn addWrap(r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize,) Allocator.Error!bool` |
| `addSat` | `pub fn addSat(r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize) Allocator.Error!void` |
| `sub` | `pub fn sub(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `subWrap` | `pub fn subWrap(r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize,) Allocator.Error!bool` |
| `subSat` | `pub fn subSat(r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize,) Allocator.Error!void` |
| `mul` | `pub fn mul(rma: *Managed, a: *const Managed, b: *const Managed) !void` |
| `mulWrap` | `pub fn mulWrap(rma: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize,) !void` |
| `ensureTwosCompCapacity` | `pub fn ensureTwosCompCapacity(r: *Managed, bit_count: usize) !void` |
| `ensureAddScalarCapacity` | `pub fn ensureAddScalarCapacity(r: *Managed, a: *const Managed, scalar: anytype) !void` |
| `ensureAddCapacity` | `pub fn ensureAddCapacity(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `ensureMulCapacity` | `pub fn ensureMulCapacity(rma: *Managed, a: *const Managed, b: *const Managed) !void` |
| `divFloor` | `pub fn divFloor(q: *Managed, r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `divTrunc` | `pub fn divTrunc(q: *Managed, r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `shiftLeft` | `pub fn shiftLeft(r: *Managed, a: *const Managed, shift: usize) !void` |
| `shiftLeftSat` | `pub fn shiftLeftSat(r: *Managed, a: *const Managed, shift: usize, signedness: Signedness, bit_count: usize) !void` |
| `shiftRight` | `pub fn shiftRight(r: *Managed, a: *const Managed, shift: usize) !void` |
| `bitNotWrap` | `pub fn bitNotWrap(r: *Managed, a: *const Managed, signedness: Signedness, bit_count: usize) !void` |
| `bitOr` | `pub fn bitOr(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `bitAnd` | `pub fn bitAnd(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `bitXor` | `pub fn bitXor(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `gcd` | `pub fn gcd(rma: *Managed, x: *const Managed, y: *const Managed) !void` |
| `sqr` | `pub fn sqr(rma: *Managed, a: *const Managed) !void` |
| `pow` | `pub fn pow(rma: *Managed, a: *const Managed, b: u32) !void` |
| `sqrt` | `pub fn sqrt(rma: *Managed, a: *const Managed) !void` |
| `truncate` | `pub fn truncate(r: *Managed, a: *const Managed, signedness: Signedness, bit_count: usize) !void` |
| `saturate` | `pub fn saturate(r: *Managed, a: *const Managed, signedness: Signedness, bit_count: usize) !void` |
| `popCount` | `pub fn popCount(r: *Managed, a: *const Managed, bit_count: usize) !void` |
| `llcmp` | `pub fn llcmp(a: []const Limb, b: []const Limb) i8` |

## time / epoch

| Function | Signature |
|----------|-----------|
| `isLeapYear` | `pub fn isLeapYear(year: Year) bool` |
| `getDaysInYear` | `pub fn getDaysInYear(year: Year) u9` |
| `numeric` | `pub fn numeric(self: Month) u4` |
| `getDaysInMonth` | `pub fn getDaysInMonth(year: Year, month: Month) u5` |
| `calculateMonthDay` | `pub fn calculateMonthDay(self: YearAndDay) MonthAndDay` |
| `calculateYearDay` | `pub fn calculateYearDay(self: EpochDay) YearAndDay` |
| `getHoursIntoDay` | `pub fn getHoursIntoDay(self: DaySeconds) u5` |
| `getMinutesIntoHour` | `pub fn getMinutesIntoHour(self: DaySeconds) u6` |
| `getSecondsIntoMinute` | `pub fn getSecondsIntoMinute(self: DaySeconds) u6` |
| `getEpochDay` | `pub fn getEpochDay(self: EpochSeconds) EpochDay` |
| `getDaySeconds` | `pub fn getDaySeconds(self: EpochSeconds) DaySeconds` |

## json / Scanner

| Function | Signature |
|----------|-----------|
| `initStreaming` | `pub fn initStreaming(allocator: Allocator) @This()` |
| `initCompleteInput` | `pub fn initCompleteInput(allocator: Allocator, complete_input: []const u8) @This()` |
| `deinit` | `pub fn deinit(self: *@This() ) void` |
| `enableDiagnostics` | `pub fn enableDiagnostics(self: *@This() , diagnostics: *Diagnostics) void` |
| `feedInput` | `pub fn feedInput(self: *@This() , input: []const u8) void` |
| `endInput` | `pub fn endInput(self: *@This() ) void` |
| `nextAlloc` | `pub fn nextAlloc(self: *@This() , allocator: Allocator, when: AllocWhen) AllocError!Token` |
| `nextAllocMax` | `pub fn nextAllocMax(self: *@This() , allocator: Allocator, when: AllocWhen, max_value_len: usize) AllocError!Token` |
| `allocNextIntoArrayList` | `pub fn allocNextIntoArrayList(self: *@This() , value_list: *std.array_list.Managed(u8), when: AllocWhen) AllocIntoArrayListError!?[]const u8` |
| `allocNextIntoArrayListMax` | `pub fn allocNextIntoArrayListMax(self: *@This() , value_list: *std.array_list.Managed(u8), when: AllocWhen, max_value_len: usize) AllocIntoArrayListError!?[]const u8` |
| `skipValue` | `pub fn skipValue(self: *@This() ) SkipError!void` |
| `skipUntilStackHeight` | `pub fn skipUntilStackHeight(self: *@This() , terminal_stack_height: usize) NextError!void` |
| `stackHeight` | `pub fn stackHeight(self: *const @This() ) usize` |
| `ensureTotalStackCapacity` | `pub fn ensureTotalStackCapacity(self: *@This() , height: usize) Allocator.Error!void` |
| `next` | `pub fn next(self: *@This() ) NextError!Token` |
| `peekNextTokenType` | `pub fn peekNextTokenType(self: *@This() ) PeekError!TokenType` |
| `validate` | `pub fn validate(allocator: Allocator, s: []const u8) Allocator.Error!bool` |
| `getLine` | `pub fn getLine(self: *const @This() ) u64` |
| `getColumn` | `pub fn getColumn(self: *const @This() ) u64` |
| `getByteOffset` | `pub fn getByteOffset(self: *const @This() ) u64` |
| `init` | `pub fn init(allocator: Allocator, io_reader: *std.Io.Reader) @This()` |
| `nextAlloc` | `pub fn nextAlloc(self: *@This() , allocator: Allocator, when: AllocWhen) Reader.AllocError!Token` |
| `nextAllocMax` | `pub fn nextAllocMax(self: *@This() , allocator: Allocator, when: AllocWhen, max_value_len: usize) Reader.AllocError!Token` |
| `allocNextIntoArrayList` | `pub fn allocNextIntoArrayList(self: *@This() , value_list: *std.array_list.Managed(u8), when: AllocWhen) Reader.AllocError!?[]const u8` |
| `allocNextIntoArrayListMax` | `pub fn allocNextIntoArrayListMax(self: *@This() , value_list: *std.array_list.Managed(u8), when: AllocWhen, max_value_len: usize) Reader.AllocError!?[]const u8` |
| `skipValue` | `pub fn skipValue(self: *@This() ) Reader.SkipError!void` |
| `skipUntilStackHeight` | `pub fn skipUntilStackHeight(self: *@This() , terminal_stack_height: usize) Reader.NextError!void` |
| `next` | `pub fn next(self: *@This() ) Reader.NextError!Token` |
| `peekNextTokenType` | `pub fn peekNextTokenType(self: *@This() ) Reader.PeekError!TokenType` |
| `isNumberFormattedLikeAnInteger` | `pub fn isNumberFormattedLikeAnInteger(value: []const u8) bool` |

## json / Stringify

| Function | Signature |
|----------|-----------|
| `beginArray` | `pub fn beginArray(self: *Stringify) Error!void` |
| `beginObject` | `pub fn beginObject(self: *Stringify) Error!void` |
| `endArray` | `pub fn endArray(self: *Stringify) Error!void` |
| `endObject` | `pub fn endObject(self: *Stringify) Error!void` |
| `print` | `pub fn print(self: *Stringify, comptime fmt: []const u8, args: anytype) Error!void` |
| `beginWriteRaw` | `pub fn beginWriteRaw(self: *Stringify) !void` |
| `endWriteRaw` | `pub fn endWriteRaw(self: *Stringify) void` |
| `objectField` | `pub fn objectField(self: *Stringify, key: []const u8) Error!void` |
| `objectFieldRaw` | `pub fn objectFieldRaw(self: *Stringify, quoted_key: []const u8) Error!void` |
| `beginObjectFieldRaw` | `pub fn beginObjectFieldRaw(self: *Stringify) !void` |
| `endObjectFieldRaw` | `pub fn endObjectFieldRaw(self: *Stringify) void` |
| `jsonStringify` | `pub fn jsonStringify(self: *@This() , jw: anytype) !void`, it is called to do the serialization instead of the default behavior. The given `jw` is a pointer to this `Stringify`. See `std.json.Value` for an example. /// * See `Options.emit_null_opt...` |
| `jsonStringify` | `pub fn jsonStringify(self: *@This() , jw: anytype) !void`, it is called to do the serialization instead of the default behavior. The given `jw` is a pointer to this `Stringify`. /// * Zig `enum` -> JSON string naming the active tag. /// * If the e...` |
| `value` | `pub fn value(v: anytype, options: Options, writer: *Writer) Error!void` |
| `valueAlloc` | `pub fn valueAlloc(gpa: Allocator, v: anytype, options: Options) error` |
| `encodeJsonString` | `pub fn encodeJsonString(string: []const u8, options: Options, writer: *Writer) Error!void` |
| `encodeJsonStringChars` | `pub fn encodeJsonStringChars(chars: []const u8, options: Options, writer: *Writer) Error!void` |
| `jsonStringify` | `pub fn jsonStringify(v: @This() , jws: anytype) !void` |

## json / dynamic

| Function | Signature |
|----------|-----------|
| `parseFromNumberSlice` | `pub fn parseFromNumberSlice(s: []const u8) Value` |
| `dump` | `pub fn dump(v: Value) void` |
| `jsonStringify` | `pub fn jsonStringify(value: @This() , jws: anytype) !void` |
| `jsonParse` | `pub fn jsonParse(allocator: Allocator, source: anytype, options: ParseOptions) ParseError(@TypeOf(source.*))!@This()` |
| `jsonParseFromValue` | `pub fn jsonParseFromValue(allocator: Allocator, source: Value, options: ParseOptions) !@This()` |

## json / hashmap

| Function | Signature |
|----------|-----------|
| `ArrayHashMap` | `pub fn ArrayHashMap(comptime T: type) type` |
| `deinit` | `pub fn deinit(self: *@This() , allocator: Allocator) void` |
| `jsonParse` | `pub fn jsonParse(allocator: Allocator, source: anytype, options: ParseOptions) !@This()` |
| `jsonParseFromValue` | `pub fn jsonParseFromValue(allocator: Allocator, source: Value, options: ParseOptions) !@This()` |
| `jsonStringify` | `pub fn jsonStringify(self: @This() , jws: anytype) !void` |

## json / static

| Function | Signature |
|----------|-----------|
| `Parsed` | `pub fn Parsed(comptime T: type) type` |
| `deinit` | `pub fn deinit(self: @This() ) void` |
| `parseFromSlice` | `pub fn parseFromSlice(comptime T: type, allocator: Allocator, s: []const u8, options: ParseOptions,) ParseError(Scanner)!Parsed(T)` |
| `parseFromSliceLeaky` | `pub fn parseFromSliceLeaky(comptime T: type, allocator: Allocator, s: []const u8, options: ParseOptions,) ParseError(Scanner)!T` |
| `parseFromTokenSource` | `pub fn parseFromTokenSource(comptime T: type, allocator: Allocator, scanner_or_reader: anytype, options: ParseOptions,) ParseError(@TypeOf(scanner_or_reader.*))!Parsed(T)` |
| `parseFromTokenSourceLeaky` | `pub fn parseFromTokenSourceLeaky(comptime T: type, allocator: Allocator, scanner_or_reader: anytype, options: ParseOptions,) ParseError(@TypeOf(scanner_or_reader.*))!T` |
| `parseFromValue` | `pub fn parseFromValue(comptime T: type, allocator: Allocator, source: Value, options: ParseOptions,) ParseFromValueError!Parsed(T)` |
| `parseFromValueLeaky` | `pub fn parseFromValueLeaky(comptime T: type, allocator: Allocator, source: Value, options: ParseOptions,) ParseFromValueError!T` |
| `ParseError` | `pub fn ParseError(comptime Source: type) type` |
| `innerParse` | `pub fn innerParse(comptime T: type, allocator: Allocator, source: anytype, options: ParseOptions,) ParseError(@TypeOf(source.*))!T` |
| `innerParseFromValue` | `pub fn innerParseFromValue(comptime T: type, allocator: Allocator, source: Value, options: ParseOptions,) ParseFromValueError!T` |

## mem / Allocator

| Function | Signature |
|----------|-----------|
| `noAlloc` | `pub fn noAlloc(self: *anyopaque, len: usize, alignment: Alignment, ret_addr: usize,) ?[*]u8` |
| `noResize` | `pub fn noResize(self: *anyopaque, memory: []u8, alignment: Alignment, new_len: usize, ret_addr: usize,) bool` |
| `noRemap` | `pub fn noRemap(self: *anyopaque, memory: []u8, alignment: Alignment, new_len: usize, ret_addr: usize,) ?[*]u8` |
| `noFree` | `pub fn noFree(self: *anyopaque, memory: []u8, alignment: Alignment, ret_addr: usize,) void` |
| `rawAlloc` | `pub fn rawAlloc(a: Allocator, len: usize, alignment: Alignment, ret_addr: usize) ?[*]u8` |
| `rawResize` | `pub fn rawResize(a: Allocator, memory: []u8, alignment: Alignment, new_len: usize, ret_addr: usize) bool` |
| `rawRemap` | `pub fn rawRemap(a: Allocator, memory: []u8, alignment: Alignment, new_len: usize, ret_addr: usize) ?[*]u8` |
| `rawFree` | `pub fn rawFree(a: Allocator, memory: []u8, alignment: Alignment, ret_addr: usize) void` |
| `create` | `pub fn create(a: Allocator, comptime T: type) Error!*T` |
| `destroy` | `pub fn destroy(self: Allocator, ptr: anytype) void` |
| `alloc` | `pub fn alloc(self: Allocator, comptime T: type, n: usize) Error![]T` |
| `allocWithOptions` | `pub fn allocWithOptions(self: Allocator, comptime Elem: type, n: usize, /// null means naturally aligned comptime optional_alignment: ?Alignment, comptime optional_sentinel: ?Elem,) Error!AllocWithOptionsPayload(Elem, optional_alignment, optional_...` |
| `allocWithOptionsRetAddr` | `pub fn allocWithOptionsRetAddr(self: Allocator, comptime Elem: type, n: usize, /// null means naturally aligned comptime optional_alignment: ?Alignment, comptime optional_sentinel: ?Elem, return_address: usize,) Error!AllocWithOptionsPayload(Elem,...` |
| `allocSentinel` | `pub fn allocSentinel(self: Allocator, comptime Elem: type, n: usize, comptime sentinel: Elem,) Error![:sentinel]Elem` |
| `alignedAlloc` | `pub fn alignedAlloc(self: Allocator, comptime T: type, /// null means naturally aligned comptime alignment: ?Alignment, n: usize,) Error![]align(if (alignment) |a| a.toByteUnits() else @alignOf(T)) T` |
| `allocAdvancedWithRetAddr` | `pub fn allocAdvancedWithRetAddr(self: Allocator, comptime T: type, /// null means naturally aligned comptime alignment: ?Alignment, n: usize, return_address: usize,) Error![]align(if (alignment) |a| a.toByteUnits() else @alignOf(T)) T` |
| `resize` | `pub fn resize(self: Allocator, allocation: anytype, new_len: usize) bool` |
| `remap` | `pub fn remap(self: Allocator, allocation: anytype, new_len: usize) t:` |
| `realloc` | `pub fn realloc(self: Allocator, old_mem: anytype, new_n: usize) t:` |
| `reallocAdvanced` | `pub fn reallocAdvanced(self: Allocator, old_mem: anytype, new_n: usize, return_address: usize,) t:` |
| `free` | `pub fn free(self: Allocator, memory: anytype) void` |
| `dupe` | `pub fn dupe(allocator: Allocator, comptime T: type, m: []const T) Error![]T` |
| `dupeZ` | `pub fn dupeZ(allocator: Allocator, comptime T: type, m: []const T) Error![:0]T` |
| `dupeSentinel` | `pub fn dupeSentinel(allocator: Allocator, comptime T: type, m: []const T, comptime sentinel: T,) Error![:sentinel]T` |

## meta / trailer_flags

| Function | Signature |
|----------|-----------|
| `TrailerFlags` | `pub fn TrailerFlags(comptime Fields: type) type` |
| `has` | `pub fn has(self: Self, comptime field: FieldEnum) bool` |
| `get` | `pub fn get(self: Self, p: [*]align(@alignOf(Fields) ) const u8, comptime field: FieldEnum) ?Field(field)` |
| `setFlag` | `pub fn setFlag(self: *Self, comptime field: FieldEnum) void` |
| `init` | `pub fn init(fields: ActiveFields) Self` |
| `setMany` | `pub fn setMany(self: Self, p: [*]align(@alignOf(Fields) ) u8, fields: FieldValues) void` |
| `set` | `pub fn set(self: Self, p: [*]align(@alignOf(Fields) ) u8, comptime field: FieldEnum, value: Field(field), ) void` |
| `ptr` | `pub fn ptr(self: Self, p: [*]align(@alignOf(Fields) ) u8, comptime field: FieldEnum) *Field(field)` |
| `ptrConst` | `pub fn ptrConst(self: Self, p: [*]align(@alignOf(Fields) ) const u8, comptime field: FieldEnum) *const Field(field)` |
| `offset` | `pub fn offset(self: Self, comptime field: FieldEnum) usize` |
| `Field` | `pub fn Field(comptime field: FieldEnum) type` |
| `sizeInBytes` | `pub fn sizeInBytes(self: Self) usize` |

## zig / Ast

| Function | Signature |
|----------|-----------|
| `unwrap` | `pub fn unwrap(oti: OptionalTokenIndex) ?TokenIndex` |
| `fromToken` | `pub fn fromToken(ti: TokenIndex) OptionalTokenIndex` |
| `fromOptional` | `pub fn fromOptional(oti: ?TokenIndex) OptionalTokenIndex` |
| `init` | `pub fn init(base: TokenIndex, destination: TokenIndex) TokenOffset` |
| `toOptional` | `pub fn toOptional(to: TokenOffset) OptionalTokenOffset` |
| `toAbsolute` | `pub fn toAbsolute(offset: TokenOffset, base: TokenIndex) TokenIndex` |
| `unwrap` | `pub fn unwrap(oto: OptionalTokenOffset) ?TokenOffset` |
| `tokenTag` | `pub fn tokenTag(tree: *const Ast, token_index: TokenIndex) Token.Tag` |
| `tokenStart` | `pub fn tokenStart(tree: *const Ast, token_index: TokenIndex) ByteOffset` |
| `nodeTag` | `pub fn nodeTag(tree: *const Ast, node: Node.Index) Node.Tag` |
| `nodeMainToken` | `pub fn nodeMainToken(tree: *const Ast, node: Node.Index) TokenIndex` |
| `nodeData` | `pub fn nodeData(tree: *const Ast, node: Node.Index) Node.Data` |
| `isTokenPrecededByTags` | `pub fn isTokenPrecededByTags(tree: *const Ast, ti: TokenIndex, expected_token_tags: []const Token.Tag,) bool` |
| `deinit` | `pub fn deinit(tree: *Ast, gpa: Allocator) void` |
| `parse` | `pub fn parse(gpa: Allocator, source: [:0]const u8, mode: Mode) Allocator.Error!Ast` |
| `renderAlloc` | `pub fn renderAlloc(tree: Ast, gpa: Allocator) error` |
| `render` | `pub fn render(tree: Ast, gpa: Allocator, w: *Writer, fixups: Render.Fixups) Render.Error!void` |
| `errorOffset` | `pub fn errorOffset(tree: Ast, parse_error: Error) u32` |
| `tokenLocation` | `pub fn tokenLocation(self: Ast, start_offset: ByteOffset, token_index: TokenIndex) Location` |
| `tokenSlice` | `pub fn tokenSlice(tree: Ast, token_index: TokenIndex) []const u8` |
| `extraDataSlice` | `pub fn extraDataSlice(tree: Ast, range: Node.SubRange, comptime T: type) []const T` |
| `extraDataSliceWithLen` | `pub fn extraDataSliceWithLen(tree: Ast, start: ExtraIndex, len: u32, comptime T: type) []const T` |
| `extraData` | `pub fn extraData(tree: Ast, index: ExtraIndex, comptime T: type) T` |
| `rootDecls` | `pub fn rootDecls(tree: Ast) []const Node.Index` |
| `renderError` | `pub fn renderError(tree: Ast, parse_error: Error, w: *Writer) Writer.Error!void` |
| `firstToken` | `pub fn firstToken(tree: Ast, node: Node.Index) TokenIndex` |
| `lastToken` | `pub fn lastToken(tree: Ast, node: Node.Index) TokenIndex` |
| `tokensOnSameLine` | `pub fn tokensOnSameLine(tree: Ast, token1: TokenIndex, token2: TokenIndex) bool` |
| `getNodeSource` | `pub fn getNodeSource(tree: Ast, node: Node.Index) []const u8` |
| `globalVarDecl` | `pub fn globalVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `localVarDecl` | `pub fn localVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `simpleVarDecl` | `pub fn simpleVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `alignedVarDecl` | `pub fn alignedVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `assignDestructure` | `pub fn assignDestructure(tree: Ast, node: Node.Index) full.AssignDestructure` |
| `ifSimple` | `pub fn ifSimple(tree: Ast, node: Node.Index) full.If` |
| `ifFull` | `pub fn ifFull(tree: Ast, node: Node.Index) full.If` |
| `containerField` | `pub fn containerField(tree: Ast, node: Node.Index) full.ContainerField` |
| `containerFieldInit` | `pub fn containerFieldInit(tree: Ast, node: Node.Index) full.ContainerField` |
| `containerFieldAlign` | `pub fn containerFieldAlign(tree: Ast, node: Node.Index) full.ContainerField` |
| `fnProtoSimple` | `pub fn fnProtoSimple(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.FnProto` |
| `fnProtoMulti` | `pub fn fnProtoMulti(tree: Ast, node: Node.Index) full.FnProto` |
| `fnProtoOne` | `pub fn fnProtoOne(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.FnProto` |
| `fnProto` | `pub fn fnProto(tree: Ast, node: Node.Index) full.FnProto` |
| `structInitOne` | `pub fn structInitOne(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.StructInit` |
| `structInitDotTwo` | `pub fn structInitDotTwo(tree: Ast, buffer: *[2]Node.Index, node: Node.Index) full.StructInit` |
| `structInitDot` | `pub fn structInitDot(tree: Ast, node: Node.Index) full.StructInit` |
| `structInit` | `pub fn structInit(tree: Ast, node: Node.Index) full.StructInit` |
| `arrayInitOne` | `pub fn arrayInitOne(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.ArrayInit` |
| `arrayInitDotTwo` | `pub fn arrayInitDotTwo(tree: Ast, buffer: *[2]Node.Index, node: Node.Index) full.ArrayInit` |
| `arrayInitDot` | `pub fn arrayInitDot(tree: Ast, node: Node.Index) full.ArrayInit` |
| `arrayInit` | `pub fn arrayInit(tree: Ast, node: Node.Index) full.ArrayInit` |
| `arrayType` | `pub fn arrayType(tree: Ast, node: Node.Index) full.ArrayType` |
| `arrayTypeSentinel` | `pub fn arrayTypeSentinel(tree: Ast, node: Node.Index) full.ArrayType` |
| `ptrTypeAligned` | `pub fn ptrTypeAligned(tree: Ast, node: Node.Index) full.PtrType` |
| `ptrTypeSentinel` | `pub fn ptrTypeSentinel(tree: Ast, node: Node.Index) full.PtrType` |
| `ptrType` | `pub fn ptrType(tree: Ast, node: Node.Index) full.PtrType` |
| `ptrTypeBitRange` | `pub fn ptrTypeBitRange(tree: Ast, node: Node.Index) full.PtrType` |
| `sliceOpen` | `pub fn sliceOpen(tree: Ast, node: Node.Index) full.Slice` |
| `slice` | `pub fn slice(tree: Ast, node: Node.Index) full.Slice` |
| `sliceSentinel` | `pub fn sliceSentinel(tree: Ast, node: Node.Index) full.Slice` |
| `containerDeclTwo` | `pub fn containerDeclTwo(tree: Ast, buffer: *[2]Node.Index, node: Node.Index) full.ContainerDecl` |
| `containerDecl` | `pub fn containerDecl(tree: Ast, node: Node.Index) full.ContainerDecl` |
| `containerDeclArg` | `pub fn containerDeclArg(tree: Ast, node: Node.Index) full.ContainerDecl` |
| `containerDeclRoot` | `pub fn containerDeclRoot(tree: Ast) full.ContainerDecl` |
| `taggedUnionTwo` | `pub fn taggedUnionTwo(tree: Ast, buffer: *[2]Node.Index, node: Node.Index) full.ContainerDecl` |
| `taggedUnion` | `pub fn taggedUnion(tree: Ast, node: Node.Index) full.ContainerDecl` |
| `taggedUnionEnumTag` | `pub fn taggedUnionEnumTag(tree: Ast, node: Node.Index) full.ContainerDecl` |
| `switchFull` | `pub fn switchFull(tree: Ast, node: Node.Index) full.Switch` |
| `switchCaseOne` | `pub fn switchCaseOne(tree: Ast, node: Node.Index) full.SwitchCase` |
| `switchCase` | `pub fn switchCase(tree: Ast, node: Node.Index) full.SwitchCase` |
| `asmSimple` | `pub fn asmSimple(tree: Ast, node: Node.Index) full.Asm` |
| `asmFull` | `pub fn asmFull(tree: Ast, node: Node.Index) full.Asm` |
| `whileSimple` | `pub fn whileSimple(tree: Ast, node: Node.Index) full.While` |
| `whileCont` | `pub fn whileCont(tree: Ast, node: Node.Index) full.While` |
| `whileFull` | `pub fn whileFull(tree: Ast, node: Node.Index) full.While` |
| `forSimple` | `pub fn forSimple(tree: Ast, node: Node.Index) full.For` |
| `forFull` | `pub fn forFull(tree: Ast, node: Node.Index) full.For` |
| `callOne` | `pub fn callOne(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.Call` |
| `callFull` | `pub fn callFull(tree: Ast, node: Node.Index) full.Call` |
| `fullVarDecl` | `pub fn fullVarDecl(tree: Ast, node: Node.Index) ?full.VarDecl` |
| `fullIf` | `pub fn fullIf(tree: Ast, node: Node.Index) ?full.If` |
| `fullWhile` | `pub fn fullWhile(tree: Ast, node: Node.Index) ?full.While` |
| `fullFor` | `pub fn fullFor(tree: Ast, node: Node.Index) ?full.For` |
| `fullContainerField` | `pub fn fullContainerField(tree: Ast, node: Node.Index) ?full.ContainerField` |
| `fullFnProto` | `pub fn fullFnProto(tree: Ast, buffer: *[1]Ast.Node.Index, node: Node.Index) ?full.FnProto` |
| `fullStructInit` | `pub fn fullStructInit(tree: Ast, buffer: *[2]Ast.Node.Index, node: Node.Index) ?full.StructInit` |
| `fullArrayInit` | `pub fn fullArrayInit(tree: Ast, buffer: *[2]Node.Index, node: Node.Index) ?full.ArrayInit` |
| `fullArrayType` | `pub fn fullArrayType(tree: Ast, node: Node.Index) ?full.ArrayType` |
| `fullPtrType` | `pub fn fullPtrType(tree: Ast, node: Node.Index) ?full.PtrType` |
| `fullSlice` | `pub fn fullSlice(tree: Ast, node: Node.Index) ?full.Slice` |
| `fullContainerDecl` | `pub fn fullContainerDecl(tree: Ast, buffer: *[2]Ast.Node.Index, node: Node.Index) ?full.ContainerDecl` |
| `fullSwitch` | `pub fn fullSwitch(tree: Ast, node: Node.Index) ?full.Switch` |
| `fullSwitchCase` | `pub fn fullSwitchCase(tree: Ast, node: Node.Index) ?full.SwitchCase` |
| `fullAsm` | `pub fn fullAsm(tree: Ast, node: Node.Index) ?full.Asm` |
| `fullCall` | `pub fn fullCall(tree: Ast, buffer: *[1]Ast.Node.Index, node: Node.Index) ?full.Call` |
| `builtinCallParams` | `pub fn builtinCallParams(tree: Ast, buffer: *[2]Ast.Node.Index, node: Ast.Node.Index) ?[]const Node.Index` |
| `blockStatements` | `pub fn blockStatements(tree: Ast, buffer: *[2]Ast.Node.Index, node: Ast.Node.Index) ?[]const Node.Index` |
| `firstToken` | `pub fn firstToken(var_decl: VarDecl) TokenIndex` |
| `firstToken` | `pub fn firstToken(cf: ContainerField) TokenIndex` |
| `convertToNonTupleLike` | `pub fn convertToNonTupleLike(cf: *ContainerField, tree: *const Ast) void` |
| `firstToken` | `pub fn firstToken(fn_proto: FnProto) TokenIndex` |
| `next` | `pub fn next(it: *Iterator) ?Param` |
| `iterate` | `pub fn iterate(fn_proto: *const FnProto, tree: *const Ast) Iterator` |
| `toOptional` | `pub fn toOptional(i: Index) OptionalIndex` |
| `toOffset` | `pub fn toOffset(base: Index, destination: Index) Offset` |
| `unwrap` | `pub fn unwrap(oi: OptionalIndex) ?Index` |
| `fromOptional` | `pub fn fromOptional(oi: ?Index) OptionalIndex` |
| `toOptional` | `pub fn toOptional(o: Offset) OptionalOffset` |
| `toAbsolute` | `pub fn toAbsolute(offset: Offset, base: Index) Index` |
| `unwrap` | `pub fn unwrap(oo: OptionalOffset) ?Offset` |
| `isContainerField` | `pub fn isContainerField(tag: Tag) bool` |
| `nodeToSpan` | `pub fn nodeToSpan(tree: *const Ast, node: Ast.Node.Index) Span` |
| `tokenToSpan` | `pub fn tokenToSpan(tree: *const Ast, token: Ast.TokenIndex) Span` |
| `tokensToSpan` | `pub fn tokensToSpan(tree: *const Ast, start: Ast.TokenIndex, end: Ast.TokenIndex, main: Ast.TokenIndex) Span` |

## zig / AstGen

| Function | Signature |
|----------|-----------|
| `generate` | `pub fn generate(gpa: Allocator, tree: Ast) Allocator.Error!Zir` |

## zig / AstRlAnnotate

| Function | Signature |
|----------|-----------|
| `annotate` | `pub fn annotate(gpa: Allocator, arena: Allocator, tree: Ast) Allocator.Error!RlNeededSet` |

## zig / ErrorBundle

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(eb: *ErrorBundle, gpa: Allocator) void` |
| `errorMessageCount` | `pub fn errorMessageCount(eb: ErrorBundle) u32` |
| `getErrorMessageList` | `pub fn getErrorMessageList(eb: ErrorBundle) ErrorMessageList` |
| `getMessages` | `pub fn getMessages(eb: ErrorBundle) []const MessageIndex` |
| `getErrorMessage` | `pub fn getErrorMessage(eb: ErrorBundle, index: MessageIndex) ErrorMessage` |
| `getSourceLocation` | `pub fn getSourceLocation(eb: ErrorBundle, index: SourceLocationIndex) SourceLocation` |
| `getNotes` | `pub fn getNotes(eb: ErrorBundle, index: MessageIndex) []const MessageIndex` |
| `getCompileLogOutput` | `pub fn getCompileLogOutput(eb: ErrorBundle) [:0]const u8` |
| `nullTerminatedString` | `pub fn nullTerminatedString(eb: ErrorBundle, index: String) [:0]const u8` |
| `renderToStderr` | `pub fn renderToStderr(eb: ErrorBundle, io: Io, options: RenderOptions, color: std.zig.Color) RenderToStderrError!void` |
| `renderToWriter` | `pub fn renderToWriter(eb: ErrorBundle, options: RenderOptions, w: *Writer) Writer.Error!void` |
| `renderToTerminal` | `pub fn renderToTerminal(eb: ErrorBundle, options: RenderOptions, t: Io.Terminal) Io.Terminal.SetColorError!void` |
| `init` | `pub fn init(wip: *Wip, gpa: Allocator) !void` |
| `deinit` | `pub fn deinit(wip: *Wip) void` |
| `toOwnedBundle` | `pub fn toOwnedBundle(wip: *Wip, compile_log_text: []const u8) !ErrorBundle` |
| `tmpBundle` | `pub fn tmpBundle(wip: Wip) ErrorBundle` |
| `addString` | `pub fn addString(wip: *Wip, s: []const u8) Allocator.Error!String` |
| `printString` | `pub fn printString(wip: *Wip, comptime fmt: []const u8, args: anytype) Allocator.Error!String` |
| `addRootErrorMessage` | `pub fn addRootErrorMessage(wip: *Wip, em: ErrorMessage) Allocator.Error!void` |
| `addRootErrorMessageWithNotes` | `pub fn addRootErrorMessageWithNotes(wip: *Wip, msg: ErrorMessage, notes: []const ErrorMessage,) !void` |
| `addErrorMessage` | `pub fn addErrorMessage(wip: *Wip, em: ErrorMessage) Allocator.Error!MessageIndex` |
| `addErrorMessageAssumeCapacity` | `pub fn addErrorMessageAssumeCapacity(wip: *Wip, em: ErrorMessage) MessageIndex` |
| `addSourceLocation` | `pub fn addSourceLocation(wip: *Wip, sl: SourceLocation) Allocator.Error!SourceLocationIndex` |
| `addReferenceTrace` | `pub fn addReferenceTrace(wip: *Wip, rt: ReferenceTrace) Allocator.Error!void` |
| `addBundleAsNotes` | `pub fn addBundleAsNotes(wip: *Wip, other: ErrorBundle) Allocator.Error!void` |
| `addBundleAsRoots` | `pub fn addBundleAsRoots(wip: *Wip, other: ErrorBundle) !void` |
| `reserveNotes` | `pub fn reserveNotes(wip: *Wip, notes_len: u32) !u32` |
| `addZirErrorMessages` | `pub fn addZirErrorMessages(eb: *ErrorBundle.Wip, zir: std.zig.Zir, tree: std.zig.Ast, source: [:0]const u8, src_path: []const u8,) !void` |
| `addZoirErrorMessages` | `pub fn addZoirErrorMessages(eb: *ErrorBundle.Wip, zoir: std.zig.Zoir, tree: std.zig.Ast, source: [:0]const u8, src_path: []const u8,) !void` |

## zig / LibCDirs

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(arena: Allocator, io: Io, zig_lib_dir: []const u8, target: *const std.Target, is_native_abi: bool, link_libc: bool, libc_installation: ?*const LibCInstallation, environ_map: *const std.process.Environ.Map,) LibCInstallation.FindError...` |
| `detectFromBuilding` | `pub fn detectFromBuilding(arena: Allocator, zig_lib_dir: []const u8, target: *const std.Target,) !LibCDirs` |

## zig / LibCInstallation

| Function | Signature |
|----------|-----------|
| `parse` | `pub fn parse(allocator: Allocator, io: Io, libc_file: []const u8, target: *const std.Target) !LibCInstallation` |
| `render` | `pub fn render(self: LibCInstallation, out: *std.Io.Writer) !void` |
| `findNative` | `pub fn findNative(gpa: Allocator, io: Io, args: FindNativeOptions) FindError!LibCInstallation` |
| `deinit` | `pub fn deinit(self: *LibCInstallation, allocator: Allocator) void` |
| `get` | `pub fn get(args: GetArgs) CrtBasenames` |
| `resolveCrtPaths` | `pub fn resolveCrtPaths(lci: LibCInstallation, arena: Allocator, crt_basenames: CrtBasenames, target: *const std.Target,) error` |

## zig / Parse

| Function | Signature |
|----------|-----------|
| `parseRoot` | `pub fn parseRoot(p: *Parse) !void` |
| `parseZon` | `pub fn parseZon(p: *Parse) !void` |

## zig / Server

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) !Server` |
| `receiveMessage` | `pub fn receiveMessage(s: *Server) !InMessage.Header` |
| `receiveBody_u8` | `pub fn receiveBody_u8(s: *Server) !u8` |
| `receiveBody_u32` | `pub fn receiveBody_u32(s: *Server) !u32` |
| `receiveBody_u64` | `pub fn receiveBody_u64(s: *Server) !u64` |
| `serveStringMessage` | `pub fn serveStringMessage(s: *Server, tag: OutMessage.Tag, msg: []const u8) !void` |
| `serveMessageHeader` | `pub fn serveMessageHeader(s: *const Server, header: OutMessage.Header) !void` |
| `serveU64Message` | `pub fn serveU64Message(s: *const Server, tag: OutMessage.Tag, int: u64) !void` |
| `serveCoverageIdMessage` | `pub fn serveCoverageIdMessage(s: *const Server, id: u64, runs: u64, unique: u64, cov: u64) !void` |
| `serveEmitDigest` | `pub fn serveEmitDigest(s: *Server, digest: *const [Cache.bin_digest_len]u8, header: OutMessage.EmitDigest,) !void` |
| `serveTestResults` | `pub fn serveTestResults(s: *Server, msg: OutMessage.TestResults) !void` |
| `serveErrorBundle` | `pub fn serveErrorBundle(s: *Server, error_bundle: std.zig.ErrorBundle) !void` |
| `allocErrorBundle` | `pub fn allocErrorBundle(gpa: std.mem.Allocator, body: []const u8) error` |
| `serveTestMetadata` | `pub fn serveTestMetadata(s: *Server, test_metadata: TestMetadata) !void` |

## zig / WindowsSdk

| Function | Signature |
|----------|-----------|
| `find` | `pub fn find(gpa: Allocator, io: Io, arch: std.Target.Cpu.Arch, environ_map: *const Environ.Map,) error` |
| `free` | `pub fn free(sdk: WindowsSdk, gpa: Allocator) void` |
| `lessThan` | `pub fn lessThan(context: @This() , lhs: usize, rhs: usize) bool` |
| `swap` | `pub fn swap(context: @This() , lhs: usize, rhs: usize) void` |
| `getString` | `pub fn getString(reg: RegistryWtf8, gpa: Allocator, subkey: []const u8, value_name: []const u8) error` |
| `getDword` | `pub fn getDword(reg: RegistryWtf8, subkey: []const u8, value_name: []const u8) error` |

## zig / Zir

| Function | Signature |
|----------|-----------|
| `extraData` | `pub fn extraData(code: Zir, comptime T: type, index: usize) ExtraData(T)` |
| `nullTerminatedString` | `pub fn nullTerminatedString(code: Zir, index: NullTerminatedString) [:0]const u8` |
| `refSlice` | `pub fn refSlice(code: Zir, start: usize, len: usize) []Inst.Ref` |
| `bodySlice` | `pub fn bodySlice(zir: Zir, start: usize, len: usize) []Inst.Index` |
| `hasCompileErrors` | `pub fn hasCompileErrors(code: Zir) bool` |
| `loweringFailed` | `pub fn loweringFailed(code: Zir) bool` |
| `deinit` | `pub fn deinit(code: *Zir, gpa: Allocator) void` |
| `isNoReturn` | `pub fn isNoReturn(tag: Tag) bool` |
| `isAlwaysVoid` | `pub fn isAlwaysVoid(tag: Tag, data: Data) bool` |
| `toRef` | `pub fn toRef(i: Index) Inst.Ref` |
| `toOptional` | `pub fn toOptional(i: Index) OptionalIndex` |
| `unwrap` | `pub fn unwrap(oi: OptionalIndex) ?Index` |
| `toIndex` | `pub fn toIndex(inst: Ref) ?Index` |
| `toIndexAllowNone` | `pub fn toIndexAllowNone(inst: Ref) ?Index` |
| `get` | `pub fn get(self: @This() , code: Zir) []const u8` |
| `get` | `pub fn get(self: @This() , code: Zir) [:0]const u8` |
| `getStr` | `pub fn getStr(self: @This() , zir: Zir) [:0]const u8` |
| `hasName` | `pub fn hasName(id: Id) bool` |
| `hasLibName` | `pub fn hasLibName(id: Id) bool` |
| `hasTypeBody` | `pub fn hasTypeBody(id: Id) bool` |
| `hasValueBody` | `pub fn hasValueBody(id: Id) bool` |
| `hasSpecialBodies` | `pub fn hasSpecialBodies(id: Id) bool` |
| `linkage` | `pub fn linkage(id: Id) Declaration.Unwrapped.Linkage` |
| `kind` | `pub fn kind(id: Id) Declaration.Unwrapped.Kind` |
| `isPub` | `pub fn isPub(id: Id) bool` |
| `isThreadlocal` | `pub fn isThreadlocal(id: Id) bool` |
| `isNamedTest` | `pub fn isNamedTest(name: Name, zir: Zir) bool` |
| `toString` | `pub fn toString(name: Name, zir: Zir) ?NullTerminatedString` |
| `getBodies` | `pub fn getBodies(declaration: Declaration, extra_end: u32, zir: Zir) Bodies` |
| `wrap` | `pub fn wrap(unwrapped: ItemInfo.Unwrapped) ItemInfo` |
| `unwrap` | `pub fn unwrap(item_info: ItemInfo) ItemInfo.Unwrapped` |
| `bodyLen` | `pub fn bodyLen(item_info: ItemInfo) ?u32` |
| `wrap` | `pub fn wrap(cap: Unwrapped) Capture` |
| `unwrap` | `pub fn unwrap(cap: Capture) Unwrapped` |
| `needResultTypeBuiltinName` | `pub fn needResultTypeBuiltinName(flags: FullPtrCastFlags) []const u8` |
| `get` | `pub fn get(self: Float128) f128` |
| `notesLen` | `pub fn notesLen(item: Item, zir: Zir) u32` |
| `next` | `pub fn next(it: *DeclIterator) ?Inst.Index` |
| `clear` | `pub fn clear(contents: *DeclContents) void` |
| `deinit` | `pub fn deinit(contents: *DeclContents, gpa: Allocator) void` |
| `findTrackable` | `pub fn findTrackable(zir: Zir, gpa: Allocator, contents: *DeclContents, decl_inst: Zir.Inst.Index) !void` |
| `findTrackableRoot` | `pub fn findTrackableRoot(zir: Zir, gpa: Allocator, contents: *DeclContents) !void` |
| `getParamBody` | `pub fn getParamBody(zir: Zir, fn_inst: Inst.Index) []const Zir.Inst.Index` |
| `getParamName` | `pub fn getParamName(zir: Zir, param_inst: Inst.Index) ?NullTerminatedString` |
| `getFnInfo` | `pub fn getFnInfo(zir: Zir, fn_inst: Inst.Index) FnInfo` |
| `getDeclaration` | `pub fn getDeclaration(zir: Zir, inst: Zir.Inst.Index) Inst.Declaration.Unwrapped` |
| `getAssociatedSrcHash` | `pub fn getAssociatedSrcHash(zir: Zir, inst: Zir.Inst.Index) ?std.zig.SrcHash` |
| `getSwitchBlock` | `pub fn getSwitchBlock(zir: *const Zir, switch_inst: Inst.Index) UnwrappedSwitchBlock` |
| `anyRanges` | `pub fn anyRanges(unwrapped: *const UnwrappedSwitchBlock) bool` |
| `scalarCasesLen` | `pub fn scalarCasesLen(unwrapped: *const UnwrappedSwitchBlock) u32` |
| `multiCasesLen` | `pub fn multiCasesLen(unwrapped: *const UnwrappedSwitchBlock) u32` |
| `totalItemsLen` | `pub fn totalItemsLen(unwrapped: *const UnwrappedSwitchBlock) u32` |
| `next` | `pub fn next(it: *Iterator) ?Case` |
| `iterateCases` | `pub fn iterateCases(unwrapped: UnwrappedSwitchBlock) Case.Iterator` |
| `assertTrackable` | `pub fn assertTrackable(zir: Zir, inst_idx: Zir.Inst.Index) void` |

## zig / Zoir

| Function | Signature |
|----------|-----------|
| `hasCompileErrors` | `pub fn hasCompileErrors(zoir: Zoir) bool` |
| `deinit` | `pub fn deinit(zoir: Zoir, gpa: Allocator) void` |
| `get` | `pub fn get(idx: Index, zoir: Zoir) Node` |
| `getAstNode` | `pub fn getAstNode(idx: Index, zoir: Zoir) std.zig.Ast.Node.Index` |
| `at` | `pub fn at(r: Range, i: u32) Index` |
| `get` | `pub fn get(nts: NullTerminatedString, zoir: Zoir) [:0]const u8` |
| `getNotes` | `pub fn getNotes(err: CompileError, zoir: Zoir) []const Note` |

## zig / ZonGen

| Function | Signature |
|----------|-----------|
| `generate` | `pub fn generate(gpa: Allocator, tree: Ast, options: Options) Allocator.Error!Zoir` |
| `strLitSizeHint` | `pub fn strLitSizeHint(tree: Ast, node: Ast.Node.Index) usize` |
| `parseStrLit` | `pub fn parseStrLit(tree: Ast, node: Ast.Node.Index, writer: *Writer,) Writer.Error!std.zig.string_literal.Result` |

## zig / number_literal

| Function | Signature |
|----------|-----------|
| `parseNumberLiteral` | `pub fn parseNumberLiteral(bytes: []const u8) Result` |

## zig / primitives

| Function | Signature |
|----------|-----------|
| `isPrimitive` | `pub fn isPrimitive(name: []const u8) bool` |

## zig / string_literal

| Function | Signature |
|----------|-----------|
| `fmt` | `pub fn fmt(self: @This() , raw_string: []const u8) std.fmt.Alt(FormatMessage, formatMessage)` |
| `offset` | `pub fn offset(err: Error) usize` |
| `parseCharLiteral` | `pub fn parseCharLiteral(slice: []const u8) ParsedCharLiteral` |
| `parseEscapeSequence` | `pub fn parseEscapeSequence(slice: []const u8, offset: *usize) ParsedCharLiteral` |
| `parseWrite` | `pub fn parseWrite(writer: *Writer, bytes: []const u8) Writer.Error!Result` |
| `parseAlloc` | `pub fn parseAlloc(allocator: std.mem.Allocator, bytes: []const u8) ParseError![]u8` |

## zig / system

| Function | Signature |
|----------|-----------|
| `getExternalExecutor` | `pub fn getExternalExecutor(io: Io, host: *const std.Target, candidate: *const std.Target, options: GetExternalExecutorOptions,) Executor` |
| `resolveTargetQuery` | `pub fn resolveTargetQuery(io: Io, query: Target.Query) DetectError!Target` |

## zig / target

| Function | Signature |
|----------|-----------|
| `canBuildLibC` | `pub fn canBuildLibC(target: *const std.Target) bool` |
| `glibcRuntimeTriple` | `pub fn glibcRuntimeTriple(allocator: Allocator, arch: std.Target.Cpu.Arch, os: std.Target.Os.Tag, abi: std.Target.Abi,) Allocator.Error![]const u8` |
| `muslRuntimeTriple` | `pub fn muslRuntimeTriple(allocator: Allocator, arch: std.Target.Cpu.Arch, abi: std.Target.Abi,) Allocator.Error![]const u8` |
| `osArchName` | `pub fn osArchName(target: *const std.Target) [:0]const u8` |
| `muslArchName` | `pub fn muslArchName(arch: std.Target.Cpu.Arch, abi: std.Target.Abi) [:0]const u8` |
| `muslArchNameHeaders` | `pub fn muslArchNameHeaders(arch: std.Target.Cpu.Arch) [:0]const u8` |
| `muslAbiNameHeaders` | `pub fn muslAbiNameHeaders(abi: std.Target.Abi) [:0]const u8` |
| `glibcArchNameHeaders` | `pub fn glibcArchNameHeaders(arch: std.Target.Cpu.Arch) [:0]const u8` |
| `glibcAbiNameHeaders` | `pub fn glibcAbiNameHeaders(abi: std.Target.Abi) [:0]const u8` |
| `freebsdArchNameHeaders` | `pub fn freebsdArchNameHeaders(arch: std.Target.Cpu.Arch) [:0]const u8` |
| `netbsdArchNameHeaders` | `pub fn netbsdArchNameHeaders(arch: std.Target.Cpu.Arch) [:0]const u8` |
| `netbsdAbiNameHeaders` | `pub fn netbsdAbiNameHeaders(abi: std.Target.Abi) [:0]const u8` |
| `openbsdArchNameHeaders` | `pub fn openbsdArchNameHeaders(arch: std.Target.Cpu.Arch) [:0]const u8` |
| `isLibCLibName` | `pub fn isLibCLibName(target: *const std.Target, name: []const u8) bool` |
| `isLibCxxLibName` | `pub fn isLibCxxLibName(target: *const std.Target, name: []const u8) bool` |
| `intByteSize` | `pub fn intByteSize(target: *const std.Target, bits: u16) u16` |
| `intAlignment` | `pub fn intAlignment(target: *const std.Target, bits: u16) u16` |

## zig / tokenizer

| Function | Signature |
|----------|-----------|
| `getKeyword` | `pub fn getKeyword(bytes: []const u8) ?Tag` |
| `lexeme` | `pub fn lexeme(tag: Tag) ?[]const u8` |
| `symbol` | `pub fn symbol(tag: Tag) []const u8` |
| `dump` | `pub fn dump(self: *Tokenizer, token: *const Token) void` |
| `init` | `pub fn init(buffer: [:0]const u8) Tokenizer` |
| `next` | `pub fn next(self: *Tokenizer) Token` |

## zig / c_translation / builtins

| Function | Signature |
|----------|-----------|
| `abs` | `pub fn abs(val: c_int) c_int` |
| `assume` | `pub fn assume(cond: bool) void` |
| `bswap16` | `pub fn bswap16(val: u16) u16` |
| `bswap32` | `pub fn bswap32(val: u32) u32` |
| `bswap64` | `pub fn bswap64(val: u64) u64` |
| `ceilf` | `pub fn ceilf(val: f32) f32` |
| `ceil` | `pub fn ceil(val: f64) f64` |
| `clz` | `pub fn clz(val: c_uint) c_int` |
| `constant_p` | `pub fn constant_p(expr: anytype) c_int` |
| `cosf` | `pub fn cosf(val: f32) f32` |
| `cos` | `pub fn cos(val: f64) f64` |
| `ctz` | `pub fn ctz(val: c_uint) c_int` |
| `exp2f` | `pub fn exp2f(val: f32) f32` |
| `exp2` | `pub fn exp2(val: f64) f64` |
| `expf` | `pub fn expf(val: f32) f32` |
| `exp` | `pub fn exp(val: f64) f64` |
| `expect` | `pub fn expect(expr: c_long, c: c_long) c_long` |
| `fabsf` | `pub fn fabsf(val: f32) f32` |
| `fabs` | `pub fn fabs(val: f64) f64` |
| `floorf` | `pub fn floorf(val: f32) f32` |
| `floor` | `pub fn floor(val: f64) f64` |
| `has_builtin` | `pub fn has_builtin(func: anytype) c_int` |
| `huge_valf` | `pub fn huge_valf() f32` |
| `inff` | `pub fn inff() f32` |
| `isinf_sign` | `pub fn isinf_sign(x: anytype) c_int` |
| `isinf` | `pub fn isinf(x: anytype) c_int` |
| `isnan` | `pub fn isnan(x: anytype) c_int` |
| `labs` | `pub fn labs(val: c_long) c_long` |
| `llabs` | `pub fn llabs(val: c_longlong) c_longlong` |
| `log10f` | `pub fn log10f(val: f32) f32` |
| `log10` | `pub fn log10(val: f64) f64` |
| `log2f` | `pub fn log2f(val: f32) f32` |
| `log2` | `pub fn log2(val: f64) f64` |
| `logf` | `pub fn logf(val: f32) f32` |
| `log` | `pub fn log(val: f64) f64` |
| `memcpy_chk` | `pub fn memcpy_chk(noalias dst: ?*anyopaque, noalias src: ?*const anyopaque, len: usize, remaining: usize,) ?*anyopaque` |
| `memcpy` | `pub fn memcpy(noalias dst: ?*anyopaque, noalias src: ?*const anyopaque, len: usize,) ?*anyopaque` |
| `memset_chk` | `pub fn memset_chk(dst: ?*anyopaque, val: c_int, len: usize, remaining: usize,) ?*anyopaque` |
| `memset` | `pub fn memset(dst: ?*anyopaque, val: c_int, len: usize) ?*anyopaque` |
| `mul_overflow` | `pub fn mul_overflow(a: anytype, b: anytype, result: *@TypeOf(a, b) ) c_int` |
| `nanf` | `pub fn nanf(tagp: []const u8) f32` |
| `object_size` | `pub fn object_size(ptr: ?*const anyopaque, ty: c_int) usize` |
| `popcount` | `pub fn popcount(val: c_uint) c_int` |
| `roundf` | `pub fn roundf(val: f32) f32` |
| `round` | `pub fn round(val: f64) f64` |
| `signbitf` | `pub fn signbitf(val: f32) c_int` |
| `signbit` | `pub fn signbit(val: f64) c_int` |
| `sinf` | `pub fn sinf(val: f32) f32` |
| `sin` | `pub fn sin(val: f64) f64` |
| `sqrtf` | `pub fn sqrtf(val: f32) f32` |
| `sqrt` | `pub fn sqrt(val: f64) f64` |
| `strcmp` | `pub fn strcmp(s1: [*c]const u8, s2: [*c]const u8) c_int` |
| `strlen` | `pub fn strlen(s: [*c]const u8) usize` |
| `truncf` | `pub fn truncf(val: f32) f32` |
| `trunc` | `pub fn trunc(val: f64) f64` |

## zig / c_translation / helpers

| Function | Signature |
|----------|-----------|
| `ArithmeticConversion` | `pub fn ArithmeticConversion(comptime A: type, comptime B: type) type` |
| `FlexibleArrayType` | `pub fn FlexibleArrayType(comptime Self: type, comptime Element: type) type` |
| `promoteIntLiteral` | `pub fn promoteIntLiteral(comptime SuffixType: type, comptime number: comptime_int, comptime base: CIntLiteralBase,) PromoteIntLiteralReturnType(SuffixType, number, base)` |
| `shuffleVectorIndex` | `pub fn shuffleVectorIndex(comptime this_index: c_int, comptime source_vector_len: usize) i32` |
| `signedRemainder` | `pub fn signedRemainder(numerator: anytype, denominator: anytype) @TypeOf(numerator, denominator)` |
| `cast` | `pub fn cast(comptime DestType: type, target: anytype) DestType` |
| `sizeof` | `pub fn sizeof(target: anytype) usize` |
| `div` | `pub fn div(a: anytype, b: anytype) ArithmeticConversion(@TypeOf(a), @TypeOf(b))` |
| `rem` | `pub fn rem(a: anytype, b: anytype) ArithmeticConversion(@TypeOf(a), @TypeOf(b))` |
| `CAST_OR_CALL` | `pub fn CAST_OR_CALL(a: anytype, b: anytype) switch (@typeInfo(@TypeOf(a)))` |
| `DISCARD` | `pub fn DISCARD(x: anytype) void` |
| `F_SUFFIX` | `pub fn F_SUFFIX(comptime f: comptime_float) f32` |
| `L_SUFFIX` | `pub fn L_SUFFIX(comptime number: anytype) L_SUFFIX_ReturnType(number)` |
| `LL_SUFFIX` | `pub fn LL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_longlong, n, .decimal))` |
| `U_SUFFIX` | `pub fn U_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_uint, n, .decimal))` |
| `UL_SUFFIX` | `pub fn UL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_ulong, n, .decimal))` |
| `ULL_SUFFIX` | `pub fn ULL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_ulonglong, n, .decimal))` |
| `WL_CONTAINER_OF` | `pub fn WL_CONTAINER_OF(ptr: anytype, sample: anytype, comptime member: []const u8) @TypeOf(sample)` |

## zig / Ast / Render

| Function | Signature |
|----------|-----------|
| `count` | `pub fn count(f: Fixups) usize` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(f: *Fixups) void` |
| `deinit` | `pub fn deinit(f: *Fixups, gpa: Allocator) void` |
| `renderTree` | `pub fn renderTree(gpa: Allocator, w: *Writer, tree: Ast, fixups: Fixups) Error!void` |
| `init` | `pub fn init(gpa: Allocator, w: *Writer, starting_indent_delta: usize) AutoIndentingStream` |
| `deinit` | `pub fn deinit(self: *AutoIndentingStream) void` |
| `writeAll` | `pub fn writeAll(ais: *AutoIndentingStream, bytes: []const u8) Error!void` |
| `print` | `pub fn print(ais: *AutoIndentingStream, comptime format: []const u8, args: anytype) Error!void` |
| `writeByte` | `pub fn writeByte(ais: *AutoIndentingStream, byte: u8) Error!void` |
| `splatByteAll` | `pub fn splatByteAll(ais: *AutoIndentingStream, byte: u8, n: usize) Error!void` |
| `setIndentDelta` | `pub fn setIndentDelta(ais: *AutoIndentingStream, new_indent_delta: usize) void` |
| `insertNewline` | `pub fn insertNewline(ais: *AutoIndentingStream) Error!void` |
| `maybeInsertNewline` | `pub fn maybeInsertNewline(ais: *AutoIndentingStream) Error!void` |
| `isLineOverIndented` | `pub fn isLineOverIndented(ais: *AutoIndentingStream) bool` |
| `disableIndentCommitting` | `pub fn disableIndentCommitting(ais: *AutoIndentingStream) void` |
| `enableIndentCommitting` | `pub fn enableIndentCommitting(ais: *AutoIndentingStream) void` |
| `pushSpace` | `pub fn pushSpace(ais: *AutoIndentingStream, space: Space) !void` |
| `popSpace` | `pub fn popSpace(ais: *AutoIndentingStream) void` |
| `enableSpaceMode` | `pub fn enableSpaceMode(ais: *AutoIndentingStream, space: Space) void` |
| `disableSpaceMode` | `pub fn disableSpaceMode(ais: *AutoIndentingStream) void` |
| `lastSpaceModeIndent` | `pub fn lastSpaceModeIndent(ais: *AutoIndentingStream) usize` |
| `pushIndent` | `pub fn pushIndent(ais: *AutoIndentingStream, indent_type: IndentType) !void` |
| `forcePushIndent` | `pub fn forcePushIndent(ais: *AutoIndentingStream, indent_type: IndentType) !void` |
| `popIndent` | `pub fn popIndent(ais: *AutoIndentingStream) void` |
| `indentStackEmpty` | `pub fn indentStackEmpty(ais: *AutoIndentingStream) bool` |

## zig / llvm / BitcodeReader

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(allocator: std.mem.Allocator, options: InitOptions) BitcodeReader` |
| `deinit` | `pub fn deinit(bc: *BitcodeReader) void` |
| `checkMagic` | `pub fn checkMagic(bc: *BitcodeReader, magic: *const [4]u8) !void` |
| `next` | `pub fn next(bc: *BitcodeReader) !?Item` |
| `skipBlock` | `pub fn skipBlock(bc: *BitcodeReader, block: Block) !void` |

## zig / llvm / Builder

| Function | Signature |
|----------|-----------|
| `isAnon` | `pub fn isAnon(self: String) bool` |
| `slice` | `pub fn slice(self: String, builder: *const Builder) ?[]const u8` |
| `fmt` | `pub fn fmt(self: String, builder: *const Builder) std.fmt.Alt(FormatData, format)` |
| `fmtQ` | `pub fn fmtQ(self: String, builder: *const Builder) std.fmt.Alt(FormatData, format)` |
| `fmtRaw` | `pub fn fmtRaw(self: String, builder: *const Builder) std.fmt.Alt(FormatData, format)` |
| `hash` | `pub fn hash(_: Adapter, key: []const u8) u32` |
| `eql` | `pub fn eql(ctx: Adapter, lhs_key: []const u8, _: void, rhs_index: usize) bool` |
| `tag` | `pub fn tag(self: Type, builder: *const Builder) Tag` |
| `unnamedTag` | `pub fn unnamedTag(self: Type, builder: *const Builder) Tag` |
| `scalarTag` | `pub fn scalarTag(self: Type, builder: *const Builder) Tag` |
| `isFloatingPoint` | `pub fn isFloatingPoint(self: Type) bool` |
| `isInteger` | `pub fn isInteger(self: Type, builder: *const Builder) bool` |
| `isPointer` | `pub fn isPointer(self: Type, builder: *const Builder) bool` |
| `pointerAddrSpace` | `pub fn pointerAddrSpace(self: Type, builder: *const Builder) AddrSpace` |
| `isFunction` | `pub fn isFunction(self: Type, builder: *const Builder) bool` |
| `functionKind` | `pub fn functionKind(self: Type, builder: *const Builder) Type.Function.Kind` |
| `functionParameters` | `pub fn functionParameters(self: Type, builder: *const Builder) []const Type` |
| `functionReturn` | `pub fn functionReturn(self: Type, builder: *const Builder) Type` |
| `isVector` | `pub fn isVector(self: Type, builder: *const Builder) bool` |
| `vectorKind` | `pub fn vectorKind(self: Type, builder: *const Builder) Type.Vector.Kind` |
| `isStruct` | `pub fn isStruct(self: Type, builder: *const Builder) bool` |
| `structKind` | `pub fn structKind(self: Type, builder: *const Builder) Type.Structure.Kind` |
| `isAggregate` | `pub fn isAggregate(self: Type, builder: *const Builder) bool` |
| `scalarBits` | `pub fn scalarBits(self: Type, builder: *const Builder) u24` |
| `childType` | `pub fn childType(self: Type, builder: *const Builder) Type` |
| `scalarType` | `pub fn scalarType(self: Type, builder: *const Builder) Type` |
| `changeScalar` | `pub fn changeScalar(self: Type, scalar: Type, builder: *Builder) Allocator.Error!Type` |
| `changeScalarAssumeCapacity` | `pub fn changeScalarAssumeCapacity(self: Type, scalar: Type, builder: *Builder) Type` |
| `vectorLen` | `pub fn vectorLen(self: Type, builder: *const Builder) u32` |
| `changeLength` | `pub fn changeLength(self: Type, len: u32, builder: *Builder) Allocator.Error!Type` |
| `changeLengthAssumeCapacity` | `pub fn changeLengthAssumeCapacity(self: Type, len: u32, builder: *Builder) Type` |
| `aggregateLen` | `pub fn aggregateLen(self: Type, builder: *const Builder) usize` |
| `structFields` | `pub fn structFields(self: Type, builder: *const Builder) []const Type` |
| `childTypeAt` | `pub fn childTypeAt(self: Type, indices: []const u32, builder: *const Builder) Type` |
| `targetLayoutType` | `pub fn targetLayoutType(self: Type, builder: *const Builder) Type` |
| `isSized` | `pub fn isSized(self: Type, builder: *const Builder) Allocator.Error!bool` |
| `fmt` | `pub fn fmt(self: Type, builder: *const Builder, mode: FormatData.Mode) std.fmt.Alt(FormatData, format)` |
| `getKind` | `pub fn getKind(self: Index, builder: *const Builder) Kind` |
| `toAttribute` | `pub fn toAttribute(self: Index, builder: *const Builder) Attribute` |
| `fmt` | `pub fn fmt(self: Index, builder: *const Builder, flags: FormatData.Flags) std.fmt.Alt(FormatData, format)` |
| `fromString` | `pub fn fromString(str: String) Kind` |
| `getKind` | `pub fn getKind(self: Attribute) Kind` |
| `slice` | `pub fn slice(self: Attributes, builder: *const Builder) []const Attribute.Index` |
| `fmt` | `pub fn fmt(self: Attributes, builder: *const Builder, flags: FormatData.Flags) std.fmt.Alt(FormatData, format)` |
| `deinit` | `pub fn deinit(self: *Wip, builder: *const Builder) void` |
| `addFnAttr` | `pub fn addFnAttr(self: *Wip, attribute: Attribute, builder: *Builder) Allocator.Error!void` |
| `addFnAttrIndex` | `pub fn addFnAttrIndex(self: *Wip, attribute_index: Attribute.Index, builder: *const Builder,) Allocator.Error!void` |
| `removeFnAttr` | `pub fn removeFnAttr(self: *Wip, attribute_kind: Attribute.Kind) Allocator.Error!bool` |
| `addRetAttr` | `pub fn addRetAttr(self: *Wip, attribute: Attribute, builder: *Builder) Allocator.Error!void` |
| `addRetAttrIndex` | `pub fn addRetAttrIndex(self: *Wip, attribute_index: Attribute.Index, builder: *const Builder,) Allocator.Error!void` |
| `removeRetAttr` | `pub fn removeRetAttr(self: *Wip, attribute_kind: Attribute.Kind) Allocator.Error!bool` |
| `addParamAttr` | `pub fn addParamAttr(self: *Wip, param_index: usize, attribute: Attribute, builder: *Builder,) Allocator.Error!void` |
| `addParamAttrIndex` | `pub fn addParamAttrIndex(self: *Wip, param_index: usize, attribute_index: Attribute.Index, builder: *const Builder,) Allocator.Error!void` |
| `removeParamAttr` | `pub fn removeParamAttr(self: *Wip, param_index: usize, attribute_kind: Attribute.Kind,) Allocator.Error!bool` |
| `finish` | `pub fn finish(self: *const Wip, builder: *Builder) Allocator.Error!FunctionAttributes` |
| `func` | `pub fn func(self: FunctionAttributes, builder: *const Builder) Attributes` |
| `ret` | `pub fn ret(self: FunctionAttributes, builder: *const Builder) Attributes` |
| `param` | `pub fn param(self: FunctionAttributes, param_index: usize, builder: *const Builder) Attributes` |
| `toWip` | `pub fn toWip(self: FunctionAttributes, builder: *const Builder) Allocator.Error!Wip` |
| `format` | `pub fn format(self: Linkage, w: *Writer) Writer.Error!void` |
| `fmtOptional` | `pub fn fmtOptional(self: ?Linkage) std.fmt.Alt(?Linkage, formatOptional)` |
| `format` | `pub fn format(self: Preemption, w: *Writer) Writer.Error!void` |
| `fromSymbolVisibility` | `pub fn fromSymbolVisibility(sv: std.builtin.SymbolVisibility) Visibility` |
| `format` | `pub fn format(self: Visibility, writer: *Writer) Writer.Error!void` |
| `format` | `pub fn format(self: DllStorageClass, w: *Writer) Writer.Error!void` |
| `format` | `pub fn format(tl: ThreadLocal, w: *Writer) Writer.Error!void` |
| `format` | `pub fn format(p: Prefixed, w: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(tl: ThreadLocal, prefix: []const u8) Prefixed` |
| `format` | `pub fn format(self: UnnamedAddr, w: *Writer) Writer.Error!void` |
| `format` | `pub fn format(addr_space: AddrSpace, w: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(addr_space: AddrSpace, prefix: []const u8) Prefixed` |
| `format` | `pub fn format(self: ExternallyInitialized, w: *Writer) Writer.Error!void` |
| `fromByteUnits` | `pub fn fromByteUnits(bytes: u64) Alignment` |
| `toByteUnits` | `pub fn toByteUnits(self: Alignment) ?u64` |
| `toLlvm` | `pub fn toLlvm(self: Alignment) u6` |
| `fmt` | `pub fn fmt(alignment: Alignment, prefix: []const u8) Prefixed` |
| `format` | `pub fn format(self: CallConv, w: *Writer) Writer.Error!void` |
| `isAnon` | `pub fn isAnon(self: StrtabString) bool` |
| `slice` | `pub fn slice(self: StrtabString, builder: *const Builder) ?[]const u8` |
| `fmt` | `pub fn fmt(self: StrtabString, builder: *const Builder, quote_behavior: ?QuoteBehavior,) std.fmt.Alt(FormatData, format)` |
| `strtabString` | `pub fn strtabString(self: *Builder, bytes: []const u8) Allocator.Error!StrtabString` |
| `strtabStringIfExists` | `pub fn strtabStringIfExists(self: *const Builder, bytes: []const u8) ?StrtabString` |
| `strtabStringFmt` | `pub fn strtabStringFmt(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype) Allocator.Error!StrtabString` |
| `strtabStringFmtAssumeCapacity` | `pub fn strtabStringFmtAssumeCapacity(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype) StrtabString` |
| `trailingStrtabString` | `pub fn trailingStrtabString(self: *Builder) Allocator.Error!StrtabString` |
| `trailingStrtabStringAssumeCapacity` | `pub fn trailingStrtabStringAssumeCapacity(self: *Builder) StrtabString` |
| `unwrap` | `pub fn unwrap(self: Index, builder: *const Builder) Index` |
| `eql` | `pub fn eql(self: Index, other: Index, builder: *const Builder) bool` |
| `ptr` | `pub fn ptr(self: Index, builder: *Builder) *Global` |
| `ptrConst` | `pub fn ptrConst(self: Index, builder: *const Builder) *const Global` |
| `name` | `pub fn name(self: Index, builder: *const Builder) StrtabString` |
| `strtab` | `pub fn strtab(self: Index, builder: *const Builder) struct` |
| `typeOf` | `pub fn typeOf(self: Index, builder: *const Builder) Type` |
| `toConst` | `pub fn toConst(self: Index) Constant` |
| `setLinkage` | `pub fn setLinkage(self: Index, linkage: Linkage, builder: *Builder) void` |
| `setVisibility` | `pub fn setVisibility(self: Index, visibility: Visibility, builder: *Builder) void` |
| `setDllStorageClass` | `pub fn setDllStorageClass(self: Index, class: DllStorageClass, builder: *Builder) void` |
| `setUnnamedAddr` | `pub fn setUnnamedAddr(self: Index, unnamed_addr: UnnamedAddr, builder: *Builder) void` |
| `setDebugMetadata` | `pub fn setDebugMetadata(self: Index, dbg: Metadata, builder: *Builder) void` |
| `getDebugMetadata` | `pub fn getDebugMetadata(self: Index, builder: *const Builder) Metadata.Optional` |
| `fmt` | `pub fn fmt(self: Index, builder: *const Builder) std.fmt.Alt(FormatData, format)` |
| `rename` | `pub fn rename(self: Index, new_name: StrtabString, builder: *Builder) Allocator.Error!void` |
| `takeName` | `pub fn takeName(self: Index, other: Index, builder: *Builder) Allocator.Error!void` |
| `replace` | `pub fn replace(self: Index, other: Index, builder: *Builder) Allocator.Error!void` |
| `delete` | `pub fn delete(self: Index, builder: *Builder) void` |
| `ptr` | `pub fn ptr(self: Index, builder: *Builder) *Alias` |
| `ptrConst` | `pub fn ptrConst(self: Index, builder: *const Builder) *const Alias` |
| `toConst` | `pub fn toConst(self: Index, builder: *const Builder) Constant` |
| `toValue` | `pub fn toValue(self: Index, builder: *const Builder) Value` |
| `getAliasee` | `pub fn getAliasee(self: Index, builder: *const Builder) Global.Index` |
| `setAliasee` | `pub fn setAliasee(self: Index, aliasee: Constant, builder: *Builder) void` |
| `ptr` | `pub fn ptr(self: Index, builder: *Builder) *Variable` |
| `ptrConst` | `pub fn ptrConst(self: Index, builder: *const Builder) *const Variable` |
| `setThreadLocal` | `pub fn setThreadLocal(self: Index, thread_local: ThreadLocal, builder: *Builder) void` |
| `setMutability` | `pub fn setMutability(self: Index, mutability: Mutability, builder: *Builder) void` |
| `setInitializer` | `pub fn setInitializer(self: Index, initializer: Constant, builder: *Builder,) Allocator.Error!void` |
| `setSection` | `pub fn setSection(self: Index, section: String, builder: *Builder) void` |
| `setAlignment` | `pub fn setAlignment(self: Index, alignment: Alignment, builder: *Builder) void` |
| `getAlignment` | `pub fn getAlignment(self: Index, builder: *Builder) Alignment` |
| `setGlobalVariableExpression` | `pub fn setGlobalVariableExpression(self: Index, expression: Metadata, builder: *Builder) void` |
| `getGlobalVariableExpression` | `pub fn getGlobalVariableExpression(self: Index, builder: *Builder) Metadata.Optional` |
| `ptr` | `pub fn ptr(self: Index, builder: *Builder) *Function` |
| `ptrConst` | `pub fn ptrConst(self: Index, builder: *const Builder) *const Function` |
| `setCallConv` | `pub fn setCallConv(self: Index, call_conv: CallConv, builder: *Builder) void` |
| `setAttributes` | `pub fn setAttributes(self: Index, new_function_attributes: FunctionAttributes, builder: *Builder,) void` |
| `setSubprogram` | `pub fn setSubprogram(self: Index, subprogram: Metadata, builder: *Builder) void` |
| `getSubprogram` | `pub fn getSubprogram(self: Index, builder: *const Builder) Metadata.Optional` |
| `toBinaryOpcode` | `pub fn toBinaryOpcode(self: Tag) BinaryOpcode` |
| `toCastOpcode` | `pub fn toCastOpcode(self: Tag) CastOpcode` |
| `toCmpPredicate` | `pub fn toCmpPredicate(self: Tag) CmpPredicate` |
| `name` | `pub fn name(self: Instruction.Index, function: *const Function) String` |
| `valueIndex` | `pub fn valueIndex(self: Instruction.Index, function: *const Function) u32` |
| `toValue` | `pub fn toValue(self: Instruction.Index) Value` |
| `isTerminatorWip` | `pub fn isTerminatorWip(self: Instruction.Index, wip: *const WipFunction) bool` |
| `hasResultWip` | `pub fn hasResultWip(self: Instruction.Index, wip: *const WipFunction) bool` |
| `typeOfWip` | `pub fn typeOfWip(self: Instruction.Index, wip: *const WipFunction) Type` |
| `typeOf` | `pub fn typeOf(self: Instruction.Index, function_index: Function.Index, builder: *Builder,) Type` |
| `fmt` | `pub fn fmt(self: Instruction.Index, function: Function.Index, builder: *Builder, flags: FormatFlags,) std.fmt.Alt(FormatData, format)` |
| `fromMetadata` | `pub fn fromMetadata(metadata: Metadata) Weights` |
| `toMetadata` | `pub fn toMetadata(weights: Weights) Metadata` |
| `deinit` | `pub fn deinit(self: *Function, gpa: Allocator) void` |
| `arg` | `pub fn arg(self: *const Function, index: u32) Value` |
| `toMetadata` | `pub fn toMetadata(self: DebugLocation, builder: *Builder) Allocator.Error!Metadata.Optional` |
| `ptr` | `pub fn ptr(self: Index, wip: *WipFunction) *Block` |
| `ptrConst` | `pub fn ptrConst(self: Index, wip: *const WipFunction) *const Block` |
| `toInst` | `pub fn toInst(self: Index, function: *const Function) Instruction.Index` |
| `init` | `pub fn init(builder: *Builder, options: struct { function: Function.Index, strip: bool, }) Allocator.Error!WipFunction` |
| `arg` | `pub fn arg(self: *const WipFunction, index: u32) Value` |
| `block` | `pub fn block(self: *WipFunction, incoming: u32, name: []const u8) Allocator.Error!Block.Index` |
| `ret` | `pub fn ret(self: *WipFunction, val: Value) Allocator.Error!Instruction.Index` |
| `retVoid` | `pub fn retVoid(self: *WipFunction) Allocator.Error!Instruction.Index` |
| `br` | `pub fn br(self: *WipFunction, dest: Block.Index) Allocator.Error!Instruction.Index` |
| `brCond` | `pub fn brCond(self: *WipFunction, cond: Value, then: Block.Index, @"else": Block.Index, weights: enum { none, unpredictable, then_likely, else_likely },) Allocator.Error!Instruction.Index` |
| `addCase` | `pub fn addCase(self: *WipSwitch, val: Constant, dest: Block.Index, wip: *WipFunction,) Allocator.Error!void` |
| `finish` | `pub fn finish(self: WipSwitch, wip: *WipFunction) void` |
| `indirectbr` | `pub fn indirectbr(self: *WipFunction, addr: Value, targets: []const Block.Index,) Allocator.Error!Instruction.Index` |
| `un` | `pub fn un(self: *WipFunction, tag: Instruction.Tag, val: Value, name: []const u8,) Allocator.Error!Value` |
| `not` | `pub fn not(self: *WipFunction, val: Value, name: []const u8) Allocator.Error!Value` |
| `neg` | `pub fn neg(self: *WipFunction, val: Value, name: []const u8) Allocator.Error!Value` |
| `bin` | `pub fn bin(self: *WipFunction, tag: Instruction.Tag, lhs: Value, rhs: Value, name: []const u8,) Allocator.Error!Value` |
| `extractElement` | `pub fn extractElement(self: *WipFunction, val: Value, index: Value, name: []const u8,) Allocator.Error!Value` |
| `insertElement` | `pub fn insertElement(self: *WipFunction, val: Value, elem: Value, index: Value, name: []const u8,) Allocator.Error!Value` |
| `shuffleVector` | `pub fn shuffleVector(self: *WipFunction, lhs: Value, rhs: Value, mask: Value, name: []const u8,) Allocator.Error!Value` |
| `splatVector` | `pub fn splatVector(self: *WipFunction, ty: Type, elem: Value, name: []const u8,) Allocator.Error!Value` |
| `extractValue` | `pub fn extractValue(self: *WipFunction, val: Value, indices: []const u32, name: []const u8,) Allocator.Error!Value` |
| `insertValue` | `pub fn insertValue(self: *WipFunction, val: Value, elem: Value, indices: []const u32, name: []const u8,) Allocator.Error!Value` |
| `buildAggregate` | `pub fn buildAggregate(self: *WipFunction, ty: Type, elems: []const Value, name: []const u8,) Allocator.Error!Value` |
| `alloca` | `pub fn alloca(self: *WipFunction, kind: Instruction.Alloca.Kind, ty: Type, len: Value, alignment: Alignment, addr_space: AddrSpace, name: []const u8,) Allocator.Error!Value` |
| `load` | `pub fn load(self: *WipFunction, access_kind: MemoryAccessKind, ty: Type, ptr: Value, alignment: Alignment, name: []const u8,) Allocator.Error!Value` |
| `loadAtomic` | `pub fn loadAtomic(self: *WipFunction, access_kind: MemoryAccessKind, ty: Type, ptr: Value, sync_scope: SyncScope, ordering: AtomicOrdering, alignment: Alignment, name: []const u8,) Allocator.Error!Value` |
| `store` | `pub fn store(self: *WipFunction, kind: MemoryAccessKind, val: Value, ptr: Value, alignment: Alignment,) Allocator.Error!Instruction.Index` |
| `storeAtomic` | `pub fn storeAtomic(self: *WipFunction, access_kind: MemoryAccessKind, val: Value, ptr: Value, sync_scope: SyncScope, ordering: AtomicOrdering, alignment: Alignment,) Allocator.Error!Instruction.Index` |
| `fence` | `pub fn fence(self: *WipFunction, sync_scope: SyncScope, ordering: AtomicOrdering,) Allocator.Error!Instruction.Index` |
| `cmpxchg` | `pub fn cmpxchg(self: *WipFunction, kind: Instruction.CmpXchg.Kind, access_kind: MemoryAccessKind, ptr: Value, cmp: Value, new: Value, sync_scope: SyncScope, success_ordering: AtomicOrdering, failure_ordering: AtomicOrdering, alignment: Alignment, ...` |
| `atomicrmw` | `pub fn atomicrmw(self: *WipFunction, access_kind: MemoryAccessKind, operation: Instruction.AtomicRmw.Operation, ptr: Value, val: Value, sync_scope: SyncScope, ordering: AtomicOrdering, alignment: Alignment, name: []const u8,) Allocator.Error!Value` |
| `gep` | `pub fn gep(self: *WipFunction, kind: Instruction.GetElementPtr.Kind, ty: Type, base: Value, indices: []const Value, name: []const u8,) Allocator.Error!Value` |
| `gepStruct` | `pub fn gepStruct(self: *WipFunction, ty: Type, base: Value, index: usize, name: []const u8,) Allocator.Error!Value` |
| `conv` | `pub fn conv(self: *WipFunction, signedness: Instruction.Cast.Signedness, val: Value, ty: Type, name: []const u8,) Allocator.Error!Value` |
| `cast` | `pub fn cast(self: *WipFunction, tag: Instruction.Tag, val: Value, ty: Type, name: []const u8,) Allocator.Error!Value` |
| `icmp` | `pub fn icmp(self: *WipFunction, cond: IntegerCondition, lhs: Value, rhs: Value, name: []const u8,) Allocator.Error!Value` |
| `fcmp` | `pub fn fcmp(self: *WipFunction, fast: FastMathKind, cond: FloatCondition, lhs: Value, rhs: Value, name: []const u8,) Allocator.Error!Value` |
| `toValue` | `pub fn toValue(self: WipPhi) Value` |
| `finish` | `pub fn finish(self: WipPhi, vals: []const Value, blocks: []const Block.Index, wip: *WipFunction,) void` |
| `phi` | `pub fn phi(self: *WipFunction, ty: Type, name: []const u8) Allocator.Error!WipPhi` |
| `phiFast` | `pub fn phiFast(self: *WipFunction, ty: Type, name: []const u8) Allocator.Error!WipPhi` |
| `select` | `pub fn select(self: *WipFunction, fast: FastMathKind, cond: Value, lhs: Value, rhs: Value, name: []const u8,) Allocator.Error!Value` |
| `call` | `pub fn call(self: *WipFunction, kind: Instruction.Call.Kind, call_conv: CallConv, function_attributes: FunctionAttributes, ty: Type, callee: Value, args: []const Value, name: []const u8,) Allocator.Error!Value` |
| `callAsm` | `pub fn callAsm(self: *WipFunction, function_attributes: FunctionAttributes, ty: Type, kind: Constant.Assembly.Info, assembly: String, constraints: String, args: []const Value, name: []const u8,) Allocator.Error!Value` |
| `callIntrinsic` | `pub fn callIntrinsic(self: *WipFunction, fast: FastMathKind, function_attributes: FunctionAttributes, id: Intrinsic, overload: []const Type, args: []const Value, name: []const u8,) Allocator.Error!Value` |
| `callIntrinsicAssumeCold` | `pub fn callIntrinsicAssumeCold(self: *WipFunction) Allocator.Error!Value` |
| `callMemCpy` | `pub fn callMemCpy(self: *WipFunction, dst: Value, dst_align: Alignment, src: Value, src_align: Alignment, len: Value, kind: MemoryAccessKind, @"inline": bool,) Allocator.Error!Instruction.Index` |
| `callMemMove` | `pub fn callMemMove(self: *WipFunction, dst: Value, dst_align: Alignment, src: Value, src_align: Alignment, len: Value, kind: MemoryAccessKind,) Allocator.Error!Instruction.Index` |
| `callMemSet` | `pub fn callMemSet(self: *WipFunction, dst: Value, dst_align: Alignment, val: Value, len: Value, kind: MemoryAccessKind, @"inline": bool,) Allocator.Error!Instruction.Index` |
| `vaArg` | `pub fn vaArg(self: *WipFunction, list: Value, ty: Type, name: []const u8) Allocator.Error!Value` |
| `debugValue` | `pub fn debugValue(self: *WipFunction, value: Value) Allocator.Error!Metadata.Optional` |
| `finish` | `pub fn finish(self: *WipFunction) Allocator.Error!void` |
| `deinit` | `pub fn deinit(self: *WipFunction) void` |
| `format` | `pub fn format(memory_access_kind: MemoryAccessKind, w: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(memory_access_kind: MemoryAccessKind, prefix: []const u8) Prefixed` |
| `format` | `pub fn format(sync_scope: SyncScope, w: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(sync_scope: SyncScope, prefix: []const u8) Prefixed` |
| `format` | `pub fn format(atomic_ordering: AtomicOrdering, w: *Writer) Writer.Error!void` |
| `fmt` | `pub fn fmt(atomic_ordering: AtomicOrdering, prefix: []const u8) Prefixed` |
| `toCallKind` | `pub fn toCallKind(self: FastMathKind) Function.Instruction.Call.Kind` |
| `unwrap` | `pub fn unwrap(self: Constant) union(enum)` |
| `toValue` | `pub fn toValue(self: Constant) Value` |
| `typeOf` | `pub fn typeOf(self: Constant, builder: *Builder) Type` |
| `isZeroInit` | `pub fn isZeroInit(self: Constant, builder: *const Builder) bool` |
| `getBase` | `pub fn getBase(self: Constant, builder: *const Builder) Global.Index` |
| `fmt` | `pub fn fmt(self: Constant, builder: *Builder, flags: FormatFlags) std.fmt.Alt(FormatData, format)` |
| `unwrap` | `pub fn unwrap(self: Value) union(enum)` |
| `typeOfWip` | `pub fn typeOfWip(self: Value, wip: *const WipFunction) Type` |
| `typeOf` | `pub fn typeOf(self: Value, function: Function.Index, builder: *Builder) Type` |
| `toConst` | `pub fn toConst(self: Value) ?Constant` |
| `fmt` | `pub fn fmt(self: Value, function: Function.Index, builder: *Builder, flags: FormatFlags) std.fmt.Alt(FormatData, format)` |
| `wrap` | `pub fn wrap(metadata: ?Metadata) Metadata.Optional` |
| `unwrap` | `pub fn unwrap(metadata: Metadata.Optional) ?Metadata` |
| `toValue` | `pub fn toValue(metadata: Metadata.Optional) Value` |
| `toString` | `pub fn toString(metadata: Metadata.Optional) Metadata.String.Optional` |
| `toOptional` | `pub fn toOptional(metadata: Metadata) Metadata.Optional` |
| `toValue` | `pub fn toValue(metadata: Metadata) Value` |
| `wrap` | `pub fn wrap(metadata: ?Metadata.String) Metadata.String.Optional` |
| `unwrap` | `pub fn unwrap(metadata: Metadata.String.Optional) ?Metadata.String` |
| `toMetadata` | `pub fn toMetadata(metadata: Metadata.String.Optional) Metadata.Optional` |
| `toOptional` | `pub fn toOptional(metadata: Metadata.String) Metadata.String.Optional` |
| `toMetadata` | `pub fn toMetadata(metadata: Metadata.String) Metadata` |
| `slice` | `pub fn slice(metadata: Metadata.String, builder: *const Builder) []const u8` |
| `toString` | `pub fn toString(metadata: Metadata) Metadata.String` |
| `isInline` | `pub fn isInline(metadata_tag: Metadata.Tag) bool` |
| `tag` | `pub fn tag(metadata: Metadata, builder: *const Builder) Tag` |
| `item` | `pub fn item(metadata: Metadata, builder: *const Builder) Item` |
| `isInline` | `pub fn isInline(metadata: Metadata, builder: *const Builder) bool` |
| `unwrap` | `pub fn unwrap(metadata: Metadata, builder: *const Builder) Metadata` |
| `format` | `pub fn format(self: DIFlags, w: *Writer) Writer.Error!void` |
| `format` | `pub fn format(self: DISPFlags, w: *Writer) Writer.Error!void` |
| `getSubprogram` | `pub fn getSubprogram(metadata: Metadata, builder: *const Builder) Subprogram` |
| `bitSize` | `pub fn bitSize(self: BasicType) u64` |
| `bitSize` | `pub fn bitSize(self: CompositeType) u64` |
| `bitAlign` | `pub fn bitAlign(self: CompositeType) u64` |
| `bitSize` | `pub fn bitSize(self: DerivedType) u64` |
| `bitAlign` | `pub fn bitAlign(self: DerivedType) u64` |
| `bitOffset` | `pub fn bitOffset(self: DerivedType) u64` |
| `init` | `pub fn init(options: Options) Allocator.Error!Builder` |
| `clearAndFree` | `pub fn clearAndFree(self: *Builder) void` |
| `deinit` | `pub fn deinit(self: *Builder) void` |
| `finishModuleAsm` | `pub fn finishModuleAsm(self: *Builder, aw: *Writer.Allocating) Allocator.Error!void` |
| `string` | `pub fn string(self: *Builder, bytes: []const u8) Allocator.Error!String` |
| `stringNull` | `pub fn stringNull(self: *Builder, bytes: [:0]const u8) Allocator.Error!String` |
| `stringIfExists` | `pub fn stringIfExists(self: *const Builder, bytes: []const u8) ?String` |
| `fmt` | `pub fn fmt(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype) Allocator.Error!String` |
| `fmtAssumeCapacity` | `pub fn fmtAssumeCapacity(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype) String` |
| `trailingString` | `pub fn trailingString(self: *Builder) Allocator.Error!String` |
| `trailingStringAssumeCapacity` | `pub fn trailingStringAssumeCapacity(self: *Builder) String` |
| `fnType` | `pub fn fnType(self: *Builder, ret: Type, params: []const Type, kind: Type.Function.Kind,) Allocator.Error!Type` |
| `intType` | `pub fn intType(self: *Builder, bits: u24) Allocator.Error!Type` |
| `ptrType` | `pub fn ptrType(self: *Builder, addr_space: AddrSpace) Allocator.Error!Type` |
| `vectorType` | `pub fn vectorType(self: *Builder, kind: Type.Vector.Kind, len: u32, child: Type,) Allocator.Error!Type` |
| `arrayType` | `pub fn arrayType(self: *Builder, len: u64, child: Type) Allocator.Error!Type` |
| `structType` | `pub fn structType(self: *Builder, kind: Type.Structure.Kind, fields: []const Type,) Allocator.Error!Type` |
| `opaqueType` | `pub fn opaqueType(self: *Builder, name: String) Allocator.Error!Type` |
| `namedTypeSetBody` | `pub fn namedTypeSetBody(self: *Builder, named_type: Type, body_type: Type,) void` |
| `attr` | `pub fn attr(self: *Builder, attribute: Attribute) Allocator.Error!Attribute.Index` |
| `attrs` | `pub fn attrs(self: *Builder, attributes: []Attribute.Index) Allocator.Error!Attributes` |
| `lessThan` | `pub fn lessThan(builder: *const Builder, lhs: Attribute.Index, rhs: Attribute.Index) bool` |
| `fnAttrs` | `pub fn fnAttrs(self: *Builder, fn_attributes: []const Attributes) Allocator.Error!FunctionAttributes` |
| `addGlobal` | `pub fn addGlobal(self: *Builder, name: StrtabString, global: Global) Allocator.Error!Global.Index` |
| `addGlobalAssumeCapacity` | `pub fn addGlobalAssumeCapacity(self: *Builder, name: StrtabString, global: Global) Global.Index` |
| `getGlobal` | `pub fn getGlobal(self: *const Builder, name: StrtabString) ?Global.Index` |
| `addAlias` | `pub fn addAlias(self: *Builder, name: StrtabString, ty: Type, addr_space: AddrSpace, aliasee: Constant,) Allocator.Error!Alias.Index` |
| `addAliasAssumeCapacity` | `pub fn addAliasAssumeCapacity(self: *Builder, name: StrtabString, ty: Type, addr_space: AddrSpace, aliasee: Constant,) Alias.Index` |
| `addVariable` | `pub fn addVariable(self: *Builder, name: StrtabString, ty: Type, addr_space: AddrSpace,) Allocator.Error!Variable.Index` |
| `addVariableAssumeCapacity` | `pub fn addVariableAssumeCapacity(self: *Builder, ty: Type, name: StrtabString, addr_space: AddrSpace,) Variable.Index` |
| `addFunction` | `pub fn addFunction(self: *Builder, ty: Type, name: StrtabString, addr_space: AddrSpace,) Allocator.Error!Function.Index` |
| `addFunctionAssumeCapacity` | `pub fn addFunctionAssumeCapacity(self: *Builder, ty: Type, name: StrtabString, addr_space: AddrSpace,) Function.Index` |
| `getIntrinsic` | `pub fn getIntrinsic(self: *Builder, id: Intrinsic, overload: []const Type,) Allocator.Error!Function.Index` |
| `intConst` | `pub fn intConst(self: *Builder, ty: Type, value: anytype) Allocator.Error!Constant` |
| `intValue` | `pub fn intValue(self: *Builder, ty: Type, value: anytype) Allocator.Error!Value` |
| `bigIntConst` | `pub fn bigIntConst(self: *Builder, ty: Type, value: std.math.big.int.Const) Allocator.Error!Constant` |
| `bigIntValue` | `pub fn bigIntValue(self: *Builder, ty: Type, value: std.math.big.int.Const) Allocator.Error!Value` |
| `fpConst` | `pub fn fpConst(self: *Builder, ty: Type, comptime val: comptime_float) Allocator.Error!Constant` |
| `fpValue` | `pub fn fpValue(self: *Builder, ty: Type, comptime value: comptime_float) Allocator.Error!Value` |
| `nanConst` | `pub fn nanConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `nanValue` | `pub fn nanValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `halfConst` | `pub fn halfConst(self: *Builder, val: f16) Allocator.Error!Constant` |
| `halfValue` | `pub fn halfValue(self: *Builder, value: f16) Allocator.Error!Value` |
| `bfloatConst` | `pub fn bfloatConst(self: *Builder, val: f32) Allocator.Error!Constant` |
| `bfloatValue` | `pub fn bfloatValue(self: *Builder, value: f32) Allocator.Error!Value` |
| `floatConst` | `pub fn floatConst(self: *Builder, val: f32) Allocator.Error!Constant` |
| `floatValue` | `pub fn floatValue(self: *Builder, value: f32) Allocator.Error!Value` |
| `doubleConst` | `pub fn doubleConst(self: *Builder, val: f64) Allocator.Error!Constant` |
| `doubleValue` | `pub fn doubleValue(self: *Builder, value: f64) Allocator.Error!Value` |
| `fp128Const` | `pub fn fp128Const(self: *Builder, val: f128) Allocator.Error!Constant` |
| `fp128Value` | `pub fn fp128Value(self: *Builder, value: f128) Allocator.Error!Value` |
| `x86_fp80Const` | `pub fn x86_fp80Const(self: *Builder, val: f80) Allocator.Error!Constant` |
| `x86_fp80Value` | `pub fn x86_fp80Value(self: *Builder, value: f80) Allocator.Error!Value` |
| `ppc_fp128Const` | `pub fn ppc_fp128Const(self: *Builder, val: [2]f64) Allocator.Error!Constant` |
| `ppc_fp128Value` | `pub fn ppc_fp128Value(self: *Builder, value: [2]f64) Allocator.Error!Value` |
| `nullConst` | `pub fn nullConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `nullValue` | `pub fn nullValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `noneConst` | `pub fn noneConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `noneValue` | `pub fn noneValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `structConst` | `pub fn structConst(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Constant` |
| `structValue` | `pub fn structValue(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Value` |
| `arrayConst` | `pub fn arrayConst(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Constant` |
| `arrayValue` | `pub fn arrayValue(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Value` |
| `stringConst` | `pub fn stringConst(self: *Builder, val: String) Allocator.Error!Constant` |
| `stringValue` | `pub fn stringValue(self: *Builder, val: String) Allocator.Error!Value` |
| `vectorConst` | `pub fn vectorConst(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Constant` |
| `vectorValue` | `pub fn vectorValue(self: *Builder, ty: Type, vals: []const Constant) Allocator.Error!Value` |
| `splatConst` | `pub fn splatConst(self: *Builder, ty: Type, val: Constant) Allocator.Error!Constant` |
| `splatValue` | `pub fn splatValue(self: *Builder, ty: Type, val: Constant) Allocator.Error!Value` |
| `zeroInitConst` | `pub fn zeroInitConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `zeroInitValue` | `pub fn zeroInitValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `undefConst` | `pub fn undefConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `undefValue` | `pub fn undefValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `poisonConst` | `pub fn poisonConst(self: *Builder, ty: Type) Allocator.Error!Constant` |
| `poisonValue` | `pub fn poisonValue(self: *Builder, ty: Type) Allocator.Error!Value` |
| `blockAddrConst` | `pub fn blockAddrConst(self: *Builder, function: Function.Index, block: Function.Block.Index,) Allocator.Error!Constant` |
| `blockAddrValue` | `pub fn blockAddrValue(self: *Builder, function: Function.Index, block: Function.Block.Index,) Allocator.Error!Value` |
| `dsoLocalEquivalentConst` | `pub fn dsoLocalEquivalentConst(self: *Builder, function: Function.Index) Allocator.Error!Constant` |
| `dsoLocalEquivalentValue` | `pub fn dsoLocalEquivalentValue(self: *Builder, function: Function.Index) Allocator.Error!Value` |
| `noCfiConst` | `pub fn noCfiConst(self: *Builder, function: Function.Index) Allocator.Error!Constant` |
| `noCfiValue` | `pub fn noCfiValue(self: *Builder, function: Function.Index) Allocator.Error!Value` |
| `convConst` | `pub fn convConst(self: *Builder, val: Constant, ty: Type,) Allocator.Error!Constant` |
| `convValue` | `pub fn convValue(self: *Builder, val: Constant, ty: Type,) Allocator.Error!Value` |
| `castConst` | `pub fn castConst(self: *Builder, tag: Constant.Tag, val: Constant, ty: Type) Allocator.Error!Constant` |
| `castValue` | `pub fn castValue(self: *Builder, tag: Constant.Tag, val: Constant, ty: Type) Allocator.Error!Value` |
| `gepConst` | `pub fn gepConst(self: *Builder, comptime kind: Constant.GetElementPtr.Kind, ty: Type, base: Constant, inrange: ?u16, indices: []const Constant,) Allocator.Error!Constant` |
| `gepValue` | `pub fn gepValue(self: *Builder, comptime kind: Constant.GetElementPtr.Kind, ty: Type, base: Constant, inrange: ?u16, indices: []const Constant,) Allocator.Error!Value` |
| `binConst` | `pub fn binConst(self: *Builder, tag: Constant.Tag, lhs: Constant, rhs: Constant,) Allocator.Error!Constant` |
| `binValue` | `pub fn binValue(self: *Builder, tag: Constant.Tag, lhs: Constant, rhs: Constant) Allocator.Error!Value` |
| `asmConst` | `pub fn asmConst(self: *Builder, ty: Type, info: Constant.Assembly.Info, assembly: String, constraints: String,) Allocator.Error!Constant` |
| `asmValue` | `pub fn asmValue(self: *Builder, ty: Type, info: Constant.Assembly.Info, assembly: String, constraints: String,) Allocator.Error!Value` |
| `dump` | `pub fn dump(b: *Builder, io: Io) void` |
| `printToFilePath` | `pub fn printToFilePath(b: *Builder, io: Io, dir: Io.Dir, path: []const u8) !void` |
| `printToFile` | `pub fn printToFile(b: *Builder, io: Io, file: Io.File, buffer: []u8) !void` |
| `print` | `pub fn print(self: *Builder, w: *Writer) (Writer.Error || Allocator.Error)!void` |
| `hash` | `pub fn hash(_: @This() , key: Key) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Key, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Type.Vector) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Type.Vector, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Type.Array) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Type.Array, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: []const Type) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: []const Type, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: String) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: String, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Type.Item) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Type.Item, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: []const u32) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: []const u32, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: f64) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: f64, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: f128) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: f128, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: f80) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: f80, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: [2]f64) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: [2]f64, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Constant.Splat) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Constant.Splat, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Constant.BlockAddress) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Constant.BlockAddress, _: void, rhs_index: usize) bool` |
| `hash` | `pub fn hash(_: @This() , key: Constant.Item) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Constant.Item, _: void, rhs_index: usize) bool` |
| `metadataString` | `pub fn metadataString(self: *Builder, bytes: []const u8) Allocator.Error!Metadata.String` |
| `metadataStringFromStrtabString` | `pub fn metadataStringFromStrtabString(self: *Builder, str: StrtabString,) Allocator.Error!Metadata.String` |
| `metadataStringFmt` | `pub fn metadataStringFmt(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype,) Allocator.Error!Metadata.String` |
| `metadataStringFmtAssumeCapacity` | `pub fn metadataStringFmtAssumeCapacity(self: *Builder, comptime fmt_str: []const u8, fmt_args: anytype,) Metadata.String` |
| `trailingMetadataString` | `pub fn trailingMetadataString(self: *Builder) Allocator.Error!Metadata.String` |
| `trailingMetadataStringAssumeCapacity` | `pub fn trailingMetadataStringAssumeCapacity(self: *Builder) Metadata.String` |
| `addNamedMetadata` | `pub fn addNamedMetadata(self: *Builder, name: String, operands: []const Metadata) Allocator.Error!void` |
| `debugFile` | `pub fn debugFile(self: *Builder, filename: ?Metadata.String, directory: ?Metadata.String,) Allocator.Error!Metadata` |
| `debugCompileUnit` | `pub fn debugCompileUnit(self: *Builder, file: ?Metadata, producer: ?Metadata.String, enums: ?Metadata, globals: ?Metadata, options: Metadata.CompileUnit.Options,) Allocator.Error!Metadata` |
| `debugSubprogram` | `pub fn debugSubprogram(self: *Builder, file: ?Metadata, name: ?Metadata.String, linkage_name: ?Metadata.String, line: u32, scope_line: u32, ty: ?Metadata, options: Metadata.Subprogram.Options, compile_unit: ?Metadata,) Allocator.Error!Metadata` |
| `debugLexicalBlock` | `pub fn debugLexicalBlock(self: *Builder, scope: ?Metadata, file: ?Metadata, line: u32, column: u32,) Allocator.Error!Metadata` |
| `debugLocation` | `pub fn debugLocation(self: *Builder, line: u32, column: u32, scope: Metadata, inlined_at: ?Metadata,) Allocator.Error!Metadata` |
| `debugBoolType` | `pub fn debugBoolType(self: *Builder, name: ?Metadata.String, size_in_bits: u64,) Allocator.Error!Metadata` |
| `debugUnsignedType` | `pub fn debugUnsignedType(self: *Builder, name: ?Metadata.String, size_in_bits: u64,) Allocator.Error!Metadata` |
| `debugSignedType` | `pub fn debugSignedType(self: *Builder, name: ?Metadata.String, size_in_bits: u64,) Allocator.Error!Metadata` |
| `debugFloatType` | `pub fn debugFloatType(self: *Builder, name: ?Metadata.String, size_in_bits: u64,) Allocator.Error!Metadata` |
| `debugForwardReference` | `pub fn debugForwardReference(self: *Builder) Allocator.Error!Metadata` |
| `debugStructType` | `pub fn debugStructType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, fields_tuple: ?Metadata,) Allocator.Error!Metadata` |
| `debugUnionType` | `pub fn debugUnionType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, fields_tuple: ?Metadata,) Allocator.Error!Metadata` |
| `debugEnumerationType` | `pub fn debugEnumerationType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, fields_tuple: ?Metadata,) Allocator.Error!Metadata` |
| `debugArrayType` | `pub fn debugArrayType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, fields_tuple: ?Metadata,) Allocator.Error!Metadata` |
| `debugVectorType` | `pub fn debugVectorType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, fields_tuple: ?Metadata,) Allocator.Error!Metadata` |
| `debugPointerType` | `pub fn debugPointerType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, offset_in_bits: u64,) Allocator.Error!Metadata` |
| `debugMemberType` | `pub fn debugMemberType(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, underlying_type: ?Metadata, size_in_bits: u64, align_in_bits: u64, offset_in_bits: u64,) Allocator.Error!Metadata` |
| `debugSubroutineType` | `pub fn debugSubroutineType(self: *Builder, types_tuple: ?Metadata) Allocator.Error!Metadata` |
| `debugEnumerator` | `pub fn debugEnumerator(self: *Builder, name: ?Metadata.String, unsigned: bool, bit_width: u32, value: std.math.big.int.Const,) Allocator.Error!Metadata` |
| `debugSubrange` | `pub fn debugSubrange(self: *Builder, lower_bound: ?Metadata, count: ?Metadata,) Allocator.Error!Metadata` |
| `debugExpression` | `pub fn debugExpression(self: *Builder, elements: []const u32) Allocator.Error!Metadata` |
| `metadataTuple` | `pub fn metadataTuple(self: *Builder, elements: []const Metadata) Allocator.Error!Metadata` |
| `metadataTupleOptionals` | `pub fn metadataTupleOptionals(self: *Builder, elements: []const Metadata.Optional,) Allocator.Error!Metadata` |
| `debugLocalVar` | `pub fn debugLocalVar(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, ty: ?Metadata,) Allocator.Error!Metadata` |
| `debugParameter` | `pub fn debugParameter(self: *Builder, name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, ty: ?Metadata, arg_no: u32,) Allocator.Error!Metadata` |
| `debugGlobalVar` | `pub fn debugGlobalVar(self: *Builder, name: ?Metadata.String, linkage_name: ?Metadata.String, file: ?Metadata, scope: ?Metadata, line: u32, ty: ?Metadata, variable: Variable.Index, options: Metadata.GlobalVar.Options,) Allocator.Error!Metadata` |
| `debugGlobalVarExpression` | `pub fn debugGlobalVarExpression(self: *Builder, variable: ?Metadata, expression: ?Metadata,) Allocator.Error!Metadata` |
| `metadataConstant` | `pub fn metadataConstant(self: *Builder, value: Constant) Allocator.Error!Metadata` |
| `resolveDebugForwardReference` | `pub fn resolveDebugForwardReference(self: *Builder, fwd_ref: Metadata, value: Metadata) void` |
| `debugCompileUnitAssumeCapacity` | `pub fn debugCompileUnitAssumeCapacity(self: *Builder, file: ?Metadata, producer: ?Metadata.String, enums: ?Metadata, globals: ?Metadata, options: Metadata.CompileUnit.Options,) Metadata` |
| `hash` | `pub fn hash(_: @This() , key: Constant) u32` |
| `eql` | `pub fn eql(ctx: @This() , lhs_key: Constant, _: void, rhs_index: usize) bool` |
| `toBitcode` | `pub fn toBitcode(self: *Builder, allocator: Allocator, producer: Producer) bitcode_writer.Error![]const u32` |
| `get` | `pub fn get(adapter: @This() , param: anytype) switch (@TypeOf(param))` |
| `getConstantIndex` | `pub fn getConstantIndex(adapter: @This() , constant: Constant) u32` |
| `numConstants` | `pub fn numConstants(adapter: @This() ) u32` |
| `numGlobals` | `pub fn numGlobals(adapter: @This() ) u32` |
| `getMetadataIndex` | `pub fn getMetadataIndex(adapter: @This() , metadata: Metadata) u32` |
| `getOptionalMetadataIndex` | `pub fn getOptionalMetadataIndex(adapter: @This() , metadata: Metadata.Optional) u32` |
| `getValueIndex` | `pub fn getValueIndex(adapter: @This() , value: Value) u32` |
| `getOffsetValueIndex` | `pub fn getOffsetValueIndex(adapter: @This() , value: Value) u32` |
| `getOffsetValueSignedIndex` | `pub fn getOffsetValueSignedIndex(adapter: @This() , value: Value) i32` |
| `getOffsetConstantIndex` | `pub fn getOffsetConstantIndex(adapter: @This() , constant: Constant) u32` |
| `offset` | `pub fn offset(adapter: @This() ) u32` |

## zig / llvm / bitcode_writer

| Function | Signature |
|----------|-----------|
| `BitcodeWriter` | `pub fn BitcodeWriter(comptime types: []const type) type` |
| `getTypeWidth` | `pub fn getTypeWidth(self: BcWriter, comptime Type: type) u16` |
| `init` | `pub fn init(allocator: std.mem.Allocator, widths: [types.len]u16) BcWriter` |
| `deinit` | `pub fn deinit(self: BcWriter) void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *BcWriter) Error![]const u32` |
| `length` | `pub fn length(self: BcWriter) usize` |
| `writeBits` | `pub fn writeBits(self: *BcWriter, value: anytype, bits: u16) Error!void` |
| `writeVbr` | `pub fn writeVbr(self: *BcWriter, value: anytype, comptime vbr_bits: usize) Error!void` |
| `bitsVbr` | `pub fn bitsVbr(value: anytype, comptime vbr_bits: usize) u16` |
| `write6BitChar` | `pub fn write6BitChar(self: *BcWriter, c: u8) Error!void` |
| `writeBlob` | `pub fn writeBlob(self: *BcWriter, blob: []const u8) Error!void` |
| `alignTo32` | `pub fn alignTo32(self: *BcWriter) Error!void` |
| `enterTopBlock` | `pub fn enterTopBlock(self: *BcWriter, comptime SubBlock: type) Error!BlockWriter(SubBlock)` |
| `init` | `pub fn init(bitcode: *BcWriter, comptime parent_abbrev_len: u6, comptime define_abbrevs: bool) Error!Self` |
| `enterSubBlock` | `pub fn enterSubBlock(self: Self, comptime SubBlock: type, comptime define_abbrevs: bool) Error!BlockWriter(SubBlock)` |
| `end` | `pub fn end(self: *Self) Error!void` |
| `writeUnabbrev` | `pub fn writeUnabbrev(self: *Self, code: u32, values: []const u64) Error!void` |
| `writeAbbrev` | `pub fn writeAbbrev(self: *Self, params: anytype) Error!void` |
| `get` | `pub fn get(_: @This() , param: anytype) @TypeOf(param)` |
| `abbrevId` | `pub fn abbrevId(comptime Abbrev: type) u32` |
| `writeAbbrevAdapted` | `pub fn writeAbbrevAdapted(self: *Self, params: anytype, adapter: anytype,) Error!void` |
| `defineAbbrev` | `pub fn defineAbbrev(self: *Self, comptime ops: []const AbbrevOp) Error!void` |

## zig / system / NativePaths

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(arena: Allocator, io: Io, native_target: *const std.Target, environ_map: *process.Environ.Map,) !NativePaths` |
| `addIncludeDir` | `pub fn addIncludeDir(self: *NativePaths, s: []const u8) !void` |
| `addIncludeDirFmt` | `pub fn addIncludeDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addLibDir` | `pub fn addLibDir(self: *NativePaths, s: []const u8) !void` |
| `addLibDirFmt` | `pub fn addLibDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addWarning` | `pub fn addWarning(self: *NativePaths, s: []const u8) !void` |
| `addFrameworkDir` | `pub fn addFrameworkDir(self: *NativePaths, s: []const u8) !void` |
| `addFrameworkDirFmt` | `pub fn addFrameworkDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addWarningFmt` | `pub fn addWarningFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addRPath` | `pub fn addRPath(self: *NativePaths, s: []const u8) !void` |

## zig / system / arm

| Function | Signature |
|----------|-----------|
| `isKnown` | `pub fn isKnown(core: CoreInfo, is_64bit: bool) ?*const Target.Cpu.Model` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(arch: Target.Cpu.Arch, registers: [12]u64) ?Target.Cpu` |

## zig / system / darwin

| Function | Signature |
|----------|-----------|
| `isSdkInstalled` | `pub fn isSdkInstalled(gpa: Allocator, io: Io) bool` |
| `getSdk` | `pub fn getSdk(gpa: Allocator, io: Io, target: *const Target) ?[]const u8` |

## zig / system / linux

| Function | Signature |
|----------|-----------|
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(io: Io) ?Target.Cpu` |

## zig / system / loongarch

| Function | Signature |
|----------|-----------|
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(arch: std.Target.Cpu.Arch, os: std.Target.Os, query: std.Target.Query,) ?std.Target.Cpu` |

## zig / system / windows

| Function | Signature |
|----------|-----------|
| `detectRuntimeVersion` | `pub fn detectRuntimeVersion() WindowsVersion` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures() ?Target.Cpu` |

## zig / system / x86

| Function | Signature |
|----------|-----------|
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(arch: Target.Cpu.Arch, os: Target.Os, query: Target.Query) Target.Cpu` |

## zig / system / darwin / macos

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(io: Io, target_os: *Target.Os) !void` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures() ?Target.Cpu` |

## testing / FailingAllocator

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(internal_allocator: mem.Allocator, config: Config) FailingAllocator` |
| `allocator` | `pub fn allocator(self: *FailingAllocator) mem.Allocator` |
| `getStackTrace` | `pub fn getStackTrace(self: *FailingAllocator) std.builtin.StackTrace` |

## Target / Query

| Function | Signature |
|----------|-----------|
| `eql` | `pub fn eql(a: CpuModel, b: CpuModel) bool` |
| `eql` | `pub fn eql(a: OsVersion, b: OsVersion) bool` |
| `eqlOpt` | `pub fn eqlOpt(a: ?OsVersion, b: ?OsVersion) bool` |
| `fromTarget` | `pub fn fromTarget(target: *const Target) Query` |
| `parse` | `pub fn parse(args: ParseOptions) !Query` |
| `parseCpuArch` | `pub fn parseCpuArch(args: ParseOptions) ?Target.Cpu.Arch` |
| `parseVersion` | `pub fn parseVersion(ver: []const u8) error` |
| `isNativeCpu` | `pub fn isNativeCpu(self: Query) bool` |
| `isNativeOs` | `pub fn isNativeOs(self: Query) bool` |
| `isNativeAbi` | `pub fn isNativeAbi(self: Query) bool` |
| `isNativeTriple` | `pub fn isNativeTriple(self: Query) bool` |
| `isNative` | `pub fn isNative(self: Query) bool` |
| `canDetectLibC` | `pub fn canDetectLibC(self: Query) bool` |
| `zigTriple` | `pub fn zigTriple(self: Query, gpa: Allocator) Allocator.Error![]u8` |
| `serializeCpu` | `pub fn serializeCpu(q: Query, buffer: *std.array_list.Managed(u8) ) Allocator.Error!void` |
| `serializeCpuAlloc` | `pub fn serializeCpuAlloc(q: Query, ally: Allocator) Allocator.Error![]u8` |
| `allocDescription` | `pub fn allocDescription(self: Query, allocator: Allocator) ![]u8` |
| `setGnuLibCVersion` | `pub fn setGnuLibCVersion(self: *Query, major: u32, minor: u32, patch: u32) void` |
| `eql` | `pub fn eql(a: Query, b: Query) bool` |

## tar / Writer

| Function | Signature |
|----------|-----------|
| `setRoot` | `pub fn setRoot(w: *Writer, root: []const u8) Error!void` |
| `writeDir` | `pub fn writeDir(w: *Writer, sub_path: []const u8, options: Options) Error!void` |
| `writeFileTimestamp` | `pub fn writeFileTimestamp(w: *Writer, sub_path: []const u8, file_reader: *Io.File.Reader, mtime: Io.Timestamp,) WriteFileError!void` |
| `writeFile` | `pub fn writeFile(w: *Writer, sub_path: []const u8, file_reader: *Io.File.Reader, /// If you want to match the file format's expectations, it wants number of /// seconds since POSIX epoch. Zero is also a great option here to make /// generated tarb...` |
| `writeFileStream` | `pub fn writeFileStream(w: *Writer, sub_path: []const u8, size: u64, reader: *Io.Reader, options: Options,) WriteFileStreamError!void` |
| `writeFileBytes` | `pub fn writeFileBytes(w: *Writer, sub_path: []const u8, content: []const u8, options: Options) Error!void` |
| `writeLink` | `pub fn writeLink(w: *Writer, sub_path: []const u8, link_name: []const u8, options: Options) Error!void` |
| `finishPedantically` | `pub fn finishPedantically(w: *Writer) Io.Writer.Error!void` |
| `init` | `pub fn init(typeflag: FileType) Header` |
| `setSize` | `pub fn setSize(w: *Header, size: u64) error` |
| `setMode` | `pub fn setMode(w: *Header, mode: u32) error` |
| `setMtime` | `pub fn setMtime(w: *Header, mtime: u64) error` |
| `updateChecksum` | `pub fn updateChecksum(w: *Header) !void` |
| `write` | `pub fn write(h: *Header, bw: *Io.Writer) error` |
| `setLinkname` | `pub fn setLinkname(w: *Header, link: []const u8) !void` |
| `setPath` | `pub fn setPath(w: *Header, prefix: []const u8, sub_path: []const u8) !void` |

## os / emscripten

| Function | Signature |
|----------|-----------|
| `CPU_COUNT` | `pub fn CPU_COUNT(set: cpu_set_t) cpu_count_t` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) SIG` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `ISREG` | `pub fn ISREG(m: mode_t) bool` |
| `ISDIR` | `pub fn ISDIR(m: mode_t) bool` |
| `ISCHR` | `pub fn ISCHR(m: mode_t) bool` |
| `ISBLK` | `pub fn ISBLK(m: mode_t) bool` |
| `ISFIFO` | `pub fn ISFIFO(m: mode_t) bool` |
| `ISLNK` | `pub fn ISLNK(m: mode_t) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: mode_t) bool` |
| `sigemptyset` | `pub fn sigemptyset() sigset_t` |
| `atime` | `pub fn atime(self: @This() ) timespec` |
| `mtime` | `pub fn mtime(self: @This() ) timespec` |
| `ctime` | `pub fn ctime(self: @This() ) timespec` |

## os / linux

| Function | Signature |
|----------|-----------|
| `clone` | `pub fn clone(func: *const fn (arg: usize) callconv(.c) u8, stack: usize, flags: u32, arg: usize, ptid: ?*i32, tp: usize, // aka tls ctid: ?*i32, ) usize` |
| `errno` | `pub fn errno(r: usize) E` |
| `dup` | `pub fn dup(old: i32) usize` |
| `dup2` | `pub fn dup2(old: i32, new: i32) usize` |
| `dup3` | `pub fn dup3(old: i32, new: i32, flags: u32) usize` |
| `chdir` | `pub fn chdir(path: [*:0]const u8) usize` |
| `fchdir` | `pub fn fchdir(fd: fd_t) usize` |
| `chroot` | `pub fn chroot(path: [*:0]const u8) usize` |
| `execve` | `pub fn execve(path: [*:0]const u8, argv: [*:null]const ?[*:0]const u8, envp: [*:null]const ?[*:0]const u8) usize` |
| `execveat` | `pub fn execveat(dirfd: fd_t, path: [*:0]const u8, argv: [*:null]const ?[*:0]const u8, envp: [*:null]const ?[*:0]const u8, flags: EXECVEAT) usize` |
| `fork` | `pub fn fork() usize` |
| `vfork` | `pub fn vfork() usize` |
| `futimens` | `pub fn futimens(fd: i32, times: ?*const [2]timespec) usize` |
| `utimensat` | `pub fn utimensat(dirfd: i32, path: ?[*:0]const u8, times: ?*const [2]timespec, flags: u32) usize` |
| `fallocate` | `pub fn fallocate(fd: i32, mode: i32, offset: i64, length: i64) usize` |
| `futex` | `pub fn futex(uaddr: *const anyopaque, futex_op: FUTEX_OP, val: u32, val2timeout: futex_param4, uaddr2: ?*const anyopaque, val3: u32) usize` |
| `futex_3arg` | `pub fn futex_3arg(uaddr: *const anyopaque, futex_op: FUTEX_OP, val: u32) usize` |
| `futex_4arg` | `pub fn futex_4arg(uaddr: *const anyopaque, futex_op: FUTEX_OP, val: u32, timeout: ?*const timespec) usize` |
| `futex2_waitv` | `pub fn futex2_waitv(futexes: [*]const futex2_waitone, /// Length of `futexes`. Max of FUTEX2_WAITONE_MAX. nr_futexes: u32, flags: FUTEX2_FLAGS_WAITV, /// Optional absolute timeout. Always 64-bit, even on 32-bit platforms. timeout: ?*const kernel_t...` |
| `futex2_wait` | `pub fn futex2_wait(/// Address of the futex to wait on. uaddr: *const anyopaque, /// Value of `uaddr`. val: usize, /// Bitmask to match against incoming wakeup masks. Must not be zero. mask: usize, flags: FUTEX2_FLAGS, /// Optional absolute timeou...` |
| `futex2_wake` | `pub fn futex2_wake(/// Futex to wake uaddr: *const anyopaque, /// Bitmask to match against waiters. mask: usize, /// Maximum number of waiters on the futex to wake. nr_wake: i32, flags: FUTEX2_FLAGS,) usize` |
| `futex2_requeue` | `pub fn futex2_requeue(/// The source and destination futexes. Must be a 2-element array. waiters: [*]const futex2_waitone, /// Currently unused. flags: FUTEX2_FLAGS_REQUEUE, /// Maximum number of waiters to wake on the source futex. nr_wake: i32, ...` |
| `getcwd` | `pub fn getcwd(buf: [*]u8, size: usize) usize` |
| `getdents` | `pub fn getdents(fd: i32, dirp: [*]u8, len: usize) usize` |
| `getdents64` | `pub fn getdents64(fd: i32, dirp: [*]u8, len: usize) usize` |
| `inotify_init1` | `pub fn inotify_init1(flags: u32) usize` |
| `inotify_add_watch` | `pub fn inotify_add_watch(fd: i32, pathname: [*:0]const u8, mask: u32) usize` |
| `inotify_rm_watch` | `pub fn inotify_rm_watch(fd: i32, wd: i32) usize` |
| `fanotify_init` | `pub fn fanotify_init(flags: fanotify.InitFlags, event_f_flags: u32) usize` |
| `fanotify_mark` | `pub fn fanotify_mark(fd: fd_t, flags: fanotify.MarkFlags, mask: fanotify.MarkMask, dirfd: fd_t, pathname: ?[*:0]const u8,) usize` |
| `name_to_handle_at` | `pub fn name_to_handle_at(dirfd: fd_t, pathname: [*:0]const u8, handle: *std.os.linux.file_handle, mount_id: *i32, flags: u32,) usize` |
| `readlink` | `pub fn readlink(noalias path: [*:0]const u8, noalias buf_ptr: [*]u8, buf_len: usize) usize` |
| `readlinkat` | `pub fn readlinkat(dirfd: i32, noalias path: [*:0]const u8, noalias buf_ptr: [*]u8, buf_len: usize) usize` |
| `mkdir` | `pub fn mkdir(path: [*:0]const u8, mode: mode_t) usize` |
| `mkdirat` | `pub fn mkdirat(dirfd: i32, path: [*:0]const u8, mode: mode_t) usize` |
| `mknod` | `pub fn mknod(path: [*:0]const u8, mode: u32, dev: u32) usize` |
| `mknodat` | `pub fn mknodat(dirfd: i32, path: [*:0]const u8, mode: u32, dev: u32) usize` |
| `mount` | `pub fn mount(special: ?[*:0]const u8, dir: [*:0]const u8, fstype: ?[*:0]const u8, flags: u32, data: usize) usize` |
| `umount` | `pub fn umount(special: [*:0]const u8) usize` |
| `umount2` | `pub fn umount2(special: [*:0]const u8, flags: u32) usize` |
| `move_mount` | `pub fn move_mount(from_dirfd: fd_t, from_path: [*:0]const u8, to_dirfd: fd_t, to_path: [*:0]const u8, flags: MOVE_MOUNT) usize` |
| `mount_setattr` | `pub fn mount_setattr(dirfd: fd_t, path: [*:0]const u8, flags: MOUNT_ATTR) usize` |
| `fsopen` | `pub fn fsopen(fsname: [*:0]const u8, flags: FSOPEN) usize` |
| `fsconfig` | `pub fn fsconfig(fd: fd_t, cmd: FSCONFIG_CMD, key: ?[*:0]const u8, value: ?[*:0]const u8, aux: u32) usize` |
| `fsmount` | `pub fn fsmount(fsfd: fd_t, flags: FSMOUNT, attr_flags: MOUNT_ATTR) usize` |
| `fspick` | `pub fn fspick(dirfd: fd_t, path: [*:0]const u8, flags: FSPICK) usize` |
| `pivot_root` | `pub fn pivot_root(new_root: [*:0]const u8, put_old: [*:0]const u8) usize` |
| `mmap` | `pub fn mmap(address: ?[*]u8, length: usize, prot: PROT, flags: MAP, fd: i32, offset: i64) usize` |
| `mprotect` | `pub fn mprotect(address: [*]const u8, length: usize, protection: PROT) usize` |
| `mremap` | `pub fn mremap(old_addr: ?[*]const u8, old_len: usize, new_len: usize, flags: MREMAP, new_addr: ?[*]const u8) usize` |
| `mseal` | `pub fn mseal(address: [*]const u8, length: usize, flags: usize) usize` |
| `msync` | `pub fn msync(address: [*]const u8, length: usize, flags: i32) usize` |
| `munmap` | `pub fn munmap(address: [*]const u8, length: usize) usize` |
| `mlock` | `pub fn mlock(address: [*]const u8, length: usize) usize` |
| `munlock` | `pub fn munlock(address: [*]const u8, length: usize) usize` |
| `mlock2` | `pub fn mlock2(address: [*]const u8, length: usize, flags: MLOCK) usize` |
| `mlockall` | `pub fn mlockall(flags: MCL) usize` |
| `munlockall` | `pub fn munlockall() usize` |
| `poll` | `pub fn poll(fds: [*]pollfd, n: nfds_t, timeout: i32) usize` |
| `ppoll` | `pub fn ppoll(fds: [*]pollfd, n: nfds_t, timeout: ?*timespec, sigmask: ?*const sigset_t) usize` |
| `read` | `pub fn read(fd: i32, buf: [*]u8, count: usize) usize` |
| `preadv` | `pub fn preadv(fd: i32, iov: [*]const iovec, count: usize, offset: i64) usize` |
| `preadv2` | `pub fn preadv2(fd: i32, iov: [*]const iovec, count: usize, offset: i64, flags: kernel_rwf) usize` |
| `readv` | `pub fn readv(fd: i32, iov: [*]const iovec, count: usize) usize` |
| `writev` | `pub fn writev(fd: i32, iov: [*]const iovec_const, count: usize) usize` |
| `pwritev` | `pub fn pwritev(fd: i32, iov: [*]const iovec_const, count: usize, offset: i64) usize` |
| `pwritev2` | `pub fn pwritev2(fd: i32, iov: [*]const iovec_const, count: usize, offset: i64, flags: kernel_rwf) usize` |
| `rmdir` | `pub fn rmdir(path: [*:0]const u8) usize` |
| `symlink` | `pub fn symlink(existing: [*:0]const u8, new: [*:0]const u8) usize` |
| `symlinkat` | `pub fn symlinkat(existing: [*:0]const u8, newfd: i32, newpath: [*:0]const u8) usize` |
| `pread` | `pub fn pread(fd: i32, buf: [*]u8, count: usize, offset: i64) usize` |
| `access` | `pub fn access(path: [*:0]const u8, mode: u32) usize` |
| `faccessat` | `pub fn faccessat(dirfd: i32, path: [*:0]const u8, mode: u32, flags: u32) usize` |
| `acct` | `pub fn acct(path: [*:0]const u8) usize` |
| `pipe` | `pub fn pipe(fd: *[2]i32) usize` |
| `pipe2` | `pub fn pipe2(fd: *[2]i32, flags: O) usize` |
| `write` | `pub fn write(fd: i32, buf: [*]const u8, count: usize) usize` |
| `ftruncate` | `pub fn ftruncate(fd: i32, length: i64) usize` |
| `pwrite` | `pub fn pwrite(fd: i32, buf: [*]const u8, count: usize, offset: i64) usize` |
| `rename` | `pub fn rename(old: [*:0]const u8, new: [*:0]const u8) usize` |
| `renameat` | `pub fn renameat(oldfd: i32, oldpath: [*:0]const u8, newfd: i32, newpath: [*:0]const u8) usize` |
| `renameat2` | `pub fn renameat2(oldfd: i32, oldpath: [*:0]const u8, newfd: i32, newpath: [*:0]const u8, flags: RENAME) usize` |
| `open` | `pub fn open(path: [*:0]const u8, flags: O, perm: mode_t) usize` |
| `create` | `pub fn create(path: [*:0]const u8, perm: mode_t) usize` |
| `openat` | `pub fn openat(dirfd: i32, path: [*:0]const u8, flags: O, mode: mode_t) usize` |
| `clone5` | `pub fn clone5(flags: usize, child_stack_ptr: usize, parent_tid: *i32, child_tid: *i32, newtls: usize) usize` |
| `clone2` | `pub fn clone2(flags: u32, child_stack_ptr: usize) usize` |
| `close` | `pub fn close(fd: i32) usize` |
| `close_range` | `pub fn close_range(first: fd_t, last: fd_t, flags: CLOSE_RANGE) usize` |
| `fchmod` | `pub fn fchmod(fd: i32, mode: mode_t) usize` |
| `chmod` | `pub fn chmod(path: [*:0]const u8, mode: mode_t) usize` |
| `fchown` | `pub fn fchown(fd: i32, owner: uid_t, group: gid_t) usize` |
| `fchownat` | `pub fn fchownat(fd: i32, path: [*:0]const u8, owner: uid_t, group: gid_t, flags: u32) usize` |
| `chown` | `pub fn chown(path: [*:0]const u8, owner: uid_t, group: gid_t) usize` |
| `lchown` | `pub fn lchown(path: [*:0]const u8, owner: uid_t, group: gid_t) usize` |
| `fchmodat` | `pub fn fchmodat(fd: i32, path: [*:0]const u8, mode: mode_t) usize` |
| `fchmodat2` | `pub fn fchmodat2(fd: i32, path: [*:0]const u8, mode: mode_t, flags: u32) usize` |
| `llseek` | `pub fn llseek(fd: i32, offset: u64, result: ?*u64, whence: usize) usize` |
| `lseek` | `pub fn lseek(fd: i32, offset: i64, whence: usize) usize` |
| `exit` | `pub fn exit(status: i32) noreturn` |
| `exit_group` | `pub fn exit_group(status: i32) noreturn` |
| `reboot` | `pub fn reboot(magic: LINUX_REBOOT.MAGIC1, magic2: LINUX_REBOOT.MAGIC2, cmd: LINUX_REBOOT.CMD, arg: ?*const anyopaque) usize` |
| `getrandom` | `pub fn getrandom(buf: [*]u8, count: usize, flags: u32) usize` |
| `kill` | `pub fn kill(pid: pid_t, sig: SIG) usize` |
| `tkill` | `pub fn tkill(tid: pid_t, sig: SIG) usize` |
| `tgkill` | `pub fn tgkill(tgid: pid_t, tid: pid_t, sig: SIG) usize` |
| `link` | `pub fn link(oldpath: [*:0]const u8, newpath: [*:0]const u8) usize` |
| `linkat` | `pub fn linkat(oldfd: fd_t, oldpath: [*:0]const u8, newfd: fd_t, newpath: [*:0]const u8, flags: u32) usize` |
| `unlink` | `pub fn unlink(path: [*:0]const u8) usize` |
| `unlinkat` | `pub fn unlinkat(dirfd: i32, path: [*:0]const u8, flags: u32) usize` |
| `waitpid` | `pub fn waitpid(pid: pid_t, status: *u32, flags: u32) usize` |
| `wait4` | `pub fn wait4(pid: pid_t, status: *u32, flags: u32, usage: ?*rusage) usize` |
| `waitid` | `pub fn waitid(id_type: P, id: i32, infop: *siginfo_t, flags: u32, usage: ?*rusage) usize` |
| `fcntl` | `pub fn fcntl(fd: fd_t, cmd: i32, arg: usize) usize` |
| `flock` | `pub fn flock(fd: fd_t, operation: i32) usize` |
| `clock_gettime` | `pub fn clock_gettime(clk_id: clockid_t, tp: *timespec) usize` |
| `clock_getres` | `pub fn clock_getres(clk_id: clockid_t, tp: *timespec) usize` |
| `clock_settime` | `pub fn clock_settime(clk_id: clockid_t, tp: *const timespec) usize` |
| `clock_nanosleep` | `pub fn clock_nanosleep(clockid: clockid_t, flags: TIMER, request: *const timespec, remain: ?*timespec) usize` |
| `gettimeofday` | `pub fn gettimeofday(tv: ?*timeval, tz: ?*timezone) usize` |
| `settimeofday` | `pub fn settimeofday(tv: *const timeval, tz: *const timezone) usize` |
| `nanosleep` | `pub fn nanosleep(req: *const timespec, rem: ?*timespec) usize` |
| `pause` | `pub fn pause() usize` |
| `setuid` | `pub fn setuid(uid: uid_t) usize` |
| `setgid` | `pub fn setgid(gid: gid_t) usize` |
| `setreuid` | `pub fn setreuid(ruid: uid_t, euid: uid_t) usize` |
| `setregid` | `pub fn setregid(rgid: gid_t, egid: gid_t) usize` |
| `getuid` | `pub fn getuid() uid_t` |
| `getgid` | `pub fn getgid() gid_t` |
| `geteuid` | `pub fn geteuid() uid_t` |
| `getegid` | `pub fn getegid() gid_t` |
| `seteuid` | `pub fn seteuid(euid: uid_t) usize` |
| `setegid` | `pub fn setegid(egid: gid_t) usize` |
| `getresuid` | `pub fn getresuid(ruid: *uid_t, euid: *uid_t, suid: *uid_t) usize` |
| `getresgid` | `pub fn getresgid(rgid: *gid_t, egid: *gid_t, sgid: *gid_t) usize` |
| `setresuid` | `pub fn setresuid(ruid: uid_t, euid: uid_t, suid: uid_t) usize` |
| `setresgid` | `pub fn setresgid(rgid: gid_t, egid: gid_t, sgid: gid_t) usize` |
| `setpgid` | `pub fn setpgid(pid: pid_t, pgid: pid_t) usize` |
| `getpgid` | `pub fn getpgid(pid: pid_t) usize` |
| `getgroups` | `pub fn getgroups(size: usize, list: ?[*]gid_t) usize` |
| `setgroups` | `pub fn setgroups(size: usize, list: [*]const gid_t) usize` |
| `setsid` | `pub fn setsid() usize` |
| `getsid` | `pub fn getsid(pid: pid_t) usize` |
| `getpid` | `pub fn getpid() pid_t` |
| `getppid` | `pub fn getppid() pid_t` |
| `gettid` | `pub fn gettid() pid_t` |
| `sigprocmask` | `pub fn sigprocmask(flags: u32, noalias set: ?*const sigset_t, noalias oldset: ?*sigset_t) usize` |
| `sigaction` | `pub fn sigaction(sig: SIG, noalias act: ?*const Sigaction, noalias oact: ?*Sigaction) usize` |
| `sigrtmin` | `pub fn sigrtmin() u8` |
| `sigrtmax` | `pub fn sigrtmax() u8` |
| `sigemptyset` | `pub fn sigemptyset() sigset_t` |
| `sigfillset` | `pub fn sigfillset() sigset_t` |
| `sigaddset` | `pub fn sigaddset(set: *sigset_t, sig: SIG) void` |
| `sigdelset` | `pub fn sigdelset(set: *sigset_t, sig: SIG) void` |
| `sigismember` | `pub fn sigismember(set: *const sigset_t, sig: SIG) bool` |
| `getsockname` | `pub fn getsockname(fd: i32, noalias addr: *sockaddr, noalias len: *socklen_t) usize` |
| `getpeername` | `pub fn getpeername(fd: i32, noalias addr: *sockaddr, noalias len: *socklen_t) usize` |
| `socket` | `pub fn socket(domain: u32, socket_type: u32, protocol: u32) usize` |
| `setsockopt` | `pub fn setsockopt(fd: i32, level: i32, optname: u32, optval: [*]const u8, optlen: socklen_t) usize` |
| `getsockopt` | `pub fn getsockopt(fd: i32, level: i32, optname: u32, noalias optval: [*]u8, noalias optlen: *socklen_t) usize` |
| `sendmsg` | `pub fn sendmsg(fd: i32, msg: *const msghdr_const, flags: u32) usize` |
| `sendmmsg` | `pub fn sendmmsg(fd: i32, msgvec: [*]mmsghdr, vlen: u32, flags: u32) usize` |
| `connect` | `pub fn connect(fd: i32, addr: *const anyopaque, len: socklen_t) usize` |
| `recvmsg` | `pub fn recvmsg(fd: i32, msg: *msghdr, flags: u32) usize` |
| `recvmmsg` | `pub fn recvmmsg(fd: i32, msgvec: ?[*]mmsghdr, vlen: u32, flags: u32, timeout: ?*timespec) usize` |
| `recvfrom` | `pub fn recvfrom(fd: i32, noalias buf: [*]u8, len: usize, flags: u32, noalias addr: ?*sockaddr, noalias alen: ?*socklen_t,) usize` |
| `shutdown` | `pub fn shutdown(fd: i32, how: i32) usize` |
| `bind` | `pub fn bind(fd: i32, addr: *const sockaddr, len: socklen_t) usize` |
| `listen` | `pub fn listen(fd: i32, backlog: u32) usize` |
| `sendto` | `pub fn sendto(fd: i32, buf: [*]const u8, len: usize, flags: u32, addr: ?*const sockaddr, alen: socklen_t) usize` |
| `sendfile` | `pub fn sendfile(outfd: i32, infd: i32, offset: ?*i64, count: usize) usize` |
| `socketpair` | `pub fn socketpair(domain: u32, socket_type: u32, protocol: u32, fd: *[2]i32) usize` |
| `accept` | `pub fn accept(fd: i32, noalias addr: ?*sockaddr, noalias len: ?*socklen_t) usize` |
| `accept4` | `pub fn accept4(fd: i32, noalias addr: ?*sockaddr, noalias len: ?*socklen_t, flags: u32) usize` |
| `statx` | `pub fn statx(dirfd: i32, path: [*:0]const u8, flags: u32, mask: STATX, statx_buf: *Statx) usize` |
| `listxattr` | `pub fn listxattr(path: [*:0]const u8, list: [*]u8, size: usize) usize` |
| `llistxattr` | `pub fn llistxattr(path: [*:0]const u8, list: [*]u8, size: usize) usize` |
| `flistxattr` | `pub fn flistxattr(fd: fd_t, list: [*]u8, size: usize) usize` |
| `getxattr` | `pub fn getxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `lgetxattr` | `pub fn lgetxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `fgetxattr` | `pub fn fgetxattr(fd: fd_t, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `setxattr` | `pub fn setxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]const u8, size: usize, flags: usize) usize` |
| `lsetxattr` | `pub fn lsetxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]const u8, size: usize, flags: usize) usize` |
| `fsetxattr` | `pub fn fsetxattr(fd: fd_t, name: [*:0]const u8, value: [*]const u8, size: usize, flags: usize) usize` |
| `removexattr` | `pub fn removexattr(path: [*:0]const u8, name: [*:0]const u8) usize` |
| `lremovexattr` | `pub fn lremovexattr(path: [*:0]const u8, name: [*:0]const u8) usize` |
| `fremovexattr` | `pub fn fremovexattr(fd: usize, name: [*:0]const u8) usize` |
| `sched_setparam` | `pub fn sched_setparam(pid: pid_t, param: *const sched_param) usize` |
| `sched_getparam` | `pub fn sched_getparam(pid: pid_t, param: *sched_param) usize` |
| `sched_setscheduler` | `pub fn sched_setscheduler(pid: pid_t, policy: SCHED, param: *const sched_param) usize` |
| `sched_getscheduler` | `pub fn sched_getscheduler(pid: pid_t) usize` |
| `sched_get_priority_max` | `pub fn sched_get_priority_max(policy: SCHED) usize` |
| `sched_get_priority_min` | `pub fn sched_get_priority_min(policy: SCHED) usize` |
| `getcpu` | `pub fn getcpu(cpu: ?*usize, node: ?*usize) usize` |
| `sched_setattr` | `pub fn sched_setattr(pid: pid_t, attr: *const sched_attr, flags: usize) usize` |
| `sched_getattr` | `pub fn sched_getattr(pid: pid_t, attr: *sched_attr, size: usize, flags: usize) usize` |
| `sched_rr_get_interval` | `pub fn sched_rr_get_interval(pid: pid_t, tp: *timespec) usize` |
| `sched_yield` | `pub fn sched_yield() usize` |
| `sched_getaffinity` | `pub fn sched_getaffinity(pid: pid_t, size: usize, set: *cpu_set_t) usize` |
| `sched_setaffinity` | `pub fn sched_setaffinity(pid: pid_t, set: *const cpu_set_t) !void` |
| `epoll_create` | `pub fn epoll_create() usize` |
| `epoll_create1` | `pub fn epoll_create1(flags: usize) usize` |
| `epoll_ctl` | `pub fn epoll_ctl(epoll_fd: i32, op: u32, fd: i32, ev: ?*epoll_event) usize` |
| `epoll_wait` | `pub fn epoll_wait(epoll_fd: i32, events: [*]epoll_event, maxevents: u32, timeout: i32) usize` |
| `epoll_pwait` | `pub fn epoll_pwait(epoll_fd: i32, events: [*]epoll_event, maxevents: u32, timeout: i32, sigmask: ?*const sigset_t) usize` |
| `eventfd` | `pub fn eventfd(count: u32, flags: u32) usize` |
| `timerfd_create` | `pub fn timerfd_create(clockid: timerfd_clockid_t, flags: TFD) usize` |
| `timerfd_gettime` | `pub fn timerfd_gettime(fd: i32, curr_value: *itimerspec) usize` |
| `timerfd_settime` | `pub fn timerfd_settime(fd: i32, flags: TFD.TIMER, new_value: *const itimerspec, old_value: ?*itimerspec) usize` |
| `getitimer` | `pub fn getitimer(which: i32, curr_value: *itimerspec) usize` |
| `setitimer` | `pub fn setitimer(which: i32, new_value: *const itimerspec, old_value: ?*itimerspec) usize` |
| `unshare` | `pub fn unshare(flags: usize) usize` |
| `setns` | `pub fn setns(fd: fd_t, flags: u32) usize` |
| `capget` | `pub fn capget(hdrp: *cap_user_header_t, datap: *cap_user_data_t) usize` |
| `capset` | `pub fn capset(hdrp: *cap_user_header_t, datap: *const cap_user_data_t) usize` |
| `sigaltstack` | `pub fn sigaltstack(ss: ?*const stack_t, old_ss: ?*stack_t) usize` |
| `uname` | `pub fn uname(uts: *utsname) usize` |
| `io_uring_setup` | `pub fn io_uring_setup(entries: u32, p: *io_uring_params) usize` |
| `io_uring_enter` | `pub fn io_uring_enter(fd: i32, to_submit: u32, min_complete: u32, flags: u32, sig: ?*sigset_t) usize` |
| `io_uring_register` | `pub fn io_uring_register(fd: i32, opcode: IORING_REGISTER, arg: ?*const anyopaque, nr_args: u32) usize` |
| `memfd_create` | `pub fn memfd_create(name: [*:0]const u8, flags: u32) usize` |
| `getrusage` | `pub fn getrusage(who: i32, usage: *rusage) usize` |
| `tcgetattr` | `pub fn tcgetattr(fd: fd_t, termios_p: *termios) usize` |
| `tcsetattr` | `pub fn tcsetattr(fd: fd_t, optional_action: TCSA, termios_p: *const termios) usize` |
| `tcgetpgrp` | `pub fn tcgetpgrp(fd: fd_t, pgrp: *pid_t) usize` |
| `tcsetpgrp` | `pub fn tcsetpgrp(fd: fd_t, pgrp: *const pid_t) usize` |
| `tcdrain` | `pub fn tcdrain(fd: fd_t) usize` |
| `ioctl` | `pub fn ioctl(fd: fd_t, request: u32, arg: usize) usize` |
| `signalfd` | `pub fn signalfd(fd: fd_t, mask: *const sigset_t, flags: u32) usize` |
| `copy_file_range` | `pub fn copy_file_range(fd_in: fd_t, off_in: ?*i64, fd_out: fd_t, off_out: ?*i64, len: usize, flags: u32) usize` |
| `bpf` | `pub fn bpf(cmd: BPF.Cmd, attr: *BPF.Attr, size: u32) usize` |
| `sync` | `pub fn sync() void` |
| `syncfs` | `pub fn syncfs(fd: fd_t) usize` |
| `fsync` | `pub fn fsync(fd: fd_t) usize` |
| `fdatasync` | `pub fn fdatasync(fd: fd_t) usize` |
| `prctl` | `pub fn prctl(option: i32, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `getrlimit` | `pub fn getrlimit(resource: rlimit_resource, rlim: *rlimit) usize` |
| `setrlimit` | `pub fn setrlimit(resource: rlimit_resource, rlim: *const rlimit) usize` |
| `prlimit` | `pub fn prlimit(pid: pid_t, resource: rlimit_resource, new_limit: ?*const rlimit, old_limit: ?*rlimit) usize` |
| `mincore` | `pub fn mincore(address: [*]u8, len: usize, vec: [*]u8) usize` |
| `madvise` | `pub fn madvise(address: [*]u8, len: usize, advice: u32) usize` |
| `pidfd_open` | `pub fn pidfd_open(pid: pid_t, flags: u32) usize` |
| `pidfd_getfd` | `pub fn pidfd_getfd(pidfd: fd_t, targetfd: fd_t, flags: u32) usize` |
| `pidfd_send_signal` | `pub fn pidfd_send_signal(pidfd: fd_t, sig: SIG, info: ?*siginfo_t, flags: u32) usize` |
| `process_vm_readv` | `pub fn process_vm_readv(pid: pid_t, local: []const iovec, remote: []const iovec_const, flags: usize) usize` |
| `process_vm_writev` | `pub fn process_vm_writev(pid: pid_t, local: []const iovec_const, remote: []const iovec_const, flags: usize) usize` |
| `fadvise` | `pub fn fadvise(fd: fd_t, offset: i64, len: i64, advice: usize) usize` |
| `perf_event_open` | `pub fn perf_event_open(attr: *perf_event_attr, pid: pid_t, cpu: i32, group_fd: fd_t, flags: usize,) usize` |
| `seccomp` | `pub fn seccomp(operation: u32, flags: u32, args: ?*const anyopaque) usize` |
| `ptrace` | `pub fn ptrace(req: u32, pid: pid_t, addr: usize, data: usize, addr2: usize,) usize` |
| `cachestat` | `pub fn cachestat(/// The open file descriptor to retrieve statistics from. fd: fd_t, /// The byte range in `fd` to query. /// When `len > 0`, the range is `[off..off + len]`. /// When `len` == 0, the range is from `off` to the end of `fd`. cstat_r...` |
| `map_shadow_stack` | `pub fn map_shadow_stack(addr: u64, size: u64, flags: u32) usize` |
| `sysinfo` | `pub fn sysinfo(info: *Sysinfo) usize` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) SIG` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `TOS` | `pub fn TOS(t: anytype) @TypeOf(t)` |
| `PREC` | `pub fn PREC(t: anytype) @TypeOf(t)` |
| `T` | `pub fn T(t: anytype) @TypeOf(t)` |
| `ISREG` | `pub fn ISREG(m: mode_t) bool` |
| `ISDIR` | `pub fn ISDIR(m: mode_t) bool` |
| `ISCHR` | `pub fn ISCHR(m: mode_t) bool` |
| `ISBLK` | `pub fn ISBLK(m: mode_t) bool` |
| `ISFIFO` | `pub fn ISFIFO(m: mode_t) bool` |
| `ISLNK` | `pub fn ISLNK(m: mode_t) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: mode_t) bool` |
| `valid` | `pub fn valid(x: u8) bool` |
| `TO_MASK` | `pub fn TO_MASK(cap: u8) u32` |
| `TO_INDEX` | `pub fn TO_INDEX(cap: u8) u8` |
| `getName` | `pub fn getName(self: *const inotify_event) ?[:0]const u8` |
| `CPU_COUNT` | `pub fn CPU_COUNT(set: cpu_set_t) cpu_count_t` |
| `err` | `pub fn err(self: io_uring_cqe) E` |
| `buffer_id` | `pub fn buffer_id(self: io_uring_cqe) !u16` |
| `is_supported` | `pub fn is_supported(self: @This() ) bool` |
| `is_supported` | `pub fn is_supported(self: @This() , op: IORING_OP) bool` |

## os / plan9

| Function | Signature |
|----------|-----------|
| `errno` | `pub fn errno(r: usize) E` |
| `errstr` | `pub fn errstr() []const u8` |
| `getpid` | `pub fn getpid() u32` |
| `sigemptyset` | `pub fn sigemptyset() sigset_t` |
| `sigaction` | `pub fn sigaction(sig: u6, noalias act: ?*const Sigaction, noalias oact: ?*Sigaction) usize` |
| `write` | `pub fn write(fd: i32, buf: [*]const u8, count: usize) usize` |
| `pwrite` | `pub fn pwrite(fd: i32, buf: [*]const u8, count: usize, offset: isize) usize` |
| `read` | `pub fn read(fd: i32, buf: [*]const u8, count: usize) usize` |
| `pread` | `pub fn pread(fd: i32, buf: [*]const u8, count: usize, offset: isize) usize` |
| `open` | `pub fn open(path: [*:0]const u8, flags: u32) usize` |
| `openat` | `pub fn openat(dirfd: i32, path: [*:0]const u8, flags: u32, _: mode_t) usize` |
| `fd2path` | `pub fn fd2path(fd: i32, buf: [*]u8, nbuf: usize) usize` |
| `create` | `pub fn create(path: [*:0]const u8, omode: mode_t, perms: usize) usize` |
| `exit` | `pub fn exit(status: u8) noreturn` |
| `exits` | `pub fn exits(status: ?[*:0]const u8) noreturn` |
| `close` | `pub fn close(fd: i32) usize` |
| `brk_` | `pub fn brk_(addr: usize) i32` |
| `sbrk` | `pub fn sbrk(n: usize) usize` |

## os / uefi

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format(self: Guid, writer: *std.Io.Writer) std.Io.Writer.Error!void` |
| `eql` | `pub fn eql(a: Guid, b: Guid) bool` |
| `toEpoch` | `pub fn toEpoch(self: std.os.uefi.Time) u64` |
| `unexpectedStatus` | `pub fn unexpectedStatus(status: Status) UnexpectedError` |

## os / windows

| Function | Signature |
|----------|-----------|
| `getVolumeLabel` | `pub fn getVolumeLabel(fvi: *const FS_VOLUME_INFORMATION) []const WCHAR` |
| `fileName` | `pub fn fileName(info: *INFORMATION) []WCHAR` |
| `init` | `pub fn init(opts: struct { Timeout: ?LARGE_INTEGER = null, Name: []const WCHAR, }) WAIT_FOR_BUFFER` |
| `getName` | `pub fn getName(fpwfb: *const WAIT_FOR_BUFFER) []const WCHAR` |
| `toBuffer` | `pub fn toBuffer(fpwfb: *const WAIT_FOR_BUFFER) []const u8` |
| `init` | `pub fn init(opts: struct { Flags: FLAGS = .{}, RootDirectory: ?HANDLE = null, FileName: []const WCHAR, }) RENAME_INFORMATION` |
| `getFileName` | `pub fn getFileName(ri: *const RENAME_INFORMATION) []const WCHAR` |
| `toBuffer` | `pub fn toBuffer(fri: *RENAME_INFORMATION) []u8` |
| `GET_CP` | `pub fn GET_CP(mode: INFO.CP.MODE) Header.With(INFO.CP)` |
| `SET_MODE` | `pub fn SET_MODE(mode: DWORD) Header.With(DWORD)` |
| `WRITE` | `pub fn WRITE(mode: INFO.WRITE.MODE) Header.With(INFO.WRITE)` |
| `FILL` | `pub fn FILL(with: INFO.FILL.WITH, len: DWORD, coord: COORD) Header.With(INFO.FILL)` |
| `SET_CP` | `pub fn SET_CP(mode: INFO.CP.MODE, cp: UINT) Header.With(INFO.CP)` |
| `SET_CURSOR_POSITION` | `pub fn SET_CURSOR_POSITION(coord: COORD) Header.With(COORD)` |
| `SET_TEXT_ATTRIBUTE` | `pub fn SET_TEXT_ATTRIBUTE(attribute: WORD) Header.With(WORD)` |
| `READ_OUTPUT_CHARACTER` | `pub fn READ_OUTPUT_CHARACTER(coord: COORD, mode: INFO.READ_OUTPUT_CHARACTER.MODE,) Header.With(INFO.READ_OUTPUT_CHARACTER)` |
| `Request` | `pub fn Request(comptime in_len: u32, comptime out_len: u32) type` |
| `init` | `pub fn init(handle: ?HANDLE, in: [in_len]InputBuffer, out: [out_len]OutputBuffer,) @This()` |
| `With` | `pub fn With(comptime Data: type) type` |
| `init` | `pub fn init(operation: Operation, data: Data) @This()` |
| `request` | `pub fn request(with: *@This() , file: ?Io.File, comptime in_len: u32, in: [in_len]InputBuffer, comptime out_len: u32, out: [out_len]OutputBuffer, ) Request(1 + in_len, 1 + out_len)` |
| `operate` | `pub fn operate(with: *@This() , io: Io, file: ?Io.File) Io.Cancelable!NTSTATUS` |
| `WCI` | `pub fn WCI(index: u1) IO_REPARSE_TAG` |
| `CLOUD` | `pub fn CLOUD(index: u4) IO_REPARSE_TAG` |
| `WCI_LINK` | `pub fn WCI_LINK(index: u1) IO_REPARSE_TAG` |
| `fromProtection` | `pub fn fromProtection(protection: std.process.MemoryProtection) ?PAGE` |
| `GetProcessHeap` | `pub fn GetProcessHeap() ?*HEAP` |
| `GetCurrentProcess` | `pub fn GetCurrentProcess() HANDLE` |
| `GetCurrentProcessId` | `pub fn GetCurrentProcessId() DWORD` |
| `GetCurrentThread` | `pub fn GetCurrentThread() HANDLE` |
| `GetCurrentThreadId` | `pub fn GetCurrentThreadId() DWORD` |
| `GetLastError` | `pub fn GetLastError() Win32Error` |
| `CloseHandle` | `pub fn CloseHandle(hObject: HANDLE) void` |
| `teb` | `pub fn teb() *TEB` |
| `peb` | `pub fn peb() *PEB` |
| `fromSysTime` | `pub fn fromSysTime(hns: i64) Io.Timestamp` |
| `toSysTime` | `pub fn toSysTime(ns: Io.Timestamp) i64` |
| `toUpperWtf16` | `pub fn toUpperWtf16(c: u16) u16` |
| `eqlIgnoreCaseWtf16` | `pub fn eqlIgnoreCaseWtf16(a: []const u16, b: []const u16) bool` |
| `eqlIgnoreCaseWtf8` | `pub fn eqlIgnoreCaseWtf8(a: []const u8, b: []const u8) bool` |
| `removeDotDirsSanitized` | `pub fn removeDotDirsSanitized(comptime T: type, path: []T) RemoveDotDirsError!usize` |
| `normalizePath` | `pub fn normalizePath(comptime T: type, path: []T) RemoveDotDirsError!usize` |
| `hasCommonNtPrefix` | `pub fn hasCommonNtPrefix(comptime T: type, path: []const T) bool` |
| `ntToWin32Namespace` | `pub fn ntToWin32Namespace(path: []const u16, out: []u16) error` |
| `unexpectedError` | `pub fn unexpectedError(err: Win32Error) UnexpectedError` |
| `unexpectedStatus` | `pub fn unexpectedStatus(status: NTSTATUS) UnexpectedError` |
| `statusBug` | `pub fn statusBug(status: NTSTATUS) UnexpectedError` |
| `errorBug` | `pub fn errorBug(err: Win32Error) UnexpectedError` |
| `init` | `pub fn init(string: []const C) @This()` |
| `isEmpty` | `pub fn isEmpty(string: *const @This() ) bool` |
| `slice` | `pub fn slice(string: *const @This() ) []C` |
| `sliceZ` | `pub fn sliceZ(string: *const @This() ) [:0]C` |
| `parse` | `pub fn parse(s: []const u8) GUID` |
| `parseNoBraces` | `pub fn parseNoBraces(s: []const u8) !GUID` |
| `getRegs` | `pub fn getRegs(ctx: *const CONTEXT) struct` |
| `setIp` | `pub fn setIp(ctx: *CONTEXT, ip: usize) void` |
| `setSp` | `pub fn setSp(ctx: *CONTEXT, sp: usize) void` |
| `FileInformationIterator` | `pub fn FileInformationIterator(comptime FileInformationType: type) type` |
| `next` | `pub fn next(self: *@This() ) ?*FileInformationType` |
| `IsProcessorFeaturePresent` | `pub fn IsProcessorFeaturePresent(feature: PF) bool` |
| `wtf8ToWtf16Le` | `pub fn wtf8ToWtf16Le(wtf16le: []u16, wtf8: []const u8) error` |

## os / windows / nls

| Function | Signature |
|----------|-----------|
| `upcaseW` | `pub fn upcaseW(c: u16) u16` |

## os / uefi / device_path

| Function | Signature |
|----------|-----------|
| `adrs` | `pub fn adrs(self: *const AdrDevicePath) []align(1) const u32` |
| `serial_number` | `pub fn serial_number(self: *const UsbWwidDevicePath) []align(1) const u16` |
| `getPath` | `pub fn getPath(self: *const FilePathDevicePath) [*:0]align(1) const u16` |
| `getDescription` | `pub fn getDescription(self: *const BBS101DevicePath) [*:0]const u8` |

## os / uefi / hii

| Function | Signature |
|----------|-----------|
| `getNarrowGlyphs` | `pub fn getNarrowGlyphs(self: *SimplifiedFontPackage) []NarrowGlyph` |

## os / uefi / status

| Function | Signature |
|----------|-----------|
| `err` | `pub fn err(self: Status) Error!void` |
| `fromError` | `pub fn fromError(e: Error) Status` |

## os / uefi / tables

| Function | Signature |
|----------|-----------|
| `fromOem` | `pub fn fromOem(value: Oem) MemoryType` |
| `toOem` | `pub fn toOem(memtype: MemoryType) ?Oem` |
| `fromVendor` | `pub fn fromVendor(value: Vendor) MemoryType` |
| `toVendor` | `pub fn toVendor(memtype: MemoryType) ?Vendor` |
| `format` | `pub fn format(self: MemoryType, w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `iterator` | `pub fn iterator(self: MemoryMapSlice) MemoryDescriptorIterator` |
| `get` | `pub fn get(self: MemoryMapSlice, index: usize) ?*MemoryDescriptor` |
| `getUnchecked` | `pub fn getUnchecked(self: MemoryMapSlice, index: usize) *MemoryDescriptor` |
| `next` | `pub fn next(self: *MemoryDescriptorIterator) ?*MemoryDescriptor` |
| `fromBits` | `pub fn fromBits(bits: Bits) OpenProtocolAttributes` |
| `toBits` | `pub fn toBits(self: OpenProtocolAttributes) Bits` |

## os / uefi / tables / boot_services

| Function | Signature |
|----------|-----------|
| `allocatePages` | `pub fn allocatePages(self: *BootServices, location: AllocateLocation, mem_type: MemoryType, pages: usize,) AllocatePagesError![]align(4096) Page` |
| `freePages` | `pub fn freePages(self: *BootServices, pages: []align(4096) Page) FreePagesError!void` |
| `getMemoryMapInfo` | `pub fn getMemoryMapInfo(self: *const BootServices) uefi.UnexpectedError!MemoryMapInfo` |
| `getMemoryMap` | `pub fn getMemoryMap(self: *const BootServices, buffer: []align(@alignOf(MemoryDescriptor) ) u8, ) GetMemoryMapError!MemoryMapSlice` |
| `allocatePool` | `pub fn allocatePool(self: *BootServices, pool_type: MemoryType, size: usize,) AllocatePoolError![]align(8) u8` |
| `freePool` | `pub fn freePool(self: *BootServices, ptr: [*]align(8) u8) FreePoolError!void` |
| `createEvent` | `pub fn createEvent(self: *BootServices, event_type: uefi.EventType, notify_opts: NotifyOpts,) CreateEventError!Event` |
| `setTimer` | `pub fn setTimer(self: *BootServices, event: Event, @"type": TimerDelay, trigger_time: u64,) SetTimerError!void` |
| `waitForEvent` | `pub fn waitForEvent(self: *BootServices, events: []const Event,) WaitForEventError!struct` |
| `signalEvent` | `pub fn signalEvent(self: *BootServices, event: Event) uefi.UnexpectedError!void` |
| `closeEvent` | `pub fn closeEvent(self: *BootServices, event: Event) uefi.UnexpectedError!void` |
| `checkEvent` | `pub fn checkEvent(self: *BootServices, event: Event) CheckEventError!bool` |
| `installProtocolInterface` | `pub fn installProtocolInterface(self: *BootServices, handle: ?Handle, interface: anytype,) InstallProtocolInterfacesError!Handle` |
| `reinstallProtocolInterface` | `pub fn reinstallProtocolInterface(self: *BootServices, handle: Handle, Protocol: type, old: ?*const Protocol, new: ?*const Protocol,) ReinstallProtocolInterfaceError!void` |
| `uninstallProtocolInterface` | `pub fn uninstallProtocolInterface(self: *BootServices, handle: Handle, interface: anytype,) UninstallProtocolInterfacesError!void` |
| `handleProtocol` | `pub fn handleProtocol(self: *BootServices, Protocol: type, handle: Handle,) HandleProtocolError!?*Protocol` |
| `registerProtocolNotify` | `pub fn registerProtocolNotify(self: *BootServices, Protocol: type, event: Event,) RegisterProtocolNotifyError!EventRegistration` |
| `locateHandleLen` | `pub fn locateHandleLen(self: *const BootServices, search: LocateSearch) NumHandlesError!usize` |
| `locateHandle` | `pub fn locateHandle(self: *BootServices, search: LocateSearch, buffer: []Handle,) LocateHandleError![]Handle` |
| `locateDevicePath` | `pub fn locateDevicePath(self: *const BootServices, device_path: *const DevicePathProtocol, Protocol: type,) LocateHandleError!?struct` |
| `installConfigurationTable` | `pub fn installConfigurationTable(self: *BootServices, guid: *const Guid, table: *anyopaque,) InstallConfigurationTableError!void` |
| `uninstallConfigurationTable` | `pub fn uninstallConfigurationTable(self: *BootServices, guid: *const Guid,) UninstallConfigurationTableError!void` |
| `loadImage` | `pub fn loadImage(self: *BootServices, boot_policy: bool, parent_image: Handle, source: LoadImageSource,) LoadImageError!Handle` |
| `startImage` | `pub fn startImage(self: *BootServices, image: Handle) StartImageError!ImageExitData` |
| `exit` | `pub fn exit(self: *BootServices, handle: Handle, status: Status, message: ?[:0]const u16,) ExitError!void` |
| `exitWithData` | `pub fn exitWithData(self: *BootServices, handle: Handle, status: Status, data: []align(2) const u8, ) ExitError!void` |
| `unloadImage` | `pub fn unloadImage(self: *BootServices, image: Handle,) Status.Error!Status` |
| `exitBootServices` | `pub fn exitBootServices(self: *BootServices, image: Handle, map_key: MemoryMapKey,) ExitBootServicesError!void` |
| `getNextMonotonicCount` | `pub fn getNextMonotonicCount(self: *const BootServices, count: *u64,) GetNextMonotonicCountError!void` |
| `stall` | `pub fn stall(self: *const BootServices, microseconds: usize) uefi.UnexpectedError!void` |
| `setWatchdogTimer` | `pub fn setWatchdogTimer(self: *BootServices, timeout: usize, watchdog_code: u64, data: ?[]const u16,) SetWatchdogTimerError!void` |
| `connectController` | `pub fn connectController(self: *BootServices, controller: Handle, driver_image: ?[*:null]?Handle, remaining_device_path: ?*const DevicePathProtocol, recursive: bool,) ConnectControllerError!void` |
| `disconnectController` | `pub fn disconnectController(self: *BootServices, controller: Handle, driver_image: ?Handle, child: ?Handle,) DisconnectControllerError!void` |
| `openProtocol` | `pub fn openProtocol(self: *BootServices, Protocol: type, handle: Handle, attributes: OpenProtocolArgs,) OpenProtocolError!?*Protocol` |
| `closeProtocol` | `pub fn closeProtocol(self: *BootServices, handle: Handle, Protocol: type, agent: Handle, controller: ?Handle,) CloseProtocolError!void` |
| `openProtocolInformation` | `pub fn openProtocolInformation(self: *const BootServices, handle: Handle, Protocol: type,) OpenProtocolInformationError!?[]ProtocolInformationEntry` |
| `protocolsPerHandle` | `pub fn protocolsPerHandle(self: *const BootServices, handle: Handle,) ProtocolsPerHandleError![]*const Guid` |
| `locateHandleBuffer` | `pub fn locateHandleBuffer(self: *const BootServices, search: LocateSearch,) LocateHandleBufferError!?[]Handle` |
| `locateProtocol` | `pub fn locateProtocol(self: *const BootServices, Protocol: type, registration: ?EventRegistration,) LocateProtocolError!?*Protocol` |
| `installProtocolInterfaces` | `pub fn installProtocolInterfaces(self: *BootServices, handle: ?Handle, interfaces: anytype,) InstallProtocolInterfacesError!Handle` |
| `uninstallProtocolInterfaces` | `pub fn uninstallProtocolInterfaces(self: *BootServices, handle: Handle, interfaces: anytype,) UninstallProtocolInterfacesError!void` |
| `calculateCrc32` | `pub fn calculateCrc32(self: *const BootServices, data: []const u8,) CalculateCrc32Error!u32` |

## os / uefi / tables / runtime_services

| Function | Signature |
|----------|-----------|
| `getTime` | `pub fn getTime(self: *const RuntimeServices,) GetTimeError!struct` |
| `setTime` | `pub fn setTime(self: *RuntimeServices, time: *const Time) SetTimeError!void` |
| `getWakeupTime` | `pub fn getWakeupTime(self: *const RuntimeServices,) GetWakeupTimeError!GetWakeupTime` |
| `setWakeupTime` | `pub fn setWakeupTime(self: *RuntimeServices, set: SetWakeupTime,) SetWakeupTimeError!void` |
| `setVirtualAddressMap` | `pub fn setVirtualAddressMap(self: *RuntimeServices, map: MemoryMapSlice,) SetVirtualAddressMapError!void` |
| `convertPointer` | `pub fn convertPointer(self: *const RuntimeServices, comptime disposition: DebugDisposition, cvt: @FieldType(PointerConversion, @tagName(disposition) ), ) ConvertPointerError!?@FieldType(PointerConversion, @tagName(disposition))` |
| `getVariableSize` | `pub fn getVariableSize(self: *const RuntimeServices, name: [*:0]const u16, guid: *const Guid,) GetVariableSizeError!?struct` |
| `getVariable` | `pub fn getVariable(self: *const RuntimeServices, name: [*:0]const u16, guid: *const Guid, buffer: []u8,) GetVariableError!?struct` |
| `variableNameIterator` | `pub fn variableNameIterator(self: *const RuntimeServices, buffer: []u16,) VariableNameIterator` |
| `setVariable` | `pub fn setVariable(self: *RuntimeServices, name: [*:0]const u16, guid: *const Guid, attributes: VariableAttributes, data: []const u8,) SetVariableError!void` |
| `getNextHighMonotonicCount` | `pub fn getNextHighMonotonicCount(self: *const RuntimeServices) GetNextHighMonotonicCountError!u32` |
| `resetSystem` | `pub fn resetSystem(self: *RuntimeServices, reset_type: ResetType, reset_status: Status, data: ?[]align(2) const u8, ) noreturn` |
| `updateCapsule` | `pub fn updateCapsule(self: *RuntimeServices, capsules: []*const CapsuleHeader, scatter_gather_list: PhysicalAddress,) UpdateCapsuleError!void` |
| `queryCapsuleCapabilities` | `pub fn queryCapsuleCapabilities(self: *const RuntimeServices, capsules: []*const CapsuleHeader,) QueryCapsuleCapabilitiesError!struct` |
| `queryVariableInfo` | `pub fn queryVariableInfo(self: *const RuntimeServices, // Note: .append_write is ignored attributes: VariableAttributes,) QueryVariableInfoError!VariableInfo` |
| `payloadConst` | `pub fn payloadConst(self: *const VariableAuthentication3) []const u8` |
| `payload` | `pub fn payload(self: *VariableAuthentication3) []u8` |
| `nextSize` | `pub fn nextSize(self: *VariableNameIterator) NextSizeError!?usize` |
| `next` | `pub fn next(self: *VariableNameIterator,) IterateVariableNameError!?[:0]const u16` |

## os / uefi / protocol / absolute_pointer

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *AbsolutePointer, verify: bool) ResetError!void` |
| `getState` | `pub fn getState(self: *const AbsolutePointer) GetStateError!State` |

## os / uefi / protocol / block_io

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *Self, extended_verification: bool) ResetError!void` |
| `readBlocks` | `pub fn readBlocks(self: *Self, media_id: u32, lba: u64, buf: []u8) ReadBlocksError!void` |
| `writeBlocks` | `pub fn writeBlocks(self: *Self, media_id: u32, lba: u64, buf: []const u8) WriteBlocksError!void` |
| `flushBlocks` | `pub fn flushBlocks(self: *Self) FlushBlocksError!void` |

## os / uefi / protocol / device_path

| Function | Signature |
|----------|-----------|
| `next` | `pub fn next(self: *const DevicePath) ?*const DevicePath` |
| `size` | `pub fn size(self: *const DevicePath) usize` |
| `createFileDevicePath` | `pub fn createFileDevicePath(self: *const DevicePath, allocator: Allocator, path: []const u16,) CreateFileDevicePathError!*const DevicePath` |
| `getDevicePath` | `pub fn getDevicePath(self: *const DevicePath) ?uefi.DevicePath` |
| `initSubtype` | `pub fn initSubtype(self: *const DevicePath, comptime TUnion: type) ?TUnion` |

## os / uefi / protocol / edid

| Function | Signature |
|----------|-----------|
| `getEdid` | `pub fn getEdid(self: *const Override, handle: Handle) GetEdidError!Edid` |

## os / uefi / protocol / file

| Function | Signature |
|----------|-----------|
| `open` | `pub fn open(self: *const File, file_name: [*:0]const u16, mode: OpenMode, create_attributes: Attributes,) OpenError!*File` |
| `close` | `pub fn close(self: *File) CloseError!void` |
| `delete` | `pub fn delete(self: *File) uefi.UnexpectedError!bool` |
| `read` | `pub fn read(self: *File, buffer: []u8) ReadError!usize` |
| `write` | `pub fn write(self: *File, buffer: []const u8) WriteError!usize` |
| `getPosition` | `pub fn getPosition(self: *const File) SeekError!u64` |
| `setPosition` | `pub fn setPosition(self: *File, position: u64) SeekError!void` |
| `getInfoSize` | `pub fn getInfoSize(self: *const File, comptime info: std.meta.Tag(Info) ) GetInfoError!usize` |
| `getInfo` | `pub fn getInfo(self: *const File, comptime info: std.meta.Tag(Info) , buffer: []align(@alignOf(@FieldType(Info, @tagName(info)))) u8, ) GetInfoError!*@FieldType(Info, @tagName(info))` |
| `setInfo` | `pub fn setInfo(self: *File, comptime info: std.meta.Tag(Info) , data: *const @FieldType(Info, @tagName(info)), ) SetInfoError!void` |
| `flush` | `pub fn flush(self: *File) FlushError!void` |
| `getFileName` | `pub fn getFileName(self: *const Info.File) [*:0]const u16` |
| `getVolumeLabel` | `pub fn getVolumeLabel(self: *const FileSystem) [*:0]const u16` |
| `getVolumeLabel` | `pub fn getVolumeLabel(self: *const VolumeLabel) [*:0]const u16` |

## os / uefi / protocol / graphics_output

| Function | Signature |
|----------|-----------|
| `queryMode` | `pub fn queryMode(self: *const GraphicsOutput, mode_id: u32) QueryModeError!*Mode.Info` |
| `setMode` | `pub fn setMode(self: *GraphicsOutput, mode_id: u32) SetModeError!void` |
| `blt` | `pub fn blt(self: *GraphicsOutput, blt_buffer: ?[*]BltPixel, blt_operation: BltOperation, source_x: usize, source_y: usize, destination_x: usize, destination_y: usize, width: usize, height: usize, delta: usize,) BltError!void` |

## os / uefi / protocol / hii_database

| Function | Signature |
|----------|-----------|
| `removePackageList` | `pub fn removePackageList(self: *HiiDatabase, handle: hii.Handle) !void` |
| `updatePackageList` | `pub fn updatePackageList(self: *HiiDatabase, handle: hii.Handle, buffer: *const hii.PackageList,) UpdatePackageListError!void` |
| `listPackageLists` | `pub fn listPackageLists(self: *const HiiDatabase, package_type: u8, package_guid: ?*const Guid, handles: []hii.Handle,) ListPackageListsError![]hii.Handle` |
| `exportPackageLists` | `pub fn exportPackageLists(self: *const HiiDatabase, handle: ?hii.Handle, buffer: []hii.PackageList,) ExportPackageListError![]hii.PackageList` |

## os / uefi / protocol / hii_popup

| Function | Signature |
|----------|-----------|
| `createPopup` | `pub fn createPopup(self: *const HiiPopup, style: PopupStyle, popup_type: PopupType, handle: hii.Handle, msg: u16,) CreatePopupError!PopupSelection` |

## os / uefi / protocol / ip6

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const Ip6) GetModeDataError!ModeData` |
| `configure` | `pub fn configure(self: *Ip6, ip6_config_data: *const Config) ConfigureError!void` |
| `disable` | `pub fn disable(self: *Ip6) ConfigureError!void` |
| `leaveAllGroups` | `pub fn leaveAllGroups(self: *Ip6) GroupsError!void` |
| `groups` | `pub fn groups(self: *Ip6, join_flag: JoinFlag, group_address: *const Address,) GroupsError!void` |
| `routes` | `pub fn routes(self: *Ip6, delete_route: DeleteFlag, destination: ?*const Address, prefix_length: u8, gateway_address: ?*const Address,) RoutesError!void` |
| `neighbors` | `pub fn neighbors(self: *Ip6, delete_flag: DeleteFlag, target_ip6_address: *const Address, target_link_address: ?*const MacAddress, timeout: u32, override: bool,) NeighborsError!void` |
| `transmit` | `pub fn transmit(self: *Ip6, token: *CompletionToken) TransmitError!void` |
| `receive` | `pub fn receive(self: *Ip6, token: *CompletionToken) ReceiveError!void` |
| `cancel` | `pub fn cancel(self: *Ip6, token: ?*CompletionToken) CancelError!void` |
| `poll` | `pub fn poll(self: *Ip6) PollError!bool` |

## os / uefi / protocol / ip6_config

| Function | Signature |
|----------|-----------|
| `setData` | `pub fn setData(self: *const Ip6Config, comptime data_type: std.meta.Tag(DataType) , payload: *const @FieldType(DataType, @tagName(data_type)), ) SetDataError!void` |
| `getData` | `pub fn getData(self: *const Ip6Config, comptime data_type: std.meta.Tag(DataType) , ) GetDataError!@FieldType(DataType, @tagName(data_type))` |
| `registerDataNotify` | `pub fn registerDataNotify(self: *const Ip6Config, data_type: DataType, event: Event,) RegisterDataNotifyError!void` |
| `unregisterDataNotify` | `pub fn unregisterDataNotify(self: *const Ip6Config, data_type: DataType, event: Event,) UnregisterDataNotifyError!void` |

## os / uefi / protocol / loaded_image

| Function | Signature |
|----------|-----------|
| `unload` | `pub fn unload(self: *LoadedImage, handle: Handle) UnloadError!void` |

## os / uefi / protocol / managed_network

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const ManagedNetwork) GetModeDataError!GetModeDataData` |
| `configure` | `pub fn configure(self: *ManagedNetwork, mnp_config_data: ?*const Config) ConfigureError!void` |
| `mcastIpToMac` | `pub fn mcastIpToMac(self: *ManagedNetwork, ipv6flag: bool, ipaddress: *const uefi.IpAddress,) McastIpToMacError!MacAddress` |
| `groups` | `pub fn groups(self: *ManagedNetwork, join_flag: bool, mac_address: ?*const MacAddress,) GroupsError!void` |
| `transmit` | `pub fn transmit(self: *ManagedNetwork, token: *CompletionToken) TransmitError!void` |
| `receive` | `pub fn receive(self: *ManagedNetwork, token: *CompletionToken) TransmitError!void` |
| `cancel` | `pub fn cancel(self: *ManagedNetwork, token: ?*const CompletionToken) CancelError!void` |
| `poll` | `pub fn poll(self: *ManagedNetwork) PollError!void` |
| `createChild` | `pub fn createChild(self: *const ServiceBinding, handle: *?Handle) Status` |
| `destroyChild` | `pub fn destroyChild(self: *const ServiceBinding, handle: Handle) Status` |
| `getFragments` | `pub fn getFragments(self: *TransmitData) []Fragment` |

## os / uefi / protocol / rng

| Function | Signature |
|----------|-----------|
| `getInfo` | `pub fn getInfo(self: *const Rng, list: []align(8) Guid) GetInfoError![]align(8) Guid` |
| `getRNG` | `pub fn getRNG(self: *const Rng, algo: ?*align(8) const Guid, value: []u8) GetRNGError!void` |

## os / uefi / protocol / serial_io

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *SerialIo) ResetError!void` |
| `setAttribute` | `pub fn setAttribute(self: *SerialIo, baud_rate: u64, receiver_fifo_depth: u32, timeout: u32, parity: ParityType, data_bits: u8, stop_bits: StopBitsType,) SetAttributeError!void` |
| `setControl` | `pub fn setControl(self: *SerialIo, control: u32) SetControlError!void` |
| `getControl` | `pub fn getControl(self: *SerialIo) GetControlError!u32` |
| `write` | `pub fn write(self: *SerialIo, buffer: []const u8) WriteError!usize` |
| `read` | `pub fn read(self: *SerialIo, buffer: []u8) ReadError!usize` |

## os / uefi / protocol / service_binding

| Function | Signature |
|----------|-----------|
| `ServiceBinding` | `pub fn ServiceBinding(service_guid: Guid) type` |
| `createChild` | `pub fn createChild(self: *Self) CreateChildError!Handle` |
| `addToHandle` | `pub fn addToHandle(self: *Self, handle: Handle) CreateChildError!void` |
| `destroyChild` | `pub fn destroyChild(self: *Self, handle: Handle) DestroyChildError!void` |

## os / uefi / protocol / simple_file_system

| Function | Signature |
|----------|-----------|
| `openVolume` | `pub fn openVolume(self: *const SimpleFileSystem) OpenVolumeError!*File` |

## os / uefi / protocol / simple_network

| Function | Signature |
|----------|-----------|
| `start` | `pub fn start(self: *SimpleNetwork) StartError!void` |
| `stop` | `pub fn stop(self: *SimpleNetwork) StopError!void` |
| `initialize` | `pub fn initialize(self: *SimpleNetwork, extra_rx_buffer_size: usize, extra_tx_buffer_size: usize,) InitializeError!void` |
| `reset` | `pub fn reset(self: *SimpleNetwork, extended_verification: bool) ResetError!void` |
| `shutdown` | `pub fn shutdown(self: *SimpleNetwork) ShutdownError!void` |
| `receiveFilters` | `pub fn receiveFilters(self: *SimpleNetwork, enable: ReceiveFilter, disable: ReceiveFilter, reset_mcast_filter: bool, mcast_filter: ?[]const MacAddress,) ReceiveFiltersError!void` |
| `stationAddress` | `pub fn stationAddress(self: *SimpleNetwork, reset_flag: bool, new: ?*const MacAddress,) StationAddressError!void` |
| `resetStatistics` | `pub fn resetStatistics(self: *SimpleNetwork) StatisticsError!void` |
| `statistics` | `pub fn statistics(self: *SimpleNetwork, reset_flag: bool) StatisticsError!Statistics` |
| `mcastIpToMac` | `pub fn mcastIpToMac(self: *SimpleNetwork, ipv6: bool, ip: *const anyopaque,) McastIpToMacError!MacAddress` |
| `nvData` | `pub fn nvData(self: *SimpleNetwork, read_write: NvDataOperation, offset: usize, buffer: []u8,) NvDataError!void` |
| `getStatus` | `pub fn getStatus(self: *SimpleNetwork, interrupt_status: ?*InterruptStatus, recycled_tx_buf: ?*?[*]u8,) GetStatusError!void` |
| `transmit` | `pub fn transmit(self: *SimpleNetwork, header_size: usize, buffer: []const u8, src_addr: ?*const MacAddress, dest_addr: ?*const MacAddress, protocol: ?*const u16,) TransmitError!void` |
| `receive` | `pub fn receive(self: *SimpleNetwork, buffer: []u8) ReceiveError!Packet` |

## os / uefi / protocol / simple_pointer

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *SimplePointer, verify: bool) ResetError!void` |
| `getState` | `pub fn getState(self: *const SimplePointer) GetStateError!State` |

## os / uefi / protocol / simple_text_input

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *SimpleTextInput, verify: bool) ResetError!void` |
| `readKeyStroke` | `pub fn readKeyStroke(self: *SimpleTextInput) ReadKeyStrokeError!Key.Input` |

## os / uefi / protocol / simple_text_input_ex

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *SimpleTextInputEx, verify: bool) ResetError!void` |
| `readKeyStroke` | `pub fn readKeyStroke(self: *SimpleTextInputEx) ReadKeyStrokeError!Key` |
| `setState` | `pub fn setState(self: *SimpleTextInputEx, state: *const Key.State.Toggle) SetStateError!void` |
| `registerKeyNotify` | `pub fn registerKeyNotify(self: *SimpleTextInputEx, key_data: *const Key, notify: *const fn (*const Key) callconv(cc) Status, ) RegisterKeyNotifyError!uefi.Handle` |
| `unregisterKeyNotify` | `pub fn unregisterKeyNotify(self: *SimpleTextInputEx, handle: uefi.Handle,) UnregisterKeyNotifyError!void` |

## os / uefi / protocol / simple_text_output

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *SimpleTextOutput, verify: bool) ResetError!void` |
| `outputString` | `pub fn outputString(self: *SimpleTextOutput, msg: [*:0]const u16) OutputStringError!bool` |
| `testString` | `pub fn testString(self: *const SimpleTextOutput, msg: [*:0]const u16) uefi.UnexpectedError!bool` |
| `queryMode` | `pub fn queryMode(self: *const SimpleTextOutput, mode_number: usize) QueryModeError!Geometry` |
| `setMode` | `pub fn setMode(self: *SimpleTextOutput, mode_number: usize) SetModeError!void` |
| `setAttribute` | `pub fn setAttribute(self: *SimpleTextOutput, attribute: Attribute) SetAttributeError!void` |
| `clearScreen` | `pub fn clearScreen(self: *SimpleTextOutput) ClearScreenError!void` |
| `setCursorPosition` | `pub fn setCursorPosition(self: *SimpleTextOutput, column: usize, row: usize,) SetCursorPositionError!void` |
| `enableCursor` | `pub fn enableCursor(self: *SimpleTextOutput, visible: bool) EnableCursorError!void` |

## os / uefi / protocol / udp6

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const Udp6) GetModeDataError!ModeData` |
| `configure` | `pub fn configure(self: *Udp6, udp6_config_data: ?*const Config) ConfigureError!void` |
| `groups` | `pub fn groups(self: *Udp6, join_flag: JoinFlag, multicast_address: ?*const Ip6.Address,) GroupsError!void` |
| `transmit` | `pub fn transmit(self: *Udp6, token: *CompletionToken) TransmitError!void` |
| `receive` | `pub fn receive(self: *Udp6, token: *CompletionToken) ReceiveError!void` |
| `cancel` | `pub fn cancel(self: *Udp6, token: ?*CompletionToken) CancelError!void` |
| `poll` | `pub fn poll(self: *Udp6) PollError!void` |
| `getFragments` | `pub fn getFragments(self: *ReceiveData) []Fragment` |
| `getFragments` | `pub fn getFragments(self: *TransmitData) []Fragment` |

## os / linux / IoUring

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(entries: u16, flags: u32) !IoUring` |
| `init_params` | `pub fn init_params(entries: u16, p: *linux.io_uring_params) !IoUring` |
| `deinit` | `pub fn deinit(self: *IoUring) void` |
| `get_sqe` | `pub fn get_sqe(self: *IoUring) !*linux.io_uring_sqe` |
| `submit` | `pub fn submit(self: *IoUring) !u32` |
| `submit_and_wait` | `pub fn submit_and_wait(self: *IoUring, wait_nr: u32) !u32` |
| `enter` | `pub fn enter(self: *IoUring, to_submit: u32, min_complete: u32, flags: u32) !u32` |
| `flush_sq` | `pub fn flush_sq(self: *IoUring) u32` |
| `sq_ring_needs_enter` | `pub fn sq_ring_needs_enter(self: *IoUring, flags: *u32) bool` |
| `sq_ready` | `pub fn sq_ready(self: *IoUring) u32` |
| `cq_ready` | `pub fn cq_ready(self: *IoUring) u32` |
| `copy_cqes` | `pub fn copy_cqes(self: *IoUring, cqes: []linux.io_uring_cqe, wait_nr: u32) !u32` |
| `copy_cqe` | `pub fn copy_cqe(ring: *IoUring) !linux.io_uring_cqe` |
| `cq_ring_needs_flush` | `pub fn cq_ring_needs_flush(self: *IoUring) bool` |
| `cqe_seen` | `pub fn cqe_seen(self: *IoUring, cqe: *linux.io_uring_cqe) void` |
| `cq_advance` | `pub fn cq_advance(self: *IoUring, count: u32) void` |
| `fsync` | `pub fn fsync(self: *IoUring, user_data: u64, fd: linux.fd_t, flags: u32) !*linux.io_uring_sqe` |
| `nop` | `pub fn nop(self: *IoUring, user_data: u64) !*linux.io_uring_sqe` |
| `read` | `pub fn read(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: ReadBuffer, offset: u64,) !*linux.io_uring_sqe` |
| `write` | `pub fn write(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: []const u8, offset: u64,) !*linux.io_uring_sqe` |
| `splice` | `pub fn splice(self: *IoUring, user_data: u64, fd_in: linux.fd_t, off_in: u64, fd_out: linux.fd_t, off_out: u64, len: usize) !*linux.io_uring_sqe` |
| `read_fixed` | `pub fn read_fixed(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: *posix.iovec, offset: u64, buffer_index: u16,) !*linux.io_uring_sqe` |
| `writev` | `pub fn writev(self: *IoUring, user_data: u64, fd: linux.fd_t, iovecs: []const posix.iovec_const, offset: u64,) !*linux.io_uring_sqe` |
| `write_fixed` | `pub fn write_fixed(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: *posix.iovec, offset: u64, buffer_index: u16,) !*linux.io_uring_sqe` |
| `accept` | `pub fn accept(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: ?*posix.sockaddr, addrlen: ?*posix.socklen_t, flags: u32,) !*linux.io_uring_sqe` |
| `accept_multishot` | `pub fn accept_multishot(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: ?*posix.sockaddr, addrlen: ?*posix.socklen_t, flags: u32,) !*linux.io_uring_sqe` |
| `accept_direct` | `pub fn accept_direct(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: ?*posix.sockaddr, addrlen: ?*posix.socklen_t, flags: u32,) !*linux.io_uring_sqe` |
| `accept_multishot_direct` | `pub fn accept_multishot_direct(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: ?*posix.sockaddr, addrlen: ?*posix.socklen_t, flags: u32,) !*linux.io_uring_sqe` |
| `connect` | `pub fn connect(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: *const posix.sockaddr, addrlen: posix.socklen_t,) !*linux.io_uring_sqe` |
| `epoll_ctl` | `pub fn epoll_ctl(self: *IoUring, user_data: u64, epfd: linux.fd_t, fd: linux.fd_t, op: u32, ev: ?*linux.epoll_event,) !*linux.io_uring_sqe` |
| `recv` | `pub fn recv(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: RecvBuffer, flags: u32,) !*linux.io_uring_sqe` |
| `send` | `pub fn send(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: []const u8, flags: u32,) !*linux.io_uring_sqe` |
| `send_zc` | `pub fn send_zc(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: []const u8, send_flags: u32, zc_flags: u16,) !*linux.io_uring_sqe` |
| `send_zc_fixed` | `pub fn send_zc_fixed(self: *IoUring, user_data: u64, fd: linux.fd_t, buffer: []const u8, send_flags: u32, zc_flags: u16, buf_index: u16,) !*linux.io_uring_sqe` |
| `recvmsg` | `pub fn recvmsg(self: *IoUring, user_data: u64, fd: linux.fd_t, msg: *linux.msghdr, flags: u32,) !*linux.io_uring_sqe` |
| `sendmsg` | `pub fn sendmsg(self: *IoUring, user_data: u64, fd: linux.fd_t, msg: *const linux.msghdr_const, flags: u32,) !*linux.io_uring_sqe` |
| `sendmsg_zc` | `pub fn sendmsg_zc(self: *IoUring, user_data: u64, fd: linux.fd_t, msg: *const linux.msghdr_const, flags: u32,) !*linux.io_uring_sqe` |
| `openat` | `pub fn openat(self: *IoUring, user_data: u64, fd: linux.fd_t, path: [*:0]const u8, flags: linux.O, mode: posix.mode_t,) !*linux.io_uring_sqe` |
| `openat_direct` | `pub fn openat_direct(self: *IoUring, user_data: u64, fd: linux.fd_t, path: [*:0]const u8, flags: linux.O, mode: posix.mode_t, file_index: u32,) !*linux.io_uring_sqe` |
| `close` | `pub fn close(self: *IoUring, user_data: u64, fd: linux.fd_t) !*linux.io_uring_sqe` |
| `close_direct` | `pub fn close_direct(self: *IoUring, user_data: u64, file_index: u32) !*linux.io_uring_sqe` |
| `timeout` | `pub fn timeout(self: *IoUring, user_data: u64, ts: *const linux.kernel_timespec, count: u32, flags: u32,) !*linux.io_uring_sqe` |
| `timeout_remove` | `pub fn timeout_remove(self: *IoUring, user_data: u64, timeout_user_data: u64, flags: u32,) !*linux.io_uring_sqe` |
| `link_timeout` | `pub fn link_timeout(self: *IoUring, user_data: u64, ts: *const linux.kernel_timespec, flags: u32,) !*linux.io_uring_sqe` |
| `poll_add` | `pub fn poll_add(self: *IoUring, user_data: u64, fd: linux.fd_t, poll_mask: u32,) !*linux.io_uring_sqe` |
| `poll_remove` | `pub fn poll_remove(self: *IoUring, user_data: u64, target_user_data: u64,) !*linux.io_uring_sqe` |
| `poll_update` | `pub fn poll_update(self: *IoUring, user_data: u64, old_user_data: u64, new_user_data: u64, poll_mask: u32, flags: u32,) !*linux.io_uring_sqe` |
| `fallocate` | `pub fn fallocate(self: *IoUring, user_data: u64, fd: linux.fd_t, mode: i32, offset: u64, len: u64,) !*linux.io_uring_sqe` |
| `statx` | `pub fn statx(self: *IoUring, user_data: u64, fd: linux.fd_t, path: [:0]const u8, flags: u32, mask: linux.STATX, buf: *linux.Statx,) !*linux.io_uring_sqe` |
| `cancel` | `pub fn cancel(self: *IoUring, user_data: u64, cancel_user_data: u64, flags: u32,) !*linux.io_uring_sqe` |
| `shutdown` | `pub fn shutdown(self: *IoUring, user_data: u64, sockfd: posix.socket_t, how: u32,) !*linux.io_uring_sqe` |
| `renameat` | `pub fn renameat(self: *IoUring, user_data: u64, old_dir_fd: linux.fd_t, old_path: [*:0]const u8, new_dir_fd: linux.fd_t, new_path: [*:0]const u8, flags: u32,) !*linux.io_uring_sqe` |
| `unlinkat` | `pub fn unlinkat(self: *IoUring, user_data: u64, dir_fd: linux.fd_t, path: [*:0]const u8, flags: u32,) !*linux.io_uring_sqe` |
| `mkdirat` | `pub fn mkdirat(self: *IoUring, user_data: u64, dir_fd: linux.fd_t, path: [*:0]const u8, mode: posix.mode_t,) !*linux.io_uring_sqe` |
| `symlinkat` | `pub fn symlinkat(self: *IoUring, user_data: u64, target: [*:0]const u8, new_dir_fd: linux.fd_t, link_path: [*:0]const u8,) !*linux.io_uring_sqe` |
| `linkat` | `pub fn linkat(self: *IoUring, user_data: u64, old_dir_fd: linux.fd_t, old_path: [*:0]const u8, new_dir_fd: linux.fd_t, new_path: [*:0]const u8, flags: u32,) !*linux.io_uring_sqe` |
| `provide_buffers` | `pub fn provide_buffers(self: *IoUring, user_data: u64, buffers: [*]u8, buffer_size: usize, buffers_count: usize, group_id: usize, buffer_id: usize,) !*linux.io_uring_sqe` |
| `remove_buffers` | `pub fn remove_buffers(self: *IoUring, user_data: u64, buffers_count: usize, group_id: usize,) !*linux.io_uring_sqe` |
| `waitid` | `pub fn waitid(self: *IoUring, user_data: u64, id_type: linux.P, id: i32, infop: *linux.siginfo_t, options: u32, flags: u32,) !*linux.io_uring_sqe` |
| `register_files` | `pub fn register_files(self: *IoUring, fds: []const linux.fd_t) !void` |
| `register_files_update` | `pub fn register_files_update(self: *IoUring, offset: u32, fds: []const linux.fd_t) !void` |
| `register_files_sparse` | `pub fn register_files_sparse(self: *IoUring, nr_files: u32) !void` |
| `register_file_alloc_range` | `pub fn register_file_alloc_range(self: *IoUring, offset: u32, len: u32) !void` |
| `register_eventfd` | `pub fn register_eventfd(self: *IoUring, fd: linux.fd_t) !void` |
| `register_eventfd_async` | `pub fn register_eventfd_async(self: *IoUring, fd: linux.fd_t) !void` |
| `unregister_eventfd` | `pub fn unregister_eventfd(self: *IoUring) !void` |
| `register_napi` | `pub fn register_napi(self: *IoUring, napi: *linux.io_uring_napi) !void` |
| `unregister_napi` | `pub fn unregister_napi(self: *IoUring, napi: *linux.io_uring_napi) !void` |
| `register_buffers` | `pub fn register_buffers(self: *IoUring, buffers: []const posix.iovec) !void` |
| `unregister_buffers` | `pub fn unregister_buffers(self: *IoUring) !void` |
| `get_probe` | `pub fn get_probe(self: *IoUring) !linux.io_uring_probe` |
| `unregister_files` | `pub fn unregister_files(self: *IoUring) !void` |
| `socket` | `pub fn socket(self: *IoUring, user_data: u64, domain: u32, socket_type: u32, protocol: u32, flags: u32,) !*linux.io_uring_sqe` |
| `socket_direct` | `pub fn socket_direct(self: *IoUring, user_data: u64, domain: u32, socket_type: u32, protocol: u32, flags: u32, file_index: u32,) !*linux.io_uring_sqe` |
| `socket_direct_alloc` | `pub fn socket_direct_alloc(self: *IoUring, user_data: u64, domain: u32, socket_type: u32, protocol: u32, flags: u32,) !*linux.io_uring_sqe` |
| `bind` | `pub fn bind(self: *IoUring, user_data: u64, fd: linux.fd_t, addr: *const posix.sockaddr, addrlen: posix.socklen_t, flags: u32,) !*linux.io_uring_sqe` |
| `listen` | `pub fn listen(self: *IoUring, user_data: u64, fd: linux.fd_t, backlog: usize, flags: u32,) !*linux.io_uring_sqe` |
| `cmd_sock` | `pub fn cmd_sock(self: *IoUring, user_data: u64, cmd_op: linux.IO_URING_SOCKET_OP, fd: linux.fd_t, level: u32, // linux.SOL optname: u32, // linux.SO optval: u64, // pointer to the option value optlen: u32, // size of the option value) !*linux.io_u...` |
| `setsockopt` | `pub fn setsockopt(self: *IoUring, user_data: u64, fd: linux.fd_t, level: u32, // linux.SOL optname: u32, // linux.SO opt: []const u8,) !*linux.io_uring_sqe` |
| `getsockopt` | `pub fn getsockopt(self: *IoUring, user_data: u64, fd: linux.fd_t, level: u32, // linux.SOL optname: u32, // linux.SO opt: []u8,) !*linux.io_uring_sqe` |
| `init` | `pub fn init(fd: linux.fd_t, p: linux.io_uring_params) !SubmissionQueue` |
| `deinit` | `pub fn deinit(self: *SubmissionQueue) void` |
| `init` | `pub fn init(fd: linux.fd_t, p: linux.io_uring_params, sq: SubmissionQueue) !CompletionQueue` |
| `deinit` | `pub fn deinit(self: *CompletionQueue) void` |
| `init` | `pub fn init(ring: *IoUring, allocator: Allocator, group_id: u16, buffer_size: u32, buffers_count: u16,) !BufferGroup` |
| `deinit` | `pub fn deinit(self: *BufferGroup, allocator: Allocator) void` |
| `recv` | `pub fn recv(self: *BufferGroup, user_data: u64, fd: linux.fd_t, flags: u32) !*linux.io_uring_sqe` |
| `recv_multishot` | `pub fn recv_multishot(self: *BufferGroup, user_data: u64, fd: linux.fd_t, flags: u32) !*linux.io_uring_sqe` |
| `get_by_id` | `pub fn get_by_id(self: *BufferGroup, buffer_id: u16) []u8` |
| `get` | `pub fn get(self: *BufferGroup, cqe: linux.io_uring_cqe) ![]u8` |
| `put` | `pub fn put(self: *BufferGroup, cqe: linux.io_uring_cqe) !void` |
| `setup_buf_ring` | `pub fn setup_buf_ring(fd: linux.fd_t, entries: u16, group_id: u16, flags: linux.io_uring_buf_reg.Flags,) !*align(page_size_min) linux.io_uring_buf_ring` |
| `free_buf_ring` | `pub fn free_buf_ring(fd: linux.fd_t, br: *align(page_size_min) linux.io_uring_buf_ring, entries: u32, group_id: u16) void` |
| `buf_ring_init` | `pub fn buf_ring_init(br: *linux.io_uring_buf_ring) void` |
| `buf_ring_mask` | `pub fn buf_ring_mask(entries: u16) u16` |
| `buf_ring_add` | `pub fn buf_ring_add(br: *linux.io_uring_buf_ring, buffer: []u8, buffer_id: u16, mask: u16, buffer_offset: u16,) void` |
| `buf_ring_advance` | `pub fn buf_ring_advance(br: *linux.io_uring_buf_ring, count: u16) void` |

## os / linux / aarch64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / arm

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / bpf

| Function | Signature |
|----------|-----------|
| `alu` | `pub fn alu(comptime width: comptime_int, op: AluOp, dst: Reg, src: anytype) Insn` |
| `mov` | `pub fn mov(dst: Reg, src: anytype) Insn` |
| `add` | `pub fn add(dst: Reg, src: anytype) Insn` |
| `sub` | `pub fn sub(dst: Reg, src: anytype) Insn` |
| `mul` | `pub fn mul(dst: Reg, src: anytype) Insn` |
| `div` | `pub fn div(dst: Reg, src: anytype) Insn` |
| `alu_or` | `pub fn alu_or(dst: Reg, src: anytype) Insn` |
| `alu_and` | `pub fn alu_and(dst: Reg, src: anytype) Insn` |
| `lsh` | `pub fn lsh(dst: Reg, src: anytype) Insn` |
| `rsh` | `pub fn rsh(dst: Reg, src: anytype) Insn` |
| `neg` | `pub fn neg(dst: Reg) Insn` |
| `mod` | `pub fn mod(dst: Reg, src: anytype) Insn` |
| `xor` | `pub fn xor(dst: Reg, src: anytype) Insn` |
| `arsh` | `pub fn arsh(dst: Reg, src: anytype) Insn` |
| `jmp` | `pub fn jmp(op: JmpOp, dst: Reg, src: anytype, off: i16) Insn` |
| `ja` | `pub fn ja(off: i16) Insn` |
| `jeq` | `pub fn jeq(dst: Reg, src: anytype, off: i16) Insn` |
| `jgt` | `pub fn jgt(dst: Reg, src: anytype, off: i16) Insn` |
| `jge` | `pub fn jge(dst: Reg, src: anytype, off: i16) Insn` |
| `jlt` | `pub fn jlt(dst: Reg, src: anytype, off: i16) Insn` |
| `jle` | `pub fn jle(dst: Reg, src: anytype, off: i16) Insn` |
| `jset` | `pub fn jset(dst: Reg, src: anytype, off: i16) Insn` |
| `jne` | `pub fn jne(dst: Reg, src: anytype, off: i16) Insn` |
| `jsgt` | `pub fn jsgt(dst: Reg, src: anytype, off: i16) Insn` |
| `jsge` | `pub fn jsge(dst: Reg, src: anytype, off: i16) Insn` |
| `jslt` | `pub fn jslt(dst: Reg, src: anytype, off: i16) Insn` |
| `jsle` | `pub fn jsle(dst: Reg, src: anytype, off: i16) Insn` |
| `xadd` | `pub fn xadd(dst: Reg, src: Reg) Insn` |
| `ld_abs` | `pub fn ld_abs(size: Size, dst: Reg, src: Reg, imm: i32) Insn` |
| `ld_ind` | `pub fn ld_ind(size: Size, dst: Reg, src: Reg, imm: i32) Insn` |
| `ldx` | `pub fn ldx(size: Size, dst: Reg, src: Reg, off: i16) Insn` |
| `ld_dw1` | `pub fn ld_dw1(dst: Reg, imm: u64) Insn` |
| `ld_dw2` | `pub fn ld_dw2(imm: u64) Insn` |
| `ld_map_fd1` | `pub fn ld_map_fd1(dst: Reg, map_fd: fd_t) Insn` |
| `ld_map_fd2` | `pub fn ld_map_fd2(map_fd: fd_t) Insn` |
| `st` | `pub fn st(size: Size, dst: Reg, off: i16, imm: i32) Insn` |
| `stx` | `pub fn stx(size: Size, dst: Reg, off: i16, src: Reg) Insn` |
| `le` | `pub fn le(comptime size: Size, dst: Reg) Insn` |
| `be` | `pub fn be(comptime size: Size, dst: Reg) Insn` |
| `call` | `pub fn call(helper: Helper) Insn` |
| `exit` | `pub fn exit() Insn` |
| `map_create` | `pub fn map_create(map_type: MapType, key_size: u32, value_size: u32, max_entries: u32) !fd_t` |
| `map_lookup_elem` | `pub fn map_lookup_elem(fd: fd_t, key: []const u8, value: []u8) !void` |
| `map_update_elem` | `pub fn map_update_elem(fd: fd_t, key: []const u8, value: []const u8, flags: u64) !void` |
| `map_delete_elem` | `pub fn map_delete_elem(fd: fd_t, key: []const u8) !void` |
| `map_get_next_key` | `pub fn map_get_next_key(fd: fd_t, key: []const u8, next_key: []u8) !bool` |
| `prog_load` | `pub fn prog_load(prog_type: ProgType, insns: []const Insn, log: ?*Log, license: []const u8, kern_version: u32, flags: u32,) !fd_t` |

## os / linux / hexagon

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |

## os / linux / io_uring_sqe

| Function | Signature |
|----------|-----------|
| `prep_nop` | `pub fn prep_nop(sqe: *linux.io_uring_sqe) void` |
| `prep_fsync` | `pub fn prep_fsync(sqe: *linux.io_uring_sqe, fd: linux.fd_t, flags: u32) void` |
| `prep_rw` | `pub fn prep_rw(sqe: *linux.io_uring_sqe, op: linux.IORING_OP, fd: linux.fd_t, addr: u64, len: usize, offset: u64,) void` |
| `prep_read` | `pub fn prep_read(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []u8, offset: u64) void` |
| `prep_write` | `pub fn prep_write(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []const u8, offset: u64) void` |
| `prep_splice` | `pub fn prep_splice(sqe: *linux.io_uring_sqe, fd_in: linux.fd_t, off_in: u64, fd_out: linux.fd_t, off_out: u64, len: usize) void` |
| `prep_readv` | `pub fn prep_readv(sqe: *linux.io_uring_sqe, fd: linux.fd_t, iovecs: []const std.posix.iovec, offset: u64,) void` |
| `prep_writev` | `pub fn prep_writev(sqe: *linux.io_uring_sqe, fd: linux.fd_t, iovecs: []const std.posix.iovec_const, offset: u64,) void` |
| `prep_read_fixed` | `pub fn prep_read_fixed(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: *std.posix.iovec, offset: u64, buffer_index: u16) void` |
| `prep_write_fixed` | `pub fn prep_write_fixed(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: *std.posix.iovec, offset: u64, buffer_index: u16) void` |
| `prep_accept` | `pub fn prep_accept(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: ?*linux.sockaddr, addrlen: ?*linux.socklen_t, flags: u32,) void` |
| `prep_accept_direct` | `pub fn prep_accept_direct(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: ?*linux.sockaddr, addrlen: ?*linux.socklen_t, flags: u32, file_index: u32,) void` |
| `prep_multishot_accept_direct` | `pub fn prep_multishot_accept_direct(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: ?*linux.sockaddr, addrlen: ?*linux.socklen_t, flags: u32,) void` |
| `prep_connect` | `pub fn prep_connect(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: *const linux.sockaddr, addrlen: linux.socklen_t,) void` |
| `prep_epoll_ctl` | `pub fn prep_epoll_ctl(sqe: *linux.io_uring_sqe, epfd: linux.fd_t, fd: linux.fd_t, op: u32, ev: ?*linux.epoll_event,) void` |
| `prep_recv` | `pub fn prep_recv(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []u8, flags: u32) void` |
| `prep_recv_multishot` | `pub fn prep_recv_multishot(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []u8, flags: u32,) void` |
| `prep_recvmsg` | `pub fn prep_recvmsg(sqe: *linux.io_uring_sqe, fd: linux.fd_t, msg: *linux.msghdr, flags: u32,) void` |
| `prep_recvmsg_multishot` | `pub fn prep_recvmsg_multishot(sqe: *linux.io_uring_sqe, fd: linux.fd_t, msg: *linux.msghdr, flags: u32,) void` |
| `prep_send` | `pub fn prep_send(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []const u8, flags: u32) void` |
| `prep_send_zc` | `pub fn prep_send_zc(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []const u8, flags: u32, zc_flags: u16) void` |
| `prep_send_zc_fixed` | `pub fn prep_send_zc_fixed(sqe: *linux.io_uring_sqe, fd: linux.fd_t, buffer: []const u8, flags: u32, zc_flags: u16, buf_index: u16) void` |
| `prep_sendmsg_zc` | `pub fn prep_sendmsg_zc(sqe: *linux.io_uring_sqe, fd: linux.fd_t, msg: *const linux.msghdr_const, flags: u32,) void` |
| `prep_sendmsg` | `pub fn prep_sendmsg(sqe: *linux.io_uring_sqe, fd: linux.fd_t, msg: *const linux.msghdr_const, flags: u32,) void` |
| `prep_openat` | `pub fn prep_openat(sqe: *linux.io_uring_sqe, fd: linux.fd_t, path: [*:0]const u8, flags: linux.O, mode: linux.mode_t,) void` |
| `prep_openat_direct` | `pub fn prep_openat_direct(sqe: *linux.io_uring_sqe, fd: linux.fd_t, path: [*:0]const u8, flags: linux.O, mode: linux.mode_t, file_index: u32,) void` |
| `prep_close` | `pub fn prep_close(sqe: *linux.io_uring_sqe, fd: linux.fd_t) void` |
| `prep_close_direct` | `pub fn prep_close_direct(sqe: *linux.io_uring_sqe, file_index: u32) void` |
| `prep_timeout` | `pub fn prep_timeout(sqe: *linux.io_uring_sqe, ts: *const linux.kernel_timespec, count: u32, flags: u32,) void` |
| `prep_timeout_remove` | `pub fn prep_timeout_remove(sqe: *linux.io_uring_sqe, timeout_user_data: u64, flags: u32) void` |
| `prep_link_timeout` | `pub fn prep_link_timeout(sqe: *linux.io_uring_sqe, ts: *const linux.kernel_timespec, flags: u32,) void` |
| `prep_poll_add` | `pub fn prep_poll_add(sqe: *linux.io_uring_sqe, fd: linux.fd_t, poll_mask: u32,) void` |
| `prep_poll_remove` | `pub fn prep_poll_remove(sqe: *linux.io_uring_sqe, target_user_data: u64,) void` |
| `prep_poll_update` | `pub fn prep_poll_update(sqe: *linux.io_uring_sqe, old_user_data: u64, new_user_data: u64, poll_mask: u32, flags: u32,) void` |
| `prep_fallocate` | `pub fn prep_fallocate(sqe: *linux.io_uring_sqe, fd: linux.fd_t, mode: i32, offset: u64, len: u64,) void` |
| `prep_statx` | `pub fn prep_statx(sqe: *linux.io_uring_sqe, fd: linux.fd_t, path: [*:0]const u8, flags: u32, mask: linux.STATX, buf: *linux.Statx,) void` |
| `prep_cancel` | `pub fn prep_cancel(sqe: *linux.io_uring_sqe, cancel_user_data: u64, flags: u32,) void` |
| `prep_cancel_fd` | `pub fn prep_cancel_fd(sqe: *linux.io_uring_sqe, fd: linux.fd_t, flags: u32,) void` |
| `prep_shutdown` | `pub fn prep_shutdown(sqe: *linux.io_uring_sqe, sockfd: linux.socket_t, how: u32,) void` |
| `prep_renameat` | `pub fn prep_renameat(sqe: *linux.io_uring_sqe, old_dir_fd: linux.fd_t, old_path: [*:0]const u8, new_dir_fd: linux.fd_t, new_path: [*:0]const u8, flags: u32,) void` |
| `prep_unlinkat` | `pub fn prep_unlinkat(sqe: *linux.io_uring_sqe, dir_fd: linux.fd_t, path: [*:0]const u8, flags: u32,) void` |
| `prep_mkdirat` | `pub fn prep_mkdirat(sqe: *linux.io_uring_sqe, dir_fd: linux.fd_t, path: [*:0]const u8, mode: linux.mode_t,) void` |
| `prep_symlinkat` | `pub fn prep_symlinkat(sqe: *linux.io_uring_sqe, target: [*:0]const u8, new_dir_fd: linux.fd_t, link_path: [*:0]const u8,) void` |
| `prep_linkat` | `pub fn prep_linkat(sqe: *linux.io_uring_sqe, old_dir_fd: linux.fd_t, old_path: [*:0]const u8, new_dir_fd: linux.fd_t, new_path: [*:0]const u8, flags: u32,) void` |
| `prep_files_update` | `pub fn prep_files_update(sqe: *linux.io_uring_sqe, fds: []const linux.fd_t, offset: u32,) void` |
| `prep_files_update_alloc` | `pub fn prep_files_update_alloc(sqe: *linux.io_uring_sqe, fds: []linux.fd_t,) void` |
| `prep_provide_buffers` | `pub fn prep_provide_buffers(sqe: *linux.io_uring_sqe, buffers: [*]u8, buffer_len: usize, num: usize, group_id: usize, buffer_id: usize,) void` |
| `prep_remove_buffers` | `pub fn prep_remove_buffers(sqe: *linux.io_uring_sqe, num: usize, group_id: usize,) void` |
| `prep_multishot_accept` | `pub fn prep_multishot_accept(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: ?*linux.sockaddr, addrlen: ?*linux.socklen_t, flags: u32,) void` |
| `prep_socket` | `pub fn prep_socket(sqe: *linux.io_uring_sqe, domain: u32, socket_type: u32, protocol: u32, flags: u32,) void` |
| `prep_socket_direct` | `pub fn prep_socket_direct(sqe: *linux.io_uring_sqe, domain: u32, socket_type: u32, protocol: u32, flags: u32, file_index: u32,) void` |
| `prep_socket_direct_alloc` | `pub fn prep_socket_direct_alloc(sqe: *linux.io_uring_sqe, domain: u32, socket_type: u32, protocol: u32, flags: u32,) void` |
| `prep_waitid` | `pub fn prep_waitid(sqe: *linux.io_uring_sqe, id_type: linux.P, id: i32, infop: *linux.siginfo_t, options: u32, flags: u32,) void` |
| `prep_bind` | `pub fn prep_bind(sqe: *linux.io_uring_sqe, fd: linux.fd_t, addr: *const linux.sockaddr, addrlen: linux.socklen_t, flags: u32,) void` |
| `prep_listen` | `pub fn prep_listen(sqe: *linux.io_uring_sqe, fd: linux.fd_t, backlog: usize, flags: u32,) void` |
| `prep_cmd_sock` | `pub fn prep_cmd_sock(sqe: *linux.io_uring_sqe, cmd_op: linux.IO_URING_SOCKET_OP, fd: linux.fd_t, level: u32, optname: u32, optval: u64, optlen: u32,) void` |
| `set_flags` | `pub fn set_flags(sqe: *linux.io_uring_sqe, flags: u8) void` |
| `link_next` | `pub fn link_next(sqe: *linux.io_uring_sqe) void` |

## os / linux / ioctl

| Function | Signature |
|----------|-----------|
| `IO` | `pub fn IO(io_type: u8, nr: u8) u32` |
| `IOR` | `pub fn IOR(io_type: u8, nr: u8, comptime T: type) u32` |
| `IOW` | `pub fn IOW(io_type: u8, nr: u8, comptime T: type) u32` |
| `IOWR` | `pub fn IOWR(io_type: u8, nr: u8, comptime T: type) u32` |

## os / linux / loongarch64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |

## os / linux / m68k

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / mips

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `syscall7` | `pub fn syscall7(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32, arg7: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |

## os / linux / mips64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |

## os / linux / mipsn32

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |

## os / linux / or1k

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |

## os / linux / powerpc

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / powerpc64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / riscv32

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |

## os / linux / riscv64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |

## os / linux / s390x

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / sparc64

| Function | Signature |
|----------|-----------|
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) u64` |
| `syscall_fork` | `pub fn syscall_fork() u64` |
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |
| `restore_rt` | `pub fn restore_rt() callconv(.c) void` |

## os / linux / thumb

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / tls

| Function | Signature |
|----------|-----------|
| `setThreadPointer` | `pub fn setThreadPointer(addr: usize) void` |
| `prepareArea` | `pub fn prepareArea(area: []u8) usize` |
| `initStatic` | `pub fn initStatic(phdrs: []elf.Phdr) void` |

## os / linux / vdso

| Function | Signature |
|----------|-----------|
| `lookup` | `pub fn lookup(vername: []const u8, name: []const u8) usize` |

## os / linux / x32

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / x86

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u32` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u32) u32` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u32, arg2: u32) u32` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u32, arg2: u32, arg3: u32) u32` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32) u32` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32) u32` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u32, arg2: u32, arg3: u32, arg4: u32, arg5: u32, arg6: u32,) u32` |
| `socketcall` | `pub fn socketcall(call: u32, args: [*]const u32) u32` |
| `clone` | `pub fn clone() callconv(.naked) u32` |
| `restore` | `pub fn restore() callconv(.naked) noreturn` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / linux / x86_64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) u64` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: u64) u64` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: u64, arg2: u64) u64` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: u64, arg2: u64, arg3: u64) u64` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64) u64` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64) u64` |
| `syscall6` | `pub fn syscall6(number: SYS, arg1: u64, arg2: u64, arg3: u64, arg4: u64, arg5: u64, arg6: u64,) u64` |
| `clone` | `pub fn clone() callconv(.naked) u64` |
| `restore_rt` | `pub fn restore_rt() callconv(.naked) noreturn` |

## os / plan9 / x86_64

| Function | Signature |
|----------|-----------|
| `syscall1` | `pub fn syscall1(sys: plan9.SYS, arg0: usize) usize` |
| `syscall2` | `pub fn syscall2(sys: plan9.SYS, arg0: usize, arg1: usize) usize` |
| `syscall3` | `pub fn syscall3(sys: plan9.SYS, arg0: usize, arg1: usize, arg2: usize) usize` |
| `syscall4` | `pub fn syscall4(sys: plan9.SYS, arg0: usize, arg1: usize, arg2: usize, arg3: usize) usize` |

## fmt / float

| Function | Signature |
|----------|-----------|
| `bufferSize` | `pub fn bufferSize(comptime mode: Mode, comptime T: type) comptime_int` |
| `render` | `pub fn render(buf: []u8, value: anytype, options: Options) Error![]const u8` |
| `FloatDecimal` | `pub fn FloatDecimal(comptime T: type) type` |
| `formatScientific` | `pub fn formatScientific(comptime T: type, buf: []u8, f_: FloatDecimal(T) , precision: ?usize) Error![]const u8` |
| `formatDecimal` | `pub fn formatDecimal(comptime T: type, buf: []u8, f_: FloatDecimal(T) , precision: ?usize) Error![]const u8` |
| `binaryToDecimal` | `pub fn binaryToDecimal(comptime T: type, bits: T, mantissa_bits: std.math.Log2Int(T) , exponent_bits: u5, explicit_leading_bit: bool, comptime tables: anytype) FloatDecimal(T)` |

## fmt / parse_float

| Function | Signature |
|----------|-----------|
| `parseFloat` | `pub fn parseFloat(comptime T: type, s: []const u8) ParseFloatError!T` |

## fmt / parse_float / FloatInfo

| Function | Signature |
|----------|-----------|
| `from` | `pub fn from(comptime T: type) Self` |

## fmt / parse_float / FloatStream

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(s: []const u8) FloatStream` |
| `offsetTrue` | `pub fn offsetTrue(self: FloatStream) usize` |
| `reset` | `pub fn reset(self: *FloatStream) void` |
| `len` | `pub fn len(self: FloatStream) usize` |
| `hasLen` | `pub fn hasLen(self: FloatStream, n: usize) bool` |
| `firstUnchecked` | `pub fn firstUnchecked(self: FloatStream) u8` |
| `first` | `pub fn first(self: FloatStream) ?u8` |
| `isEmpty` | `pub fn isEmpty(self: FloatStream) bool` |
| `firstIs` | `pub fn firstIs(self: FloatStream, comptime cs: []const u8) bool` |
| `firstIsLower` | `pub fn firstIsLower(self: FloatStream, comptime cs: []const u8) bool` |
| `firstIsDigit` | `pub fn firstIsDigit(self: FloatStream, comptime base: u8) bool` |
| `advance` | `pub fn advance(self: *FloatStream, n: usize) void` |
| `skipChars` | `pub fn skipChars(self: *FloatStream, comptime cs: []const u8) void` |
| `readU64Unchecked` | `pub fn readU64Unchecked(self: FloatStream) u64` |
| `readU64` | `pub fn readU64(self: FloatStream) ?u64` |
| `atUnchecked` | `pub fn atUnchecked(self: *FloatStream, i: usize) u8` |
| `scanDigit` | `pub fn scanDigit(self: *FloatStream, comptime base: u8) ?u8` |

## fmt / parse_float / common

| Function | Signature |
|----------|-----------|
| `BiasedFp` | `pub fn BiasedFp(comptime T: type) type` |
| `zero` | `pub fn zero() Self` |
| `zeroPow2` | `pub fn zeroPow2(e: i32) Self` |
| `inf` | `pub fn inf(comptime FloatT: type) Self` |
| `eql` | `pub fn eql(self: Self, other: Self) bool` |
| `toFloat` | `pub fn toFloat(self: Self, comptime FloatT: type, negative: bool) FloatT` |
| `floatFromUnsigned` | `pub fn floatFromUnsigned(comptime T: type, comptime MantissaT: type, v: MantissaT) T` |
| `Number` | `pub fn Number(comptime T: type) type` |
| `isEightDigits` | `pub fn isEightDigits(v: u64) bool` |
| `isDigit` | `pub fn isDigit(c: u8, comptime base: u8) bool` |
| `mantissaType` | `pub fn mantissaType(comptime T: type) type` |

## fmt / parse_float / convert_eisel_lemire

| Function | Signature |
|----------|-----------|
| `convertEiselLemire` | `pub fn convertEiselLemire(comptime T: type, q: i64, w_: u64) ?BiasedFp(f64)` |
| `new` | `pub fn new(lo: u64, hi: u64) U128` |
| `mul` | `pub fn mul(a: u64, b: u64) U128` |

## fmt / parse_float / convert_fast

| Function | Signature |
|----------|-----------|
| `convertFast` | `pub fn convertFast(comptime T: type, n: Number(T) ) ?T` |

## fmt / parse_float / convert_hex

| Function | Signature |
|----------|-----------|
| `convertHex` | `pub fn convertHex(comptime T: type, n_: Number(T) ) T` |

## fmt / parse_float / convert_slow

| Function | Signature |
|----------|-----------|
| `getShift` | `pub fn getShift(n: usize) usize` |
| `convertSlow` | `pub fn convertSlow(comptime T: type, s: []const u8) BiasedFp(T)` |

## fmt / parse_float / decimal

| Function | Signature |
|----------|-----------|
| `Decimal` | `pub fn Decimal(comptime T: type) type` |
| `new` | `pub fn new() Self` |
| `tryAddDigit` | `pub fn tryAddDigit(self: *Self, digit: u8) void` |
| `trim` | `pub fn trim(self: *Self) void` |
| `round` | `pub fn round(self: *Self) MantissaT` |
| `leftShift` | `pub fn leftShift(self: *Self, shift: usize) void` |
| `rightShift` | `pub fn rightShift(self: *Self, shift: usize) void` |
| `parse` | `pub fn parse(s: []const u8) Self` |
| `numberOfDigitsLeftShift` | `pub fn numberOfDigitsLeftShift(self: *Self, shift: usize) usize` |

## fmt / parse_float / parse

| Function | Signature |
|----------|-----------|
| `parseNumber` | `pub fn parseNumber(comptime T: type, s: []const u8, negative: bool) ?Number(T)` |
| `parseInfOrNan` | `pub fn parseInfOrNan(comptime T: type, s: []const u8, negative: bool) ?T` |
| `validUnderscores` | `pub fn validUnderscores(s: []const u8, comptime base: u8) bool` |

## fs / path

| Function | Signature |
|----------|-----------|
| `isSep` | `pub fn isSep(byte: u8) bool` |
| `isSep` | `pub fn isSep(comptime path_type: PathType, comptime T: type, c: T) bool` |
| `join` | `pub fn join(allocator: Allocator, paths: []const []const u8) ![]u8` |
| `joinZ` | `pub fn joinZ(allocator: Allocator, paths: []const []const u8) ![:0]u8` |
| `fmtJoin` | `pub fn fmtJoin(paths: []const []const u8) std.fmt.Alt([]const []const u8, formatJoin)` |
| `isAbsoluteZ` | `pub fn isAbsoluteZ(path_c: [*:0]const u8) bool` |
| `isAbsolute` | `pub fn isAbsolute(path: []const u8) bool` |
| `isAbsoluteWindows` | `pub fn isAbsoluteWindows(path: []const u8) bool` |
| `isAbsoluteWindowsW` | `pub fn isAbsoluteWindowsW(path_w: [*:0]const u16) bool` |
| `isAbsoluteWindowsWtf16` | `pub fn isAbsoluteWindowsWtf16(path: []const u16) bool` |
| `isAbsoluteWindowsZ` | `pub fn isAbsoluteWindowsZ(path_c: [*:0]const u8) bool` |
| `isAbsolutePosix` | `pub fn isAbsolutePosix(path: []const u8) bool` |
| `isAbsolutePosixZ` | `pub fn isAbsolutePosixZ(path_c: [*:0]const u8) bool` |
| `windowsParsePath` | `pub fn windowsParsePath(path: []const u8) WindowsPath` |
| `parsePath` | `pub fn parsePath(path: []const u8) switch (native_os)` |
| `parsePathPosix` | `pub fn parsePathPosix(path: []const u8) PosixPath` |
| `WindowsPath2` | `pub fn WindowsPath2(comptime T: type) type` |
| `parsePathWindows` | `pub fn parsePathWindows(comptime T: type, path: []const T) WindowsPath2(T)` |
| `diskDesignator` | `pub fn diskDesignator(path: []const u8) []const u8` |
| `diskDesignatorWindows` | `pub fn diskDesignatorWindows(path: []const u8) []const u8` |
| `resolve` | `pub fn resolve(allocator: Allocator, paths: []const []const u8) Allocator.Error![]u8` |
| `resolveWindows` | `pub fn resolveWindows(allocator: Allocator, paths: []const []const u8) Allocator.Error![]u8` |
| `resolvePosix` | `pub fn resolvePosix(allocator: Allocator, paths: []const []const u8) Allocator.Error![]u8` |
| `dirname` | `pub fn dirname(path: []const u8) ?[]const u8` |
| `dirnameWindows` | `pub fn dirnameWindows(path: []const u8) ?[]const u8` |
| `dirnamePosix` | `pub fn dirnamePosix(path: []const u8) ?[]const u8` |
| `basename` | `pub fn basename(path: []const u8) []const u8` |
| `basenamePosix` | `pub fn basenamePosix(path: []const u8) []const u8` |
| `basenameWindows` | `pub fn basenameWindows(path: []const u8) []const u8` |
| `relative` | `pub fn relative(gpa: Allocator, cwd: []const u8, environ_map: ?*const std.process.Environ.Map, from: []const u8, to: []const u8,) Allocator.Error![]u8` |
| `relativeWindows` | `pub fn relativeWindows(gpa: Allocator, cwd: []const u8, environ_map: ?*const std.process.Environ.Map, from: []const u8, to: []const u8,) Allocator.Error![]u8` |
| `relativePosix` | `pub fn relativePosix(allocator: Allocator, cwd: []const u8, from: []const u8, to: []const u8) Allocator.Error![]u8` |
| `extension` | `pub fn extension(path: []const u8) []const u8` |
| `stem` | `pub fn stem(path: []const u8) []const u8` |
| `ComponentIterator` | `pub fn ComponentIterator(comptime path_type: PathType, comptime T: type) type` |
| `init` | `pub fn init(path: []const T) Self` |
| `root` | `pub fn root(self: Self) ?[]const T` |
| `first` | `pub fn first(self: *Self) ?Component` |
| `last` | `pub fn last(self: *Self) ?Component` |
| `next` | `pub fn next(self: *Self) ?Component` |
| `peekNext` | `pub fn peekNext(self: Self) ?Component` |
| `previous` | `pub fn previous(self: *Self) ?Component` |
| `peekPrevious` | `pub fn peekPrevious(self: Self) ?Component` |
| `componentIterator` | `pub fn componentIterator(path: []const u8) NativeComponentIterator` |
| `getWin32PathType` | `pub fn getWin32PathType(comptime T: type, path: []const T) Win32PathType` |

## compress / flate

| Function | Signature |
|----------|-----------|
| `size` | `pub fn size(w: Container) usize` |
| `headerSize` | `pub fn headerSize(w: Container) usize` |
| `footerSize` | `pub fn footerSize(w: Container) usize` |
| `header` | `pub fn header(container: Container) []const u8` |
| `init` | `pub fn init(containter: Container) Hasher` |
| `container` | `pub fn container(h: Hasher) Container` |
| `update` | `pub fn update(h: *Hasher, buf: []const u8) void` |
| `writeFooter` | `pub fn writeFooter(hasher: *Hasher, writer: *std.Io.Writer) std.Io.Writer.Error!void` |
| `init` | `pub fn init(containter: Container) Metadata` |
| `container` | `pub fn container(m: Metadata) Container` |

## compress / lzma

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(reader: *Reader) !RangeDecoder` |
| `initCounting` | `pub fn initCounting(reader: *Reader, n_read: *u64) !RangeDecoder` |
| `isFinished` | `pub fn isFinished(self: RangeDecoder) bool` |
| `get` | `pub fn get(self: *RangeDecoder, reader: *Reader, count: usize, n_read: *u64) !u32` |
| `decodeBit` | `pub fn decodeBit(self: *RangeDecoder, reader: *Reader, prob: *u16, n_read: *u64) !bool` |
| `parseReverseBitTree` | `pub fn parseReverseBitTree(self: *RangeDecoder, reader: *Reader, num_bits: u5, probs: []u16, offset: usize, n_read: *u64,) !u32` |
| `init` | `pub fn init(gpa: Allocator, properties: Properties) !Decode` |
| `deinit` | `pub fn deinit(self: *Decode, gpa: Allocator) void` |
| `resetState` | `pub fn resetState(self: *Decode, gpa: Allocator, new_props: Properties) !void` |
| `process` | `pub fn process(self: *Decode, reader: *Reader, allocating: *Writer.Allocating, /// `CircularBuffer` or `std.compress.lzma2.AccumBuffer`. buffer: anytype, decoder: *RangeDecoder, n_read: *u64,) !ProcessingStatus` |
| `init` | `pub fn init(dict_size: usize, mem_limit: usize) CircularBuffer` |
| `get` | `pub fn get(self: CircularBuffer, index: usize) u8` |
| `set` | `pub fn set(self: *CircularBuffer, gpa: Allocator, index: usize, value: u8) !void` |
| `lastOr` | `pub fn lastOr(self: CircularBuffer, lit: u8) u8` |
| `lastN` | `pub fn lastN(self: CircularBuffer, dist: usize) !u8` |
| `appendLiteral` | `pub fn appendLiteral(self: *CircularBuffer, gpa: Allocator, lit: u8, writer: *Writer,) !void` |
| `appendLz` | `pub fn appendLz(self: *CircularBuffer, gpa: Allocator, len: usize, dist: usize, writer: *Writer,) !void` |
| `finish` | `pub fn finish(self: *CircularBuffer, writer: *Writer) !void` |
| `deinit` | `pub fn deinit(self: *CircularBuffer, gpa: Allocator) void` |
| `BitTree` | `pub fn BitTree(comptime num_bits: usize) type` |
| `parse` | `pub fn parse(self: *@This() , reader: *Reader, decoder: *RangeDecoder, n_read: *u64) !u32` |
| `parseReverse` | `pub fn parseReverse(self: *@This() , reader: *Reader, decoder: *RangeDecoder, n_read: *u64, ) !u32` |
| `reset` | `pub fn reset(self: *@This() ) void` |
| `decode` | `pub fn decode(self: *LenDecoder, reader: *Reader, decoder: *RangeDecoder, pos_state: usize, n_read: *u64,) !usize` |
| `reset` | `pub fn reset(self: *LenDecoder) void` |
| `init` | `pub fn init(gpa: Allocator, value: u16, w: usize, h: usize) !Vec2d` |
| `deinit` | `pub fn deinit(v: *Vec2d, gpa: Allocator) void` |
| `fill` | `pub fn fill(v: *Vec2d, value: u16) void` |
| `readHeader` | `pub fn readHeader(reader: *Reader, options: Options) !Params` |
| `initParams` | `pub fn initParams(input: *Reader, gpa: Allocator, buffer: []u8, params: Decode.Params, mem_limit: usize,) !Decompress` |
| `initOptions` | `pub fn initOptions(input: *Reader, gpa: Allocator, buffer: []u8, options: Decode.Options, mem_limit: usize,) !Decompress` |
| `takeBuffer` | `pub fn takeBuffer(d: *Decompress) []u8` |
| `deinit` | `pub fn deinit(d: *Decompress) void` |

## compress / lzma2

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(memlimit: usize) AccumBuffer` |
| `appendByte` | `pub fn appendByte(self: *AccumBuffer, allocator: Allocator, byte: u8) !void` |
| `reset` | `pub fn reset(self: *AccumBuffer, writer: *Writer) !void` |
| `lastOr` | `pub fn lastOr(self: AccumBuffer, lit: u8) u8` |
| `lastN` | `pub fn lastN(self: AccumBuffer, dist: usize) !u8` |
| `appendLiteral` | `pub fn appendLiteral(self: *AccumBuffer, allocator: Allocator, lit: u8, writer: *Writer,) !void` |
| `appendLz` | `pub fn appendLz(self: *AccumBuffer, allocator: Allocator, len: usize, dist: usize, writer: *Writer,) !void` |
| `finish` | `pub fn finish(self: *AccumBuffer, writer: *Writer) !void` |
| `deinit` | `pub fn deinit(self: *AccumBuffer, allocator: Allocator) void` |
| `init` | `pub fn init(gpa: Allocator) !Decode` |
| `deinit` | `pub fn deinit(self: *Decode, gpa: Allocator) void` |
| `decompress` | `pub fn decompress(d: *Decode, reader: *Reader, allocating: *Writer.Allocating) !u64` |

## compress / flate / Compress

| Function | Signature |
|----------|-----------|
| `int` | `pub fn int(p: PackedOptionalU15) u16` |
| `init` | `pub fn init(w: *Writer) BitWriter` |
| `write` | `pub fn write(b: *BitWriter, bits: u56, n: u6) Writer.Error!void` |
| `byteAlign` | `pub fn byteAlign(b: *BitWriter) void` |
| `writeClen` | `pub fn writeClen(b: *BitWriter, hclen: u4, clen_values: []u8, clen_extra: []u8, clen_codes: [19]u16, clen_bits: [19]u4,) Writer.Error!void` |
| `int` | `pub fn int(h: BlockHeader) u3` |
| `int` | `pub fn int(h: Dynamic) u17` |
| `init` | `pub fn init(output: *Writer, buffer: []u8, container: flate.Container, opts: Options,) Writer.Error!Compress` |
| `smaller` | `pub fn smaller(a: Node, b: Node) bool` |
| `build` | `pub fn build(freqs: []const u16, out_codes: []u16, out_bits: []u4, max_bits: u4, incomplete_allowed: bool,) struct` |
| `val` | `pub fn val(c: @This() ) flate.Container` |
| `init` | `pub fn init(output: *Writer, buffer: []u8, container: flate.Container) Writer.Error!Raw` |
| `init` | `pub fn init(buf: []u8, container: flate.Container) @This()` |
| `init` | `pub fn init(output: *Writer, buffer: []u8, container: flate.Container) Writer.Error!Huffman` |

## compress / flate / Decompress

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(input: *Reader, container: Container, buffer: []u8) Decompress` |
| `asc` | `pub fn asc(_: void, a: Symbol, b: Symbol) bool` |
| `generate` | `pub fn generate(self: *Self, lens: []const u4) !void` |
| `find` | `pub fn find(self: *Self, code: u16) !Symbol` |

## compress / flate / token

| Function | Signature |
|----------|-----------|
| `fromVal` | `pub fn fromVal(v: Value) @This()` |
| `base` | `pub fn base(c: @This() ) Value` |
| `extraBits` | `pub fn extraBits(c: @This() ) std.math.IntFittingRange(0, max_extra)` |
| `toInt` | `pub fn toInt(c: @This() ) u5` |
| `fromInt` | `pub fn fromInt(x: u5) @This()` |
| `fromVal` | `pub fn fromVal(v: u8) LookupLenCode` |
| `base` | `pub fn base(c: LookupLenCode) u8` |
| `extraBits` | `pub fn extraBits(c: LookupLenCode) u3` |
| `toInt` | `pub fn toInt(c: LookupLenCode) u5` |
| `fromInt` | `pub fn fromInt(x: u5) LookupLenCode` |
| `fromVal` | `pub fn fromVal(v: u15) LookupDistCode` |
| `base` | `pub fn base(c: LookupDistCode) u15` |
| `extraBits` | `pub fn extraBits(c: LookupDistCode) u4` |
| `toInt` | `pub fn toInt(c: LookupDistCode) u5` |
| `fromInt` | `pub fn fromInt(x: u5) LookupDistCode` |

## compress / xz / Decompress

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(input: *Reader, gpa: Allocator, /// Decompress takes ownership of this buffer and resizes it with `gpa`. buffer: []u8,) !Decompress` |
| `takeBuffer` | `pub fn takeBuffer(d: *Decompress) []u8` |
| `deinit` | `pub fn deinit(d: *Decompress) void` |

## compress / zstd / Decompress

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(input: *Reader, buffer: []u8, options: Options) Decompress` |
| `kind` | `pub fn kind(m: Magic) ?Kind` |
| `isSkippable` | `pub fn isSkippable(m: Magic) bool` |
| `decode` | `pub fn decode(in: *Reader) DecodeError!Header` |
| `windowSize` | `pub fn windowSize(header: Header) ?u64` |
| `prepare` | `pub fn prepare(self: *Decode, in: *Reader, remaining: *Limit, literals: LiteralsSection, sequences_header: SequencesSection.Header,) PrepareError!void` |
| `readInitialFseState` | `pub fn readInitialFseState(self: *Decode, bit_reader: *ReverseBitReader) error` |
| `init` | `pub fn init(frame_header: Frame.Zstandard.Header, window_size_max: usize, verify_checksum: bool,) InitError!Frame` |
| `decode` | `pub fn decode(in: *Reader, remaining: *Limit) !Header` |
| `query` | `pub fn query(self: HuffmanTree, index: usize, prefix: u16) error` |
| `weightToBitCount` | `pub fn weightToBitCount(weight: u4, max_bit_count: u4) u4` |
| `decode` | `pub fn decode(in: *Reader, remaining: *Limit) HuffmanTree.DecodeError!HuffmanTree` |
| `streamCount` | `pub fn streamCount(size_format: u2, block_type: BlockType) StreamCount` |
| `decode` | `pub fn decode(in: *Reader, remaining: *Limit, buffer: []u8) DecodeError!LiteralsSection` |
| `decode` | `pub fn decode(in: *Reader, remaining: *Limit) DecodeError!Header` |
| `decode` | `pub fn decode(bit_reader: *BitReader, expected_symbol_count: usize, max_accuracy_log: u4, entries: []Table.Fse,) !usize` |
| `build` | `pub fn build(values: []const u16, entries: []Table.Fse) !void` |

## debug / Coverage

| Function | Signature |
|----------|-----------|
| `eql` | `pub fn eql(self: @This() , a: String, b: String, b_index: usize) bool` |
| `hash` | `pub fn hash(self: @This() , a: String) u32` |
| `eql` | `pub fn eql(self: @This() , a_slice: []const u8, b: String, b_index: usize) bool` |
| `hash` | `pub fn hash(self: @This() , a: []const u8) u32` |
| `hash` | `pub fn hash(self: MapContext, a: File) u32` |
| `eql` | `pub fn eql(self: MapContext, a: File, b: File, b_index: usize) bool` |
| `hash` | `pub fn hash(self: @This() , a: Entry) u32` |
| `eql` | `pub fn eql(self: @This() , a: Entry, b: File, b_index: usize) bool` |
| `deinit` | `pub fn deinit(cov: *Coverage, gpa: Allocator) void` |
| `fileAt` | `pub fn fileAt(cov: *Coverage, index: File.Index) *File` |
| `stringAt` | `pub fn stringAt(cov: *Coverage, index: String) [:0]const u8` |
| `resolveAddressesDwarf` | `pub fn resolveAddressesDwarf(cov: *Coverage, gpa: Allocator, io: Io, endian: std.builtin.Endian, /// Asserts the addresses are in ascending order. sorted_pc_addrs: []const u64, /// Asserts its length equals length of `sorted_pc_addrs`. output: []S...` |
| `addStringAssumeCapacity` | `pub fn addStringAssumeCapacity(cov: *Coverage, s: []const u8) String` |

## debug / Dwarf

| Function | Signature |
|----------|-----------|
| `isInvalid` | `pub fn isInvalid(le: LineEntry) bool` |
| `findSource` | `pub fn findSource(slc: *const SrcLocCache, address: u64) !LineEntry` |
| `getAttrString` | `pub fn getAttrString(self: *const Die, di: *Dwarf, endian: Endian, id: u64, opt_str: ?[]const u8, compile_unit: *const CompileUnit,) error` |
| `open` | `pub fn open(d: *Dwarf, gpa: Allocator, endian: Endian) OpenError!void` |
| `section` | `pub fn section(di: Dwarf, dwarf_section: Section.Id) ?[]const u8` |
| `deinit` | `pub fn deinit(di: *Dwarf, gpa: Allocator) void` |
| `getSymbolName` | `pub fn getSymbolName(di: *const Dwarf, address: u64) ?[]const u8` |
| `populateRanges` | `pub fn populateRanges(d: *Dwarf, gpa: Allocator, endian: Endian) ScanError!void` |
| `lessThan` | `pub fn lessThan(ctx: void, a: Range, b: Range) bool` |
| `init` | `pub fn init(ranges_value: *const FormValue, di: *const Dwarf, endian: Endian, compile_unit: *const CompileUnit) !@This()` |
| `next` | `pub fn next(self: *@This() ) !?PcRange` |
| `findCompileUnit` | `pub fn findCompileUnit(di: *const Dwarf, endian: Endian, target_address: u64) !*CompileUnit` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a_index: usize, b_index: usize) bool` |
| `populateSrcLocCache` | `pub fn populateSrcLocCache(d: *Dwarf, gpa: Allocator, endian: Endian, cu: *CompileUnit) ScanError!void` |
| `getLineNumberInfo` | `pub fn getLineNumberInfo(d: *Dwarf, gpa: Allocator, endian: Endian, compile_unit: *CompileUnit, target_address: u64,) !std.debug.SourceLocation` |
| `reset` | `pub fn reset(self: *LineNumberProgram) void` |
| `init` | `pub fn init(is_stmt: bool, version: u16) LineNumberProgram` |
| `addRow` | `pub fn addRow(prog: *LineNumberProgram, gpa: Allocator, table: *CompileUnit.SrcLocCache.LineTable) !void` |
| `readUnitHeader` | `pub fn readUnitHeader(r: *Reader, endian: Endian) ScanError!UnitHeader` |
| `compactUnwindToDwarfRegNumber` | `pub fn compactUnwindToDwarfRegNumber(unwind_reg_number: u3) !u16` |
| `ipRegNum` | `pub fn ipRegNum(arch: std.Target.Cpu.Arch) ?u16` |
| `fpRegNum` | `pub fn fpRegNum(arch: std.Target.Cpu.Arch) u16` |
| `spRegNum` | `pub fn spRegNum(arch: std.Target.Cpu.Arch) u16` |
| `supportsUnwinding` | `pub fn supportsUnwinding(target: *const std.Target) bool` |
| `bad` | `pub fn bad() error` |
| `invalidDebugInfoDetected` | `pub fn invalidDebugInfoDetected() void` |
| `missing` | `pub fn missing() error` |

## debug / ElfFile

| Function | Signature |
|----------|-----------|
| `native` | `pub fn native(exe_path: []const u8) DebugInfoSearchPaths` |
| `deinit` | `pub fn deinit(ef: *ElfFile, gpa: Allocator) void` |
| `load` | `pub fn load(gpa: Allocator, io: Io, elf_file: Io.File, opt_build_id: ?[]const u8, di_search_paths: *const DebugInfoSearchPaths,) LoadError!ElfFile` |
| `searchSymtab` | `pub fn searchSymtab(ef: *ElfFile, gpa: Allocator, vaddr: u64) error` |

## debug / Info

| Function | Signature |
|----------|-----------|
| `load` | `pub fn load(gpa: Allocator, io: Io, path: Path, coverage: *Coverage, format: std.Target.ObjectFormat, arch: std.Target.Cpu.Arch,) LoadError!Info` |
| `deinit` | `pub fn deinit(info: *Info, gpa: Allocator) void` |
| `resolveAddresses` | `pub fn resolveAddresses(info: *Info, gpa: Allocator, io: Io, /// Asserts the addresses are in ascending order. sorted_pc_addrs: []const u64, /// Asserts its length equals length of `sorted_pc_addrs`. output: []SourceLocation,) ResolveAddressesErro...` |

## debug / MachOFile

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(mf: *MachOFile, gpa: Allocator) void` |
| `load` | `pub fn load(gpa: Allocator, io: Io, path: []const u8, arch: std.Target.Cpu.Arch) Error!MachOFile` |
| `getDwarfForAddress` | `pub fn getDwarfForAddress(mf: *MachOFile, gpa: Allocator, io: Io, vaddr: u64) !struct` |
| `lookupSymbolName` | `pub fn lookupSymbolName(mf: *MachOFile, vaddr: u64) error` |
| `hash` | `pub fn hash(ctx: SymbolAdapter, sym_name: []const u8) u32` |
| `eql` | `pub fn eql(ctx: SymbolAdapter, a_sym_name: []const u8, b_sym_index: u32, b_index: usize) bool` |

## debug / Pdb

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *Module, allocator: Allocator) void` |
| `init` | `pub fn init(gpa: Allocator, file_reader: *File.Reader) !Pdb` |
| `deinit` | `pub fn deinit(self: *Pdb) void` |
| `parseDbiStream` | `pub fn parseDbiStream(self: *Pdb) !void` |
| `parseInfoStream` | `pub fn parseInfoStream(self: *Pdb) !void` |
| `getSymbolName` | `pub fn getSymbolName(self: *Pdb, module: *Module, address: u64) ?[]const u8` |
| `getLineNumberInfo` | `pub fn getLineNumberInfo(self: *Pdb, module: *Module, address: u64) !std.debug.SourceLocation` |
| `getModule` | `pub fn getModule(self: *Pdb, index: usize) !?*Module` |
| `getStreamById` | `pub fn getStreamById(self: *Pdb, id: u32) ?*MsfStream` |
| `getStream` | `pub fn getStream(self: *Pdb, stream: pdb.StreamType) ?*MsfStream` |
| `logicalPos` | `pub fn logicalPos(ms: *const MsfStream) u64` |
| `seekBy` | `pub fn seekBy(ms: *MsfStream, len: i64) !void` |
| `seekTo` | `pub fn seekTo(ms: *MsfStream, len: u64) !void` |

## debug / cpu_context

| Function | Signature |
|----------|-----------|
| `fromPosixSignalContext` | `pub fn fromPosixSignalContext(ctx_ptr: ?*const anyopaque) ?Native` |
| `fromWindowsContext` | `pub fn fromWindowsContext(ctx: *const std.os.windows.CONTEXT) Native` |
| `current` | `pub fn current() Aarch64` |
| `getFp` | `pub fn getFp(ctx: *const Aarch64) u64` |
| `getPc` | `pub fn getPc(ctx: *const Aarch64) u64` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Aarch64, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Arc` |
| `getFp` | `pub fn getFp(ctx: *const Arc) u32` |
| `getPc` | `pub fn getPc(ctx: *const Arc) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Arc, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Arm` |
| `getFp` | `pub fn getFp(ctx: *const Arm) u32` |
| `getPc` | `pub fn getPc(ctx: *const Arm) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Arm, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Csky` |
| `getFp` | `pub fn getFp(ctx: *const Csky) u32` |
| `getPc` | `pub fn getPc(ctx: *const Csky) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Csky, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Hexagon` |
| `getFp` | `pub fn getFp(ctx: *const Hexagon) u32` |
| `getPc` | `pub fn getPc(ctx: *const Hexagon) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Hexagon, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Kvx` |
| `getFp` | `pub fn getFp(ctx: *const Kvx) u64` |
| `getPc` | `pub fn getPc(ctx: *const Kvx) u64` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Kvx, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Lanai` |
| `getFp` | `pub fn getFp(ctx: *const Lanai) u32` |
| `getPc` | `pub fn getPc(ctx: *const Lanai) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Lanai, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() LoongArch` |
| `getFp` | `pub fn getFp(ctx: *const LoongArch) Gpr` |
| `getPc` | `pub fn getPc(ctx: *const LoongArch) Gpr` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *LoongArch, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() M68k` |
| `getFp` | `pub fn getFp(ctx: *const M68k) u32` |
| `getPc` | `pub fn getPc(ctx: *const M68k) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *M68k, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Mips` |
| `getFp` | `pub fn getFp(ctx: *const Mips) usize` |
| `getPc` | `pub fn getPc(ctx: *const Mips) usize` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Mips, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Or1k` |
| `getFp` | `pub fn getFp(ctx: *const Or1k) u32` |
| `getPc` | `pub fn getPc(ctx: *const Or1k) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Or1k, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Powerpc` |
| `getFp` | `pub fn getFp(ctx: *const Powerpc) Gpr` |
| `getPc` | `pub fn getPc(ctx: *const Powerpc) Gpr` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Powerpc, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Riscv` |
| `getFp` | `pub fn getFp(ctx: *const Riscv) Gpr` |
| `getPc` | `pub fn getPc(ctx: *const Riscv) Gpr` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Riscv, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() S390x` |
| `getFp` | `pub fn getFp(ctx: *const S390x) u64` |
| `getPc` | `pub fn getPc(ctx: *const S390x) u64` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *S390x, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Sparc` |
| `getFp` | `pub fn getFp(ctx: *const Sparc) Gpr` |
| `getPc` | `pub fn getPc(ctx: *const Sparc) Gpr` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Sparc, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() Ve` |
| `getFp` | `pub fn getFp(ctx: *const Ve) u64` |
| `getPc` | `pub fn getPc(ctx: *const Ve) u64` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *Ve, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() X86_16` |
| `getFp` | `pub fn getFp(ctx: *const X86_16) u16` |
| `getPc` | `pub fn getPc(ctx: *const X86_16) u16` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *X86_16, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() X86` |
| `getFp` | `pub fn getFp(ctx: *const X86) u32` |
| `getPc` | `pub fn getPc(ctx: *const X86) u32` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *X86, register_num: u16) DwarfRegisterError![]u8` |
| `current` | `pub fn current() X86_64` |
| `getFp` | `pub fn getFp(ctx: *const X86_64) usize` |
| `getPc` | `pub fn getPc(ctx: *const X86_64) usize` |
| `dwarfRegisterBytes` | `pub fn dwarfRegisterBytes(ctx: *X86_64, register_num: u16) DwarfRegisterError![]u8` |

## debug / no_panic

| Function | Signature |
|----------|-----------|
| `call` | `pub fn call(_: []const u8, _: ?usize) noreturn` |
| `sentinelMismatch` | `pub fn sentinelMismatch(_: anytype, _: anytype) noreturn` |
| `unwrapError` | `pub fn unwrapError(_: anyerror) noreturn` |
| `outOfBounds` | `pub fn outOfBounds(_: usize, _: usize) noreturn` |
| `startGreaterThanEnd` | `pub fn startGreaterThanEnd(_: usize, _: usize) noreturn` |
| `inactiveUnionField` | `pub fn inactiveUnionField(_: anytype, _: anytype) noreturn` |
| `sliceCastLenRemainder` | `pub fn sliceCastLenRemainder(_: usize) noreturn` |
| `reachedUnreachable` | `pub fn reachedUnreachable() noreturn` |
| `unwrapNull` | `pub fn unwrapNull() noreturn` |
| `castToNull` | `pub fn castToNull() noreturn` |
| `incorrectAlignment` | `pub fn incorrectAlignment() noreturn` |
| `invalidErrorCode` | `pub fn invalidErrorCode() noreturn` |
| `integerOutOfBounds` | `pub fn integerOutOfBounds() noreturn` |
| `integerOverflow` | `pub fn integerOverflow() noreturn` |
| `shlOverflow` | `pub fn shlOverflow() noreturn` |
| `shrOverflow` | `pub fn shrOverflow() noreturn` |
| `divideByZero` | `pub fn divideByZero() noreturn` |
| `exactDivisionRemainder` | `pub fn exactDivisionRemainder() noreturn` |
| `integerPartOutOfBounds` | `pub fn integerPartOutOfBounds() noreturn` |
| `corruptSwitch` | `pub fn corruptSwitch() noreturn` |
| `shiftRhsTooBig` | `pub fn shiftRhsTooBig() noreturn` |
| `invalidEnumValue` | `pub fn invalidEnumValue() noreturn` |
| `forLenMismatch` | `pub fn forLenMismatch() noreturn` |
| `copyLenMismatch` | `pub fn copyLenMismatch() noreturn` |
| `memcpyAlias` | `pub fn memcpyAlias() noreturn` |
| `noreturnReturned` | `pub fn noreturnReturned() noreturn` |

## debug / simple_panic

| Function | Signature |
|----------|-----------|
| `call` | `pub fn call(msg: []const u8, ra: ?usize) noreturn` |
| `sentinelMismatch` | `pub fn sentinelMismatch(expected: anytype, found: @TypeOf(expected) ) noreturn` |
| `unwrapError` | `pub fn unwrapError(err: anyerror) noreturn` |
| `outOfBounds` | `pub fn outOfBounds(index: usize, len: usize) noreturn` |
| `startGreaterThanEnd` | `pub fn startGreaterThanEnd(start: usize, end: usize) noreturn` |
| `inactiveUnionField` | `pub fn inactiveUnionField(active: anytype, accessed: @TypeOf(active) ) noreturn` |
| `sliceCastLenRemainder` | `pub fn sliceCastLenRemainder(src_len: usize) noreturn` |
| `reachedUnreachable` | `pub fn reachedUnreachable() noreturn` |
| `unwrapNull` | `pub fn unwrapNull() noreturn` |
| `castToNull` | `pub fn castToNull() noreturn` |
| `incorrectAlignment` | `pub fn incorrectAlignment() noreturn` |
| `invalidErrorCode` | `pub fn invalidErrorCode() noreturn` |
| `integerOutOfBounds` | `pub fn integerOutOfBounds() noreturn` |
| `integerOverflow` | `pub fn integerOverflow() noreturn` |
| `shlOverflow` | `pub fn shlOverflow() noreturn` |
| `shrOverflow` | `pub fn shrOverflow() noreturn` |
| `divideByZero` | `pub fn divideByZero() noreturn` |
| `exactDivisionRemainder` | `pub fn exactDivisionRemainder() noreturn` |
| `integerPartOutOfBounds` | `pub fn integerPartOutOfBounds() noreturn` |
| `corruptSwitch` | `pub fn corruptSwitch() noreturn` |
| `shiftRhsTooBig` | `pub fn shiftRhsTooBig() noreturn` |
| `invalidEnumValue` | `pub fn invalidEnumValue() noreturn` |
| `forLenMismatch` | `pub fn forLenMismatch() noreturn` |
| `copyLenMismatch` | `pub fn copyLenMismatch() noreturn` |
| `memcpyAlias` | `pub fn memcpyAlias() noreturn` |
| `noreturnReturned` | `pub fn noreturnReturned() noreturn` |

## debug / SelfInfo / Elf

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void` |
| `getModuleName` | `pub fn getModuleName(si: *SelfInfo, io: Io, address: usize) Error![]const u8` |
| `getModuleSlide` | `pub fn getModuleSlide(si: *SelfInfo, io: Io, address: usize) Error!usize` |
| `unwindFrame` | `pub fn unwindFrame(si: *SelfInfo, io: Io, context: *UnwindContext) Error!usize` |

## debug / SelfInfo / MachO

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void` |
| `getModuleName` | `pub fn getModuleName(si: *SelfInfo, io: Io, address: usize) Error![]const u8` |
| `getModuleSlide` | `pub fn getModuleSlide(si: *SelfInfo, io: Io, address: usize) Error!usize` |
| `unwindFrame` | `pub fn unwindFrame(si: *SelfInfo, io: Io, context: *UnwindContext) Error!usize` |
| `hash` | `pub fn hash(_: Adapter, text_base: usize) u32` |
| `eql` | `pub fn eql(_: Adapter, a_text_base: usize, b_module: Module, b_index: usize) bool` |
| `hash` | `pub fn hash(_: Context, module: Module) u32` |
| `eql` | `pub fn eql(_: Context, a_module: Module, b_module: Module, b_index: usize) bool` |

## debug / SelfInfo / Windows

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(si: *SelfInfo, io: Io) void` |
| `getModuleName` | `pub fn getModuleName(si: *SelfInfo, io: Io, address: usize) Error![]const u8` |
| `getModuleSlide` | `pub fn getModuleSlide(si: *SelfInfo, io: Io, address: usize) Error!usize` |
| `init` | `pub fn init(ctx: *const std.debug.cpu_context.Native) UnwindContext` |
| `deinit` | `pub fn deinit(ctx: *UnwindContext) void` |
| `getFp` | `pub fn getFp(ctx: *UnwindContext) usize` |
| `unwindFrame` | `pub fn unwindFrame(si: *SelfInfo, io: Io, context: *UnwindContext) Error!usize` |

## debug / Dwarf / SelfUnwinder

| Function | Signature |
|----------|-----------|
| `find` | `pub fn find(entries: []const CacheEntry, pc: usize) ?*const CacheEntry` |
| `populate` | `pub fn populate(entry: *const CacheEntry, entries: []CacheEntry) void` |
| `init` | `pub fn init(cpu_context: *const std.debug.cpu_context.Native) SelfUnwinder` |
| `deinit` | `pub fn deinit(unwinder: *SelfUnwinder) void` |
| `getFp` | `pub fn getFp(unwinder: *const SelfUnwinder) usize` |
| `computeRules` | `pub fn computeRules(unwinder: *SelfUnwinder, gpa: Allocator, unwind: *const Dwarf.Unwind, load_offset: usize, explicit_fde_offset: ?usize,) !CacheEntry` |
| `next` | `pub fn next(unwinder: *SelfUnwinder, gpa: Allocator, cache_entry: *const CacheEntry) std.debug.SelfInfoError!usize` |
| `regNative` | `pub fn regNative(ctx: *std.debug.cpu_context.Native, num: u16) error` |

## debug / Dwarf / Unwind

| Function | Signature |
|----------|-----------|
| `initEhFrameHdr` | `pub fn initEhFrameHdr(header: EhFrameHeader, section_vaddr: u64, section_bytes_ptr: [*]const u8) Unwind` |
| `initSection` | `pub fn initSection(section: Section, section_vaddr: u64, section_bytes: []const u8) Unwind` |
| `deinit` | `pub fn deinit(unwind: *Unwind, gpa: Allocator) void` |
| `parse` | `pub fn parse(eh_frame_hdr_vaddr: u64, eh_frame_hdr_bytes: []const u8, addr_size_bytes: u8, endian: Endian,) !EhFrameHeader` |
| `prepare` | `pub fn prepare(unwind: *Unwind, gpa: Allocator, addr_size_bytes: u8, endian: Endian, need_lookup: bool, /// The `__eh_frame` section in Mach-O binaries deviates from the standard `.eh_frame` section /// in one way which this function needs to be a...` |
| `lookupPc` | `pub fn lookupPc(unwind: *const Unwind, pc: u64, addr_size_bytes: u8, endian: Endian) !?u64` |
| `getFde` | `pub fn getFde(unwind: *const Unwind, fde_offset: u64, endian: Endian) !struct` |

## debug / Dwarf / expression

| Function | Signature |
|----------|-----------|
| `StackMachine` | `pub fn StackMachine(comptime options: Options) type` |
| `asIntegral` | `pub fn asIntegral(self: Value) !addr_type` |
| `reset` | `pub fn reset(self: *Self) void` |
| `deinit` | `pub fn deinit(self: *Self, allocator: std.mem.Allocator) void` |
| `readOperand` | `pub fn readOperand(reader: *std.Io.Reader, opcode: u8, context: Context) !?Operand` |
| `run` | `pub fn run(self: *Self, expression: []const u8, allocator: std.mem.Allocator, context: Context, initial_value: ?usize,) Error!?Value` |
| `step` | `pub fn step(self: *Self, stream: *std.Io.Reader, allocator: std.mem.Allocator, context: Context,) Error!bool` |
| `Builder` | `pub fn Builder(comptime options: Options) type` |
| `writeOpcode` | `pub fn writeOpcode(writer: *Writer, comptime opcode: u8) !void` |
| `writeLiteral` | `pub fn writeLiteral(writer: *Writer, literal: u8) !void` |
| `writeConst` | `pub fn writeConst(writer: *Writer, comptime T: type, value: T) !void` |
| `writeConstx` | `pub fn writeConstx(writer: *Writer, debug_addr_offset: anytype) !void` |
| `writeConstType` | `pub fn writeConstType(writer: *Writer, die_offset: anytype, value_bytes: []const u8) !void` |
| `writeAddr` | `pub fn writeAddr(writer: *Writer, value: addr_type) !void` |
| `writeAddrx` | `pub fn writeAddrx(writer: *Writer, debug_addr_offset: anytype) !void` |
| `writeFbreg` | `pub fn writeFbreg(writer: *Writer, offset: anytype) !void` |
| `writeBreg` | `pub fn writeBreg(writer: *Writer, register: u8, offset: anytype) !void` |
| `writeBregx` | `pub fn writeBregx(writer: *Writer, register: anytype, offset: anytype) !void` |
| `writeRegvalType` | `pub fn writeRegvalType(writer: *Writer, register: anytype, offset: anytype) !void` |
| `writePick` | `pub fn writePick(writer: *Writer, index: u8) !void` |
| `writeDerefSize` | `pub fn writeDerefSize(writer: *Writer, size: u8) !void` |
| `writeXDerefSize` | `pub fn writeXDerefSize(writer: *Writer, size: u8) !void` |
| `writeDerefType` | `pub fn writeDerefType(writer: *Writer, size: u8, die_offset: anytype) !void` |
| `writeXDerefType` | `pub fn writeXDerefType(writer: *Writer, size: u8, die_offset: anytype) !void` |
| `writePlusUconst` | `pub fn writePlusUconst(writer: *Writer, uint_value: anytype) !void` |
| `writeSkip` | `pub fn writeSkip(writer: *Writer, offset: i16) !void` |
| `writeBra` | `pub fn writeBra(writer: *Writer, offset: i16) !void` |
| `writeCall` | `pub fn writeCall(writer: *Writer, comptime T: type, offset: T) !void` |
| `writeCallRef` | `pub fn writeCallRef(writer: *Writer, comptime is_64: bool, value: if (is_64) u64 else u32) !void` |
| `writeConvert` | `pub fn writeConvert(writer: *Writer, die_offset: anytype) !void` |
| `writeReinterpret` | `pub fn writeReinterpret(writer: *Writer, die_offset: anytype) !void` |
| `writeEntryValue` | `pub fn writeEntryValue(writer: *Writer, expression: []const u8) !void` |
| `writeReg` | `pub fn writeReg(writer: *Writer, register: u8) !void` |
| `writeRegx` | `pub fn writeRegx(writer: *Writer, register: anytype) !void` |
| `writeImplicitValue` | `pub fn writeImplicitValue(writer: *Writer, value_bytes: []const u8) !void` |

## debug / Dwarf / Unwind / VirtualMachine

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *VirtualMachine, gpa: Allocator) void` |
| `reset` | `pub fn reset(self: *VirtualMachine) void` |
| `rowColumns` | `pub fn rowColumns(self: *const VirtualMachine, row: *const Row) []Column` |
| `populateCieLastRow` | `pub fn populateCieLastRow(gpa: Allocator, cie: *Unwind.CommonInformationEntry, addr_size_bytes: u8, endian: std.builtin.Endian,) !void` |
| `runTo` | `pub fn runTo(vm: *VirtualMachine, gpa: Allocator, pc: u64, cie: *const Unwind.CommonInformationEntry, fde: *const Unwind.FrameDescriptionEntry, addr_size_bytes: u8, endian: std.builtin.Endian,) !Row` |
| `read` | `pub fn read(reader: *std.Io.Reader, addr_size_bytes: u8, endian: std.builtin.Endian,) !Instruction` |

## http / ChunkParser

| Function | Signature |
|----------|-----------|
| `feed` | `pub fn feed(p: *ChunkParser, bytes: []const u8) usize` |

## http / HeadParser

| Function | Signature |
|----------|-----------|
| `feed` | `pub fn feed(p: *HeadParser, bytes: []const u8) usize` |

## http / HeaderIterator

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(bytes: []const u8) HeaderIterator` |
| `next` | `pub fn next(it: *HeaderIterator) ?std.http.Header` |

## hash / Adler32

| Function | Signature |
|----------|-----------|
| `permute` | `pub fn permute(state: u32, input: []const u8) u32` |
| `update` | `pub fn update(a: *Adler32, input: []const u8) void` |
| `hash` | `pub fn hash(input: []const u8) u32` |

## hash / auto_hash

| Function | Signature |
|----------|-----------|
| `hashPointer` | `pub fn hashPointer(hasher: anytype, key: anytype, comptime strat: HashStrategy) void` |
| `hashArray` | `pub fn hashArray(hasher: anytype, key: anytype, comptime strat: HashStrategy) void` |
| `hash` | `pub fn hash(hasher: anytype, key: anytype, comptime strat: HashStrategy) void` |
| `autoHash` | `pub fn autoHash(hasher: anytype, key: anytype) void` |
| `init` | `pub fn init(allocator: mem.Allocator, a_: u32, b_: u16, c_: bool) !Self` |

## hash / benchmark

| Function | Signature |
|----------|-----------|
| `benchmarkHash` | `pub fn benchmarkHash(comptime H: anytype, bytes: usize, allocator: std.mem.Allocator) !Result` |
| `benchmarkHashSmallKeys` | `pub fn benchmarkHashSmallKeys(comptime H: anytype, key_size: usize, bytes: usize, allocator: std.mem.Allocator) !Result` |
| `benchmarkHashSmallKeysArrayPtr` | `pub fn benchmarkHashSmallKeysArrayPtr(comptime H: anytype, comptime key_size: usize, bytes: usize, allocator: std.mem.Allocator,) !Result` |
| `benchmarkHashSmallKeysArray` | `pub fn benchmarkHashSmallKeysArray(comptime H: anytype, comptime key_size: usize, bytes: usize, allocator: std.mem.Allocator,) !Result` |
| `benchmarkHashSmallApi` | `pub fn benchmarkHashSmallApi(comptime H: anytype, key_size: usize, bytes: usize, allocator: std.mem.Allocator) !Result` |
| `main` | `pub fn main(init: std.process.Init) !void` |

## hash / cityhash

| Function | Signature |
|----------|-----------|
| `hash` | `pub fn hash(str: []const u8) u32` |
| `hash` | `pub fn hash(str: []const u8) u64` |
| `hashWithSeed` | `pub fn hashWithSeed(str: []const u8, seed: u64) u64` |
| `hashWithSeeds` | `pub fn hashWithSeeds(str: []const u8, seed0: u64, seed1: u64) u64` |

## hash / fnv

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init() Self` |
| `update` | `pub fn update(self: *Self, input: []const u8) void` |
| `final` | `pub fn final(self: *Self) T` |
| `hash` | `pub fn hash(input: []const u8) T` |

## hash / murmur

| Function | Signature |
|----------|-----------|
| `hash` | `pub fn hash(str: []const u8) u32` |
| `hashWithSeed` | `pub fn hashWithSeed(str: []const u8, seed: u32) u32` |
| `hashUint32` | `pub fn hashUint32(v: u32) u32` |
| `hashUint32WithSeed` | `pub fn hashUint32WithSeed(v: u32, seed: u32) u32` |
| `hashUint64` | `pub fn hashUint64(v: u64) u32` |
| `hashUint64WithSeed` | `pub fn hashUint64WithSeed(v: u64, seed: u32) u32` |
| `hash` | `pub fn hash(str: []const u8) u64` |
| `hashWithSeed` | `pub fn hashWithSeed(str: []const u8, seed: u64) u64` |
| `hashUint32` | `pub fn hashUint32(v: u32) u64` |
| `hashUint32WithSeed` | `pub fn hashUint32WithSeed(v: u32, seed: u64) u64` |
| `hashUint64` | `pub fn hashUint64(v: u64) u64` |
| `hashUint64WithSeed` | `pub fn hashUint64WithSeed(v: u64, seed: u64) u64` |

## hash / verify

| Function | Signature |
|----------|-----------|
| `smhasher` | `pub fn smhasher(comptime hash_fn: anytype) u32` |
| `iterativeApi` | `pub fn iterativeApi(comptime Hash: anytype) !void` |

## hash / wyhash

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(seed: u64) Wyhash` |
| `update` | `pub fn update(self: *Wyhash, input: []const u8) void` |
| `final` | `pub fn final(self: *Wyhash) u64` |
| `hash` | `pub fn hash(seed: u64, input: []const u8) u64` |

## hash / xxhash

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(seed: u64) XxHash64` |
| `update` | `pub fn update(self: *XxHash64, input: anytype) void` |
| `final` | `pub fn final(self: *XxHash64) u64` |
| `hash` | `pub fn hash(seed: u64, input: anytype) u64` |
| `init` | `pub fn init(seed: u32) XxHash32` |
| `update` | `pub fn update(self: *XxHash32, input: []const u8) void` |
| `final` | `pub fn final(self: *XxHash32) u32` |
| `hash` | `pub fn hash(seed: u32, input: anytype) u32` |
| `init` | `pub fn init(seed: u64) XxHash3` |
| `update` | `pub fn update(self: *XxHash3, input: anytype) void` |
| `final` | `pub fn final(self: *XxHash3) u64` |

## hash / crc / impl

| Function | Signature |
|----------|-----------|
| `Algorithm` | `pub fn Algorithm(comptime W: type) type` |
| `Crc` | `pub fn Crc(comptime W: type, comptime algorithm: Algorithm(W) ) type` |
| `init` | `pub fn init() Self` |
| `update` | `pub fn update(self: *Self, bytes: []const u8) void` |
| `final` | `pub fn final(self: Self) W` |
| `hash` | `pub fn hash(bytes: []const u8) W` |

## c / darwin

| Function | Signature |
|----------|-----------|
| `MAKE_TAG` | `pub fn MAKE_TAG(tag: u8) u32` |
| `sendAndRcv` | `pub fn sendAndRcv(send: MACH.SEND, rcv: MACH.RCV) mach_msg_option_t` |
| `mach_task_self` | `pub fn mach_task_self() callconv(.c) mach_port_t` |
| `extractResourceError` | `pub fn extractResourceError(ret: mach_msg_return_t) struct` |

## c / freebsd

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This() ) timespec` |
| `mtime` | `pub fn mtime(self: @This() ) timespec` |
| `ctime` | `pub fn ctime(self: @This() ) timespec` |
| `birthtime` | `pub fn birthtime(self: @This() ) timespec` |

## c / haiku

| Function | Signature |
|----------|-----------|
| `getName` | `pub fn getName(dirent: *const DirEnt) [*:0]const u8` |

## c / illumos

| Function | Signature |
|----------|-----------|
| `isException` | `pub fn isException(event: u32) bool` |
| `IO` | `pub fn IO(io_type: u8, nr: u8) i32` |
| `IOR` | `pub fn IOR(io_type: u8, nr: u8, comptime IOT: type) i32` |
| `IOW` | `pub fn IOW(io_type: u8, nr: u8, comptime IOT: type) i32` |
| `IOWR` | `pub fn IOWR(io_type: u8, nr: u8, comptime IOT: type) i32` |

## c / netbsd

| Function | Signature |
|----------|-----------|
| `CLASS` | `pub fn CLASS(t: anytype) @TypeOf(t)` |
| `DSCP` | `pub fn DSCP(t: anytype) @TypeOf(t)` |
| `ECN` | `pub fn ECN(t: anytype) @TypeOf(t)` |

## Random / Ascon

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(secret_seed: [secret_seed_length]u8) Self` |
| `addEntropy` | `pub fn addEntropy(self: *Self, bytes: []const u8) void` |
| `random` | `pub fn random(self: *Self) std.Random` |
| `fill` | `pub fn fill(self: *Self, buf: []u8) void` |

## Random / ChaCha

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(secret_seed: [secret_seed_length]u8) Self` |
| `addEntropy` | `pub fn addEntropy(self: *Self, bytes: []const u8) void` |
| `random` | `pub fn random(self: *Self) std.Random` |
| `fill` | `pub fn fill(self: *Self, buf_: []u8) void` |

## Random / Isaac64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Isaac64` |
| `random` | `pub fn random(self: *Isaac64) std.Random` |
| `fill` | `pub fn fill(self: *Isaac64, buf: []u8) void` |

## Random / Pcg

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Pcg` |
| `random` | `pub fn random(self: *Pcg) std.Random` |
| `fill` | `pub fn fill(self: *Pcg, buf: []u8) void` |

## Random / RomuTrio

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) RomuTrio` |
| `random` | `pub fn random(self: *RomuTrio) std.Random` |
| `seedWithBuf` | `pub fn seedWithBuf(self: *RomuTrio, buf: [24]u8) void` |
| `seed` | `pub fn seed(self: *RomuTrio, init_s: u64) void` |
| `fill` | `pub fn fill(self: *RomuTrio, buf: []u8) void` |

## Random / Sfc64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Sfc64` |
| `random` | `pub fn random(self: *Sfc64) std.Random` |
| `fill` | `pub fn fill(self: *Sfc64, buf: []u8) void` |

## Random / SplitMix64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(seed: u64) SplitMix64` |
| `next` | `pub fn next(self: *SplitMix64) u64` |

## Random / Xoroshiro128

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Xoroshiro128` |
| `random` | `pub fn random(self: *Xoroshiro128) std.Random` |
| `next` | `pub fn next(self: *Xoroshiro128) u64` |
| `jump` | `pub fn jump(self: *Xoroshiro128) void` |
| `seed` | `pub fn seed(self: *Xoroshiro128, init_s: u64) void` |
| `fill` | `pub fn fill(self: *Xoroshiro128, buf: []u8) void` |

## Random / Xoshiro256

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Xoshiro256` |
| `random` | `pub fn random(self: *Xoshiro256) std.Random` |
| `next` | `pub fn next(self: *Xoshiro256) u64` |
| `jump` | `pub fn jump(self: *Xoshiro256) void` |
| `seed` | `pub fn seed(self: *Xoshiro256, init_s: u64) void` |
| `fill` | `pub fn fill(self: *Xoshiro256, buf: []u8) void` |

## Random / benchmark

| Function | Signature |
|----------|-----------|
| `benchmark` | `pub fn benchmark(comptime H: anytype, bytes: usize, comptime block_size: usize) !Result` |
| `main` | `pub fn main(init: std.process.Init) !void` |

## Random / lcg

| Function | Signature |
|----------|-----------|
| `Wrapping` | `pub fn Wrapping(comptime T: type) type` |
| `init` | `pub fn init(xi: T, a: T, c: T) LcgSelf` |
| `next` | `pub fn next(lcg: *LcgSelf) T` |

## Random / ziggurat

| Function | Signature |
|----------|-----------|
| `next_f64` | `pub fn next_f64(random: Random, comptime tables: ZigTable) f64` |
| `ZigTableGen` | `pub fn ZigTableGen(comptime is_symmetric: bool, comptime r: f64, comptime v: f64, comptime f: fn (f64) f64, comptime f_inv: fn (f64) f64, comptime zero_case: fn (Random, f64) f64, ) ZigTable` |
| `norm_f` | `pub fn norm_f(x: f64) f64` |
| `norm_f_inv` | `pub fn norm_f_inv(y: f64) f64` |
| `norm_zero_case` | `pub fn norm_zero_case(random: Random, u: f64) f64` |
| `exp_f` | `pub fn exp_f(x: f64) f64` |
| `exp_f_inv` | `pub fn exp_f_inv(y: f64) f64` |
| `exp_zero_case` | `pub fn exp_zero_case(random: Random, _: f64) f64` |

## Build / Cache

| Function | Signature |
|----------|-----------|
| `addPrefix` | `pub fn addPrefix(cache: *Cache, directory: Directory) void` |
| `obtain` | `pub fn obtain(cache: *Cache) Manifest` |
| `prefixes` | `pub fn prefixes(cache: *const Cache) []const Directory` |
| `fromFs` | `pub fn fromFs(fs_stat: Io.File.Stat) Stat` |
| `deinit` | `pub fn deinit(self: *File, gpa: Allocator) void` |
| `updateMaxSize` | `pub fn updateMaxSize(file: *File, new_max_size: ?usize) void` |
| `updateHandle` | `pub fn updateHandle(file: *File, new_handle: ?Io.File) void` |
| `addBytes` | `pub fn addBytes(hh: *HashHelper, bytes: []const u8) void` |
| `addOptionalBytes` | `pub fn addOptionalBytes(hh: *HashHelper, optional_bytes: ?[]const u8) void` |
| `addListOfBytes` | `pub fn addListOfBytes(hh: *HashHelper, list_of_bytes: []const []const u8) void` |
| `addOptionalListOfBytes` | `pub fn addOptionalListOfBytes(hh: *HashHelper, optional_list_of_bytes: ?[]const []const u8) void` |
| `add` | `pub fn add(hh: *HashHelper, x: anytype) void` |
| `addOptional` | `pub fn addOptional(hh: *HashHelper, optional: anytype) void` |
| `peek` | `pub fn peek(hh: HashHelper) [hex_digest_len]u8` |
| `peekBin` | `pub fn peekBin(hh: HashHelper) BinDigest` |
| `final` | `pub fn final(hh: *HashHelper) HexDigest` |
| `oneShot` | `pub fn oneShot(bytes: []const u8) [hex_digest_len]u8` |
| `binToHex` | `pub fn binToHex(bin_digest: BinDigest) HexDigest` |
| `release` | `pub fn release(lock: *Lock, io: Io) void` |
| `hash` | `pub fn hash(fc: FilesContext, file: File) u32` |
| `eql` | `pub fn eql(fc: FilesContext, a: File, b: File, b_index: usize) bool` |
| `eql` | `pub fn eql(context: @This() , a: PrefixedPath, b: File, b_index: usize) bool` |
| `hash` | `pub fn hash(context: @This() , key: PrefixedPath) u32` |
| `addFilePath` | `pub fn addFilePath(m: *Manifest, file_path: Path, max_file_size: ?usize) !usize` |
| `addOpenedFile` | `pub fn addOpenedFile(m: *Manifest, path: Path, handle: ?Io.File, max_file_size: ?usize) !usize` |
| `addFile` | `pub fn addFile(self: *Manifest, file_path: []const u8, max_file_size: ?usize) !usize` |
| `addOptionalFile` | `pub fn addOptionalFile(self: *Manifest, optional_file_path: ?[]const u8) !void` |
| `addOptionalFilePath` | `pub fn addOptionalFilePath(self: *Manifest, optional_file_path: ?Path) !void` |
| `addListOfFiles` | `pub fn addListOfFiles(self: *Manifest, list_of_files: []const []const u8) !void` |
| `addDepFile` | `pub fn addDepFile(self: *Manifest, dir: Io.Dir, dep_file_sub_path: []const u8) !void` |
| `hit` | `pub fn hit(self: *Manifest) HitError!bool` |
| `unhit` | `pub fn unhit(self: *Manifest, bin_digest: BinDigest, input_file_count: usize) void` |
| `addFilePostFetch` | `pub fn addFilePostFetch(self: *Manifest, file_path: []const u8, max_file_size: usize) ![]const u8` |
| `addFilePost` | `pub fn addFilePost(self: *Manifest, file_path: []const u8) !void` |
| `addFilePostContents` | `pub fn addFilePostContents(self: *Manifest, file_path: []const u8, bytes: []const u8, stat: File.Stat,) !void` |
| `addDepFilePost` | `pub fn addDepFilePost(self: *Manifest, dir: Io.Dir, dep_file_sub_path: []const u8) !void` |
| `finalBin` | `pub fn finalBin(self: *Manifest) BinDigest` |
| `final` | `pub fn final(self: *Manifest) HexDigest` |
| `writeManifest` | `pub fn writeManifest(self: *Manifest) !void` |
| `toOwnedLock` | `pub fn toOwnedLock(self: *Manifest) Lock` |
| `deinit` | `pub fn deinit(self: *Manifest) void` |
| `populateFileSystemInputs` | `pub fn populateFileSystemInputs(man: *Manifest, buf: *std.ArrayList(u8) ) Allocator.Error!void` |
| `populateOtherManifest` | `pub fn populateOtherManifest(man: *Manifest, other: *Manifest, prefix_map: [4]u8) Allocator.Error!void` |

## Build / Fuzz

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(gpa: Allocator, io: Io, all_steps: []const *Build.Step, root_prog_node: std.Progress.Node, mode: Mode,) error` |
| `start` | `pub fn start(fuzz: *Fuzz) void` |
| `deinit` | `pub fn deinit(fuzz: *Fuzz) void` |
| `serveSourcesTar` | `pub fn serveSourcesTar(fuzz: *Fuzz, req: *std.http.Server.Request) !void` |
| `lessThan` | `pub fn lessThan(this: @This() , lhs: Build.Cache.Path, rhs: Build.Cache.Path) bool` |
| `sendUpdate` | `pub fn sendUpdate(fuzz: *Fuzz, socket: *std.http.Server.WebSocket, prev: *Previous,) !void` |
| `lessThan` | `pub fn lessThan(ctx: @This() , a_index: usize, b_index: usize) bool` |
| `waitAndPrintReport` | `pub fn waitAndPrintReport(fuzz: *Fuzz) Io.Cancelable!void` |

## Build / Module

| Function | Signature |
|----------|-----------|
| `internalIdentifier` | `pub fn internalIdentifier(self: CSourceLanguage) []const u8` |
| `dupe` | `pub fn dupe(file: CSourceFile, b: *std.Build) CSourceFile` |
| `dupe` | `pub fn dupe(file: RcSourceFile, b: *std.Build) RcSourceFile` |
| `appendZigProcessFlags` | `pub fn appendZigProcessFlags(include_dir: IncludeDir, b: *std.Build, zig_args: *std.array_list.Managed([]const u8) , asking_step: ?*Step, ) !void` |
| `init` | `pub fn init(m: *Module, owner: *std.Build, value: union(enum)` |
| `create` | `pub fn create(owner: *std.Build, options: CreateOptions) *Module` |
| `addImport` | `pub fn addImport(m: *Module, name: []const u8, module: *Module) void` |
| `addAnonymousImport` | `pub fn addAnonymousImport(m: *Module, name: []const u8, options: CreateOptions) void` |
| `addOptions` | `pub fn addOptions(m: *Module, module_name: []const u8, options: *Step.Options) void` |
| `linkSystemLibrary` | `pub fn linkSystemLibrary(m: *Module, name: []const u8, options: LinkSystemLibraryOptions,) void` |
| `linkFramework` | `pub fn linkFramework(m: *Module, name: []const u8, options: LinkFrameworkOptions) void` |
| `addCSourceFiles` | `pub fn addCSourceFiles(m: *Module, options: AddCSourceFilesOptions) void` |
| `addCSourceFile` | `pub fn addCSourceFile(m: *Module, source: CSourceFile) void` |
| `addWin32ResourceFile` | `pub fn addWin32ResourceFile(m: *Module, source: RcSourceFile) void` |
| `addAssemblyFile` | `pub fn addAssemblyFile(m: *Module, source: LazyPath) void` |
| `addObjectFile` | `pub fn addObjectFile(m: *Module, object: LazyPath) void` |
| `addObject` | `pub fn addObject(m: *Module, object: *Step.Compile) void` |
| `linkLibrary` | `pub fn linkLibrary(m: *Module, library: *Step.Compile) void` |
| `addAfterIncludePath` | `pub fn addAfterIncludePath(m: *Module, lazy_path: LazyPath) void` |
| `addSystemIncludePath` | `pub fn addSystemIncludePath(m: *Module, lazy_path: LazyPath) void` |
| `addIncludePath` | `pub fn addIncludePath(m: *Module, lazy_path: LazyPath) void` |
| `addConfigHeader` | `pub fn addConfigHeader(m: *Module, config_header: *Step.ConfigHeader) void` |
| `addSystemFrameworkPath` | `pub fn addSystemFrameworkPath(m: *Module, directory_path: LazyPath) void` |
| `addFrameworkPath` | `pub fn addFrameworkPath(m: *Module, directory_path: LazyPath) void` |
| `addEmbedPath` | `pub fn addEmbedPath(m: *Module, lazy_path: LazyPath) void` |
| `addLibraryPath` | `pub fn addLibraryPath(m: *Module, directory_path: LazyPath) void` |
| `addRPath` | `pub fn addRPath(m: *Module, directory_path: LazyPath) void` |
| `addRPathSpecial` | `pub fn addRPathSpecial(m: *Module, bytes: []const u8) void` |
| `addCMacro` | `pub fn addCMacro(m: *Module, name: []const u8, value: []const u8) void` |
| `appendZigProcessFlags` | `pub fn appendZigProcessFlags(m: *Module, zig_args: *std.array_list.Managed([]const u8) , asking_step: ?*Step, ) !void` |
| `getGraph` | `pub fn getGraph(root: *Module) Graph` |

## Build / Step

| Function | Signature |
|----------|-----------|
| `isSuccess` | `pub fn isSuccess(tr: TestResults) bool` |
| `passCount` | `pub fn passCount(tr: TestResults) u32` |
| `Type` | `pub fn Type(comptime id: Id) type` |
| `populated` | `pub fn populated(inputs: *Inputs) bool` |
| `clear` | `pub fn clear(inputs: *Inputs, gpa: Allocator) void` |
| `init` | `pub fn init(options: StepOptions) Step` |
| `make` | `pub fn make(s: *Step, options: MakeOptions) error` |
| `dependOn` | `pub fn dependOn(step: *Step, other: *Step) void` |
| `cast` | `pub fn cast(step: *Step, comptime T: type) ?*T` |
| `dump` | `pub fn dump(step: *Step, t: Io.Terminal) void` |
| `captureChildProcess` | `pub fn captureChildProcess(s: *Step, gpa: Allocator, progress_node: std.Progress.Node, argv: []const []const u8,) !std.process.RunResult` |
| `fail` | `pub fn fail(step: *Step, comptime fmt: []const u8, args: anytype) error` |
| `addError` | `pub fn addError(step: *Step, comptime fmt: []const u8, args: anytype) error` |
| `saveState` | `pub fn saveState(zp: *ZigProcess, prog_node: std.Progress.Node) void` |
| `deinit` | `pub fn deinit(zp: *ZigProcess, io: Io) void` |
| `evalZigProcess` | `pub fn evalZigProcess(s: *Step, argv: []const []const u8, prog_node: std.Progress.Node, watch: bool, web_server: ?*Build.WebServer, gpa: Allocator,) !?Path` |
| `installFile` | `pub fn installFile(s: *Step, src_lazy_path: Build.LazyPath, dest_path: []const u8) !Io.Dir.PrevStatus` |
| `installDir` | `pub fn installDir(s: *Step, dest_path: []const u8) !Io.Dir.CreatePathStatus` |
| `getZigProcess` | `pub fn getZigProcess(s: *Step) ?*ZigProcess` |
| `handleVerbose` | `pub fn handleVerbose(b: *Build, cwd: std.process.Child.Cwd, argv: []const []const u8,) error` |
| `handleVerbose2` | `pub fn handleVerbose2(b: *Build, cwd: std.process.Child.Cwd, opt_env: ?*const std.process.Environ.Map, argv: []const []const u8,) error` |
| `handleChildProcUnsupported` | `pub fn handleChildProcUnsupported(s: *Step) error` |
| `handleChildProcessTerm` | `pub fn handleChildProcessTerm(s: *Step, term: std.process.Child.Term) error` |
| `allocPrintCmd` | `pub fn allocPrintCmd(gpa: Allocator, cwd: std.process.Child.Cwd, opt_env: ?struct { child: *const std.process.Environ.Map, parent: *const std.process.Environ.Map, }, argv: []const []const u8,) Allocator.Error![]u8` |
| `cacheHit` | `pub fn cacheHit(s: *Step, man: *Build.Cache.Manifest) !bool` |
| `cacheHitAndWatch` | `pub fn cacheHitAndWatch(s: *Step, man: *Build.Cache.Manifest) !bool` |
| `writeManifest` | `pub fn writeManifest(s: *Step, man: *Build.Cache.Manifest) !void` |
| `writeManifestAndWatch` | `pub fn writeManifestAndWatch(s: *Step, man: *Build.Cache.Manifest) !void` |
| `singleUnchangingWatchInput` | `pub fn singleUnchangingWatchInput(step: *Step, lazy_path: Build.LazyPath) Allocator.Error!void` |
| `clearWatchInputs` | `pub fn clearWatchInputs(step: *Step) void` |
| `addWatchInput` | `pub fn addWatchInput(step: *Step, lazy_file: Build.LazyPath) Allocator.Error!void` |
| `addDirectoryWatchInput` | `pub fn addDirectoryWatchInput(step: *Step, lazy_directory: Build.LazyPath) Allocator.Error!bool` |
| `addDirectoryWatchInputFromPath` | `pub fn addDirectoryWatchInputFromPath(step: *Step, path: Build.Cache.Path) !void` |
| `reset` | `pub fn reset(step: *Step, gpa: Allocator) void` |
| `invalidateResult` | `pub fn invalidateResult(step: *Step, gpa: Allocator) bool` |

## Build / Watch

| Function | Signature |
|----------|-----------|
| `hash` | `pub fn hash(self: Adapter, a: FileHandle) u32` |
| `eql` | `pub fn eql(self: Adapter, a: FileHandle, b: FileHandle, b_index: usize) bool` |
| `hash` | `pub fn hash(_: TableAdapter, lhs_dir: *Directory) u32` |
| `eql` | `pub fn eql(_: TableAdapter, lhs_dir: *Directory, rhs_dir: *Directory, rhs_index: usize) bool` |
| `init` | `pub fn init(cwd_path: []const u8) !Watch` |
| `hash` | `pub fn hash(self: Context, a: Match) u32` |
| `eql` | `pub fn eql(self: Context, a: Match, b: Match, b_index: usize) bool` |
| `update` | `pub fn update(w: *Watch, gpa: Allocator, steps: []const *Step) !void` |
| `to_i32_ms` | `pub fn to_i32_ms(t: Timeout) i32` |
| `toTimespec` | `pub fn toTimespec(t: Timeout, buf: *std.posix.timespec) ?*std.posix.timespec` |
| `wait` | `pub fn wait(w: *Watch, gpa: Allocator, io: Io, timeout: Timeout) !WaitResult` |

## Build / WebServer

| Function | Signature |
|----------|-----------|
| `notifyUpdate` | `pub fn notifyUpdate(ws: *WebServer) void` |
| `init` | `pub fn init(opts: Options) WebServer` |
| `deinit` | `pub fn deinit(ws: *WebServer) void` |
| `start` | `pub fn start(ws: *WebServer) error` |
| `startBuild` | `pub fn startBuild(ws: *WebServer) void` |
| `updateStepStatus` | `pub fn updateStepStatus(ws: *WebServer, step: *Build.Step, new_status: abi.StepUpdate.Status) void` |
| `finishBuild` | `pub fn finishBuild(ws: *WebServer, opts: struct { fuzz: bool, }) void` |
| `now` | `pub fn now(s: *const WebServer) i64` |
| `serveFile` | `pub fn serveFile(ws: *WebServer, request: *http.Server.Request, path: Cache.Path, content_type: []const u8,) !void` |
| `serveTarFile` | `pub fn serveTarFile(ws: *WebServer, request: *http.Server.Request, paths: []const Cache.Path) !void` |
| `updateTimeReportCompile` | `pub fn updateTimeReportCompile(ws: *WebServer, opts: struct { compile: *Build.Step.Compile, use_llvm: bool, stats: abi.time_report.CompileResult.Stats, ns_total: u64, llvm_pass_timings_len: u32, files_len: u32, decls_len: u32, /// The trailing dat...` |
| `updateTimeReportGeneric` | `pub fn updateTimeReportGeneric(ws: *WebServer, step: *Build.Step, duration: Io.Duration) void` |
| `updateTimeReportRunTest` | `pub fn updateTimeReportRunTest(ws: *WebServer, run: *Build.Step.Run, tests: *const Build.Step.Run.CachedTestMetadata, ns_per_test: []const u64,) void` |
| `getRunnerRequest` | `pub fn getRunnerRequest(ws: *WebServer) ?RunnerRequest` |
| `wait` | `pub fn wait(ws: *WebServer) Io.Cancelable!RunnerRequest` |

## Build / abi

| Function | Signature |
|----------|-----------|
| `toSlice` | `pub fn toSlice(s: Slice) []const u8` |
| `fromSlice` | `pub fn fromSlice(s: []const u8) Slice` |
| `headerEnd` | `pub fn headerEnd(header: *const SeenPcsHeader) []const usize` |
| `seenBits` | `pub fn seenBits(header: *const SeenPcsHeader) []const usize` |
| `seenElemsLen` | `pub fn seenElemsLen(pcs_len: usize) usize` |
| `pcAddrs` | `pub fn pcAddrs(header: *const SeenPcsHeader) []const usize` |
| `locsLen` | `pub fn locsLen(hdr: EntryPointHeader) u24` |
| `init` | `pub fn init(locs_len: u24) EntryPointHeader` |

## Build / Step / CheckFile

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, source: std.Build.LazyPath, options: Options,) *CheckFile` |
| `setName` | `pub fn setName(check_file: *CheckFile, name: []const u8) void` |

## Build / Step / CheckObject

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, source: std.Build.LazyPath, obj_format: std.Target.ObjectFormat,) *CheckObject` |
| `format` | `pub fn format(value: ComputeCompareExpected, w: *Writer) Writer.Error!void` |
| `checkExact` | `pub fn checkExact(check_object: *CheckObject, phrase: []const u8) void` |
| `checkExactPath` | `pub fn checkExactPath(check_object: *CheckObject, phrase: []const u8, lazy_path: std.Build.LazyPath) void` |
| `checkContains` | `pub fn checkContains(check_object: *CheckObject, phrase: []const u8) void` |
| `checkContainsPath` | `pub fn checkContainsPath(check_object: *CheckObject, phrase: []const u8, lazy_path: std.Build.LazyPath,) void` |
| `checkExtract` | `pub fn checkExtract(check_object: *CheckObject, phrase: []const u8) void` |
| `checkExtractLazyPath` | `pub fn checkExtractLazyPath(check_object: *CheckObject, phrase: []const u8, lazy_path: std.Build.LazyPath) void` |
| `checkNotPresent` | `pub fn checkNotPresent(check_object: *CheckObject, phrase: []const u8) void` |
| `checkNotPresentLazyPath` | `pub fn checkNotPresentLazyPath(check_object: *CheckObject, phrase: []const u8, lazy_path: std.Build.LazyPath) void` |
| `checkInHeaders` | `pub fn checkInHeaders(check_object: *CheckObject) void` |
| `checkInSymtab` | `pub fn checkInSymtab(check_object: *CheckObject) void` |
| `checkInDyldRebase` | `pub fn checkInDyldRebase(check_object: *CheckObject) void` |
| `checkInDyldBind` | `pub fn checkInDyldBind(check_object: *CheckObject) void` |
| `checkInDyldWeakBind` | `pub fn checkInDyldWeakBind(check_object: *CheckObject) void` |
| `checkInDyldLazyBind` | `pub fn checkInDyldLazyBind(check_object: *CheckObject) void` |
| `checkInExports` | `pub fn checkInExports(check_object: *CheckObject) void` |
| `checkInIndirectSymtab` | `pub fn checkInIndirectSymtab(check_object: *CheckObject) void` |
| `checkInDynamicSymtab` | `pub fn checkInDynamicSymtab(check_object: *CheckObject) void` |
| `checkInDynamicSection` | `pub fn checkInDynamicSection(check_object: *CheckObject) void` |
| `checkInArchiveSymtab` | `pub fn checkInArchiveSymtab(check_object: *CheckObject) void` |
| `dumpSection` | `pub fn dumpSection(check_object: *CheckObject, name: [:0]const u8) void` |
| `checkComputeCompare` | `pub fn checkComputeCompare(check_object: *CheckObject, program: []const u8, expected: ComputeCompareExpected,) void` |

## Build / Step / Compile

| Function | Signature |
|----------|-----------|
| `isTest` | `pub fn isTest(kind: Kind) bool` |
| `dupe` | `pub fn dupe(file: File, b: *std.Build) File` |
| `dupe` | `pub fn dupe(opts: Directory.Options, b: *std.Build) Directory.Options` |
| `dupe` | `pub fn dupe(dir: Directory, b: *std.Build) Directory` |
| `getSource` | `pub fn getSource(installation: HeaderInstallation) LazyPath` |
| `dupe` | `pub fn dupe(installation: HeaderInstallation, b: *std.Build) HeaderInstallation` |
| `create` | `pub fn create(owner: *std.Build, options: Options) *Compile` |
| `installHeader` | `pub fn installHeader(cs: *Compile, source: LazyPath, dest_rel_path: []const u8) void` |
| `installHeadersDirectory` | `pub fn installHeadersDirectory(cs: *Compile, source: LazyPath, dest_rel_path: []const u8, options: HeaderInstallation.Directory.Options,) void` |
| `installConfigHeader` | `pub fn installConfigHeader(cs: *Compile, config_header: *Step.ConfigHeader) void` |
| `installLibraryHeaders` | `pub fn installLibraryHeaders(cs: *Compile, lib: *Compile) void` |
| `getEmittedIncludeTree` | `pub fn getEmittedIncludeTree(cs: *Compile) LazyPath` |
| `addObjCopy` | `pub fn addObjCopy(cs: *Compile, options: Step.ObjCopy.Options) *Step.ObjCopy` |
| `checkObject` | `pub fn checkObject(compile: *Compile) *Step.CheckObject` |
| `setLinkerScript` | `pub fn setLinkerScript(compile: *Compile, source: LazyPath) void` |
| `setVersionScript` | `pub fn setVersionScript(compile: *Compile, source: LazyPath) void` |
| `forceUndefinedSymbol` | `pub fn forceUndefinedSymbol(compile: *Compile, symbol_name: []const u8) void` |
| `dependsOnSystemLibrary` | `pub fn dependsOnSystemLibrary(compile: *Compile, name: []const u8) bool` |
| `isDynamicLibrary` | `pub fn isDynamicLibrary(compile: *const Compile) bool` |
| `isStaticLibrary` | `pub fn isStaticLibrary(compile: *const Compile) bool` |
| `isDll` | `pub fn isDll(compile: *Compile) bool` |
| `producesPdbFile` | `pub fn producesPdbFile(compile: *Compile) bool` |
| `producesImplib` | `pub fn producesImplib(compile: *Compile) bool` |
| `setVerboseLink` | `pub fn setVerboseLink(compile: *Compile, value: bool) void` |
| `setVerboseCC` | `pub fn setVerboseCC(compile: *Compile, value: bool) void` |
| `setLibCFile` | `pub fn setLibCFile(compile: *Compile, libc_file: ?LazyPath) void` |
| `getEmittedBinDirectory` | `pub fn getEmittedBinDirectory(compile: *Compile) LazyPath` |
| `getEmittedBin` | `pub fn getEmittedBin(compile: *Compile) LazyPath` |
| `getEmittedImplib` | `pub fn getEmittedImplib(compile: *Compile) LazyPath` |
| `getEmittedH` | `pub fn getEmittedH(compile: *Compile) LazyPath` |
| `getEmittedPdb` | `pub fn getEmittedPdb(compile: *Compile) LazyPath` |
| `getEmittedDocs` | `pub fn getEmittedDocs(compile: *Compile) LazyPath` |
| `getEmittedAsm` | `pub fn getEmittedAsm(compile: *Compile) LazyPath` |
| `getEmittedLlvmIr` | `pub fn getEmittedLlvmIr(compile: *Compile) LazyPath` |
| `getEmittedLlvmBc` | `pub fn getEmittedLlvmBc(compile: *Compile) LazyPath` |
| `setExecCmd` | `pub fn setExecCmd(compile: *Compile, args: []const ?[]const u8) void` |
| `rebuildInFuzzMode` | `pub fn rebuildInFuzzMode(c: *Compile, gpa: Allocator, progress_node: std.Progress.Node) !Path` |
| `doAtomicSymLinks` | `pub fn doAtomicSymLinks(step: *Step, output_path: []const u8, filename_major_only: []const u8, filename_name_only: []const u8,) !void` |
| `rootModuleTarget` | `pub fn rootModuleTarget(c: *Compile) std.Target` |
| `getCompileDependencies` | `pub fn getCompileDependencies(start: *Compile, chase_dynamic: bool) []const *Compile` |

## Build / Step / ConfigHeader

| Function | Signature |
|----------|-----------|
| `getPath` | `pub fn getPath(style: Style) ?std.Build.LazyPath` |
| `create` | `pub fn create(owner: *std.Build, options: Options) *ConfigHeader` |
| `addValue` | `pub fn addValue(config_header: *ConfigHeader, name: []const u8, comptime T: type, value: T) void` |
| `addValues` | `pub fn addValues(config_header: *ConfigHeader, values: anytype) void` |
| `getOutputDir` | `pub fn getOutputDir(ch: *ConfigHeader) std.Build.LazyPath` |
| `getOutputFile` | `pub fn getOutputFile(ch: *ConfigHeader) std.Build.LazyPath` |

## Build / Step / Fail

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, error_msg: []const u8) *Fail` |

## Build / Step / Fmt

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, options: Options) *Fmt` |

## Build / Step / InstallArtifact

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, artifact: *Step.Compile, options: Options) *InstallArtifact` |

## Build / Step / InstallDir

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, options: Options) *InstallDir` |

## Build / Step / InstallFile

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, source: LazyPath, dir: InstallDir, dest_rel_path: []const u8,) *InstallFile` |

## Build / Step / ObjCopy

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, input_file: std.Build.LazyPath, options: Options,) *ObjCopy` |
| `getOutput` | `pub fn getOutput(objcopy: *const ObjCopy) std.Build.LazyPath` |
| `getOutputSeparatedDebug` | `pub fn getOutputSeparatedDebug(objcopy: *const ObjCopy) ?std.Build.LazyPath` |

## Build / Step / Options

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build) *Options` |
| `addOption` | `pub fn addOption(options: *Options, comptime T: type, name: []const u8, value: T) void` |
| `addOptionPath` | `pub fn addOptionPath(options: *Options, name: []const u8, path: LazyPath,) void` |
| `createModule` | `pub fn createModule(options: *Options) *std.Build.Module` |
| `getOutput` | `pub fn getOutput(options: *Options) LazyPath` |

## Build / Step / Run

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, name: []const u8) *Run` |
| `setName` | `pub fn setName(run: *Run, name: []const u8) void` |
| `enableTestRunnerMode` | `pub fn enableTestRunnerMode(run: *Run) void` |
| `addArtifactArg` | `pub fn addArtifactArg(run: *Run, artifact: *Step.Compile) void` |
| `addPrefixedArtifactArg` | `pub fn addPrefixedArtifactArg(run: *Run, prefix: []const u8, artifact: *Step.Compile) void` |
| `addOutputFileArg` | `pub fn addOutputFileArg(run: *Run, basename: []const u8) std.Build.LazyPath` |
| `addPrefixedOutputFileArg` | `pub fn addPrefixedOutputFileArg(run: *Run, prefix: []const u8, basename: []const u8,) std.Build.LazyPath` |
| `addFileArg` | `pub fn addFileArg(run: *Run, lp: std.Build.LazyPath) void` |
| `addPrefixedFileArg` | `pub fn addPrefixedFileArg(run: *Run, prefix: []const u8, lp: std.Build.LazyPath) void` |
| `addFileContentArg` | `pub fn addFileContentArg(run: *Run, lp: std.Build.LazyPath) void` |
| `addPrefixedFileContentArg` | `pub fn addPrefixedFileContentArg(run: *Run, prefix: []const u8, lp: std.Build.LazyPath) void` |
| `addOutputDirectoryArg` | `pub fn addOutputDirectoryArg(run: *Run, basename: []const u8) std.Build.LazyPath` |
| `addPrefixedOutputDirectoryArg` | `pub fn addPrefixedOutputDirectoryArg(run: *Run, prefix: []const u8, basename: []const u8,) std.Build.LazyPath` |
| `addDirectoryArg` | `pub fn addDirectoryArg(run: *Run, lazy_directory: std.Build.LazyPath) void` |
| `addPrefixedDirectoryArg` | `pub fn addPrefixedDirectoryArg(run: *Run, prefix: []const u8, lazy_directory: std.Build.LazyPath) void` |
| `addDecoratedDirectoryArg` | `pub fn addDecoratedDirectoryArg(run: *Run, prefix: []const u8, lazy_directory: std.Build.LazyPath, suffix: []const u8,) void` |
| `addDepFileOutputArg` | `pub fn addDepFileOutputArg(run: *Run, basename: []const u8) std.Build.LazyPath` |
| `addPrefixedDepFileOutputArg` | `pub fn addPrefixedDepFileOutputArg(run: *Run, prefix: []const u8, basename: []const u8) std.Build.LazyPath` |
| `addArg` | `pub fn addArg(run: *Run, arg: []const u8) void` |
| `addArgs` | `pub fn addArgs(run: *Run, args: []const []const u8) void` |
| `setStdIn` | `pub fn setStdIn(run: *Run, stdin: StdIn) void` |
| `setCwd` | `pub fn setCwd(run: *Run, cwd: Build.LazyPath) void` |
| `clearEnvironment` | `pub fn clearEnvironment(run: *Run) void` |
| `addPathDir` | `pub fn addPathDir(run: *Run, search_path: []const u8) void` |
| `getEnvMap` | `pub fn getEnvMap(run: *Run) *EnvMap` |
| `setEnvironmentVariable` | `pub fn setEnvironmentVariable(run: *Run, key: []const u8, value: []const u8) void` |
| `removeEnvironmentVariable` | `pub fn removeEnvironmentVariable(run: *Run, key: []const u8) void` |
| `expectStdErrEqual` | `pub fn expectStdErrEqual(run: *Run, bytes: []const u8) void` |
| `expectStdErrMatch` | `pub fn expectStdErrMatch(run: *Run, bytes: []const u8) void` |
| `expectStdOutEqual` | `pub fn expectStdOutEqual(run: *Run, bytes: []const u8) void` |
| `expectStdOutMatch` | `pub fn expectStdOutMatch(run: *Run, bytes: []const u8) void` |
| `expectExitCode` | `pub fn expectExitCode(run: *Run, code: u8) void` |
| `hasTermCheck` | `pub fn hasTermCheck(run: Run) bool` |
| `addCheck` | `pub fn addCheck(run: *Run, new_check: StdIo.Check) void` |
| `captureStdErr` | `pub fn captureStdErr(run: *Run, options: CapturedStdIo.Options) std.Build.LazyPath` |
| `captureStdOut` | `pub fn captureStdOut(run: *Run, options: CapturedStdIo.Options) std.Build.LazyPath` |
| `addFileInput` | `pub fn addFileInput(self: *Run, file_input: std.Build.LazyPath) void` |
| `rerunInFuzzMode` | `pub fn rerunInFuzzMode(run: *Run, fuzz: *std.Build.Fuzz, unit_test_index: u32, prog_node: std.Progress.Node,) !void` |
| `testName` | `pub fn testName(tm: CachedTestMetadata, index: u32) []const u8` |

## Build / Step / TranslateC

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build, options: Options) *TranslateC` |
| `getOutput` | `pub fn getOutput(translate_c: *TranslateC) std.Build.LazyPath` |
| `addModule` | `pub fn addModule(translate_c: *TranslateC, name: []const u8) *std.Build.Module` |
| `createModule` | `pub fn createModule(translate_c: *TranslateC) *std.Build.Module` |
| `addAfterIncludePath` | `pub fn addAfterIncludePath(translate_c: *TranslateC, lazy_path: LazyPath) void` |
| `addSystemIncludePath` | `pub fn addSystemIncludePath(translate_c: *TranslateC, lazy_path: LazyPath) void` |
| `addIncludePath` | `pub fn addIncludePath(translate_c: *TranslateC, lazy_path: LazyPath) void` |
| `addConfigHeader` | `pub fn addConfigHeader(translate_c: *TranslateC, config_header: *Step.ConfigHeader) void` |
| `addSystemFrameworkPath` | `pub fn addSystemFrameworkPath(translate_c: *TranslateC, directory_path: LazyPath) void` |
| `addFrameworkPath` | `pub fn addFrameworkPath(translate_c: *TranslateC, directory_path: LazyPath) void` |
| `addCheckFile` | `pub fn addCheckFile(translate_c: *TranslateC, expected_matches: []const []const u8) *Step.CheckFile` |
| `defineCMacro` | `pub fn defineCMacro(translate_c: *TranslateC, name: []const u8, value: ?[]const u8) void` |
| `defineCMacroRaw` | `pub fn defineCMacroRaw(translate_c: *TranslateC, name_and_value: []const u8) void` |

## Build / Step / UpdateSourceFiles

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(owner: *std.Build) *UpdateSourceFiles` |
| `addCopyFileToSource` | `pub fn addCopyFileToSource(usf: *UpdateSourceFiles, source: std.Build.LazyPath, sub_path: []const u8) void` |
| `addBytesToSource` | `pub fn addBytesToSource(usf: *UpdateSourceFiles, bytes: []const u8, sub_path: []const u8) void` |

## Build / Step / WriteFile

| Function | Signature |
|----------|-----------|
| `dupe` | `pub fn dupe(opts: Options, b: *std.Build) Options` |
| `pathIncluded` | `pub fn pathIncluded(opts: Options, path: []const u8) bool` |
| `create` | `pub fn create(owner: *std.Build) *WriteFile` |
| `add` | `pub fn add(write_file: *WriteFile, sub_path: []const u8, bytes: []const u8) std.Build.LazyPath` |
| `addCopyFile` | `pub fn addCopyFile(write_file: *WriteFile, source: std.Build.LazyPath, sub_path: []const u8) std.Build.LazyPath` |
| `addCopyDirectory` | `pub fn addCopyDirectory(write_file: *WriteFile, source: std.Build.LazyPath, sub_path: []const u8, options: Directory.Options,) std.Build.LazyPath` |
| `getDirectory` | `pub fn getDirectory(write_file: *WriteFile) std.Build.LazyPath` |

## Build / Cache / DepTokenizer

| Function | Signature |
|----------|-----------|
| `next` | `pub fn next(self: *Tokenizer) ?Token` |
| `resolve` | `pub fn resolve(self: Token, gpa: Allocator, list: *std.ArrayList(u8) ) error` |
| `printError` | `pub fn printError(self: Token, gpa: Allocator, list: *std.ArrayList(u8) ) error` |

## Build / Cache / Directory

| Function | Signature |
|----------|-----------|
| `clone` | `pub fn clone(d: Directory, arena: Allocator) Allocator.Error!Directory` |
| `cwd` | `pub fn cwd() Directory` |
| `join` | `pub fn join(self: Directory, allocator: Allocator, paths: []const []const u8) ![]u8` |
| `joinZ` | `pub fn joinZ(self: Directory, allocator: Allocator, paths: []const []const u8) ![:0]u8` |
| `closeAndFree` | `pub fn closeAndFree(self: *Directory, gpa: Allocator, io: Io) void` |
| `format` | `pub fn format(self: Directory, writer: *std.Io.Writer) std.Io.Writer.Error!void` |
| `eql` | `pub fn eql(self: Directory, other: Directory) bool` |

## Build / Cache / Path

| Function | Signature |
|----------|-----------|
| `clone` | `pub fn clone(p: Path, arena: Allocator) Allocator.Error!Path` |
| `cwd` | `pub fn cwd() Path` |
| `initCwd` | `pub fn initCwd(sub_path: []const u8) Path` |
| `join` | `pub fn join(p: Path, arena: Allocator, sub_path: []const u8) Allocator.Error!Path` |
| `resolvePosix` | `pub fn resolvePosix(p: Path, arena: Allocator, sub_path: []const u8) Allocator.Error!Path` |
| `joinString` | `pub fn joinString(p: Path, gpa: Allocator, sub_path: []const u8) Allocator.Error![]u8` |
| `joinStringZ` | `pub fn joinStringZ(p: Path, gpa: Allocator, sub_path: []const u8) Allocator.Error![:0]u8` |
| `openFile` | `pub fn openFile(p: Path, io: Io, sub_path: []const u8, flags: Io.File.OpenFlags) !Io.File` |
| `openDir` | `pub fn openDir(p: Path, io: Io, sub_path: []const u8, args: Io.Dir.OpenOptions,) Io.Dir.OpenError!Io.Dir` |
| `createDirPathOpen` | `pub fn createDirPathOpen(p: Path, io: Io, sub_path: []const u8, opts: Io.Dir.OpenOptions) !Io.Dir` |
| `statFile` | `pub fn statFile(p: Path, io: Io, sub_path: []const u8) !Io.Dir.Stat` |
| `atomicFile` | `pub fn atomicFile(p: Path, io: Io, sub_path: []const u8, options: Io.Dir.AtomicFileOptions, buf: *[fs.max_path_bytes]u8,) !fs.AtomicFile` |
| `access` | `pub fn access(p: Path, io: Io, sub_path: []const u8, flags: Io.Dir.AccessOptions) !void` |
| `createDirPath` | `pub fn createDirPath(p: Path, io: Io, sub_path: []const u8) !void` |
| `toString` | `pub fn toString(p: Path, allocator: Allocator) Allocator.Error![]u8` |
| `toStringZ` | `pub fn toStringZ(p: Path, allocator: Allocator) Allocator.Error![:0]u8` |
| `fmtEscapeString` | `pub fn fmtEscapeString(path: Path) std.fmt.Alt(Path, formatEscapeString)` |
| `formatEscapeString` | `pub fn formatEscapeString(path: Path, writer: *Io.Writer) Io.Writer.Error!void` |
| `fmtEscapeChar` | `pub fn fmtEscapeChar(path: Path) std.fmt.Alt(Path, formatEscapeChar)` |
| `formatEscapeChar` | `pub fn formatEscapeChar(path: Path, writer: *Io.Writer) Io.Writer.Error!void` |
| `format` | `pub fn format(self: Path, writer: *Io.Writer) Io.Writer.Error!void` |
| `eql` | `pub fn eql(self: Path, other: Path) bool` |
| `subPathOpt` | `pub fn subPathOpt(self: Path) ?[]const u8` |
| `subPathOrDot` | `pub fn subPathOrDot(self: Path) []const u8` |
| `stem` | `pub fn stem(p: Path) []const u8` |
| `basename` | `pub fn basename(p: Path) []const u8` |
| `hash` | `pub fn hash(self: TableAdapter, a: Cache.Path) u32` |
| `eql` | `pub fn eql(self: TableAdapter, a: Cache.Path, b: Cache.Path, b_index: usize) bool` |

## Build / Watch / FsEvents

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(cwd_path: []const u8) error` |
| `deinit` | `pub fn deinit(fse: *FsEvents, gpa: Allocator, io: Io) void` |
| `setPaths` | `pub fn setPaths(fse: *FsEvents, gpa: Allocator, steps: []const *std.Build.Step) !void` |
| `wait` | `pub fn wait(fse: *FsEvents, gpa: Allocator, timeout_ns: ?u64) error` |

## zon / Serializer

| Function | Signature |
|----------|-----------|
| `value` | `pub fn value(self: *Serializer, val: anytype, options: ValueOptions) Error!void` |
| `valueMaxDepth` | `pub fn valueMaxDepth(self: *Serializer, val: anytype, options: ValueOptions, depth: usize) DepthError!void` |
| `valueArbitraryDepth` | `pub fn valueArbitraryDepth(self: *Serializer, val: anytype, options: ValueOptions) Error!void` |
| `int` | `pub fn int(self: *Serializer, val: anytype) Error!void` |
| `float` | `pub fn float(self: *Serializer, val: anytype) Error!void` |
| `ident` | `pub fn ident(self: *Serializer, name: []const u8) Error!void` |
| `codePoint` | `pub fn codePoint(self: *Serializer, val: u21) CodePointError!void` |
| `tuple` | `pub fn tuple(self: *Serializer, val: anytype, options: ValueOptions) Error!void` |
| `tupleMaxDepth` | `pub fn tupleMaxDepth(self: *Serializer, val: anytype, options: ValueOptions, depth: usize,) DepthError!void` |
| `tupleArbitraryDepth` | `pub fn tupleArbitraryDepth(self: *Serializer, val: anytype, options: ValueOptions,) Error!void` |
| `string` | `pub fn string(self: *Serializer, val: []const u8) Error!void` |
| `multilineString` | `pub fn multilineString(self: *Serializer, val: []const u8, options: MultilineStringOptions,) MultilineStringError!void` |
| `beginStruct` | `pub fn beginStruct(self: *Serializer, options: ContainerOptions) Error!Struct` |
| `beginTuple` | `pub fn beginTuple(self: *Serializer, options: ContainerOptions) Error!Tuple` |
| `end` | `pub fn end(self: *Tuple) Error!void` |
| `field` | `pub fn field(self: *Tuple, val: anytype, options: ValueOptions,) Error!void` |
| `fieldMaxDepth` | `pub fn fieldMaxDepth(self: *Tuple, val: anytype, options: ValueOptions, depth: usize,) DepthError!void` |
| `fieldArbitraryDepth` | `pub fn fieldArbitraryDepth(self: *Tuple, val: anytype, options: ValueOptions,) Error!void` |
| `beginStructField` | `pub fn beginStructField(self: *Tuple, options: ContainerOptions,) Error!Struct` |
| `beginTupleField` | `pub fn beginTupleField(self: *Tuple, options: ContainerOptions,) Error!Tuple` |
| `fieldPrefix` | `pub fn fieldPrefix(self: *Tuple) Error!void` |
| `end` | `pub fn end(self: *Struct) Error!void` |
| `field` | `pub fn field(self: *Struct, name: []const u8, val: anytype, options: ValueOptions,) Error!void` |
| `fieldMaxDepth` | `pub fn fieldMaxDepth(self: *Struct, name: []const u8, val: anytype, options: ValueOptions, depth: usize,) DepthError!void` |
| `fieldArbitraryDepth` | `pub fn fieldArbitraryDepth(self: *Struct, name: []const u8, val: anytype, options: ValueOptions,) Error!void` |
| `beginStructField` | `pub fn beginStructField(self: *Struct, name: []const u8, options: ContainerOptions,) Error!Struct` |
| `beginTupleField` | `pub fn beginTupleField(self: *Struct, name: []const u8, options: ContainerOptions,) Error!Tuple` |
| `fieldPrefix` | `pub fn fieldPrefix(self: *Struct, name: []const u8) Error!void` |

## zon / parse

| Function | Signature |
|----------|-----------|
| `next` | `pub fn next(self: *@This() ) ?Note` |
| `fmtMessage` | `pub fn fmtMessage(self: Note, diag: *const Diagnostics) std.fmt.Alt([]const u8, Note.formatMessage)` |
| `getLocation` | `pub fn getLocation(self: Note, diag: *const Diagnostics) Ast.Location` |
| `next` | `pub fn next(self: *@This() ) ?Error` |
| `fmtMessage` | `pub fn fmtMessage(self: @This() , diag: *const Diagnostics) std.fmt.Alt(FormatMessage, formatMessage)` |
| `getLocation` | `pub fn getLocation(self: @This() , diag: *const Diagnostics) Ast.Location` |
| `iterateNotes` | `pub fn iterateNotes(self: @This() , diag: *const Diagnostics) Note.Iterator` |
| `deinit` | `pub fn deinit(self: *Diagnostics, gpa: Allocator) void` |
| `iterateErrors` | `pub fn iterateErrors(self: *const Diagnostics) Error.Iterator` |
| `format` | `pub fn format(self: *const @This() , w: *std.Io.Writer) std.Io.Writer.Error!void` |
| `fromSlice` | `pub fn fromSlice(T: type, gpa: Allocator, source: [:0]const u8, diag: ?*Diagnostics, options: Options,) error` |
| `fromSliceAlloc` | `pub fn fromSliceAlloc(/// The type to deserialize into. May not be or contain any of the following types: /// * Any comptime-only type, except in a comptime field /// * `type` /// * `void`, except as a union payload /// * `noreturn` /// * An error...` |
| `fromZoir` | `pub fn fromZoir(T: type, ast: Ast, zoir: Zoir, diag: ?*Diagnostics, options: Options,) error` |
| `fromZoirAlloc` | `pub fn fromZoirAlloc(T: type, gpa: Allocator, ast: Ast, zoir: Zoir, diag: ?*Diagnostics, options: Options,) error` |
| `fromZoirNode` | `pub fn fromZoirNode(T: type, ast: Ast, zoir: Zoir, node: Zoir.Node.Index, diag: ?*Diagnostics, options: Options,) error` |
| `fromZoirNodeAlloc` | `pub fn fromZoirNodeAlloc(T: type, gpa: Allocator, ast: Ast, zoir: Zoir, node: Zoir.Node.Index, diag: ?*Diagnostics, options: Options,) error` |
| `free` | `pub fn free(gpa: Allocator, value: anytype) void` |

## zon / stringify

| Function | Signature |
|----------|-----------|
| `serialize` | `pub fn serialize(val: anytype, options: SerializeOptions, writer: *Writer) Writer.Error!void` |
| `serializeMaxDepth` | `pub fn serializeMaxDepth(val: anytype, options: SerializeOptions, writer: *Writer, depth: usize,) Serializer.DepthError!void` |
| `serializeArbitraryDepth` | `pub fn serializeArbitraryDepth(val: anytype, options: SerializeOptions, writer: *Writer,) Serializer.Error!void` |

