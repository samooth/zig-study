# Zig 0.10.1 — Function Signatures

Source: `<zig-install-dir>/lib/std`  (generated against `0.10.1`)

## array_hash_map

| Function | Signature |
|----------|-----------|
| `AutoArrayHashMap` | `pub fn AutoArrayHashMap(comptime K: type, comptime V: type) type` |
| `AutoArrayHashMapUnmanaged` | `pub fn AutoArrayHashMapUnmanaged(comptime K: type, comptime V: type) type` |
| `StringArrayHashMap` | `pub fn StringArrayHashMap(comptime V: type) type` |
| `StringArrayHashMapUnmanaged` | `pub fn StringArrayHashMapUnmanaged(comptime V: type) type` |
| `hash` | `pub fn hash(self: @This(), s: []const u8) u32` |
| `eql` | `pub fn eql(self: @This(), a: []const u8, b: []const u8, b_index: usize) bool` |
| `eqlString` | `pub fn eqlString(a: []const u8, b: []const u8) bool` |
| `hashString` | `pub fn hashString(s: []const u8) u32` |
| `ArrayHashMap` | `pub fn ArrayHashMap( comptime K: type, comptime V: type, comptime Context: type, comptime store_hash: bool, ) type` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `initContext` | `pub fn initContext(allocator: Allocator, ctx: Context) Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
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
| `capacity` | `pub fn capacity(self: *Self) usize` |
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
| `reIndex` | `pub fn reIndex(self: *Self) !void` |
| `sort` | `pub fn sort(self: *Self, sort_ctx: anytype) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, new_len: usize) void` |
| `pop` | `pub fn pop(self: *Self) KV` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?KV` |
| `ArrayHashMapUnmanaged` | `pub fn ArrayHashMapUnmanaged( comptime K: type, comptime V: type, comptime Context: type, comptime store_hash: bool, ) type` |
| `promote` | `pub fn promote(self: Self, allocator: Allocator) Managed` |
| `promoteContext` | `pub fn promoteContext(self: Self, allocator: Allocator, ctx: Context) Managed` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, allocator: Allocator) void` |
| `count` | `pub fn count(self: Self) usize` |
| `keys` | `pub fn keys(self: Self) []K` |
| `values` | `pub fn values(self: Self) []V` |
| `iterator` | `pub fn iterator(self: Self) Iterator` |
| `next` | `pub fn next(it: *Iterator) ?Entry` |
| `reset` | `pub fn reset(it: *Iterator) void` |
| `getOrPut` | `pub fn getOrPut(self: *Self, allocator: Allocator, key: K) !GetOrPutResult` |
| `getOrPutContext` | `pub fn getOrPutContext(self: *Self, allocator: Allocator, key: K, ctx: Context) !GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype) !GetOrPutResult` |
| `getOrPutContextAdapted` | `pub fn getOrPutContextAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype, ctx: Context) !GetOrPutResult` |
| `getOrPutAssumeCapacity` | `pub fn getOrPutAssumeCapacity(self: *Self, key: K) GetOrPutResult` |
| `getOrPutAssumeCapacityContext` | `pub fn getOrPutAssumeCapacityContext(self: *Self, key: K, ctx: Context) GetOrPutResult` |
| `getOrPutAssumeCapacityAdapted` | `pub fn getOrPutAssumeCapacityAdapted(self: *Self, key: anytype, ctx: anytype) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, allocator: Allocator, key: K, value: V) !GetOrPutResult` |
| `getOrPutValueContext` | `pub fn getOrPutValueContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) !GetOrPutResult` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, allocator: Allocator, new_capacity: usize) !void` |
| `ensureTotalCapacityContext` | `pub fn ensureTotalCapacityContext(self: *Self, allocator: Allocator, new_capacity: usize, ctx: Context) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity( self: *Self, allocator: Allocator, additional_capacity: usize, ) !void` |
| `ensureUnusedCapacityContext` | `pub fn ensureUnusedCapacityContext( self: *Self, allocator: Allocator, additional_capacity: usize, ctx: Context, ) !void` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `put` | `pub fn put(self: *Self, allocator: Allocator, key: K, value: V) !void` |
| `putContext` | `pub fn putContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) !void` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, allocator: Allocator, key: K, value: V) !void` |
| `putNoClobberContext` | `pub fn putNoClobberContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) !void` |
| `putAssumeCapacity` | `pub fn putAssumeCapacity(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityContext` | `pub fn putAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `putAssumeCapacityNoClobber` | `pub fn putAssumeCapacityNoClobber(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityNoClobberContext` | `pub fn putAssumeCapacityNoClobberContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, allocator: Allocator, key: K, value: V) !?KV` |
| `fetchPutContext` | `pub fn fetchPutContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) !?KV` |
| `fetchPutAssumeCapacity` | `pub fn fetchPutAssumeCapacity(self: *Self, key: K, value: V) ?KV` |
| `fetchPutAssumeCapacityContext` | `pub fn fetchPutAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) ?KV` |
| `getEntry` | `pub fn getEntry(self: Self, key: K) ?Entry` |
| `getEntryContext` | `pub fn getEntryContext(self: Self, key: K, ctx: Context) ?Entry` |
| `getEntryAdapted` | `pub fn getEntryAdapted(self: Self, key: anytype, ctx: anytype) ?Entry` |
| `getIndex` | `pub fn getIndex(self: Self, key: K) ?usize` |
| `getIndexContext` | `pub fn getIndexContext(self: Self, key: K, ctx: Context) ?usize` |
| `getIndexAdapted` | `pub fn getIndexAdapted(self: Self, key: anytype, ctx: anytype) ?usize` |
| `get` | `pub fn get(self: Self, key: K) ?V` |
| `getContext` | `pub fn getContext(self: Self, key: K, ctx: Context) ?V` |
| `getAdapted` | `pub fn getAdapted(self: Self, key: anytype, ctx: anytype) ?V` |
| `getPtr` | `pub fn getPtr(self: Self, key: K) ?*V` |
| `getPtrContext` | `pub fn getPtrContext(self: Self, key: K, ctx: Context) ?*V` |
| `getPtrAdapted` | `pub fn getPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*V` |
| `getKey` | `pub fn getKey(self: Self, key: K) ?K` |
| `getKeyContext` | `pub fn getKeyContext(self: Self, key: K, ctx: Context) ?K` |
| `getKeyAdapted` | `pub fn getKeyAdapted(self: Self, key: anytype, ctx: anytype) ?K` |
| `getKeyPtr` | `pub fn getKeyPtr(self: Self, key: K) ?*K` |
| `getKeyPtrContext` | `pub fn getKeyPtrContext(self: Self, key: K, ctx: Context) ?*K` |
| `getKeyPtrAdapted` | `pub fn getKeyPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*K` |
| `contains` | `pub fn contains(self: Self, key: K) bool` |
| `containsContext` | `pub fn containsContext(self: Self, key: K, ctx: Context) bool` |
| `containsAdapted` | `pub fn containsAdapted(self: Self, key: anytype, ctx: anytype) bool` |
| `fetchSwapRemove` | `pub fn fetchSwapRemove(self: *Self, key: K) ?KV` |
| `fetchSwapRemoveContext` | `pub fn fetchSwapRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `fetchSwapRemoveAdapted` | `pub fn fetchSwapRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `fetchSwapRemoveContextAdapted` | `pub fn fetchSwapRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) ?KV` |
| `fetchOrderedRemove` | `pub fn fetchOrderedRemove(self: *Self, key: K) ?KV` |
| `fetchOrderedRemoveContext` | `pub fn fetchOrderedRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `fetchOrderedRemoveAdapted` | `pub fn fetchOrderedRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `fetchOrderedRemoveContextAdapted` | `pub fn fetchOrderedRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) ?KV` |
| `swapRemove` | `pub fn swapRemove(self: *Self, key: K) bool` |
| `swapRemoveContext` | `pub fn swapRemoveContext(self: *Self, key: K, ctx: Context) bool` |
| `swapRemoveAdapted` | `pub fn swapRemoveAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `swapRemoveContextAdapted` | `pub fn swapRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) bool` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, key: K) bool` |
| `orderedRemoveContext` | `pub fn orderedRemoveContext(self: *Self, key: K, ctx: Context) bool` |
| `orderedRemoveAdapted` | `pub fn orderedRemoveAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `orderedRemoveContextAdapted` | `pub fn orderedRemoveContextAdapted(self: *Self, key: anytype, key_ctx: anytype, ctx: Context) bool` |
| `swapRemoveAt` | `pub fn swapRemoveAt(self: *Self, index: usize) void` |
| `swapRemoveAtContext` | `pub fn swapRemoveAtContext(self: *Self, index: usize, ctx: Context) void` |
| `orderedRemoveAt` | `pub fn orderedRemoveAt(self: *Self, index: usize) void` |
| `orderedRemoveAtContext` | `pub fn orderedRemoveAtContext(self: *Self, index: usize, ctx: Context) void` |
| `clone` | `pub fn clone(self: Self, allocator: Allocator) !Self` |
| `cloneContext` | `pub fn cloneContext(self: Self, allocator: Allocator, ctx: Context) !Self` |
| `reIndex` | `pub fn reIndex(self: *Self, allocator: Allocator) !void` |
| `reIndexContext` | `pub fn reIndexContext(self: *Self, allocator: Allocator, ctx: Context) !void` |
| `sort` | `pub inline fn sort(self: *Self, sort_ctx: anytype) void` |
| `sortContext` | `pub fn sortContext(self: *Self, sort_ctx: anytype, ctx: Context) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `shrinkRetainingCapacityContext` | `pub fn shrinkRetainingCapacityContext(self: *Self, new_len: usize, ctx: Context) void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, allocator: Allocator, new_len: usize) void` |
| `shrinkAndFreeContext` | `pub fn shrinkAndFreeContext(self: *Self, allocator: Allocator, new_len: usize, ctx: Context) void` |
| `pop` | `pub fn pop(self: *Self) KV` |
| `popContext` | `pub fn popContext(self: *Self, ctx: Context) KV` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?KV` |
| `popOrNullContext` | `pub fn popOrNullContext(self: *Self, ctx: Context) ?KV` |
| `f` | `pub fn f(allocator: Allocator) !void` |
| `lessThan` | `pub fn lessThan(ctx: @This(), a_index: usize, b_index: usize) bool` |
| `getHashPtrAddrFn` | `pub fn getHashPtrAddrFn(comptime K: type, comptime Context: type) (fn (Context, K) u32)` |
| `getTrivialEqlFn` | `pub fn getTrivialEqlFn(comptime K: type, comptime Context: type) (fn (Context, K, K) bool)` |
| `AutoContext` | `pub fn AutoContext(comptime K: type) type` |
| `getAutoHashFn` | `pub fn getAutoHashFn(comptime K: type, comptime Context: type) (fn (Context, K) u32)` |
| `getAutoEqlFn` | `pub fn getAutoEqlFn(comptime K: type, comptime Context: type) (fn (Context, K, K, usize) bool)` |
| `autoEqlIsCheap` | `pub fn autoEqlIsCheap(comptime K: type) bool` |
| `getAutoHashStratFn` | `pub fn getAutoHashStratFn(comptime K: type, comptime Context: type, comptime strategy: std.hash.Strategy) (fn (Context, K) u32)` |

## array_list

| Function | Signature |
|----------|-----------|
| `ArrayList` | `pub fn ArrayList(comptime T: type) type` |
| `ArrayListAligned` | `pub fn ArrayListAligned(comptime T: type, comptime alignment: ?u29) type` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `initCapacity` | `pub fn initCapacity(allocator: Allocator, num: usize) Allocator.Error!Self` |
| `deinit` | `pub fn deinit(self: Self) void` |
| `fromOwnedSlice` | `pub fn fromOwnedSlice(allocator: Allocator, slice: Slice) Self` |
| `moveToUnmanaged` | `pub fn moveToUnmanaged(self: *Self) ArrayListAlignedUnmanaged(T, alignment)` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self) Slice` |
| `toOwnedSliceSentinel` | `pub fn toOwnedSliceSentinel(self: *Self, comptime sentinel: T) Allocator.Error![:sentinel]T` |
| `clone` | `pub fn clone(self: *Self) Allocator.Error!Self` |
| `insert` | `pub fn insert(self: *Self, n: usize, item: T) Allocator.Error!void` |
| `insertSlice` | `pub fn insertSlice(self: *Self, i: usize, items: []const T) Allocator.Error!void` |
| `replaceRange` | `pub fn replaceRange(self: *Self, start: usize, len: usize, new_items: []const T) Allocator.Error!void` |
| `append` | `pub fn append(self: *Self, item: T) Allocator.Error!void` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, item: T) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, i: usize) T` |
| `swapRemove` | `pub fn swapRemove(self: *Self, i: usize) T` |
| `appendSlice` | `pub fn appendSlice(self: *Self, items: []const T) Allocator.Error!void` |
| `appendSliceAssumeCapacity` | `pub fn appendSliceAssumeCapacity(self: *Self, items: []const T) void` |
| `appendUnalignedSlice` | `pub fn appendUnalignedSlice(self: *Self, items: []align(1) const T) Allocator.Error!void` |
| `appendUnalignedSliceAssumeCapacity` | `pub fn appendUnalignedSliceAssumeCapacity(self: *Self, items: []align(1) const T) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
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
| `pop` | `pub fn pop(self: *Self) T` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?T` |
| `allocatedSlice` | `pub fn allocatedSlice(self: Self) Slice` |
| `unusedCapacitySlice` | `pub fn unusedCapacitySlice(self: Self) Slice` |
| `ArrayListUnmanaged` | `pub fn ArrayListUnmanaged(comptime T: type) type` |
| `ArrayListAlignedUnmanaged` | `pub fn ArrayListAlignedUnmanaged(comptime T: type, comptime alignment: ?u29) type` |
| `initCapacity` | `pub fn initCapacity(allocator: Allocator, num: usize) Allocator.Error!Self` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `toManaged` | `pub fn toManaged(self: *Self, allocator: Allocator) ArrayListAligned(T, alignment)` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self, allocator: Allocator) Slice` |
| `toOwnedSliceSentinel` | `pub fn toOwnedSliceSentinel(self: *Self, allocator: Allocator, comptime sentinel: T) Allocator.Error![:sentinel]T` |
| `clone` | `pub fn clone(self: *Self, allocator: Allocator) Allocator.Error!Self` |
| `insert` | `pub fn insert(self: *Self, allocator: Allocator, n: usize, item: T) Allocator.Error!void` |
| `insertSlice` | `pub fn insertSlice(self: *Self, allocator: Allocator, i: usize, items: []const T) Allocator.Error!void` |
| `replaceRange` | `pub fn replaceRange(self: *Self, allocator: Allocator, start: usize, len: usize, new_items: []const T) Allocator.Error!void` |
| `append` | `pub fn append(self: *Self, allocator: Allocator, item: T) Allocator.Error!void` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, item: T) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, i: usize) T` |
| `swapRemove` | `pub fn swapRemove(self: *Self, i: usize) T` |
| `appendSlice` | `pub fn appendSlice(self: *Self, allocator: Allocator, items: []const T) Allocator.Error!void` |
| `appendSliceAssumeCapacity` | `pub fn appendSliceAssumeCapacity(self: *Self, items: []const T) void` |
| `appendUnalignedSlice` | `pub fn appendUnalignedSlice(self: *Self, allocator: Allocator, items: []align(1) const T) Allocator.Error!void` |
| `appendUnalignedSliceAssumeCapacity` | `pub fn appendUnalignedSliceAssumeCapacity(self: *Self, items: []align(1) const T) void` |
| `writer` | `pub fn writer(self: *Self, allocator: Allocator) Writer` |
| `appendNTimes` | `pub fn appendNTimes(self: *Self, allocator: Allocator, value: T, n: usize) Allocator.Error!void` |
| `appendNTimesAssumeCapacity` | `pub fn appendNTimesAssumeCapacity(self: *Self, value: T, n: usize) void` |
| `resize` | `pub fn resize(self: *Self, allocator: Allocator, new_len: usize) Allocator.Error!void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, allocator: Allocator, new_len: usize) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, allocator: Allocator) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, allocator: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureTotalCapacityPrecise` | `pub fn ensureTotalCapacityPrecise(self: *Self, allocator: Allocator, new_capacity: usize) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity( self: *Self, allocator: Allocator, additional_count: usize, ) Allocator.Error!void` |
| `expandToCapacity` | `pub fn expandToCapacity(self: *Self) void` |
| `addOne` | `pub fn addOne(self: *Self, allocator: Allocator) Allocator.Error!*T` |
| `addOneAssumeCapacity` | `pub fn addOneAssumeCapacity(self: *Self) *T` |
| `addManyAsArray` | `pub fn addManyAsArray(self: *Self, allocator: Allocator, comptime n: usize) Allocator.Error!*[n]T` |
| `addManyAsArrayAssumeCapacity` | `pub fn addManyAsArrayAssumeCapacity(self: *Self, comptime n: usize) *[n]T` |
| `pop` | `pub fn pop(self: *Self) T` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?T` |
| `allocatedSlice` | `pub fn allocatedSlice(self: Self) Slice` |
| `unusedCapacitySlice` | `pub fn unusedCapacitySlice(self: Self) Slice` |

## ascii

| Function | Signature |
|----------|-----------|
| `isAlphanumeric` | `pub fn isAlphanumeric(c: u8) bool` |
| `isAlphabetic` | `pub fn isAlphabetic(c: u8) bool` |
| `isControl` | `pub fn isControl(c: u8) bool` |
| `isDigit` | `pub fn isDigit(c: u8) bool` |
| `isGraph` | `pub fn isGraph(c: u8) bool` |
| `isLower` | `pub fn isLower(c: u8) bool` |
| `isPrint` | `pub fn isPrint(c: u8) bool` |
| `isPunct` | `pub fn isPunct(c: u8) bool` |
| `isWhitespace` | `pub fn isWhitespace(c: u8) bool` |
| `isUpper` | `pub fn isUpper(c: u8) bool` |
| `isHex` | `pub fn isHex(c: u8) bool` |
| `isASCII` | `pub fn isASCII(c: u8) bool` |
| `isBlank` | `pub fn isBlank(c: u8) bool` |
| `toUpper` | `pub fn toUpper(c: u8) u8` |
| `toLower` | `pub fn toLower(c: u8) u8` |
| `lowerString` | `pub fn lowerString(output: []u8, ascii_string: []const u8) []u8` |
| `allocLowerString` | `pub fn allocLowerString(allocator: std.mem.Allocator, ascii_string: []const u8) ![]u8` |
| `upperString` | `pub fn upperString(output: []u8, ascii_string: []const u8) []u8` |
| `allocUpperString` | `pub fn allocUpperString(allocator: std.mem.Allocator, ascii_string: []const u8) ![]u8` |
| `eqlIgnoreCase` | `pub fn eqlIgnoreCase(a: []const u8, b: []const u8) bool` |
| `startsWithIgnoreCase` | `pub fn startsWithIgnoreCase(haystack: []const u8, needle: []const u8) bool` |
| `endsWithIgnoreCase` | `pub fn endsWithIgnoreCase(haystack: []const u8, needle: []const u8) bool` |
| `indexOfIgnoreCase` | `pub fn indexOfIgnoreCase(haystack: []const u8, needle: []const u8) ?usize` |
| `indexOfIgnoreCasePos` | `pub fn indexOfIgnoreCasePos(haystack: []const u8, start_index: usize, needle: []const u8) ?usize` |
| `indexOfIgnoreCasePosLinear` | `pub fn indexOfIgnoreCasePosLinear(haystack: []const u8, start_index: usize, needle: []const u8) ?usize` |
| `orderIgnoreCase` | `pub fn orderIgnoreCase(lhs: []const u8, rhs: []const u8) std.math.Order` |
| `lessThanIgnoreCase` | `pub fn lessThanIgnoreCase(lhs: []const u8, rhs: []const u8) bool` |

## atomic

| Function | Signature |
|----------|-----------|
| `fence` | `pub inline fn fence(comptime ordering: Ordering) void` |
| `compilerFence` | `pub inline fn compilerFence(comptime ordering: Ordering) void` |
| `spinLoopHint` | `pub inline fn spinLoopHint() void` |

## atomic / Atomic

| Function | Signature |
|----------|-----------|
| `Atomic` | `pub fn Atomic(comptime T: type) type` |
| `init` | `pub fn init(value: T) Self` |
| `fence` | `pub inline fn fence(self: *Self, comptime ordering: Ordering) void` |
| `loadUnchecked` | `pub inline fn loadUnchecked(self: Self) T` |
| `storeUnchecked` | `pub inline fn storeUnchecked(self: *Self, value: T) void` |
| `load` | `pub inline fn load(self: *const Self, comptime ordering: Ordering) T` |
| `store` | `pub inline fn store(self: *Self, value: T, comptime ordering: Ordering) void` |
| `swap` | `pub inline fn swap(self: *Self, value: T, comptime ordering: Ordering) T` |
| `compareAndSwap` | `pub inline fn compareAndSwap( self: *Self, compare: T, exchange: T, comptime success: Ordering, comptime failure: Ordering, ) ?T` |
| `tryCompareAndSwap` | `pub inline fn tryCompareAndSwap( self: *Self, compare: T, exchange: T, comptime success: Ordering, comptime failure: Ordering, ) ?T` |
| `fetchAdd` | `pub inline fn fetchAdd(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchSub` | `pub inline fn fetchSub(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchMin` | `pub inline fn fetchMin(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchMax` | `pub inline fn fetchMax(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchAnd` | `pub inline fn fetchAnd(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchNand` | `pub inline fn fetchNand(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchOr` | `pub inline fn fetchOr(self: *Self, value: T, comptime ordering: Ordering) T` |
| `fetchXor` | `pub inline fn fetchXor(self: *Self, value: T, comptime ordering: Ordering) T` |
| `bitSet` | `pub inline fn bitSet(self: *Self, bit: Bit, comptime ordering: Ordering) u1` |
| `bitReset` | `pub inline fn bitReset(self: *Self, bit: Bit, comptime ordering: Ordering) u1` |
| `bitToggle` | `pub inline fn bitToggle(self: *Self, bit: Bit, comptime ordering: Ordering) u1` |

## atomic / queue

| Function | Signature |
|----------|-----------|
| `Queue` | `pub fn Queue(comptime T: type) type` |
| `init` | `pub fn init() Self` |
| `put` | `pub fn put(self: *Self, node: *Node) void` |
| `get` | `pub fn get(self: *Self) ?*Node` |
| `unget` | `pub fn unget(self: *Self, node: *Node) void` |
| `remove` | `pub fn remove(self: *Self, node: *Node) bool` |
| `isEmpty` | `pub fn isEmpty(self: *Self) bool` |
| `dump` | `pub fn dump(self: *Self) void` |
| `dumpToStream` | `pub fn dumpToStream(self: *Self, stream: anytype) !void` |

## atomic / stack

| Function | Signature |
|----------|-----------|
| `Stack` | `pub fn Stack(comptime T: type) type` |
| `init` | `pub fn init() Self` |
| `pushFirst` | `pub fn pushFirst(self: *Self, node: *Node) ?*Node` |
| `push` | `pub fn push(self: *Self, node: *Node) void` |
| `pop` | `pub fn pop(self: *Self) ?*Node` |
| `isEmpty` | `pub fn isEmpty(self: *Self) bool` |

## base64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8) Base64Encoder` |
| `calcSize` | `pub fn calcSize(encoder: *const Base64Encoder, source_len: usize) usize` |
| `encode` | `pub fn encode(encoder: *const Base64Encoder, dest: []u8, source: []const u8) []const u8` |
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8) Base64Decoder` |
| `calcSizeUpperBound` | `pub fn calcSizeUpperBound(decoder: *const Base64Decoder, source_len: usize) Error!usize` |
| `calcSizeForSlice` | `pub fn calcSizeForSlice(decoder: *const Base64Decoder, source: []const u8) Error!usize` |
| `decode` | `pub fn decode(decoder: *const Base64Decoder, dest: []u8, source: []const u8) Error!void` |
| `init` | `pub fn init(alphabet_chars: [64]u8, pad_char: ?u8, ignore_chars: []const u8) Base64DecoderWithIgnore` |
| `calcSizeUpperBound` | `pub fn calcSizeUpperBound(decoder_with_ignore: *const Base64DecoderWithIgnore, source_len: usize) Error!usize` |
| `decode` | `pub fn decode(decoder_with_ignore: *const Base64DecoderWithIgnore, dest: []u8, source: []const u8) Error!usize` |

## bit_set

| Function | Signature |
|----------|-----------|
| `StaticBitSet` | `pub fn StaticBitSet(comptime size: usize) type` |
| `IntegerBitSet` | `pub fn IntegerBitSet(comptime size: u16) type` |
| `initEmpty` | `pub fn initEmpty() Self` |
| `initFull` | `pub fn initFull() Self` |
| `capacity` | `pub inline fn capacity(self: Self) usize` |
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
| `toggleFirstSet` | `pub fn toggleFirstSet(self: *Self) ?usize` |
| `iterator` | `pub fn iterator(self: *const Self, comptime options: IteratorOptions) Iterator(options)` |
| `Iterator` | `pub fn Iterator(comptime options: IteratorOptions) type` |
| `next` | `pub fn next(self: *IterSelf) ?usize` |
| `ArrayBitSet` | `pub fn ArrayBitSet(comptime MaskIntType: type, comptime size: usize) type` |
| `initEmpty` | `pub fn initEmpty() Self` |
| `initFull` | `pub fn initFull() Self` |
| `capacity` | `pub inline fn capacity(self: Self) usize` |
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
| `toggleFirstSet` | `pub fn toggleFirstSet(self: *Self) ?usize` |
| `iterator` | `pub fn iterator(self: *const Self, comptime options: IteratorOptions) Iterator(options)` |
| `Iterator` | `pub fn Iterator(comptime options: IteratorOptions) type` |
| `initEmpty` | `pub fn initEmpty(allocator: Allocator, bit_length: usize) !Self` |
| `initFull` | `pub fn initFull(allocator: Allocator, bit_length: usize) !Self` |
| `resize` | `pub fn resize(self: *@This(), allocator: Allocator, new_len: usize, fill: bool) !void` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `clone` | `pub fn clone(self: *const Self, new_allocator: Allocator) !Self` |
| `capacity` | `pub inline fn capacity(self: Self) usize` |
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
| `toggleFirstSet` | `pub fn toggleFirstSet(self: *Self) ?usize` |
| `iterator` | `pub fn iterator(self: *const Self, comptime options: IteratorOptions) Iterator(options)` |
| `Iterator` | `pub fn Iterator(comptime options: IteratorOptions) type` |
| `initEmpty` | `pub fn initEmpty(allocator: Allocator, bit_length: usize) !Self` |
| `initFull` | `pub fn initFull(allocator: Allocator, bit_length: usize) !Self` |
| `resize` | `pub fn resize(self: *@This(), new_len: usize, fill: bool) !void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `clone` | `pub fn clone(self: *const Self, new_allocator: Allocator) !Self` |
| `capacity` | `pub inline fn capacity(self: Self) usize` |
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
| `toggleFirstSet` | `pub fn toggleFirstSet(self: *Self) ?usize` |
| `iterator` | `pub fn iterator(self: *const Self, comptime options: IteratorOptions) Iterator(options)` |
| `next` | `pub fn next(self: *Self) ?usize` |

## bounded_array

| Function | Signature |
|----------|-----------|
| `BoundedArray` | `pub fn BoundedArray(comptime T: type, comptime buffer_capacity: usize) type` |
| `init` | `pub fn init(len: usize) error` |
| `slice` | `pub fn slice(self: anytype) mem.Span(@TypeOf(&self.buffer))` |
| `constSlice` | `pub fn constSlice(self: *const Self) []const T` |
| `resize` | `pub fn resize(self: *Self, len: usize) error` |
| `fromSlice` | `pub fn fromSlice(m: []const T) error` |
| `get` | `pub fn get(self: Self, i: usize) T` |
| `set` | `pub fn set(self: *Self, i: usize, item: T) void` |
| `capacity` | `pub fn capacity(self: Self) usize` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: Self, additional_count: usize) error` |
| `addOne` | `pub fn addOne(self: *Self) error` |
| `addOneAssumeCapacity` | `pub fn addOneAssumeCapacity(self: *Self) *T` |
| `addManyAsArray` | `pub fn addManyAsArray(self: *Self, comptime n: usize) error` |
| `pop` | `pub fn pop(self: *Self) T` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?T` |
| `unusedCapacitySlice` | `pub fn unusedCapacitySlice(self: *Self) []T` |
| `insert` | `pub fn insert( self: *Self, i: usize, item: T, ) error` |
| `insertSlice` | `pub fn insertSlice(self: *Self, i: usize, items: []const T) error` |
| `replaceRange` | `pub fn replaceRange( self: *Self, start: usize, len: usize, new_items: []const T, ) error` |
| `append` | `pub fn append(self: *Self, item: T) error` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, item: T) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, i: usize) T` |
| `swapRemove` | `pub fn swapRemove(self: *Self, i: usize) T` |
| `appendSlice` | `pub fn appendSlice(self: *Self, items: []const T) error` |
| `appendSliceAssumeCapacity` | `pub fn appendSliceAssumeCapacity(self: *Self, items: []const T) void` |
| `appendNTimes` | `pub fn appendNTimes(self: *Self, value: T, n: usize) error` |
| `appendNTimesAssumeCapacity` | `pub fn appendNTimesAssumeCapacity(self: *Self, value: T, n: usize) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |

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
| `cloneWithAllocator` | `pub fn cloneWithAllocator( self: *const BufSet, new_allocator: Allocator, ) Allocator.Error!BufSet` |
| `clone` | `pub fn clone(self: *const BufSet) Allocator.Error!BufSet` |

## build

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create( allocator: Allocator, zig_exe: []const u8, build_root: []const u8, cache_root: []const u8, global_cache_root: []const u8, ) !*Builder` |
| `destroy` | `pub fn destroy(self: *Builder) void` |
| `resolveInstallPrefix` | `pub fn resolveInstallPrefix(self: *Builder, install_prefix: ?[]const u8, dir_list: DirList) void` |
| `addExecutable` | `pub fn addExecutable(self: *Builder, name: []const u8, root_src: ?[]const u8) *LibExeObjStep` |
| `addExecutableSource` | `pub fn addExecutableSource(builder: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `addOptions` | `pub fn addOptions(self: *Builder) *OptionsStep` |
| `addObject` | `pub fn addObject(self: *Builder, name: []const u8, root_src: ?[]const u8) *LibExeObjStep` |
| `addObjectSource` | `pub fn addObjectSource(builder: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `addSharedLibrary` | `pub fn addSharedLibrary( self: *Builder, name: []const u8, root_src: ?[]const u8, kind: LibExeObjStep.SharedLibKind, ) *LibExeObjStep` |
| `addSharedLibrarySource` | `pub fn addSharedLibrarySource( self: *Builder, name: []const u8, root_src: ?FileSource, kind: LibExeObjStep.SharedLibKind, ) *LibExeObjStep` |
| `addStaticLibrary` | `pub fn addStaticLibrary(self: *Builder, name: []const u8, root_src: ?[]const u8) *LibExeObjStep` |
| `addStaticLibrarySource` | `pub fn addStaticLibrarySource(self: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `addTest` | `pub fn addTest(self: *Builder, root_src: []const u8) *LibExeObjStep` |
| `addTestSource` | `pub fn addTestSource(self: *Builder, root_src: FileSource) *LibExeObjStep` |
| `addTestExe` | `pub fn addTestExe(self: *Builder, name: []const u8, root_src: []const u8) *LibExeObjStep` |
| `addTestExeSource` | `pub fn addTestExeSource(self: *Builder, name: []const u8, root_src: FileSource) *LibExeObjStep` |
| `addAssemble` | `pub fn addAssemble(self: *Builder, name: []const u8, src: []const u8) *LibExeObjStep` |
| `addAssembleSource` | `pub fn addAssembleSource(self: *Builder, name: []const u8, src: FileSource) *LibExeObjStep` |
| `addSystemCommand` | `pub fn addSystemCommand(self: *Builder, argv: []const []const u8) *RunStep` |
| `dupe` | `pub fn dupe(self: *Builder, bytes: []const u8) []u8` |
| `dupeStrings` | `pub fn dupeStrings(self: *Builder, strings: []const []const u8) [][]u8` |
| `dupePath` | `pub fn dupePath(self: *Builder, bytes: []const u8) []u8` |
| `dupePkg` | `pub fn dupePkg(self: *Builder, package: Pkg) Pkg` |
| `addWriteFile` | `pub fn addWriteFile(self: *Builder, file_path: []const u8, data: []const u8) *WriteFileStep` |
| `addWriteFiles` | `pub fn addWriteFiles(self: *Builder) *WriteFileStep` |
| `addLog` | `pub fn addLog(self: *Builder, comptime format: []const u8, args: anytype) *LogStep` |
| `addRemoveDirTree` | `pub fn addRemoveDirTree(self: *Builder, dir_path: []const u8) *RemoveDirStep` |
| `addFmt` | `pub fn addFmt(self: *Builder, paths: []const []const u8) *FmtStep` |
| `addTranslateC` | `pub fn addTranslateC(self: *Builder, source: FileSource) *TranslateCStep` |
| `version` | `pub fn version(self: *const Builder, major: u32, minor: u32, patch: u32) LibExeObjStep.SharedLibKind` |
| `make` | `pub fn make(self: *Builder, step_names: []const []const u8) !void` |
| `getInstallStep` | `pub fn getInstallStep(self: *Builder) *Step` |
| `getUninstallStep` | `pub fn getUninstallStep(self: *Builder) *Step` |
| `option` | `pub fn option(self: *Builder, comptime T: type, name_raw: []const u8, description_raw: []const u8) ?T` |
| `step` | `pub fn step(self: *Builder, name: []const u8, description: []const u8) *Step` |
| `setPreferredReleaseMode` | `pub fn setPreferredReleaseMode(self: *Builder, mode: std.builtin.Mode) void` |
| `standardReleaseOptions` | `pub fn standardReleaseOptions(self: *Builder) std.builtin.Mode` |
| `standardTargetOptions` | `pub fn standardTargetOptions(self: *Builder, args: StandardTargetOptionsArgs) CrossTarget` |
| `addUserInputOption` | `pub fn addUserInputOption(self: *Builder, name_raw: []const u8, value_raw: []const u8) !bool` |
| `addUserInputFlag` | `pub fn addUserInputFlag(self: *Builder, name_raw: []const u8) !bool` |
| `validateUserInputDidItFail` | `pub fn validateUserInputDidItFail(self: *Builder) bool` |
| `spawnChild` | `pub fn spawnChild(self: *Builder, argv: []const []const u8) !void` |
| `spawnChildEnvMap` | `pub fn spawnChildEnvMap(self: *Builder, cwd: ?[]const u8, env_map: *const EnvMap, argv: []const []const u8) !void` |
| `makePath` | `pub fn makePath(self: *Builder, path: []const u8) !void` |
| `installArtifact` | `pub fn installArtifact(self: *Builder, artifact: *LibExeObjStep) void` |
| `addInstallArtifact` | `pub fn addInstallArtifact(self: *Builder, artifact: *LibExeObjStep) *InstallArtifactStep` |
| `installFile` | `pub fn installFile(self: *Builder, src_path: []const u8, dest_rel_path: []const u8) void` |
| `installDirectory` | `pub fn installDirectory(self: *Builder, options: InstallDirectoryOptions) void` |
| `installBinFile` | `pub fn installBinFile(self: *Builder, src_path: []const u8, dest_rel_path: []const u8) void` |
| `installLibFile` | `pub fn installLibFile(self: *Builder, src_path: []const u8, dest_rel_path: []const u8) void` |
| `installRaw` | `pub fn installRaw(self: *Builder, artifact: *LibExeObjStep, dest_filename: []const u8, options: InstallRawStep.CreateOptions) *InstallRawStep` |
| `addInstallFile` | `pub fn addInstallFile(self: *Builder, source: FileSource, dest_rel_path: []const u8) *InstallFileStep` |
| `addInstallBinFile` | `pub fn addInstallBinFile(self: *Builder, source: FileSource, dest_rel_path: []const u8) *InstallFileStep` |
| `addInstallLibFile` | `pub fn addInstallLibFile(self: *Builder, source: FileSource, dest_rel_path: []const u8) *InstallFileStep` |
| `addInstallRaw` | `pub fn addInstallRaw(self: *Builder, artifact: *LibExeObjStep, dest_filename: []const u8, options: InstallRawStep.CreateOptions) *InstallRawStep` |
| `addInstallFileWithDir` | `pub fn addInstallFileWithDir( self: *Builder, source: FileSource, install_dir: InstallDir, dest_rel_path: []const u8, ) *InstallFileStep` |
| `addInstallDirectory` | `pub fn addInstallDirectory(self: *Builder, options: InstallDirectoryOptions) *InstallDirStep` |
| `pushInstalledFile` | `pub fn pushInstalledFile(self: *Builder, dir: InstallDir, dest_rel_path: []const u8) void` |
| `updateFile` | `pub fn updateFile(self: *Builder, source_path: []const u8, dest_path: []const u8) !void` |
| `truncateFile` | `pub fn truncateFile(self: *Builder, dest_path: []const u8) !void` |
| `pathFromRoot` | `pub fn pathFromRoot(self: *Builder, rel_path: []const u8) []u8` |
| `pathJoin` | `pub fn pathJoin(self: *Builder, paths: []const []const u8) []u8` |
| `fmt` | `pub fn fmt(self: *Builder, comptime format: []const u8, args: anytype) []u8` |
| `findProgram` | `pub fn findProgram(self: *Builder, names: []const []const u8, paths: []const []const u8) ![]const u8` |
| `execAllowFail` | `pub fn execAllowFail( self: *Builder, argv: []const []const u8, out_code: *u8, stderr_behavior: std.ChildProcess.StdIo, ) ExecError![]u8` |
| `execFromStep` | `pub fn execFromStep(self: *Builder, argv: []const []const u8, src_step: ?*Step) ![]u8` |
| `exec` | `pub fn exec(self: *Builder, argv: []const []const u8) ![]u8` |
| `addSearchPrefix` | `pub fn addSearchPrefix(self: *Builder, search_prefix: []const u8) void` |
| `getInstallPath` | `pub fn getInstallPath(self: *Builder, dir: InstallDir, dest_rel_path: []const u8) []const u8` |
| `getPath` | `pub fn getPath(self: GeneratedFile) []const u8` |
| `relative` | `pub fn relative(path: []const u8) FileSource` |
| `getDisplayName` | `pub fn getDisplayName(self: FileSource) []const u8` |
| `addStepDependencies` | `pub fn addStepDependencies(self: FileSource, step: *Step) void` |
| `getPath` | `pub fn getPath(self: FileSource, builder: *Builder) []const u8` |
| `dupe` | `pub fn dupe(self: FileSource, b: *Builder) FileSource` |
| `createSharedLibrary` | `pub fn createSharedLibrary(builder: *Builder, name: []const u8, root_src: ?FileSource, kind: SharedLibKind) *LibExeObjStep` |
| `createStaticLibrary` | `pub fn createStaticLibrary(builder: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `createObject` | `pub fn createObject(builder: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `createExecutable` | `pub fn createExecutable(builder: *Builder, name: []const u8, root_src: ?FileSource) *LibExeObjStep` |
| `createTest` | `pub fn createTest(builder: *Builder, name: []const u8, root_src: FileSource) *LibExeObjStep` |
| `createTestExe` | `pub fn createTestExe(builder: *Builder, name: []const u8, root_src: FileSource) *LibExeObjStep` |
| `setTarget` | `pub fn setTarget(self: *LibExeObjStep, target: CrossTarget) void` |
| `setOutputDir` | `pub fn setOutputDir(self: *LibExeObjStep, dir: []const u8) void` |
| `install` | `pub fn install(self: *LibExeObjStep) void` |
| `installRaw` | `pub fn installRaw(self: *LibExeObjStep, dest_filename: []const u8, options: InstallRawStep.CreateOptions) *InstallRawStep` |
| `run` | `pub fn run(exe: *LibExeObjStep) *RunStep` |
| `runEmulatable` | `pub fn runEmulatable(exe: *LibExeObjStep) *EmulatableRunStep` |
| `checkObject` | `pub fn checkObject(self: *LibExeObjStep, obj_format: std.Target.ObjectFormat) *CheckObjectStep` |
| `setLinkerScriptPath` | `pub fn setLinkerScriptPath(self: *LibExeObjStep, source: FileSource) void` |
| `linkFramework` | `pub fn linkFramework(self: *LibExeObjStep, framework_name: []const u8) void` |
| `linkFrameworkNeeded` | `pub fn linkFrameworkNeeded(self: *LibExeObjStep, framework_name: []const u8) void` |
| `linkFrameworkWeak` | `pub fn linkFrameworkWeak(self: *LibExeObjStep, framework_name: []const u8) void` |
| `dependsOnSystemLibrary` | `pub fn dependsOnSystemLibrary(self: LibExeObjStep, name: []const u8) bool` |
| `linkLibrary` | `pub fn linkLibrary(self: *LibExeObjStep, lib: *LibExeObjStep) void` |
| `isDynamicLibrary` | `pub fn isDynamicLibrary(self: *LibExeObjStep) bool` |
| `producesPdbFile` | `pub fn producesPdbFile(self: *LibExeObjStep) bool` |
| `linkLibC` | `pub fn linkLibC(self: *LibExeObjStep) void` |
| `linkLibCpp` | `pub fn linkLibCpp(self: *LibExeObjStep) void` |
| `defineCMacro` | `pub fn defineCMacro(self: *LibExeObjStep, name: []const u8, value: ?[]const u8) void` |
| `defineCMacroRaw` | `pub fn defineCMacroRaw(self: *LibExeObjStep, name_and_value: []const u8) void` |
| `linkSystemLibraryName` | `pub fn linkSystemLibraryName(self: *LibExeObjStep, name: []const u8) void` |
| `linkSystemLibraryNeededName` | `pub fn linkSystemLibraryNeededName(self: *LibExeObjStep, name: []const u8) void` |
| `linkSystemLibraryWeakName` | `pub fn linkSystemLibraryWeakName(self: *LibExeObjStep, name: []const u8) void` |
| `linkSystemLibraryPkgConfigOnly` | `pub fn linkSystemLibraryPkgConfigOnly(self: *LibExeObjStep, lib_name: []const u8) void` |
| `linkSystemLibraryNeededPkgConfigOnly` | `pub fn linkSystemLibraryNeededPkgConfigOnly(self: *LibExeObjStep, lib_name: []const u8) void` |
| `runPkgConfig` | `pub fn runPkgConfig(self: *LibExeObjStep, lib_name: []const u8) ![]const []const u8` |
| `linkSystemLibrary` | `pub fn linkSystemLibrary(self: *LibExeObjStep, name: []const u8) void` |
| `linkSystemLibraryNeeded` | `pub fn linkSystemLibraryNeeded(self: *LibExeObjStep, name: []const u8) void` |
| `linkSystemLibraryWeak` | `pub fn linkSystemLibraryWeak(self: *LibExeObjStep, name: []const u8) void` |
| `setNamePrefix` | `pub fn setNamePrefix(self: *LibExeObjStep, text: []const u8) void` |
| `setFilter` | `pub fn setFilter(self: *LibExeObjStep, text: ?[]const u8) void` |
| `addCSourceFiles` | `pub fn addCSourceFiles(self: *LibExeObjStep, files: []const []const u8, flags: []const []const u8) void` |
| `addCSourceFile` | `pub fn addCSourceFile(self: *LibExeObjStep, file: []const u8, flags: []const []const u8) void` |
| `addCSourceFileSource` | `pub fn addCSourceFileSource(self: *LibExeObjStep, source: CSourceFile) void` |
| `setVerboseLink` | `pub fn setVerboseLink(self: *LibExeObjStep, value: bool) void` |
| `setVerboseCC` | `pub fn setVerboseCC(self: *LibExeObjStep, value: bool) void` |
| `setBuildMode` | `pub fn setBuildMode(self: *LibExeObjStep, mode: std.builtin.Mode) void` |
| `overrideZigLibDir` | `pub fn overrideZigLibDir(self: *LibExeObjStep, dir_path: []const u8) void` |
| `setMainPkgPath` | `pub fn setMainPkgPath(self: *LibExeObjStep, dir_path: []const u8) void` |
| `setLibCFile` | `pub fn setLibCFile(self: *LibExeObjStep, libc_file: ?FileSource) void` |
| `getOutputSource` | `pub fn getOutputSource(self: *LibExeObjStep) FileSource` |
| `getOutputLibSource` | `pub fn getOutputLibSource(self: *LibExeObjStep) FileSource` |
| `getOutputHSource` | `pub fn getOutputHSource(self: *LibExeObjStep) FileSource` |
| `getOutputPdbSource` | `pub fn getOutputPdbSource(self: *LibExeObjStep) FileSource` |
| `addAssemblyFile` | `pub fn addAssemblyFile(self: *LibExeObjStep, path: []const u8) void` |
| `addAssemblyFileSource` | `pub fn addAssemblyFileSource(self: *LibExeObjStep, source: FileSource) void` |
| `addObjectFile` | `pub fn addObjectFile(self: *LibExeObjStep, source_file: []const u8) void` |
| `addObjectFileSource` | `pub fn addObjectFileSource(self: *LibExeObjStep, source: FileSource) void` |
| `addObject` | `pub fn addObject(self: *LibExeObjStep, obj: *LibExeObjStep) void` |
| `addSystemIncludePath` | `pub fn addSystemIncludePath(self: *LibExeObjStep, path: []const u8) void` |
| `addIncludePath` | `pub fn addIncludePath(self: *LibExeObjStep, path: []const u8) void` |
| `addLibraryPath` | `pub fn addLibraryPath(self: *LibExeObjStep, path: []const u8) void` |
| `addRPath` | `pub fn addRPath(self: *LibExeObjStep, path: []const u8) void` |
| `addFrameworkPath` | `pub fn addFrameworkPath(self: *LibExeObjStep, dir_path: []const u8) void` |
| `addPackage` | `pub fn addPackage(self: *LibExeObjStep, package: Pkg) void` |
| `addOptions` | `pub fn addOptions(self: *LibExeObjStep, package_name: []const u8, options: *OptionsStep) void` |
| `addPackagePath` | `pub fn addPackagePath(self: *LibExeObjStep, name: []const u8, pkg_index_path: []const u8) void` |
| `addVcpkgPaths` | `pub fn addVcpkgPaths(self: *LibExeObjStep, linkage: LibExeObjStep.Linkage) !void` |
| `setExecCmd` | `pub fn setExecCmd(self: *LibExeObjStep, args: []const ?[]const u8) void` |
| `constructCMacro` | `pub fn constructCMacro(allocator: Allocator, name: []const u8, value: ?[]const u8) []const u8` |
| `create` | `pub fn create(builder: *Builder, artifact: *LibExeObjStep) *Self` |
| `init` | `pub fn init( builder: *Builder, source: FileSource, dir: InstallDir, dest_rel_path: []const u8, ) InstallFileStep` |
| `init` | `pub fn init( builder: *Builder, options: InstallDirectoryOptions, ) InstallDirStep` |
| `init` | `pub fn init(builder: *Builder, data: []const u8) LogStep` |
| `init` | `pub fn init(builder: *Builder, dir_path: []const u8) RemoveDirStep` |
| `init` | `pub fn init(id: Id, name: []const u8, allocator: Allocator, makeFn: MakeFn) Step` |
| `initNoOp` | `pub fn initNoOp(id: Id, name: []const u8, allocator: Allocator) Step` |
| `make` | `pub fn make(self: *Step) !void` |
| `dependOn` | `pub fn dependOn(self: *Step, other: *Step) void` |
| `cast` | `pub fn cast(step: *Step, comptime T: type) ?*T` |
| `dupe` | `pub fn dupe(self: InstallDir, builder: *Builder) InstallDir` |
| `dupe` | `pub fn dupe(self: InstalledFile, builder: *Builder) InstalledFile` |

## build / CheckFileStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create( builder: *Builder, source: build.FileSource, expected_matches: []const []const u8, ) *CheckFileStep` |

## build / CheckObjectStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder, source: build.FileSource, obj_format: std.Target.ObjectFormat) *CheckObjectStep` |
| `runAndCompare` | `pub fn runAndCompare(self: *CheckObjectStep) *EmulatableRunStep` |
| `format` | `pub fn format( value: @This(), comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `checkStart` | `pub fn checkStart(self: *CheckObjectStep, phrase: []const u8) void` |
| `checkNext` | `pub fn checkNext(self: *CheckObjectStep, phrase: []const u8) void` |
| `checkNotPresent` | `pub fn checkNotPresent(self: *CheckObjectStep, phrase: []const u8) void` |
| `checkInSymtab` | `pub fn checkInSymtab(self: *CheckObjectStep) void` |
| `checkComputeCompare` | `pub fn checkComputeCompare( self: *CheckObjectStep, program: []const u8, expected: ComputeCompareExpected, ) void` |

## build / EmulatableRunStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder, name: []const u8, artifact: *LibExeObjStep) *EmulatableRunStep` |
| `expectStdErrEqual` | `pub fn expectStdErrEqual(self: *EmulatableRunStep, bytes: []const u8) void` |
| `expectStdOutEqual` | `pub fn expectStdOutEqual(self: *EmulatableRunStep, bytes: []const u8) void` |

## build / FmtStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder, paths: []const []const u8) *FmtStep` |

## build / InstallRawStep

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *Self) void` |
| `parse` | `pub fn parse(allocator: Allocator, elf_file: File) !Self` |
| `writeSegment` | `pub fn writeSegment(self: *HexWriter, segment: *const BinaryElfSegment, elf_file: File) !void` |
| `create` | `pub fn create(builder: *Builder, artifact: *LibExeObjStep, dest_filename: []const u8, options: CreateOptions) *InstallRawStep` |
| `getOutputSource` | `pub fn getOutputSource(self: *const InstallRawStep) std.build.FileSource` |

## build / OptionsStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder) *OptionsStep` |
| `addOption` | `pub fn addOption(self: *OptionsStep, comptime T: type, name: []const u8, value: T) void` |
| `addOptionFileSource` | `pub fn addOptionFileSource( self: *OptionsStep, name: []const u8, source: FileSource, ) void` |
| `addOptionArtifact` | `pub fn addOptionArtifact(self: *OptionsStep, name: []const u8, artifact: *LibExeObjStep) void` |
| `getPackage` | `pub fn getPackage(self: *OptionsStep, package_name: []const u8) build.Pkg` |
| `getSource` | `pub fn getSource(self: *OptionsStep) FileSource` |

## build / RunStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder, name: []const u8) *RunStep` |
| `addArtifactArg` | `pub fn addArtifactArg(self: *RunStep, artifact: *LibExeObjStep) void` |
| `addFileSourceArg` | `pub fn addFileSourceArg(self: *RunStep, file_source: build.FileSource) void` |
| `addArg` | `pub fn addArg(self: *RunStep, arg: []const u8) void` |
| `addArgs` | `pub fn addArgs(self: *RunStep, args: []const []const u8) void` |
| `clearEnvironment` | `pub fn clearEnvironment(self: *RunStep) void` |
| `addPathDir` | `pub fn addPathDir(self: *RunStep, search_path: []const u8) void` |
| `addPathDirInternal` | `pub fn addPathDirInternal(step: *Step, builder: *Builder, search_path: []const u8) void` |
| `getEnvMap` | `pub fn getEnvMap(self: *RunStep) *EnvMap` |
| `setEnvironmentVariable` | `pub fn setEnvironmentVariable(self: *RunStep, key: []const u8, value: []const u8) void` |
| `expectStdErrEqual` | `pub fn expectStdErrEqual(self: *RunStep, bytes: []const u8) void` |
| `expectStdOutEqual` | `pub fn expectStdOutEqual(self: *RunStep, bytes: []const u8) void` |
| `runCommand` | `pub fn runCommand( argv: []const []const u8, builder: *Builder, expected_exit_code: ?u8, stdout_action: StdIoAction, stderr_action: StdIoAction, stdin_behavior: std.ChildProcess.StdIo, env_map: ?*EnvMap, maybe_cwd: ?[]const u8, print: bool, ) !void` |
| `addPathForDynLibsInternal` | `pub fn addPathForDynLibsInternal(step: *Step, builder: *Builder, artifact: *LibExeObjStep) void` |

## build / TranslateCStep

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(builder: *Builder, source: build.FileSource) *TranslateCStep` |
| `setTarget` | `pub fn setTarget(self: *TranslateCStep, target: CrossTarget) void` |
| `addExecutable` | `pub fn addExecutable(self: *TranslateCStep) *LibExeObjStep` |
| `addIncludeDir` | `pub fn addIncludeDir(self: *TranslateCStep, include_dir: []const u8) void` |
| `addCheckFile` | `pub fn addCheckFile(self: *TranslateCStep, expected_matches: []const []const u8) *CheckFileStep` |
| `defineCMacro` | `pub fn defineCMacro(self: *TranslateCStep, name: []const u8, value: ?[]const u8) void` |
| `defineCMacroRaw` | `pub fn defineCMacroRaw(self: *TranslateCStep, name_and_value: []const u8) void` |

## build / WriteFileStep

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(builder: *Builder) WriteFileStep` |
| `add` | `pub fn add(self: *WriteFileStep, basename: []const u8, bytes: []const u8) void` |
| `getFileSource` | `pub fn getFileSource(step: *WriteFileStep, basename: []const u8) ?build.FileSource` |

## builtin

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format( self: StackTrace, comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `includesVersion` | `pub fn includesVersion(self: Range, ver: Version) bool` |
| `isAtLeast` | `pub fn isAtLeast(self: Range, ver: Version) ?bool` |
| `order` | `pub fn order(lhs: Version, rhs: Version) std.math.Order` |
| `parse` | `pub fn parse(text: []const u8) !Version` |
| `format` | `pub fn format( self: Version, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `default_panic` | `pub fn default_panic(msg: []const u8, error_return_trace: ?*StackTrace, ret_addr: ?usize) noreturn` |
| `create_exit_data` | `pub fn create_exit_data(exit_msg: []const u8, exit_size: *usize) ![*:0]u16` |
| `checkNonScalarSentinel` | `pub fn checkNonScalarSentinel(expected: anytype, actual: @TypeOf(expected)) void` |
| `panicSentinelMismatch` | `pub fn panicSentinelMismatch(expected: anytype, actual: @TypeOf(expected)) noreturn` |
| `panicUnwrapError` | `pub fn panicUnwrapError(st: ?*StackTrace, err: anyerror) noreturn` |
| `panicOutOfBounds` | `pub fn panicOutOfBounds(index: usize, len: usize) noreturn` |
| `addErrRetTraceAddr` | `pub inline fn addErrRetTraceAddr(st: *StackTrace, addr: usize) void` |

## c

| Function | Signature |
|----------|-----------|
| `versionCheck` | `pub fn versionCheck(comptime glibc_version: std.builtin.Version) type` |
| `getErrno` | `pub fn getErrno(rc: anytype) c.E` |

## c / darwin

| Function | Signature |
|----------|-----------|
| `mach_task_self` | `pub fn mach_task_self() callconv(.C) mach_port_t` |
| `sigaddset` | `pub fn sigaddset(set: *sigset_t, signo: u5) void` |
| `dispatch_once_f` | `pub extern fn dispatch_once_f( predicate: *dispatch_once_t, context: ?*anyopaque, function: dispatch_function_t, ) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `birthtime` | `pub fn birthtime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(x: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(x: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(x: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(x: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(x: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(x: u32) bool` |
| `getKernError` | `pub fn getKernError(err: kern_return_t) KernE` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `IWHT` | `pub fn IWHT(m: u32) bool` |

## c / dragonfly

| Function | Signature |
|----------|-----------|
| `_errno` | `pub fn _errno() *c_int` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |

## c / freebsd

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `birthtime` | `pub fn birthtime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `IDX` | `pub inline fn IDX(sig: usize) usize` |
| `WORD` | `pub inline fn WORD(sig: usize) usize` |
| `BIT` | `pub inline fn BIT(sig: usize) usize` |
| `VALID` | `pub inline fn VALID(sig: usize) usize` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `IWHT` | `pub fn IWHT(m: u32) bool` |

## c / haiku

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `birthtime` | `pub fn birthtime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `ISINDEX` | `pub fn ISINDEX(m: u32) bool` |

## c / linux

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## c / netbsd

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `birthtime` | `pub fn birthtime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFCONTINUED` | `pub fn IFCONTINUED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `IDX` | `pub inline fn IDX(sig: usize) usize` |
| `WORD` | `pub inline fn WORD(sig: usize) usize` |
| `BIT` | `pub inline fn BIT(sig: usize) usize` |
| `VALID` | `pub inline fn VALID(sig: usize) usize` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `IWHT` | `pub fn IWHT(m: u32) bool` |

## c / openbsd

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `birthtime` | `pub fn birthtime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFCONTINUED` | `pub fn IFCONTINUED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |

## c / solaris

| Function | Signature |
|----------|-----------|
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |
| `reclen` | `pub fn reclen(self: dirent) u16` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
| `STOPSIG` | `pub fn STOPSIG(s: u32) u32` |
| `IFEXITED` | `pub fn IFEXITED(s: u32) bool` |
| `IFCONTINUED` | `pub fn IFCONTINUED(s: u32) bool` |
| `IFSTOPPED` | `pub fn IFSTOPPED(s: u32) bool` |
| `IFSIGNALED` | `pub fn IFSIGNALED(s: u32) bool` |
| `IDX` | `pub inline fn IDX(sig: usize) usize` |
| `WORD` | `pub inline fn WORD(sig: usize) usize` |
| `BIT` | `pub inline fn BIT(sig: usize) usize` |
| `VALID` | `pub inline fn VALID(sig: usize) usize` |
| `ISFIFO` | `pub fn ISFIFO(m: u32) bool` |
| `ISCHR` | `pub fn ISCHR(m: u32) bool` |
| `ISDIR` | `pub fn ISDIR(m: u32) bool` |
| `ISBLK` | `pub fn ISBLK(m: u32) bool` |
| `ISREG` | `pub fn ISREG(m: u32) bool` |
| `ISLNK` | `pub fn ISLNK(m: u32) bool` |
| `ISSOCK` | `pub fn ISSOCK(m: u32) bool` |
| `ISDOOR` | `pub fn ISDOOR(m: u32) bool` |
| `ISPORT` | `pub fn ISPORT(m: u32) bool` |
| `isException` | `pub fn isException(event: u32) bool` |
| `IO` | `pub fn IO(io_type: u8, nr: u8) i32` |
| `IOR` | `pub fn IOR(io_type: u8, nr: u8, comptime IOT: type) i32` |
| `IOW` | `pub fn IOW(io_type: u8, nr: u8, comptime IOT: type) i32` |
| `IOWR` | `pub fn IOWR(io_type: u8, nr: u8, comptime IOT: type) i32` |

## c / tokenizer

| Function | Signature |
|----------|-----------|
| `symbol` | `pub fn symbol(id: Id) []const u8` |
| `symbolName` | `pub fn symbolName(id: std.meta.Tag(Id)) []const u8` |
| `getKeyword` | `pub fn getKeyword(bytes: []const u8, pp_directive: bool) ?Id` |
| `next` | `pub fn next(self: *Tokenizer) Token` |

## c / wasi

| Function | Signature |
|----------|-----------|
| `_errno` | `pub fn _errno() *c_int` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## child_process

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(argv: []const []const u8, allocator: mem.Allocator) ChildProcess` |
| `setUserName` | `pub fn setUserName(self: *ChildProcess, name: []const u8) !void` |
| `spawn` | `pub fn spawn(self: *ChildProcess) SpawnError!void` |
| `spawnAndWait` | `pub fn spawnAndWait(self: *ChildProcess) SpawnError!Term` |
| `kill` | `pub fn kill(self: *ChildProcess) !Term` |
| `killWindows` | `pub fn killWindows(self: *ChildProcess, exit_code: windows.UINT) !Term` |
| `killPosix` | `pub fn killPosix(self: *ChildProcess) !Term` |
| `wait` | `pub fn wait(self: *ChildProcess) !Term` |
| `exec` | `pub fn exec(args: struct { allocator: mem.Allocator, argv: []const []const u8, cwd: ?[]const u8 = null, cwd_dir: ?fs.Dir = null, env_map: ?*const EnvMap = null, max_output_bytes: usize = 50 * 1024, expand_arg0: Arg0Expand = .no_expand, }) !ExecResult` |
| `createWindowsEnvBlock` | `pub fn createWindowsEnvBlock(allocator: mem.Allocator, env_map: *const EnvMap) ![]u16` |
| `createNullDelimitedEnvMap` | `pub fn createNullDelimitedEnvMap(arena: mem.Allocator, env_map: *const EnvMap) ![:null]?[*:0]u8` |

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
| `sizeOf` | `pub fn sizeOf() usize` |
| `getName` | `pub fn getName(self: *const Symbol) ?[]const u8` |
| `getNameOffset` | `pub fn getNameOffset(self: Symbol) ?u32` |
| `getFileName` | `pub fn getFileName(self: *const FileDefinition) []const u8` |
| `fromTargetCpuArch` | `pub fn fromTargetCpuArch(arch: std.Target.Cpu.Arch) MachineType` |
| `toTargetCpuArch` | `pub fn toTargetCpuArch(machine_type: MachineType) ?std.Target.Cpu.Arch` |
| `deinit` | `pub fn deinit(self: *Coff) void` |
| `parse` | `pub fn parse(self: *Coff, data: []const u8) !void` |
| `getPdbPath` | `pub fn getPdbPath(self: *Coff, buffer: []u8) !usize` |
| `getCoffHeader` | `pub fn getCoffHeader(self: Coff) CoffHeader` |
| `getOptionalHeader` | `pub fn getOptionalHeader(self: Coff) OptionalHeader` |
| `getOptionalHeader32` | `pub fn getOptionalHeader32(self: Coff) OptionalHeaderPE32` |
| `getOptionalHeader64` | `pub fn getOptionalHeader64(self: Coff) OptionalHeaderPE64` |
| `getImageBase` | `pub fn getImageBase(self: Coff) u64` |
| `getNumberOfDataDirectories` | `pub fn getNumberOfDataDirectories(self: Coff) u32` |
| `getDataDirectories` | `pub fn getDataDirectories(self: *const Coff) []align(1) const ImageDataDirectory` |
| `getSymtab` | `pub fn getSymtab(self: *const Coff) ?Symtab` |
| `getStrtab` | `pub fn getStrtab(self: *const Coff) ?Strtab` |
| `getSectionHeaders` | `pub fn getSectionHeaders(self: *const Coff) []align(1) const SectionHeader` |
| `getSectionName` | `pub fn getSectionName(self: *const Coff, sect_hdr: *align(1) const SectionHeader) []const u8` |
| `getSectionByName` | `pub fn getSectionByName(self: *const Coff, comptime name: []const u8) ?*align(1) const SectionHeader` |
| `getSectionDataAlloc` | `pub fn getSectionDataAlloc(self: *const Coff, comptime name: []const u8, allocator: mem.Allocator) ![]u8` |
| `len` | `pub fn len(self: Symtab) usize` |
| `at` | `pub fn at(self: Symtab, index: usize, tag: Tag) Record` |
| `next` | `pub fn next(self: *Slice) ?Symbol` |
| `slice` | `pub fn slice(self: Symtab, start: usize, end: ?usize) Slice` |
| `get` | `pub fn get(self: Strtab, off: u32) []const u8` |

## compress / deflate / bits_utils

| Function | Signature |
|----------|-----------|
| `bitReverse` | `pub fn bitReverse(comptime T: type, value: T, N: usize) T` |

## compress / deflate / compressor

| Function | Signature |
|----------|-----------|
| `compressor` | `pub fn compressor( allocator: Allocator, writer: anytype, options: CompressorOptions, ) !Compressor(@TypeOf(writer))` |
| `Compressor` | `pub fn Compressor(comptime WriterType: anytype) type` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `bytesWritten` | `pub fn bytesWritten(self: *Self) usize` |
| `write` | `pub fn write(self: *Self, input: []const u8) !usize` |
| `flush` | `pub fn flush(self: *Self) !void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `reset` | `pub fn reset(self: *Self, new_writer: WriterType) void` |
| `close` | `pub fn close(self: *Self) !void` |

## compress / deflate / decompressor

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *Self) void` |
| `decompressor` | `pub fn decompressor(allocator: Allocator, reader: anytype, dictionary: ?[]const u8) !Decompressor(@TypeOf(reader))` |
| `Decompressor` | `pub fn Decompressor(comptime ReaderType: type) type` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `read` | `pub fn read(self: *Self, output: []u8) Error!usize` |
| `close` | `pub fn close(self: *Self) ?Error` |
| `reset` | `pub fn reset(s: *Self, new_reader: ReaderType, new_dict: ?[]const u8) !void` |

## compress / deflate / deflate_fast

| Function | Signature |
|----------|-----------|
| `deflateFast` | `pub fn deflateFast() DeflateFast` |
| `init` | `pub fn init(self: *Self, allocator: Allocator) !void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `encode` | `pub fn encode(self: *Self, dst: []token.Token, tokens_count: *u16, src: []u8) void` |
| `reset` | `pub fn reset(self: *Self) void` |

## compress / deflate / dict_decoder

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(self: *Self, allocator: Allocator, size: u32, dict: ?[]const u8) !void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `histSize` | `pub fn histSize(self: *Self) u32` |
| `availRead` | `pub fn availRead(self: *Self) u32` |
| `availWrite` | `pub fn availWrite(self: *Self) u32` |
| `writeSlice` | `pub fn writeSlice(self: *Self) []u8` |
| `writeMark` | `pub fn writeMark(self: *Self, count: u32) void` |
| `writeByte` | `pub fn writeByte(self: *Self, byte: u8) void` |
| `writeCopy` | `pub fn writeCopy(self: *Self, dist: u32, length: u32) u32` |
| `tryWriteCopy` | `pub fn tryWriteCopy(self: *Self, dist: u32, length: u32) u32` |
| `readFlush` | `pub fn readFlush(self: *Self) []u8` |

## compress / deflate / huffman_bit_writer

| Function | Signature |
|----------|-----------|
| `HuffmanBitWriter` | `pub fn HuffmanBitWriter(comptime WriterType: type) type` |
| `reset` | `pub fn reset(self: *Self, new_writer: WriterType) void` |
| `flush` | `pub fn flush(self: *Self) Error!void` |
| `writeBytes` | `pub fn writeBytes(self: *Self, bytes: []u8) Error!void` |
| `writeStoredHeader` | `pub fn writeStoredHeader(self: *Self, length: usize, is_eof: bool) Error!void` |
| `writeBlock` | `pub fn writeBlock( self: *Self, tokens: []const token.Token, eof: bool, input: ?[]u8, ) Error!void` |
| `writeBlockDynamic` | `pub fn writeBlockDynamic( self: *Self, tokens: []const token.Token, eof: bool, input: ?[]u8, ) Error!void` |
| `writeBlockHuff` | `pub fn writeBlockHuff(self: *Self, eof: bool, input: []u8) Error!void` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `huffmanBitWriter` | `pub fn huffmanBitWriter(allocator: Allocator, writer: anytype) !HuffmanBitWriter(@TypeOf(writer))` |

## compress / deflate / huffman_code

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *HuffmanEncoder) void` |
| `generate` | `pub fn generate(self: *HuffmanEncoder, freq: []u16, max_bits: u32) void` |
| `bitLength` | `pub fn bitLength(self: *HuffmanEncoder, freq: []u16) u32` |
| `newHuffmanEncoder` | `pub fn newHuffmanEncoder(allocator: Allocator, size: u32) !HuffmanEncoder` |
| `generateFixedLiteralEncoding` | `pub fn generateFixedLiteralEncoding(allocator: Allocator) !HuffmanEncoder` |
| `generateFixedOffsetEncoding` | `pub fn generateFixedOffsetEncoding(allocator: Allocator) !HuffmanEncoder` |

## compress / deflate / mem_utils

| Function | Signature |
|----------|-----------|
| `copy` | `pub fn copy(dst: []u8, src: []const u8) usize` |

## compress / deflate / token

| Function | Signature |
|----------|-----------|
| `literalToken` | `pub fn literalToken(lit: u32) Token` |
| `matchToken` | `pub fn matchToken(xlength: u32, xoffset: u32) Token` |
| `literal` | `pub fn literal(t: Token) u32` |
| `offset` | `pub fn offset(t: Token) u32` |
| `length` | `pub fn length(t: Token) u32` |
| `lengthCode` | `pub fn lengthCode(len: u32) u32` |
| `offsetCode` | `pub fn offsetCode(off: u32) u32` |

## compress / gzip

| Function | Signature |
|----------|-----------|
| `GzipStream` | `pub fn GzipStream(comptime ReaderType: type) type` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `read` | `pub fn read(self: *Self, buffer: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `gzipStream` | `pub fn gzipStream(allocator: mem.Allocator, reader: anytype) !GzipStream(@TypeOf(reader))` |

## compress / zlib

| Function | Signature |
|----------|-----------|
| `ZlibStream` | `pub fn ZlibStream(comptime ReaderType: type) type` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `read` | `pub fn read(self: *Self, buffer: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `zlibStream` | `pub fn zlibStream(allocator: mem.Allocator, reader: anytype) !ZlibStream(@TypeOf(reader))` |

## comptime_string_map

| Function | Signature |
|----------|-----------|
| `ComptimeStringMap` | `pub fn ComptimeStringMap(comptime V: type, comptime kvs_list: anytype) type` |
| `has` | `pub fn has(str: []const u8) bool` |
| `get` | `pub fn get(str: []const u8) ?V` |

## crypto / 25519 / curve25519

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub inline fn fromBytes(s: [32]u8) Curve25519` |
| `toBytes` | `pub inline fn toBytes(p: Curve25519) [32]u8` |
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
| `verify` | `pub fn verify(self: *Verifier) (SignatureVerificationError || WeakPublicKeyError || IdentityElementError)!void` |
| `toBytes` | `pub fn toBytes(self: Signature) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) Signature` |
| `verifier` | `pub fn verifier(self: Signature, public_key: PublicKey) (NonCanonicalError || EncodingError || IdentityElementError)!Verifier` |
| `verify` | `pub fn verify(self: Signature, msg: []const u8, public_key: PublicKey) (IdentityElementError || NonCanonicalError || SignatureVerificationError || EncodingError || WeakPublicKeyError)!void` |
| `create` | `pub fn create(seed: ?[seed_length]u8) IdentityElementError!KeyPair` |
| `fromSecretKey` | `pub fn fromSecretKey(secret_key: SecretKey) (NonCanonicalError || EncodingError || IdentityElementError)!KeyPair` |
| `sign` | `pub fn sign(key_pair: KeyPair, msg: []const u8, noise: ?[noise_length]u8) (IdentityElementError || NonCanonicalError || KeyMismatchError || WeakPublicKeyError)!Signature` |
| `signer` | `pub fn signer(key_pair: KeyPair, noise: ?[noise_length]u8) (IdentityElementError || KeyMismatchError || NonCanonicalError || WeakPublicKeyError)!Signer` |
| `verifyBatch` | `pub fn verifyBatch(comptime count: usize, signature_batch: [count]BatchElement) (SignatureVerificationError || IdentityElementError || WeakPublicKeyError || EncodingError || NonCanonicalError)!void` |
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
| `clearCofactor` | `pub fn clearCofactor(p: Edwards25519) Edwards25519` |
| `neg` | `pub inline fn neg(p: Edwards25519) Edwards25519` |
| `dbl` | `pub fn dbl(p: Edwards25519) Edwards25519` |
| `add` | `pub fn add(p: Edwards25519, q: Edwards25519) Edwards25519` |
| `sub` | `pub fn sub(p: Edwards25519, q: Edwards25519) Edwards25519` |
| `mul` | `pub fn mul(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `mulPublic` | `pub fn mulPublic(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: Edwards25519, s1: [32]u8, p2: Edwards25519, s2: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `mulMulti` | `pub fn mulMulti(comptime count: usize, ps: [count]Edwards25519, ss: [count][32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `clampedMul` | `pub fn clampedMul(p: Edwards25519, s: [32]u8) (IdentityElementError || WeakPublicKeyError)!Edwards25519` |
| `elligator2` | `pub fn elligator2(r: Fe) struct` |
| `fromHash` | `pub fn fromHash(h: [64]u8) Edwards25519` |
| `fromString` | `pub fn fromString(comptime random_oracle: bool, ctx: []const u8, s: []const u8) Edwards25519` |
| `fromUniform` | `pub fn fromUniform(r: [32]u8) Edwards25519` |

## crypto / 25519 / field

| Function | Signature |
|----------|-----------|
| `isZero` | `pub inline fn isZero(fe: Fe) bool` |
| `equivalent` | `pub inline fn equivalent(a: Fe, b: Fe) bool` |
| `fromBytes` | `pub fn fromBytes(s: [32]u8) Fe` |
| `toBytes` | `pub fn toBytes(fe: Fe) [32]u8` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8) Fe` |
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: [32]u8, comptime ignore_extra_bit: bool) NonCanonicalError!void` |
| `add` | `pub inline fn add(a: Fe, b: Fe) Fe` |
| `sub` | `pub inline fn sub(a: Fe, b: Fe) Fe` |
| `neg` | `pub inline fn neg(a: Fe) Fe` |
| `isNegative` | `pub inline fn isNegative(a: Fe) bool` |
| `cMov` | `pub inline fn cMov(fe: *Fe, a: Fe, c: u64) void` |
| `cSwap2` | `pub fn cSwap2(a0: *Fe, b0: *Fe, a1: *Fe, b1: *Fe, c: u64) void` |
| `mul` | `pub inline fn mul(a: Fe, b: Fe) Fe` |
| `sq` | `pub inline fn sq(a: Fe) Fe` |
| `sq2` | `pub inline fn sq2(a: Fe) Fe` |
| `mul32` | `pub inline fn mul32(a: Fe, comptime n: u32) Fe` |
| `invert` | `pub fn invert(a: Fe) Fe` |
| `pow2523` | `pub fn pow2523(a: Fe) Fe` |
| `abs` | `pub fn abs(a: Fe) Fe` |
| `isSquare` | `pub fn isSquare(a: Fe) bool` |
| `sqrt` | `pub fn sqrt(x2: Fe) NotSquareError!Fe` |

## crypto / 25519 / ristretto255

| Function | Signature |
|----------|-----------|
| `rejectIdentity` | `pub inline fn rejectIdentity(p: Ristretto255) IdentityElementError!void` |
| `fromBytes` | `pub fn fromBytes(s: [encoded_length]u8) (NonCanonicalError || EncodingError)!Ristretto255` |
| `toBytes` | `pub fn toBytes(e: Ristretto255) [encoded_length]u8` |
| `fromUniform` | `pub fn fromUniform(h: [64]u8) Ristretto255` |
| `dbl` | `pub inline fn dbl(p: Ristretto255) Ristretto255` |
| `add` | `pub inline fn add(p: Ristretto255, q: Ristretto255) Ristretto255` |
| `mul` | `pub inline fn mul(p: Ristretto255, s: [encoded_length]u8) (IdentityElementError || WeakPublicKeyError)!Ristretto255` |
| `equivalent` | `pub fn equivalent(p: Ristretto255, q: Ristretto255) bool` |

## crypto / 25519 / scalar

| Function | Signature |
|----------|-----------|
| `rejectNonCanonical` | `pub fn rejectNonCanonical(s: CompressedScalar) NonCanonicalError!void` |
| `reduce` | `pub fn reduce(s: CompressedScalar) CompressedScalar` |
| `reduce64` | `pub fn reduce64(s: [64]u8) CompressedScalar` |
| `clamp` | `pub inline fn clamp(s: *CompressedScalar) void` |
| `mul` | `pub fn mul(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `mulAdd` | `pub fn mulAdd(a: CompressedScalar, b: CompressedScalar, c: CompressedScalar) CompressedScalar` |
| `mul8` | `pub fn mul8(s: CompressedScalar) CompressedScalar` |
| `add` | `pub fn add(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `neg` | `pub fn neg(s: CompressedScalar) CompressedScalar` |
| `sub` | `pub fn sub(a: CompressedScalar, b: CompressedScalar) CompressedScalar` |
| `random` | `pub fn random() CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(bytes: CompressedScalar) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(bytes: [64]u8) Scalar` |
| `toBytes` | `pub fn toBytes(expanded: *const Scalar) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(x: Scalar) Scalar` |
| `invert` | `pub fn invert(x: Scalar) Scalar` |
| `random` | `pub fn random() Scalar` |

## crypto / 25519 / x25519

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create(seed: ?[seed_length]u8) IdentityElementError!KeyPair` |
| `fromEd25519` | `pub fn fromEd25519(ed25519_key_pair: crypto.sign.Ed25519.KeyPair) (IdentityElementError || EncodingError)!KeyPair` |
| `recoverPublicKey` | `pub fn recoverPublicKey(secret_key: [secret_length]u8) IdentityElementError![public_length]u8` |
| `publicKeyFromEd25519` | `pub fn publicKeyFromEd25519(ed25519_public_key: crypto.sign.Ed25519.PublicKey) (IdentityElementError || EncodingError)![public_length]u8` |
| `scalarmult` | `pub fn scalarmult(secret_key: [secret_length]u8, public_key: [public_length]u8) IdentityElementError![shared_length]u8` |

## crypto / aegis

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / aes / aesni

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub inline fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub inline fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub inline fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub inline fn encrypt(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub inline fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub inline fn decrypt(block: Block, inv_round_key: Block) Block` |
| `decryptLast` | `pub inline fn decryptLast(block: Block, inv_round_key: Block) Block` |
| `xorBlocks` | `pub inline fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub inline fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub inline fn orBlocks(block1: Block, block2: Block) Block` |
| `encryptParallel` | `pub inline fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub inline fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub inline fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub inline fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub inline fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub inline fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes)) Self` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / aes / armcrypto

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub inline fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub inline fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub inline fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub inline fn encrypt(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub inline fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub inline fn decrypt(block: Block, inv_round_key: Block) Block` |
| `decryptLast` | `pub inline fn decryptLast(block: Block, inv_round_key: Block) Block` |
| `xorBlocks` | `pub inline fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub inline fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub inline fn orBlocks(block1: Block, block2: Block) Block` |
| `encryptParallel` | `pub inline fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub inline fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub inline fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub inline fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub inline fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub inline fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes)) Self` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / aes / soft

| Function | Signature |
|----------|-----------|
| `fromBytes` | `pub inline fn fromBytes(bytes: *const [16]u8) Block` |
| `toBytes` | `pub inline fn toBytes(block: Block) [16]u8` |
| `xorBytes` | `pub inline fn xorBytes(block: Block, bytes: *const [16]u8) [16]u8` |
| `encrypt` | `pub inline fn encrypt(block: Block, round_key: Block) Block` |
| `encryptLast` | `pub inline fn encryptLast(block: Block, round_key: Block) Block` |
| `decrypt` | `pub inline fn decrypt(block: Block, round_key: Block) Block` |
| `decryptLast` | `pub inline fn decryptLast(block: Block, round_key: Block) Block` |
| `xorBlocks` | `pub inline fn xorBlocks(block1: Block, block2: Block) Block` |
| `andBlocks` | `pub inline fn andBlocks(block1: Block, block2: Block) Block` |
| `orBlocks` | `pub inline fn orBlocks(block1: Block, block2: Block) Block` |
| `encryptParallel` | `pub fn encryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `decryptParallel` | `pub fn decryptParallel(comptime count: usize, blocks: [count]Block, round_keys: [count]Block) [count]Block` |
| `encryptWide` | `pub fn encryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptWide` | `pub fn decryptWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `encryptLastWide` | `pub fn encryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `decryptLastWide` | `pub fn decryptLastWide(comptime count: usize, blocks: [count]Block, round_key: Block) [count]Block` |
| `invert` | `pub fn invert(key_schedule: Self) Self` |
| `AesEncryptCtx` | `pub fn AesEncryptCtx(comptime Aes: type) type` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `encrypt` | `pub fn encrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `xor` | `pub fn xor(ctx: Self, dst: *[16]u8, src: *const [16]u8, counter: [16]u8) void` |
| `encryptWide` | `pub fn encryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `xorWide` | `pub fn xorWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8, counters: [16 * count]u8) void` |
| `AesDecryptCtx` | `pub fn AesDecryptCtx(comptime Aes: type) type` |
| `initFromEnc` | `pub fn initFromEnc(ctx: AesEncryptCtx(Aes)) Self` |
| `init` | `pub fn init(key: [Aes.key_bits / 8]u8) Self` |
| `decrypt` | `pub fn decrypt(ctx: Self, dst: *[16]u8, src: *const [16]u8) void` |
| `decryptWide` | `pub fn decryptWide(ctx: Self, comptime count: usize, dst: *[16 * count]u8, src: *const [16 * count]u8) void` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes128)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes128)` |
| `initEnc` | `pub fn initEnc(key: [key_bits / 8]u8) AesEncryptCtx(Aes256)` |
| `initDec` | `pub fn initDec(key: [key_bits / 8]u8) AesDecryptCtx(Aes256)` |

## crypto / aes_gcm

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / aes_ocb

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / argon2

| Function | Signature |
|----------|-----------|
| `fromLimits` | `pub fn fromLimits(ops_limit: u32, mem_limit: usize) Self` |
| `kdf` | `pub fn kdf( allocator: mem.Allocator, derived_key: []u8, password: []const u8, salt: []const u8, params: Params, mode: Mode, ) KdfError!void` |
| `create` | `pub fn create( allocator: mem.Allocator, password: []const u8, params: Params, mode: Mode, buf: []u8, ) HasherError![]const u8` |
| `verify` | `pub fn verify( allocator: mem.Allocator, str: []const u8, password: []const u8, ) HasherError!void` |
| `strHash` | `pub fn strHash( password: []const u8, options: HashOptions, out: []u8, ) Error![]const u8` |
| `strVerify` | `pub fn strVerify( str: []const u8, password: []const u8, options: VerifyOptions, ) Error!void` |

## crypto / bcrypt

| Function | Signature |
|----------|-----------|
| `bcrypt` | `pub fn bcrypt( password: []const u8, salt: [salt_length]u8, params: Params, ) [dk_length]u8` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: []const u8) void` |
| `init` | `pub fn init(key: []const u8) Self` |
| `update` | `pub fn update(self: *Self, msg: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |
| `pbkdf` | `pub fn pbkdf(pass: []const u8, salt: []const u8, key: []u8, rounds: u32) !void` |
| `create` | `pub fn create( password: []const u8, params: Params, buf: []u8, ) HasherError![]const u8` |
| `verify` | `pub fn verify( str: []const u8, password: []const u8, ) HasherError!void` |
| `create` | `pub fn create( password: []const u8, params: Params, buf: []u8, ) HasherError![]const u8` |
| `verify` | `pub fn verify( str: []const u8, password: []const u8, ) HasherError!void` |
| `strHash` | `pub fn strHash( password: []const u8, options: HashOptions, out: []u8, ) Error![]const u8` |
| `strVerify` | `pub fn strVerify( str: []const u8, password: []const u8, _: VerifyOptions, ) Error!void` |

## crypto / benchmark

| Function | Signature |
|----------|-----------|
| `benchmarkHash` | `pub fn benchmarkHash(comptime Hash: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkMac` | `pub fn benchmarkMac(comptime Mac: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkKeyExchange` | `pub fn benchmarkKeyExchange(comptime DhKeyExchange: anytype, comptime exchange_count: comptime_int) !u64` |
| `benchmarkSignature` | `pub fn benchmarkSignature(comptime Signature: anytype, comptime signatures_count: comptime_int) !u64` |
| `benchmarkSignatureVerification` | `pub fn benchmarkSignatureVerification(comptime Signature: anytype, comptime signatures_count: comptime_int) !u64` |
| `benchmarkBatchSignatureVerification` | `pub fn benchmarkBatchSignatureVerification(comptime Signature: anytype, comptime signatures_count: comptime_int) !u64` |
| `benchmarkAead` | `pub fn benchmarkAead(comptime Aead: anytype, comptime bytes: comptime_int) !u64` |
| `benchmarkAes` | `pub fn benchmarkAes(comptime Aes: anytype, comptime count: comptime_int) !u64` |
| `benchmarkAes8` | `pub fn benchmarkAes8(comptime Aes: anytype, comptime count: comptime_int) !u64` |
| `main` | `pub fn main() !void` |

## crypto / blake2

| Function | Signature |
|----------|-----------|
| `Blake2s` | `pub fn Blake2s(comptime out_bits: usize) type` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `Blake2b` | `pub fn Blake2b(comptime out_bits: usize) type` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |

## crypto / blake3

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Blake3` |
| `initKdf` | `pub fn initKdf(context: []const u8, options: KdfOptions) Blake3` |
| `hash` | `pub fn hash(b: []const u8, out: []u8, options: Options) void` |
| `update` | `pub fn update(self: *Blake3, input_slice: []const u8) void` |
| `final` | `pub fn final(self: *const Blake3, out_slice: []u8) void` |
| `writer` | `pub fn writer(self: *Blake3) Writer` |

## crypto / chacha20

| Function | Signature |
|----------|-----------|
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u32, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u64, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u32, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |

## crypto / ecdsa

| Function | Signature |
|----------|-----------|
| `Ecdsa` | `pub fn Ecdsa(comptime Curve: type, comptime Hash: type) type` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) !SecretKey` |
| `toBytes` | `pub fn toBytes(sk: SecretKey) [encoded_length]u8` |
| `fromSec1` | `pub fn fromSec1(sec1: []const u8) !PublicKey` |
| `toCompressedSec1` | `pub fn toCompressedSec1(pk: PublicKey) [compressed_sec1_encoded_length]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(pk: PublicKey) [uncompressed_sec1_encoded_length]u8` |
| `verifier` | `pub fn verifier(self: Signature, public_key: PublicKey) (NonCanonicalError || EncodingError || IdentityElementError)!Verifier` |
| `verify` | `pub fn verify(self: Signature, msg: []const u8, public_key: PublicKey) (IdentityElementError || NonCanonicalError || SignatureVerificationError)!void` |
| `toBytes` | `pub fn toBytes(self: Signature) [encoded_length]u8` |
| `fromBytes` | `pub fn fromBytes(bytes: [encoded_length]u8) Signature` |
| `toDer` | `pub fn toDer(self: Signature, buf: *[der_encoded_max_length]u8) []u8` |
| `fromDer` | `pub fn fromDer(der: []const u8) EncodingError!Signature` |
| `update` | `pub fn update(self: *Signer, data: []const u8) void` |
| `finalize` | `pub fn finalize(self: *Signer) (IdentityElementError || NonCanonicalError)!Signature` |
| `update` | `pub fn update(self: *Verifier, data: []const u8) void` |
| `verify` | `pub fn verify(self: *Verifier) (IdentityElementError || SignatureVerificationError)!void` |
| `create` | `pub fn create(seed: ?[seed_length]u8) IdentityElementError!KeyPair` |
| `fromSecretKey` | `pub fn fromSecretKey(secret_key: SecretKey) IdentityElementError!KeyPair` |
| `sign` | `pub fn sign(key_pair: KeyPair, msg: []const u8, noise: ?[noise_length]u8) (IdentityElementError || NonCanonicalError)!Signature` |
| `signer` | `pub fn signer(key_pair: KeyPair, noise: ?[noise_length]u8) !Signer` |

## crypto / ghash

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(key: *const [key_length]u8) Ghash` |
| `update` | `pub fn update(st: *Ghash, m: []const u8) void` |
| `pad` | `pub fn pad(st: *Ghash) void` |
| `final` | `pub fn final(st: *Ghash, out: *[mac_length]u8) void` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |

## crypto / gimli

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(initial_state: [State.BLOCKBYTES]u8) Self` |
| `toSlice` | `pub fn toSlice(self: *Self) *[BLOCKBYTES]u8` |
| `toSliceConst` | `pub fn toSliceConst(self: *const Self) *const [BLOCKBYTES]u8` |
| `squeeze` | `pub fn squeeze(self: *Self, out: []u8) void` |
| `init` | `pub fn init(options: Options) Self` |
| `update` | `pub fn update(self: *Self, data: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: []u8) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `hash` | `pub fn hash(out: []u8, in: []const u8, options: Hash.Options) void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |

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
| `extract` | `pub fn extract(salt: []const u8, ikm: []const u8) [Hmac.mac_length]u8` |
| `expand` | `pub fn expand(out: []u8, ctx: []const u8, prk: [Hmac.mac_length]u8) void` |

## crypto / hmac

| Function | Signature |
|----------|-----------|
| `Hmac` | `pub fn Hmac(comptime Hash: type) type` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: []const u8) void` |
| `init` | `pub fn init(key: []const u8) Self` |
| `update` | `pub fn update(ctx: *Self, msg: []const u8) void` |
| `final` | `pub fn final(ctx: *Self, out: *[mac_length]u8) void` |

## crypto / isap

| Function | Signature |
|----------|-----------|
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, key: [key_length]u8) AuthenticationError!void` |

## crypto / md5

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |

## crypto / modes

| Function | Signature |
|----------|-----------|
| `ctr` | `pub fn ctr(comptime BlockCipher: anytype, block_cipher: BlockCipher, dst: []u8, src: []const u8, iv: [BlockCipher.block_length]u8, endian: std.builtin.Endian) void` |

## crypto / pbkdf2

| Function | Signature |
|----------|-----------|
| `pbkdf2` | `pub fn pbkdf2(dk: []u8, password: []const u8, salt: []const u8, rounds: u32, comptime Prf: type) (WeakParametersError || OutputTooLongError)!void` |

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
| `random` | `pub fn random() P256` |
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
| `random` | `pub fn random(endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes48` | `pub fn fromBytes48(s: [48]u8, endian: std.builtin.Endian) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) Scalar` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random() Scalar` |

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
| `random` | `pub fn random() P384` |
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
| `random` | `pub fn random(endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) Scalar` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random() Scalar` |

## crypto / pcurves / secp256k1

| Function | Signature |
|----------|-----------|
| `splitScalar` | `pub fn splitScalar(s: [32]u8, endian: std.builtin.Endian) SplitScalar` |
| `rejectIdentity` | `pub fn rejectIdentity(p: Secp256k1) IdentityElementError!void` |
| `fromAffineCoordinates` | `pub fn fromAffineCoordinates(p: AffineCoordinates) EncodingError!Secp256k1` |
| `fromSerializedAffineCoordinates` | `pub fn fromSerializedAffineCoordinates(xs: [32]u8, ys: [32]u8, endian: std.builtin.Endian) (NonCanonicalError || EncodingError)!Secp256k1` |
| `recoverY` | `pub fn recoverY(x: Fe, is_odd: bool) NotSquareError!Fe` |
| `fromSec1` | `pub fn fromSec1(s: []const u8) (EncodingError || NotSquareError || NonCanonicalError)!Secp256k1` |
| `toCompressedSec1` | `pub fn toCompressedSec1(p: Secp256k1) [33]u8` |
| `toUncompressedSec1` | `pub fn toUncompressedSec1(p: Secp256k1) [65]u8` |
| `random` | `pub fn random() Secp256k1` |
| `neg` | `pub fn neg(p: Secp256k1) Secp256k1` |
| `dbl` | `pub fn dbl(p: Secp256k1) Secp256k1` |
| `addMixed` | `pub fn addMixed(p: Secp256k1, q: AffineCoordinates) Secp256k1` |
| `add` | `pub fn add(p: Secp256k1, q: Secp256k1) Secp256k1` |
| `sub` | `pub fn sub(p: Secp256k1, q: Secp256k1) Secp256k1` |
| `subMixed` | `pub fn subMixed(p: Secp256k1, q: AffineCoordinates) Secp256k1` |
| `affineCoordinates` | `pub fn affineCoordinates(p: Secp256k1) AffineCoordinates` |
| `equivalent` | `pub fn equivalent(a: Secp256k1, b: Secp256k1) bool` |
| `mul` | `pub fn mul(p: Secp256k1, s_: [32]u8, endian: std.builtin.Endian) IdentityElementError!Secp256k1` |
| `mulPublic` | `pub fn mulPublic(p: Secp256k1, s_: [32]u8, endian: std.builtin.Endian) IdentityElementError!Secp256k1` |
| `mulDoubleBasePublic` | `pub fn mulDoubleBasePublic(p1: Secp256k1, s1_: [32]u8, p2: Secp256k1, s2_: [32]u8, endian: std.builtin.Endian) IdentityElementError!Secp256k1` |

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
| `random` | `pub fn random(endian: std.builtin.Endian) CompressedScalar` |
| `fromBytes` | `pub fn fromBytes(s: CompressedScalar, endian: std.builtin.Endian) NonCanonicalError!Scalar` |
| `fromBytes48` | `pub fn fromBytes48(s: [48]u8, endian: std.builtin.Endian) Scalar` |
| `fromBytes64` | `pub fn fromBytes64(s: [64]u8, endian: std.builtin.Endian) Scalar` |
| `toBytes` | `pub fn toBytes(n: Scalar, endian: std.builtin.Endian) CompressedScalar` |
| `isZero` | `pub fn isZero(n: Scalar) bool` |
| `equivalent` | `pub fn equivalent(a: Scalar, b: Scalar) bool` |
| `add` | `pub fn add(x: Scalar, y: Scalar) Scalar` |
| `sub` | `pub fn sub(x: Scalar, y: Scalar) Scalar` |
| `dbl` | `pub fn dbl(n: Scalar) Scalar` |
| `mul` | `pub fn mul(x: Scalar, y: Scalar) Scalar` |
| `sq` | `pub fn sq(n: Scalar) Scalar` |
| `pow` | `pub fn pow(a: Scalar, comptime T: type, comptime n: T) Scalar` |
| `neg` | `pub fn neg(n: Scalar) Scalar` |
| `invert` | `pub fn invert(n: Scalar) Scalar` |
| `isSquare` | `pub fn isSquare(n: Scalar) Scalar` |
| `sqrt` | `pub fn sqrt(n: Scalar) NotSquareError!Scalar` |
| `random` | `pub fn random() Scalar` |

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
| `xor` | `pub fn xor(out: []u8, in: []const u8, counter: u64, key: [key_length]u8, nonce: [nonce_length]u8) void` |
| `encrypt` | `pub fn encrypt(c: []u8, tag: *[tag_length]u8, m: []const u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `decrypt` | `pub fn decrypt(m: []u8, c: []const u8, tag: [tag_length]u8, ad: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `seal` | `pub fn seal(c: []u8, m: []const u8, npub: [nonce_length]u8, k: [key_length]u8) void` |
| `open` | `pub fn open(m: []u8, c: []const u8, npub: [nonce_length]u8, k: [key_length]u8) AuthenticationError!void` |
| `createSharedSecret` | `pub fn createSharedSecret(public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError)![shared_length]u8` |
| `seal` | `pub fn seal(c: []u8, m: []const u8, npub: [nonce_length]u8, public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError)!void` |
| `open` | `pub fn open(m: []u8, c: []const u8, npub: [nonce_length]u8, public_key: [public_length]u8, secret_key: [secret_length]u8) (IdentityElementError || WeakPublicKeyError || AuthenticationError)!void` |
| `seal` | `pub fn seal(c: []u8, m: []const u8, public_key: [public_length]u8) (WeakPublicKeyError || IdentityElementError)!void` |
| `open` | `pub fn open(m: []u8, c: []const u8, keypair: KeyPair) (IdentityElementError || WeakPublicKeyError || AuthenticationError)!void` |

## crypto / scrypt

| Function | Signature |
|----------|-----------|
| `fromLimits` | `pub fn fromLimits(ops_limit: u64, mem_limit: usize) Self` |
| `kdf` | `pub fn kdf( allocator: mem.Allocator, derived_key: []u8, password: []const u8, salt: []const u8, params: Params, ) KdfError!void` |
| `HashResult` | `pub fn HashResult(comptime crypt_max_hash_len: usize) type` |
| `BinValue` | `pub fn BinValue(comptime max_len: usize) type` |
| `fromSlice` | `pub fn fromSlice(slice: []const u8) EncodingError!Self` |
| `constSlice` | `pub fn constSlice(self: *const Self) []const u8` |
| `saltFromBin` | `pub fn saltFromBin(comptime len: usize, salt: [len]u8) [Codec.encodedLen(len)]u8` |
| `deserialize` | `pub fn deserialize(comptime T: type, str: []const u8) EncodingError!T` |
| `serialize` | `pub fn serialize(params: anytype, str: []u8) EncodingError![]const u8` |
| `calcSize` | `pub fn calcSize(params: anytype) usize` |
| `create` | `pub fn create( allocator: mem.Allocator, password: []const u8, params: Params, buf: []u8, ) HasherError![]const u8` |
| `verify` | `pub fn verify( allocator: mem.Allocator, str: []const u8, password: []const u8, ) HasherError!void` |
| `create` | `pub fn create( allocator: mem.Allocator, password: []const u8, params: Params, buf: []u8, ) HasherError![]const u8` |
| `verify` | `pub fn verify( allocator: mem.Allocator, str: []const u8, password: []const u8, ) HasherError!void` |
| `strHash` | `pub fn strHash( password: []const u8, options: HashOptions, out: []u8, ) Error![]const u8` |
| `strVerify` | `pub fn strVerify( str: []const u8, password: []const u8, options: VerifyOptions, ) Error!void` |

## crypto / sha1

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |

## crypto / sha2

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |

## crypto / sha3

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(options: Options) Self` |
| `hash` | `pub fn hash(b: []const u8, out: *[digest_length]u8, options: Options) void` |
| `update` | `pub fn update(d: *Self, b: []const u8) void` |
| `final` | `pub fn final(d: *Self, out: *[digest_length]u8) void` |
| `writer` | `pub fn writer(self: *Self) Writer` |

## crypto / siphash

| Function | Signature |
|----------|-----------|
| `SipHash64` | `pub fn SipHash64(comptime c_rounds: usize, comptime d_rounds: usize) type` |
| `SipHash128` | `pub fn SipHash128(comptime c_rounds: usize, comptime d_rounds: usize) type` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(self: *Self, b: []const u8) void` |
| `final` | `pub fn final(self: *Self, b: []const u8) T` |
| `hash` | `pub fn hash(msg: []const u8, key: *const [key_length]u8) T` |
| `init` | `pub fn init(key: *const [key_length]u8) Self` |
| `update` | `pub fn update(self: *Self, b: []const u8) void` |
| `final` | `pub fn final(self: *Self, out: *[mac_length]u8) void` |
| `create` | `pub fn create(out: *[mac_length]u8, msg: []const u8, key: *const [key_length]u8) void` |
| `finalInt` | `pub fn finalInt(self: *Self) T` |
| `toInt` | `pub fn toInt(msg: []const u8, key: *const [key_length]u8) T` |
| `writer` | `pub fn writer(self: *Self) Writer` |

## crypto / utils

| Function | Signature |
|----------|-----------|
| `timingSafeEql` | `pub fn timingSafeEql(comptime T: type, a: T, b: T) bool` |
| `timingSafeCompare` | `pub fn timingSafeCompare(comptime T: type, a: []const T, b: []const T, endian: Endian) Order` |
| `timingSafeAdd` | `pub fn timingSafeAdd(comptime T: type, a: []const T, b: []const T, result: []T, endian: Endian) bool` |
| `timingSafeSub` | `pub fn timingSafeSub(comptime T: type, a: []const T, b: []const T, result: []T, endian: Endian) bool` |
| `secureZero` | `pub fn secureZero(comptime T: type, s: []T) void` |

## crypto / xoodoo

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(initial_state: [block_bytes]u8) State` |
| `asBytes` | `pub fn asBytes(self: *State) *[block_bytes]u8` |
| `endianSwapPartial` | `pub fn endianSwapPartial(self: *State, from: usize, to: usize) void` |
| `endianSwap` | `pub fn endianSwap(self: *State) void` |
| `addByte` | `pub fn addByte(self: *State, byte: u8, offset: usize) void` |
| `addBytes` | `pub fn addBytes(self: *State, bytes: []const u8) void` |
| `extract` | `pub fn extract(self: *State, out: []u8) void` |
| `clear` | `pub fn clear(self: *State, from: usize, to: usize) void` |
| `permute` | `pub fn permute(self: *State) void` |

## cstr

| Function | Signature |
|----------|-----------|
| `cmp` | `pub fn cmp(a: [*:0]const u8, b: [*:0]const u8) i8` |
| `addNullByte` | `pub fn addNullByte(allocator: mem.Allocator, slice: []const u8) ![:0]u8` |
| `fromSlices` | `pub fn fromSlices(allocator: mem.Allocator, slices: []const []const []const u8) !NullTerminated2DArray` |
| `deinit` | `pub fn deinit(self: *NullTerminated2DArray) void` |

## debug

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: LineInfo, allocator: mem.Allocator) void` |
| `deinit` | `pub fn deinit(self: SymbolInfo, allocator: mem.Allocator) void` |
| `print` | `pub fn print(comptime fmt: []const u8, args: anytype) void` |
| `getStderrMutex` | `pub fn getStderrMutex() *std.Thread.Mutex` |
| `getSelfDebugInfo` | `pub fn getSelfDebugInfo() !*DebugInfo` |
| `detectTTYConfig` | `pub fn detectTTYConfig() TTY.Config` |
| `dumpCurrentStackTrace` | `pub fn dumpCurrentStackTrace(start_addr: ?usize) void` |
| `dumpStackTraceFromBase` | `pub fn dumpStackTraceFromBase(bp: usize, ip: usize) void` |
| `captureStackTrace` | `pub fn captureStackTrace(first_address: ?usize, stack_trace: *std.builtin.StackTrace) void` |
| `dumpStackTrace` | `pub fn dumpStackTrace(stack_trace: std.builtin.StackTrace) void` |
| `assert` | `pub fn assert(ok: bool) void` |
| `panic` | `pub fn panic(comptime format: []const u8, args: anytype) noreturn` |
| `panicExtra` | `pub fn panicExtra( trace: ?*std.builtin.StackTrace, ret_addr: ?usize, comptime format: []const u8, args: anytype, ) noreturn` |
| `panicImpl` | `pub fn panicImpl(trace: ?*const std.builtin.StackTrace, first_trace_addr: ?usize, msg: []const u8) noreturn` |
| `writeStackTrace` | `pub fn writeStackTrace( stack_trace: std.builtin.StackTrace, out_stream: anytype, allocator: mem.Allocator, debug_info: *DebugInfo, tty_config: TTY.Config, ) !void` |
| `init` | `pub fn init(first_address: ?usize, fp: ?usize) StackIterator` |
| `next` | `pub fn next(self: *StackIterator) ?usize` |
| `writeCurrentStackTrace` | `pub fn writeCurrentStackTrace( out_stream: anytype, debug_info: *DebugInfo, tty_config: TTY.Config, start_addr: ?usize, ) !void` |
| `writeCurrentStackTraceWindows` | `pub fn writeCurrentStackTraceWindows( out_stream: anytype, debug_info: *DebugInfo, tty_config: TTY.Config, start_addr: ?usize, ) !void` |
| `setColor` | `pub fn setColor(conf: Config, out_stream: anytype, color: Color) void` |
| `printSourceAtAddress` | `pub fn printSourceAtAddress(debug_info: *DebugInfo, out_stream: anytype, address: usize, tty_config: TTY.Config) !void` |
| `openSelfDebugInfo` | `pub fn openSelfDebugInfo(allocator: mem.Allocator) anyerror!DebugInfo` |
| `readElfDebugInfo` | `pub fn readElfDebugInfo(allocator: mem.Allocator, elf_file: File) !ModuleDebugInfo` |
| `init` | `pub fn init(allocator: mem.Allocator) DebugInfo` |
| `deinit` | `pub fn deinit(self: *DebugInfo) void` |
| `getModuleForAddress` | `pub fn getModuleForAddress(self: *DebugInfo, address: usize) !*ModuleDebugInfo` |
| `getSymbolAtAddress` | `pub fn getSymbolAtAddress(self: *@This(), allocator: mem.Allocator, address: usize) !SymbolInfo` |
| `getSymbolAtAddress` | `pub fn getSymbolAtAddress(self: *@This(), allocator: mem.Allocator, address: usize) !SymbolInfo` |
| `getSymbolAtAddress` | `pub fn getSymbolAtAddress(self: *@This(), allocator: mem.Allocator, address: usize) !SymbolInfo` |
| `getSymbolAtAddress` | `pub fn getSymbolAtAddress(self: *@This(), allocator: mem.Allocator, address: usize) !SymbolInfo` |
| `maybeEnableSegfaultHandler` | `pub fn maybeEnableSegfaultHandler() void` |
| `updateSegfaultHandler` | `pub fn updateSegfaultHandler(act: ?*const os.Sigaction) error` |
| `attachSegfaultHandler` | `pub fn attachSegfaultHandler() void` |
| `dumpStackPointerAddr` | `pub fn dumpStackPointerAddr(prefix: []const u8) void` |
| `ConfigurableTrace` | `pub fn ConfigurableTrace(comptime size: usize, comptime stack_frame_count: usize, comptime is_enabled: bool) type` |
| `addNoOp` | `pub inline fn addNoOp(t: *@This(), note: []const u8) void` |
| `addAddr` | `pub fn addAddr(t: *@This(), addr: usize, note: []const u8) void` |
| `dump` | `pub fn dump(t: @This()) void` |
| `format` | `pub fn format( t: Trace, comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |

## dwarf

| Function | Signature |
|----------|-----------|
| `getAttrString` | `pub fn getAttrString( self: *const Die, di: *DwarfInfo, id: u64, opt_str: ?[]const u8, compile_unit: CompileUnit, ) error` |
| `reset` | `pub fn reset(self: *LineNumberProgram) void` |
| `init` | `pub fn init( is_stmt: bool, include_dirs: []const FileEntry, target_address: u64, version: u16, ) LineNumberProgram` |
| `checkLineMatch` | `pub fn checkLineMatch( self: *LineNumberProgram, allocator: mem.Allocator, file_entries: []const FileEntry, ) !?debug.LineInfo` |
| `deinit` | `pub fn deinit(di: *DwarfInfo, allocator: mem.Allocator) void` |
| `getSymbolName` | `pub fn getSymbolName(di: *DwarfInfo, address: u64) ?[]const u8` |
| `findCompileUnit` | `pub fn findCompileUnit(di: *DwarfInfo, target_address: u64) !*const CompileUnit` |
| `getLineNumberInfo` | `pub fn getLineNumberInfo( di: *DwarfInfo, allocator: mem.Allocator, compile_unit: CompileUnit, target_address: u64, ) !debug.LineInfo` |
| `openDwarfDebugInfo` | `pub fn openDwarfDebugInfo(di: *DwarfInfo, allocator: mem.Allocator) !void` |

## dynamic_library

| Function | Signature |
|----------|-----------|
| `end` | `pub fn end(self: *Iterator) bool` |
| `next` | `pub fn next(self: *Iterator) ?*LinkMap` |
| `get_DYNAMIC` | `pub fn get_DYNAMIC() ?[*]elf.Dyn` |
| `linkmap_iterator` | `pub fn linkmap_iterator(phdrs: []elf.Phdr) !LinkMap.Iterator` |
| `open` | `pub fn open(path: []const u8) !ElfDynLib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8) !ElfDynLib` |
| `close` | `pub fn close(self: *ElfDynLib) void` |
| `lookup` | `pub fn lookup(self: *ElfDynLib, comptime T: type, name: [:0]const u8) ?T` |
| `lookupAddress` | `pub fn lookupAddress(self: *const ElfDynLib, vername: []const u8, name: []const u8) ?usize` |
| `open` | `pub fn open(path: []const u8) !WindowsDynLib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8) !WindowsDynLib` |
| `openW` | `pub fn openW(path_w: [*:0]const u16) !WindowsDynLib` |
| `close` | `pub fn close(self: *WindowsDynLib) void` |
| `lookup` | `pub fn lookup(self: *WindowsDynLib, comptime T: type, name: [:0]const u8) ?T` |
| `open` | `pub fn open(path: []const u8) !DlDynlib` |
| `openZ` | `pub fn openZ(path_c: [*:0]const u8) !DlDynlib` |
| `close` | `pub fn close(self: *DlDynlib) void` |
| `lookup` | `pub fn lookup(self: *DlDynlib, comptime T: type, name: [:0]const u8) ?T` |

## elf

| Function | Signature |
|----------|-----------|
| `program_header_iterator` | `pub fn program_header_iterator(self: Header, parse_source: anytype) ProgramHeaderIterator(@TypeOf(parse_source))` |
| `section_header_iterator` | `pub fn section_header_iterator(self: Header, parse_source: anytype) SectionHeaderIterator(@TypeOf(parse_source))` |
| `read` | `pub fn read(parse_source: anytype) !Header` |
| `parse` | `pub fn parse(hdr_buf: *align(@alignOf(Elf64_Ehdr)) const [@sizeOf(Elf64_Ehdr)]u8) !Header` |
| `ProgramHeaderIterator` | `pub fn ProgramHeaderIterator(comptime ParseSource: anytype) type` |
| `next` | `pub fn next(self: *@This()) !?Elf64_Phdr` |
| `SectionHeaderIterator` | `pub fn SectionHeaderIterator(comptime ParseSource: anytype) type` |
| `next` | `pub fn next(self: *@This()) !?Elf64_Shdr` |
| `int` | `pub fn int(is_64: bool, need_bswap: bool, int_32: anytype, int_64: anytype) @TypeOf(int_64)` |
| `int32` | `pub fn int32(need_bswap: bool, int_32: anytype, comptime Int64: anytype) Int64` |
| `r_sym` | `pub inline fn r_sym(self: @This()) u24` |
| `r_type` | `pub inline fn r_type(self: @This()) u8` |
| `r_sym` | `pub inline fn r_sym(self: @This()) u32` |
| `r_type` | `pub inline fn r_type(self: @This()) u32` |
| `r_sym` | `pub inline fn r_sym(self: @This()) u24` |
| `r_type` | `pub inline fn r_type(self: @This()) u8` |
| `r_sym` | `pub inline fn r_sym(self: @This()) u32` |
| `r_type` | `pub inline fn r_type(self: @This()) u32` |
| `toTargetCpuArch` | `pub fn toTargetCpuArch(em: EM) ?std.Target.Cpu.Arch` |

## enums

| Function | Signature |
|----------|-----------|
| `EnumFieldStruct` | `pub fn EnumFieldStruct(comptime E: type, comptime Data: type, comptime field_default: ?Data) type` |
| `valuesFromFields` | `pub fn valuesFromFields(comptime E: type, comptime fields: []const EnumField) []const E` |
| `values` | `pub fn values(comptime E: type) []const E` |
| `directEnumArrayLen` | `pub fn directEnumArrayLen(comptime E: type, comptime max_unused_slots: comptime_int) comptime_int` |
| `directEnumArray` | `pub fn directEnumArray( comptime E: type, comptime Data: type, comptime max_unused_slots: comptime_int, init_values: EnumFieldStruct(E, Data, null), ) [directEnumArrayLen(E, max_unused_slots)]Data` |
| `directEnumArrayDefault` | `pub fn directEnumArrayDefault( comptime E: type, comptime Data: type, comptime default: ?Data, comptime max_unused_slots: comptime_int, init_values: EnumFieldStruct(E, Data, default), ) [directEnumArrayLen(E, max_unused_slots)]Data` |
| `nameCast` | `pub fn nameCast(comptime E: type, comptime value: anytype) E` |
| `EnumSet` | `pub fn EnumSet(comptime E: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, bool, false)) Self` |
| `EnumMap` | `pub fn EnumMap(comptime E: type, comptime V: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, ?V, @as(?V, null))) Self` |
| `initFull` | `pub fn initFull(value: V) Self` |
| `initFullWith` | `pub fn initFullWith(init_values: EnumFieldStruct(E, V, @as(?V, null))) Self` |
| `initFullWithDefault` | `pub fn initFullWithDefault(comptime default: ?V, init_values: EnumFieldStruct(E, V, default)) Self` |
| `EnumArray` | `pub fn EnumArray(comptime E: type, comptime V: type) type` |
| `init` | `pub fn init(init_values: EnumFieldStruct(E, V, @as(?V, null))) Self` |
| `initDefault` | `pub fn initDefault(comptime default: ?V, init_values: EnumFieldStruct(E, V, default)) Self` |
| `NoExtension` | `pub fn NoExtension(comptime Self: type) type` |
| `IndexedSet` | `pub fn IndexedSet(comptime I: type, comptime Ext: fn (type) type) type` |
| `initFull` | `pub fn initFull() Self` |
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
| `iterator` | `pub fn iterator(self: *Self) Iterator` |
| `next` | `pub fn next(self: *Iterator) ?Key` |
| `IndexedMap` | `pub fn IndexedMap(comptime I: type, comptime V: type, comptime Ext: fn (type) type) type` |
| `count` | `pub fn count(self: Self) usize` |
| `contains` | `pub fn contains(self: Self, key: Key) bool` |
| `get` | `pub fn get(self: Self, key: Key) ?Value` |
| `getAssertContains` | `pub fn getAssertContains(self: Self, key: Key) Value` |
| `getPtr` | `pub fn getPtr(self: *Self, key: Key) ?*Value` |
| `getPtrConst` | `pub fn getPtrConst(self: *const Self, key: Key) ?*const Value` |
| `getPtrAssertContains` | `pub fn getPtrAssertContains(self: *Self, key: Key) *Value` |
| `put` | `pub fn put(self: *Self, key: Key, value: Value) void` |
| `putUninitialized` | `pub fn putUninitialized(self: *Self, key: Key) *Value` |
| `fetchPut` | `pub fn fetchPut(self: *Self, key: Key, value: Value) ?Value` |
| `remove` | `pub fn remove(self: *Self, key: Key) void` |
| `fetchRemove` | `pub fn fetchRemove(self: *Self, key: Key) ?Value` |
| `iterator` | `pub fn iterator(self: *Self) Iterator` |
| `next` | `pub fn next(self: *Iterator) ?Entry` |
| `IndexedArray` | `pub fn IndexedArray(comptime I: type, comptime V: type, comptime Ext: fn (type) type) type` |
| `initUndefined` | `pub fn initUndefined() Self` |
| `initFill` | `pub fn initFill(v: Value) Self` |
| `get` | `pub fn get(self: Self, key: Key) Value` |
| `getPtr` | `pub fn getPtr(self: *Self, key: Key) *Value` |
| `getPtrConst` | `pub fn getPtrConst(self: *const Self, key: Key) *const Value` |
| `set` | `pub fn set(self: *Self, key: Key, value: Value) void` |
| `iterator` | `pub fn iterator(self: *Self) Iterator` |
| `next` | `pub fn next(self: *Iterator) ?Entry` |
| `indexOf` | `pub fn indexOf(Key) usize` |
| `keyForIndex` | `pub fn keyForIndex(usize) Key` |
| `ensureIndexer` | `pub fn ensureIndexer(comptime T: type) void` |
| `indexOf` | `pub fn indexOf(k: Key) usize` |
| `keyForIndex` | `pub fn keyForIndex(index: usize) Key` |
| `EnumIndexer` | `pub fn EnumIndexer(comptime E: type) type` |
| `indexOf` | `pub fn indexOf(e: E) usize` |
| `keyForIndex` | `pub fn keyForIndex(i: usize) E` |
| `indexOf` | `pub fn indexOf(e: E) usize` |
| `keyForIndex` | `pub fn keyForIndex(i: usize) E` |
| `indexOf` | `pub fn indexOf(e: E) usize` |
| `keyForIndex` | `pub fn keyForIndex(i: usize) E` |

## event / batch

| Function | Signature |
|----------|-----------|
| `Batch` | `pub fn Batch( /// The return value for each job. /// If a job slot was re-used due to maxed out concurrency, then its result /// value will be overwritten. The values can be accessed with the `results` field. comptime Result: type, /// How many jobs to run in parallel. comptime max_jobs: comptime_int, /// Controls whether the `add` and `wait` functions will be async functions. comptime async_behavior: enum { /// Observe the value of `std.io.is_async` to decide whether `add` /// and `wait` will be async functions. Asserts that the jobs do not suspend when /// `std.io.mode == .blocking`. This is a generally safe assumption, and the /// usual recommended option for this parameter. auto_async, /// Always uses the `nosuspend` keyword when using `await` on the jobs, /// making `add` and `wait` non-async functions. Asserts that the jobs do not suspend. never_async, /// `add` and `wait` use regular `await` keyword, making them async functions. always_async, }, ) type` |
| `init` | `pub fn init() Self` |
| `add` | `pub fn add(self: *Self, frame: anyframe->Result) void` |
| `wait` | `pub fn wait(self: *Self) CollectedResult` |

## event / channel

| Function | Signature |
|----------|-----------|
| `Channel` | `pub fn Channel(comptime T: type) type` |
| `init` | `pub fn init(self: *SelfChannel, buffer: []T) void` |
| `deinit` | `pub fn deinit(self: *SelfChannel) void` |
| `put` | `pub fn put(self: *SelfChannel, data: T) void` |
| `get` | `pub fn get(self: *SelfChannel) callconv(.Async) T` |
| `getOrNull` | `pub fn getOrNull(self: *SelfChannel) ?T` |

## event / future

| Function | Signature |
|----------|-----------|
| `Future` | `pub fn Future(comptime T: type) type` |
| `init` | `pub fn init() Self` |
| `get` | `pub fn get(self: *Self) callconv(.Async) *T` |
| `getOrNull` | `pub fn getOrNull(self: *Self) ?*T` |
| `start` | `pub fn start(self: *Self) callconv(.Async) ?*T` |
| `resolve` | `pub fn resolve(self: *Self) void` |

## event / group

| Function | Signature |
|----------|-----------|
| `Group` | `pub fn Group(comptime ReturnType: type) type` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `add` | `pub fn add(self: *Self, handle: anyframe->ReturnType) (error` |
| `addNode` | `pub fn addNode(self: *Self, node: *Stack.Node) void` |
| `call` | `pub fn call(self: *Self, comptime func: anytype, args: anytype) error` |
| `wait` | `pub fn wait(self: *Self) callconv(.Async) ReturnType` |

## event / lock

| Function | Signature |
|----------|-----------|
| `initLocked` | `pub fn initLocked() Lock` |
| `acquire` | `pub fn acquire(self: *Lock) Held` |
| `release` | `pub fn release(self: Held) void` |

## event / locked

| Function | Signature |
|----------|-----------|
| `Locked` | `pub fn Locked(comptime T: type) type` |
| `release` | `pub fn release(self: HeldLock) void` |
| `init` | `pub fn init(data: T) Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `acquire` | `pub fn acquire(self: *Self) callconv(.Async) HeldLock` |

## event / loop

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(self: *Loop) !void` |
| `initSingleThreaded` | `pub fn initSingleThreaded(self: *Loop) !void` |
| `initMultiThreaded` | `pub fn initMultiThreaded(self: *Loop) !void` |
| `initThreadPool` | `pub fn initThreadPool(self: *Loop, thread_count: usize) !void` |
| `deinit` | `pub fn deinit(self: *Loop) void` |
| `linuxAddFd` | `pub fn linuxAddFd(self: *Loop, fd: i32, resume_node: *ResumeNode, flags: u32) !void` |
| `linuxModFd` | `pub fn linuxModFd(self: *Loop, fd: i32, op: u32, flags: u32, resume_node: *ResumeNode) !void` |
| `linuxRemoveFd` | `pub fn linuxRemoveFd(self: *Loop, fd: i32) void` |
| `linuxWaitFd` | `pub fn linuxWaitFd(self: *Loop, fd: i32, flags: u32) void` |
| `waitUntilFdReadable` | `pub fn waitUntilFdReadable(self: *Loop, fd: os.fd_t) void` |
| `waitUntilFdWritable` | `pub fn waitUntilFdWritable(self: *Loop, fd: os.fd_t) void` |
| `waitUntilFdWritableOrReadable` | `pub fn waitUntilFdWritableOrReadable(self: *Loop, fd: os.fd_t) void` |
| `bsdWaitKev` | `pub fn bsdWaitKev(self: *Loop, ident: usize, filter: i16, flags: u16) void` |
| `bsdAddKev` | `pub fn bsdAddKev(self: *Loop, resume_node: *ResumeNode.Basic, ident: usize, filter: i16, flags: u16) !void` |
| `bsdRemoveKev` | `pub fn bsdRemoveKev(self: *Loop, ident: usize, filter: i16) void` |
| `onNextTick` | `pub fn onNextTick(self: *Loop, node: *NextTickNode) void` |
| `cancelOnNextTick` | `pub fn cancelOnNextTick(self: *Loop, node: *NextTickNode) void` |
| `run` | `pub fn run(self: *Loop) void` |
| `runDetached` | `pub fn runDetached(self: *Loop, alloc: mem.Allocator, comptime func: anytype, args: anytype) error` |
| `yield` | `pub fn yield(self: *Loop) void` |
| `startCpuBoundOperation` | `pub fn startCpuBoundOperation() void` |
| `beginOneEvent` | `pub fn beginOneEvent(self: *Loop) void` |
| `finishOneEvent` | `pub fn finishOneEvent(self: *Loop) void` |
| `sleep` | `pub fn sleep(self: *Loop, nanoseconds: u64) void` |
| `accept` | `pub fn accept( self: *Loop, /// This argument is a socket that has been created with `socket`, bound to a local address /// with `bind`, and is listening for connections after a `listen`. sockfd: os.socket_t, /// This argument is a pointer to a sockaddr structure. This structure is filled in with the /// address of the peer socket, as known to the communications layer. The exact format of the /// address returned addr is determined by the socket's address family (see `socket` and the /// respective protocol man pages). addr: *os.sockaddr, /// This argument is a value-result argument: the caller must initialize it to contain the /// size (in bytes) of the structure pointed to by addr; on return it will contain the actual size /// of the peer address. /// /// The returned address is truncated if the buffer provided is too small; in this case, `addr_size` /// will return a value greater than was supplied to the call. addr_size: *os.socklen_t, /// The following values can be bitwise ORed in flags to obtain different behavior: /// * `SOCK.CLOEXEC` - Set the close-on-exec (`FD_CLOEXEC`) flag on the new file descriptor. See the /// description of the `O.CLOEXEC` flag in `open` for reasons why this may be useful. flags: u32, ) os.AcceptError!os.socket_t { while (true) { return os.accept(sockfd, addr, addr_size, flags | os.SOCK.NONBLOCK) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(sockfd); continue; }, else => return err, }; } } pub fn connect(self: *Loop, sockfd: os.socket_t, sock_addr: *const os.sockaddr, len: os.socklen_t) os.ConnectError!void { os.connect(sockfd, sock_addr, len) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(sockfd); return os.getsockoptError(sockfd); }, else => return err, }; } /// Performs an async `os.open` using a separate thread. pub fn openZ(self: *Loop, file_path: [*:0]const u8, flags: u32, mode: os.mode_t) os.OpenError!os.fd_t { var req_node = Request.Node{ .data = .{ .msg = .{ .open = .{ .path = file_path, .flags = flags, .mode = mode, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.open.result; } /// Performs an async `os.opent` using a separate thread. pub fn openatZ(self: *Loop, fd: os.fd_t, file_path: [*:0]const u8, flags: u32, mode: os.mode_t) os.OpenError!os.fd_t { var req_node = Request.Node{ .data = .{ .msg = .{ .openat = .{ .fd = fd, .path = file_path, .flags = flags, .mode = mode, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.openat.result; } /// Performs an async `os.close` using a separate thread. pub fn close(self: *Loop, fd: os.fd_t) void { var req_node = Request.Node{ .data = .{ .msg = .{ .close = .{ .fd = fd } }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } } /// Performs an async `os.read` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn read(self: *Loop, fd: os.fd_t, buf: []u8, simulate_evented: bool) os.ReadError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .read = .{ .fd = fd, .buf = buf, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.read.result; } else { while (true) { return os.read(fd, buf) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.readv` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn readv(self: *Loop, fd: os.fd_t, iov: []const os.iovec, simulate_evented: bool) os.ReadError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .readv = .{ .fd = fd, .iov = iov, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.readv.result; } else { while (true) { return os.readv(fd, iov) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.pread` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn pread(self: *Loop, fd: os.fd_t, buf: []u8, offset: u64, simulate_evented: bool) os.PReadError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .pread = .{ .fd = fd, .buf = buf, .offset = offset, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.pread.result; } else { while (true) { return os.pread(fd, buf, offset) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.preadv` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn preadv(self: *Loop, fd: os.fd_t, iov: []const os.iovec, offset: u64, simulate_evented: bool) os.ReadError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .preadv = .{ .fd = fd, .iov = iov, .offset = offset, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.preadv.result; } else { while (true) { return os.preadv(fd, iov, offset) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.write` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn write(self: *Loop, fd: os.fd_t, bytes: []const u8, simulate_evented: bool) os.WriteError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .write = .{ .fd = fd, .bytes = bytes, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.write.result; } else { while (true) { return os.write(fd, bytes) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.writev` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn writev(self: *Loop, fd: os.fd_t, iov: []const os.iovec_const, simulate_evented: bool) os.WriteError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .writev = .{ .fd = fd, .iov = iov, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.writev.result; } else { while (true) { return os.writev(fd, iov) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.pwrite` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn pwrite(self: *Loop, fd: os.fd_t, bytes: []const u8, offset: u64, simulate_evented: bool) os.PerformsWriteError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .pwrite = .{ .fd = fd, .bytes = bytes, .offset = offset, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.pwrite.result; } else { while (true) { return os.pwrite(fd, bytes, offset) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(fd); continue; }, else => return err, }; } } } /// Performs an async `os.pwritev` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn pwritev(self: *Loop, fd: os.fd_t, iov: []const os.iovec_const, offset: u64, simulate_evented: bool) os.PWriteError!usize { if (simulate_evented) { var req_node = Request.Node{ .data = .{ .msg = .{ .pwritev = .{ .fd = fd, .iov = iov, .offset = offset, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.pwritev.result; } else { while (true) { return os.pwritev(fd, iov, offset) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(fd); continue; }, else => return err, }; } } } pub fn sendto( self: *Loop, /// The file descriptor of the sending socket. sockfd: os.fd_t, /// Message to send. buf: []const u8, flags: u32, dest_addr: ?*const os.sockaddr, addrlen: os.socklen_t, ) os.SendToError!usize { while (true) { return os.sendto(sockfd, buf, flags, dest_addr, addrlen) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdWritable(sockfd); continue; }, else => return err, }; } } pub fn recvfrom( self: *Loop, sockfd: os.fd_t, buf: []u8, flags: u32, src_addr: ?*os.sockaddr, addrlen: ?*os.socklen_t, ) os.RecvFromError!usize { while (true) { return os.recvfrom(sockfd, buf, flags, src_addr, addrlen) catch |err| switch (err) { error.WouldBlock => { self.waitUntilFdReadable(sockfd); continue; }, else => return err, }; } } /// Performs an async `os.faccessatZ` using a separate thread. /// `fd` must block and not return EAGAIN. pub fn faccessatZ( self: *Loop, dirfd: os.fd_t, path_z: [*:0]const u8, mode: u32, flags: u32, ) os.AccessError!void { var req_node = Request.Node{ .data = .{ .msg = .{ .faccessat = .{ .dirfd = dirfd, .path = path_z, .mode = mode, .flags = flags, .result = undefined, }, }, .finish = .{ .TickNode = .{ .data = @frame() } }, }, }; suspend { self.posixFsRequest(&req_node); } return req_node.data.msg.faccessat.result; } fn workerRun(self: *Loop) void { while (true) { while (true) { const next_tick_node = self.next_tick_queue.get() orelse break; self.dispatch(); resume next_tick_node.data; self.finishOneEvent(); } switch (builtin.os.tag) { .linux => { // only process 1 event so we don't steal from other threads var events: [1]os.linux.epoll_event = undefined; const count = os.epoll_wait(self.os_data.epollfd, events[0..], -1); for (events[0..count]) |ev| { const resume_node = @intToPtr(*ResumeNode, ev.data.ptr); const handle = resume_node.handle; const resume_node_id = resume_node.id; switch (resume_node_id) { .Basic => {}, .Stop => return, .EventFd => { const event_fd_node = @fieldParentPtr(ResumeNode.EventFd, "base", resume_node); event_fd_node.epoll_op = os.linux.EPOLL.CTL_MOD; const stack_node = @fieldParentPtr(std.atomic.Stack(ResumeNode.EventFd).Node, "data", event_fd_node); self.available_eventfd_resume_nodes.push(stack_node); }, } resume handle; if (resume_node_id == ResumeNode.Id.EventFd) { self.finishOneEvent(); } } }, .macos, .ios, .tvos, .watchos, .freebsd, .netbsd, .dragonfly, .openbsd => { var eventlist: [1]os.Kevent = undefined; const empty_kevs = &[0]os.Kevent{}; const count = os.kevent(self.os_data.kqfd, empty_kevs, eventlist[0..], null) catch unreachable; for (eventlist[0..count]) |ev| { const resume_node = @intToPtr(*ResumeNode, ev.udata); const handle = resume_node.handle; const resume_node_id = resume_node.id; switch (resume_node_id) { .Basic => { const basic_node = @fieldParentPtr(ResumeNode.Basic, "base", resume_node); basic_node.kev = ev; }, .Stop => return, .EventFd => { const event_fd_node = @fieldParentPtr(ResumeNode.EventFd, "base", resume_node); const stack_node = @fieldParentPtr(std.atomic.Stack(ResumeNode.EventFd).Node, "data", event_fd_node); self.available_eventfd_resume_nodes.push(stack_node); }, } resume handle; if (resume_node_id == ResumeNode.Id.EventFd) { self.finishOneEvent(); } } }, .windows => { var completion_key: usize = undefined; const overlapped = while (true) { var nbytes: windows.DWORD = undefined; var overlapped: ?*windows.OVERLAPPED = undefined; switch (windows.GetQueuedCompletionStatus(self.os_data.io_port, &nbytes, &completion_key, &overlapped, windows.INFINITE)) { .Aborted => return, .Normal => {}, .EOF => {}, .Cancelled => continue, } if (overlapped) |o| break o; } else unreachable; // TODO else unreachable should not be necessary const resume_node = @fieldParentPtr(ResumeNode, "overlapped", overlapped); const handle = resume_node.handle; const resume_node_id = resume_node.id; switch (resume_node_id) { .Basic => {}, .Stop => return, .EventFd => { const event_fd_node = @fieldParentPtr(ResumeNode.EventFd, "base", resume_node); const stack_node = @fieldParentPtr(std.atomic.Stack(ResumeNode.EventFd).Node, "data", event_fd_node); self.available_eventfd_resume_nodes.push(stack_node); }, } resume handle; self.finishOneEvent(); }, else => @compileError("unsupported OS"), } } } fn posixFsRequest(self: *Loop, request_node: *Request.Node) void { self.beginOneEvent(); // finished in posixFsRun after processing the msg self.fs_queue.put(request_node); self.fs_thread_wakeup.set(); } fn posixFsCancel(self: *Loop, request_node: *Request.Node) void { if (self.fs_queue.remove(request_node)) { self.finishOneEvent(); } } fn posixFsRun(self: *Loop) void { nosuspend while (true) { self.fs_thread_wakeup.reset(); while (self.fs_queue.get()) |node| { switch (node.data.msg) { .end => return, .read => |*msg| { msg.result = os.read(msg.fd, msg.buf); }, .readv => |*msg| { msg.result = os.readv(msg.fd, msg.iov); }, .write => |*msg| { msg.result = os.write(msg.fd, msg.bytes); }, .writev => |*msg| { msg.result = os.writev(msg.fd, msg.iov); }, .pwrite => |*msg| { msg.result = os.pwrite(msg.fd, msg.bytes, msg.offset); }, .pwritev => |*msg| { msg.result = os.pwritev(msg.fd, msg.iov, msg.offset); }, .pread => |*msg| { msg.result = os.pread(msg.fd, msg.buf, msg.offset); }, .preadv => |*msg| { msg.result = os.preadv(msg.fd, msg.iov, msg.offset); }, .open => |*msg| { if (is_windows) unreachable; // TODO msg.result = os.openZ(msg.path, msg.flags, msg.mode); }, .openat => |*msg| { if (is_windows) unreachable; // TODO msg.result = os.openatZ(msg.fd, msg.path, msg.flags, msg.mode); }, .faccessat => |*msg| { msg.result = os.faccessatZ(msg.dirfd, msg.path, msg.mode, msg.flags); }, .close => |*msg| os.close(msg.fd), } switch (node.data.finish) { .TickNode => |*tick_node| self.onNextTick(tick_node), .NoAction => {}, } self.finishOneEvent(); } self.fs_thread_wakeup.wait(); }; } const OsData = switch (builtin.os.tag) { .linux => LinuxOsData, .macos, .ios, .tvos, .watchos, .freebsd, .netbsd, .dragonfly, .openbsd => KEventData, .windows => struct { io_port: windows.HANDLE, extra_thread_count: usize, }, else => struct {}, }; const KEventData = struct { kqfd: i32, final_kevent: os.Kevent, }; const LinuxOsData = struct { epollfd: i32, final_eventfd: i32, final_eventfd_event: os.linux.epoll_event, }; pub const Request = struct { msg: Msg, finish: Finish, pub const Node = std.atomic.Queue(Request).Node; pub const Finish = union(enum) { TickNode: Loop.NextTickNode, NoAction, }; pub const Msg = union(enum) { read: Read, readv: ReadV, write: Write, writev: WriteV, pwrite: PWrite, pwritev: PWriteV, pread: PRead, preadv: PReadV, open: Open, openat: OpenAt, close: Close, faccessat: FAccessAt, /// special - means the fs thread should exit end, pub const Read = struct { fd: os.fd_t, buf: []u8, result: Error!usize, pub const Error = os.ReadError; }; pub const ReadV = struct { fd: os.fd_t, iov: []const os.iovec, result: Error!usize, pub const Error = os.ReadError; }; pub const Write = struct { fd: os.fd_t, bytes: []const u8, result: Error!usize, pub const Error = os.WriteError; }; pub const WriteV = struct { fd: os.fd_t, iov: []const os.iovec_const, result: Error!usize, pub const Error = os.WriteError; }; pub const PWrite = struct { fd: os.fd_t, bytes: []const u8, offset: usize, result: Error!usize, pub const Error = os.PWriteError; }; pub const PWriteV = struct { fd: os.fd_t, iov: []const os.iovec_const, offset: usize, result: Error!usize, pub const Error = os.PWriteError; }; pub const PRead = struct { fd: os.fd_t, buf: []u8, offset: usize, result: Error!usize, pub const Error = os.PReadError; }; pub const PReadV = struct { fd: os.fd_t, iov: []const os.iovec, offset: usize, result: Error!usize, pub const Error = os.PReadError; }; pub const Open = struct { path: [*:0]const u8, flags: u32, mode: os.mode_t, result: Error!os.fd_t, pub const Error = os.OpenError; }; pub const OpenAt = struct { fd: os.fd_t, path: [*:0]const u8, flags: u32, mode: os.mode_t, result: Error!os.fd_t, pub const Error = os.OpenError; }; pub const Close = struct { fd: os.fd_t, }; pub const FAccessAt = struct { dirfd: os.fd_t, path: [*:0]const u8, mode: u32, flags: u32, result: Error!void, pub const Error = os.AccessError; }; }; }; }; test "std.event.Loop - basic" { // https://github.com/ziglang/zig/issues/1908 if (builtin.single_threaded) return error.SkipZigTest; if (true) { // https://github.com/ziglang/zig/issues/4922 return error.SkipZigTest; } var loop: Loop = undefined; try loop.initMultiThreaded(); defer loop.deinit(); loop.run(); } fn testEventLoop() i32 { return 1234; } fn testEventLoop2(h: anyframe->i32, did_it: *bool) void { const value = await h; try testing.expect(value == 1234); did_it.* = true; } var testRunDetachedData: usize = 0; test "std.event.Loop - runDetached" { // https://github.com/ziglang/zig/issues/1908 if (builtin.single_threaded) return error.SkipZigTest; if (!std.io.is_async) return error.SkipZigTest; if (true) { // https://github.com/ziglang/zig/issues/4922 return error.SkipZigTest; } var loop: Loop = undefined; try loop.initMultiThreaded(); defer loop.deinit(); // Schedule the execution, won't actually start until we start the // event loop. try loop.runDetached(std.testing.allocator, testRunDetached, .{}); // Now we can start the event loop. The function will return only // after all tasks have been completed, allowing us to synchonize // with the previous runDetached. loop.run(); try testing.expect(testRunDetachedData == 1); } fn testRunDetached() void { testRunDetachedData += 1; } test "std.event.Loop - sleep" { // https://github.com/ziglang/zig/issues/1908 if (builtin.single_threaded) return error.SkipZigTest; if (!std.io.is_async) return error.SkipZigTest; const frames = try testing.allocator.alloc(@Frame(testSleep), 10); defer testing.allocator.free(frames); const wait_time = 100 * std.time.ns_per_ms; var sleep_count: usize = 0; for (frames) |*frame| frame.* = async testSleep(wait_time, &sleep_count); for (frames) |*frame| await frame; try testing.expect(sleep_count == frames.len); } fn testSleep(wait_ns: u64, sleep_count: *usize) void { Loop.instance.?.sleep(wait_ns); _ = @atomicRmw(usize, sleep_count, .Add, 1, .SeqCst); }` |

## event / rwlock

| Function | Signature |
|----------|-----------|
| `release` | `pub fn release(self: HeldRead) void` |
| `release` | `pub fn release(self: HeldWrite) void` |
| `init` | `pub fn init() RwLock` |
| `deinit` | `pub fn deinit(self: *RwLock) void` |
| `acquireRead` | `pub fn acquireRead(self: *RwLock) callconv(.Async) HeldRead` |
| `acquireWrite` | `pub fn acquireWrite(self: *RwLock) callconv(.Async) HeldWrite` |

## event / rwlocked

| Function | Signature |
|----------|-----------|
| `RwLocked` | `pub fn RwLocked(comptime T: type) type` |
| `release` | `pub fn release(self: HeldReadLock) void` |
| `release` | `pub fn release(self: HeldWriteLock) void` |
| `init` | `pub fn init(data: T) Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `acquireRead` | `pub fn acquireRead(self: *Self) callconv(.Async) HeldReadLock` |
| `acquireWrite` | `pub fn acquireWrite(self: *Self) callconv(.Async) HeldWriteLock` |

## event / wait_group

| Function | Signature |
|----------|-----------|
| `WaitGroupGeneric` | `pub fn WaitGroupGeneric(comptime counter_size: u16) type` |
| `begin` | `pub fn begin(self: *Self, count: CounterType) error` |
| `finish` | `pub fn finish(self: *Self, count: CounterType) void` |
| `wait` | `pub fn wait(self: *Self) void` |

## fifo

| Function | Signature |
|----------|-----------|
| `LinearFifo` | `pub fn LinearFifo( comptime T: type, comptime buffer_type: LinearFifoBufferType, ) type` |
| `init` | `pub fn init() Self` |
| `init` | `pub fn init(buf: []T) Self` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `deinit` | `pub fn deinit(self: Self) void` |
| `realign` | `pub fn realign(self: *Self) void` |
| `shrink` | `pub fn shrink(self: *Self, size: usize) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, size: usize) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, size: usize) error` |
| `readableLength` | `pub fn readableLength(self: Self) usize` |
| `readableSlice` | `pub fn readableSlice(self: SliceSelfArg, offset: usize) []const T` |
| `discard` | `pub fn discard(self: *Self, count: usize) void` |
| `readItem` | `pub fn readItem(self: *Self) ?T` |
| `read` | `pub fn read(self: *Self, dst: []T) usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `writableLength` | `pub fn writableLength(self: Self) usize` |
| `writableSlice` | `pub fn writableSlice(self: SliceSelfArg, offset: usize) []T` |
| `writableWithSize` | `pub fn writableWithSize(self: *Self, size: usize) ![]T` |
| `update` | `pub fn update(self: *Self, count: usize) void` |
| `writeAssumeCapacity` | `pub fn writeAssumeCapacity(self: *Self, src: []const T) void` |
| `writeItem` | `pub fn writeItem(self: *Self, item: T) !void` |
| `writeItemAssumeCapacity` | `pub fn writeItemAssumeCapacity(self: *Self, item: T) void` |
| `write` | `pub fn write(self: *Self, src: []const T) !void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `unget` | `pub fn unget(self: *Self, src: []const T) !void` |
| `peekItem` | `pub fn peekItem(self: Self, offset: usize) T` |
| `pump` | `pub fn pump(self: *Self, src_reader: anytype, dest_writer: anytype) !void` |

## fmt

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format(value: ?, comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype) !void /// ``` /// with `?` being the type formatted, this function will be called instead of the default implementation. /// This allows user types to be formatted in a logical manner instead of dumping all fields of the type. /// /// A user type may be a `struct`, `vector`, `union` or `enum` type. /// /// To print literal curly braces, escape them by writing them twice, e.g. `` |
| `format` | `pub fn format( writer: anytype, comptime fmt: []const u8, args: anytype, ) !void` |
| `formatAddress` | `pub fn formatAddress(value: anytype, options: FormatOptions, writer: anytype) @TypeOf(writer).Error!void` |
| `formatType` | `pub fn formatType( value: anytype, comptime fmt: []const u8, options: FormatOptions, writer: anytype, max_depth: usize, ) @TypeOf(writer).Error!void` |
| `formatIntValue` | `pub fn formatIntValue( value: anytype, comptime fmt: []const u8, options: FormatOptions, writer: anytype, ) !void` |
| `f` | `pub fn f( bytes: []const u8, comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `fmtSliceHexLower` | `pub fn fmtSliceHexLower(bytes: []const u8) std.fmt.Formatter(formatSliceHexLower)` |
| `fmtSliceHexUpper` | `pub fn fmtSliceHexUpper(bytes: []const u8) std.fmt.Formatter(formatSliceHexUpper)` |
| `f` | `pub fn f( bytes: []const u8, comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `fmtSliceEscapeLower` | `pub fn fmtSliceEscapeLower(bytes: []const u8) std.fmt.Formatter(formatSliceEscapeLower)` |
| `fmtSliceEscapeUpper` | `pub fn fmtSliceEscapeUpper(bytes: []const u8) std.fmt.Formatter(formatSliceEscapeUpper)` |
| `fmtIntSizeDec` | `pub fn fmtIntSizeDec(value: u64) std.fmt.Formatter(formatSizeDec)` |
| `fmtIntSizeBin` | `pub fn fmtIntSizeBin(value: u64) std.fmt.Formatter(formatSizeBin)` |
| `formatText` | `pub fn formatText( bytes: []const u8, comptime fmt: []const u8, options: FormatOptions, writer: anytype, ) !void` |
| `formatAsciiChar` | `pub fn formatAsciiChar( c: u8, options: FormatOptions, writer: anytype, ) !void` |
| `formatUnicodeCodepoint` | `pub fn formatUnicodeCodepoint( c: u21, options: FormatOptions, writer: anytype, ) !void` |
| `formatBuf` | `pub fn formatBuf( buf: []const u8, options: FormatOptions, writer: anytype, ) !void` |
| `formatFloatScientific` | `pub fn formatFloatScientific( value: anytype, options: FormatOptions, writer: anytype, ) !void` |
| `formatFloatHexadecimal` | `pub fn formatFloatHexadecimal( value: anytype, options: FormatOptions, writer: anytype, ) !void` |
| `formatFloatDecimal` | `pub fn formatFloatDecimal( value: anytype, options: FormatOptions, writer: anytype, ) !void` |
| `formatInt` | `pub fn formatInt( value: anytype, base: u8, case: Case, options: FormatOptions, writer: anytype, ) !void` |
| `formatIntBuf` | `pub fn formatIntBuf(out_buf: []u8, value: anytype, base: u8, case: Case, options: FormatOptions) usize` |
| `fmtDuration` | `pub fn fmtDuration(ns: u64) Formatter(formatDuration)` |
| `fmtDurationSigned` | `pub fn fmtDurationSigned(ns: i64) Formatter(formatDurationSigned)` |
| `Formatter` | `pub fn Formatter(comptime format_fn: anytype) type` |
| `format` | `pub fn format( self: @This(), comptime fmt: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) @TypeOf(writer).Error!void` |
| `parseInt` | `pub fn parseInt(comptime T: type, buf: []const u8, radix: u8) ParseIntError!T` |
| `parseUnsigned` | `pub fn parseUnsigned(comptime T: type, buf: []const u8, radix: u8) ParseIntError!T` |
| `charToDigit` | `pub fn charToDigit(c: u8, radix: u8) (error` |
| `digitToChar` | `pub fn digitToChar(digit: u8, case: Case) u8` |
| `bufPrint` | `pub fn bufPrint(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![]u8` |
| `bufPrintZ` | `pub fn bufPrintZ(buf: []u8, comptime fmt: []const u8, args: anytype) BufPrintError![:0]u8` |
| `count` | `pub fn count(comptime fmt: []const u8, args: anytype) u64` |
| `allocPrint` | `pub fn allocPrint(allocator: mem.Allocator, comptime fmt: []const u8, args: anytype) AllocPrintError![]u8` |
| `allocPrintZ` | `pub fn allocPrintZ(allocator: mem.Allocator, comptime fmt: []const u8, args: anytype) AllocPrintError![:0]u8` |
| `bufPrintIntToSlice` | `pub fn bufPrintIntToSlice(buf: []u8, value: anytype, base: u8, case: Case, options: FormatOptions) []u8` |
| `comptimePrint` | `pub fn comptimePrint(comptime fmt: []const u8, args: anytype) *const [count(fmt, args):0]u8` |
| `format` | `pub fn format( self: SelfType, comptime fmt: []const u8, options: FormatOptions, writer: anytype, ) !void` |
| `hexToBytes` | `pub fn hexToBytes(out: []u8, input: []const u8) ![]u8` |
| `format` | `pub fn format( self: SelfType, comptime fmt: []const u8, options: FormatOptions, writer: anytype, ) !void` |

## fmt / errol

| Function | Signature |
|----------|-----------|
| `roundToPrecision` | `pub fn roundToPrecision(float_decimal: *FloatDecimal, precision: usize, mode: RoundMode) void` |
| `errol3` | `pub fn errol3(value: f64, buffer: []u8) FloatDecimal` |

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
| `convertFast` | `pub fn convertFast(comptime T: type, n: Number(T)) ?T` |

## fmt / parse_float / convert_hex

| Function | Signature |
|----------|-----------|
| `convertHex` | `pub fn convertHex(comptime T: type, n_: Number(T)) T` |

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
| `firstIs` | `pub fn firstIs(self: FloatStream, c: u8) bool` |
| `firstIsLower` | `pub fn firstIsLower(self: FloatStream, c: u8) bool` |
| `firstIs2` | `pub fn firstIs2(self: FloatStream, c1: u8, c2: u8) bool` |
| `firstIs3` | `pub fn firstIs3(self: FloatStream, c1: u8, c2: u8, c3: u8) bool` |
| `firstIsDigit` | `pub fn firstIsDigit(self: FloatStream, comptime base: u8) bool` |
| `advance` | `pub fn advance(self: *FloatStream, n: usize) void` |
| `skipChars` | `pub fn skipChars(self: *FloatStream, c: u8) void` |
| `skipChars2` | `pub fn skipChars2(self: *FloatStream, c1: u8, c2: u8) void` |
| `readU64Unchecked` | `pub fn readU64Unchecked(self: FloatStream) u64` |
| `readU64` | `pub fn readU64(self: FloatStream) ?u64` |
| `atUnchecked` | `pub fn atUnchecked(self: *FloatStream, i: usize) u8` |
| `scanDigit` | `pub fn scanDigit(self: *FloatStream, comptime base: u8) ?u8` |

## fmt / parse_float / parse

| Function | Signature |
|----------|-----------|
| `parseNumber` | `pub fn parseNumber(comptime T: type, s: []const u8, negative: bool) ?Number(T)` |
| `parseInfOrNan` | `pub fn parseInfOrNan(comptime T: type, s: []const u8, negative: bool) ?T` |
| `validUnderscores` | `pub fn validUnderscores(s: []const u8, comptime base: u8) bool` |

## fmt / parse_float / parse_float

| Function | Signature |
|----------|-----------|
| `parseFloat` | `pub fn parseFloat(comptime T: type, s: []const u8) ParseFloatError!T` |

## fs

| Function | Signature |
|----------|-----------|
| `atomicSymLink` | `pub fn atomicSymLink(allocator: Allocator, existing_path: []const u8, new_path: []const u8) !void` |
| `updateFileAbsolute` | `pub fn updateFileAbsolute( source_path: []const u8, dest_path: []const u8, args: CopyFileOptions, ) !PrevStatus` |
| `copyFileAbsolute` | `pub fn copyFileAbsolute(source_path: []const u8, dest_path: []const u8, args: CopyFileOptions) !void` |
| `init` | `pub fn init( dest_basename: []const u8, mode: File.Mode, dir: Dir, close_dir_on_deinit: bool, ) InitError!AtomicFile` |
| `deinit` | `pub fn deinit(self: *AtomicFile) void` |
| `finish` | `pub fn finish(self: *AtomicFile) FinishError!void` |
| `makeDirAbsolute` | `pub fn makeDirAbsolute(absolute_path: []const u8) !void` |
| `makeDirAbsoluteZ` | `pub fn makeDirAbsoluteZ(absolute_path_z: [*:0]const u8) !void` |
| `makeDirAbsoluteW` | `pub fn makeDirAbsoluteW(absolute_path_w: [*:0]const u16) !void` |
| `deleteDirAbsolute` | `pub fn deleteDirAbsolute(dir_path: []const u8) !void` |
| `deleteDirAbsoluteZ` | `pub fn deleteDirAbsoluteZ(dir_path: [*:0]const u8) !void` |
| `deleteDirAbsoluteW` | `pub fn deleteDirAbsoluteW(dir_path: [*:0]const u16) !void` |
| `renameAbsolute` | `pub fn renameAbsolute(old_path: []const u8, new_path: []const u8) !void` |
| `renameAbsoluteZ` | `pub fn renameAbsoluteZ(old_path: [*:0]const u8, new_path: [*:0]const u8) !void` |
| `renameAbsoluteW` | `pub fn renameAbsoluteW(old_path: [*:0]const u16, new_path: [*:0]const u16) !void` |
| `rename` | `pub fn rename(old_dir: Dir, old_sub_path: []const u8, new_dir: Dir, new_sub_path: []const u8) !void` |
| `renameZ` | `pub fn renameZ(old_dir: Dir, old_sub_path_z: [*:0]const u8, new_dir: Dir, new_sub_path_z: [*:0]const u8) !void` |
| `renameW` | `pub fn renameW(old_dir: Dir, old_sub_path_w: []const u16, new_dir: Dir, new_sub_path_w: []const u16) !void` |
| `next` | `pub fn next(self: *Self) Error!?Entry` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) Error!?Entry` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) Error!?Entry` |
| `nextLinux` | `pub fn nextLinux(self: *Self) ErrorLinux!?Entry` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) Error!?Entry` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) Error!?Entry` |
| `nextWasi` | `pub fn nextWasi(self: *Self) ErrorWasi!?Entry` |
| `reset` | `pub fn reset(self: *Self) void` |
| `iterate` | `pub fn iterate(self: IterableDir) Iterator` |
| `iterateAssumeFirstIteration` | `pub fn iterateAssumeFirstIteration(self: IterableDir) Iterator` |
| `next` | `pub fn next(self: *Walker) !?WalkerEntry` |
| `deinit` | `pub fn deinit(self: *Walker) void` |
| `walk` | `pub fn walk(self: IterableDir, allocator: Allocator) !Walker` |
| `close` | `pub fn close(self: *IterableDir) void` |
| `chmod` | `pub fn chmod(self: IterableDir, new_mode: File.Mode) ChmodError!void` |
| `chown` | `pub fn chown(self: IterableDir, owner: ?File.Uid, group: ?File.Gid) ChownError!void` |
| `close` | `pub fn close(self: *Dir) void` |
| `openFile` | `pub fn openFile(self: Dir, sub_path: []const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileWasi` | `pub fn openFileWasi(self: Dir, sub_path: []const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileZ` | `pub fn openFileZ(self: Dir, sub_path: [*:0]const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileW` | `pub fn openFileW(self: Dir, sub_path_w: []const u16, flags: File.OpenFlags) File.OpenError!File` |
| `createFile` | `pub fn createFile(self: Dir, sub_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileWasi` | `pub fn createFileWasi(self: Dir, sub_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileZ` | `pub fn createFileZ(self: Dir, sub_path_c: [*:0]const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileW` | `pub fn createFileW(self: Dir, sub_path_w: []const u16, flags: File.CreateFlags) File.OpenError!File` |
| `makeDir` | `pub fn makeDir(self: Dir, sub_path: []const u8) !void` |
| `makeDirZ` | `pub fn makeDirZ(self: Dir, sub_path: [*:0]const u8) !void` |
| `makeDirW` | `pub fn makeDirW(self: Dir, sub_path: [*:0]const u16) !void` |
| `makePath` | `pub fn makePath(self: Dir, sub_path: []const u8) !void` |
| `makeOpenPath` | `pub fn makeOpenPath(self: Dir, sub_path: []const u8, open_dir_options: OpenDirOptions) !Dir` |
| `makeOpenPathIterable` | `pub fn makeOpenPathIterable(self: Dir, sub_path: []const u8, open_dir_options: OpenDirOptions) !IterableDir` |
| `realpath` | `pub fn realpath(self: Dir, pathname: []const u8, out_buffer: []u8) ![]u8` |
| `realpathZ` | `pub fn realpathZ(self: Dir, pathname: [*:0]const u8, out_buffer: []u8) ![]u8` |
| `realpathW` | `pub fn realpathW(self: Dir, pathname: []const u16, out_buffer: []u8) ![]u8` |
| `realpathAlloc` | `pub fn realpathAlloc(self: Dir, allocator: Allocator, pathname: []const u8) ![]u8` |
| `setAsCwd` | `pub fn setAsCwd(self: Dir) !void` |
| `openDir` | `pub fn openDir(self: Dir, sub_path: []const u8, args: OpenDirOptions) OpenError!Dir` |
| `openIterableDir` | `pub fn openIterableDir(self: Dir, sub_path: []const u8, args: OpenDirOptions) OpenError!IterableDir` |
| `openDirWasi` | `pub fn openDirWasi(self: Dir, sub_path: []const u8, args: OpenDirOptions) OpenError!Dir` |
| `openDirZ` | `pub fn openDirZ(self: Dir, sub_path_c: [*:0]const u8, args: OpenDirOptions, iterable: bool) OpenError!Dir` |
| `openDirW` | `pub fn openDirW(self: Dir, sub_path_w: [*:0]const u16, args: OpenDirOptions, iterable: bool) OpenError!Dir` |
| `deleteFile` | `pub fn deleteFile(self: Dir, sub_path: []const u8) DeleteFileError!void` |
| `deleteFileZ` | `pub fn deleteFileZ(self: Dir, sub_path_c: [*:0]const u8) DeleteFileError!void` |
| `deleteFileW` | `pub fn deleteFileW(self: Dir, sub_path_w: []const u16) DeleteFileError!void` |
| `deleteDir` | `pub fn deleteDir(self: Dir, sub_path: []const u8) DeleteDirError!void` |
| `deleteDirZ` | `pub fn deleteDirZ(self: Dir, sub_path_c: [*:0]const u8) DeleteDirError!void` |
| `deleteDirW` | `pub fn deleteDirW(self: Dir, sub_path_w: []const u16) DeleteDirError!void` |
| `rename` | `pub fn rename(self: Dir, old_sub_path: []const u8, new_sub_path: []const u8) RenameError!void` |
| `renameZ` | `pub fn renameZ(self: Dir, old_sub_path_z: [*:0]const u8, new_sub_path_z: [*:0]const u8) RenameError!void` |
| `renameW` | `pub fn renameW(self: Dir, old_sub_path_w: []const u16, new_sub_path_w: []const u16) RenameError!void` |
| `symLink` | `pub fn symLink( self: Dir, target_path: []const u8, sym_link_path: []const u8, flags: SymLinkFlags, ) !void` |
| `symLinkWasi` | `pub fn symLinkWasi( self: Dir, target_path: []const u8, sym_link_path: []const u8, _: SymLinkFlags, ) !void` |
| `symLinkZ` | `pub fn symLinkZ( self: Dir, target_path_c: [*:0]const u8, sym_link_path_c: [*:0]const u8, flags: SymLinkFlags, ) !void` |
| `symLinkW` | `pub fn symLinkW( self: Dir, target_path_w: []const u16, sym_link_path_w: []const u16, flags: SymLinkFlags, ) !void` |
| `readLink` | `pub fn readLink(self: Dir, sub_path: []const u8, buffer: []u8) ![]u8` |
| `readLinkWasi` | `pub fn readLinkWasi(self: Dir, sub_path: []const u8, buffer: []u8) ![]u8` |
| `readLinkZ` | `pub fn readLinkZ(self: Dir, sub_path_c: [*:0]const u8, buffer: []u8) ![]u8` |
| `readLinkW` | `pub fn readLinkW(self: Dir, sub_path_w: []const u16, buffer: []u8) ![]u8` |
| `readFile` | `pub fn readFile(self: Dir, file_path: []const u8, buffer: []u8) ![]u8` |
| `readFileAlloc` | `pub fn readFileAlloc(self: Dir, allocator: mem.Allocator, file_path: []const u8, max_bytes: usize) ![]u8` |
| `readFileAllocOptions` | `pub fn readFileAllocOptions( self: Dir, allocator: mem.Allocator, file_path: []const u8, max_bytes: usize, size_hint: ?usize, comptime alignment: u29, comptime optional_sentinel: ?u8, ) !(if (optional_sentinel) |s| [:s]align(alignment) u8 else []align(alignment) u8)` |
| `deleteTree` | `pub fn deleteTree(self: Dir, sub_path: []const u8) DeleteTreeError!void` |
| `deleteTreeMinStackSize` | `pub fn deleteTreeMinStackSize(self: Dir, sub_path: []const u8) DeleteTreeError!void` |
| `writeFile` | `pub fn writeFile(self: Dir, sub_path: []const u8, data: []const u8) !void` |
| `access` | `pub fn access(self: Dir, sub_path: []const u8, flags: File.OpenFlags) AccessError!void` |
| `accessZ` | `pub fn accessZ(self: Dir, sub_path: [*:0]const u8, flags: File.OpenFlags) AccessError!void` |
| `accessW` | `pub fn accessW(self: Dir, sub_path_w: [*:0]const u16, flags: File.OpenFlags) AccessError!void` |
| `updateFile` | `pub fn updateFile( source_dir: Dir, source_path: []const u8, dest_dir: Dir, dest_path: []const u8, options: CopyFileOptions, ) !PrevStatus` |
| `copyFile` | `pub fn copyFile(source_dir: Dir, source_path: []const u8, dest_dir: Dir, dest_path: []const u8, options: CopyFileOptions) CopyFileError!void` |
| `atomicFile` | `pub fn atomicFile(self: Dir, dest_path: []const u8, options: AtomicFileOptions) !AtomicFile` |
| `stat` | `pub fn stat(self: Dir) StatError!Stat` |
| `statFile` | `pub fn statFile(self: Dir, sub_path: []const u8) StatFileError!File.Stat` |
| `setPermissions` | `pub fn setPermissions(self: Dir, permissions: Permissions) SetPermissionsError!void` |
| `metadata` | `pub fn metadata(self: Dir) MetadataError!Metadata` |
| `cwd` | `pub fn cwd() Dir` |
| `openDirAbsolute` | `pub fn openDirAbsolute(absolute_path: []const u8, flags: Dir.OpenDirOptions) File.OpenError!Dir` |
| `openDirAbsoluteZ` | `pub fn openDirAbsoluteZ(absolute_path_c: [*:0]const u8, flags: Dir.OpenDirOptions) File.OpenError!Dir` |
| `openDirAbsoluteW` | `pub fn openDirAbsoluteW(absolute_path_c: [*:0]const u16, flags: Dir.OpenDirOptions) File.OpenError!Dir` |
| `openIterableDirAbsolute` | `pub fn openIterableDirAbsolute(absolute_path: []const u8, flags: Dir.OpenDirOptions) File.OpenError!IterableDir` |
| `openIterableDirAbsoluteZ` | `pub fn openIterableDirAbsoluteZ(absolute_path_c: [*:0]const u8, flags: Dir.OpenDirOptions) File.OpenError!IterableDir` |
| `openIterableDirAbsoluteW` | `pub fn openIterableDirAbsoluteW(absolute_path_c: [*:0]const u16, flags: Dir.OpenDirOptions) File.OpenError!IterableDir` |
| `openFileAbsolute` | `pub fn openFileAbsolute(absolute_path: []const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileAbsoluteZ` | `pub fn openFileAbsoluteZ(absolute_path_c: [*:0]const u8, flags: File.OpenFlags) File.OpenError!File` |
| `openFileAbsoluteW` | `pub fn openFileAbsoluteW(absolute_path_w: []const u16, flags: File.OpenFlags) File.OpenError!File` |
| `accessAbsolute` | `pub fn accessAbsolute(absolute_path: []const u8, flags: File.OpenFlags) Dir.AccessError!void` |
| `accessAbsoluteZ` | `pub fn accessAbsoluteZ(absolute_path: [*:0]const u8, flags: File.OpenFlags) Dir.AccessError!void` |
| `accessAbsoluteW` | `pub fn accessAbsoluteW(absolute_path: [*:0]const 16, flags: File.OpenFlags) Dir.AccessError!void` |
| `createFileAbsolute` | `pub fn createFileAbsolute(absolute_path: []const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileAbsoluteZ` | `pub fn createFileAbsoluteZ(absolute_path_c: [*:0]const u8, flags: File.CreateFlags) File.OpenError!File` |
| `createFileAbsoluteW` | `pub fn createFileAbsoluteW(absolute_path_w: [*:0]const u16, flags: File.CreateFlags) File.OpenError!File` |
| `deleteFileAbsolute` | `pub fn deleteFileAbsolute(absolute_path: []const u8) Dir.DeleteFileError!void` |
| `deleteFileAbsoluteZ` | `pub fn deleteFileAbsoluteZ(absolute_path_c: [*:0]const u8) Dir.DeleteFileError!void` |
| `deleteFileAbsoluteW` | `pub fn deleteFileAbsoluteW(absolute_path_w: [*:0]const u16) Dir.DeleteFileError!void` |
| `deleteTreeAbsolute` | `pub fn deleteTreeAbsolute(absolute_path: []const u8) !void` |
| `readLinkAbsolute` | `pub fn readLinkAbsolute(pathname: []const u8, buffer: *[MAX_PATH_BYTES]u8) ![]u8` |
| `readlinkAbsoluteW` | `pub fn readlinkAbsoluteW(pathname_w: [*:0]const u16, buffer: *[MAX_PATH_BYTES]u8) ![]u8` |
| `readLinkAbsoluteZ` | `pub fn readLinkAbsoluteZ(pathname_c: [*:0]const u8, buffer: *[MAX_PATH_BYTES]u8) ![]u8` |
| `symLinkAbsolute` | `pub fn symLinkAbsolute(target_path: []const u8, sym_link_path: []const u8, flags: SymLinkFlags) !void` |
| `symLinkAbsoluteW` | `pub fn symLinkAbsoluteW(target_path_w: []const u16, sym_link_path_w: []const u16, flags: SymLinkFlags) !void` |
| `symLinkAbsoluteZ` | `pub fn symLinkAbsoluteZ(target_path_c: [*:0]const u8, sym_link_path_c: [*:0]const u8, flags: SymLinkFlags) !void` |
| `openSelfExe` | `pub fn openSelfExe(flags: File.OpenFlags) OpenSelfExeError!File` |
| `selfExePathAlloc` | `pub fn selfExePathAlloc(allocator: Allocator) ![]u8` |
| `selfExePath` | `pub fn selfExePath(out_buffer: []u8) SelfExePathError![]u8` |
| `selfExePathW` | `pub fn selfExePathW() [:0]const u16` |
| `selfExeDirPathAlloc` | `pub fn selfExeDirPathAlloc(allocator: Allocator) ![]u8` |
| `selfExeDirPath` | `pub fn selfExeDirPath(out_buffer: []u8) SelfExePathError![]const u8` |
| `realpathAlloc` | `pub fn realpathAlloc(allocator: Allocator, pathname: []const u8) ![]u8` |

## fs / file

| Function | Signature |
|----------|-----------|
| `isRead` | `pub fn isRead(self: OpenFlags) bool` |
| `isWrite` | `pub fn isWrite(self: OpenFlags) bool` |
| `close` | `pub fn close(self: File) void` |
| `sync` | `pub fn sync(self: File) SyncError!void` |
| `isTty` | `pub fn isTty(self: File) bool` |
| `supportsAnsiEscapeCodes` | `pub fn supportsAnsiEscapeCodes(self: File) bool` |
| `setEndPos` | `pub fn setEndPos(self: File, length: u64) SetEndPosError!void` |
| `seekBy` | `pub fn seekBy(self: File, offset: i64) SeekError!void` |
| `seekFromEnd` | `pub fn seekFromEnd(self: File, offset: i64) SeekError!void` |
| `seekTo` | `pub fn seekTo(self: File, offset: u64) SeekError!void` |
| `getPos` | `pub fn getPos(self: File) GetSeekPosError!u64` |
| `getEndPos` | `pub fn getEndPos(self: File) GetSeekPosError!u64` |
| `mode` | `pub fn mode(self: File) ModeError!Mode` |
| `stat` | `pub fn stat(self: File) StatError!Stat` |
| `chmod` | `pub fn chmod(self: File, new_mode: Mode) ChmodError!void` |
| `chown` | `pub fn chown(self: File, owner: ?Uid, group: ?Gid) ChownError!void` |
| `readOnly` | `pub fn readOnly(self: Self) bool` |
| `setReadOnly` | `pub fn setReadOnly(self: *Self, read_only: bool) void` |
| `readOnly` | `pub fn readOnly(self: Self) bool` |
| `setReadOnly` | `pub fn setReadOnly(self: *Self, read_only: bool) void` |
| `readOnly` | `pub fn readOnly(self: Self) bool` |
| `setReadOnly` | `pub fn setReadOnly(self: *Self, read_only: bool) void` |
| `unixHas` | `pub fn unixHas(self: Self, class: Class, permission: Permission) bool` |
| `unixSet` | `pub fn unixSet(self: *Self, class: Class, permissions: struct { read: ?bool = null, write: ?bool = null, execute: ?bool = null, }) void` |
| `unixNew` | `pub fn unixNew(new_mode: Mode) Self` |
| `setPermissions` | `pub fn setPermissions(self: File, permissions: Permissions) SetPermissionsError!void` |
| `size` | `pub fn size(self: Self) u64` |
| `permissions` | `pub fn permissions(self: Self) Permissions` |
| `kind` | `pub fn kind(self: Self) Kind` |
| `accessed` | `pub fn accessed(self: Self) i128` |
| `modified` | `pub fn modified(self: Self) i128` |
| `created` | `pub fn created(self: Self) ?i128` |
| `size` | `pub fn size(self: Self) u64` |
| `permissions` | `pub fn permissions(self: Self) Permissions` |
| `kind` | `pub fn kind(self: Self) Kind` |
| `accessed` | `pub fn accessed(self: Self) i128` |
| `modified` | `pub fn modified(self: Self) i128` |
| `created` | `pub fn created(self: Self) ?i128` |
| `size` | `pub fn size(self: Self) u64` |
| `permissions` | `pub fn permissions(self: Self) Permissions` |
| `kind` | `pub fn kind(self: Self) Kind` |
| `accessed` | `pub fn accessed(self: Self) i128` |
| `modified` | `pub fn modified(self: Self) i128` |
| `created` | `pub fn created(self: Self) ?i128` |
| `size` | `pub fn size(self: Self) u64` |
| `permissions` | `pub fn permissions(self: Self) Permissions` |
| `kind` | `pub fn kind(self: Self) Kind` |
| `accessed` | `pub fn accessed(self: Self) i128` |
| `modified` | `pub fn modified(self: Self) i128` |
| `created` | `pub fn created(self: Self) ?i128` |
| `metadata` | `pub fn metadata(self: File) MetadataError!Metadata` |
| `updateTimes` | `pub fn updateTimes( self: File, /// access timestamp in nanoseconds atime: i128, /// last modification timestamp in nanoseconds mtime: i128, ) UpdateTimesError!void` |
| `readToEndAlloc` | `pub fn readToEndAlloc(self: File, allocator: mem.Allocator, max_bytes: usize) ![]u8` |
| `readToEndAllocOptions` | `pub fn readToEndAllocOptions( self: File, allocator: mem.Allocator, max_bytes: usize, size_hint: ?usize, comptime alignment: u29, comptime optional_sentinel: ?u8, ) !(if (optional_sentinel) |s| [:s]align(alignment) u8 else []align(alignment) u8)` |
| `read` | `pub fn read(self: File, buffer: []u8) ReadError!usize` |
| `readAll` | `pub fn readAll(self: File, buffer: []u8) ReadError!usize` |
| `pread` | `pub fn pread(self: File, buffer: []u8, offset: u64) PReadError!usize` |
| `preadAll` | `pub fn preadAll(self: File, buffer: []u8, offset: u64) PReadError!usize` |
| `readv` | `pub fn readv(self: File, iovecs: []const os.iovec) ReadError!usize` |
| `readvAll` | `pub fn readvAll(self: File, iovecs: []os.iovec) ReadError!usize` |
| `preadv` | `pub fn preadv(self: File, iovecs: []const os.iovec, offset: u64) PReadError!usize` |
| `preadvAll` | `pub fn preadvAll(self: File, iovecs: []os.iovec, offset: u64) PReadError!usize` |
| `write` | `pub fn write(self: File, bytes: []const u8) WriteError!usize` |
| `writeAll` | `pub fn writeAll(self: File, bytes: []const u8) WriteError!void` |
| `pwrite` | `pub fn pwrite(self: File, bytes: []const u8, offset: u64) PWriteError!usize` |
| `pwriteAll` | `pub fn pwriteAll(self: File, bytes: []const u8, offset: u64) PWriteError!void` |
| `writev` | `pub fn writev(self: File, iovecs: []const os.iovec_const) WriteError!usize` |
| `writevAll` | `pub fn writevAll(self: File, iovecs: []os.iovec_const) WriteError!void` |
| `pwritev` | `pub fn pwritev(self: File, iovecs: []os.iovec_const, offset: u64) PWriteError!usize` |
| `pwritevAll` | `pub fn pwritevAll(self: File, iovecs: []os.iovec_const, offset: u64) PWriteError!void` |
| `copyRange` | `pub fn copyRange(in: File, in_offset: u64, out: File, out_offset: u64, len: u64) CopyRangeError!u64` |
| `copyRangeAll` | `pub fn copyRangeAll(in: File, in_offset: u64, out: File, out_offset: u64, len: u64) CopyRangeError!u64` |
| `writeFileAll` | `pub fn writeFileAll(self: File, in_file: File, args: WriteFileOptions) WriteFileError!void` |
| `writeFileAllUnseekable` | `pub fn writeFileAllUnseekable(self: File, in_file: File, args: WriteFileOptions) WriteFileError!void` |
| `reader` | `pub fn reader(file: File) Reader` |
| `writer` | `pub fn writer(file: File) Writer` |
| `seekableStream` | `pub fn seekableStream(file: File) SeekableStream` |
| `lock` | `pub fn lock(file: File, l: Lock) LockError!void` |
| `unlock` | `pub fn unlock(file: File) void` |
| `tryLock` | `pub fn tryLock(file: File, l: Lock) LockError!bool` |
| `downgradeLock` | `pub fn downgradeLock(file: File) LockError!void` |

## fs / get_app_data_dir

| Function | Signature |
|----------|-----------|
| `getAppDataDir` | `pub fn getAppDataDir(allocator: mem.Allocator, appname: []const u8) GetAppDataDirError![]u8` |

## fs / path

| Function | Signature |
|----------|-----------|
| `isSep` | `pub fn isSep(byte: u8) bool` |
| `join` | `pub fn join(allocator: Allocator, paths: []const []const u8) ![]u8` |
| `joinZ` | `pub fn joinZ(allocator: Allocator, paths: []const []const u8) ![:0]u8` |
| `isAbsoluteZ` | `pub fn isAbsoluteZ(path_c: [*:0]const u8) bool` |
| `isAbsolute` | `pub fn isAbsolute(path: []const u8) bool` |
| `isAbsoluteWindows` | `pub fn isAbsoluteWindows(path: []const u8) bool` |
| `isAbsoluteWindowsW` | `pub fn isAbsoluteWindowsW(path_w: [*:0]const u16) bool` |
| `isAbsoluteWindowsWTF16` | `pub fn isAbsoluteWindowsWTF16(path: []const u16) bool` |
| `isAbsoluteWindowsZ` | `pub fn isAbsoluteWindowsZ(path_c: [*:0]const u8) bool` |
| `isAbsolutePosix` | `pub fn isAbsolutePosix(path: []const u8) bool` |
| `isAbsolutePosixZ` | `pub fn isAbsolutePosixZ(path_c: [*:0]const u8) bool` |
| `windowsParsePath` | `pub fn windowsParsePath(path: []const u8) WindowsPath` |
| `diskDesignator` | `pub fn diskDesignator(path: []const u8) []const u8` |
| `diskDesignatorWindows` | `pub fn diskDesignatorWindows(path: []const u8) []const u8` |
| `resolve` | `pub fn resolve(allocator: Allocator, paths: []const []const u8) ![]u8` |
| `resolveWindows` | `pub fn resolveWindows(allocator: Allocator, paths: []const []const u8) ![]u8` |
| `resolvePosix` | `pub fn resolvePosix(allocator: Allocator, paths: []const []const u8) ![]u8` |
| `dirname` | `pub fn dirname(path: []const u8) ?[]const u8` |
| `dirnameWindows` | `pub fn dirnameWindows(path: []const u8) ?[]const u8` |
| `dirnamePosix` | `pub fn dirnamePosix(path: []const u8) ?[]const u8` |
| `basename` | `pub fn basename(path: []const u8) []const u8` |
| `basenamePosix` | `pub fn basenamePosix(path: []const u8) []const u8` |
| `basenameWindows` | `pub fn basenameWindows(path: []const u8) []const u8` |
| `relative` | `pub fn relative(allocator: Allocator, from: []const u8, to: []const u8) ![]u8` |
| `relativeWindows` | `pub fn relativeWindows(allocator: Allocator, from: []const u8, to: []const u8) ![]u8` |
| `relativePosix` | `pub fn relativePosix(allocator: Allocator, from: []const u8, to: []const u8) ![]u8` |
| `extension` | `pub fn extension(path: []const u8) []const u8` |

## fs / wasi

| Function | Signature |
|----------|-----------|
| `eql` | `pub fn eql(self: Self, other: PreopenType) bool` |
| `getRelativePath` | `pub fn getRelativePath(self: Self, other: PreopenType) ?[]const u8` |
| `format` | `pub fn format(self: Self, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype) !void` |
| `new` | `pub fn new(fd: fd_t, preopen_type: PreopenType) Preopen` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `deinit` | `pub fn deinit(pm: Self) void` |
| `populate` | `pub fn populate(self: *Self, cwd_root: ?[]const u8) Error!void` |
| `findContaining` | `pub fn findContaining(self: Self, preopen_type: PreopenType) ?PreopenUri` |
| `findByFd` | `pub fn findByFd(self: Self, fd: fd_t) ?Preopen` |
| `find` | `pub fn find(self: Self, preopen_type: PreopenType) ?*const Preopen` |
| `asSlice` | `pub fn asSlice(self: Self) []const Preopen` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self) []Preopen` |

## fs / watch

| Function | Signature |
|----------|-----------|
| `Watch` | `pub fn Watch(comptime V: type) type` |
| `init` | `pub fn init(allocator: Allocator, event_buf_count: usize) !*Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `addFile` | `pub fn addFile(self: *Self, file_path: []const u8, value: V) !?V` |
| `removeFile` | `pub fn removeFile(self: *Self, file_path: []const u8) !?V` |

## hash / adler

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init() Adler32` |
| `update` | `pub fn update(self: *Adler32, input: []const u8) void` |
| `final` | `pub fn final(self: *Adler32) u32` |
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
| `benchmarkHash` | `pub fn benchmarkHash(comptime H: anytype, bytes: usize) !Result` |
| `benchmarkHashSmallKeys` | `pub fn benchmarkHashSmallKeys(comptime H: anytype, key_size: usize, bytes: usize) !Result` |
| `main` | `pub fn main() !void` |

## hash / cityhash

| Function | Signature |
|----------|-----------|
| `hash` | `pub fn hash(str: []const u8) u32` |
| `hash` | `pub fn hash(str: []const u8) u64` |
| `hashWithSeed` | `pub fn hashWithSeed(str: []const u8, seed: u64) u64` |
| `hashWithSeeds` | `pub fn hashWithSeeds(str: []const u8, seed0: u64, seed1: u64) u64` |

## hash / crc

| Function | Signature |
|----------|-----------|
| `Crc32WithPoly` | `pub fn Crc32WithPoly(comptime poly: Polynomial) type` |
| `init` | `pub fn init() Self` |
| `update` | `pub fn update(self: *Self, input: []const u8) void` |
| `final` | `pub fn final(self: *Self) u32` |
| `hash` | `pub fn hash(input: []const u8) u32` |
| `Crc32SmallWithPoly` | `pub fn Crc32SmallWithPoly(comptime poly: Polynomial) type` |
| `init` | `pub fn init() Self` |
| `update` | `pub fn update(self: *Self, input: []const u8) void` |
| `final` | `pub fn final(self: *Self) u32` |
| `hash` | `pub fn hash(input: []const u8) u32` |

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
| `hash` | `pub fn hash(str: []const u8) u32` |
| `hashWithSeed` | `pub fn hashWithSeed(str: []const u8, seed: u32) u32` |
| `hashUint32` | `pub fn hashUint32(v: u32) u32` |
| `hashUint32WithSeed` | `pub fn hashUint32WithSeed(v: u32, seed: u32) u32` |
| `hashUint64` | `pub fn hashUint64(v: u64) u32` |
| `hashUint64WithSeed` | `pub fn hashUint64WithSeed(v: u64, seed: u32) u32` |

## hash / wyhash

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(seed: u64) WyhashStateless` |
| `update` | `pub fn update(self: *WyhashStateless, b: []const u8) void` |
| `final` | `pub fn final(self: *WyhashStateless, b: []const u8) u64` |
| `hash` | `pub fn hash(seed: u64, input: []const u8) u64` |
| `init` | `pub fn init(seed: u64) Wyhash` |
| `update` | `pub fn update(self: *Wyhash, b: []const u8) void` |
| `final` | `pub fn final(self: *Wyhash) u64` |
| `hash` | `pub fn hash(seed: u64, input: []const u8) u64` |

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
| `hash` | `pub fn hash(self: @This(), s: []const u8) u64` |
| `eql` | `pub fn eql(self: @This(), a: []const u8, b: []const u8) bool` |
| `eqlString` | `pub fn eqlString(a: []const u8, b: []const u8) bool` |
| `hashString` | `pub fn hashString(s: []const u8) u64` |
| `eql` | `pub fn eql(self: @This(), a: u32, b: u32) bool` |
| `hash` | `pub fn hash(self: @This(), x: u32) u64` |
| `eql` | `pub fn eql(self: @This(), a_slice: []const u8, b: u32) bool` |
| `hash` | `pub fn hash(self: @This(), adapted_key: []const u8) u64` |
| `verifyContext` | `pub fn verifyContext( comptime RawContext: type, comptime PseudoKey: type, comptime Key: type, comptime Hash: type, comptime is_array: bool, ) void` |
| `HashMap` | `pub fn HashMap( comptime K: type, comptime V: type, comptime Context: type, comptime max_load_percentage: u64, ) type` |
| `init` | `pub fn init(allocator: Allocator) Self` |
| `initContext` | `pub fn initContext(allocator: Allocator, ctx: Context) Self` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self) void` |
| `count` | `pub fn count(self: Self) Size` |
| `iterator` | `pub fn iterator(self: *const Self) Iterator` |
| `keyIterator` | `pub fn keyIterator(self: *const Self) KeyIterator` |
| `valueIterator` | `pub fn valueIterator(self: *const Self) ValueIterator` |
| `getOrPut` | `pub fn getOrPut(self: *Self, key: K) Allocator.Error!GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, key: anytype, ctx: anytype) Allocator.Error!GetOrPutResult` |
| `getOrPutAssumeCapacity` | `pub fn getOrPutAssumeCapacity(self: *Self, key: K) GetOrPutResult` |
| `getOrPutAssumeCapacityAdapted` | `pub fn getOrPutAssumeCapacityAdapted(self: *Self, key: anytype, ctx: anytype) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, key: K, value: V) Allocator.Error!Entry` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, expected_count: Size) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, additional_count: Size) Allocator.Error!void` |
| `capacity` | `pub fn capacity(self: *Self) Size` |
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
| `removeByPtr` | `pub fn removeByPtr(self: *Self, keyPtr: *K) void` |
| `clone` | `pub fn clone(self: Self) Allocator.Error!Self` |
| `cloneWithAllocator` | `pub fn cloneWithAllocator(self: Self, new_allocator: Allocator) Allocator.Error!Self` |
| `cloneWithContext` | `pub fn cloneWithContext(self: Self, new_ctx: anytype) Allocator.Error!HashMap(K, V, @TypeOf(new_ctx), max_load_percentage)` |
| `cloneWithAllocatorAndContext` | `pub fn cloneWithAllocatorAndContext( self: Self, new_allocator: Allocator, new_ctx: anytype, ) Allocator.Error!HashMap(K, V, @TypeOf(new_ctx), max_load_percentage)` |
| `HashMapUnmanaged` | `pub fn HashMapUnmanaged( comptime K: type, comptime V: type, comptime Context: type, comptime max_load_percentage: u64, ) type` |
| `isUsed` | `pub fn isUsed(self: Metadata) bool` |
| `isTombstone` | `pub fn isTombstone(self: Metadata) bool` |
| `isFree` | `pub fn isFree(self: Metadata) bool` |
| `takeFingerprint` | `pub fn takeFingerprint(hash: Hash) FingerPrint` |
| `fill` | `pub fn fill(self: *Metadata, fp: FingerPrint) void` |
| `remove` | `pub fn remove(self: *Metadata) void` |
| `next` | `pub fn next(it: *Iterator) ?Entry` |
| `next` | `pub fn next(self: *@This()) ?*T` |
| `promote` | `pub fn promote(self: Self, allocator: Allocator) Managed` |
| `promoteContext` | `pub fn promoteContext(self: Self, allocator: Allocator, ctx: Context) Managed` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, allocator: Allocator, new_size: Size) Allocator.Error!void` |
| `ensureTotalCapacityContext` | `pub fn ensureTotalCapacityContext(self: *Self, allocator: Allocator, new_size: Size, ctx: Context) Allocator.Error!void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, allocator: Allocator, additional_size: Size) Allocator.Error!void` |
| `ensureUnusedCapacityContext` | `pub fn ensureUnusedCapacityContext(self: *Self, allocator: Allocator, additional_size: Size, ctx: Context) Allocator.Error!void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, allocator: Allocator) void` |
| `count` | `pub fn count(self: *const Self) Size` |
| `capacity` | `pub fn capacity(self: *const Self) Size` |
| `iterator` | `pub fn iterator(self: *const Self) Iterator` |
| `keyIterator` | `pub fn keyIterator(self: *const Self) KeyIterator` |
| `valueIterator` | `pub fn valueIterator(self: *const Self) ValueIterator` |
| `putNoClobber` | `pub fn putNoClobber(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!void` |
| `putNoClobberContext` | `pub fn putNoClobberContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!void` |
| `putAssumeCapacity` | `pub fn putAssumeCapacity(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityContext` | `pub fn putAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `putAssumeCapacityNoClobber` | `pub fn putAssumeCapacityNoClobber(self: *Self, key: K, value: V) void` |
| `putAssumeCapacityNoClobberContext` | `pub fn putAssumeCapacityNoClobberContext(self: *Self, key: K, value: V, ctx: Context) void` |
| `fetchPut` | `pub fn fetchPut(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!?KV` |
| `fetchPutContext` | `pub fn fetchPutContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!?KV` |
| `fetchPutAssumeCapacity` | `pub fn fetchPutAssumeCapacity(self: *Self, key: K, value: V) ?KV` |
| `fetchPutAssumeCapacityContext` | `pub fn fetchPutAssumeCapacityContext(self: *Self, key: K, value: V, ctx: Context) ?KV` |
| `fetchRemove` | `pub fn fetchRemove(self: *Self, key: K) ?KV` |
| `fetchRemoveContext` | `pub fn fetchRemoveContext(self: *Self, key: K, ctx: Context) ?KV` |
| `fetchRemoveAdapted` | `pub fn fetchRemoveAdapted(self: *Self, key: anytype, ctx: anytype) ?KV` |
| `getEntry` | `pub fn getEntry(self: Self, key: K) ?Entry` |
| `getEntryContext` | `pub fn getEntryContext(self: Self, key: K, ctx: Context) ?Entry` |
| `getEntryAdapted` | `pub fn getEntryAdapted(self: Self, key: anytype, ctx: anytype) ?Entry` |
| `put` | `pub fn put(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!void` |
| `putContext` | `pub fn putContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!void` |
| `getKeyPtr` | `pub fn getKeyPtr(self: Self, key: K) ?*K` |
| `getKeyPtrContext` | `pub fn getKeyPtrContext(self: Self, key: K, ctx: Context) ?*K` |
| `getKeyPtrAdapted` | `pub fn getKeyPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*K` |
| `getKey` | `pub fn getKey(self: Self, key: K) ?K` |
| `getKeyContext` | `pub fn getKeyContext(self: Self, key: K, ctx: Context) ?K` |
| `getKeyAdapted` | `pub fn getKeyAdapted(self: Self, key: anytype, ctx: anytype) ?K` |
| `getPtr` | `pub fn getPtr(self: Self, key: K) ?*V` |
| `getPtrContext` | `pub fn getPtrContext(self: Self, key: K, ctx: Context) ?*V` |
| `getPtrAdapted` | `pub fn getPtrAdapted(self: Self, key: anytype, ctx: anytype) ?*V` |
| `get` | `pub fn get(self: Self, key: K) ?V` |
| `getContext` | `pub fn getContext(self: Self, key: K, ctx: Context) ?V` |
| `getAdapted` | `pub fn getAdapted(self: Self, key: anytype, ctx: anytype) ?V` |
| `getOrPut` | `pub fn getOrPut(self: *Self, allocator: Allocator, key: K) Allocator.Error!GetOrPutResult` |
| `getOrPutContext` | `pub fn getOrPutContext(self: *Self, allocator: Allocator, key: K, ctx: Context) Allocator.Error!GetOrPutResult` |
| `getOrPutAdapted` | `pub fn getOrPutAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype) Allocator.Error!GetOrPutResult` |
| `getOrPutContextAdapted` | `pub fn getOrPutContextAdapted(self: *Self, allocator: Allocator, key: anytype, key_ctx: anytype, ctx: Context) Allocator.Error!GetOrPutResult` |
| `getOrPutAssumeCapacity` | `pub fn getOrPutAssumeCapacity(self: *Self, key: K) GetOrPutResult` |
| `getOrPutAssumeCapacityContext` | `pub fn getOrPutAssumeCapacityContext(self: *Self, key: K, ctx: Context) GetOrPutResult` |
| `getOrPutAssumeCapacityAdapted` | `pub fn getOrPutAssumeCapacityAdapted(self: *Self, key: anytype, ctx: anytype) GetOrPutResult` |
| `getOrPutValue` | `pub fn getOrPutValue(self: *Self, allocator: Allocator, key: K, value: V) Allocator.Error!Entry` |
| `getOrPutValueContext` | `pub fn getOrPutValueContext(self: *Self, allocator: Allocator, key: K, value: V, ctx: Context) Allocator.Error!Entry` |
| `contains` | `pub fn contains(self: *const Self, key: K) bool` |
| `containsContext` | `pub fn containsContext(self: *const Self, key: K, ctx: Context) bool` |
| `containsAdapted` | `pub fn containsAdapted(self: *const Self, key: anytype, ctx: anytype) bool` |
| `remove` | `pub fn remove(self: *Self, key: K) bool` |
| `removeContext` | `pub fn removeContext(self: *Self, key: K, ctx: Context) bool` |
| `removeAdapted` | `pub fn removeAdapted(self: *Self, key: anytype, ctx: anytype) bool` |
| `removeByPtr` | `pub fn removeByPtr(self: *Self, keyPtr: *K) void` |
| `clone` | `pub fn clone(self: Self, allocator: Allocator) Allocator.Error!Self` |
| `cloneContext` | `pub fn cloneContext(self: Self, allocator: Allocator, new_ctx: anytype) Allocator.Error!HashMapUnmanaged(K, V, @TypeOf(new_ctx), max_load_percentage)` |

## heap

| Function | Signature |
|----------|-----------|
| `alignPageAllocLen` | `pub fn alignPageAllocLen(full_len: usize, len: usize, len_align: u29) usize` |
| `init` | `pub fn init() HeapAllocator` |
| `allocator` | `pub fn allocator(self: *HeapAllocator) Allocator` |
| `deinit` | `pub fn deinit(self: *HeapAllocator) void` |
| `init` | `pub fn init(buffer: []u8) FixedBufferAllocator` |
| `allocator` | `pub fn allocator(self: *FixedBufferAllocator) Allocator` |
| `threadSafeAllocator` | `pub fn threadSafeAllocator(self: *FixedBufferAllocator) Allocator` |
| `ownsPtr` | `pub fn ownsPtr(self: *FixedBufferAllocator, ptr: [*]u8) bool` |
| `ownsSlice` | `pub fn ownsSlice(self: *FixedBufferAllocator, slice: []u8) bool` |
| `isLastAllocation` | `pub fn isLastAllocation(self: *FixedBufferAllocator, buf: []u8) bool` |
| `reset` | `pub fn reset(self: *FixedBufferAllocator) void` |
| `stackFallback` | `pub fn stackFallback(comptime size: usize, fallback_allocator: Allocator) StackFallbackAllocator(size)` |
| `StackFallbackAllocator` | `pub fn StackFallbackAllocator(comptime size: usize) type` |
| `get` | `pub fn get(self: *Self) Allocator` |
| `testAllocator` | `pub fn testAllocator(base_allocator: mem.Allocator) !void` |
| `testAllocatorAligned` | `pub fn testAllocatorAligned(base_allocator: mem.Allocator) !void` |
| `testAllocatorLargeAlignment` | `pub fn testAllocatorLargeAlignment(base_allocator: mem.Allocator) !void` |
| `testAllocatorAlignedShrink` | `pub fn testAllocatorAlignedShrink(base_allocator: mem.Allocator) !void` |

## heap / arena_allocator

| Function | Signature |
|----------|-----------|
| `promote` | `pub fn promote(self: State, child_allocator: Allocator) ArenaAllocator` |
| `allocator` | `pub fn allocator(self: *ArenaAllocator) Allocator` |
| `init` | `pub fn init(child_allocator: Allocator) ArenaAllocator` |
| `deinit` | `pub fn deinit(self: ArenaAllocator) void` |

## heap / general_purpose_allocator

| Function | Signature |
|----------|-----------|
| `GeneralPurposeAllocator` | `pub fn GeneralPurposeAllocator(comptime config: Config) type` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `detectLeaks` | `pub fn detectLeaks(self: *Self) bool` |
| `flushRetainedMetadata` | `pub fn flushRetainedMetadata(self: *Self) void` |
| `deinit` | `pub fn deinit(self: *Self) bool` |
| `setRequestedMemoryLimit` | `pub fn setRequestedMemoryLimit(self: *Self, limit: usize) void` |

## heap / log_to_writer_allocator

| Function | Signature |
|----------|-----------|
| `LogToWriterAllocator` | `pub fn LogToWriterAllocator(comptime Writer: type) type` |
| `init` | `pub fn init(parent_allocator: Allocator, writer: Writer) Self` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `logToWriterAllocator` | `pub fn logToWriterAllocator( parent_allocator: Allocator, writer: anytype, ) LogToWriterAllocator(@TypeOf(writer))` |

## heap / logging_allocator

| Function | Signature |
|----------|-----------|
| `LoggingAllocator` | `pub fn LoggingAllocator( comptime success_log_level: std.log.Level, comptime failure_log_level: std.log.Level, ) type` |
| `ScopedLoggingAllocator` | `pub fn ScopedLoggingAllocator( comptime scope: @Type(.EnumLiteral), comptime success_log_level: std.log.Level, comptime failure_log_level: std.log.Level, ) type` |
| `init` | `pub fn init(parent_allocator: Allocator) Self` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `loggingAllocator` | `pub fn loggingAllocator(parent_allocator: Allocator) LoggingAllocator(.debug, .err)` |

## http / method

| Function | Signature |
|----------|-----------|
| `requestHasBody` | `pub fn requestHasBody(self: Method) bool` |
| `responseHasBody` | `pub fn responseHasBody(self: Method) bool` |
| `safe` | `pub fn safe(self: Method) bool` |
| `idempotent` | `pub fn idempotent(self: Method) bool` |
| `cacheable` | `pub fn cacheable(self: Method) bool` |

## http / status

| Function | Signature |
|----------|-----------|
| `phrase` | `pub fn phrase(self: Status) ?[]const u8` |
| `class` | `pub fn class(self: Status) ?Class` |

## io

| Function | Signature |
|----------|-----------|
| `getStdOut` | `pub fn getStdOut() File` |
| `getStdErr` | `pub fn getStdErr() File` |
| `getStdIn` | `pub fn getStdIn() File` |

## io / bit_reader

| Function | Signature |
|----------|-----------|
| `BitReader` | `pub fn BitReader(comptime endian: std.builtin.Endian, comptime ReaderType: type) type` |
| `init` | `pub fn init(forward_reader: ReaderType) Self` |
| `readBitsNoEof` | `pub fn readBitsNoEof(self: *Self, comptime U: type, bits: usize) !U` |
| `readBits` | `pub fn readBits(self: *Self, comptime U: type, bits: usize, out_bits: *usize) Error!U` |
| `alignToByte` | `pub fn alignToByte(self: *Self) void` |
| `read` | `pub fn read(self: *Self, buffer: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `bitReader` | `pub fn bitReader( comptime endian: std.builtin.Endian, underlying_stream: anytype, ) BitReader(endian, @TypeOf(underlying_stream))` |

## io / bit_writer

| Function | Signature |
|----------|-----------|
| `BitWriter` | `pub fn BitWriter(comptime endian: std.builtin.Endian, comptime WriterType: type) type` |
| `init` | `pub fn init(forward_writer: WriterType) Self` |
| `writeBits` | `pub fn writeBits(self: *Self, value: anytype, bits: usize) Error!void` |
| `flushBits` | `pub fn flushBits(self: *Self) Error!void` |
| `write` | `pub fn write(self: *Self, buffer: []const u8) Error!usize` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `bitWriter` | `pub fn bitWriter( comptime endian: std.builtin.Endian, underlying_stream: anytype, ) BitWriter(endian, @TypeOf(underlying_stream))` |

## io / buffered_atomic_file

| Function | Signature |
|----------|-----------|
| `create` | `pub fn create( allocator: mem.Allocator, dir: fs.Dir, dest_path: []const u8, atomic_file_options: fs.Dir.AtomicFileOptions, ) !*BufferedAtomicFile` |
| `destroy` | `pub fn destroy(self: *BufferedAtomicFile) void` |
| `finish` | `pub fn finish(self: *BufferedAtomicFile) !void` |
| `writer` | `pub fn writer(self: *BufferedAtomicFile) Writer` |

## io / buffered_reader

| Function | Signature |
|----------|-----------|
| `BufferedReader` | `pub fn BufferedReader(comptime buffer_size: usize, comptime ReaderType: type) type` |
| `read` | `pub fn read(self: *Self, dest: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `bufferedReader` | `pub fn bufferedReader(underlying_stream: anytype) BufferedReader(4096, @TypeOf(underlying_stream))` |

## io / buffered_writer

| Function | Signature |
|----------|-----------|
| `BufferedWriter` | `pub fn BufferedWriter(comptime buffer_size: usize, comptime WriterType: type) type` |
| `flush` | `pub fn flush(self: *Self) !void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `write` | `pub fn write(self: *Self, bytes: []const u8) Error!usize` |
| `bufferedWriter` | `pub fn bufferedWriter(underlying_stream: anytype) BufferedWriter(4096, @TypeOf(underlying_stream))` |

## io / c_writer

| Function | Signature |
|----------|-----------|
| `cWriter` | `pub fn cWriter(c_file: *std.c.FILE) CWriter` |

## io / change_detection_stream

| Function | Signature |
|----------|-----------|
| `ChangeDetectionStream` | `pub fn ChangeDetectionStream(comptime WriterType: type) type` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `changeDetected` | `pub fn changeDetected(self: *Self) bool` |
| `changeDetectionStream` | `pub fn changeDetectionStream( source: []const u8, underlying_writer: anytype, ) ChangeDetectionStream(@TypeOf(underlying_writer))` |

## io / counting_reader

| Function | Signature |
|----------|-----------|
| `CountingReader` | `pub fn CountingReader(comptime ReaderType: anytype) type` |
| `read` | `pub fn read(self: *@This(), buf: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *@This()) Reader` |
| `countingReader` | `pub fn countingReader(reader: anytype) CountingReader(@TypeOf(reader))` |

## io / counting_writer

| Function | Signature |
|----------|-----------|
| `CountingWriter` | `pub fn CountingWriter(comptime WriterType: type) type` |
| `write` | `pub fn write(self: *Self, bytes: []const u8) Error!usize` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `countingWriter` | `pub fn countingWriter(child_stream: anytype) CountingWriter(@TypeOf(child_stream))` |

## io / find_byte_writer

| Function | Signature |
|----------|-----------|
| `FindByteWriter` | `pub fn FindByteWriter(comptime UnderlyingWriter: type) type` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `findByteWriter` | `pub fn findByteWriter(byte: u8, underlying_writer: anytype) FindByteWriter(@TypeOf(underlying_writer))` |

## io / fixed_buffer_stream

| Function | Signature |
|----------|-----------|
| `FixedBufferStream` | `pub fn FixedBufferStream(comptime Buffer: type) type` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `seekableStream` | `pub fn seekableStream(self: *Self) SeekableStream` |
| `read` | `pub fn read(self: *Self, dest: []u8) ReadError!usize` |
| `write` | `pub fn write(self: *Self, bytes: []const u8) WriteError!usize` |
| `seekTo` | `pub fn seekTo(self: *Self, pos: u64) SeekError!void` |
| `seekBy` | `pub fn seekBy(self: *Self, amt: i64) SeekError!void` |
| `getEndPos` | `pub fn getEndPos(self: *Self) GetSeekPosError!u64` |
| `getPos` | `pub fn getPos(self: *Self) GetSeekPosError!u64` |
| `getWritten` | `pub fn getWritten(self: Self) Buffer` |
| `reset` | `pub fn reset(self: *Self) void` |
| `fixedBufferStream` | `pub fn fixedBufferStream(buffer: anytype) FixedBufferStream(NonSentinelSpan(@TypeOf(buffer)))` |

## io / limited_reader

| Function | Signature |
|----------|-----------|
| `LimitedReader` | `pub fn LimitedReader(comptime ReaderType: type) type` |
| `read` | `pub fn read(self: *Self, dest: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `limitedReader` | `pub fn limitedReader(inner_reader: anytype, bytes_left: u64) LimitedReader(@TypeOf(inner_reader))` |

## io / multi_writer

| Function | Signature |
|----------|-----------|
| `MultiWriter` | `pub fn MultiWriter(comptime Writers: type) type` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `write` | `pub fn write(self: *Self, bytes: []const u8) Error!usize` |
| `multiWriter` | `pub fn multiWriter(streams: anytype) MultiWriter(@TypeOf(streams))` |

## io / peek_stream

| Function | Signature |
|----------|-----------|
| `PeekStream` | `pub fn PeekStream( comptime buffer_type: std.fifo.LinearFifoBufferType, comptime ReaderType: type, ) type` |
| `init` | `pub fn init(base: ReaderType) Self` |
| `init` | `pub fn init(base: ReaderType, buf: []u8) Self` |
| `init` | `pub fn init(base: ReaderType, allocator: mem.Allocator) Self` |
| `putBackByte` | `pub fn putBackByte(self: *Self, byte: u8) !void` |
| `putBack` | `pub fn putBack(self: *Self, bytes: []const u8) !void` |
| `read` | `pub fn read(self: *Self, dest: []u8) Error!usize` |
| `reader` | `pub fn reader(self: *Self) Reader` |
| `peekStream` | `pub fn peekStream( comptime lookahead: comptime_int, underlying_stream: anytype, ) PeekStream(.` |

## io / reader

| Function | Signature |
|----------|-----------|
| `Reader` | `pub fn Reader( comptime Context: type, comptime ReadError: type, /// Returns the number of bytes read. It may be less than buffer.len. /// If the number of bytes read is 0, it means end of stream. /// End of stream is not an error condition. comptime readFn: fn (context: Context, buffer: []u8) ReadError!usize, ) type` |
| `read` | `pub fn read(self: Self, buffer: []u8) Error!usize` |
| `readAll` | `pub fn readAll(self: Self, buffer: []u8) Error!usize` |
| `readNoEof` | `pub fn readNoEof(self: Self, buf: []u8) !void` |
| `readAllArrayList` | `pub fn readAllArrayList(self: Self, array_list: *std.ArrayList(u8), max_append_size: usize) !void` |
| `readAllArrayListAligned` | `pub fn readAllArrayListAligned( self: Self, comptime alignment: ?u29, array_list: *std.ArrayListAligned(u8, alignment), max_append_size: usize, ) !void` |
| `readAllAlloc` | `pub fn readAllAlloc(self: Self, allocator: mem.Allocator, max_size: usize) ![]u8` |
| `readUntilDelimiterArrayList` | `pub fn readUntilDelimiterArrayList( self: Self, array_list: *std.ArrayList(u8), delimiter: u8, max_size: usize, ) !void` |
| `readUntilDelimiterAlloc` | `pub fn readUntilDelimiterAlloc( self: Self, allocator: mem.Allocator, delimiter: u8, max_size: usize, ) ![]u8` |
| `readUntilDelimiter` | `pub fn readUntilDelimiter(self: Self, buf: []u8, delimiter: u8) ![]u8` |
| `readUntilDelimiterOrEofAlloc` | `pub fn readUntilDelimiterOrEofAlloc( self: Self, allocator: mem.Allocator, delimiter: u8, max_size: usize, ) !?[]u8` |
| `readUntilDelimiterOrEof` | `pub fn readUntilDelimiterOrEof(self: Self, buf: []u8, delimiter: u8) !?[]u8` |
| `skipUntilDelimiterOrEof` | `pub fn skipUntilDelimiterOrEof(self: Self, delimiter: u8) !void` |
| `readByte` | `pub fn readByte(self: Self) !u8` |
| `readByteSigned` | `pub fn readByteSigned(self: Self) !i8` |
| `readBytesNoEof` | `pub fn readBytesNoEof(self: Self, comptime num_bytes: usize) ![num_bytes]u8` |
| `readIntoBoundedBytes` | `pub fn readIntoBoundedBytes( self: Self, comptime num_bytes: usize, bounded: *std.BoundedArray(u8, num_bytes), ) !void` |
| `readBoundedBytes` | `pub fn readBoundedBytes(self: Self, comptime num_bytes: usize) !std.BoundedArray(u8, num_bytes)` |
| `readIntNative` | `pub fn readIntNative(self: Self, comptime T: type) !T` |
| `readIntForeign` | `pub fn readIntForeign(self: Self, comptime T: type) !T` |
| `readIntLittle` | `pub fn readIntLittle(self: Self, comptime T: type) !T` |
| `readIntBig` | `pub fn readIntBig(self: Self, comptime T: type) !T` |
| `readInt` | `pub fn readInt(self: Self, comptime T: type, endian: std.builtin.Endian) !T` |
| `readVarInt` | `pub fn readVarInt(self: Self, comptime ReturnType: type, endian: std.builtin.Endian, size: usize) !ReturnType` |
| `skipBytes` | `pub fn skipBytes(self: Self, num_bytes: u64, comptime options: SkipBytesOptions) !void` |
| `isBytes` | `pub fn isBytes(self: Self, slice: []const u8) !bool` |
| `readStruct` | `pub fn readStruct(self: Self, comptime T: type) !T` |
| `readEnum` | `pub fn readEnum(self: Self, comptime Enum: type, endian: std.builtin.Endian) !Enum` |

## io / seekable_stream

| Function | Signature |
|----------|-----------|
| `SeekableStream` | `pub fn SeekableStream( comptime Context: type, comptime SeekErrorType: type, comptime GetSeekPosErrorType: type, comptime seekToFn: fn (context: Context, pos: u64) SeekErrorType!void, comptime seekByFn: fn (context: Context, pos: i64) SeekErrorType!void, comptime getPosFn: fn (context: Context) GetSeekPosErrorType!u64, comptime getEndPosFn: fn (context: Context) GetSeekPosErrorType!u64, ) type` |
| `seekTo` | `pub fn seekTo(self: Self, pos: u64) SeekError!void` |
| `seekBy` | `pub fn seekBy(self: Self, amt: i64) SeekError!void` |
| `getEndPos` | `pub fn getEndPos(self: Self) GetSeekPosError!u64` |
| `getPos` | `pub fn getPos(self: Self) GetSeekPosError!u64` |

## io / stream_source

| Function | Signature |
|----------|-----------|
| `read` | `pub fn read(self: *StreamSource, dest: []u8) ReadError!usize` |
| `write` | `pub fn write(self: *StreamSource, bytes: []const u8) WriteError!usize` |
| `seekTo` | `pub fn seekTo(self: *StreamSource, pos: u64) SeekError!void` |
| `seekBy` | `pub fn seekBy(self: *StreamSource, amt: i64) SeekError!void` |
| `getEndPos` | `pub fn getEndPos(self: *StreamSource) GetSeekPosError!u64` |
| `getPos` | `pub fn getPos(self: *StreamSource) GetSeekPosError!u64` |
| `reader` | `pub fn reader(self: *StreamSource) Reader` |
| `writer` | `pub fn writer(self: *StreamSource) Writer` |
| `seekableStream` | `pub fn seekableStream(self: *StreamSource) SeekableStream` |

## io / writer

| Function | Signature |
|----------|-----------|
| `Writer` | `pub fn Writer( comptime Context: type, comptime WriteError: type, comptime writeFn: fn (context: Context, bytes: []const u8) WriteError!usize, ) type` |
| `write` | `pub fn write(self: Self, bytes: []const u8) Error!usize` |
| `writeAll` | `pub fn writeAll(self: Self, bytes: []const u8) Error!void` |
| `print` | `pub fn print(self: Self, comptime format: []const u8, args: anytype) Error!void` |
| `writeByte` | `pub fn writeByte(self: Self, byte: u8) Error!void` |
| `writeByteNTimes` | `pub fn writeByteNTimes(self: Self, byte: u8, n: usize) Error!void` |
| `writeIntNative` | `pub fn writeIntNative(self: Self, comptime T: type, value: T) Error!void` |
| `writeIntForeign` | `pub fn writeIntForeign(self: Self, comptime T: type, value: T) Error!void` |
| `writeIntLittle` | `pub fn writeIntLittle(self: Self, comptime T: type, value: T) Error!void` |
| `writeIntBig` | `pub fn writeIntBig(self: Self, comptime T: type, value: T) Error!void` |
| `writeInt` | `pub fn writeInt(self: Self, comptime T: type, value: T, endian: std.builtin.Endian) Error!void` |
| `writeStruct` | `pub fn writeStruct(self: Self, value: anytype) Error!void` |

## json

| Function | Signature |
|----------|-----------|
| `decodedLength` | `pub fn decodedLength(self: @This()) usize` |
| `slice` | `pub fn slice(self: @This(), input: []const u8, i: usize) []const u8` |
| `slice` | `pub fn slice(self: @This(), input: []const u8, i: usize) []const u8` |
| `init` | `pub fn init(self: *Self) void` |
| `push` | `pub fn push(self: *Self, ty: AggregateContainerType) ?void` |
| `peek` | `pub fn peek(self: *Self) ?AggregateContainerType` |
| `pop` | `pub fn pop(self: *Self) ?AggregateContainerType` |
| `init` | `pub fn init() StreamingParser` |
| `reset` | `pub fn reset(p: *StreamingParser) void` |
| `fromAggregateContainerType` | `pub fn fromAggregateContainerType(ty: AggregateContainerType) State` |
| `feed` | `pub fn feed(p: *StreamingParser, c: u8, token1: *?Token, token2: *?Token) Error!void` |
| `init` | `pub fn init(slice: []const u8) TokenStream` |
| `next` | `pub fn next(self: *TokenStream) Error!?Token` |
| `validate` | `pub fn validate(s: []const u8) bool` |
| `deinit` | `pub fn deinit(self: *ValueTree) void` |
| `jsonStringify` | `pub fn jsonStringify( value: @This(), options: StringifyOptions, out_stream: anytype, ) @TypeOf(out_stream).Error!void` |
| `dump` | `pub fn dump(self: Value) void` |
| `ParseError` | `pub fn ParseError(comptime T: type) type` |
| `parse` | `pub fn parse(comptime T: type, tokens: *TokenStream, options: ParseOptions) ParseError(T)!T` |
| `parseFree` | `pub fn parseFree(comptime T: type, value: T, options: ParseOptions) void` |
| `init` | `pub fn init(allocator: Allocator, copy_strings: bool) Parser` |
| `deinit` | `pub fn deinit(p: *Parser) void` |
| `reset` | `pub fn reset(p: *Parser) void` |
| `parse` | `pub fn parse(p: *Parser, input: []const u8) !ValueTree` |
| `unescapeValidString` | `pub fn unescapeValidString(output: []u8, input: []const u8) UnescapeValidStringError!void` |
| `outputIndent` | `pub fn outputIndent( whitespace: @This(), out_stream: anytype, ) @TypeOf(out_stream).Error!void` |
| `encodeJsonString` | `pub fn encodeJsonString(string: []const u8, options: StringifyOptions, writer: anytype) !void` |
| `encodeJsonStringChars` | `pub fn encodeJsonStringChars(chars: []const u8, options: StringifyOptions, writer: anytype) !void` |
| `stringify` | `pub fn stringify( value: anytype, options: StringifyOptions, out_stream: anytype, ) @TypeOf(out_stream).Error!void` |
| `stringifyAlloc` | `pub fn stringifyAlloc(allocator: std.mem.Allocator, value: anytype, options: StringifyOptions) ![]const u8` |
| `jsonStringify` | `pub fn jsonStringify( value: Self, options: StringifyOptions, out_stream: anytype, ) !void` |
| `writer` | `pub fn writer(self: *Self) Writer` |

## json / write_stream

| Function | Signature |
|----------|-----------|
| `WriteStream` | `pub fn WriteStream(comptime OutStream: type, comptime max_depth: usize) type` |
| `init` | `pub fn init(stream: OutStream) Self` |
| `beginArray` | `pub fn beginArray(self: *Self) !void` |
| `beginObject` | `pub fn beginObject(self: *Self) !void` |
| `arrayElem` | `pub fn arrayElem(self: *Self) !void` |
| `objectField` | `pub fn objectField(self: *Self, name: []const u8) !void` |
| `endArray` | `pub fn endArray(self: *Self) !void` |
| `endObject` | `pub fn endObject(self: *Self) !void` |
| `emitNull` | `pub fn emitNull(self: *Self) !void` |
| `emitBool` | `pub fn emitBool(self: *Self, value: bool) !void` |
| `emitNumber` | `pub fn emitNumber( self: *Self, /// An integer, float, or `std.math.BigInt`. Emitted as a bare number if it fits losslessly /// in a IEEE 754 double float, otherwise emitted as a string to the full precision. value: anytype, ) !void` |
| `emitString` | `pub fn emitString(self: *Self, string: []const u8) !void` |
| `emitJson` | `pub fn emitJson(self: *Self, json: std.json.Value) Stream.Error!void` |
| `writeStream` | `pub fn writeStream( out_stream: anytype, comptime max_depth: usize, ) WriteStream(@TypeOf(out_stream), max_depth)` |

## leb128

| Function | Signature |
|----------|-----------|
| `readULEB128` | `pub fn readULEB128(comptime T: type, reader: anytype) !T` |
| `writeULEB128` | `pub fn writeULEB128(writer: anytype, uint_value: anytype) !void` |
| `readILEB128` | `pub fn readILEB128(comptime T: type, reader: anytype) !T` |
| `writeILEB128` | `pub fn writeILEB128(writer: anytype, int_value: anytype) !void` |
| `writeUnsignedFixed` | `pub fn writeUnsignedFixed(comptime l: usize, ptr: *[l]u8, int: std.meta.Int(.unsigned, l * 7)) void` |

## linked_list

| Function | Signature |
|----------|-----------|
| `SinglyLinkedList` | `pub fn SinglyLinkedList(comptime T: type) type` |
| `insertAfter` | `pub fn insertAfter(node: *Node, new_node: *Node) void` |
| `removeNext` | `pub fn removeNext(node: *Node) ?*Node` |
| `findLast` | `pub fn findLast(node: *Node) *Node` |
| `countChildren` | `pub fn countChildren(node: *const Node) usize` |
| `prepend` | `pub fn prepend(list: *Self, new_node: *Node) void` |
| `remove` | `pub fn remove(list: *Self, node: *Node) void` |
| `popFirst` | `pub fn popFirst(list: *Self) ?*Node` |
| `len` | `pub fn len(list: Self) usize` |
| `TailQueue` | `pub fn TailQueue(comptime T: type) type` |
| `insertAfter` | `pub fn insertAfter(list: *Self, node: *Node, new_node: *Node) void` |
| `insertBefore` | `pub fn insertBefore(list: *Self, node: *Node, new_node: *Node) void` |
| `concatByMoving` | `pub fn concatByMoving(list1: *Self, list2: *Self) void` |
| `append` | `pub fn append(list: *Self, new_node: *Node) void` |
| `prepend` | `pub fn prepend(list: *Self, new_node: *Node) void` |
| `remove` | `pub fn remove(list: *Self, node: *Node) void` |
| `pop` | `pub fn pop(list: *Self) ?*Node` |
| `popFirst` | `pub fn popFirst(list: *Self) ?*Node` |

## log

| Function | Signature |
|----------|-----------|
| `log` | `pub fn log( //! comptime level: std.log.Level, //! comptime scope: @TypeOf(.EnumLiteral), //! comptime format: []const u8, //! args: anytype, //! ) void` |
| `main` | `pub fn main() void` |
| `asText` | `pub fn asText(comptime self: Level) []const u8` |
| `defaultLog` | `pub fn defaultLog( comptime message_level: Level, comptime scope: @Type(.EnumLiteral), comptime format: []const u8, args: anytype, ) void` |
| `scoped` | `pub fn scoped(comptime scope: @Type(.EnumLiteral)) type` |
| `err` | `pub fn err( comptime format: []const u8, args: anytype, ) void` |
| `warn` | `pub fn warn( comptime format: []const u8, args: anytype, ) void` |
| `info` | `pub fn info( comptime format: []const u8, args: anytype, ) void` |
| `debug` | `pub fn debug( comptime format: []const u8, args: anytype, ) void` |

## macho

| Function | Signature |
|----------|-----------|
| `segName` | `pub fn segName(seg: *const segment_command_64) []const u8` |
| `sectName` | `pub fn sectName(sect: *const section_64) []const u8` |
| `segName` | `pub fn segName(sect: *const section_64) []const u8` |
| `attrs` | `pub fn attrs(sect: section_64) u32` |
| `isCode` | `pub fn isCode(sect: section_64) bool` |
| `isZerofill` | `pub fn isZerofill(sect: section_64) bool` |
| `isSymbolStubs` | `pub fn isSymbolStubs(sect: section_64) bool` |
| `isDebug` | `pub fn isDebug(sect: section_64) bool` |
| `isDontDeadStrip` | `pub fn isDontDeadStrip(sect: section_64) bool` |
| `isDontDeadStripIfReferencesLive` | `pub fn isDontDeadStripIfReferencesLive(sect: section_64) bool` |
| `stab` | `pub fn stab(sym: nlist_64) bool` |
| `pext` | `pub fn pext(sym: nlist_64) bool` |
| `ext` | `pub fn ext(sym: nlist_64) bool` |
| `sect` | `pub fn sect(sym: nlist_64) bool` |
| `undf` | `pub fn undf(sym: nlist_64) bool` |
| `indr` | `pub fn indr(sym: nlist_64) bool` |
| `abs` | `pub fn abs(sym: nlist_64) bool` |
| `weakDef` | `pub fn weakDef(sym: nlist_64) bool` |
| `weakRef` | `pub fn weakRef(sym: nlist_64) bool` |
| `discarded` | `pub fn discarded(sym: nlist_64) bool` |
| `tentative` | `pub fn tentative(sym: nlist_64) bool` |
| `cmd` | `pub fn cmd(lc: LoadCommand) LC` |
| `cmdsize` | `pub fn cmdsize(lc: LoadCommand) u32` |
| `cast` | `pub fn cast(lc: LoadCommand, comptime Cmd: type) ?Cmd` |
| `getSections` | `pub fn getSections(lc: LoadCommand) []const section_64` |
| `getDylibPathName` | `pub fn getDylibPathName(lc: LoadCommand) []const u8` |
| `getRpathPathName` | `pub fn getRpathPathName(lc: LoadCommand) []const u8` |
| `next` | `pub fn next(it: *LoadCommandIterator) ?LoadCommand` |

## math

| Function | Signature |
|----------|-----------|
| `approxEqAbs` | `pub fn approxEqAbs(comptime T: type, x: T, y: T, tolerance: T) bool` |
| `approxEqRel` | `pub fn approxEqRel(comptime T: type, x: T, y: T, tolerance: T) bool` |
| `doNotOptimizeAway` | `pub fn doNotOptimizeAway(value: anytype) void` |
| `raiseInvalid` | `pub fn raiseInvalid() void` |
| `raiseUnderflow` | `pub fn raiseUnderflow() void` |
| `raiseOverflow` | `pub fn raiseOverflow() void` |
| `raiseInexact` | `pub fn raiseInexact() void` |
| `raiseDivByZero` | `pub fn raiseDivByZero() void` |
| `sin` | `pub inline fn sin(value: anytype) @TypeOf(value)` |
| `cos` | `pub inline fn cos(value: anytype) @TypeOf(value)` |
| `tan` | `pub inline fn tan(value: anytype) @TypeOf(value)` |
| `radiansToDegrees` | `pub fn radiansToDegrees(comptime T: type, angle_in_radians: T) T` |
| `degreesToRadians` | `pub fn degreesToRadians(comptime T: type, angle_in_degrees: T) T` |
| `exp` | `pub inline fn exp(value: anytype) @TypeOf(value)` |
| `exp2` | `pub inline fn exp2(value: anytype) @TypeOf(value)` |
| `Min` | `pub fn Min(comptime A: type, comptime B: type) type` |
| `min` | `pub fn min(x: anytype, y: anytype) Min(@TypeOf(x), @TypeOf(y))` |
| `min3` | `pub fn min3(x: anytype, y: anytype, z: anytype) @TypeOf(x, y, z)` |
| `max` | `pub fn max(x: anytype, y: anytype) @TypeOf(x, y)` |
| `max3` | `pub fn max3(x: anytype, y: anytype, z: anytype) @TypeOf(x, y, z)` |
| `clamp` | `pub fn clamp(val: anytype, lower: anytype, upper: anytype) @TypeOf(val, lower, upper)` |
| `mul` | `pub fn mul(comptime T: type, a: T, b: T) (error` |
| `add` | `pub fn add(comptime T: type, a: T, b: T) (error` |
| `sub` | `pub fn sub(comptime T: type, a: T, b: T) (error` |
| `negate` | `pub fn negate(x: anytype) !@TypeOf(x)` |
| `shlExact` | `pub fn shlExact(comptime T: type, a: T, shift_amt: Log2Int(T)) !T` |
| `shl` | `pub fn shl(comptime T: type, a: T, shift_amt: anytype) T` |
| `shr` | `pub fn shr(comptime T: type, a: T, shift_amt: anytype) T` |
| `rotr` | `pub fn rotr(comptime T: type, x: T, r: anytype) T` |
| `rotl` | `pub fn rotl(comptime T: type, x: T, r: anytype) T` |
| `Log2Int` | `pub fn Log2Int(comptime T: type) type` |
| `Log2IntCeil` | `pub fn Log2IntCeil(comptime T: type) type` |
| `IntFittingRange` | `pub fn IntFittingRange(comptime from: comptime_int, comptime to: comptime_int) type` |
| `absInt` | `pub fn absInt(x: anytype) !@TypeOf(x)` |
| `divTrunc` | `pub fn divTrunc(comptime T: type, numerator: T, denominator: T) !T` |
| `divFloor` | `pub fn divFloor(comptime T: type, numerator: T, denominator: T) !T` |
| `divCeil` | `pub fn divCeil(comptime T: type, numerator: T, denominator: T) !T` |
| `divExact` | `pub fn divExact(comptime T: type, numerator: T, denominator: T) !T` |
| `mod` | `pub fn mod(comptime T: type, numerator: T, denominator: T) !T` |
| `rem` | `pub fn rem(comptime T: type, numerator: T, denominator: T) !T` |
| `fabs` | `pub inline fn fabs(value: anytype) @TypeOf(value)` |
| `absCast` | `pub fn absCast(x: anytype) switch (@typeInfo(@TypeOf(x)))` |
| `negateCast` | `pub fn negateCast(x: anytype) !std.meta.Int(.signed, @bitSizeOf(@TypeOf(x)))` |
| `cast` | `pub fn cast(comptime T: type, x: anytype) ?T` |
| `alignCast` | `pub fn alignCast(comptime alignment: u29, ptr: anytype) AlignCastError!@TypeOf(@alignCast(alignment, ptr))` |
| `isPowerOfTwo` | `pub fn isPowerOfTwo(v: anytype) bool` |
| `round` | `pub inline fn round(value: anytype) @TypeOf(value)` |
| `trunc` | `pub inline fn trunc(value: anytype) @TypeOf(value)` |
| `floor` | `pub inline fn floor(value: anytype) @TypeOf(value)` |
| `floorPowerOfTwo` | `pub fn floorPowerOfTwo(comptime T: type, value: T) T` |
| `ceil` | `pub inline fn ceil(value: anytype) @TypeOf(value)` |
| `ceilPowerOfTwoPromote` | `pub fn ceilPowerOfTwoPromote(comptime T: type, value: T) std.meta.Int(@typeInfo(T).Int.signedness, @typeInfo(T).Int.bits + 1)` |
| `ceilPowerOfTwo` | `pub fn ceilPowerOfTwo(comptime T: type, value: T) (error` |
| `ceilPowerOfTwoAssert` | `pub fn ceilPowerOfTwoAssert(comptime T: type, value: T) T` |
| `log2_int` | `pub fn log2_int(comptime T: type, x: T) Log2Int(T)` |
| `log2_int_ceil` | `pub fn log2_int_ceil(comptime T: type, x: T) Log2IntCeil(T)` |
| `lossyCast` | `pub fn lossyCast(comptime T: type, value: anytype) T` |
| `maxInt` | `pub fn maxInt(comptime T: type) comptime_int` |
| `minInt` | `pub fn minInt(comptime T: type) comptime_int` |
| `mulWide` | `pub fn mulWide(comptime T: type, a: T, b: T) std.meta.Int( @typeInfo(T).Int.signedness, @typeInfo(T).Int.bits * 2, )` |
| `invert` | `pub fn invert(self: Order) Order` |
| `compare` | `pub fn compare(self: Order, op: CompareOperator) bool` |
| `order` | `pub fn order(a: anytype, b: anytype) Order` |
| `compare` | `pub fn compare(a: anytype, op: CompareOperator, b: anytype) bool` |
| `boolMask` | `pub inline fn boolMask(comptime MaskInt: type, value: bool) MaskInt` |
| `comptimeMod` | `pub fn comptimeMod(num: anytype, comptime denom: comptime_int) IntFittingRange(0, denom - 1)` |
| `make_f80` | `pub fn make_f80(repr: F80) f80` |
| `break_f80` | `pub fn break_f80(x: f80) F80` |
| `sign` | `pub inline fn sign(i: anytype) @TypeOf(i)` |

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
| `atan2` | `pub fn atan2(comptime T: type, y: T, x: T) T` |

## math / atanh

| Function | Signature |
|----------|-----------|
| `atanh` | `pub fn atanh(x: anytype) @TypeOf(x)` |

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
| `calcTwosCompLimbCount` | `pub fn calcTwosCompLimbCount(bit_count: usize) usize` |
| `addMulLimbWithCarry` | `pub fn addMulLimbWithCarry(a: Limb, b: Limb, c: Limb, carry: *Limb) Limb` |
| `toConst` | `pub fn toConst(self: Mutable) Const` |
| `eqZero` | `pub fn eqZero(self: Mutable) bool` |
| `toManaged` | `pub fn toManaged(self: Mutable, allocator: Allocator) Managed` |
| `init` | `pub fn init(limbs_buffer: []Limb, value: anytype) Mutable` |
| `copy` | `pub fn copy(self: *Mutable, other: Const) void` |
| `swap` | `pub fn swap(self: *Mutable, other: *Mutable) void` |
| `dump` | `pub fn dump(self: Mutable) void` |
| `clone` | `pub fn clone(other: Mutable, limbs: []Limb) Mutable` |
| `negate` | `pub fn negate(self: *Mutable) void` |
| `abs` | `pub fn abs(self: *Mutable) void` |
| `set` | `pub fn set(self: *Mutable, value: anytype) void` |
| `setString` | `pub fn setString( self: *Mutable, base: u8, value: []const u8, limbs_buffer: []Limb, allocator: ?Allocator, ) error` |
| `setTwosCompIntLimit` | `pub fn setTwosCompIntLimit( r: *Mutable, limit: TwosCompIntLimit, signedness: Signedness, bit_count: usize, ) void` |
| `addScalar` | `pub fn addScalar(r: *Mutable, a: Const, scalar: anytype) void` |
| `add` | `pub fn add(r: *Mutable, a: Const, b: Const) void` |
| `addWrap` | `pub fn addWrap(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) bool` |
| `addSat` | `pub fn addSat(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) void` |
| `sub` | `pub fn sub(r: *Mutable, a: Const, b: Const) void` |
| `subWrap` | `pub fn subWrap(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) bool` |
| `subSat` | `pub fn subSat(r: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize) void` |
| `mul` | `pub fn mul(rma: *Mutable, a: Const, b: Const, limbs_buffer: []Limb, allocator: ?Allocator) void` |
| `mulNoAlias` | `pub fn mulNoAlias(rma: *Mutable, a: Const, b: Const, allocator: ?Allocator) void` |
| `mulWrap` | `pub fn mulWrap( rma: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize, limbs_buffer: []Limb, allocator: ?Allocator, ) void` |
| `mulWrapNoAlias` | `pub fn mulWrapNoAlias( rma: *Mutable, a: Const, b: Const, signedness: Signedness, bit_count: usize, allocator: ?Allocator, ) void` |
| `bitReverse` | `pub fn bitReverse(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `byteSwap` | `pub fn byteSwap(r: *Mutable, a: Const, signedness: Signedness, byte_count: usize) void` |
| `popCount` | `pub fn popCount(r: *Mutable, a: Const, bit_count: usize) void` |
| `sqrNoAlias` | `pub fn sqrNoAlias(rma: *Mutable, a: Const, opt_allocator: ?Allocator) void` |
| `divFloor` | `pub fn divFloor( q: *Mutable, r: *Mutable, a: Const, b: Const, limbs_buffer: []Limb, ) void` |
| `divTrunc` | `pub fn divTrunc( q: *Mutable, r: *Mutable, a: Const, b: Const, limbs_buffer: []Limb, ) void` |
| `shiftLeft` | `pub fn shiftLeft(r: *Mutable, a: Const, shift: usize) void` |
| `shiftLeftSat` | `pub fn shiftLeftSat(r: *Mutable, a: Const, shift: usize, signedness: Signedness, bit_count: usize) void` |
| `shiftRight` | `pub fn shiftRight(r: *Mutable, a: Const, shift: usize) void` |
| `bitNotWrap` | `pub fn bitNotWrap(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `bitOr` | `pub fn bitOr(r: *Mutable, a: Const, b: Const) void` |
| `bitAnd` | `pub fn bitAnd(r: *Mutable, a: Const, b: Const) void` |
| `bitXor` | `pub fn bitXor(r: *Mutable, a: Const, b: Const) void` |
| `gcd` | `pub fn gcd(rma: *Mutable, x: Const, y: Const, limbs_buffer: *std.ArrayList(Limb)) !void` |
| `pow` | `pub fn pow(r: *Mutable, a: Const, b: u32, limbs_buffer: []Limb) !void` |
| `gcdNoAlias` | `pub fn gcdNoAlias(rma: *Mutable, x: Const, y: Const, limbs_buffer: *std.ArrayList(Limb)) !void` |
| `truncate` | `pub fn truncate(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `saturate` | `pub fn saturate(r: *Mutable, a: Const, signedness: Signedness, bit_count: usize) void` |
| `readTwosComplement` | `pub fn readTwosComplement( x: *Mutable, buffer: []const u8, bit_count: usize, endian: Endian, signedness: Signedness, ) void` |
| `readPackedTwosComplement` | `pub fn readPackedTwosComplement( x: *Mutable, bytes: []const u8, bit_offset: usize, bit_count: usize, endian: Endian, signedness: Signedness, ) void` |
| `normalize` | `pub fn normalize(r: *Mutable, length: usize) void` |
| `toManaged` | `pub fn toManaged(self: Const, allocator: Allocator) Allocator.Error!Managed` |
| `toMutable` | `pub fn toMutable(self: Const, limbs: []Limb) Mutable` |
| `dump` | `pub fn dump(self: Const) void` |
| `abs` | `pub fn abs(self: Const) Const` |
| `negate` | `pub fn negate(self: Const) Const` |
| `isOdd` | `pub fn isOdd(self: Const) bool` |
| `isEven` | `pub fn isEven(self: Const) bool` |
| `bitCountAbs` | `pub fn bitCountAbs(self: Const) usize` |
| `bitCountTwosComp` | `pub fn bitCountTwosComp(self: Const) usize` |
| `fitsInTwosComp` | `pub fn fitsInTwosComp(self: Const, signedness: Signedness, bit_count: usize) bool` |
| `fits` | `pub fn fits(self: Const, comptime T: type) bool` |
| `sizeInBaseUpperBound` | `pub fn sizeInBaseUpperBound(self: Const, base: usize) usize` |
| `to` | `pub fn to(self: Const, comptime T: type) ConvertError!T` |
| `format` | `pub fn format( self: Const, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `toStringAlloc` | `pub fn toStringAlloc(self: Const, allocator: Allocator, base: u8, case: std.fmt.Case) Allocator.Error![]u8` |
| `toString` | `pub fn toString(self: Const, string: []u8, base: u8, case: std.fmt.Case, limbs_buffer: []Limb) usize` |
| `writeTwosComplement` | `pub fn writeTwosComplement(x: Const, buffer: []u8, endian: Endian) void` |
| `writePackedTwosComplement` | `pub fn writePackedTwosComplement(x: Const, bytes: []u8, bit_offset: usize, bit_count: usize, endian: Endian) void` |
| `orderAbs` | `pub fn orderAbs(a: Const, b: Const) math.Order` |
| `order` | `pub fn order(a: Const, b: Const) math.Order` |
| `orderAgainstScalar` | `pub fn orderAgainstScalar(lhs: Const, scalar: anytype) math.Order` |
| `eqZero` | `pub fn eqZero(a: Const) bool` |
| `eqAbs` | `pub fn eqAbs(a: Const, b: Const) bool` |
| `eq` | `pub fn eq(a: Const, b: Const) bool` |
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
| `to` | `pub fn to(self: Managed, comptime T: type) ConvertError!T` |
| `setString` | `pub fn setString(self: *Managed, base: u8, value: []const u8) !void` |
| `setTwosCompIntLimit` | `pub fn setTwosCompIntLimit( r: *Managed, limit: TwosCompIntLimit, signedness: Signedness, bit_count: usize, ) !void` |
| `toString` | `pub fn toString(self: Managed, allocator: Allocator, base: u8, case: std.fmt.Case) ![]u8` |
| `format` | `pub fn format( self: Managed, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `orderAbs` | `pub fn orderAbs(a: Managed, b: Managed) math.Order` |
| `order` | `pub fn order(a: Managed, b: Managed) math.Order` |
| `eqZero` | `pub fn eqZero(a: Managed) bool` |
| `eqAbs` | `pub fn eqAbs(a: Managed, b: Managed) bool` |
| `eq` | `pub fn eq(a: Managed, b: Managed) bool` |
| `normalize` | `pub fn normalize(r: *Managed, length: usize) void` |
| `addScalar` | `pub fn addScalar(r: *Managed, a: *const Managed, scalar: anytype) Allocator.Error!void` |
| `add` | `pub fn add(r: *Managed, a: *const Managed, b: *const Managed) Allocator.Error!void` |
| `addWrap` | `pub fn addWrap( r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize, ) Allocator.Error!bool` |
| `addSat` | `pub fn addSat(r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize) Allocator.Error!void` |
| `sub` | `pub fn sub(r: *Managed, a: *const Managed, b: *const Managed) !void` |
| `subWrap` | `pub fn subWrap( r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize, ) Allocator.Error!bool` |
| `subSat` | `pub fn subSat( r: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize, ) Allocator.Error!void` |
| `mul` | `pub fn mul(rma: *Managed, a: *const Managed, b: *const Managed) !void` |
| `mulWrap` | `pub fn mulWrap( rma: *Managed, a: *const Managed, b: *const Managed, signedness: Signedness, bit_count: usize, ) !void` |
| `ensureTwosCompCapacity` | `pub fn ensureTwosCompCapacity(r: *Managed, bit_count: usize) !void` |
| `ensureAddScalarCapacity` | `pub fn ensureAddScalarCapacity(r: *Managed, a: Const, scalar: anytype) !void` |
| `ensureAddCapacity` | `pub fn ensureAddCapacity(r: *Managed, a: Const, b: Const) !void` |
| `ensureMulCapacity` | `pub fn ensureMulCapacity(rma: *Managed, a: Const, b: Const) !void` |
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
| `truncate` | `pub fn truncate(r: *Managed, a: *const Managed, signedness: Signedness, bit_count: usize) !void` |
| `saturate` | `pub fn saturate(r: *Managed, a: *const Managed, signedness: Signedness, bit_count: usize) !void` |
| `popCount` | `pub fn popCount(r: *Managed, a: *const Managed, bit_count: usize) !void` |
| `llcmp` | `pub fn llcmp(a: []const Limb, b: []const Limb) i8` |

## math / big / rational

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(a: Allocator) !Rational` |
| `deinit` | `pub fn deinit(self: *Rational) void` |
| `setInt` | `pub fn setInt(self: *Rational, a: anytype) !void` |
| `setFloatString` | `pub fn setFloatString(self: *Rational, str: []const u8) !void` |
| `setFloat` | `pub fn setFloat(self: *Rational, comptime T: type, f: T) !void` |
| `toFloat` | `pub fn toFloat(self: Rational, comptime T: type) !T` |
| `setRatio` | `pub fn setRatio(self: *Rational, p: anytype, q: anytype) !void` |
| `copyInt` | `pub fn copyInt(self: *Rational, a: Int) !void` |
| `copyRatio` | `pub fn copyRatio(self: *Rational, a: Int, b: Int) !void` |
| `abs` | `pub fn abs(r: *Rational) void` |
| `negate` | `pub fn negate(r: *Rational) void` |
| `swap` | `pub fn swap(r: *Rational, other: *Rational) void` |
| `order` | `pub fn order(a: Rational, b: Rational) !math.Order` |
| `orderAbs` | `pub fn orderAbs(a: Rational, b: Rational) !math.Order` |
| `add` | `pub fn add(rma: *Rational, a: Rational, b: Rational) !void` |
| `sub` | `pub fn sub(rma: *Rational, a: Rational, b: Rational) !void` |
| `mul` | `pub fn mul(r: *Rational, a: Rational, b: Rational) !void` |
| `div` | `pub fn div(r: *Rational, a: Rational, b: Rational) !void` |
| `invert` | `pub fn invert(r: *Rational) void` |

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

## math / complex / abs

| Function | Signature |
|----------|-----------|
| `abs` | `pub fn abs(z: anytype) @TypeOf(z.re)` |

## math / complex / acos

| Function | Signature |
|----------|-----------|
| `acos` | `pub fn acos(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / acosh

| Function | Signature |
|----------|-----------|
| `acosh` | `pub fn acosh(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / arg

| Function | Signature |
|----------|-----------|
| `arg` | `pub fn arg(z: anytype) @TypeOf(z.re)` |

## math / complex / asin

| Function | Signature |
|----------|-----------|
| `asin` | `pub fn asin(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / asinh

| Function | Signature |
|----------|-----------|
| `asinh` | `pub fn asinh(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / atan

| Function | Signature |
|----------|-----------|
| `atan` | `pub fn atan(z: anytype) @TypeOf(z)` |

## math / complex / atanh

| Function | Signature |
|----------|-----------|
| `atanh` | `pub fn atanh(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / conj

| Function | Signature |
|----------|-----------|
| `conj` | `pub fn conj(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / cos

| Function | Signature |
|----------|-----------|
| `cos` | `pub fn cos(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / cosh

| Function | Signature |
|----------|-----------|
| `cosh` | `pub fn cosh(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / exp

| Function | Signature |
|----------|-----------|
| `exp` | `pub fn exp(z: anytype) @TypeOf(z)` |

## math / complex / ldexp

| Function | Signature |
|----------|-----------|
| `ldexp_cexp` | `pub fn ldexp_cexp(z: anytype, expt: i32) @TypeOf(z)` |

## math / complex / log

| Function | Signature |
|----------|-----------|
| `log` | `pub fn log(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / pow

| Function | Signature |
|----------|-----------|
| `pow` | `pub fn pow(comptime T: type, z: T, c: T) T` |

## math / complex / proj

| Function | Signature |
|----------|-----------|
| `proj` | `pub fn proj(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / sin

| Function | Signature |
|----------|-----------|
| `sin` | `pub fn sin(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / sinh

| Function | Signature |
|----------|-----------|
| `sinh` | `pub fn sinh(z: anytype) @TypeOf(z)` |

## math / complex / sqrt

| Function | Signature |
|----------|-----------|
| `sqrt` | `pub fn sqrt(z: anytype) @TypeOf(z)` |

## math / complex / tan

| Function | Signature |
|----------|-----------|
| `tan` | `pub fn tan(z: anytype) Complex(@TypeOf(z.re))` |

## math / complex / tanh

| Function | Signature |
|----------|-----------|
| `tanh` | `pub fn tanh(z: anytype) @TypeOf(z)` |

## math / copysign

| Function | Signature |
|----------|-----------|
| `copysign` | `pub fn copysign(magnitude: anytype, sign: @TypeOf(magnitude)) @TypeOf(magnitude)` |

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
| `floatExponentBits` | `pub inline fn floatExponentBits(comptime T: type) comptime_int` |
| `floatMantissaBits` | `pub inline fn floatMantissaBits(comptime T: type) comptime_int` |
| `floatFractionalBits` | `pub inline fn floatFractionalBits(comptime T: type) comptime_int` |
| `floatExponentMin` | `pub inline fn floatExponentMin(comptime T: type) comptime_int` |
| `floatExponentMax` | `pub inline fn floatExponentMax(comptime T: type) comptime_int` |
| `floatTrueMin` | `pub inline fn floatTrueMin(comptime T: type) T` |
| `floatMin` | `pub inline fn floatMin(comptime T: type) T` |
| `floatMax` | `pub inline fn floatMax(comptime T: type) T` |
| `floatEps` | `pub inline fn floatEps(comptime T: type) T` |
| `inf` | `pub inline fn inf(comptime T: type) T` |

## math / frexp

| Function | Signature |
|----------|-----------|
| `Frexp` | `pub fn Frexp(comptime T: type) type` |
| `frexp` | `pub fn frexp(x: anytype) Frexp(@TypeOf(x))` |

## math / gcd

| Function | Signature |
|----------|-----------|
| `gcd` | `pub fn gcd(a: anytype, b: anytype) @TypeOf(a, b)` |

## math / hypot

| Function | Signature |
|----------|-----------|
| `hypot` | `pub fn hypot(comptime T: type, x: T, y: T) T` |

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
| `isInf` | `pub inline fn isInf(x: anytype) bool` |
| `isPositiveInf` | `pub inline fn isPositiveInf(x: anytype) bool` |
| `isNegativeInf` | `pub inline fn isNegativeInf(x: anytype) bool` |

## math / isnan

| Function | Signature |
|----------|-----------|
| `isNan` | `pub fn isNan(x: anytype) bool` |
| `isSignalNan` | `pub fn isSignalNan(x: anytype) bool` |

## math / isnormal

| Function | Signature |
|----------|-----------|
| `isNormal` | `pub fn isNormal(x: anytype) bool` |

## math / ldexp

| Function | Signature |
|----------|-----------|
| `ldexp` | `pub fn ldexp(x: anytype, n: i32) @TypeOf(x)` |

## math / ln

| Function | Signature |
|----------|-----------|
| `ln` | `pub fn ln(x: anytype) @TypeOf(x)` |

## math / log

| Function | Signature |
|----------|-----------|
| `log` | `pub fn log(comptime T: type, base: T, x: T) T` |

## math / log10

| Function | Signature |
|----------|-----------|
| `log10` | `pub fn log10(x: anytype) @TypeOf(x)` |

## math / log1p

| Function | Signature |
|----------|-----------|
| `log1p` | `pub fn log1p(x: anytype) @TypeOf(x)` |

## math / log2

| Function | Signature |
|----------|-----------|
| `log2` | `pub fn log2(x: anytype) @TypeOf(x)` |

## math / modf

| Function | Signature |
|----------|-----------|
| `modf` | `pub fn modf(x: anytype) modf_result(@TypeOf(x))` |

## math / nan

| Function | Signature |
|----------|-----------|
| `nan` | `pub inline fn nan(comptime T: type) T` |
| `snan` | `pub inline fn snan(comptime T: type) T` |

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

## mem

| Function | Signature |
|----------|-----------|
| `ValidationAllocator` | `pub fn ValidationAllocator(comptime T: type) type` |
| `init` | `pub fn init(underlying_allocator: T) @This()` |
| `allocator` | `pub fn allocator(self: *Self) Allocator` |
| `alloc` | `pub fn alloc( self: *Self, n: usize, ptr_align: u29, len_align: u29, ret_addr: usize, ) Allocator.Error![]u8` |
| `resize` | `pub fn resize( self: *Self, buf: []u8, buf_align: u29, new_len: usize, len_align: u29, ret_addr: usize, ) ?usize` |
| `free` | `pub fn free( self: *Self, buf: []u8, buf_align: u29, ret_addr: usize, ) void` |
| `reset` | `pub fn reset(self: *Self) void` |
| `validationWrap` | `pub fn validationWrap(allocator: anytype) ValidationAllocator(@TypeOf(allocator))` |
| `alignAllocLen` | `pub fn alignAllocLen(full_len: usize, alloc_len: usize, len_align: u29) usize` |
| `copy` | `pub fn copy(comptime T: type, dest: []T, source: []const T) void` |
| `copyBackwards` | `pub fn copyBackwards(comptime T: type, dest: []T, source: []const T) void` |
| `set` | `pub fn set(comptime T: type, dest: []T, value: T) void` |
| `zeroes` | `pub fn zeroes(comptime T: type) T` |
| `zeroInit` | `pub fn zeroInit(comptime T: type, init: anytype) T` |
| `order` | `pub fn order(comptime T: type, lhs: []const T, rhs: []const T) math.Order` |
| `lessThan` | `pub fn lessThan(comptime T: type, lhs: []const T, rhs: []const T) bool` |
| `eql` | `pub fn eql(comptime T: type, a: []const T, b: []const T) bool` |
| `indexOfDiff` | `pub fn indexOfDiff(comptime T: type, a: []const T, b: []const T) ?usize` |
| `Span` | `pub fn Span(comptime T: type) type` |
| `span` | `pub fn span(ptr: anytype) Span(@TypeOf(ptr))` |
| `sliceTo` | `pub fn sliceTo(ptr: anytype, comptime end: meta.Elem(@TypeOf(ptr))) SliceTo(@TypeOf(ptr), end)` |
| `len` | `pub fn len(value: anytype) usize` |
| `indexOfSentinel` | `pub fn indexOfSentinel(comptime Elem: type, comptime sentinel: Elem, ptr: [*:sentinel]const Elem) usize` |
| `allEqual` | `pub fn allEqual(comptime T: type, slice: []const T, scalar: T) bool` |
| `trimLeft` | `pub fn trimLeft(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `trimRight` | `pub fn trimRight(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `trim` | `pub fn trim(comptime T: type, slice: []const T, values_to_strip: []const T) []const T` |
| `indexOfScalar` | `pub fn indexOfScalar(comptime T: type, slice: []const T, value: T) ?usize` |
| `lastIndexOfScalar` | `pub fn lastIndexOfScalar(comptime T: type, slice: []const T, value: T) ?usize` |
| `indexOfScalarPos` | `pub fn indexOfScalarPos(comptime T: type, slice: []const T, start_index: usize, value: T) ?usize` |
| `indexOfAny` | `pub fn indexOfAny(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `lastIndexOfAny` | `pub fn lastIndexOfAny(comptime T: type, slice: []const T, values: []const T) ?usize` |
| `indexOfAnyPos` | `pub fn indexOfAnyPos(comptime T: type, slice: []const T, start_index: usize, values: []const T) ?usize` |
| `indexOf` | `pub fn indexOf(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `lastIndexOfLinear` | `pub fn lastIndexOfLinear(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `indexOfPosLinear` | `pub fn indexOfPosLinear(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize` |
| `lastIndexOf` | `pub fn lastIndexOf(comptime T: type, haystack: []const T, needle: []const T) ?usize` |
| `indexOfPos` | `pub fn indexOfPos(comptime T: type, haystack: []const T, start_index: usize, needle: []const T) ?usize` |
| `count` | `pub fn count(comptime T: type, haystack: []const T, needle: []const T) usize` |
| `containsAtLeast` | `pub fn containsAtLeast(comptime T: type, haystack: []const T, expected_count: usize, needle: []const T) bool` |
| `readVarInt` | `pub fn readVarInt(comptime ReturnType: type, bytes: []const u8, endian: Endian) ReturnType` |
| `readVarPackedInt` | `pub fn readVarPackedInt( comptime T: type, bytes: []const u8, bit_offset: usize, bit_count: usize, endian: std.builtin.Endian, signedness: std.builtin.Signedness, ) T` |
| `readIntNative` | `pub fn readIntNative(comptime T: type, bytes: *const [@divExact(@typeInfo(T).Int.bits, 8)]u8) T` |
| `readIntForeign` | `pub fn readIntForeign(comptime T: type, bytes: *const [@divExact(@typeInfo(T).Int.bits, 8)]u8) T` |
| `readIntSliceNative` | `pub fn readIntSliceNative(comptime T: type, bytes: []const u8) T` |
| `readIntSliceForeign` | `pub fn readIntSliceForeign(comptime T: type, bytes: []const u8) T` |
| `readInt` | `pub fn readInt(comptime T: type, bytes: *const [@divExact(@typeInfo(T).Int.bits, 8)]u8, endian: Endian) T` |
| `readPackedInt` | `pub fn readPackedInt(comptime T: type, bytes: []const u8, bit_offset: usize, endian: Endian) T` |
| `readIntSlice` | `pub fn readIntSlice(comptime T: type, bytes: []const u8, endian: Endian) T` |
| `writeIntNative` | `pub fn writeIntNative(comptime T: type, buf: *[(@typeInfo(T).Int.bits + 7) / 8]u8, value: T) void` |
| `writeIntForeign` | `pub fn writeIntForeign(comptime T: type, buf: *[@divExact(@typeInfo(T).Int.bits, 8)]u8, value: T) void` |
| `writeInt` | `pub fn writeInt(comptime T: type, buffer: *[@divExact(@typeInfo(T).Int.bits, 8)]u8, value: T, endian: Endian) void` |
| `writePackedIntLittle` | `pub fn writePackedIntLittle(comptime T: type, bytes: []u8, bit_offset: usize, value: T) void` |
| `writePackedIntBig` | `pub fn writePackedIntBig(comptime T: type, bytes: []u8, bit_offset: usize, value: T) void` |
| `writePackedInt` | `pub fn writePackedInt(comptime T: type, bytes: []u8, bit_offset: usize, value: T, endian: Endian) void` |
| `writeIntSliceLittle` | `pub fn writeIntSliceLittle(comptime T: type, buffer: []u8, value: T) void` |
| `writeIntSliceBig` | `pub fn writeIntSliceBig(comptime T: type, buffer: []u8, value: T) void` |
| `writeIntSlice` | `pub fn writeIntSlice(comptime T: type, buffer: []u8, value: T, endian: Endian) void` |
| `writeVarPackedInt` | `pub fn writeVarPackedInt(bytes: []u8, bit_offset: usize, bit_count: usize, value: anytype, endian: std.builtin.Endian) void` |
| `byteSwapAllFields` | `pub fn byteSwapAllFields(comptime S: type, ptr: *S) void` |
| `tokenize` | `pub fn tokenize(comptime T: type, buffer: []const T, delimiter_bytes: []const T) TokenIterator(T)` |
| `split` | `pub fn split(comptime T: type, buffer: []const T, delimiter: []const T) SplitIterator(T)` |
| `splitBackwards` | `pub fn splitBackwards(comptime T: type, buffer: []const T, delimiter: []const T) SplitBackwardsIterator(T)` |
| `startsWith` | `pub fn startsWith(comptime T: type, haystack: []const T, needle: []const T) bool` |
| `endsWith` | `pub fn endsWith(comptime T: type, haystack: []const T, needle: []const T) bool` |
| `TokenIterator` | `pub fn TokenIterator(comptime T: type) type` |
| `next` | `pub fn next(self: *Self) ?[]const T` |
| `peek` | `pub fn peek(self: *Self) ?[]const T` |
| `rest` | `pub fn rest(self: Self) []const T` |
| `reset` | `pub fn reset(self: *Self) void` |
| `SplitIterator` | `pub fn SplitIterator(comptime T: type) type` |
| `first` | `pub fn first(self: *Self) []const T` |
| `next` | `pub fn next(self: *Self) ?[]const T` |
| `rest` | `pub fn rest(self: Self) []const T` |
| `reset` | `pub fn reset(self: *Self) void` |
| `SplitBackwardsIterator` | `pub fn SplitBackwardsIterator(comptime T: type) type` |
| `first` | `pub fn first(self: *Self) []const T` |
| `next` | `pub fn next(self: *Self) ?[]const T` |
| `rest` | `pub fn rest(self: Self) []const T` |
| `reset` | `pub fn reset(self: *Self) void` |
| `join` | `pub fn join(allocator: Allocator, separator: []const u8, slices: []const []const u8) ![]u8` |
| `joinZ` | `pub fn joinZ(allocator: Allocator, separator: []const u8, slices: []const []const u8) ![:0]u8` |
| `concat` | `pub fn concat(allocator: Allocator, comptime T: type, slices: []const []const T) ![]T` |
| `concatWithSentinel` | `pub fn concatWithSentinel(allocator: Allocator, comptime T: type, slices: []const []const T, comptime s: T) ![:s]T` |
| `concatMaybeSentinel` | `pub fn concatMaybeSentinel(allocator: Allocator, comptime T: type, slices: []const []const T, comptime s: ?T) ![]T` |
| `min` | `pub fn min(comptime T: type, slice: []const T) T` |
| `max` | `pub fn max(comptime T: type, slice: []const T) T` |
| `minMax` | `pub fn minMax(comptime T: type, slice: []const T) struct` |
| `indexOfMin` | `pub fn indexOfMin(comptime T: type, slice: []const T) usize` |
| `indexOfMax` | `pub fn indexOfMax(comptime T: type, slice: []const T) usize` |
| `indexOfMinMax` | `pub fn indexOfMinMax(comptime T: type, slice: []const T) struct` |
| `swap` | `pub fn swap(comptime T: type, a: *T, b: *T) void` |
| `reverse` | `pub fn reverse(comptime T: type, items: []T) void` |
| `rotate` | `pub fn rotate(comptime T: type, items: []T, amount: usize) void` |
| `replace` | `pub fn replace(comptime T: type, input: []const T, needle: []const T, replacement: []const T, output: []T) usize` |
| `replaceScalar` | `pub fn replaceScalar(comptime T: type, slice: []T, needle: T, replacement: T) void` |
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
| `alignPointerOffset` | `pub fn alignPointerOffset(ptr: anytype, align_to: u29) ?usize` |
| `alignPointer` | `pub fn alignPointer(ptr: anytype, align_to: u29) ?@TypeOf(ptr)` |
| `asBytes` | `pub fn asBytes(ptr: anytype) AsBytesReturnType(@TypeOf(ptr))` |
| `toBytes` | `pub fn toBytes(value: anytype) [@sizeOf(@TypeOf(value))]u8` |
| `bytesAsValue` | `pub fn bytesAsValue(comptime T: type, bytes: anytype) BytesAsValueReturnType(T, @TypeOf(bytes))` |
| `bytesToValue` | `pub fn bytesToValue(comptime T: type, bytes: anytype) T` |
| `bytesAsSlice` | `pub fn bytesAsSlice(comptime T: type, bytes: anytype) BytesAsSliceReturnType(T, @TypeOf(bytes))` |
| `sliceAsBytes` | `pub fn sliceAsBytes(slice: anytype) SliceAsBytesReturnType(@TypeOf(slice))` |
| `alignForward` | `pub fn alignForward(addr: usize, alignment: usize) usize` |
| `alignForwardGeneric` | `pub fn alignForwardGeneric(comptime T: type, addr: T, alignment: T) T` |
| `doNotOptimizeAway` | `pub fn doNotOptimizeAway(val: anytype) void` |
| `alignBackwardAnyAlign` | `pub fn alignBackwardAnyAlign(i: usize, alignment: usize) usize` |
| `alignBackward` | `pub fn alignBackward(addr: usize, alignment: usize) usize` |
| `alignBackwardGeneric` | `pub fn alignBackwardGeneric(comptime T: type, addr: T, alignment: T) T` |
| `isValidAlign` | `pub fn isValidAlign(alignment: u29) bool` |
| `isAlignedAnyAlign` | `pub fn isAlignedAnyAlign(i: usize, alignment: usize) bool` |
| `isAligned` | `pub fn isAligned(addr: usize, alignment: usize) bool` |
| `isAlignedGeneric` | `pub fn isAlignedGeneric(comptime T: type, addr: T, alignment: T) bool` |
| `alignInBytes` | `pub fn alignInBytes(bytes: []u8, comptime new_alignment: usize) ?[]align(new_alignment) u8` |
| `alignInSlice` | `pub fn alignInSlice(slice: anytype, comptime new_alignment: usize) ?AlignedSlice(@TypeOf(slice), new_alignment)` |

## mem / Allocator

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init( pointer: anytype, comptime allocFn: fn (ptr: @TypeOf(pointer), len: usize, ptr_align: u29, len_align: u29, ret_addr: usize) Error![]u8, comptime resizeFn: fn (ptr: @TypeOf(pointer), buf: []u8, buf_align: u29, new_len: usize, len_align: u29, ret_addr: usize) ?usize, comptime freeFn: fn (ptr: @TypeOf(pointer), buf: []u8, buf_align: u29, ret_addr: usize) void, ) Allocator` |
| `NoResize` | `pub fn NoResize(comptime AllocatorType: type) type` |
| `noResize` | `pub fn noResize( self: *AllocatorType, buf: []u8, buf_align: u29, new_len: usize, len_align: u29, ret_addr: usize, ) ?usize` |
| `NoOpFree` | `pub fn NoOpFree(comptime AllocatorType: type) type` |
| `noOpFree` | `pub fn noOpFree( self: *AllocatorType, buf: []u8, buf_align: u29, ret_addr: usize, ) void` |
| `PanicFree` | `pub fn PanicFree(comptime AllocatorType: type) type` |
| `panicFree` | `pub fn panicFree( self: *AllocatorType, buf: []u8, buf_align: u29, ret_addr: usize, ) void` |
| `rawAlloc` | `pub inline fn rawAlloc(self: Allocator, len: usize, ptr_align: u29, len_align: u29, ret_addr: usize) Error![]u8` |
| `rawResize` | `pub inline fn rawResize(self: Allocator, buf: []u8, buf_align: u29, new_len: usize, len_align: u29, ret_addr: usize) ?usize` |
| `rawFree` | `pub inline fn rawFree(self: Allocator, buf: []u8, buf_align: u29, ret_addr: usize) void` |
| `create` | `pub fn create(self: Allocator, comptime T: type) Error!*T` |
| `destroy` | `pub fn destroy(self: Allocator, ptr: anytype) void` |
| `alloc` | `pub fn alloc(self: Allocator, comptime T: type, n: usize) Error![]T` |
| `allocWithOptions` | `pub fn allocWithOptions( self: Allocator, comptime Elem: type, n: usize, /// null means naturally aligned comptime optional_alignment: ?u29, comptime optional_sentinel: ?Elem, ) Error!AllocWithOptionsPayload(Elem, optional_alignment, optional_sentinel)` |
| `allocWithOptionsRetAddr` | `pub fn allocWithOptionsRetAddr( self: Allocator, comptime Elem: type, n: usize, /// null means naturally aligned comptime optional_alignment: ?u29, comptime optional_sentinel: ?Elem, return_address: usize, ) Error!AllocWithOptionsPayload(Elem, optional_alignment, optional_sentinel)` |
| `allocSentinel` | `pub fn allocSentinel( self: Allocator, comptime Elem: type, n: usize, comptime sentinel: Elem, ) Error![:sentinel]Elem` |
| `alignedAlloc` | `pub fn alignedAlloc( self: Allocator, comptime T: type, /// null means naturally aligned comptime alignment: ?u29, n: usize, ) Error![]align(alignment orelse @alignOf(T)) T` |
| `allocAdvanced` | `pub fn allocAdvanced( self: Allocator, comptime T: type, /// null means naturally aligned comptime alignment: ?u29, n: usize, exact: Exact, ) Error![]align(alignment orelse @alignOf(T)) T` |
| `allocAdvancedWithRetAddr` | `pub fn allocAdvancedWithRetAddr( self: Allocator, comptime T: type, /// null means naturally aligned comptime alignment: ?u29, n: usize, exact: Exact, return_address: usize, ) Error![]align(alignment orelse @alignOf(T)) T` |
| `resize` | `pub fn resize(self: Allocator, old_mem: anytype, new_n: usize) ?@TypeOf(old_mem)` |
| `realloc` | `pub fn realloc(self: Allocator, old_mem: anytype, new_n: usize) t:` |
| `reallocAtLeast` | `pub fn reallocAtLeast(self: Allocator, old_mem: anytype, new_n: usize) t:` |
| `reallocAdvanced` | `pub fn reallocAdvanced( self: Allocator, old_mem: anytype, comptime new_alignment: u29, new_n: usize, exact: Exact, ) Error![]align(new_alignment) @typeInfo(@TypeOf(old_mem)).Pointer.child` |
| `reallocAdvancedWithRetAddr` | `pub fn reallocAdvancedWithRetAddr( self: Allocator, old_mem: anytype, comptime new_alignment: u29, new_n: usize, exact: Exact, return_address: usize, ) Error![]align(new_alignment) @typeInfo(@TypeOf(old_mem)).Pointer.child` |
| `shrink` | `pub fn shrink(self: Allocator, old_mem: anytype, new_n: usize) t:` |
| `alignedShrink` | `pub fn alignedShrink( self: Allocator, old_mem: anytype, comptime new_alignment: u29, new_n: usize, ) []align(new_alignment) @typeInfo(@TypeOf(old_mem)).Pointer.child` |
| `alignedShrinkWithRetAddr` | `pub fn alignedShrinkWithRetAddr( self: Allocator, old_mem: anytype, comptime new_alignment: u29, new_n: usize, return_address: usize, ) []align(new_alignment) @typeInfo(@TypeOf(old_mem)).Pointer.child` |
| `free` | `pub fn free(self: Allocator, memory: anytype) void` |
| `dupe` | `pub fn dupe(allocator: Allocator, comptime T: type, m: []const T) ![]T` |
| `dupeZ` | `pub fn dupeZ(allocator: Allocator, comptime T: type, m: []const T) ![:0]T` |
| `allocBytes` | `pub fn allocBytes( self: Allocator, /// Must be >= 1. /// Must be a power of 2. /// Returned slice's pointer will have this alignment. alignment: u29, byte_count: usize, /// 0 indicates the length of the slice returned MUST match `byte_count` exactly /// non-zero means the length of the returned slice must be aligned by `len_align` /// `byte_count` must be aligned by `len_align` len_align: u29, return_address: usize, ) Error![]u8 { const new_mem = try self.rawAlloc(byte_count, alignment, len_align, return_address); // TODO: https://github.com/ziglang/zig/issues/4298 @memset(new_mem.ptr, undefined, new_mem.len); return new_mem; } test "allocBytes" { const number_of_bytes: usize = 10; var runtime_alignment: u29 = 2; { const new_mem = try std.testing.allocator.allocBytes(runtime_alignment, number_of_bytes, 0, @returnAddress()); defer std.testing.allocator.free(new_mem); try std.testing.expectEqual(number_of_bytes, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } runtime_alignment = 8; { const new_mem = try std.testing.allocator.allocBytes(runtime_alignment, number_of_bytes, 0, @returnAddress()); defer std.testing.allocator.free(new_mem); try std.testing.expectEqual(number_of_bytes, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } } test "allocBytes non-zero len_align" { const number_of_bytes: usize = 10; var runtime_alignment: u29 = 1; var len_align: u29 = 2; { const new_mem = try std.testing.allocator.allocBytes(runtime_alignment, number_of_bytes, len_align, @returnAddress()); defer std.testing.allocator.free(new_mem); try std.testing.expect(new_mem.len >= number_of_bytes); try std.testing.expect(new_mem.len % len_align == 0); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } runtime_alignment = 16; len_align = 5; { const new_mem = try std.testing.allocator.allocBytes(runtime_alignment, number_of_bytes, len_align, @returnAddress()); defer std.testing.allocator.free(new_mem); try std.testing.expect(new_mem.len >= number_of_bytes); try std.testing.expect(new_mem.len % len_align == 0); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } } /// Realloc is used to modify the size or alignment of an existing allocation, /// as well as to provide the allocator with an opportunity to move an allocation /// to a better location. /// The returned slice will have its pointer aligned at least to `new_alignment` bytes. /// /// This function allows a runtime `alignment` value. Callers should generally prefer /// to call the `realloc*` functions. /// /// If the size/alignment is greater than the previous allocation, and the requested new /// allocation could not be granted this function returns `error.OutOfMemory`. /// When the size/alignment is less than or equal to the previous allocation, /// this function returns `error.OutOfMemory` when the allocator decides the client /// would be better off keeping the extra alignment/size. /// Clients will call `resizeFn` when they require the allocator to track a new alignment/size, /// and so this function should only return success when the allocator considers /// the reallocation desirable from the allocator's perspective. /// /// As an example, `std.ArrayList` tracks a "capacity", and therefore can handle /// reallocation failure, even when `new_n` <= `old_mem.len`. A `FixedBufferAllocator` /// would always return `error.OutOfMemory` for `reallocFn` when the size/alignment /// is less than or equal to the old allocation, because it cannot reclaim the memory, /// and thus the `std.ArrayList` would be better off retaining its capacity. pub fn reallocBytes( self: Allocator, /// Must be the same as what was returned from most recent call to `allocFn` or `resizeFn`. /// If `old_mem.len == 0` then this is a new allocation and `new_byte_count` must be >= 1. old_mem: []u8, /// If `old_mem.len == 0` then this is `undefined`, otherwise: /// Must be the same as what was passed to `allocFn`. /// Must be >= 1. /// Must be a power of 2. old_alignment: u29, /// If `new_byte_count` is 0 then this is a free and it is required that `old_mem.len != 0`. new_byte_count: usize, /// Must be >= 1. /// Must be a power of 2. /// Returned slice's pointer will have this alignment. new_alignment: u29, /// 0 indicates the length of the slice returned MUST match `new_byte_count` exactly /// non-zero means the length of the returned slice must be aligned by `len_align` /// `new_byte_count` must be aligned by `len_align` len_align: u29, return_address: usize, ) Error![]u8 { if (old_mem.len == 0) { return self.allocBytes(new_alignment, new_byte_count, len_align, return_address); } if (new_byte_count == 0) { // TODO https://github.com/ziglang/zig/issues/4298 @memset(old_mem.ptr, undefined, old_mem.len); self.rawFree(old_mem, old_alignment, return_address); return &[0]u8{}; } if (mem.isAligned(@ptrToInt(old_mem.ptr), new_alignment)) { if (new_byte_count <= old_mem.len) { const shrunk_len = self.shrinkBytes(old_mem, old_alignment, new_byte_count, len_align, return_address); return old_mem.ptr[0..shrunk_len]; } if (self.rawResize(old_mem, old_alignment, new_byte_count, len_align, return_address)) |resized_len| { assert(resized_len >= new_byte_count); // TODO: https://github.com/ziglang/zig/issues/4298 @memset(old_mem.ptr + new_byte_count, undefined, resized_len - new_byte_count); return old_mem.ptr[0..resized_len]; } } if (new_byte_count <= old_mem.len and new_alignment <= old_alignment) { return error.OutOfMemory; } const new_mem = try self.rawAlloc(new_byte_count, new_alignment, len_align, return_address); @memcpy(new_mem.ptr, old_mem.ptr, math.min(new_byte_count, old_mem.len)); // TODO https://github.com/ziglang/zig/issues/4298 @memset(old_mem.ptr, undefined, old_mem.len); self.rawFree(old_mem, old_alignment, return_address); return new_mem; } test "reallocBytes" { var new_mem: []u8 = &.{}; var new_byte_count: usize = 16; var runtime_alignment: u29 = 4; // `new_mem.len == 0`, this is a new allocation { new_mem = try std.testing.allocator.reallocBytes(new_mem, undefined, new_byte_count, runtime_alignment, 0, @returnAddress()); try std.testing.expectEqual(new_byte_count, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } // `new_byte_count < new_mem.len`, this is a shrink, alignment is unmodified new_byte_count = 14; { new_mem = try std.testing.allocator.reallocBytes(new_mem, runtime_alignment, new_byte_count, runtime_alignment, 0, @returnAddress()); try std.testing.expectEqual(new_byte_count, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } // `new_byte_count < new_mem.len`, this is a shrink, alignment is decreased from 4 to 2 runtime_alignment = 2; new_byte_count = 12; { new_mem = try std.testing.allocator.reallocBytes(new_mem, 4, new_byte_count, runtime_alignment, 0, @returnAddress()); try std.testing.expectEqual(new_byte_count, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } // `new_byte_count > new_mem.len`, this is a growth, alignment is increased from 2 to 8 runtime_alignment = 8; new_byte_count = 32; { new_mem = try std.testing.allocator.reallocBytes(new_mem, 2, new_byte_count, runtime_alignment, 0, @returnAddress()); try std.testing.expectEqual(new_byte_count, new_mem.len); try std.testing.expect(mem.isAligned(@ptrToInt(new_mem.ptr), runtime_alignment)); } // `new_byte_count == 0`, this is a free new_byte_count = 0; { new_mem = try std.testing.allocator.reallocBytes(new_mem, runtime_alignment, new_byte_count, runtime_alignment, 0, @returnAddress()); try std.testing.expectEqual(new_byte_count, new_mem.len); } } /// Call `vtable.resize`, but caller guarantees that `new_len` <= `buf.len` meaning /// than a `null` return value should be impossible. /// This function allows a runtime `buf_align` value. Callers should generally prefer /// to call `shrink`. pub fn shrinkBytes( self: Allocator, /// Must be the same as what was returned from most recent call to `allocFn` or `resizeFn`. buf: []u8, /// Must be the same as what was passed to `allocFn`. /// Must be >= 1. /// Must be a power of 2. buf_align: u29, /// Must be >= 1. new_len: usize, /// 0 indicates the length of the slice returned MUST match `new_len` exactly /// non-zero means the length of the returned slice must be aligned by `len_align` /// `new_len` must be aligned by `len_align` len_align: u29, return_address: usize, ) usize { assert(new_len <= buf.len); return self.rawResize(buf, buf_align, new_len, len_align, return_address) orelse unreachable; }` |

## meta

| Function | Signature |
|----------|-----------|
| `tagName` | `pub fn tagName(v: anytype) []const u8` |
| `isTag` | `pub fn isTag(tagged_value: anytype, comptime tag_name: []const u8) bool` |
| `stringToEnum` | `pub fn stringToEnum(comptime T: type, str: []const u8) ?T` |
| `bitCount` | `pub fn bitCount(comptime T: type) comptime_int` |
| `alignment` | `pub fn alignment(comptime T: type) comptime_int` |
| `Child` | `pub fn Child(comptime T: type) type` |
| `Elem` | `pub fn Elem(comptime T: type) type` |
| `sentinel` | `pub fn sentinel(comptime T: type) ?Elem(T)` |
| `Sentinel` | `pub fn Sentinel(comptime T: type, comptime sentinel_val: Elem(T)) type` |
| `assumeSentinel` | `pub fn assumeSentinel(p: anytype, comptime sentinel_val: Elem(@TypeOf(p))) Sentinel(@TypeOf(p), sentinel_val)` |
| `containerLayout` | `pub fn containerLayout(comptime T: type) Type.ContainerLayout` |
| `declarations` | `pub fn declarations(comptime T: type) []const Type.Declaration` |
| `declarationInfo` | `pub fn declarationInfo(comptime T: type, comptime decl_name: []const u8) Type.Declaration` |
| `fields` | `pub fn fields(comptime T: type) switch (@typeInfo(T))` |
| `fieldInfo` | `pub fn fieldInfo(comptime T: type, comptime field: FieldEnum(T)) switch (@typeInfo(T))` |
| `fieldNames` | `pub fn fieldNames(comptime T: type) *const [fields(T).len][]const u8` |
| `tags` | `pub fn tags(comptime T: type) *const [fields(T).len]T` |
| `FieldEnum` | `pub fn FieldEnum(comptime T: type) type` |
| `DeclEnum` | `pub fn DeclEnum(comptime T: type) type` |
| `Tag` | `pub fn Tag(comptime T: type) type` |
| `activeTag` | `pub fn activeTag(u: anytype) Tag(@TypeOf(u))` |
| `TagPayload` | `pub fn TagPayload(comptime U: type, comptime tag: Tag(U)) type` |
| `eql` | `pub fn eql(a: anytype, b: @TypeOf(a)) bool` |
| `intToEnum` | `pub fn intToEnum(comptime EnumTag: type, tag_int: anytype) IntToEnumError!EnumTag` |
| `fieldIndex` | `pub fn fieldIndex(comptime T: type, comptime name: []const u8) ?comptime_int` |
| `declList` | `pub fn declList(comptime Namespace: type, comptime Decl: type) []const *const Decl` |
| `Int` | `pub fn Int(comptime signedness: std.builtin.Signedness, comptime bit_count: u16) type` |
| `Float` | `pub fn Float(comptime bit_count: u8) type` |
| `Vector` | `pub fn Vector(comptime len: u32, comptime child: type) type` |
| `ArgsTuple` | `pub fn ArgsTuple(comptime Function: type) type` |
| `Tuple` | `pub fn Tuple(comptime types: []const type) type` |
| `globalOption` | `pub fn globalOption(comptime name: []const u8, comptime T: type) ?T` |
| `isError` | `pub fn isError(error_union: anytype) bool` |
| `FnPtr` | `pub fn FnPtr(comptime Fn: type) type` |

## meta / trailer_flags

| Function | Signature |
|----------|-----------|
| `TrailerFlags` | `pub fn TrailerFlags(comptime Fields: type) type` |
| `has` | `pub fn has(self: Self, comptime field: FieldEnum) bool` |
| `get` | `pub fn get(self: Self, p: [*]align(@alignOf(Fields)) const u8, comptime field: FieldEnum) ?Field(field)` |
| `setFlag` | `pub fn setFlag(self: *Self, comptime field: FieldEnum) void` |
| `init` | `pub fn init(fields: ActiveFields) Self` |
| `setMany` | `pub fn setMany(self: Self, p: [*]align(@alignOf(Fields)) u8, fields: FieldValues) void` |
| `set` | `pub fn set( self: Self, p: [*]align(@alignOf(Fields)) u8, comptime field: FieldEnum, value: Field(field), ) void` |
| `ptr` | `pub fn ptr(self: Self, p: [*]align(@alignOf(Fields)) u8, comptime field: FieldEnum) *Field(field)` |
| `ptrConst` | `pub fn ptrConst(self: Self, p: [*]align(@alignOf(Fields)) const u8, comptime field: FieldEnum) *const Field(field)` |
| `offset` | `pub fn offset(self: Self, comptime field: FieldEnum) usize` |
| `Field` | `pub fn Field(comptime field: FieldEnum) type` |
| `sizeInBytes` | `pub fn sizeInBytes(self: Self) usize` |

## meta / trait

| Function | Signature |
|----------|-----------|
| `multiTrait` | `pub fn multiTrait(comptime traits: anytype) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `add` | `pub fn add(self: MyType, other: MyType) MyType` |
| `hasFn` | `pub fn hasFn(comptime name: []const u8) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `useless` | `pub fn useless() void` |
| `hasField` | `pub fn hasField(comptime name: []const u8) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `is` | `pub fn is(comptime id: std.builtin.TypeId) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `isPtrTo` | `pub fn isPtrTo(comptime id: std.builtin.TypeId) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `isSliceOf` | `pub fn isSliceOf(comptime id: std.builtin.TypeId) TraitFn` |
| `trait` | `pub fn trait(comptime T: type) bool` |
| `isExtern` | `pub fn isExtern(comptime T: type) bool` |
| `isPacked` | `pub fn isPacked(comptime T: type) bool` |
| `isUnsignedInt` | `pub fn isUnsignedInt(comptime T: type) bool` |
| `isSignedInt` | `pub fn isSignedInt(comptime T: type) bool` |
| `isSingleItemPtr` | `pub fn isSingleItemPtr(comptime T: type) bool` |
| `isManyItemPtr` | `pub fn isManyItemPtr(comptime T: type) bool` |
| `isSlice` | `pub fn isSlice(comptime T: type) bool` |
| `isIndexable` | `pub fn isIndexable(comptime T: type) bool` |
| `isNumber` | `pub fn isNumber(comptime T: type) bool` |
| `isIntegral` | `pub fn isIntegral(comptime T: type) bool` |
| `isFloat` | `pub fn isFloat(comptime T: type) bool` |
| `isConstPtr` | `pub fn isConstPtr(comptime T: type) bool` |
| `isContainer` | `pub fn isContainer(comptime T: type) bool` |
| `isTuple` | `pub fn isTuple(comptime T: type) bool` |
| `isZigString` | `pub fn isZigString(comptime T: type) bool` |
| `hasDecls` | `pub fn hasDecls(comptime T: type, comptime names: anytype) bool` |
| `useless` | `pub fn useless() void` |
| `hasFields` | `pub fn hasFields(comptime T: type, comptime names: anytype) bool` |
| `useless` | `pub fn useless() void` |
| `hasFunctions` | `pub fn hasFunctions(comptime T: type, comptime names: anytype) bool` |
| `a` | `pub fn a() void` |
| `hasUniqueRepresentation` | `pub fn hasUniqueRepresentation(comptime T: type) bool` |

## multi_array_list

| Function | Signature |
|----------|-----------|
| `MultiArrayList` | `pub fn MultiArrayList(comptime S: type) type` |
| `items` | `pub fn items(self: Slice, comptime field: Field) []FieldType(field)` |
| `toMultiArrayList` | `pub fn toMultiArrayList(self: Slice) Self` |
| `deinit` | `pub fn deinit(self: *Slice, gpa: Allocator) void` |
| `deinit` | `pub fn deinit(self: *Self, gpa: Allocator) void` |
| `toOwnedSlice` | `pub fn toOwnedSlice(self: *Self) Slice` |
| `slice` | `pub fn slice(self: Self) Slice` |
| `items` | `pub fn items(self: Self, comptime field: Field) []FieldType(field)` |
| `set` | `pub fn set(self: *Self, index: usize, elem: S) void` |
| `get` | `pub fn get(self: Self, index: usize) S` |
| `append` | `pub fn append(self: *Self, gpa: Allocator, elem: S) !void` |
| `appendAssumeCapacity` | `pub fn appendAssumeCapacity(self: *Self, elem: S) void` |
| `addOne` | `pub fn addOne(self: *Self, allocator: Allocator) Allocator.Error!usize` |
| `addOneAssumeCapacity` | `pub fn addOneAssumeCapacity(self: *Self) usize` |
| `pop` | `pub fn pop(self: *Self) S` |
| `popOrNull` | `pub fn popOrNull(self: *Self) ?S` |
| `insert` | `pub fn insert(self: *Self, gpa: Allocator, index: usize, elem: S) !void` |
| `insertAssumeCapacity` | `pub fn insertAssumeCapacity(self: *Self, index: usize, elem: S) void` |
| `swapRemove` | `pub fn swapRemove(self: *Self, index: usize) void` |
| `orderedRemove` | `pub fn orderedRemove(self: *Self, index: usize) void` |
| `resize` | `pub fn resize(self: *Self, gpa: Allocator, new_len: usize) !void` |
| `shrinkAndFree` | `pub fn shrinkAndFree(self: *Self, gpa: Allocator, new_len: usize) void` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `ensureTotalCapacity` | `pub fn ensureTotalCapacity(self: *Self, gpa: Allocator, new_capacity: usize) !void` |
| `ensureUnusedCapacity` | `pub fn ensureUnusedCapacity(self: *Self, gpa: Allocator, additional_count: usize) !void` |
| `setCapacity` | `pub fn setCapacity(self: *Self, gpa: Allocator, new_capacity: usize) !void` |
| `clone` | `pub fn clone(self: Self, gpa: Allocator) !Self` |
| `sort` | `pub fn sort(self: Self, ctx: anytype) void` |
| `swap` | `pub fn swap(sc: @This(), a_index: usize, b_index: usize) void` |
| `lessThan` | `pub fn lessThan(sc: @This(), a_index: usize, b_index: usize) bool` |

## net

| Function | Signature |
|----------|-----------|
| `parseIp` | `pub fn parseIp(name: []const u8, port: u16) !Address` |
| `resolveIp` | `pub fn resolveIp(name: []const u8, port: u16) !Address` |
| `parseExpectingFamily` | `pub fn parseExpectingFamily(name: []const u8, family: os.sa_family_t, port: u16) !Address` |
| `parseIp6` | `pub fn parseIp6(buf: []const u8, port: u16) !Address` |
| `resolveIp6` | `pub fn resolveIp6(buf: []const u8, port: u16) !Address` |
| `parseIp4` | `pub fn parseIp4(buf: []const u8, port: u16) !Address` |
| `initIp4` | `pub fn initIp4(addr: [4]u8, port: u16) Address` |
| `initIp6` | `pub fn initIp6(addr: [16]u8, port: u16, flowinfo: u32, scope_id: u32) Address` |
| `initUnix` | `pub fn initUnix(path: []const u8) !Address` |
| `getPort` | `pub fn getPort(self: Address) u16` |
| `setPort` | `pub fn setPort(self: *Address, port: u16) void` |
| `initPosix` | `pub fn initPosix(addr: *align(4) const os.sockaddr) Address` |
| `format` | `pub fn format( self: Address, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `eql` | `pub fn eql(a: Address, b: Address) bool` |
| `getOsSockLen` | `pub fn getOsSockLen(self: Address) os.socklen_t` |
| `parse` | `pub fn parse(buf: []const u8, port: u16) !Ip4Address` |
| `resolveIp` | `pub fn resolveIp(name: []const u8, port: u16) !Ip4Address` |
| `init` | `pub fn init(addr: [4]u8, port: u16) Ip4Address` |
| `getPort` | `pub fn getPort(self: Ip4Address) u16` |
| `setPort` | `pub fn setPort(self: *Ip4Address, port: u16) void` |
| `format` | `pub fn format( self: Ip4Address, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `getOsSockLen` | `pub fn getOsSockLen(self: Ip4Address) os.socklen_t` |
| `parse` | `pub fn parse(buf: []const u8, port: u16) !Ip6Address` |
| `resolve` | `pub fn resolve(buf: []const u8, port: u16) !Ip6Address` |
| `init` | `pub fn init(addr: [16]u8, port: u16, flowinfo: u32, scope_id: u32) Ip6Address` |
| `getPort` | `pub fn getPort(self: Ip6Address) u16` |
| `setPort` | `pub fn setPort(self: *Ip6Address, port: u16) void` |
| `format` | `pub fn format( self: Ip6Address, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `getOsSockLen` | `pub fn getOsSockLen(self: Ip6Address) os.socklen_t` |
| `connectUnixSocket` | `pub fn connectUnixSocket(path: []const u8) !Stream` |
| `deinit` | `pub fn deinit(self: *AddressList) void` |
| `tcpConnectToHost` | `pub fn tcpConnectToHost(allocator: mem.Allocator, name: []const u8, port: u16) !Stream` |
| `tcpConnectToAddress` | `pub fn tcpConnectToAddress(address: Address) !Stream` |
| `getAddressList` | `pub fn getAddressList(allocator: mem.Allocator, name: []const u8, port: u16) !*AddressList` |
| `isValidHostName` | `pub fn isValidHostName(hostname: []const u8) bool` |
| `close` | `pub fn close(self: Stream) void` |
| `reader` | `pub fn reader(self: Stream) Reader` |
| `writer` | `pub fn writer(self: Stream) Writer` |
| `read` | `pub fn read(self: Stream, buffer: []u8) ReadError!usize` |
| `write` | `pub fn write(self: Stream, buffer: []const u8) WriteError!usize` |
| `writev` | `pub fn writev(self: Stream, iovecs: []const os.iovec_const) WriteError!usize` |
| `writevAll` | `pub fn writevAll(self: Stream, iovecs: []os.iovec_const) WriteError!void` |
| `init` | `pub fn init(options: Options) StreamServer` |
| `deinit` | `pub fn deinit(self: *StreamServer) void` |
| `listen` | `pub fn listen(self: *StreamServer, address: Address) !void` |
| `close` | `pub fn close(self: *StreamServer) void` |
| `accept` | `pub fn accept(self: *StreamServer) AcceptError!Connection` |

## once

| Function | Signature |
|----------|-----------|
| `once` | `pub fn once(comptime f: fn () void) Once(f)` |
| `Once` | `pub fn Once(comptime f: fn () void) type` |
| `call` | `pub fn call(self: *@This()) void` |

## os

| Function | Signature |
|----------|-----------|
| `close` | `pub fn close(fd: fd_t) void` |
| `fchmod` | `pub fn fchmod(fd: fd_t, mode: mode_t) FChmodError!void` |
| `fchown` | `pub fn fchown(fd: fd_t, owner: ?uid_t, group: ?gid_t) FChownError!void` |
| `reboot` | `pub fn reboot(cmd: RebootCommand) RebootError!void` |
| `getrandom` | `pub fn getrandom(buffer: []u8) GetRandomError!void` |
| `abort` | `pub fn abort() noreturn` |
| `raise` | `pub fn raise(sig: u8) RaiseError!void` |
| `kill` | `pub fn kill(pid: pid_t, sig: u8) KillError!void` |
| `exit` | `pub fn exit(status: u8) noreturn` |
| `read` | `pub fn read(fd: fd_t, buf: []u8) ReadError!usize` |
| `readv` | `pub fn readv(fd: fd_t, iov: []const iovec) ReadError!usize` |
| `pread` | `pub fn pread(fd: fd_t, buf: []u8, offset: u64) PReadError!usize` |
| `ftruncate` | `pub fn ftruncate(fd: fd_t, length: u64) TruncateError!void` |
| `preadv` | `pub fn preadv(fd: fd_t, iov: []const iovec, offset: u64) PReadError!usize` |
| `write` | `pub fn write(fd: fd_t, bytes: []const u8) WriteError!usize` |
| `writev` | `pub fn writev(fd: fd_t, iov: []const iovec_const) WriteError!usize` |
| `pwrite` | `pub fn pwrite(fd: fd_t, bytes: []const u8, offset: u64) PWriteError!usize` |
| `pwritev` | `pub fn pwritev(fd: fd_t, iov: []const iovec_const, offset: u64) PWriteError!usize` |
| `open` | `pub fn open(file_path: []const u8, flags: u32, perm: mode_t) OpenError!fd_t` |
| `openZ` | `pub fn openZ(file_path: [*:0]const u8, flags: u32, perm: mode_t) OpenError!fd_t` |
| `openW` | `pub fn openW(file_path_w: []const u16, flags: u32, perm: mode_t) OpenError!fd_t` |
| `initPreopensWasi` | `pub fn initPreopensWasi(alloc: Allocator, cwd_root: []const u8) !void` |
| `resolvePathWasi` | `pub fn resolvePathWasi(path: []const u8, out_buffer: *[MAX_PATH_BYTES]u8) !RelativePathWasi` |
| `openat` | `pub fn openat(dir_fd: fd_t, file_path: []const u8, flags: u32, mode: mode_t) OpenError!fd_t` |
| `openatWasi` | `pub fn openatWasi(dir_fd: fd_t, file_path: []const u8, lookup_flags: lookupflags_t, oflags: oflags_t, fdflags: fdflags_t, base: rights_t, inheriting: rights_t) OpenError!fd_t` |
| `openatZ` | `pub fn openatZ(dir_fd: fd_t, file_path: [*:0]const u8, flags: u32, mode: mode_t) OpenError!fd_t` |
| `openatW` | `pub fn openatW(dir_fd: fd_t, file_path_w: []const u16, flags: u32, mode: mode_t) OpenError!fd_t` |
| `dup` | `pub fn dup(old_fd: fd_t) !fd_t` |
| `dup2` | `pub fn dup2(old_fd: fd_t, new_fd: fd_t) !void` |
| `execveZ` | `pub fn execveZ( path: [*:0]const u8, child_argv: [*:null]const ?[*:0]const u8, envp: [*:null]const ?[*:0]const u8, ) ExecveError` |
| `execvpeZ_expandArg0` | `pub fn execvpeZ_expandArg0( comptime arg0_expand: Arg0Expand, file: [*:0]const u8, child_argv: switch (arg0_expand) { .expand => [*:null]?[*:0]const u8, .no_expand => [*:null]const ?[*:0]const u8, }, envp: [*:null]const ?[*:0]const u8, ) ExecveError` |
| `execvpeZ` | `pub fn execvpeZ( file: [*:0]const u8, argv_ptr: [*:null]const ?[*:0]const u8, envp: [*:null]const ?[*:0]const u8, ) ExecveError` |
| `getenv` | `pub fn getenv(key: []const u8) ?[]const u8` |
| `getenvZ` | `pub fn getenvZ(key: [*:0]const u8) ?[]const u8` |
| `getenvW` | `pub fn getenvW(key: [*:0]const u16) ?[:0]const u16` |
| `getcwd` | `pub fn getcwd(out_buffer: []u8) GetCwdError![]u8` |
| `symlink` | `pub fn symlink(target_path: []const u8, sym_link_path: []const u8) SymLinkError!void` |
| `symlinkZ` | `pub fn symlinkZ(target_path: [*:0]const u8, sym_link_path: [*:0]const u8) SymLinkError!void` |
| `symlinkat` | `pub fn symlinkat(target_path: []const u8, newdirfd: fd_t, sym_link_path: []const u8) SymLinkError!void` |
| `symlinkatWasi` | `pub fn symlinkatWasi(target_path: []const u8, newdirfd: fd_t, sym_link_path: []const u8) SymLinkError!void` |
| `symlinkatZ` | `pub fn symlinkatZ(target_path: [*:0]const u8, newdirfd: fd_t, sym_link_path: [*:0]const u8) SymLinkError!void` |
| `linkZ` | `pub fn linkZ(oldpath: [*:0]const u8, newpath: [*:0]const u8, flags: i32) LinkError!void` |
| `link` | `pub fn link(oldpath: []const u8, newpath: []const u8, flags: i32) LinkError!void` |
| `linkatZ` | `pub fn linkatZ( olddir: fd_t, oldpath: [*:0]const u8, newdir: fd_t, newpath: [*:0]const u8, flags: i32, ) LinkatError!void` |
| `linkat` | `pub fn linkat( olddir: fd_t, oldpath: []const u8, newdir: fd_t, newpath: []const u8, flags: i32, ) LinkatError!void` |
| `linkatWasi` | `pub fn linkatWasi(old: RelativePathWasi, new: RelativePathWasi, flags: i32) LinkatError!void` |
| `unlink` | `pub fn unlink(file_path: []const u8) UnlinkError!void` |
| `unlinkZ` | `pub fn unlinkZ(file_path: [*:0]const u8) UnlinkError!void` |
| `unlinkW` | `pub fn unlinkW(file_path_w: []const u16) UnlinkError!void` |
| `unlinkat` | `pub fn unlinkat(dirfd: fd_t, file_path: []const u8, flags: u32) UnlinkatError!void` |
| `unlinkatWasi` | `pub fn unlinkatWasi(dirfd: fd_t, file_path: []const u8, flags: u32) UnlinkatError!void` |
| `unlinkatZ` | `pub fn unlinkatZ(dirfd: fd_t, file_path_c: [*:0]const u8, flags: u32) UnlinkatError!void` |
| `unlinkatW` | `pub fn unlinkatW(dirfd: fd_t, sub_path_w: []const u16, flags: u32) UnlinkatError!void` |
| `rename` | `pub fn rename(old_path: []const u8, new_path: []const u8) RenameError!void` |
| `renameZ` | `pub fn renameZ(old_path: [*:0]const u8, new_path: [*:0]const u8) RenameError!void` |
| `renameW` | `pub fn renameW(old_path: [*:0]const u16, new_path: [*:0]const u16) RenameError!void` |
| `renameat` | `pub fn renameat( old_dir_fd: fd_t, old_path: []const u8, new_dir_fd: fd_t, new_path: []const u8, ) RenameError!void` |
| `renameatWasi` | `pub fn renameatWasi(old: RelativePathWasi, new: RelativePathWasi) RenameError!void` |
| `renameatZ` | `pub fn renameatZ( old_dir_fd: fd_t, old_path: [*:0]const u8, new_dir_fd: fd_t, new_path: [*:0]const u8, ) RenameError!void` |
| `renameatW` | `pub fn renameatW( old_dir_fd: fd_t, old_path_w: []const u16, new_dir_fd: fd_t, new_path_w: []const u16, ReplaceIfExists: windows.BOOLEAN, ) RenameError!void` |
| `mkdirat` | `pub fn mkdirat(dir_fd: fd_t, sub_dir_path: []const u8, mode: u32) MakeDirError!void` |
| `mkdiratWasi` | `pub fn mkdiratWasi(dir_fd: fd_t, sub_dir_path: []const u8, mode: u32) MakeDirError!void` |
| `mkdiratZ` | `pub fn mkdiratZ(dir_fd: fd_t, sub_dir_path: [*:0]const u8, mode: u32) MakeDirError!void` |
| `mkdiratW` | `pub fn mkdiratW(dir_fd: fd_t, sub_path_w: []const u16, mode: u32) MakeDirError!void` |
| `mkdir` | `pub fn mkdir(dir_path: []const u8, mode: u32) MakeDirError!void` |
| `mkdirZ` | `pub fn mkdirZ(dir_path: [*:0]const u8, mode: u32) MakeDirError!void` |
| `mkdirW` | `pub fn mkdirW(dir_path_w: []const u16, mode: u32) MakeDirError!void` |
| `rmdir` | `pub fn rmdir(dir_path: []const u8) DeleteDirError!void` |
| `rmdirZ` | `pub fn rmdirZ(dir_path: [*:0]const u8) DeleteDirError!void` |
| `rmdirW` | `pub fn rmdirW(dir_path_w: []const u16) DeleteDirError!void` |
| `chdir` | `pub fn chdir(dir_path: []const u8) ChangeCurDirError!void` |
| `chdirZ` | `pub fn chdirZ(dir_path: [*:0]const u8) ChangeCurDirError!void` |
| `chdirW` | `pub fn chdirW(dir_path: []const u16) ChangeCurDirError!void` |
| `fchdir` | `pub fn fchdir(dirfd: fd_t) FchdirError!void` |
| `readlink` | `pub fn readlink(file_path: []const u8, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkW` | `pub fn readlinkW(file_path: []const u16, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkZ` | `pub fn readlinkZ(file_path: [*:0]const u8, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkat` | `pub fn readlinkat(dirfd: fd_t, file_path: []const u8, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkatWasi` | `pub fn readlinkatWasi(dirfd: fd_t, file_path: []const u8, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkatW` | `pub fn readlinkatW(dirfd: fd_t, file_path: []const u16, out_buffer: []u8) ReadLinkError![]u8` |
| `readlinkatZ` | `pub fn readlinkatZ(dirfd: fd_t, file_path: [*:0]const u8, out_buffer: []u8) ReadLinkError![]u8` |
| `setuid` | `pub fn setuid(uid: uid_t) SetIdError!void` |
| `seteuid` | `pub fn seteuid(uid: uid_t) SetEidError!void` |
| `setreuid` | `pub fn setreuid(ruid: uid_t, euid: uid_t) SetIdError!void` |
| `setgid` | `pub fn setgid(gid: gid_t) SetIdError!void` |
| `setegid` | `pub fn setegid(uid: uid_t) SetEidError!void` |
| `setregid` | `pub fn setregid(rgid: gid_t, egid: gid_t) SetIdError!void` |
| `isatty` | `pub fn isatty(handle: fd_t) bool` |
| `isCygwinPty` | `pub fn isCygwinPty(handle: fd_t) bool` |
| `socket` | `pub fn socket(domain: u32, socket_type: u32, protocol: u32) SocketError!socket_t` |
| `shutdown` | `pub fn shutdown(sock: socket_t, how: ShutdownHow) ShutdownError!void` |
| `closeSocket` | `pub fn closeSocket(sock: socket_t) void` |
| `bind` | `pub fn bind(sock: socket_t, addr: *const sockaddr, len: socklen_t) BindError!void` |
| `listen` | `pub fn listen(sock: socket_t, backlog: u31) ListenError!void` |
| `accept` | `pub fn accept( /// This argument is a socket that has been created with `socket`, bound to a local address /// with `bind`, and is listening for connections after a `listen`. sock: socket_t, /// This argument is a pointer to a sockaddr structure. This structure is filled in with the /// address of the peer socket, as known to the communications layer. The exact format of the /// address returned addr is determined by the socket's address family (see `socket` and the /// respective protocol man pages). addr: ?*sockaddr, /// This argument is a value-result argument: the caller must initialize it to contain the /// size (in bytes) of the structure pointed to by addr; on return it will contain the actual size /// of the peer address. /// /// The returned address is truncated if the buffer provided is too small; in this case, `addr_size` /// will return a value greater than was supplied to the call. addr_size: ?*socklen_t, /// The following values can be bitwise ORed in flags to obtain different behavior: /// * `SOCK.NONBLOCK` - Set the `O.NONBLOCK` file status flag on the open file description (see `open`) /// referred to by the new file descriptor. Using this flag saves extra calls to `fcntl` to achieve /// the same result. /// * `SOCK.CLOEXEC` - Set the close-on-exec (`FD_CLOEXEC`) flag on the new file descriptor. See the /// description of the `O.CLOEXEC` flag in `open` for reasons why this may be useful. flags: u32, ) AcceptError!socket_t { const have_accept4 = comptime !(builtin.target.isDarwin() or builtin.os.tag == .windows); assert(0 == (flags & ~@as(u32, SOCK.NONBLOCK | SOCK.CLOEXEC))); // Unsupported flag(s) const accepted_sock = while (true) { const rc = if (have_accept4) system.accept4(sock, addr, addr_size, flags) else if (builtin.os.tag == .windows) windows.accept(sock, addr, addr_size) else system.accept(sock, addr, addr_size); if (builtin.os.tag == .windows) { if (rc == windows.ws2_32.INVALID_SOCKET) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, // not initialized WSA .WSAECONNRESET => return error.ConnectionResetByPeer, .WSAEFAULT => unreachable, .WSAEINVAL => return error.SocketNotListening, .WSAEMFILE => return error.ProcessFdQuotaExceeded, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENOBUFS => return error.FileDescriptorNotASocket, .WSAEOPNOTSUPP => return error.OperationNotSupported, .WSAEWOULDBLOCK => return error.WouldBlock, else => |err| return windows.unexpectedWSAError(err), } } else { break rc; } } else { switch (errno(rc)) { .SUCCESS => { break @intCast(socket_t, rc); }, .INTR => continue, .AGAIN => return error.WouldBlock, .BADF => unreachable, // always a race condition .CONNABORTED => return error.ConnectionAborted, .FAULT => unreachable, .INVAL => return error.SocketNotListening, .NOTSOCK => unreachable, .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NOBUFS => return error.SystemResources, .NOMEM => return error.SystemResources, .OPNOTSUPP => unreachable, .PROTO => return error.ProtocolFailure, .PERM => return error.BlockedByFirewall, else => |err| return unexpectedErrno(err), } } } else unreachable; if (!have_accept4) { try setSockFlags(accepted_sock, flags); } return accepted_sock; } pub const EpollCreateError = error{ /// The per-user limit on the number of epoll instances imposed by /// /proc/sys/fs/epoll/max_user_instances was encountered. See epoll(7) for further /// details. /// Or, The per-process limit on the number of open file descriptors has been reached. ProcessFdQuotaExceeded, /// The system-wide limit on the total number of open files has been reached. SystemFdQuotaExceeded, /// There was insufficient memory to create the kernel object. SystemResources, } || UnexpectedError; pub fn epoll_create1(flags: u32) EpollCreateError!i32 { const rc = system.epoll_create1(flags); switch (errno(rc)) { .SUCCESS => return @intCast(i32, rc), else => |err| return unexpectedErrno(err), .INVAL => unreachable, .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NOMEM => return error.SystemResources, } } pub const EpollCtlError = error{ /// op was EPOLL_CTL_ADD, and the supplied file descriptor fd is already registered /// with this epoll instance. FileDescriptorAlreadyPresentInSet, /// fd refers to an epoll instance and this EPOLL_CTL_ADD operation would result in a /// circular loop of epoll instances monitoring one another. OperationCausesCircularLoop, /// op was EPOLL_CTL_MOD or EPOLL_CTL_DEL, and fd is not registered with this epoll /// instance. FileDescriptorNotRegistered, /// There was insufficient memory to handle the requested op control operation. SystemResources, /// The limit imposed by /proc/sys/fs/epoll/max_user_watches was encountered while /// trying to register (EPOLL_CTL_ADD) a new file descriptor on an epoll instance. /// See epoll(7) for further details. UserResourceLimitReached, /// The target file fd does not support epoll. This error can occur if fd refers to, /// for example, a regular file or a directory. FileDescriptorIncompatibleWithEpoll, } || UnexpectedError; pub fn epoll_ctl(epfd: i32, op: u32, fd: i32, event: ?*linux.epoll_event) EpollCtlError!void { const rc = system.epoll_ctl(epfd, op, fd, event); switch (errno(rc)) { .SUCCESS => return, else => |err| return unexpectedErrno(err), .BADF => unreachable, // always a race condition if this happens .EXIST => return error.FileDescriptorAlreadyPresentInSet, .INVAL => unreachable, .LOOP => return error.OperationCausesCircularLoop, .NOENT => return error.FileDescriptorNotRegistered, .NOMEM => return error.SystemResources, .NOSPC => return error.UserResourceLimitReached, .PERM => return error.FileDescriptorIncompatibleWithEpoll, } } /// Waits for an I/O event on an epoll file descriptor. /// Returns the number of file descriptors ready for the requested I/O, /// or zero if no file descriptor became ready during the requested timeout milliseconds. pub fn epoll_wait(epfd: i32, events: []linux.epoll_event, timeout: i32) usize { while (true) { // TODO get rid of the @intCast const rc = system.epoll_wait(epfd, events.ptr, @intCast(u32, events.len), timeout); switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .INTR => continue, .BADF => unreachable, .FAULT => unreachable, .INVAL => unreachable, else => unreachable, } } } pub const EventFdError = error{ SystemResources, ProcessFdQuotaExceeded, SystemFdQuotaExceeded, } || UnexpectedError; pub fn eventfd(initval: u32, flags: u32) EventFdError!i32 { const rc = system.eventfd(initval, flags); switch (errno(rc)) { .SUCCESS => return @intCast(i32, rc), else => |err| return unexpectedErrno(err), .INVAL => unreachable, // invalid parameters .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NODEV => return error.SystemResources, .NOMEM => return error.SystemResources, } } pub const GetSockNameError = error{ /// Insufficient resources were available in the system to perform the operation. SystemResources, /// The network subsystem has failed. NetworkSubsystemFailed, /// Socket hasn't been bound yet SocketNotBound, FileDescriptorNotASocket, } || UnexpectedError; pub fn getsockname(sock: socket_t, addr: *sockaddr, addrlen: *socklen_t) GetSockNameError!void { if (builtin.os.tag == .windows) { const rc = windows.getsockname(sock, addr, addrlen); if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAEFAULT => unreachable, // addr or addrlen have invalid pointers or addrlen points to an incorrect value .WSAENOTSOCK => return error.FileDescriptorNotASocket, .WSAEINVAL => return error.SocketNotBound, else => |err| return windows.unexpectedWSAError(err), } } return; } else { const rc = system.getsockname(sock, addr, addrlen); switch (errno(rc)) { .SUCCESS => return, else => |err| return unexpectedErrno(err), .BADF => unreachable, // always a race condition .FAULT => unreachable, .INVAL => unreachable, // invalid parameters .NOTSOCK => return error.FileDescriptorNotASocket, .NOBUFS => return error.SystemResources, } } } pub fn getpeername(sock: socket_t, addr: *sockaddr, addrlen: *socklen_t) GetSockNameError!void { if (builtin.os.tag == .windows) { const rc = windows.getpeername(sock, addr, addrlen); if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAEFAULT => unreachable, // addr or addrlen have invalid pointers or addrlen points to an incorrect value .WSAENOTSOCK => return error.FileDescriptorNotASocket, .WSAEINVAL => return error.SocketNotBound, else => |err| return windows.unexpectedWSAError(err), } } return; } else { const rc = system.getpeername(sock, addr, addrlen); switch (errno(rc)) { .SUCCESS => return, else => |err| return unexpectedErrno(err), .BADF => unreachable, // always a race condition .FAULT => unreachable, .INVAL => unreachable, // invalid parameters .NOTSOCK => return error.FileDescriptorNotASocket, .NOBUFS => return error.SystemResources, } } } pub const ConnectError = error{ /// For UNIX domain sockets, which are identified by pathname: Write permission is denied on the socket /// file, or search permission is denied for one of the directories in the path prefix. /// or /// The user tried to connect to a broadcast address without having the socket broadcast flag enabled or /// the connection request failed because of a local firewall rule. PermissionDenied, /// Local address is already in use. AddressInUse, /// (Internet domain sockets) The socket referred to by sockfd had not previously been bound to an /// address and, upon attempting to bind it to an ephemeral port, it was determined that all port numbers /// in the ephemeral port range are currently in use. See the discussion of /// /proc/sys/net/ipv4/ip_local_port_range in ip(7). AddressNotAvailable, /// The passed address didn't have the correct address family in its sa_family field. AddressFamilyNotSupported, /// Insufficient entries in the routing cache. SystemResources, /// A connect() on a stream socket found no one listening on the remote address. ConnectionRefused, /// Network is unreachable. NetworkUnreachable, /// Timeout while attempting connection. The server may be too busy to accept new connections. Note /// that for IP sockets the timeout may be very long when syncookies are enabled on the server. ConnectionTimedOut, /// This error occurs when no global event loop is configured, /// and connecting to the socket would block. WouldBlock, /// The given path for the unix socket does not exist. FileNotFound, /// Connection was reset by peer before connect could complete. ConnectionResetByPeer, /// Socket is non-blocking and already has a pending connection in progress. ConnectionPending, } || UnexpectedError; /// Initiate a connection on a socket. /// If `sockfd` is opened in non blocking mode, the function will /// return error.WouldBlock when EAGAIN or EINPROGRESS is received. pub fn connect(sock: socket_t, sock_addr: *const sockaddr, len: socklen_t) ConnectError!void { if (builtin.os.tag == .windows) { const rc = windows.ws2_32.connect(sock, sock_addr, @intCast(i32, len)); if (rc == 0) return; switch (windows.ws2_32.WSAGetLastError()) { .WSAEADDRINUSE => return error.AddressInUse, .WSAEADDRNOTAVAIL => return error.AddressNotAvailable, .WSAECONNREFUSED => return error.ConnectionRefused, .WSAECONNRESET => return error.ConnectionResetByPeer, .WSAETIMEDOUT => return error.ConnectionTimedOut, .WSAEHOSTUNREACH, // TODO: should we return NetworkUnreachable in this case as well? .WSAENETUNREACH, => return error.NetworkUnreachable, .WSAEFAULT => unreachable, .WSAEINVAL => unreachable, .WSAEISCONN => unreachable, .WSAENOTSOCK => unreachable, .WSAEWOULDBLOCK => unreachable, .WSAEACCES => unreachable, .WSAENOBUFS => return error.SystemResources, .WSAEAFNOSUPPORT => return error.AddressFamilyNotSupported, else => |err| return windows.unexpectedWSAError(err), } return; } while (true) { switch (errno(system.connect(sock, sock_addr, len))) { .SUCCESS => return, .ACCES => return error.PermissionDenied, .PERM => return error.PermissionDenied, .ADDRINUSE => return error.AddressInUse, .ADDRNOTAVAIL => return error.AddressNotAvailable, .AFNOSUPPORT => return error.AddressFamilyNotSupported, .AGAIN, .INPROGRESS => return error.WouldBlock, .ALREADY => return error.ConnectionPending, .BADF => unreachable, // sockfd is not a valid open file descriptor. .CONNREFUSED => return error.ConnectionRefused, .CONNRESET => return error.ConnectionResetByPeer, .FAULT => unreachable, // The socket structure address is outside the user's address space. .INTR => continue, .ISCONN => unreachable, // The socket is already connected. .HOSTUNREACH => return error.NetworkUnreachable, .NETUNREACH => return error.NetworkUnreachable, .NOTSOCK => unreachable, // The file descriptor sockfd does not refer to a socket. .PROTOTYPE => unreachable, // The socket type does not support the requested communications protocol. .TIMEDOUT => return error.ConnectionTimedOut, .NOENT => return error.FileNotFound, // Returned when socket is AF.UNIX and the given path does not exist. else => |err| return unexpectedErrno(err), } } } pub fn getsockoptError(sockfd: fd_t) ConnectError!void { var err_code: i32 = undefined; var size: u32 = @sizeOf(u32); const rc = system.getsockopt(sockfd, SOL.SOCKET, SO.ERROR, @ptrCast([*]u8, &err_code), &size); assert(size == 4); switch (errno(rc)) { .SUCCESS => switch (@intToEnum(E, err_code)) { .SUCCESS => return, .ACCES => return error.PermissionDenied, .PERM => return error.PermissionDenied, .ADDRINUSE => return error.AddressInUse, .ADDRNOTAVAIL => return error.AddressNotAvailable, .AFNOSUPPORT => return error.AddressFamilyNotSupported, .AGAIN => return error.SystemResources, .ALREADY => return error.ConnectionPending, .BADF => unreachable, // sockfd is not a valid open file descriptor. .CONNREFUSED => return error.ConnectionRefused, .FAULT => unreachable, // The socket structure address is outside the user's address space. .ISCONN => unreachable, // The socket is already connected. .HOSTUNREACH => return error.NetworkUnreachable, .NETUNREACH => return error.NetworkUnreachable, .NOTSOCK => unreachable, // The file descriptor sockfd does not refer to a socket. .PROTOTYPE => unreachable, // The socket type does not support the requested communications protocol. .TIMEDOUT => return error.ConnectionTimedOut, .CONNRESET => return error.ConnectionResetByPeer, else => |err| return unexpectedErrno(err), }, .BADF => unreachable, // The argument sockfd is not a valid file descriptor. .FAULT => unreachable, // The address pointed to by optval or optlen is not in a valid part of the process address space. .INVAL => unreachable, .NOPROTOOPT => unreachable, // The option is unknown at the level indicated. .NOTSOCK => unreachable, // The file descriptor sockfd does not refer to a socket. else => |err| return unexpectedErrno(err), } } pub const WaitPidResult = struct { pid: pid_t, status: u32, }; /// Use this version of the `waitpid` wrapper if you spawned your child process using explicit /// `fork` and `execve` method. If you spawned your child process using `posix_spawn` method, /// use `std.os.posix_spawn.waitpid` instead. pub fn waitpid(pid: pid_t, flags: u32) WaitPidResult { const Status = if (builtin.link_libc) c_int else u32; var status: Status = undefined; while (true) { const rc = system.waitpid(pid, &status, if (builtin.link_libc) @intCast(c_int, flags) else flags); switch (errno(rc)) { .SUCCESS => return .{ .pid = @intCast(pid_t, rc), .status = @bitCast(u32, status), }, .INTR => continue, .CHILD => unreachable, // The process specified does not exist. It would be a race condition to handle this error. .INVAL => unreachable, // Invalid flags. else => unreachable, } } } pub const FStatError = error{ SystemResources, /// In WASI, this error may occur when the file descriptor does /// not hold the required rights to get its filestat information. AccessDenied, } || UnexpectedError; /// Return information about a file descriptor. pub fn fstat(fd: fd_t) FStatError!Stat { if (builtin.os.tag == .wasi and !builtin.link_libc) { var stat: wasi.filestat_t = undefined; switch (wasi.fd_filestat_get(fd, &stat)) { .SUCCESS => return Stat.fromFilestat(stat), .INVAL => unreachable, .BADF => unreachable, // Always a race condition. .NOMEM => return error.SystemResources, .ACCES => return error.AccessDenied, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .windows) { @compileError("fstat is not yet implemented on Windows"); } const fstat_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.fstat64 else system.fstat; var stat = mem.zeroes(Stat); switch (errno(fstat_sym(fd, &stat))) { .SUCCESS => return stat, .INVAL => unreachable, .BADF => unreachable, // Always a race condition. .NOMEM => return error.SystemResources, .ACCES => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } pub const FStatAtError = FStatError || error{ NameTooLong, FileNotFound, SymLinkLoop }; /// Similar to `fstat`, but returns stat of a resource pointed to by `pathname` /// which is relative to `dirfd` handle. /// See also `fstatatZ` and `fstatatWasi`. pub fn fstatat(dirfd: fd_t, pathname: []const u8, flags: u32) FStatAtError!Stat { if (builtin.os.tag == .wasi and !builtin.link_libc) { const wasi_flags = if (flags & linux.AT.SYMLINK_NOFOLLOW == 0) wasi.LOOKUP_SYMLINK_FOLLOW else 0; if (dirfd == wasi.AT.FDCWD or fs.path.isAbsolute(pathname)) { // Resolve absolute or CWD-relative paths to a path within a Preopen var path_buf: [MAX_PATH_BYTES]u8 = undefined; const path = try resolvePathWasi(pathname, &path_buf); return fstatatWasi(path.dir_fd, path.relative_path, wasi_flags); } return fstatatWasi(dirfd, pathname, wasi_flags); } else if (builtin.os.tag == .windows) { @compileError("fstatat is not yet implemented on Windows"); } else { const pathname_c = try toPosixPath(pathname); return fstatatZ(dirfd, &pathname_c, flags); } } /// WASI-only. Same as `fstatat` but targeting WASI. /// See also `fstatat`. pub fn fstatatWasi(dirfd: fd_t, pathname: []const u8, flags: u32) FStatAtError!Stat { var stat: wasi.filestat_t = undefined; switch (wasi.path_filestat_get(dirfd, flags, pathname.ptr, pathname.len, &stat)) { .SUCCESS => return Stat.fromFilestat(stat), .INVAL => unreachable, .BADF => unreachable, // Always a race condition. .NOMEM => return error.SystemResources, .ACCES => return error.AccessDenied, .FAULT => unreachable, .NAMETOOLONG => return error.NameTooLong, .NOENT => return error.FileNotFound, .NOTDIR => return error.FileNotFound, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } /// Same as `fstatat` but `pathname` is null-terminated. /// See also `fstatat`. pub fn fstatatZ(dirfd: fd_t, pathname: [*:0]const u8, flags: u32) FStatAtError!Stat { if (builtin.os.tag == .wasi and !builtin.link_libc) { return fstatatWasi(dirfd, mem.sliceTo(pathname), flags); } const fstatat_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.fstatat64 else system.fstatat; var stat = mem.zeroes(Stat); switch (errno(fstatat_sym(dirfd, pathname, &stat, flags))) { .SUCCESS => return stat, .INVAL => unreachable, .BADF => unreachable, // Always a race condition. .NOMEM => return error.SystemResources, .ACCES => return error.AccessDenied, .PERM => return error.AccessDenied, .FAULT => unreachable, .NAMETOOLONG => return error.NameTooLong, .LOOP => return error.SymLinkLoop, .NOENT => return error.FileNotFound, .NOTDIR => return error.FileNotFound, else => |err| return unexpectedErrno(err), } } pub const KQueueError = error{ /// The per-process limit on the number of open file descriptors has been reached. ProcessFdQuotaExceeded, /// The system-wide limit on the total number of open files has been reached. SystemFdQuotaExceeded, } || UnexpectedError; pub fn kqueue() KQueueError!i32 { const rc = system.kqueue(); switch (errno(rc)) { .SUCCESS => return @intCast(i32, rc), .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, else => |err| return unexpectedErrno(err), } } pub const KEventError = error{ /// The process does not have permission to register a filter. AccessDenied, /// The event could not be found to be modified or deleted. EventNotFound, /// No memory was available to register the event. SystemResources, /// The specified process to attach to does not exist. ProcessNotFound, /// changelist or eventlist had too many items on it. /// TODO remove this possibility Overflow, }; pub fn kevent( kq: i32, changelist: []const Kevent, eventlist: []Kevent, timeout: ?*const timespec, ) KEventError!usize { while (true) { const rc = system.kevent( kq, changelist.ptr, math.cast(c_int, changelist.len) orelse return error.Overflow, eventlist.ptr, math.cast(c_int, eventlist.len) orelse return error.Overflow, timeout, ); switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .ACCES => return error.AccessDenied, .FAULT => unreachable, .BADF => unreachable, // Always a race condition. .INTR => continue, .INVAL => unreachable, .NOENT => return error.EventNotFound, .NOMEM => return error.SystemResources, .SRCH => return error.ProcessNotFound, else => unreachable, } } } pub const INotifyInitError = error{ ProcessFdQuotaExceeded, SystemFdQuotaExceeded, SystemResources, } || UnexpectedError; /// initialize an inotify instance pub fn inotify_init1(flags: u32) INotifyInitError!i32 { const rc = system.inotify_init1(flags); switch (errno(rc)) { .SUCCESS => return @intCast(i32, rc), .INVAL => unreachable, .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } pub const INotifyAddWatchError = error{ AccessDenied, NameTooLong, FileNotFound, SystemResources, UserResourceLimitReached, NotDir, WatchAlreadyExists, } || UnexpectedError; /// add a watch to an initialized inotify instance pub fn inotify_add_watch(inotify_fd: i32, pathname: []const u8, mask: u32) INotifyAddWatchError!i32 { const pathname_c = try toPosixPath(pathname); return inotify_add_watchZ(inotify_fd, &pathname_c, mask); } /// Same as `inotify_add_watch` except pathname is null-terminated. pub fn inotify_add_watchZ(inotify_fd: i32, pathname: [*:0]const u8, mask: u32) INotifyAddWatchError!i32 { const rc = system.inotify_add_watch(inotify_fd, pathname, mask); switch (errno(rc)) { .SUCCESS => return @intCast(i32, rc), .ACCES => return error.AccessDenied, .BADF => unreachable, .FAULT => unreachable, .INVAL => unreachable, .NAMETOOLONG => return error.NameTooLong, .NOENT => return error.FileNotFound, .NOMEM => return error.SystemResources, .NOSPC => return error.UserResourceLimitReached, .NOTDIR => return error.NotDir, .EXIST => return error.WatchAlreadyExists, else => |err| return unexpectedErrno(err), } } /// remove an existing watch from an inotify instance pub fn inotify_rm_watch(inotify_fd: i32, wd: i32) void { switch (errno(system.inotify_rm_watch(inotify_fd, wd))) { .SUCCESS => return, .BADF => unreachable, .INVAL => unreachable, else => unreachable, } } pub const MProtectError = error{ /// The memory cannot be given the specified access. This can happen, for example, if you /// mmap(2) a file to which you have read-only access, then ask mprotect() to mark it /// PROT_WRITE. AccessDenied, /// Changing the protection of a memory region would result in the total number of map‐ /// pings with distinct attributes (e.g., read versus read/write protection) exceeding the /// allowed maximum. (For example, making the protection of a range PROT_READ in the mid‐ /// dle of a region currently protected as PROT_READ|PROT_WRITE would result in three map‐ /// pings: two read/write mappings at each end and a read-only mapping in the middle.) OutOfMemory, } || UnexpectedError; /// `memory.len` must be page-aligned. pub fn mprotect(memory: []align(mem.page_size) u8, protection: u32) MProtectError!void { assert(mem.isAligned(memory.len, mem.page_size)); switch (errno(system.mprotect(memory.ptr, memory.len, protection))) { .SUCCESS => return, .INVAL => unreachable, .ACCES => return error.AccessDenied, .NOMEM => return error.OutOfMemory, else => |err| return unexpectedErrno(err), } } pub const ForkError = error{SystemResources} || UnexpectedError; pub fn fork() ForkError!pid_t { const rc = system.fork(); switch (errno(rc)) { .SUCCESS => return @intCast(pid_t, rc), .AGAIN => return error.SystemResources, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } pub const MMapError = error{ /// The underlying filesystem of the specified file does not support memory mapping. MemoryMappingNotSupported, /// A file descriptor refers to a non-regular file. Or a file mapping was requested, /// but the file descriptor is not open for reading. Or `MAP.SHARED` was requested /// and `PROT_WRITE` is set, but the file descriptor is not open in `O.RDWR` mode. /// Or `PROT_WRITE` is set, but the file is append-only. AccessDenied, /// The `prot` argument asks for `PROT_EXEC` but the mapped area belongs to a file on /// a filesystem that was mounted no-exec. PermissionDenied, LockedMemoryLimitExceeded, OutOfMemory, } || UnexpectedError; /// Map files or devices into memory. /// `length` does not need to be aligned. /// Use of a mapped region can result in these signals: /// * SIGSEGV - Attempted write into a region mapped as read-only. /// * SIGBUS - Attempted access to a portion of the buffer that does not correspond to the file pub fn mmap( ptr: ?[*]align(mem.page_size) u8, length: usize, prot: u32, flags: u32, fd: fd_t, offset: u64, ) MMapError![]align(mem.page_size) u8 { const mmap_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.mmap64 else system.mmap; const ioffset = @bitCast(i64, offset); // the OS treats this as unsigned const rc = mmap_sym(ptr, length, prot, flags, fd, ioffset); const err = if (builtin.link_libc) blk: { if (rc != std.c.MAP.FAILED) return @ptrCast([*]align(mem.page_size) u8, @alignCast(mem.page_size, rc))[0..length]; break :blk @intToEnum(E, system._errno().*); } else blk: { const err = errno(rc); if (err == .SUCCESS) return @intToPtr([*]align(mem.page_size) u8, rc)[0..length]; break :blk err; }; switch (err) { .SUCCESS => unreachable, .TXTBSY => return error.AccessDenied, .ACCES => return error.AccessDenied, .PERM => return error.PermissionDenied, .AGAIN => return error.LockedMemoryLimitExceeded, .BADF => unreachable, // Always a race condition. .OVERFLOW => unreachable, // The number of pages used for length + offset would overflow. .NODEV => return error.MemoryMappingNotSupported, .INVAL => unreachable, // Invalid parameters to mmap() .NOMEM => return error.OutOfMemory, else => return unexpectedErrno(err), } } /// Deletes the mappings for the specified address range, causing /// further references to addresses within the range to generate invalid memory references. /// Note that while POSIX allows unmapping a region in the middle of an existing mapping, /// Zig's munmap function does not, for two reasons: /// * It violates the Zig principle that resource deallocation must succeed. /// * The Windows function, VirtualFree, has this restriction. pub fn munmap(memory: []align(mem.page_size) const u8) void { switch (errno(system.munmap(memory.ptr, memory.len))) { .SUCCESS => return, .INVAL => unreachable, // Invalid parameters. .NOMEM => unreachable, // Attempted to unmap a region in the middle of an existing mapping. else => unreachable, } } pub const MSyncError = error{ UnmappedMemory, } || UnexpectedError; pub fn msync(memory: []align(mem.page_size) u8, flags: i32) MSyncError!void { switch (errno(system.msync(memory.ptr, memory.len, flags))) { .SUCCESS => return, .NOMEM => return error.UnmappedMemory, // Unsuccessful, provided pointer does not point mapped memory .INVAL => unreachable, // Invalid parameters. else => unreachable, } } pub const AccessError = error{ PermissionDenied, FileNotFound, NameTooLong, InputOutput, SystemResources, BadPathName, FileBusy, SymLinkLoop, ReadOnlyFileSystem, /// On Windows, file paths must be valid Unicode. InvalidUtf8, } || UnexpectedError; /// check user's permissions for a file /// TODO currently this assumes `mode` is `F.OK` on Windows. pub fn access(path: []const u8, mode: u32) AccessError!void { if (builtin.os.tag == .windows) { const path_w = try windows.sliceToPrefixedFileW(path); _ = try windows.GetFileAttributesW(path_w.span().ptr); return; } else if (builtin.os.tag == .wasi and !builtin.link_libc) { return faccessat(wasi.AT.FDCWD, path, mode, 0); } const path_c = try toPosixPath(path); return accessZ(&path_c, mode); } /// Same as `access` except `path` is null-terminated. pub fn accessZ(path: [*:0]const u8, mode: u32) AccessError!void { if (builtin.os.tag == .windows) { const path_w = try windows.cStrToPrefixedFileW(path); _ = try windows.GetFileAttributesW(path_w.span().ptr); return; } else if (builtin.os.tag == .wasi and !builtin.link_libc) { return access(mem.sliceTo(path, 0), mode); } switch (errno(system.access(path, mode))) { .SUCCESS => return, .ACCES => return error.PermissionDenied, .ROFS => return error.ReadOnlyFileSystem, .LOOP => return error.SymLinkLoop, .TXTBSY => return error.FileBusy, .NOTDIR => return error.FileNotFound, .NOENT => return error.FileNotFound, .NAMETOOLONG => return error.NameTooLong, .INVAL => unreachable, .FAULT => unreachable, .IO => return error.InputOutput, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } /// Call from Windows-specific code if you already have a UTF-16LE encoded, null terminated string. /// Otherwise use `access` or `accessC`. /// TODO currently this ignores `mode`. pub fn accessW(path: [*:0]const u16, mode: u32) windows.GetFileAttributesError!void { _ = mode; const ret = try windows.GetFileAttributesW(path); if (ret != windows.INVALID_FILE_ATTRIBUTES) { return; } switch (windows.kernel32.GetLastError()) { .FILE_NOT_FOUND => return error.FileNotFound, .PATH_NOT_FOUND => return error.FileNotFound, .ACCESS_DENIED => return error.PermissionDenied, else => |err| return windows.unexpectedError(err), } } /// Check user's permissions for a file, based on an open directory handle. /// TODO currently this ignores `mode` and `flags` on Windows. pub fn faccessat(dirfd: fd_t, path: []const u8, mode: u32, flags: u32) AccessError!void { if (builtin.os.tag == .windows) { const path_w = try windows.sliceToPrefixedFileW(path); return faccessatW(dirfd, path_w.span().ptr, mode, flags); } else if (builtin.os.tag == .wasi and !builtin.link_libc) { var resolved = RelativePathWasi{ .dir_fd = dirfd, .relative_path = path }; const file = blk: { if (dirfd == wasi.AT.FDCWD or fs.path.isAbsolute(path)) { // Resolve absolute or CWD-relative paths to a path within a Preopen var path_buf: [MAX_PATH_BYTES]u8 = undefined; resolved = resolvePathWasi(path, &path_buf) catch |err| break :blk @as(FStatAtError!Stat, err); break :blk fstatat(resolved.dir_fd, resolved.relative_path, flags); } break :blk fstatat(dirfd, path, flags); } catch |err| switch (err) { error.AccessDenied => return error.PermissionDenied, else => |e| return e, }; if (mode != F_OK) { var directory: wasi.fdstat_t = undefined; if (wasi.fd_fdstat_get(resolved.dir_fd, &directory) != .SUCCESS) { return error.PermissionDenied; } var rights: wasi.rights_t = 0; if (mode & R_OK != 0) { rights |= if (file.filetype == .DIRECTORY) wasi.RIGHT.FD_READDIR else wasi.RIGHT.FD_READ; } if (mode & W_OK != 0) { rights |= wasi.RIGHT.FD_WRITE; } // No validation for X_OK if ((rights & directory.fs_rights_inheriting) != rights) { return error.PermissionDenied; } } return; } const path_c = try toPosixPath(path); return faccessatZ(dirfd, &path_c, mode, flags); } /// Same as `faccessat` except the path parameter is null-terminated. pub fn faccessatZ(dirfd: fd_t, path: [*:0]const u8, mode: u32, flags: u32) AccessError!void { if (builtin.os.tag == .windows) { const path_w = try windows.cStrToPrefixedFileW(path); return faccessatW(dirfd, path_w.span().ptr, mode, flags); } else if (builtin.os.tag == .wasi and !builtin.link_libc) { return faccessat(dirfd, mem.sliceTo(path, 0), mode, flags); } switch (errno(system.faccessat(dirfd, path, mode, flags))) { .SUCCESS => return, .ACCES => return error.PermissionDenied, .ROFS => return error.ReadOnlyFileSystem, .LOOP => return error.SymLinkLoop, .TXTBSY => return error.FileBusy, .NOTDIR => return error.FileNotFound, .NOENT => return error.FileNotFound, .NAMETOOLONG => return error.NameTooLong, .INVAL => unreachable, .FAULT => unreachable, .IO => return error.InputOutput, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } /// Same as `faccessat` except asserts the target is Windows and the path parameter /// is NtDll-prefixed, null-terminated, WTF-16 encoded. /// TODO currently this ignores `mode` and `flags` pub fn faccessatW(dirfd: fd_t, sub_path_w: [*:0]const u16, mode: u32, flags: u32) AccessError!void { _ = mode; _ = flags; if (sub_path_w[0] == '.' and sub_path_w[1] == 0) { return; } if (sub_path_w[0] == '.' and sub_path_w[1] == '.' and sub_path_w[2] == 0) { return; } const path_len_bytes = math.cast(u16, mem.sliceTo(sub_path_w, 0).len * 2) orelse return error.NameTooLong; var nt_name = windows.UNICODE_STRING{ .Length = path_len_bytes, .MaximumLength = path_len_bytes, .Buffer = @intToPtr([*]u16, @ptrToInt(sub_path_w)), }; var attr = windows.OBJECT_ATTRIBUTES{ .Length = @sizeOf(windows.OBJECT_ATTRIBUTES), .RootDirectory = if (std.fs.path.isAbsoluteWindowsW(sub_path_w)) null else dirfd, .Attributes = 0, // Note we do not use OBJ_CASE_INSENSITIVE here. .ObjectName = &nt_name, .SecurityDescriptor = null, .SecurityQualityOfService = null, }; var basic_info: windows.FILE_BASIC_INFORMATION = undefined; switch (windows.ntdll.NtQueryAttributesFile(&attr, &basic_info)) { .SUCCESS => return, .OBJECT_NAME_NOT_FOUND => return error.FileNotFound, .OBJECT_PATH_NOT_FOUND => return error.FileNotFound, .OBJECT_NAME_INVALID => unreachable, .INVALID_PARAMETER => unreachable, .ACCESS_DENIED => return error.PermissionDenied, .OBJECT_PATH_SYNTAX_BAD => unreachable, else => |rc| return windows.unexpectedStatus(rc), } } pub const PipeError = error{ SystemFdQuotaExceeded, ProcessFdQuotaExceeded, } || UnexpectedError; /// Creates a unidirectional data channel that can be used for interprocess communication. pub fn pipe() PipeError![2]fd_t { var fds: [2]fd_t = undefined; switch (errno(system.pipe(&fds))) { .SUCCESS => return fds, .INVAL => unreachable, // Invalid parameters to pipe() .FAULT => unreachable, // Invalid fds pointer .NFILE => return error.SystemFdQuotaExceeded, .MFILE => return error.ProcessFdQuotaExceeded, else => |err| return unexpectedErrno(err), } } pub fn pipe2(flags: u32) PipeError![2]fd_t { if (@hasDecl(system, "pipe2")) { var fds: [2]fd_t = undefined; switch (errno(system.pipe2(&fds, flags))) { .SUCCESS => return fds, .INVAL => unreachable, // Invalid flags .FAULT => unreachable, // Invalid fds pointer .NFILE => return error.SystemFdQuotaExceeded, .MFILE => return error.ProcessFdQuotaExceeded, else => |err| return unexpectedErrno(err), } } var fds: [2]fd_t = try pipe(); errdefer { close(fds[0]); close(fds[1]); } if (flags == 0) return fds; // O.CLOEXEC is special, it's a file descriptor flag and must be set using // F.SETFD. if (flags & O.CLOEXEC != 0) { for (fds) |fd| { switch (errno(system.fcntl(fd, F.SETFD, @as(u32, FD_CLOEXEC)))) { .SUCCESS => {}, .INVAL => unreachable, // Invalid flags .BADF => unreachable, // Always a race condition else => |err| return unexpectedErrno(err), } } } const new_flags = flags & ~@as(u32, O.CLOEXEC); // Set every other flag affecting the file status using F.SETFL. if (new_flags != 0) { for (fds) |fd| { switch (errno(system.fcntl(fd, F.SETFL, new_flags))) { .SUCCESS => {}, .INVAL => unreachable, // Invalid flags .BADF => unreachable, // Always a race condition else => |err| return unexpectedErrno(err), } } } return fds; } pub const SysCtlError = error{ PermissionDenied, SystemResources, NameTooLong, UnknownName, } || UnexpectedError; pub fn sysctl( name: []const c_int, oldp: ?*anyopaque, oldlenp: ?*usize, newp: ?*anyopaque, newlen: usize, ) SysCtlError!void { if (builtin.os.tag == .wasi) { @panic("unsupported"); // TODO should be compile error, not panic } if (builtin.os.tag == .haiku) { @panic("unsupported"); // TODO should be compile error, not panic } const name_len = math.cast(c_uint, name.len) orelse return error.NameTooLong; switch (errno(system.sysctl(name.ptr, name_len, oldp, oldlenp, newp, newlen))) { .SUCCESS => return, .FAULT => unreachable, .PERM => return error.PermissionDenied, .NOMEM => return error.SystemResources, .NOENT => return error.UnknownName, else => |err| return unexpectedErrno(err), } } pub fn sysctlbynameZ( name: [*:0]const u8, oldp: ?*anyopaque, oldlenp: ?*usize, newp: ?*anyopaque, newlen: usize, ) SysCtlError!void { if (builtin.os.tag == .wasi) { @panic("unsupported"); // TODO should be compile error, not panic } if (builtin.os.tag == .haiku) { @panic("unsupported"); // TODO should be compile error, not panic } switch (errno(system.sysctlbyname(name, oldp, oldlenp, newp, newlen))) { .SUCCESS => return, .FAULT => unreachable, .PERM => return error.PermissionDenied, .NOMEM => return error.SystemResources, .NOENT => return error.UnknownName, else => |err| return unexpectedErrno(err), } } pub fn gettimeofday(tv: ?*timeval, tz: ?*timezone) void { switch (errno(system.gettimeofday(tv, tz))) { .SUCCESS => return, .INVAL => unreachable, else => unreachable, } } pub const SeekError = error{ Unseekable, /// In WASI, this error may occur when the file descriptor does /// not hold the required rights to seek on it. AccessDenied, } || UnexpectedError; /// Repositions read/write file offset relative to the beginning. pub fn lseek_SET(fd: fd_t, offset: u64) SeekError!void { if (builtin.os.tag == .linux and !builtin.link_libc and @sizeOf(usize) == 4) { var result: u64 = undefined; switch (errno(system.llseek(fd, offset, &result, SEEK.SET))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .windows) { return windows.SetFilePointerEx_BEGIN(fd, offset); } if (builtin.os.tag == .wasi and !builtin.link_libc) { var new_offset: wasi.filesize_t = undefined; switch (wasi.fd_seek(fd, @bitCast(wasi.filedelta_t, offset), .SET, &new_offset)) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } const lseek_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.lseek64 else system.lseek; const ioffset = @bitCast(i64, offset); // the OS treats this as unsigned switch (errno(lseek_sym(fd, ioffset, SEEK.SET))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } /// Repositions read/write file offset relative to the current offset. pub fn lseek_CUR(fd: fd_t, offset: i64) SeekError!void { if (builtin.os.tag == .linux and !builtin.link_libc and @sizeOf(usize) == 4) { var result: u64 = undefined; switch (errno(system.llseek(fd, @bitCast(u64, offset), &result, SEEK.CUR))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .windows) { return windows.SetFilePointerEx_CURRENT(fd, offset); } if (builtin.os.tag == .wasi and !builtin.link_libc) { var new_offset: wasi.filesize_t = undefined; switch (wasi.fd_seek(fd, offset, .CUR, &new_offset)) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } const lseek_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.lseek64 else system.lseek; const ioffset = @bitCast(i64, offset); // the OS treats this as unsigned switch (errno(lseek_sym(fd, ioffset, SEEK.CUR))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } /// Repositions read/write file offset relative to the end. pub fn lseek_END(fd: fd_t, offset: i64) SeekError!void { if (builtin.os.tag == .linux and !builtin.link_libc and @sizeOf(usize) == 4) { var result: u64 = undefined; switch (errno(system.llseek(fd, @bitCast(u64, offset), &result, SEEK.END))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .windows) { return windows.SetFilePointerEx_END(fd, offset); } if (builtin.os.tag == .wasi and !builtin.link_libc) { var new_offset: wasi.filesize_t = undefined; switch (wasi.fd_seek(fd, offset, .END, &new_offset)) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } const lseek_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.lseek64 else system.lseek; const ioffset = @bitCast(i64, offset); // the OS treats this as unsigned switch (errno(lseek_sym(fd, ioffset, SEEK.END))) { .SUCCESS => return, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } /// Returns the read/write file offset relative to the beginning. pub fn lseek_CUR_get(fd: fd_t) SeekError!u64 { if (builtin.os.tag == .linux and !builtin.link_libc and @sizeOf(usize) == 4) { var result: u64 = undefined; switch (errno(system.llseek(fd, 0, &result, SEEK.CUR))) { .SUCCESS => return result, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .windows) { return windows.SetFilePointerEx_CURRENT_get(fd); } if (builtin.os.tag == .wasi and !builtin.link_libc) { var new_offset: wasi.filesize_t = undefined; switch (wasi.fd_seek(fd, 0, .CUR, &new_offset)) { .SUCCESS => return new_offset, .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, .NOTCAPABLE => return error.AccessDenied, else => |err| return unexpectedErrno(err), } } const lseek_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.lseek64 else system.lseek; const rc = lseek_sym(fd, 0, SEEK.CUR); switch (errno(rc)) { .SUCCESS => return @bitCast(u64, rc), .BADF => unreachable, // always a race condition .INVAL => return error.Unseekable, .OVERFLOW => return error.Unseekable, .SPIPE => return error.Unseekable, .NXIO => return error.Unseekable, else => |err| return unexpectedErrno(err), } } pub const FcntlError = error{ PermissionDenied, FileBusy, ProcessFdQuotaExceeded, Locked, DeadLock, LockedRegionLimitExceeded, } || UnexpectedError; pub fn fcntl(fd: fd_t, cmd: i32, arg: usize) FcntlError!usize { while (true) { const rc = system.fcntl(fd, cmd, arg); switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .INTR => continue, .AGAIN, .ACCES => return error.Locked, .BADF => unreachable, .BUSY => return error.FileBusy, .INVAL => unreachable, // invalid parameters .PERM => return error.PermissionDenied, .MFILE => return error.ProcessFdQuotaExceeded, .NOTDIR => unreachable, // invalid parameter .DEADLK => return error.DeadLock, .NOLCK => return error.LockedRegionLimitExceeded, else => |err| return unexpectedErrno(err), } } } fn setSockFlags(sock: socket_t, flags: u32) !void { if ((flags & SOCK.CLOEXEC) != 0) { if (builtin.os.tag == .windows) { // TODO: Find out if this is supported for sockets } else { var fd_flags = fcntl(sock, F.GETFD, 0) catch |err| switch (err) { error.FileBusy => unreachable, error.Locked => unreachable, error.PermissionDenied => unreachable, error.DeadLock => unreachable, error.LockedRegionLimitExceeded => unreachable, else => |e| return e, }; fd_flags |= FD_CLOEXEC; _ = fcntl(sock, F.SETFD, fd_flags) catch |err| switch (err) { error.FileBusy => unreachable, error.Locked => unreachable, error.PermissionDenied => unreachable, error.DeadLock => unreachable, error.LockedRegionLimitExceeded => unreachable, else => |e| return e, }; } } if ((flags & SOCK.NONBLOCK) != 0) { if (builtin.os.tag == .windows) { var mode: c_ulong = 1; if (windows.ws2_32.ioctlsocket(sock, windows.ws2_32.FIONBIO, &mode) == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENOTSOCK => return error.FileDescriptorNotASocket, // TODO: handle more errors else => |err| return windows.unexpectedWSAError(err), } } } else { var fl_flags = fcntl(sock, F.GETFL, 0) catch |err| switch (err) { error.FileBusy => unreachable, error.Locked => unreachable, error.PermissionDenied => unreachable, error.DeadLock => unreachable, error.LockedRegionLimitExceeded => unreachable, else => |e| return e, }; fl_flags |= O.NONBLOCK; _ = fcntl(sock, F.SETFL, fl_flags) catch |err| switch (err) { error.FileBusy => unreachable, error.Locked => unreachable, error.PermissionDenied => unreachable, error.DeadLock => unreachable, error.LockedRegionLimitExceeded => unreachable, else => |e| return e, }; } } } pub const FlockError = error{ WouldBlock, /// The kernel ran out of memory for allocating file locks SystemResources, /// The underlying filesystem does not support file locks FileLocksNotSupported, } || UnexpectedError; /// Depending on the operating system `flock` may or may not interact with /// `fcntl` locks made by other processes. pub fn flock(fd: fd_t, operation: i32) FlockError!void { while (true) { const rc = system.flock(fd, operation); switch (errno(rc)) { .SUCCESS => return, .BADF => unreachable, .INTR => continue, .INVAL => unreachable, // invalid parameters .NOLCK => return error.SystemResources, .AGAIN => return error.WouldBlock, // TODO: integrate with async instead of just returning an error .OPNOTSUPP => return error.FileLocksNotSupported, else => |err| return unexpectedErrno(err), } } } pub const RealPathError = error{ FileNotFound, AccessDenied, NameTooLong, NotSupported, NotDir, SymLinkLoop, InputOutput, FileTooBig, IsDir, ProcessFdQuotaExceeded, SystemFdQuotaExceeded, NoDevice, SystemResources, NoSpaceLeft, FileSystem, BadPathName, DeviceBusy, SharingViolation, PipeBusy, /// On WASI, the current CWD may not be associated with an absolute path. InvalidHandle, /// On Windows, file paths must be valid Unicode. InvalidUtf8, PathAlreadyExists, } || UnexpectedError; /// Return the canonicalized absolute pathname. /// Expands all symbolic links and resolves references to `.`, `..`, and /// extra `/` characters in `pathname`. /// The return value is a slice of `out_buffer`, but not necessarily from the beginning. /// See also `realpathZ` and `realpathW`. pub fn realpath(pathname: []const u8, out_buffer: *[MAX_PATH_BYTES]u8) RealPathError![]u8 { if (builtin.os.tag == .windows) { const pathname_w = try windows.sliceToPrefixedFileW(pathname); return realpathW(pathname_w.span(), out_buffer); } else if (builtin.os.tag == .wasi and !builtin.link_libc) { var alloc = std.heap.FixedBufferAllocator.init(out_buffer); // NOTE: This emulation is incomplete. Symbolic links are not // currently expanded during path canonicalization. const paths = &.{ wasi_cwd.cwd, pathname }; return fs.path.resolve(alloc.allocator(), paths) catch error.NameTooLong; } const pathname_c = try toPosixPath(pathname); return realpathZ(&pathname_c, out_buffer); } /// Same as `realpath` except `pathname` is null-terminated. pub fn realpathZ(pathname: [*:0]const u8, out_buffer: *[MAX_PATH_BYTES]u8) RealPathError![]u8 { if (builtin.os.tag == .windows) { const pathname_w = try windows.cStrToPrefixedFileW(pathname); return realpathW(pathname_w.span(), out_buffer); } else if (builtin.os.tag == .wasi and !builtin.link_libc) { return realpath(mem.sliceTo(pathname, 0), out_buffer); } if (!builtin.link_libc) { const flags = if (builtin.os.tag == .linux) O.PATH | O.NONBLOCK | O.CLOEXEC else O.NONBLOCK | O.CLOEXEC; const fd = openZ(pathname, flags, 0) catch |err| switch (err) { error.FileLocksNotSupported => unreachable, error.WouldBlock => unreachable, error.FileBusy => unreachable, // not asking for write permissions error.InvalidHandle => unreachable, // WASI-only else => |e| return e, }; defer close(fd); return getFdPath(fd, out_buffer); } const result_path = std.c.realpath(pathname, out_buffer) orelse switch (@intToEnum(E, std.c._errno().*)) { .SUCCESS => unreachable, .INVAL => unreachable, .BADF => unreachable, .FAULT => unreachable, .ACCES => return error.AccessDenied, .NOENT => return error.FileNotFound, .OPNOTSUPP => return error.NotSupported, .NOTDIR => return error.NotDir, .NAMETOOLONG => return error.NameTooLong, .LOOP => return error.SymLinkLoop, .IO => return error.InputOutput, else => |err| return unexpectedErrno(err), }; return mem.sliceTo(result_path, 0); } /// Same as `realpath` except `pathname` is UTF16LE-encoded. pub fn realpathW(pathname: []const u16, out_buffer: *[MAX_PATH_BYTES]u8) RealPathError![]u8 { const w = windows; const dir = std.fs.cwd().fd; const access_mask = w.GENERIC_READ | w.SYNCHRONIZE; const share_access = w.FILE_SHARE_READ; const creation = w.FILE_OPEN; const h_file = blk: { const res = w.OpenFile(pathname, .{ .dir = dir, .access_mask = access_mask, .share_access = share_access, .creation = creation, .io_mode = .blocking, }) catch |err| switch (err) { error.IsDir => break :blk w.OpenFile(pathname, .{ .dir = dir, .access_mask = access_mask, .share_access = share_access, .creation = creation, .io_mode = .blocking, .filter = .dir_only, }) catch |er| switch (er) { error.WouldBlock => unreachable, else => |e2| return e2, }, error.WouldBlock => unreachable, else => |e| return e, }; break :blk res; }; defer w.CloseHandle(h_file); return getFdPath(h_file, out_buffer); } /// Return canonical path of handle `fd`. /// This function is very host-specific and is not universally supported by all hosts. /// For example, while it generally works on Linux, macOS, FreeBSD or Windows, it is /// unsupported on WASI. pub fn getFdPath(fd: fd_t, out_buffer: *[MAX_PATH_BYTES]u8) RealPathError![]u8 { switch (builtin.os.tag) { .windows => { var wide_buf: [windows.PATH_MAX_WIDE]u16 = undefined; const wide_slice = try windows.GetFinalPathNameByHandle(fd, .{}, wide_buf[0..]); // Trust that Windows gives us valid UTF-16LE. const end_index = std.unicode.utf16leToUtf8(out_buffer, wide_slice) catch unreachable; return out_buffer[0..end_index]; }, .macos, .ios, .watchos, .tvos => { // On macOS, we can use F.GETPATH fcntl command to query the OS for // the path to the file descriptor. @memset(out_buffer, 0, MAX_PATH_BYTES); switch (errno(system.fcntl(fd, F.GETPATH, out_buffer))) { .SUCCESS => {}, .BADF => return error.FileNotFound, .NOSPC => return error.NameTooLong, // TODO man pages for fcntl on macOS don't really tell you what // errno values to expect when command is F.GETPATH... else => |err| return unexpectedErrno(err), } const len = mem.indexOfScalar(u8, out_buffer[0..], @as(u8, 0)) orelse MAX_PATH_BYTES; return out_buffer[0..len]; }, .linux => { var procfs_buf: ["/proc/self/fd/-2147483648".len:0]u8 = undefined; const proc_path = std.fmt.bufPrint(procfs_buf[0..], "/proc/self/fd/{d}\x00", .{fd}) catch unreachable; const target = readlinkZ(std.meta.assumeSentinel(proc_path.ptr, 0), out_buffer) catch |err| { switch (err) { error.UnsupportedReparsePointType => unreachable, // Windows only, error.NotLink => unreachable, else => |e| return e, } }; return target; }, .solaris => { var procfs_buf: ["/proc/self/path/-2147483648".len:0]u8 = undefined; const proc_path = std.fmt.bufPrintZ(procfs_buf[0..], "/proc/self/path/{d}", .{fd}) catch unreachable; const target = readlinkZ(proc_path, out_buffer) catch |err| switch (err) { error.UnsupportedReparsePointType => unreachable, error.NotLink => unreachable, else => |e| return e, }; return target; }, .freebsd => { if (comptime builtin.os.version_range.semver.max.order(.{ .major = 13, .minor = 0 }) == .gt) { var kfile: system.kinfo_file = undefined; kfile.structsize = system.KINFO_FILE_SIZE; switch (errno(system.fcntl(fd, system.F.KINFO, @ptrToInt(&kfile)))) { .SUCCESS => {}, .BADF => return error.FileNotFound, else => |err| return unexpectedErrno(err), } const len = mem.indexOfScalar(u8, &kfile.path, 0) orelse MAX_PATH_BYTES; if (len == 0) return error.NameTooLong; mem.copy(u8, out_buffer, kfile.path[0..len]); return out_buffer[0..len]; } else { // This fallback implementation reimplements libutil's `kinfo_getfile()`. // The motivation is to avoid linking -lutil when building zig or general // user executables. var mib = [4]c_int{ CTL.KERN, KERN.PROC, KERN.PROC_FILEDESC, system.getpid() }; var len: usize = undefined; sysctl(&mib, null, &len, null, 0) catch |err| switch (err) { error.PermissionDenied => unreachable, error.SystemResources => return error.SystemResources, error.NameTooLong => unreachable, error.UnknownName => unreachable, else => return error.Unexpected, }; len = len * 4 / 3; const buf = std.heap.c_allocator.alloc(u8, len) catch return error.SystemResources; defer std.heap.c_allocator.free(buf); len = buf.len; sysctl(&mib, &buf[0], &len, null, 0) catch |err| switch (err) { error.PermissionDenied => unreachable, error.SystemResources => return error.SystemResources, error.NameTooLong => unreachable, error.UnknownName => unreachable, else => return error.Unexpected, }; var i: usize = 0; while (i < len) { const kf: *align(1) system.kinfo_file = @ptrCast(*align(1) system.kinfo_file, &buf[i]); if (kf.fd == fd) { len = mem.indexOfScalar(u8, &kf.path, 0) orelse MAX_PATH_BYTES; if (len == 0) return error.NameTooLong; mem.copy(u8, out_buffer, kf.path[0..len]); return out_buffer[0..len]; } i += @intCast(usize, kf.structsize); } return error.InvalidHandle; } }, .dragonfly => { if (comptime builtin.os.version_range.semver.max.order(.{ .major = 6, .minor = 0 }) == .lt) { @compileError("querying for canonical path of a handle is unsupported on this host"); } @memset(out_buffer, 0, MAX_PATH_BYTES); switch (errno(system.fcntl(fd, F.GETPATH, out_buffer))) { .SUCCESS => {}, .BADF => return error.FileNotFound, .RANGE => return error.NameTooLong, else => |err| return unexpectedErrno(err), } const len = mem.indexOfScalar(u8, out_buffer[0..], @as(u8, 0)) orelse MAX_PATH_BYTES; return out_buffer[0..len]; }, .netbsd => { if (comptime builtin.os.version_range.semver.max.order(.{ .major = 10, .minor = 0 }) == .lt) { @compileError("querying for canonical path of a handle is unsupported on this host"); } @memset(out_buffer, 0, MAX_PATH_BYTES); switch (errno(system.fcntl(fd, F.GETPATH, out_buffer))) { .SUCCESS => {}, .ACCES => return error.AccessDenied, .BADF => return error.FileNotFound, .NOENT => return error.FileNotFound, .NOMEM => return error.SystemResources, .RANGE => return error.NameTooLong, else => |err| return unexpectedErrno(err), } const len = mem.indexOfScalar(u8, out_buffer[0..], @as(u8, 0)) orelse MAX_PATH_BYTES; return out_buffer[0..len]; }, else => @compileError("querying for canonical path of a handle is unsupported on this host"), } } /// Spurious wakeups are possible and no precision of timing is guaranteed. pub fn nanosleep(seconds: u64, nanoseconds: u64) void { var req = timespec{ .tv_sec = math.cast(isize, seconds) orelse math.maxInt(isize), .tv_nsec = math.cast(isize, nanoseconds) orelse math.maxInt(isize), }; var rem: timespec = undefined; while (true) { switch (errno(system.nanosleep(&req, &rem))) { .FAULT => unreachable, .INVAL => { // Sometimes Darwin returns EINVAL for no reason. // We treat it as a spurious wakeup. return; }, .INTR => { req = rem; continue; }, // This prong handles success as well as unexpected errors. else => return, } } } pub fn dl_iterate_phdr( context: anytype, comptime Error: type, comptime callback: fn (info: *dl_phdr_info, size: usize, context: @TypeOf(context)) Error!void, ) Error!void { const Context = @TypeOf(context); if (builtin.object_format != .elf) @compileError("dl_iterate_phdr is not available for this target"); if (builtin.link_libc) { switch (system.dl_iterate_phdr(struct { fn callbackC(info: *dl_phdr_info, size: usize, data: ?*anyopaque) callconv(.C) c_int { const context_ptr = @ptrCast(*const Context, @alignCast(@alignOf(*const Context), data)); callback(info, size, context_ptr.*) catch |err| return @errorToInt(err); return 0; } }.callbackC, @intToPtr(?*anyopaque, @ptrToInt(&context)))) { 0 => return, else => |err| return @errSetCast(Error, @intToError(@intCast(u16, err))), // TODO don't hardcode u16 } } const elf_base = std.process.getBaseAddress(); const ehdr = @intToPtr(*elf.Ehdr, elf_base); // Make sure the base address points to an ELF image. assert(mem.eql(u8, ehdr.e_ident[0..4], elf.MAGIC)); const n_phdr = ehdr.e_phnum; const phdrs = (@intToPtr([*]elf.Phdr, elf_base + ehdr.e_phoff))[0..n_phdr]; var it = dl.linkmap_iterator(phdrs) catch unreachable; // The executable has no dynamic link segment, create a single entry for // the whole ELF image. if (it.end()) { // Find the base address for the ELF image, if this is a PIE the value // is non-zero. const base_address = for (phdrs) |*phdr| { if (phdr.p_type == elf.PT_PHDR) { break @ptrToInt(phdrs.ptr) - phdr.p_vaddr; // We could try computing the difference between _DYNAMIC and // the p_vaddr of the PT_DYNAMIC section, but using the phdr is // good enough (Is it?). } } else unreachable; var info = dl_phdr_info{ .dlpi_addr = base_address, .dlpi_name = "/proc/self/exe", .dlpi_phdr = phdrs.ptr, .dlpi_phnum = ehdr.e_phnum, }; return callback(&info, @sizeOf(dl_phdr_info), context); } // Last return value from the callback function. while (it.next()) |entry| { var dlpi_phdr: [*]elf.Phdr = undefined; var dlpi_phnum: u16 = undefined; if (entry.l_addr != 0) { const elf_header = @intToPtr(*elf.Ehdr, entry.l_addr); dlpi_phdr = @intToPtr([*]elf.Phdr, entry.l_addr + elf_header.e_phoff); dlpi_phnum = elf_header.e_phnum; } else { // This is the running ELF image dlpi_phdr = @intToPtr([*]elf.Phdr, elf_base + ehdr.e_phoff); dlpi_phnum = ehdr.e_phnum; } var info = dl_phdr_info{ .dlpi_addr = entry.l_addr, .dlpi_name = entry.l_name, .dlpi_phdr = dlpi_phdr, .dlpi_phnum = dlpi_phnum, }; try callback(&info, @sizeOf(dl_phdr_info), context); } } pub const ClockGetTimeError = error{UnsupportedClock} || UnexpectedError; /// TODO: change this to return the timespec as a return value /// TODO: look into making clk_id an enum pub fn clock_gettime(clk_id: i32, tp: *timespec) ClockGetTimeError!void { if (builtin.os.tag == .wasi and !builtin.link_libc) { var ts: timestamp_t = undefined; switch (system.clock_time_get(@bitCast(u32, clk_id), 1, &ts)) { .SUCCESS => { tp.* = .{ .tv_sec = @intCast(i64, ts / std.time.ns_per_s), .tv_nsec = @intCast(isize, ts % std.time.ns_per_s), }; }, .INVAL => return error.UnsupportedClock, else => |err| return unexpectedErrno(err), } return; } if (builtin.os.tag == .windows) { if (clk_id == CLOCK.REALTIME) { var ft: windows.FILETIME = undefined; windows.kernel32.GetSystemTimeAsFileTime(&ft); // FileTime has a granularity of 100 nanoseconds and uses the NTFS/Windows epoch. const ft64 = (@as(u64, ft.dwHighDateTime) << 32) | ft.dwLowDateTime; const ft_per_s = std.time.ns_per_s / 100; tp.* = .{ .tv_sec = @intCast(i64, ft64 / ft_per_s) + std.time.epoch.windows, .tv_nsec = @intCast(c_long, ft64 % ft_per_s) * 100, }; return; } else { // TODO POSIX implementation of CLOCK.MONOTONIC on Windows. return error.UnsupportedClock; } } switch (errno(system.clock_gettime(clk_id, tp))) { .SUCCESS => return, .FAULT => unreachable, .INVAL => return error.UnsupportedClock, else => |err| return unexpectedErrno(err), } } pub fn clock_getres(clk_id: i32, res: *timespec) ClockGetTimeError!void { if (builtin.os.tag == .wasi and !builtin.link_libc) { var ts: timestamp_t = undefined; switch (system.clock_res_get(@bitCast(u32, clk_id), &ts)) { .SUCCESS => res.* = .{ .tv_sec = @intCast(i64, ts / std.time.ns_per_s), .tv_nsec = @intCast(isize, ts % std.time.ns_per_s), }, .INVAL => return error.UnsupportedClock, else => |err| return unexpectedErrno(err), } return; } switch (errno(system.clock_getres(clk_id, res))) { .SUCCESS => return, .FAULT => unreachable, .INVAL => return error.UnsupportedClock, else => |err| return unexpectedErrno(err), } } pub const SchedGetAffinityError = error{PermissionDenied} || UnexpectedError; pub fn sched_getaffinity(pid: pid_t) SchedGetAffinityError!cpu_set_t { var set: cpu_set_t = undefined; switch (errno(system.sched_getaffinity(pid, @sizeOf(cpu_set_t), &set))) { .SUCCESS => return set, .FAULT => unreachable, .INVAL => unreachable, .SRCH => unreachable, .PERM => return error.PermissionDenied, else => |err| return unexpectedErrno(err), } } /// Used to convert a slice to a null terminated slice on the stack. /// TODO https://github.com/ziglang/zig/issues/287 pub fn toPosixPath(file_path: []const u8) ![MAX_PATH_BYTES - 1:0]u8 { if (std.debug.runtime_safety) assert(std.mem.indexOfScalar(u8, file_path, 0) == null); var path_with_null: [MAX_PATH_BYTES - 1:0]u8 = undefined; // >= rather than > to make room for the null byte if (file_path.len >= MAX_PATH_BYTES) return error.NameTooLong; mem.copy(u8, &path_with_null, file_path); path_with_null[file_path.len] = 0; return path_with_null; } /// Whether or not error.Unexpected will print its value and a stack trace. /// if this happens the fix is to add the error code to the corresponding /// switch expression, possibly introduce a new error in the error set, and /// send a patch to Zig. pub const unexpected_error_tracing = (builtin.zig_backend == .stage1 or builtin.zig_backend == .stage2_llvm) and builtin.mode == .Debug; pub const UnexpectedError = error{ /// The Operating System returned an undocumented error code. /// This error is in theory not possible, but it would be better /// to handle this error than to invoke undefined behavior. Unexpected, }; /// Call this when you made a syscall or something that sets errno /// and you get an unexpected error. pub fn unexpectedErrno(err: E) UnexpectedError { if (unexpected_error_tracing) { std.debug.print("unexpected errno: {d}\n", .{@enumToInt(err)}); std.debug.dumpCurrentStackTrace(null); } return error.Unexpected; } pub const SigaltstackError = error{ /// The supplied stack size was less than MINSIGSTKSZ. SizeTooSmall, /// Attempted to change the signal stack while it was active. PermissionDenied, } || UnexpectedError; pub fn sigaltstack(ss: ?*stack_t, old_ss: ?*stack_t) SigaltstackError!void { switch (errno(system.sigaltstack(ss, old_ss))) { .SUCCESS => return, .FAULT => unreachable, .INVAL => unreachable, .NOMEM => return error.SizeTooSmall, .PERM => return error.PermissionDenied, else => |err| return unexpectedErrno(err), } } /// Examine and change a signal action. pub fn sigaction(sig: u6, noalias act: ?*const Sigaction, noalias oact: ?*Sigaction) error{OperationNotSupported}!void { switch (errno(system.sigaction(sig, act, oact))) { .SUCCESS => return, .INVAL, .NOSYS => return error.OperationNotSupported, else => unreachable, } } /// Sets the thread signal mask. pub fn sigprocmask(flags: u32, noalias set: ?*const sigset_t, noalias oldset: ?*sigset_t) void { switch (errno(system.sigprocmask(flags, set, oldset))) { .SUCCESS => return, .FAULT => unreachable, .INVAL => unreachable, else => unreachable, } } pub const FutimensError = error{ /// times is NULL, or both tv_nsec values are UTIME_NOW, and either: /// * the effective user ID of the caller does not match the owner /// of the file, the caller does not have write access to the /// file, and the caller is not privileged (Linux: does not have /// either the CAP_FOWNER or the CAP_DAC_OVERRIDE capability); /// or, /// * the file is marked immutable (see chattr(1)). AccessDenied, /// The caller attempted to change one or both timestamps to a value /// other than the current time, or to change one of the timestamps /// to the current time while leaving the other timestamp unchanged, /// (i.e., times is not NULL, neither tv_nsec field is UTIME_NOW, /// and neither tv_nsec field is UTIME_OMIT) and either: /// * the caller's effective user ID does not match the owner of /// file, and the caller is not privileged (Linux: does not have /// the CAP_FOWNER capability); or, /// * the file is marked append-only or immutable (see chattr(1)). PermissionDenied, ReadOnlyFileSystem, } || UnexpectedError; pub fn futimens(fd: fd_t, times: *const [2]timespec) FutimensError!void { if (builtin.os.tag == .wasi and !builtin.link_libc) { // TODO WASI encodes `wasi.fstflags` to signify magic values // similar to UTIME_NOW and UTIME_OMIT. Currently, we ignore // this here, but we should really handle it somehow. const atim = times[0].toTimestamp(); const mtim = times[1].toTimestamp(); switch (wasi.fd_filestat_set_times(fd, atim, mtim, wasi.FILESTAT_SET_ATIM | wasi.FILESTAT_SET_MTIM)) { .SUCCESS => return, .ACCES => return error.AccessDenied, .PERM => return error.PermissionDenied, .BADF => unreachable, // always a race condition .FAULT => unreachable, .INVAL => unreachable, .ROFS => return error.ReadOnlyFileSystem, else => |err| return unexpectedErrno(err), } } switch (errno(system.futimens(fd, times))) { .SUCCESS => return, .ACCES => return error.AccessDenied, .PERM => return error.PermissionDenied, .BADF => unreachable, // always a race condition .FAULT => unreachable, .INVAL => unreachable, .ROFS => return error.ReadOnlyFileSystem, else => |err| return unexpectedErrno(err), } } pub const GetHostNameError = error{PermissionDenied} || UnexpectedError; pub fn gethostname(name_buffer: *[HOST_NAME_MAX]u8) GetHostNameError![]u8 { if (builtin.link_libc) { switch (errno(system.gethostname(name_buffer, name_buffer.len))) { .SUCCESS => return mem.sliceTo(std.meta.assumeSentinel(name_buffer, 0), 0), .FAULT => unreachable, .NAMETOOLONG => unreachable, // HOST_NAME_MAX prevents this .PERM => return error.PermissionDenied, else => |err| return unexpectedErrno(err), } } if (builtin.os.tag == .linux) { const uts = uname(); const hostname = mem.sliceTo(std.meta.assumeSentinel(&uts.nodename, 0), 0); mem.copy(u8, name_buffer, hostname); return name_buffer[0..hostname.len]; } @compileError("TODO implement gethostname for this OS"); } pub fn uname() utsname { var uts: utsname = undefined; switch (errno(system.uname(&uts))) { .SUCCESS => return uts, .FAULT => unreachable, else => unreachable, } } pub fn res_mkquery( op: u4, dname: []const u8, class: u8, ty: u8, data: []const u8, newrr: ?[*]const u8, buf: []u8, ) usize { _ = data; _ = newrr; // This implementation is ported from musl libc. // A more idiomatic "ziggy" implementation would be welcome. var name = dname; if (mem.endsWith(u8, name, ".")) name.len -= 1; assert(name.len <= 253); const n = 17 + name.len + @boolToInt(name.len != 0); // Construct query template - ID will be filled later var q: [280]u8 = undefined; @memset(&q, 0, n); q[2] = @as(u8, op) * 8 + 1; q[5] = 1; mem.copy(u8, q[13..], name); var i: usize = 13; var j: usize = undefined; while (q[i] != 0) : (i = j + 1) { j = i; while (q[j] != 0 and q[j] != '.') : (j += 1) {} // TODO determine the circumstances for this and whether or // not this should be an error. if (j - i - 1 > 62) unreachable; q[i - 1] = @intCast(u8, j - i); } q[i + 1] = ty; q[i + 3] = class; // Make a reasonably unpredictable id var ts: timespec = undefined; clock_gettime(CLOCK.REALTIME, &ts) catch {}; const UInt = std.meta.Int(.unsigned, @bitSizeOf(@TypeOf(ts.tv_nsec))); const unsec = @bitCast(UInt, ts.tv_nsec); const id = @truncate(u32, unsec + unsec / 65536); q[0] = @truncate(u8, id / 256); q[1] = @truncate(u8, id); mem.copy(u8, buf, q[0..n]); return n; } pub const SendError = error{ /// (For UNIX domain sockets, which are identified by pathname) Write permission is denied /// on the destination socket file, or search permission is denied for one of the /// directories the path prefix. (See path_resolution(7).) /// (For UDP sockets) An attempt was made to send to a network/broadcast address as though /// it was a unicast address. AccessDenied, /// The socket is marked nonblocking and the requested operation would block, and /// there is no global event loop configured. /// It's also possible to get this error under the following condition: /// (Internet domain datagram sockets) The socket referred to by sockfd had not previously /// been bound to an address and, upon attempting to bind it to an ephemeral port, it was /// determined that all port numbers in the ephemeral port range are currently in use. See /// the discussion of /proc/sys/net/ipv4/ip_local_port_range in ip(7). WouldBlock, /// Another Fast Open is already in progress. FastOpenAlreadyInProgress, /// Connection reset by peer. ConnectionResetByPeer, /// The socket type requires that message be sent atomically, and the size of the message /// to be sent made this impossible. The message is not transmitted. MessageTooBig, /// The output queue for a network interface was full. This generally indicates that the /// interface has stopped sending, but may be caused by transient congestion. (Normally, /// this does not occur in Linux. Packets are just silently dropped when a device queue /// overflows.) /// This is also caused when there is not enough kernel memory available. SystemResources, /// The local end has been shut down on a connection oriented socket. In this case, the /// process will also receive a SIGPIPE unless MSG.NOSIGNAL is set. BrokenPipe, FileDescriptorNotASocket, /// Network is unreachable. NetworkUnreachable, /// The local network interface used to reach the destination is down. NetworkSubsystemFailed, } || UnexpectedError; pub const SendMsgError = SendError || error{ /// The passed address didn't have the correct address family in its sa_family field. AddressFamilyNotSupported, /// Returned when socket is AF.UNIX and the given path has a symlink loop. SymLinkLoop, /// Returned when socket is AF.UNIX and the given path length exceeds `MAX_PATH_BYTES` bytes. NameTooLong, /// Returned when socket is AF.UNIX and the given path does not point to an existing file. FileNotFound, NotDir, /// The socket is not connected (connection-oriented sockets only). SocketNotConnected, AddressNotAvailable, }; pub fn sendmsg( /// The file descriptor of the sending socket. sockfd: socket_t, /// Message header and iovecs msg: msghdr_const, flags: u32, ) SendMsgError!usize { while (true) { const rc = system.sendmsg(sockfd, @ptrCast(*const std.x.os.Socket.Message, &msg), @intCast(c_int, flags)); if (builtin.os.tag == .windows) { if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSAEACCES => return error.AccessDenied, .WSAEADDRNOTAVAIL => return error.AddressNotAvailable, .WSAECONNRESET => return error.ConnectionResetByPeer, .WSAEMSGSIZE => return error.MessageTooBig, .WSAENOBUFS => return error.SystemResources, .WSAENOTSOCK => return error.FileDescriptorNotASocket, .WSAEAFNOSUPPORT => return error.AddressFamilyNotSupported, .WSAEDESTADDRREQ => unreachable, // A destination address is required. .WSAEFAULT => unreachable, // The lpBuffers, lpTo, lpOverlapped, lpNumberOfBytesSent, or lpCompletionRoutine parameters are not part of the user address space, or the lpTo parameter is too small. .WSAEHOSTUNREACH => return error.NetworkUnreachable, // TODO: WSAEINPROGRESS, WSAEINTR .WSAEINVAL => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENETRESET => return error.ConnectionResetByPeer, .WSAENETUNREACH => return error.NetworkUnreachable, .WSAENOTCONN => return error.SocketNotConnected, .WSAESHUTDOWN => unreachable, // The socket has been shut down; it is not possible to WSASendTo on a socket after shutdown has been invoked with how set to SD_SEND or SD_BOTH. .WSAEWOULDBLOCK => return error.WouldBlock, .WSANOTINITIALISED => unreachable, // A successful WSAStartup call must occur before using this function. else => |err| return windows.unexpectedWSAError(err), } } else { return @intCast(usize, rc); } } else { switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .ACCES => return error.AccessDenied, .AGAIN => return error.WouldBlock, .ALREADY => return error.FastOpenAlreadyInProgress, .BADF => unreachable, // always a race condition .CONNRESET => return error.ConnectionResetByPeer, .DESTADDRREQ => unreachable, // The socket is not connection-mode, and no peer address is set. .FAULT => unreachable, // An invalid user space address was specified for an argument. .INTR => continue, .INVAL => unreachable, // Invalid argument passed. .ISCONN => unreachable, // connection-mode socket was connected already but a recipient was specified .MSGSIZE => return error.MessageTooBig, .NOBUFS => return error.SystemResources, .NOMEM => return error.SystemResources, .NOTSOCK => unreachable, // The file descriptor sockfd does not refer to a socket. .OPNOTSUPP => unreachable, // Some bit in the flags argument is inappropriate for the socket type. .PIPE => return error.BrokenPipe, .AFNOSUPPORT => return error.AddressFamilyNotSupported, .LOOP => return error.SymLinkLoop, .NAMETOOLONG => return error.NameTooLong, .NOENT => return error.FileNotFound, .NOTDIR => return error.NotDir, .HOSTUNREACH => return error.NetworkUnreachable, .NETUNREACH => return error.NetworkUnreachable, .NOTCONN => return error.SocketNotConnected, .NETDOWN => return error.NetworkSubsystemFailed, else => |err| return unexpectedErrno(err), } } } } pub const SendToError = SendMsgError || error{ /// The destination address is not reachable by the bound address. UnreachableAddress, }; /// Transmit a message to another socket. /// /// The `sendto` call may be used only when the socket is in a connected state (so that the intended /// recipient is known). The following call /// /// send(sockfd, buf, len, flags); /// /// is equivalent to /// /// sendto(sockfd, buf, len, flags, NULL, 0); /// /// If sendto() is used on a connection-mode (`SOCK.STREAM`, `SOCK.SEQPACKET`) socket, the arguments /// `dest_addr` and `addrlen` are asserted to be `null` and `0` respectively, and asserted /// that the socket was actually connected. /// Otherwise, the address of the target is given by `dest_addr` with `addrlen` specifying its size. /// /// If the message is too long to pass atomically through the underlying protocol, /// `SendError.MessageTooBig` is returned, and the message is not transmitted. /// /// There is no indication of failure to deliver. /// /// When the message does not fit into the send buffer of the socket, `sendto` normally blocks, /// unless the socket has been placed in nonblocking I/O mode. In nonblocking mode it would fail /// with `SendError.WouldBlock`. The `select` call may be used to determine when it is /// possible to send more data. pub fn sendto( /// The file descriptor of the sending socket. sockfd: socket_t, /// Message to send. buf: []const u8, flags: u32, dest_addr: ?*const sockaddr, addrlen: socklen_t, ) SendToError!usize { while (true) { const rc = system.sendto(sockfd, buf.ptr, buf.len, flags, dest_addr, addrlen); if (builtin.os.tag == .windows) { if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSAEACCES => return error.AccessDenied, .WSAEADDRNOTAVAIL => return error.AddressNotAvailable, .WSAECONNRESET => return error.ConnectionResetByPeer, .WSAEMSGSIZE => return error.MessageTooBig, .WSAENOBUFS => return error.SystemResources, .WSAENOTSOCK => return error.FileDescriptorNotASocket, .WSAEAFNOSUPPORT => return error.AddressFamilyNotSupported, .WSAEDESTADDRREQ => unreachable, // A destination address is required. .WSAEFAULT => unreachable, // The lpBuffers, lpTo, lpOverlapped, lpNumberOfBytesSent, or lpCompletionRoutine parameters are not part of the user address space, or the lpTo parameter is too small. .WSAEHOSTUNREACH => return error.NetworkUnreachable, // TODO: WSAEINPROGRESS, WSAEINTR .WSAEINVAL => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENETRESET => return error.ConnectionResetByPeer, .WSAENETUNREACH => return error.NetworkUnreachable, .WSAENOTCONN => return error.SocketNotConnected, .WSAESHUTDOWN => unreachable, // The socket has been shut down; it is not possible to WSASendTo on a socket after shutdown has been invoked with how set to SD_SEND or SD_BOTH. .WSAEWOULDBLOCK => return error.WouldBlock, .WSANOTINITIALISED => unreachable, // A successful WSAStartup call must occur before using this function. else => |err| return windows.unexpectedWSAError(err), } } else { return @intCast(usize, rc); } } else { switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .ACCES => return error.AccessDenied, .AGAIN => return error.WouldBlock, .ALREADY => return error.FastOpenAlreadyInProgress, .BADF => unreachable, // always a race condition .CONNRESET => return error.ConnectionResetByPeer, .DESTADDRREQ => unreachable, // The socket is not connection-mode, and no peer address is set. .FAULT => unreachable, // An invalid user space address was specified for an argument. .INTR => continue, .INVAL => return error.UnreachableAddress, .ISCONN => unreachable, // connection-mode socket was connected already but a recipient was specified .MSGSIZE => return error.MessageTooBig, .NOBUFS => return error.SystemResources, .NOMEM => return error.SystemResources, .NOTSOCK => unreachable, // The file descriptor sockfd does not refer to a socket. .OPNOTSUPP => unreachable, // Some bit in the flags argument is inappropriate for the socket type. .PIPE => return error.BrokenPipe, .AFNOSUPPORT => return error.AddressFamilyNotSupported, .LOOP => return error.SymLinkLoop, .NAMETOOLONG => return error.NameTooLong, .NOENT => return error.FileNotFound, .NOTDIR => return error.NotDir, .HOSTUNREACH => return error.NetworkUnreachable, .NETUNREACH => return error.NetworkUnreachable, .NOTCONN => return error.SocketNotConnected, .NETDOWN => return error.NetworkSubsystemFailed, else => |err| return unexpectedErrno(err), } } } } /// Transmit a message to another socket. /// /// The `send` call may be used only when the socket is in a connected state (so that the intended /// recipient is known). The only difference between `send` and `write` is the presence of /// flags. With a zero flags argument, `send` is equivalent to `write`. Also, the following /// call /// /// send(sockfd, buf, len, flags); /// /// is equivalent to /// /// sendto(sockfd, buf, len, flags, NULL, 0); /// /// There is no indication of failure to deliver. /// /// When the message does not fit into the send buffer of the socket, `send` normally blocks, /// unless the socket has been placed in nonblocking I/O mode. In nonblocking mode it would fail /// with `SendError.WouldBlock`. The `select` call may be used to determine when it is /// possible to send more data. pub fn send( /// The file descriptor of the sending socket. sockfd: socket_t, buf: []const u8, flags: u32, ) SendError!usize { return sendto(sockfd, buf, flags, null, 0) catch |err| switch (err) { error.AddressFamilyNotSupported => unreachable, error.SymLinkLoop => unreachable, error.NameTooLong => unreachable, error.FileNotFound => unreachable, error.NotDir => unreachable, error.NetworkUnreachable => unreachable, error.AddressNotAvailable => unreachable, error.SocketNotConnected => unreachable, error.UnreachableAddress => unreachable, else => |e| return e, }; } pub const SendFileError = PReadError || WriteError || SendError; fn count_iovec_bytes(iovs: []const iovec_const) usize { var count: usize = 0; for (iovs) |iov| { count += iov.iov_len; } return count; } /// Transfer data between file descriptors, with optional headers and trailers. /// Returns the number of bytes written, which can be zero. /// /// The `sendfile` call copies `in_len` bytes from one file descriptor to another. When possible, /// this is done within the operating system kernel, which can provide better performance /// characteristics than transferring data from kernel to user space and back, such as with /// `read` and `write` calls. When `in_len` is `0`, it means to copy until the end of the input file has been /// reached. Note, however, that partial writes are still possible in this case. /// /// `in_fd` must be a file descriptor opened for reading, and `out_fd` must be a file descriptor /// opened for writing. They may be any kind of file descriptor; however, if `in_fd` is not a regular /// file system file, it may cause this function to fall back to calling `read` and `write`, in which case /// atomicity guarantees no longer apply. /// /// Copying begins reading at `in_offset`. The input file descriptor seek position is ignored and not updated. /// If the output file descriptor has a seek position, it is updated as bytes are written. When /// `in_offset` is past the end of the input file, it successfully reads 0 bytes. /// /// `flags` has different meanings per operating system; refer to the respective man pages. /// /// These systems support atomically sending everything, including headers and trailers: /// * macOS /// * FreeBSD /// /// These systems support in-kernel data copying, but headers and trailers are not sent atomically: /// * Linux /// /// Other systems fall back to calling `read` / `write`. /// /// Linux has a limit on how many bytes may be transferred in one `sendfile` call, which is `0x7ffff000` /// on both 64-bit and 32-bit systems. This is due to using a signed C int as the return value, as /// well as stuffing the errno codes into the last `4096` values. This is noted on the `sendfile` man page. /// The limit on Darwin is `0x7fffffff`, trying to write more than that returns EINVAL. /// The corresponding POSIX limit on this is `math.maxInt(isize)`. pub fn sendfile( out_fd: fd_t, in_fd: fd_t, in_offset: u64, in_len: u64, headers: []const iovec_const, trailers: []const iovec_const, flags: u32, ) SendFileError!usize { var header_done = false; var total_written: usize = 0; // Prevents EOVERFLOW. const size_t = std.meta.Int(.unsigned, @typeInfo(usize).Int.bits - 1); const max_count = switch (builtin.os.tag) { .linux => 0x7ffff000, .macos, .ios, .watchos, .tvos => math.maxInt(i32), else => math.maxInt(size_t), }; switch (builtin.os.tag) { .linux => sf: { // sendfile() first appeared in Linux 2.2, glibc 2.1. const call_sf = comptime if (builtin.link_libc) std.c.versionCheck(.{ .major = 2, .minor = 1 }).ok else builtin.os.version_range.linux.range.max.order(.{ .major = 2, .minor = 2 }) != .lt; if (!call_sf) break :sf; if (headers.len != 0) { const amt = try writev(out_fd, headers); total_written += amt; if (amt < count_iovec_bytes(headers)) return total_written; header_done = true; } // Here we match BSD behavior, making a zero count value send as many bytes as possible. const adjusted_count_tmp = if (in_len == 0) max_count else @min(in_len, @as(size_t, max_count)); // TODO we should not need this cast; improve return type of @min const adjusted_count = @intCast(usize, adjusted_count_tmp); const sendfile_sym = if (builtin.link_libc) system.sendfile64 else system.sendfile; while (true) { var offset: off_t = @bitCast(off_t, in_offset); const rc = sendfile_sym(out_fd, in_fd, &offset, adjusted_count); switch (errno(rc)) { .SUCCESS => { const amt = @bitCast(usize, rc); total_written += amt; if (in_len == 0 and amt == 0) { // We have detected EOF from `in_fd`. break; } else if (amt < in_len) { return total_written; } else { break; } }, .BADF => unreachable, // Always a race condition. .FAULT => unreachable, // Segmentation fault. .OVERFLOW => unreachable, // We avoid passing too large of a `count`. .NOTCONN => unreachable, // `out_fd` is an unconnected socket. .INVAL, .NOSYS => { // EINVAL could be any of the following situations: // * Descriptor is not valid or locked // * an mmap(2)-like operation is not available for in_fd // * count is negative // * out_fd has the O.APPEND flag set // Because of the "mmap(2)-like operation" possibility, we fall back to doing read/write // manually, the same as ENOSYS. break :sf; }, .AGAIN => if (std.event.Loop.instance) |loop| { loop.waitUntilFdWritable(out_fd); continue; } else { return error.WouldBlock; }, .IO => return error.InputOutput, .PIPE => return error.BrokenPipe, .NOMEM => return error.SystemResources, .NXIO => return error.Unseekable, .SPIPE => return error.Unseekable, else => |err| { unexpectedErrno(err) catch {}; break :sf; }, } } if (trailers.len != 0) { total_written += try writev(out_fd, trailers); } return total_written; }, .freebsd => sf: { var hdtr_data: std.c.sf_hdtr = undefined; var hdtr: ?*std.c.sf_hdtr = null; if (headers.len != 0 or trailers.len != 0) { // Here we carefully avoid `@intCast` by returning partial writes when // too many io vectors are provided. const hdr_cnt = math.cast(u31, headers.len) orelse math.maxInt(u31); if (headers.len > hdr_cnt) return writev(out_fd, headers); const trl_cnt = math.cast(u31, trailers.len) orelse math.maxInt(u31); hdtr_data = std.c.sf_hdtr{ .headers = headers.ptr, .hdr_cnt = hdr_cnt, .trailers = trailers.ptr, .trl_cnt = trl_cnt, }; hdtr = &hdtr_data; } const adjusted_count = @min(in_len, max_count); while (true) { var sbytes: off_t = undefined; const offset = @bitCast(off_t, in_offset); const err = errno(system.sendfile(in_fd, out_fd, offset, adjusted_count, hdtr, &sbytes, flags)); const amt = @bitCast(usize, sbytes); switch (err) { .SUCCESS => return amt, .BADF => unreachable, // Always a race condition. .FAULT => unreachable, // Segmentation fault. .NOTCONN => unreachable, // `out_fd` is an unconnected socket. .INVAL, .OPNOTSUPP, .NOTSOCK, .NOSYS => { // EINVAL could be any of the following situations: // * The fd argument is not a regular file. // * The s argument is not a SOCK.STREAM type socket. // * The offset argument is negative. // Because of some of these possibilities, we fall back to doing read/write // manually, the same as ENOSYS. break :sf; }, .INTR => if (amt != 0) return amt else continue, .AGAIN => if (amt != 0) { return amt; } else if (std.event.Loop.instance) |loop| { loop.waitUntilFdWritable(out_fd); continue; } else { return error.WouldBlock; }, .BUSY => if (amt != 0) { return amt; } else if (std.event.Loop.instance) |loop| { loop.waitUntilFdReadable(in_fd); continue; } else { return error.WouldBlock; }, .IO => return error.InputOutput, .NOBUFS => return error.SystemResources, .PIPE => return error.BrokenPipe, else => { unexpectedErrno(err) catch {}; if (amt != 0) { return amt; } else { break :sf; } }, } } }, .macos, .ios, .tvos, .watchos => sf: { var hdtr_data: std.c.sf_hdtr = undefined; var hdtr: ?*std.c.sf_hdtr = null; if (headers.len != 0 or trailers.len != 0) { // Here we carefully avoid `@intCast` by returning partial writes when // too many io vectors are provided. const hdr_cnt = math.cast(u31, headers.len) orelse math.maxInt(u31); if (headers.len > hdr_cnt) return writev(out_fd, headers); const trl_cnt = math.cast(u31, trailers.len) orelse math.maxInt(u31); hdtr_data = std.c.sf_hdtr{ .headers = headers.ptr, .hdr_cnt = hdr_cnt, .trailers = trailers.ptr, .trl_cnt = trl_cnt, }; hdtr = &hdtr_data; } const adjusted_count_temporary = @min(in_len, @as(u63, max_count)); // TODO we should not need this int cast; improve the return type of `@min` const adjusted_count = @intCast(u63, adjusted_count_temporary); while (true) { var sbytes: off_t = adjusted_count; const signed_offset = @bitCast(i64, in_offset); const err = errno(system.sendfile(in_fd, out_fd, signed_offset, &sbytes, hdtr, flags)); const amt = @bitCast(usize, sbytes); switch (err) { .SUCCESS => return amt, .BADF => unreachable, // Always a race condition. .FAULT => unreachable, // Segmentation fault. .INVAL => unreachable, .NOTCONN => unreachable, // `out_fd` is an unconnected socket. .OPNOTSUPP, .NOTSOCK, .NOSYS => break :sf, .INTR => if (amt != 0) return amt else continue, .AGAIN => if (amt != 0) { return amt; } else if (std.event.Loop.instance) |loop| { loop.waitUntilFdWritable(out_fd); continue; } else { return error.WouldBlock; }, .IO => return error.InputOutput, .PIPE => return error.BrokenPipe, else => { unexpectedErrno(err) catch {}; if (amt != 0) { return amt; } else { break :sf; } }, } } }, else => {}, // fall back to read/write } if (headers.len != 0 and !header_done) { const amt = try writev(out_fd, headers); total_written += amt; if (amt < count_iovec_bytes(headers)) return total_written; } rw: { var buf: [8 * 4096]u8 = undefined; // Here we match BSD behavior, making a zero count value send as many bytes as possible. const adjusted_count_tmp = if (in_len == 0) buf.len else @min(buf.len, in_len); // TODO we should not need this cast; improve return type of @min const adjusted_count = @intCast(usize, adjusted_count_tmp); const amt_read = try pread(in_fd, buf[0..adjusted_count], in_offset); if (amt_read == 0) { if (in_len == 0) { // We have detected EOF from `in_fd`. break :rw; } else { return total_written; } } const amt_written = try write(out_fd, buf[0..amt_read]); total_written += amt_written; if (amt_written < in_len or in_len == 0) return total_written; } if (trailers.len != 0) { total_written += try writev(out_fd, trailers); } return total_written; } pub const CopyFileRangeError = error{ FileTooBig, InputOutput, /// `fd_in` is not open for reading; or `fd_out` is not open for writing; /// or the `O.APPEND` flag is set for `fd_out`. FilesOpenedWithWrongFlags, IsDir, OutOfMemory, NoSpaceLeft, Unseekable, PermissionDenied, SwapFile, } || PReadError || PWriteError || UnexpectedError; var has_copy_file_range_syscall = std.atomic.Atomic(bool).init(true); /// Transfer data between file descriptors at specified offsets. /// Returns the number of bytes written, which can less than requested. /// /// The `copy_file_range` call copies `len` bytes from one file descriptor to another. When possible, /// this is done within the operating system kernel, which can provide better performance /// characteristics than transferring data from kernel to user space and back, such as with /// `pread` and `pwrite` calls. /// /// `fd_in` must be a file descriptor opened for reading, and `fd_out` must be a file descriptor /// opened for writing. They may be any kind of file descriptor; however, if `fd_in` is not a regular /// file system file, it may cause this function to fall back to calling `pread` and `pwrite`, in which case /// atomicity guarantees no longer apply. /// /// If `fd_in` and `fd_out` are the same, source and target ranges must not overlap. /// The file descriptor seek positions are ignored and not updated. /// When `off_in` is past the end of the input file, it successfully reads 0 bytes. /// /// `flags` has different meanings per operating system; refer to the respective man pages. /// /// These systems support in-kernel data copying: /// * Linux 4.5 (cross-filesystem 5.3) /// /// Other systems fall back to calling `pread` / `pwrite`. /// /// Maximum offsets on Linux are `math.maxInt(i64)`. pub fn copy_file_range(fd_in: fd_t, off_in: u64, fd_out: fd_t, off_out: u64, len: usize, flags: u32) CopyFileRangeError!usize { const call_cfr = comptime if (builtin.os.tag == .wasi) // WASI-libc doesn't have copy_file_range. false else if (builtin.link_libc) std.c.versionCheck(.{ .major = 2, .minor = 27, .patch = 0 }).ok else builtin.os.isAtLeast(.linux, .{ .major = 4, .minor = 5 }) orelse true; if (call_cfr and has_copy_file_range_syscall.load(.Monotonic)) { var off_in_copy = @bitCast(i64, off_in); var off_out_copy = @bitCast(i64, off_out); const rc = system.copy_file_range(fd_in, &off_in_copy, fd_out, &off_out_copy, len, flags); switch (system.getErrno(rc)) { .SUCCESS => return @intCast(usize, rc), .BADF => return error.FilesOpenedWithWrongFlags, .FBIG => return error.FileTooBig, .IO => return error.InputOutput, .ISDIR => return error.IsDir, .NOMEM => return error.OutOfMemory, .NOSPC => return error.NoSpaceLeft, .OVERFLOW => return error.Unseekable, .PERM => return error.PermissionDenied, .TXTBSY => return error.SwapFile, // these may not be regular files, try fallback .INVAL => {}, // support for cross-filesystem copy added in Linux 5.3, use fallback .XDEV => {}, // syscall added in Linux 4.5, use fallback .NOSYS => { has_copy_file_range_syscall.store(false, .Monotonic); }, else => |err| return unexpectedErrno(err), } } var buf: [8 * 4096]u8 = undefined; const adjusted_count = @min(buf.len, len); const amt_read = try pread(fd_in, buf[0..adjusted_count], off_in); // TODO without @as the line below fails to compile for wasm32-wasi: // error: integer value 0 cannot be coerced to type 'os.PWriteError!usize' if (amt_read == 0) return @as(usize, 0); return pwrite(fd_out, buf[0..amt_read], off_out); } pub const PollError = error{ /// The network subsystem has failed. NetworkSubsystemFailed, /// The kernel had no space to allocate file descriptor tables. SystemResources, } || UnexpectedError; pub fn poll(fds: []pollfd, timeout: i32) PollError!usize { while (true) { const fds_count = math.cast(nfds_t, fds.len) orelse return error.SystemResources; const rc = system.poll(fds.ptr, fds_count, timeout); if (builtin.os.tag == .windows) { if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENOBUFS => return error.SystemResources, // TODO: handle more errors else => |err| return windows.unexpectedWSAError(err), } } else { return @intCast(usize, rc); } } else { switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .FAULT => unreachable, .INTR => continue, .INVAL => unreachable, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } unreachable; } } pub const PPollError = error{ /// The operation was interrupted by a delivery of a signal before it could complete. SignalInterrupt, /// The kernel had no space to allocate file descriptor tables. SystemResources, } || UnexpectedError; pub fn ppoll(fds: []pollfd, timeout: ?*const timespec, mask: ?*const sigset_t) PPollError!usize { var ts: timespec = undefined; var ts_ptr: ?*timespec = null; if (timeout) |timeout_ns| { ts_ptr = &ts; ts = timeout_ns.*; } const fds_count = math.cast(nfds_t, fds.len) orelse return error.SystemResources; const rc = system.ppoll(fds.ptr, fds_count, ts_ptr, mask); switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .FAULT => unreachable, .INTR => return error.SignalInterrupt, .INVAL => unreachable, .NOMEM => return error.SystemResources, else => |err| return unexpectedErrno(err), } } pub const RecvFromError = error{ /// The socket is marked nonblocking and the requested operation would block, and /// there is no global event loop configured. WouldBlock, /// A remote host refused to allow the network connection, typically because it is not /// running the requested service. ConnectionRefused, /// Could not allocate kernel memory. SystemResources, ConnectionResetByPeer, /// The socket has not been bound. SocketNotBound, /// The UDP message was too big for the buffer and part of it has been discarded MessageTooBig, /// The network subsystem has failed. NetworkSubsystemFailed, /// The socket is not connected (connection-oriented sockets only). SocketNotConnected, } || UnexpectedError; pub fn recv(sock: socket_t, buf: []u8, flags: u32) RecvFromError!usize { return recvfrom(sock, buf, flags, null, null); } /// If `sockfd` is opened in non blocking mode, the function will /// return error.WouldBlock when EAGAIN is received. pub fn recvfrom( sockfd: socket_t, buf: []u8, flags: u32, src_addr: ?*sockaddr, addrlen: ?*socklen_t, ) RecvFromError!usize { while (true) { const rc = system.recvfrom(sockfd, buf.ptr, buf.len, flags, src_addr, addrlen); if (builtin.os.tag == .windows) { if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAECONNRESET => return error.ConnectionResetByPeer, .WSAEINVAL => return error.SocketNotBound, .WSAEMSGSIZE => return error.MessageTooBig, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAENOTCONN => return error.SocketNotConnected, .WSAEWOULDBLOCK => return error.WouldBlock, // TODO: handle more errors else => |err| return windows.unexpectedWSAError(err), } } else { return @intCast(usize, rc); } } else { switch (errno(rc)) { .SUCCESS => return @intCast(usize, rc), .BADF => unreachable, // always a race condition .FAULT => unreachable, .INVAL => unreachable, .NOTCONN => unreachable, .NOTSOCK => unreachable, .INTR => continue, .AGAIN => return error.WouldBlock, .NOMEM => return error.SystemResources, .CONNREFUSED => return error.ConnectionRefused, .CONNRESET => return error.ConnectionResetByPeer, else => |err| return unexpectedErrno(err), } } } } pub const DnExpandError = error{InvalidDnsPacket}; pub fn dn_expand( msg: []const u8, comp_dn: []const u8, exp_dn: []u8, ) DnExpandError!usize { // This implementation is ported from musl libc. // A more idiomatic "ziggy" implementation would be welcome. var p = comp_dn.ptr; var len: usize = std.math.maxInt(usize); const end = msg.ptr + msg.len; if (p == end or exp_dn.len == 0) return error.InvalidDnsPacket; var dest = exp_dn.ptr; const dend = dest + @min(exp_dn.len, 254); // detect reference loop using an iteration counter var i: usize = 0; while (i < msg.len) : (i += 2) { // loop invariants: p<end, dest<dend if ((p[0] & 0xc0) != 0) { if (p + 1 == end) return error.InvalidDnsPacket; var j = ((p[0] & @as(usize, 0x3f)) << 8) | p[1]; if (len == std.math.maxInt(usize)) len = @ptrToInt(p) + 2 - @ptrToInt(comp_dn.ptr); if (j >= msg.len) return error.InvalidDnsPacket; p = msg.ptr + j; } else if (p[0] != 0) { if (dest != exp_dn.ptr) { dest[0] = '.'; dest += 1; } var j = p[0]; p += 1; if (j >= @ptrToInt(end) - @ptrToInt(p) or j >= @ptrToInt(dend) - @ptrToInt(dest)) { return error.InvalidDnsPacket; } while (j != 0) { j -= 1; dest[0] = p[0]; dest += 1; p += 1; } } else { dest[0] = 0; if (len == std.math.maxInt(usize)) len = @ptrToInt(p) + 1 - @ptrToInt(comp_dn.ptr); return len; } } return error.InvalidDnsPacket; } pub const SetSockOptError = error{ /// The socket is already connected, and a specified option cannot be set while the socket is connected. AlreadyConnected, /// The option is not supported by the protocol. InvalidProtocolOption, /// The send and receive timeout values are too big to fit into the timeout fields in the socket structure. TimeoutTooBig, /// Insufficient resources are available in the system to complete the call. SystemResources, // Setting the socket option requires more elevated permissions. PermissionDenied, NetworkSubsystemFailed, FileDescriptorNotASocket, SocketNotBound, NoDevice, } || UnexpectedError; /// Set a socket's options. pub fn setsockopt(fd: socket_t, level: u32, optname: u32, opt: []const u8) SetSockOptError!void { if (builtin.os.tag == .windows) { const rc = windows.ws2_32.setsockopt(fd, @intCast(i32, level), @intCast(i32, optname), opt.ptr, @intCast(i32, opt.len)); if (rc == windows.ws2_32.SOCKET_ERROR) { switch (windows.ws2_32.WSAGetLastError()) { .WSANOTINITIALISED => unreachable, .WSAENETDOWN => return error.NetworkSubsystemFailed, .WSAEFAULT => unreachable, .WSAENOTSOCK => return error.FileDescriptorNotASocket, .WSAEINVAL => return error.SocketNotBound, else => |err| return windows.unexpectedWSAError(err), } } return; } else { switch (errno(system.setsockopt(fd, level, optname, opt.ptr, @intCast(socklen_t, opt.len)))) { .SUCCESS => {}, .BADF => unreachable, // always a race condition .NOTSOCK => unreachable, // always a race condition .INVAL => unreachable, .FAULT => unreachable, .DOM => return error.TimeoutTooBig, .ISCONN => return error.AlreadyConnected, .NOPROTOOPT => return error.InvalidProtocolOption, .NOMEM => return error.SystemResources, .NOBUFS => return error.SystemResources, .PERM => return error.PermissionDenied, .NODEV => return error.NoDevice, else => |err| return unexpectedErrno(err), } } } pub const MemFdCreateError = error{ SystemFdQuotaExceeded, ProcessFdQuotaExceeded, OutOfMemory, /// memfd_create is available in Linux 3.17 and later. This error is returned /// for older kernel versions. SystemOutdated, } || UnexpectedError; pub fn memfd_createZ(name: [*:0]const u8, flags: u32) MemFdCreateError!fd_t { switch (builtin.os.tag) { .linux => { // memfd_create is available only in glibc versions starting with 2.27. const use_c = std.c.versionCheck(.{ .major = 2, .minor = 27, .patch = 0 }).ok; const sys = if (use_c) std.c else linux; const getErrno = if (use_c) std.c.getErrno else linux.getErrno; const rc = sys.memfd_create(name, flags); switch (getErrno(rc)) { .SUCCESS => return @intCast(fd_t, rc), .FAULT => unreachable, // name has invalid memory .INVAL => unreachable, // name/flags are faulty .NFILE => return error.SystemFdQuotaExceeded, .MFILE => return error.ProcessFdQuotaExceeded, .NOMEM => return error.OutOfMemory, .NOSYS => return error.SystemOutdated, else => |err| return unexpectedErrno(err), } }, .freebsd => { if (comptime builtin.os.version_range.semver.max.order(.{ .major = 13, .minor = 0 }) == .lt) @compileError("memfd_create is unavailable on FreeBSD < 13.0"); const rc = system.memfd_create(name, flags); switch (errno(rc)) { .SUCCESS => return rc, .BADF => unreachable, // name argument NULL .INVAL => unreachable, // name too long or invalid/unsupported flags. .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NOSYS => return error.SystemOutdated, else => |err| return unexpectedErrno(err), } }, else => @compileError("target OS does not support memfd_create()"), } } pub const MFD_NAME_PREFIX = "memfd:"; pub const MFD_MAX_NAME_LEN = NAME_MAX - MFD_NAME_PREFIX.len; fn toMemFdPath(name: []const u8) ![MFD_MAX_NAME_LEN:0]u8 { var path_with_null: [MFD_MAX_NAME_LEN:0]u8 = undefined; // >= rather than > to make room for the null byte if (name.len >= MFD_MAX_NAME_LEN) return error.NameTooLong; mem.copy(u8, &path_with_null, name); path_with_null[name.len] = 0; return path_with_null; } pub fn memfd_create(name: []const u8, flags: u32) !fd_t { const name_t = try toMemFdPath(name); return memfd_createZ(&name_t, flags); } pub fn getrusage(who: i32) rusage { var result: rusage = undefined; const rc = system.getrusage(who, &result); switch (errno(rc)) { .SUCCESS => return result, .INVAL => unreachable, .FAULT => unreachable, else => unreachable, } } pub const TermiosGetError = error{NotATerminal} || UnexpectedError; pub fn tcgetattr(handle: fd_t) TermiosGetError!termios { while (true) { var term: termios = undefined; switch (errno(system.tcgetattr(handle, &term))) { .SUCCESS => return term, .INTR => continue, .BADF => unreachable, .NOTTY => return error.NotATerminal, else => |err| return unexpectedErrno(err), } } } pub const TermiosSetError = TermiosGetError || error{ProcessOrphaned}; pub fn tcsetattr(handle: fd_t, optional_action: TCSA, termios_p: termios) TermiosSetError!void { while (true) { switch (errno(system.tcsetattr(handle, optional_action, &termios_p))) { .SUCCESS => return, .BADF => unreachable, .INTR => continue, .INVAL => unreachable, .NOTTY => return error.NotATerminal, .IO => return error.ProcessOrphaned, else => |err| return unexpectedErrno(err), } } } pub const IoCtl_SIOCGIFINDEX_Error = error{ FileSystem, InterfaceNotFound, } || UnexpectedError; pub fn ioctl_SIOCGIFINDEX(fd: fd_t, ifr: *ifreq) IoCtl_SIOCGIFINDEX_Error!void { while (true) { switch (errno(system.ioctl(fd, SIOCGIFINDEX, @ptrToInt(ifr)))) { .SUCCESS => return, .INVAL => unreachable, // Bad parameters. .NOTTY => unreachable, .NXIO => unreachable, .BADF => unreachable, // Always a race condition. .FAULT => unreachable, // Bad pointer parameter. .INTR => continue, .IO => return error.FileSystem, .NODEV => return error.InterfaceNotFound, else => |err| return unexpectedErrno(err), } } } pub fn signalfd(fd: fd_t, mask: *const sigset_t, flags: u32) !fd_t { const rc = system.signalfd(fd, mask, flags); switch (errno(rc)) { .SUCCESS => return @intCast(fd_t, rc), .BADF, .INVAL => unreachable, .NFILE => return error.SystemFdQuotaExceeded, .NOMEM => return error.SystemResources, .MFILE => return error.ProcessResources, .NODEV => return error.InodeMountFail, .NOSYS => return error.SystemOutdated, else => |err| return unexpectedErrno(err), } } pub const SyncError = error{ InputOutput, NoSpaceLeft, DiskQuota, AccessDenied, } || UnexpectedError; /// Write all pending file contents and metadata modifications to all filesystems. pub fn sync() void { system.sync(); } /// Write all pending file contents and metadata modifications to the filesystem which contains the specified file. pub fn syncfs(fd: fd_t) SyncError!void { const rc = system.syncfs(fd); switch (errno(rc)) { .SUCCESS => return, .BADF, .INVAL, .ROFS => unreachable, .IO => return error.InputOutput, .NOSPC => return error.NoSpaceLeft, .DQUOT => return error.DiskQuota, else => |err| return unexpectedErrno(err), } } /// Write all pending file contents and metadata modifications for the specified file descriptor to the underlying filesystem. pub fn fsync(fd: fd_t) SyncError!void { if (builtin.os.tag == .windows) { if (windows.kernel32.FlushFileBuffers(fd) != 0) return; switch (windows.kernel32.GetLastError()) { .SUCCESS => return, .INVALID_HANDLE => unreachable, .ACCESS_DENIED => return error.AccessDenied, // a sync was performed but the system couldn't update the access time .UNEXP_NET_ERR => return error.InputOutput, else => return error.InputOutput, } } const rc = system.fsync(fd); switch (errno(rc)) { .SUCCESS => return, .BADF, .INVAL, .ROFS => unreachable, .IO => return error.InputOutput, .NOSPC => return error.NoSpaceLeft, .DQUOT => return error.DiskQuota, else => |err| return unexpectedErrno(err), } } /// Write all pending file contents for the specified file descriptor to the underlying filesystem, but not necessarily the metadata. pub fn fdatasync(fd: fd_t) SyncError!void { if (builtin.os.tag == .windows) { return fsync(fd) catch |err| switch (err) { SyncError.AccessDenied => return, // fdatasync doesn't promise that the access time was synced else => return err, }; } const rc = system.fdatasync(fd); switch (errno(rc)) { .SUCCESS => return, .BADF, .INVAL, .ROFS => unreachable, .IO => return error.InputOutput, .NOSPC => return error.NoSpaceLeft, .DQUOT => return error.DiskQuota, else => |err| return unexpectedErrno(err), } } pub const PrctlError = error{ /// Can only occur with PR_SET_SECCOMP/SECCOMP_MODE_FILTER or /// PR_SET_MM/PR_SET_MM_EXE_FILE AccessDenied, /// Can only occur with PR_SET_MM/PR_SET_MM_EXE_FILE InvalidFileDescriptor, InvalidAddress, /// Can only occur with PR_SET_SPECULATION_CTRL, PR_MPX_ENABLE_MANAGEMENT, /// or PR_MPX_DISABLE_MANAGEMENT UnsupportedFeature, /// Can only occur wih PR_SET_FP_MODE OperationNotSupported, PermissionDenied, } || UnexpectedError; pub fn prctl(option: PR, args: anytype) PrctlError!u31 { if (@typeInfo(@TypeOf(args)) != .Struct) @compileError("Expected tuple or struct argument, found " ++ @typeName(@TypeOf(args))); if (args.len > 4) @compileError("prctl takes a maximum of 4 optional arguments"); var buf: [4]usize = undefined; { comptime var i = 0; inline while (i < args.len) : (i += 1) buf[i] = args[i]; } const rc = system.prctl(@enumToInt(option), buf[0], buf[1], buf[2], buf[3]); switch (errno(rc)) { .SUCCESS => return @intCast(u31, rc), .ACCES => return error.AccessDenied, .BADF => return error.InvalidFileDescriptor, .FAULT => return error.InvalidAddress, .INVAL => unreachable, .NODEV, .NXIO => return error.UnsupportedFeature, .OPNOTSUPP => return error.OperationNotSupported, .PERM, .BUSY => return error.PermissionDenied, .RANGE => unreachable, else => |err| return unexpectedErrno(err), } } pub const GetrlimitError = UnexpectedError; pub fn getrlimit(resource: rlimit_resource) GetrlimitError!rlimit { const getrlimit_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.getrlimit64 else system.getrlimit; var limits: rlimit = undefined; switch (errno(getrlimit_sym(resource, &limits))) { .SUCCESS => return limits, .FAULT => unreachable, // bogus pointer .INVAL => unreachable, else => |err| return unexpectedErrno(err), } } pub const SetrlimitError = error{ PermissionDenied, LimitTooBig } || UnexpectedError; pub fn setrlimit(resource: rlimit_resource, limits: rlimit) SetrlimitError!void { const setrlimit_sym = if (builtin.os.tag == .linux and builtin.link_libc) system.setrlimit64 else system.setrlimit; switch (errno(setrlimit_sym(resource, &limits))) { .SUCCESS => return, .FAULT => unreachable, // bogus pointer .INVAL => return error.LimitTooBig, // this could also mean "invalid resource", but that would be unreachable .PERM => return error.PermissionDenied, else => |err| return unexpectedErrno(err), } } pub const MadviseError = error{ /// advice is MADV.REMOVE, but the specified address range is not a shared writable mapping. AccessDenied, /// advice is MADV.HWPOISON, but the caller does not have the CAP_SYS_ADMIN capability. PermissionDenied, /// A kernel resource was temporarily unavailable. SystemResources, /// One of the following: /// * addr is not page-aligned or length is negative /// * advice is not valid /// * advice is MADV.DONTNEED or MADV.REMOVE and the specified address range /// includes locked, Huge TLB pages, or VM_PFNMAP pages. /// * advice is MADV.MERGEABLE or MADV.UNMERGEABLE, but the kernel was not /// configured with CONFIG_KSM. /// * advice is MADV.FREE or MADV.WIPEONFORK but the specified address range /// includes file, Huge TLB, MAP.SHARED, or VM_PFNMAP ranges. InvalidSyscall, /// (for MADV.WILLNEED) Paging in this area would exceed the process's /// maximum resident set size. WouldExceedMaximumResidentSetSize, /// One of the following: /// * (for MADV.WILLNEED) Not enough memory: paging in failed. /// * Addresses in the specified range are not currently mapped, or /// are outside the address space of the process. OutOfMemory, /// The madvise syscall is not available on this version and configuration /// of the Linux kernel. MadviseUnavailable, /// The operating system returned an undocumented error code. Unexpected, }; /// Give advice about use of memory. /// This syscall is optional and is sometimes configured to be disabled. pub fn madvise(ptr: [*]align(mem.page_size) u8, length: usize, advice: u32) MadviseError!void { switch (errno(system.madvise(ptr, length, advice))) { .SUCCESS => return, .ACCES => return error.AccessDenied, .AGAIN => return error.SystemResources, .BADF => unreachable, // The map exists, but the area maps something that isn't a file. .INVAL => return error.InvalidSyscall, .IO => return error.WouldExceedMaximumResidentSetSize, .NOMEM => return error.OutOfMemory, .NOSYS => return error.MadviseUnavailable, else => |err| return unexpectedErrno(err), } } pub const PerfEventOpenError = error{ /// Returned if the perf_event_attr size value is too small (smaller /// than PERF_ATTR_SIZE_VER0), too big (larger than the page size), /// or larger than the kernel supports and the extra bytes are not /// zero. When E2BIG is returned, the perf_event_attr size field is /// overwritten by the kernel to be the size of the structure it was /// expecting. TooBig, /// Returned when the requested event requires CAP_SYS_ADMIN permis‐ /// sions (or a more permissive perf_event paranoid setting). Some /// common cases where an unprivileged process may encounter this /// error: attaching to a process owned by a different user; moni‐ /// toring all processes on a given CPU (i.e., specifying the pid /// argument as -1); and not setting exclude_kernel when the para‐ /// noid setting requires it. /// Also: /// Returned on many (but not all) architectures when an unsupported /// exclude_hv, exclude_idle, exclude_user, or exclude_kernel set‐ /// ting is specified. /// It can also happen, as with EACCES, when the requested event re‐ /// quires CAP_SYS_ADMIN permissions (or a more permissive /// perf_event paranoid setting). This includes setting a break‐ /// point on a kernel address, and (since Linux 3.13) setting a ker‐ /// nel function-trace tracepoint. PermissionDenied, /// Returned if another event already has exclusive access to the /// PMU. DeviceBusy, /// Each opened event uses one file descriptor. If a large number /// of events are opened, the per-process limit on the number of /// open file descriptors will be reached, and no more events can be /// created. ProcessResources, EventRequiresUnsupportedCpuFeature, /// Returned if you try to add more breakpoint /// events than supported by the hardware. TooManyBreakpoints, /// Returned if PERF_SAMPLE_STACK_USER is set in sample_type and it /// is not supported by hardware. SampleStackNotSupported, /// Returned if an event requiring a specific hardware feature is /// requested but there is no hardware support. This includes re‐ /// questing low-skid events if not supported, branch tracing if it /// is not available, sampling if no PMU interrupt is available, and /// branch stacks for software events. EventNotSupported, /// Returned if PERF_SAMPLE_CALLCHAIN is requested and sam‐ /// ple_max_stack is larger than the maximum specified in /// /proc/sys/kernel/perf_event_max_stack. SampleMaxStackOverflow, /// Returned if attempting to attach to a process that does not exist. ProcessNotFound, } || UnexpectedError; pub fn perf_event_open( attr: *linux.perf_event_attr, pid: pid_t, cpu: i32, group_fd: fd_t, flags: usize, ) PerfEventOpenError!fd_t { const rc = system.perf_event_open(attr, pid, cpu, group_fd, flags); switch (errno(rc)) { .SUCCESS => return @intCast(fd_t, rc), .@"2BIG" => return error.TooBig, .ACCES => return error.PermissionDenied, .BADF => unreachable, // group_fd file descriptor is not valid. .BUSY => return error.DeviceBusy, .FAULT => unreachable, // Segmentation fault. .INVAL => unreachable, // Bad attr settings. .INTR => unreachable, // Mixed perf and ftrace handling for a uprobe. .MFILE => return error.ProcessResources, .NODEV => return error.EventRequiresUnsupportedCpuFeature, .NOENT => unreachable, // Invalid type setting. .NOSPC => return error.TooManyBreakpoints, .NOSYS => return error.SampleStackNotSupported, .OPNOTSUPP => return error.EventNotSupported, .OVERFLOW => return error.SampleMaxStackOverflow, .PERM => return error.PermissionDenied, .SRCH => return error.ProcessNotFound, else => |err| return unexpectedErrno(err), } } pub const TimerFdCreateError = error{ AccessDenied, ProcessFdQuotaExceeded, SystemFdQuotaExceeded, NoDevice, SystemResources, } || UnexpectedError; pub const TimerFdGetError = error{InvalidHandle} || UnexpectedError; pub const TimerFdSetError = TimerFdGetError || error{Canceled}; pub fn timerfd_create(clokid: i32, flags: u32) TimerFdCreateError!fd_t { var rc = linux.timerfd_create(clokid, flags); return switch (errno(rc)) { .SUCCESS => @intCast(fd_t, rc), .INVAL => unreachable, .MFILE => return error.ProcessFdQuotaExceeded, .NFILE => return error.SystemFdQuotaExceeded, .NODEV => return error.NoDevice, .NOMEM => return error.SystemResources, .PERM => return error.AccessDenied, else => |err| return unexpectedErrno(err), }; } pub fn timerfd_settime(fd: i32, flags: u32, new_value: *const linux.itimerspec, old_value: ?*linux.itimerspec) TimerFdSetError!void { var rc = linux.timerfd_settime(fd, flags, new_value, old_value); return switch (errno(rc)) { .SUCCESS => {}, .BADF => error.InvalidHandle, .FAULT => unreachable, .INVAL => unreachable, .CANCELED => error.Canceled, else => |err| return unexpectedErrno(err), }; } pub fn timerfd_gettime(fd: i32) TimerFdGetError!linux.itimerspec { var curr_value: linux.itimerspec = undefined; var rc = linux.timerfd_gettime(fd, &curr_value); return switch (errno(rc)) { .SUCCESS => return curr_value, .BADF => error.InvalidHandle, .FAULT => unreachable, .INVAL => unreachable, else => |err| return unexpectedErrno(err), }; }` |

## os / darwin

| Function | Signature |
|----------|-----------|
| `isValid` | `pub fn isValid(self: MachTask) bool` |
| `getRegionInfo` | `pub fn getRegionInfo( task: MachTask, address: u64, len: usize, tag: RegionInfo.Tag, ) MachError!RegionInfo` |
| `getRegionSubmapInfo` | `pub fn getRegionSubmapInfo( task: MachTask, address: u64, len: usize, nesting_depth: u32, tag: RegionSubmapInfo.Tag, ) MachError!RegionSubmapInfo` |
| `getCurrProtection` | `pub fn getCurrProtection(task: MachTask, address: u64, len: usize) MachError!std.c.vm_prot_t` |
| `setMaxProtection` | `pub fn setMaxProtection(task: MachTask, address: u64, len: usize, prot: std.c.vm_prot_t) MachError!void` |
| `setCurrProtection` | `pub fn setCurrProtection(task: MachTask, address: u64, len: usize, prot: std.c.vm_prot_t) MachError!void` |
| `writeMemProtected` | `pub fn writeMemProtected(task: MachTask, address: u64, buf: []const u8, arch: std.Target.Cpu.Arch) MachError!usize` |
| `writeMem` | `pub fn writeMem(task: MachTask, address: u64, buf: []const u8, arch: std.Target.Cpu.Arch) MachError!usize` |
| `readMem` | `pub fn readMem(task: MachTask, address: u64, buf: []u8) MachError!usize` |
| `machTaskForPid` | `pub fn machTaskForPid(pid: std.os.pid_t) MachError!MachTask` |
| `machTaskForSelf` | `pub fn machTaskForSelf() MachTask` |

## os / linux

| Function | Signature |
|----------|-----------|
| `getauxval` | `pub fn getauxval(index: usize) usize` |
| `getErrno` | `pub fn getErrno(r: usize) E` |
| `dup` | `pub fn dup(old: i32) usize` |
| `dup2` | `pub fn dup2(old: i32, new: i32) usize` |
| `dup3` | `pub fn dup3(old: i32, new: i32, flags: u32) usize` |
| `chdir` | `pub fn chdir(path: [*:0]const u8) usize` |
| `fchdir` | `pub fn fchdir(fd: fd_t) usize` |
| `chroot` | `pub fn chroot(path: [*:0]const u8) usize` |
| `execve` | `pub fn execve(path: [*:0]const u8, argv: [*:null]const ?[*:0]const u8, envp: [*:null]const ?[*:0]const u8) usize` |
| `fork` | `pub fn fork() usize` |
| `vfork` | `pub inline fn vfork() usize` |
| `futimens` | `pub fn futimens(fd: i32, times: *const [2]timespec) usize` |
| `utimensat` | `pub fn utimensat(dirfd: i32, path: ?[*:0]const u8, times: *const [2]timespec, flags: u32) usize` |
| `fallocate` | `pub fn fallocate(fd: i32, mode: i32, offset: i64, length: i64) usize` |
| `futex_wait` | `pub fn futex_wait(uaddr: *const i32, futex_op: u32, val: i32, timeout: ?*const timespec) usize` |
| `futex_wake` | `pub fn futex_wake(uaddr: *const i32, futex_op: u32, val: i32) usize` |
| `getcwd` | `pub fn getcwd(buf: [*]u8, size: usize) usize` |
| `getdents` | `pub fn getdents(fd: i32, dirp: [*]u8, len: usize) usize` |
| `getdents64` | `pub fn getdents64(fd: i32, dirp: [*]u8, len: usize) usize` |
| `inotify_init1` | `pub fn inotify_init1(flags: u32) usize` |
| `inotify_add_watch` | `pub fn inotify_add_watch(fd: i32, pathname: [*:0]const u8, mask: u32) usize` |
| `inotify_rm_watch` | `pub fn inotify_rm_watch(fd: i32, wd: i32) usize` |
| `readlink` | `pub fn readlink(noalias path: [*:0]const u8, noalias buf_ptr: [*]u8, buf_len: usize) usize` |
| `readlinkat` | `pub fn readlinkat(dirfd: i32, noalias path: [*:0]const u8, noalias buf_ptr: [*]u8, buf_len: usize) usize` |
| `mkdir` | `pub fn mkdir(path: [*:0]const u8, mode: u32) usize` |
| `mkdirat` | `pub fn mkdirat(dirfd: i32, path: [*:0]const u8, mode: u32) usize` |
| `mknod` | `pub fn mknod(path: [*:0]const u8, mode: u32, dev: u32) usize` |
| `mknodat` | `pub fn mknodat(dirfd: i32, path: [*:0]const u8, mode: u32, dev: u32) usize` |
| `mount` | `pub fn mount(special: [*:0]const u8, dir: [*:0]const u8, fstype: ?[*:0]const u8, flags: u32, data: usize) usize` |
| `umount` | `pub fn umount(special: [*:0]const u8) usize` |
| `umount2` | `pub fn umount2(special: [*:0]const u8, flags: u32) usize` |
| `mmap` | `pub fn mmap(address: ?[*]u8, length: usize, prot: usize, flags: u32, fd: i32, offset: i64) usize` |
| `mprotect` | `pub fn mprotect(address: [*]const u8, length: usize, protection: usize) usize` |
| `msync` | `pub fn msync(address: [*]const u8, length: usize, flags: i32) usize` |
| `munmap` | `pub fn munmap(address: [*]const u8, length: usize) usize` |
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
| `pipe` | `pub fn pipe(fd: *[2]i32) usize` |
| `pipe2` | `pub fn pipe2(fd: *[2]i32, flags: u32) usize` |
| `write` | `pub fn write(fd: i32, buf: [*]const u8, count: usize) usize` |
| `ftruncate` | `pub fn ftruncate(fd: i32, length: i64) usize` |
| `pwrite` | `pub fn pwrite(fd: i32, buf: [*]const u8, count: usize, offset: i64) usize` |
| `rename` | `pub fn rename(old: [*:0]const u8, new: [*:0]const u8) usize` |
| `renameat` | `pub fn renameat(oldfd: i32, oldpath: [*]const u8, newfd: i32, newpath: [*]const u8) usize` |
| `renameat2` | `pub fn renameat2(oldfd: i32, oldpath: [*:0]const u8, newfd: i32, newpath: [*:0]const u8, flags: u32) usize` |
| `open` | `pub fn open(path: [*:0]const u8, flags: u32, perm: mode_t) usize` |
| `create` | `pub fn create(path: [*:0]const u8, perm: mode_t) usize` |
| `openat` | `pub fn openat(dirfd: i32, path: [*:0]const u8, flags: u32, mode: mode_t) usize` |
| `clone5` | `pub fn clone5(flags: usize, child_stack_ptr: usize, parent_tid: *i32, child_tid: *i32, newtls: usize) usize` |
| `clone2` | `pub fn clone2(flags: u32, child_stack_ptr: usize) usize` |
| `close` | `pub fn close(fd: i32) usize` |
| `fchmod` | `pub fn fchmod(fd: i32, mode: mode_t) usize` |
| `fchown` | `pub fn fchown(fd: i32, owner: uid_t, group: gid_t) usize` |
| `llseek` | `pub fn llseek(fd: i32, offset: u64, result: ?*u64, whence: usize) usize` |
| `lseek` | `pub fn lseek(fd: i32, offset: i64, whence: usize) usize` |
| `exit` | `pub fn exit(status: i32) noreturn` |
| `exit_group` | `pub fn exit_group(status: i32) noreturn` |
| `reboot` | `pub fn reboot(magic: LINUX_REBOOT.MAGIC1, magic2: LINUX_REBOOT.MAGIC2, cmd: LINUX_REBOOT.CMD, arg: ?*const anyopaque) usize` |
| `getrandom` | `pub fn getrandom(buf: [*]u8, count: usize, flags: u32) usize` |
| `kill` | `pub fn kill(pid: pid_t, sig: i32) usize` |
| `tkill` | `pub fn tkill(tid: pid_t, sig: i32) usize` |
| `tgkill` | `pub fn tgkill(tgid: pid_t, tid: pid_t, sig: i32) usize` |
| `link` | `pub fn link(oldpath: [*:0]const u8, newpath: [*:0]const u8, flags: i32) usize` |
| `linkat` | `pub fn linkat(oldfd: fd_t, oldpath: [*:0]const u8, newfd: fd_t, newpath: [*:0]const u8, flags: i32) usize` |
| `unlink` | `pub fn unlink(path: [*:0]const u8) usize` |
| `unlinkat` | `pub fn unlinkat(dirfd: i32, path: [*:0]const u8, flags: u32) usize` |
| `waitpid` | `pub fn waitpid(pid: pid_t, status: *u32, flags: u32) usize` |
| `waitid` | `pub fn waitid(id_type: P, id: i32, infop: *siginfo_t, flags: u32) usize` |
| `fcntl` | `pub fn fcntl(fd: fd_t, cmd: i32, arg: usize) usize` |
| `flock` | `pub fn flock(fd: fd_t, operation: i32) usize` |
| `clock_gettime` | `pub fn clock_gettime(clk_id: i32, tp: *timespec) usize` |
| `clock_getres` | `pub fn clock_getres(clk_id: i32, tp: *timespec) usize` |
| `clock_settime` | `pub fn clock_settime(clk_id: i32, tp: *const timespec) usize` |
| `gettimeofday` | `pub fn gettimeofday(tv: *timeval, tz: *timezone) usize` |
| `settimeofday` | `pub fn settimeofday(tv: *const timeval, tz: *const timezone) usize` |
| `nanosleep` | `pub fn nanosleep(req: *const timespec, rem: ?*timespec) usize` |
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
| `getgroups` | `pub fn getgroups(size: usize, list: *gid_t) usize` |
| `setgroups` | `pub fn setgroups(size: usize, list: [*]const gid_t) usize` |
| `getpid` | `pub fn getpid() pid_t` |
| `gettid` | `pub fn gettid() pid_t` |
| `sigprocmask` | `pub fn sigprocmask(flags: u32, noalias set: ?*const sigset_t, noalias oldset: ?*sigset_t) usize` |
| `sigaction` | `pub fn sigaction(sig: u6, noalias act: ?*const Sigaction, noalias oact: ?*Sigaction) usize` |
| `sigaddset` | `pub fn sigaddset(set: *sigset_t, sig: u6) void` |
| `sigismember` | `pub fn sigismember(set: *const sigset_t, sig: u6) bool` |
| `getsockname` | `pub fn getsockname(fd: i32, noalias addr: *sockaddr, noalias len: *socklen_t) usize` |
| `getpeername` | `pub fn getpeername(fd: i32, noalias addr: *sockaddr, noalias len: *socklen_t) usize` |
| `socket` | `pub fn socket(domain: u32, socket_type: u32, protocol: u32) usize` |
| `setsockopt` | `pub fn setsockopt(fd: i32, level: u32, optname: u32, optval: [*]const u8, optlen: socklen_t) usize` |
| `getsockopt` | `pub fn getsockopt(fd: i32, level: u32, optname: u32, noalias optval: [*]u8, noalias optlen: *socklen_t) usize` |
| `sendmsg` | `pub fn sendmsg(fd: i32, msg: *const std.x.os.Socket.Message, flags: c_int) usize` |
| `sendmmsg` | `pub fn sendmmsg(fd: i32, msgvec: [*]mmsghdr_const, vlen: u32, flags: u32) usize` |
| `connect` | `pub fn connect(fd: i32, addr: *const anyopaque, len: socklen_t) usize` |
| `recvmsg` | `pub fn recvmsg(fd: i32, msg: *std.x.os.Socket.Message, flags: c_int) usize` |
| `recvfrom` | `pub fn recvfrom(fd: i32, noalias buf: [*]u8, len: usize, flags: u32, noalias addr: ?*sockaddr, noalias alen: ?*socklen_t) usize` |
| `shutdown` | `pub fn shutdown(fd: i32, how: i32) usize` |
| `bind` | `pub fn bind(fd: i32, addr: *const sockaddr, len: socklen_t) usize` |
| `listen` | `pub fn listen(fd: i32, backlog: u32) usize` |
| `sendto` | `pub fn sendto(fd: i32, buf: [*]const u8, len: usize, flags: u32, addr: ?*const sockaddr, alen: socklen_t) usize` |
| `sendfile` | `pub fn sendfile(outfd: i32, infd: i32, offset: ?*i64, count: usize) usize` |
| `socketpair` | `pub fn socketpair(domain: i32, socket_type: i32, protocol: i32, fd: *[2]i32) usize` |
| `accept` | `pub fn accept(fd: i32, noalias addr: ?*sockaddr, noalias len: ?*socklen_t) usize` |
| `accept4` | `pub fn accept4(fd: i32, noalias addr: ?*sockaddr, noalias len: ?*socklen_t, flags: u32) usize` |
| `fstat` | `pub fn fstat(fd: i32, stat_buf: *Stat) usize` |
| `stat` | `pub fn stat(pathname: [*:0]const u8, statbuf: *Stat) usize` |
| `lstat` | `pub fn lstat(pathname: [*:0]const u8, statbuf: *Stat) usize` |
| `fstatat` | `pub fn fstatat(dirfd: i32, path: [*:0]const u8, stat_buf: *Stat, flags: u32) usize` |
| `statx` | `pub fn statx(dirfd: i32, path: [*]const u8, flags: u32, mask: u32, statx_buf: *Statx) usize` |
| `listxattr` | `pub fn listxattr(path: [*:0]const u8, list: [*]u8, size: usize) usize` |
| `llistxattr` | `pub fn llistxattr(path: [*:0]const u8, list: [*]u8, size: usize) usize` |
| `flistxattr` | `pub fn flistxattr(fd: usize, list: [*]u8, size: usize) usize` |
| `getxattr` | `pub fn getxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `lgetxattr` | `pub fn lgetxattr(path: [*:0]const u8, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `fgetxattr` | `pub fn fgetxattr(fd: usize, name: [*:0]const u8, value: [*]u8, size: usize) usize` |
| `setxattr` | `pub fn setxattr(path: [*:0]const u8, name: [*:0]const u8, value: *const void, size: usize, flags: usize) usize` |
| `lsetxattr` | `pub fn lsetxattr(path: [*:0]const u8, name: [*:0]const u8, value: *const void, size: usize, flags: usize) usize` |
| `fsetxattr` | `pub fn fsetxattr(fd: usize, name: [*:0]const u8, value: *const void, size: usize, flags: usize) usize` |
| `removexattr` | `pub fn removexattr(path: [*:0]const u8, name: [*:0]const u8) usize` |
| `lremovexattr` | `pub fn lremovexattr(path: [*:0]const u8, name: [*:0]const u8) usize` |
| `fremovexattr` | `pub fn fremovexattr(fd: usize, name: [*:0]const u8) usize` |
| `sched_yield` | `pub fn sched_yield() usize` |
| `sched_getaffinity` | `pub fn sched_getaffinity(pid: pid_t, size: usize, set: *cpu_set_t) usize` |
| `epoll_create` | `pub fn epoll_create() usize` |
| `epoll_create1` | `pub fn epoll_create1(flags: usize) usize` |
| `epoll_ctl` | `pub fn epoll_ctl(epoll_fd: i32, op: u32, fd: i32, ev: ?*epoll_event) usize` |
| `epoll_wait` | `pub fn epoll_wait(epoll_fd: i32, events: [*]epoll_event, maxevents: u32, timeout: i32) usize` |
| `epoll_pwait` | `pub fn epoll_pwait(epoll_fd: i32, events: [*]epoll_event, maxevents: u32, timeout: i32, sigmask: ?*const sigset_t) usize` |
| `eventfd` | `pub fn eventfd(count: u32, flags: u32) usize` |
| `timerfd_create` | `pub fn timerfd_create(clockid: i32, flags: u32) usize` |
| `timerfd_gettime` | `pub fn timerfd_gettime(fd: i32, curr_value: *itimerspec) usize` |
| `timerfd_settime` | `pub fn timerfd_settime(fd: i32, flags: u32, new_value: *const itimerspec, old_value: ?*itimerspec) usize` |
| `getitimer` | `pub fn getitimer(which: i32, curr_value: *itimerspec) usize` |
| `setitimer` | `pub fn setitimer(which: i32, new_value: *const itimerspec, old_value: ?*itimerspec) usize` |
| `unshare` | `pub fn unshare(flags: usize) usize` |
| `capget` | `pub fn capget(hdrp: *cap_user_header_t, datap: *cap_user_data_t) usize` |
| `capset` | `pub fn capset(hdrp: *cap_user_header_t, datap: *const cap_user_data_t) usize` |
| `sigaltstack` | `pub fn sigaltstack(ss: ?*stack_t, old_ss: ?*stack_t) usize` |
| `uname` | `pub fn uname(uts: *utsname) usize` |
| `io_uring_setup` | `pub fn io_uring_setup(entries: u32, p: *io_uring_params) usize` |
| `io_uring_enter` | `pub fn io_uring_enter(fd: i32, to_submit: u32, min_complete: u32, flags: u32, sig: ?*sigset_t) usize` |
| `io_uring_register` | `pub fn io_uring_register(fd: i32, opcode: IORING_REGISTER, arg: ?*const anyopaque, nr_args: u32) usize` |
| `memfd_create` | `pub fn memfd_create(name: [*:0]const u8, flags: u32) usize` |
| `getrusage` | `pub fn getrusage(who: i32, usage: *rusage) usize` |
| `tcgetattr` | `pub fn tcgetattr(fd: fd_t, termios_p: *termios) usize` |
| `tcsetattr` | `pub fn tcsetattr(fd: fd_t, optional_action: TCSA, termios_p: *const termios) usize` |
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
| `madvise` | `pub fn madvise(address: [*]u8, len: usize, advice: u32) usize` |
| `pidfd_open` | `pub fn pidfd_open(pid: pid_t, flags: u32) usize` |
| `pidfd_getfd` | `pub fn pidfd_getfd(pidfd: fd_t, targetfd: fd_t, flags: u32) usize` |
| `pidfd_send_signal` | `pub fn pidfd_send_signal(pidfd: fd_t, sig: i32, info: ?*siginfo_t, flags: u32) usize` |
| `process_vm_readv` | `pub fn process_vm_readv(pid: pid_t, local: [*]const iovec, local_count: usize, remote: [*]const iovec, remote_count: usize, flags: usize) usize` |
| `process_vm_writev` | `pub fn process_vm_writev(pid: pid_t, local: [*]const iovec, local_count: usize, remote: [*]const iovec, remote_count: usize, flags: usize) usize` |
| `fadvise` | `pub fn fadvise(fd: fd_t, offset: i64, len: i64, advice: usize) usize` |
| `perf_event_open` | `pub fn perf_event_open( attr: *perf_event_attr, pid: pid_t, cpu: i32, group_fd: fd_t, flags: usize, ) usize` |
| `seccomp` | `pub fn seccomp(operation: u32, flags: u32, args: ?*const anyopaque) usize` |
| `EXITSTATUS` | `pub fn EXITSTATUS(s: u32) u8` |
| `TERMSIG` | `pub fn TERMSIG(s: u32) u32` |
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
| `valid` | `pub fn valid(x: u8) bool` |
| `TO_MASK` | `pub fn TO_MASK(cap: u8) u32` |
| `TO_INDEX` | `pub fn TO_INDEX(cap: u8) u8` |
| `reclen` | `pub fn reclen(self: dirent64) u16` |
| `CPU_COUNT` | `pub fn CPU_COUNT(set: cpu_set_t) cpu_count_t` |
| `err` | `pub fn err(self: io_uring_cqe) E` |

## os / linux / arm-eabi

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: u32, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore` | `pub fn restore() callconv(.Naked) void` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / arm64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: u32, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

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
| `st` | `pub fn st(comptime size: Size, dst: Reg, off: i16, imm: i32) Insn` |
| `stx` | `pub fn stx(size: Size, dst: Reg, off: i16, src: Reg) Insn` |
| `le` | `pub fn le(comptime size: Size, dst: Reg) Insn` |
| `be` | `pub fn be(comptime size: Size, dst: Reg) Insn` |
| `call` | `pub fn call(helper: Helper) Insn` |
| `exit` | `pub fn exit() Insn` |
| `map_create` | `pub fn map_create(map_type: MapType, key_size: u32, value_size: u32, max_entries: u32) !fd_t` |
| `map_lookup_elem` | `pub fn map_lookup_elem(fd: fd_t, key: []const u8, value: []u8) !void` |
| `map_update_elem` | `pub fn map_update_elem(fd: fd_t, key: []const u8, value: []const u8, flags: u64) !void` |
| `map_delete_elem` | `pub fn map_delete_elem(fd: fd_t, key: []const u8) !void` |
| `prog_load` | `pub fn prog_load( prog_type: ProgType, insns: []const Insn, log: ?*Log, license: []const u8, kern_version: u32, ) !fd_t` |

## os / linux / i386

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `socketcall` | `pub fn socketcall(call: usize, args: [*]usize) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: u32, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore` | `pub fn restore() callconv(.Naked) void` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / io_uring

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(entries: u13, flags: u32) !IO_Uring` |
| `init_params` | `pub fn init_params(entries: u13, p: *linux.io_uring_params) !IO_Uring` |
| `deinit` | `pub fn deinit(self: *IO_Uring) void` |
| `get_sqe` | `pub fn get_sqe(self: *IO_Uring) !*linux.io_uring_sqe` |
| `submit` | `pub fn submit(self: *IO_Uring) !u32` |
| `submit_and_wait` | `pub fn submit_and_wait(self: *IO_Uring, wait_nr: u32) !u32` |
| `enter` | `pub fn enter(self: *IO_Uring, to_submit: u32, min_complete: u32, flags: u32) !u32` |
| `flush_sq` | `pub fn flush_sq(self: *IO_Uring) u32` |
| `sq_ring_needs_enter` | `pub fn sq_ring_needs_enter(self: *IO_Uring, flags: *u32) bool` |
| `sq_ready` | `pub fn sq_ready(self: *IO_Uring) u32` |
| `cq_ready` | `pub fn cq_ready(self: *IO_Uring) u32` |
| `copy_cqes` | `pub fn copy_cqes(self: *IO_Uring, cqes: []linux.io_uring_cqe, wait_nr: u32) !u32` |
| `copy_cqe` | `pub fn copy_cqe(ring: *IO_Uring) !linux.io_uring_cqe` |
| `cq_ring_needs_flush` | `pub fn cq_ring_needs_flush(self: *IO_Uring) bool` |
| `cqe_seen` | `pub fn cqe_seen(self: *IO_Uring, cqe: *linux.io_uring_cqe) void` |
| `cq_advance` | `pub fn cq_advance(self: *IO_Uring, count: u32) void` |
| `fsync` | `pub fn fsync(self: *IO_Uring, user_data: u64, fd: os.fd_t, flags: u32) !*linux.io_uring_sqe` |
| `nop` | `pub fn nop(self: *IO_Uring, user_data: u64) !*linux.io_uring_sqe` |
| `read` | `pub fn read( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: ReadBuffer, offset: u64, ) !*linux.io_uring_sqe` |
| `write` | `pub fn write( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: []const u8, offset: u64, ) !*linux.io_uring_sqe` |
| `read_fixed` | `pub fn read_fixed( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: *os.iovec, offset: u64, buffer_index: u16, ) !*linux.io_uring_sqe` |
| `writev` | `pub fn writev( self: *IO_Uring, user_data: u64, fd: os.fd_t, iovecs: []const os.iovec_const, offset: u64, ) !*linux.io_uring_sqe` |
| `write_fixed` | `pub fn write_fixed( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: *os.iovec, offset: u64, buffer_index: u16, ) !*linux.io_uring_sqe` |
| `accept` | `pub fn accept( self: *IO_Uring, user_data: u64, fd: os.fd_t, addr: ?*os.sockaddr, addrlen: ?*os.socklen_t, flags: u32, ) !*linux.io_uring_sqe` |
| `connect` | `pub fn connect( self: *IO_Uring, user_data: u64, fd: os.fd_t, addr: *const os.sockaddr, addrlen: os.socklen_t, ) !*linux.io_uring_sqe` |
| `epoll_ctl` | `pub fn epoll_ctl( self: *IO_Uring, user_data: u64, epfd: os.fd_t, fd: os.fd_t, op: u32, ev: ?*linux.epoll_event, ) !*linux.io_uring_sqe` |
| `recv` | `pub fn recv( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: RecvBuffer, flags: u32, ) !*linux.io_uring_sqe` |
| `send` | `pub fn send( self: *IO_Uring, user_data: u64, fd: os.fd_t, buffer: []const u8, flags: u32, ) !*linux.io_uring_sqe` |
| `recvmsg` | `pub fn recvmsg( self: *IO_Uring, user_data: u64, fd: os.fd_t, msg: *os.msghdr, flags: u32, ) !*linux.io_uring_sqe` |
| `sendmsg` | `pub fn sendmsg( self: *IO_Uring, user_data: u64, fd: os.fd_t, msg: *const os.msghdr_const, flags: u32, ) !*linux.io_uring_sqe` |
| `openat` | `pub fn openat( self: *IO_Uring, user_data: u64, fd: os.fd_t, path: [*:0]const u8, flags: u32, mode: os.mode_t, ) !*linux.io_uring_sqe` |
| `close` | `pub fn close(self: *IO_Uring, user_data: u64, fd: os.fd_t) !*linux.io_uring_sqe` |
| `timeout` | `pub fn timeout( self: *IO_Uring, user_data: u64, ts: *const os.linux.kernel_timespec, count: u32, flags: u32, ) !*linux.io_uring_sqe` |
| `timeout_remove` | `pub fn timeout_remove( self: *IO_Uring, user_data: u64, timeout_user_data: u64, flags: u32, ) !*linux.io_uring_sqe` |
| `link_timeout` | `pub fn link_timeout( self: *IO_Uring, user_data: u64, ts: *const os.linux.kernel_timespec, flags: u32, ) !*linux.io_uring_sqe` |
| `poll_add` | `pub fn poll_add( self: *IO_Uring, user_data: u64, fd: os.fd_t, poll_mask: u32, ) !*linux.io_uring_sqe` |
| `poll_remove` | `pub fn poll_remove( self: *IO_Uring, user_data: u64, target_user_data: u64, ) !*linux.io_uring_sqe` |
| `poll_update` | `pub fn poll_update( self: *IO_Uring, user_data: u64, old_user_data: u64, new_user_data: u64, poll_mask: u32, flags: u32, ) !*linux.io_uring_sqe` |
| `fallocate` | `pub fn fallocate( self: *IO_Uring, user_data: u64, fd: os.fd_t, mode: i32, offset: u64, len: u64, ) !*linux.io_uring_sqe` |
| `statx` | `pub fn statx( self: *IO_Uring, user_data: u64, fd: os.fd_t, path: [:0]const u8, flags: u32, mask: u32, buf: *linux.Statx, ) !*linux.io_uring_sqe` |
| `cancel` | `pub fn cancel( self: *IO_Uring, user_data: u64, cancel_user_data: u64, flags: u32, ) !*linux.io_uring_sqe` |
| `shutdown` | `pub fn shutdown( self: *IO_Uring, user_data: u64, sockfd: os.socket_t, how: u32, ) !*linux.io_uring_sqe` |
| `renameat` | `pub fn renameat( self: *IO_Uring, user_data: u64, old_dir_fd: os.fd_t, old_path: [*:0]const u8, new_dir_fd: os.fd_t, new_path: [*:0]const u8, flags: u32, ) !*linux.io_uring_sqe` |
| `unlinkat` | `pub fn unlinkat( self: *IO_Uring, user_data: u64, dir_fd: os.fd_t, path: [*:0]const u8, flags: u32, ) !*linux.io_uring_sqe` |
| `mkdirat` | `pub fn mkdirat( self: *IO_Uring, user_data: u64, dir_fd: os.fd_t, path: [*:0]const u8, mode: os.mode_t, ) !*linux.io_uring_sqe` |
| `symlinkat` | `pub fn symlinkat( self: *IO_Uring, user_data: u64, target: [*:0]const u8, new_dir_fd: os.fd_t, link_path: [*:0]const u8, ) !*linux.io_uring_sqe` |
| `linkat` | `pub fn linkat( self: *IO_Uring, user_data: u64, old_dir_fd: os.fd_t, old_path: [*:0]const u8, new_dir_fd: os.fd_t, new_path: [*:0]const u8, flags: u32, ) !*linux.io_uring_sqe` |
| `provide_buffers` | `pub fn provide_buffers( self: *IO_Uring, user_data: u64, buffers: [*]u8, buffers_count: usize, buffer_size: usize, group_id: usize, buffer_id: usize, ) !*linux.io_uring_sqe` |
| `remove_buffers` | `pub fn remove_buffers( self: *IO_Uring, user_data: u64, buffers_count: usize, group_id: usize, ) !*linux.io_uring_sqe` |
| `register_files` | `pub fn register_files(self: *IO_Uring, fds: []const os.fd_t) !void` |
| `register_files_update` | `pub fn register_files_update(self: *IO_Uring, offset: u32, fds: []const os.fd_t) !void` |
| `register_eventfd` | `pub fn register_eventfd(self: *IO_Uring, fd: os.fd_t) !void` |
| `register_eventfd_async` | `pub fn register_eventfd_async(self: *IO_Uring, fd: os.fd_t) !void` |
| `unregister_eventfd` | `pub fn unregister_eventfd(self: *IO_Uring) !void` |
| `register_buffers` | `pub fn register_buffers(self: *IO_Uring, buffers: []const os.iovec) !void` |
| `unregister_buffers` | `pub fn unregister_buffers(self: *IO_Uring) !void` |
| `unregister_files` | `pub fn unregister_files(self: *IO_Uring) !void` |
| `init` | `pub fn init(fd: os.fd_t, p: linux.io_uring_params) !SubmissionQueue` |
| `deinit` | `pub fn deinit(self: *SubmissionQueue) void` |
| `init` | `pub fn init(fd: os.fd_t, p: linux.io_uring_params, sq: SubmissionQueue) !CompletionQueue` |
| `deinit` | `pub fn deinit(self: *CompletionQueue) void` |
| `io_uring_prep_nop` | `pub fn io_uring_prep_nop(sqe: *linux.io_uring_sqe) void` |
| `io_uring_prep_fsync` | `pub fn io_uring_prep_fsync(sqe: *linux.io_uring_sqe, fd: os.fd_t, flags: u32) void` |
| `io_uring_prep_rw` | `pub fn io_uring_prep_rw( op: linux.IORING_OP, sqe: *linux.io_uring_sqe, fd: os.fd_t, addr: u64, len: usize, offset: u64, ) void` |
| `io_uring_prep_read` | `pub fn io_uring_prep_read(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: []u8, offset: u64) void` |
| `io_uring_prep_write` | `pub fn io_uring_prep_write(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: []const u8, offset: u64) void` |
| `io_uring_prep_readv` | `pub fn io_uring_prep_readv( sqe: *linux.io_uring_sqe, fd: os.fd_t, iovecs: []const os.iovec, offset: u64, ) void` |
| `io_uring_prep_writev` | `pub fn io_uring_prep_writev( sqe: *linux.io_uring_sqe, fd: os.fd_t, iovecs: []const os.iovec_const, offset: u64, ) void` |
| `io_uring_prep_read_fixed` | `pub fn io_uring_prep_read_fixed(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: *os.iovec, offset: u64, buffer_index: u16) void` |
| `io_uring_prep_write_fixed` | `pub fn io_uring_prep_write_fixed(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: *os.iovec, offset: u64, buffer_index: u16) void` |
| `__io_uring_prep_poll_mask` | `pub inline fn __io_uring_prep_poll_mask(poll_mask: u32) u32` |
| `io_uring_prep_accept` | `pub fn io_uring_prep_accept( sqe: *linux.io_uring_sqe, fd: os.fd_t, addr: ?*os.sockaddr, addrlen: ?*os.socklen_t, flags: u32, ) void` |
| `io_uring_prep_connect` | `pub fn io_uring_prep_connect( sqe: *linux.io_uring_sqe, fd: os.fd_t, addr: *const os.sockaddr, addrlen: os.socklen_t, ) void` |
| `io_uring_prep_epoll_ctl` | `pub fn io_uring_prep_epoll_ctl( sqe: *linux.io_uring_sqe, epfd: os.fd_t, fd: os.fd_t, op: u32, ev: ?*linux.epoll_event, ) void` |
| `io_uring_prep_recv` | `pub fn io_uring_prep_recv(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: []u8, flags: u32) void` |
| `io_uring_prep_send` | `pub fn io_uring_prep_send(sqe: *linux.io_uring_sqe, fd: os.fd_t, buffer: []const u8, flags: u32) void` |
| `io_uring_prep_recvmsg` | `pub fn io_uring_prep_recvmsg( sqe: *linux.io_uring_sqe, fd: os.fd_t, msg: *os.msghdr, flags: u32, ) void` |
| `io_uring_prep_sendmsg` | `pub fn io_uring_prep_sendmsg( sqe: *linux.io_uring_sqe, fd: os.fd_t, msg: *const os.msghdr_const, flags: u32, ) void` |
| `io_uring_prep_openat` | `pub fn io_uring_prep_openat( sqe: *linux.io_uring_sqe, fd: os.fd_t, path: [*:0]const u8, flags: u32, mode: os.mode_t, ) void` |
| `io_uring_prep_close` | `pub fn io_uring_prep_close(sqe: *linux.io_uring_sqe, fd: os.fd_t) void` |
| `io_uring_prep_timeout` | `pub fn io_uring_prep_timeout( sqe: *linux.io_uring_sqe, ts: *const os.linux.kernel_timespec, count: u32, flags: u32, ) void` |
| `io_uring_prep_timeout_remove` | `pub fn io_uring_prep_timeout_remove(sqe: *linux.io_uring_sqe, timeout_user_data: u64, flags: u32) void` |
| `io_uring_prep_link_timeout` | `pub fn io_uring_prep_link_timeout( sqe: *linux.io_uring_sqe, ts: *const os.linux.kernel_timespec, flags: u32, ) void` |
| `io_uring_prep_poll_add` | `pub fn io_uring_prep_poll_add( sqe: *linux.io_uring_sqe, fd: os.fd_t, poll_mask: u32, ) void` |
| `io_uring_prep_poll_remove` | `pub fn io_uring_prep_poll_remove( sqe: *linux.io_uring_sqe, target_user_data: u64, ) void` |
| `io_uring_prep_poll_update` | `pub fn io_uring_prep_poll_update( sqe: *linux.io_uring_sqe, old_user_data: u64, new_user_data: u64, poll_mask: u32, flags: u32, ) void` |
| `io_uring_prep_fallocate` | `pub fn io_uring_prep_fallocate( sqe: *linux.io_uring_sqe, fd: os.fd_t, mode: i32, offset: u64, len: u64, ) void` |
| `io_uring_prep_statx` | `pub fn io_uring_prep_statx( sqe: *linux.io_uring_sqe, fd: os.fd_t, path: [*:0]const u8, flags: u32, mask: u32, buf: *linux.Statx, ) void` |
| `io_uring_prep_cancel` | `pub fn io_uring_prep_cancel( sqe: *linux.io_uring_sqe, cancel_user_data: u64, flags: u32, ) void` |
| `io_uring_prep_shutdown` | `pub fn io_uring_prep_shutdown( sqe: *linux.io_uring_sqe, sockfd: os.socket_t, how: u32, ) void` |
| `io_uring_prep_renameat` | `pub fn io_uring_prep_renameat( sqe: *linux.io_uring_sqe, old_dir_fd: os.fd_t, old_path: [*:0]const u8, new_dir_fd: os.fd_t, new_path: [*:0]const u8, flags: u32, ) void` |
| `io_uring_prep_unlinkat` | `pub fn io_uring_prep_unlinkat( sqe: *linux.io_uring_sqe, dir_fd: os.fd_t, path: [*:0]const u8, flags: u32, ) void` |
| `io_uring_prep_mkdirat` | `pub fn io_uring_prep_mkdirat( sqe: *linux.io_uring_sqe, dir_fd: os.fd_t, path: [*:0]const u8, mode: os.mode_t, ) void` |
| `io_uring_prep_symlinkat` | `pub fn io_uring_prep_symlinkat( sqe: *linux.io_uring_sqe, target: [*:0]const u8, new_dir_fd: os.fd_t, link_path: [*:0]const u8, ) void` |
| `io_uring_prep_linkat` | `pub fn io_uring_prep_linkat( sqe: *linux.io_uring_sqe, old_dir_fd: os.fd_t, old_path: [*:0]const u8, new_dir_fd: os.fd_t, new_path: [*:0]const u8, flags: u32, ) void` |
| `io_uring_prep_provide_buffers` | `pub fn io_uring_prep_provide_buffers( sqe: *linux.io_uring_sqe, buffers: [*]u8, num: usize, buffer_len: usize, group_id: usize, buffer_id: usize, ) void` |
| `io_uring_prep_remove_buffers` | `pub fn io_uring_prep_remove_buffers( sqe: *linux.io_uring_sqe, num: usize, group_id: usize, ) void` |

## os / linux / ioctl

| Function | Signature |
|----------|-----------|
| `IO` | `pub fn IO(io_type: u8, nr: u8) u32` |
| `IOR` | `pub fn IOR(io_type: u8, nr: u8, comptime T: type) u32` |
| `IOW` | `pub fn IOW(io_type: u8, nr: u8, comptime T: type) u32` |
| `IOWR` | `pub fn IOWR(io_type: u8, nr: u8, comptime T: type) u32` |

## os / linux / mips

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `syscall7` | `pub fn syscall7( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, arg7: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: u32, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore` | `pub fn restore() callconv(.Naked) void` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / powerpc

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: usize, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / powerpc64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: usize, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / riscv64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: u32, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / sparc64

| Function | Signature |
|----------|-----------|
| `syscall_pipe` | `pub fn syscall_pipe(fd: *[2]i32) usize` |
| `syscall_fork` | `pub fn syscall_fork() usize` |
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: usize, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.C) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / linux / start_pie

| Function | Signature |
|----------|-----------|
| `relocate` | `pub fn relocate(phdrs: []elf.Phdr) void` |

## os / linux / thumb

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `restore` | `pub fn restore() callconv(.Naked) void` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |

## os / linux / tls

| Function | Signature |
|----------|-----------|
| `setThreadPointer` | `pub fn setThreadPointer(addr: usize) void` |
| `prepareTLS` | `pub fn prepareTLS(area: []u8) usize` |
| `initStaticTLS` | `pub fn initStaticTLS(phdrs: []elf.Phdr) void` |

## os / linux / vdso

| Function | Signature |
|----------|-----------|
| `lookup` | `pub fn lookup(vername: []const u8, name: []const u8) usize` |

## os / linux / x86_64

| Function | Signature |
|----------|-----------|
| `syscall0` | `pub fn syscall0(number: SYS) usize` |
| `syscall1` | `pub fn syscall1(number: SYS, arg1: usize) usize` |
| `syscall2` | `pub fn syscall2(number: SYS, arg1: usize, arg2: usize) usize` |
| `syscall3` | `pub fn syscall3(number: SYS, arg1: usize, arg2: usize, arg3: usize) usize` |
| `syscall4` | `pub fn syscall4(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize) usize` |
| `syscall5` | `pub fn syscall5(number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize) usize` |
| `syscall6` | `pub fn syscall6( number: SYS, arg1: usize, arg2: usize, arg3: usize, arg4: usize, arg5: usize, arg6: usize, ) usize` |
| `clone` | `pub extern fn clone(func: CloneFn, stack: usize, flags: usize, arg: usize, ptid: *i32, tls: usize, ctid: *i32) usize` |
| `restore_rt` | `pub fn restore_rt() callconv(.Naked) void` |
| `atime` | `pub fn atime(self: @This()) timespec` |
| `mtime` | `pub fn mtime(self: @This()) timespec` |
| `ctime` | `pub fn ctime(self: @This()) timespec` |

## os / plan9

| Function | Signature |
|----------|-----------|
| `pwrite` | `pub fn pwrite(fd: usize, buf: [*]const u8, count: usize, offset: usize) usize` |
| `open` | `pub fn open(path: [*:0]const u8, omode: OpenMode) usize` |
| `create` | `pub fn create(path: [*:0]const u8, omode: OpenMode, perms: usize) usize` |
| `exits` | `pub fn exits(status: ?[*:0]const u8) void` |
| `close` | `pub fn close(fd: usize) usize` |

## os / plan9 / x86_64

| Function | Signature |
|----------|-----------|
| `syscall1` | `pub fn syscall1(sys: plan9.SYS, arg0: usize) usize` |
| `syscall2` | `pub fn syscall2(sys: plan9.SYS, arg0: usize, arg1: usize) usize` |
| `syscall3` | `pub fn syscall3(sys: plan9.SYS, arg0: usize, arg1: usize, arg2: usize) usize` |
| `syscall4` | `pub fn syscall4(sys: plan9.SYS, arg0: usize, arg1: usize, arg2: usize, arg3: usize) usize` |

## os / posix_spawn

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init() Error!Attr` |
| `deinit` | `pub fn deinit(self: *Attr) void` |
| `get` | `pub fn get(self: Attr) Error!u16` |
| `set` | `pub fn set(self: *Attr, flags: u16) Error!void` |
| `init` | `pub fn init() Error!Actions` |
| `deinit` | `pub fn deinit(self: *Actions) void` |
| `open` | `pub fn open(self: *Actions, fd: fd_t, path: []const u8, flags: u32, mode: mode_t) Error!void` |
| `openZ` | `pub fn openZ(self: *Actions, fd: fd_t, path: [*:0]const u8, flags: u32, mode: mode_t) Error!void` |
| `close` | `pub fn close(self: *Actions, fd: fd_t) Error!void` |
| `dup2` | `pub fn dup2(self: *Actions, fd: fd_t, newfd: fd_t) Error!void` |
| `inherit` | `pub fn inherit(self: *Actions, fd: fd_t) Error!void` |
| `chdir` | `pub fn chdir(self: *Actions, path: []const u8) Error!void` |
| `chdirZ` | `pub fn chdirZ(self: *Actions, path: [*:0]const u8) Error!void` |
| `fchdir` | `pub fn fchdir(self: *Actions, fd: fd_t) Error!void` |
| `spawn` | `pub fn spawn( path: []const u8, actions: ?Actions, attr: ?Attr, argv: [*:null]?[*:0]const u8, envp: [*:null]?[*:0]const u8, ) Error!pid_t` |
| `spawnZ` | `pub fn spawnZ( path: [*:0]const u8, actions: ?Actions, attr: ?Attr, argv: [*:null]?[*:0]const u8, envp: [*:null]?[*:0]const u8, ) Error!pid_t` |
| `spawnp` | `pub fn spawnp( file: []const u8, actions: ?Actions, attr: ?Attr, argv: [*:null]?[*:0]const u8, envp: [*:null]?[*:0]const u8, ) Error!pid_t` |
| `spawnpZ` | `pub fn spawnpZ( file: [*:0]const u8, actions: ?Actions, attr: ?Attr, argv: [*:null]?[*:0]const u8, envp: [*:null]?[*:0]const u8, ) Error!pid_t` |
| `waitpid` | `pub fn waitpid(pid: pid_t, flags: u32) Error!WaitPidResult` |

## os / uefi

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format( self: @This(), comptime f: []const u8, options: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `eql` | `pub fn eql(a: std.os.uefi.Guid, b: std.os.uefi.Guid) bool` |

## os / uefi / protocols / absolute_pointer_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *const AbsolutePointerProtocol, verify: bool) Status` |
| `getState` | `pub fn getState(self: *const AbsolutePointerProtocol, state: *AbsolutePointerState) Status` |

## os / uefi / protocols / block_io_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *Self, extended_verification: bool) Status` |
| `readBlocks` | `pub fn readBlocks(self: *Self, media_id: u32, lba: u64, buffer_size: usize, buf: [*]u8) Status` |
| `writeBlocks` | `pub fn writeBlocks(self: *Self, media_id: u32, lba: u64, buffer_size: usize, buf: [*]u8) Status` |
| `flushBlocks` | `pub fn flushBlocks(self: *Self) Status` |

## os / uefi / protocols / device_path_protocol

| Function | Signature |
|----------|-----------|
| `next` | `pub fn next(self: *DevicePathProtocol) ?*DevicePathProtocol` |
| `size` | `pub fn size(self: *DevicePathProtocol) usize` |
| `create_file_device_path` | `pub fn create_file_device_path(self: *DevicePathProtocol, allocator: Allocator, path: [:0]align(1) const u16) !*DevicePathProtocol` |
| `getDevicePath` | `pub fn getDevicePath(self: *const DevicePathProtocol) ?DevicePath` |
| `initSubtype` | `pub fn initSubtype(self: *const DevicePathProtocol, comptime TUnion: type) ?TUnion` |
| `adrs` | `pub fn adrs(self: *const AdrDevicePath) []align(1) const u32` |
| `serial_number` | `pub fn serial_number(self: *const UsbWwidDevicePath) []align(1) const u16` |
| `getPath` | `pub fn getPath(self: *const FilePathDevicePath) [*:0]align(1) const u16` |
| `getDescription` | `pub fn getDescription(self: *const BBS101DevicePath) [*:0]const u8` |

## os / uefi / protocols / edid_override_protocol

| Function | Signature |
|----------|-----------|
| `getEdid` | `pub fn getEdid( self: *const EdidOverrideProtocol, handle: Handle, attributes: *EdidOverrideProtocolAttributes, edid_size: *usize, edid: *?[*]u8, ) Status` |

## os / uefi / protocols / file_protocol

| Function | Signature |
|----------|-----------|
| `seekableStream` | `pub fn seekableStream(self: *FileProtocol) SeekableStream` |
| `reader` | `pub fn reader(self: *FileProtocol) Reader` |
| `writer` | `pub fn writer(self: *FileProtocol) Writer` |
| `open` | `pub fn open(self: *const FileProtocol, new_handle: **const FileProtocol, file_name: [*:0]const u16, open_mode: u64, attributes: u64) Status` |
| `close` | `pub fn close(self: *const FileProtocol) Status` |
| `delete` | `pub fn delete(self: *const FileProtocol) Status` |
| `read` | `pub fn read(self: *const FileProtocol, buffer_size: *usize, buffer: [*]u8) Status` |
| `write` | `pub fn write(self: *const FileProtocol, buffer_size: *usize, buffer: [*]const u8) Status` |
| `getPosition` | `pub fn getPosition(self: *const FileProtocol, position: *u64) Status` |
| `setPosition` | `pub fn setPosition(self: *const FileProtocol, position: u64) Status` |
| `getInfo` | `pub fn getInfo(self: *const FileProtocol, information_type: *align(8) const Guid, buffer_size: *usize, buffer: [*]u8) Status` |
| `setInfo` | `pub fn setInfo(self: *const FileProtocol, information_type: *align(8) const Guid, buffer_size: usize, buffer: [*]const u8) Status` |
| `flush` | `pub fn flush(self: *const FileProtocol) Status` |
| `getFileName` | `pub fn getFileName(self: *const FileInfo) [*:0]const u16` |
| `getVolumeLabel` | `pub fn getVolumeLabel(self: *const FileSystemInfo) [*:0]const u16` |

## os / uefi / protocols / graphics_output_protocol

| Function | Signature |
|----------|-----------|
| `queryMode` | `pub fn queryMode(self: *const GraphicsOutputProtocol, mode: u32, size_of_info: *usize, info: **GraphicsOutputModeInformation) Status` |
| `setMode` | `pub fn setMode(self: *const GraphicsOutputProtocol, mode: u32) Status` |
| `blt` | `pub fn blt(self: *const GraphicsOutputProtocol, blt_buffer: ?[*]GraphicsOutputBltPixel, blt_operation: GraphicsOutputBltOperation, source_x: usize, source_y: usize, destination_x: usize, destination_y: usize, width: usize, height: usize, delta: usize) Status` |

## os / uefi / protocols / hii

| Function | Signature |
|----------|-----------|
| `getNarrowGlyphs` | `pub fn getNarrowGlyphs(self: *HIISimplifiedFontPackage) []NarrowGlyph` |

## os / uefi / protocols / hii_database_protocol

| Function | Signature |
|----------|-----------|
| `removePackageList` | `pub fn removePackageList(self: *const HIIDatabaseProtocol, handle: hii.HIIHandle) Status` |
| `updatePackageList` | `pub fn updatePackageList(self: *const HIIDatabaseProtocol, handle: hii.HIIHandle, buffer: *const hii.HIIPackageList) Status` |
| `listPackageLists` | `pub fn listPackageLists(self: *const HIIDatabaseProtocol, package_type: u8, package_guid: ?*const Guid, buffer_length: *usize, handles: [*]hii.HIIHandle) Status` |
| `exportPackageLists` | `pub fn exportPackageLists(self: *const HIIDatabaseProtocol, handle: ?hii.HIIHandle, buffer_size: *usize, buffer: *hii.HIIPackageList) Status` |

## os / uefi / protocols / hii_popup_protocol

| Function | Signature |
|----------|-----------|
| `createPopup` | `pub fn createPopup(self: *const HIIPopupProtocol, style: HIIPopupStyle, popup_type: HIIPopupType, handle: hii.HIIHandle, msg: u16, user_selection: ?*HIIPopupSelection) Status` |

## os / uefi / protocols / ip6_config_protocol

| Function | Signature |
|----------|-----------|
| `setData` | `pub fn setData(self: *const Ip6ConfigProtocol, data_type: Ip6ConfigDataType, data_size: usize, data: *const anyopaque) Status` |
| `getData` | `pub fn getData(self: *const Ip6ConfigProtocol, data_type: Ip6ConfigDataType, data_size: *usize, data: ?*const anyopaque) Status` |
| `registerDataNotify` | `pub fn registerDataNotify(self: *const Ip6ConfigProtocol, data_type: Ip6ConfigDataType, event: Event) Status` |
| `unregisterDataNotify` | `pub fn unregisterDataNotify(self: *const Ip6ConfigProtocol, data_type: Ip6ConfigDataType, event: Event) Status` |

## os / uefi / protocols / ip6_protocol

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const Ip6Protocol, ip6_mode_data: ?*Ip6ModeData, mnp_config_data: ?*ManagedNetworkConfigData, snp_mode_data: ?*SimpleNetworkMode) Status` |
| `configure` | `pub fn configure(self: *const Ip6Protocol, ip6_config_data: ?*const Ip6ConfigData) Status` |
| `groups` | `pub fn groups(self: *const Ip6Protocol, join_flag: bool, group_address: ?*const Ip6Address) Status` |
| `routes` | `pub fn routes(self: *const Ip6Protocol, delete_route: bool, destination: ?*const Ip6Address, prefix_length: u8, gateway_address: ?*const Ip6Address) Status` |
| `neighbors` | `pub fn neighbors(self: *const Ip6Protocol, delete_flag: bool, target_ip6_address: *const Ip6Address, target_link_address: ?*const MacAddress, timeout: u32, override: bool) Status` |
| `transmit` | `pub fn transmit(self: *const Ip6Protocol, token: *Ip6CompletionToken) Status` |
| `receive` | `pub fn receive(self: *const Ip6Protocol, token: *Ip6CompletionToken) Status` |
| `cancel` | `pub fn cancel(self: *const Ip6Protocol, token: ?*Ip6CompletionToken) Status` |
| `poll` | `pub fn poll(self: *const Ip6Protocol) Status` |

## os / uefi / protocols / ip6_service_binding_protocol

| Function | Signature |
|----------|-----------|
| `createChild` | `pub fn createChild(self: *const Ip6ServiceBindingProtocol, handle: *?Handle) Status` |
| `destroyChild` | `pub fn destroyChild(self: *const Ip6ServiceBindingProtocol, handle: Handle) Status` |

## os / uefi / protocols / loaded_image_protocol

| Function | Signature |
|----------|-----------|
| `unload` | `pub fn unload(self: *const LoadedImageProtocol, handle: Handle) Status` |

## os / uefi / protocols / managed_network_protocol

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const ManagedNetworkProtocol, mnp_config_data: ?*ManagedNetworkConfigData, snp_mode_data: ?*SimpleNetworkMode) Status` |
| `configure` | `pub fn configure(self: *const ManagedNetworkProtocol, mnp_config_data: ?*const ManagedNetworkConfigData) Status` |
| `mcastIpToMac` | `pub fn mcastIpToMac(self: *const ManagedNetworkProtocol, ipv6flag: bool, ipaddress: *const anyopaque, mac_address: *MacAddress) Status` |
| `groups` | `pub fn groups(self: *const ManagedNetworkProtocol, join_flag: bool, mac_address: ?*const MacAddress) Status` |
| `transmit` | `pub fn transmit(self: *const ManagedNetworkProtocol, token: *const ManagedNetworkCompletionToken) Status` |
| `receive` | `pub fn receive(self: *const ManagedNetworkProtocol, token: *const ManagedNetworkCompletionToken) Status` |
| `cancel` | `pub fn cancel(self: *const ManagedNetworkProtocol, token: ?*const ManagedNetworkCompletionToken) Status` |
| `poll` | `pub fn poll(self: *const ManagedNetworkProtocol) Status` |
| `getFragments` | `pub fn getFragments(self: *ManagedNetworkTransmitData) []ManagedNetworkFragmentData` |

## os / uefi / protocols / managed_network_service_binding_protocol

| Function | Signature |
|----------|-----------|
| `createChild` | `pub fn createChild(self: *const ManagedNetworkServiceBindingProtocol, handle: *?Handle) Status` |
| `destroyChild` | `pub fn destroyChild(self: *const ManagedNetworkServiceBindingProtocol, handle: Handle) Status` |

## os / uefi / protocols / rng_protocol

| Function | Signature |
|----------|-----------|
| `getInfo` | `pub fn getInfo(self: *const RNGProtocol, list_size: *usize, list: [*]align(8) Guid) Status` |
| `getRNG` | `pub fn getRNG(self: *const RNGProtocol, algo: ?*align(8) const Guid, value_length: usize, value: [*]u8) Status` |

## os / uefi / protocols / simple_file_system_protocol

| Function | Signature |
|----------|-----------|
| `openVolume` | `pub fn openVolume(self: *const SimpleFileSystemProtocol, root: **const FileProtocol) Status` |

## os / uefi / protocols / simple_network_protocol

| Function | Signature |
|----------|-----------|
| `start` | `pub fn start(self: *const SimpleNetworkProtocol) Status` |
| `stop` | `pub fn stop(self: *const SimpleNetworkProtocol) Status` |
| `initialize` | `pub fn initialize(self: *const SimpleNetworkProtocol, extra_rx_buffer_size: usize, extra_tx_buffer_size: usize) Status` |
| `reset` | `pub fn reset(self: *const SimpleNetworkProtocol, extended_verification: bool) Status` |
| `shutdown` | `pub fn shutdown(self: *const SimpleNetworkProtocol) Status` |
| `receiveFilters` | `pub fn receiveFilters(self: *const SimpleNetworkProtocol, enable: SimpleNetworkReceiveFilter, disable: SimpleNetworkReceiveFilter, reset_mcast_filter: bool, mcast_filter_cnt: usize, mcast_filter: ?[*]const MacAddress) Status` |
| `stationAddress` | `pub fn stationAddress(self: *const SimpleNetworkProtocol, reset_flag: bool, new: ?*const MacAddress) Status` |
| `statistics` | `pub fn statistics(self: *const SimpleNetworkProtocol, reset_flag: bool, statistics_size: ?*usize, statistics_table: ?*NetworkStatistics) Status` |
| `mcastIpToMac` | `pub fn mcastIpToMac(self: *const SimpleNetworkProtocol, ipv6: bool, ip: *const anyopaque, mac: *MacAddress) Status` |
| `nvdata` | `pub fn nvdata(self: *const SimpleNetworkProtocol, read_write: bool, offset: usize, buffer_size: usize, buffer: [*]u8) Status` |
| `getStatus` | `pub fn getStatus(self: *const SimpleNetworkProtocol, interrupt_status: *SimpleNetworkInterruptStatus, tx_buf: ?*?[*]u8) Status` |
| `transmit` | `pub fn transmit(self: *const SimpleNetworkProtocol, header_size: usize, buffer_size: usize, buffer: [*]const u8, src_addr: ?*const MacAddress, dest_addr: ?*const MacAddress, protocol: ?*const u16) Status` |
| `receive` | `pub fn receive(self: *const SimpleNetworkProtocol, header_size: ?*usize, buffer_size: *usize, buffer: [*]u8, src_addr: ?*MacAddress, dest_addr: ?*MacAddress, protocol: ?*u16) Status` |

## os / uefi / protocols / simple_pointer_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *const SimplePointerProtocol, verify: bool) Status` |
| `getState` | `pub fn getState(self: *const SimplePointerProtocol, state: *SimplePointerState) Status` |

## os / uefi / protocols / simple_text_input_ex_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *const SimpleTextInputExProtocol, verify: bool) Status` |
| `readKeyStrokeEx` | `pub fn readKeyStrokeEx(self: *const SimpleTextInputExProtocol, key_data: *KeyData) Status` |
| `setState` | `pub fn setState(self: *const SimpleTextInputExProtocol, state: *const u8) Status` |
| `registerKeyNotify` | `pub fn registerKeyNotify(self: *const SimpleTextInputExProtocol, key_data: *const KeyData, notify: std.meta.FnPtr(fn (*const KeyData) callconv(.C) usize), handle: **anyopaque) Status` |
| `unregisterKeyNotify` | `pub fn unregisterKeyNotify(self: *const SimpleTextInputExProtocol, handle: *const anyopaque) Status` |

## os / uefi / protocols / simple_text_input_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *const SimpleTextInputProtocol, verify: bool) Status` |
| `readKeyStroke` | `pub fn readKeyStroke(self: *const SimpleTextInputProtocol, input_key: *InputKey) Status` |

## os / uefi / protocols / simple_text_output_protocol

| Function | Signature |
|----------|-----------|
| `reset` | `pub fn reset(self: *const SimpleTextOutputProtocol, verify: bool) Status` |
| `outputString` | `pub fn outputString(self: *const SimpleTextOutputProtocol, msg: [*:0]const u16) Status` |
| `testString` | `pub fn testString(self: *const SimpleTextOutputProtocol, msg: [*:0]const u16) Status` |
| `queryMode` | `pub fn queryMode(self: *const SimpleTextOutputProtocol, mode_number: usize, columns: *usize, rows: *usize) Status` |
| `setMode` | `pub fn setMode(self: *const SimpleTextOutputProtocol, mode_number: usize) Status` |
| `setAttribute` | `pub fn setAttribute(self: *const SimpleTextOutputProtocol, attribute: usize) Status` |
| `clearScreen` | `pub fn clearScreen(self: *const SimpleTextOutputProtocol) Status` |
| `setCursorPosition` | `pub fn setCursorPosition(self: *const SimpleTextOutputProtocol, column: usize, row: usize) Status` |
| `enableCursor` | `pub fn enableCursor(self: *const SimpleTextOutputProtocol, visible: bool) Status` |

## os / uefi / protocols / udp6_protocol

| Function | Signature |
|----------|-----------|
| `getModeData` | `pub fn getModeData(self: *const Udp6Protocol, udp6_config_data: ?*Udp6ConfigData, ip6_mode_data: ?*Ip6ModeData, mnp_config_data: ?*ManagedNetworkConfigData, snp_mode_data: ?*SimpleNetworkMode) Status` |
| `configure` | `pub fn configure(self: *const Udp6Protocol, udp6_config_data: ?*const Udp6ConfigData) Status` |
| `groups` | `pub fn groups(self: *const Udp6Protocol, join_flag: bool, multicast_address: ?*const Ip6Address) Status` |
| `transmit` | `pub fn transmit(self: *const Udp6Protocol, token: *Udp6CompletionToken) Status` |
| `receive` | `pub fn receive(self: *const Udp6Protocol, token: *Udp6CompletionToken) Status` |
| `cancel` | `pub fn cancel(self: *const Udp6Protocol, token: ?*Udp6CompletionToken) Status` |
| `poll` | `pub fn poll(self: *const Udp6Protocol) Status` |
| `getFragments` | `pub fn getFragments(self: *Udp6ReceiveData) []Udp6FragmentData` |
| `getFragments` | `pub fn getFragments(self: *Udp6TransmitData) []Udp6FragmentData` |

## os / uefi / protocols / udp6_service_binding_protocol

| Function | Signature |
|----------|-----------|
| `createChild` | `pub fn createChild(self: *const Udp6ServiceBindingProtocol, handle: *?Handle) Status` |
| `destroyChild` | `pub fn destroyChild(self: *const Udp6ServiceBindingProtocol, handle: Handle) Status` |

## os / uefi / status

| Function | Signature |
|----------|-----------|
| `err` | `pub fn err(self: Status) EfiError!void` |

## os / uefi / tables / boot_services

| Function | Signature |
|----------|-----------|
| `openProtocolSt` | `pub fn openProtocolSt(self: *BootServices, comptime protocol: type, handle: Handle) !*protocol` |

## os / wasi

| Function | Signature |
|----------|-----------|
| `getErrno` | `pub fn getErrno(r: errno_t) errno_t` |
| `fromTimestamp` | `pub fn fromTimestamp(tm: timestamp_t) timespec` |
| `toTimestamp` | `pub fn toTimestamp(ts: timespec) timestamp_t` |
| `fromFilestat` | `pub fn fromFilestat(stat: filestat_t) Self` |
| `atime` | `pub fn atime(self: Self) timespec` |
| `mtime` | `pub fn mtime(self: Self) timespec` |
| `ctime` | `pub fn ctime(self: Self) timespec` |
| `atime` | `pub fn atime(self: filestat_t) timespec` |
| `mtime` | `pub fn mtime(self: filestat_t) timespec` |
| `ctime` | `pub fn ctime(self: filestat_t) timespec` |

## os / windows

| Function | Signature |
|----------|-----------|
| `OpenFile` | `pub fn OpenFile(sub_path_w: []const u16, options: OpenFileOptions) OpenError!HANDLE` |
| `CreatePipe` | `pub fn CreatePipe(rd: *HANDLE, wr: *HANDLE, sattr: *const SECURITY_ATTRIBUTES) CreatePipeError!void` |
| `CreateEventEx` | `pub fn CreateEventEx(attributes: ?*SECURITY_ATTRIBUTES, name: []const u8, flags: DWORD, desired_access: DWORD) !HANDLE` |
| `CreateEventExW` | `pub fn CreateEventExW(attributes: ?*SECURITY_ATTRIBUTES, nameW: [*:0]const u16, flags: DWORD, desired_access: DWORD) !HANDLE` |
| `DeviceIoControl` | `pub fn DeviceIoControl( h: HANDLE, ioControlCode: ULONG, in: ?[]const u8, out: ?[]u8, ) DeviceIoControlError!void` |
| `GetOverlappedResult` | `pub fn GetOverlappedResult(h: HANDLE, overlapped: *OVERLAPPED, wait: bool) !DWORD` |
| `SetHandleInformation` | `pub fn SetHandleInformation(h: HANDLE, mask: DWORD, flags: DWORD) SetHandleInformationError!void` |
| `RtlGenRandom` | `pub fn RtlGenRandom(output: []u8) RtlGenRandomError!void` |
| `WaitForSingleObject` | `pub fn WaitForSingleObject(handle: HANDLE, milliseconds: DWORD) WaitForSingleObjectError!void` |
| `WaitForSingleObjectEx` | `pub fn WaitForSingleObjectEx(handle: HANDLE, milliseconds: DWORD, alertable: bool) WaitForSingleObjectError!void` |
| `WaitForMultipleObjectsEx` | `pub fn WaitForMultipleObjectsEx(handles: []const HANDLE, waitAll: bool, milliseconds: DWORD, alertable: bool) !u32` |
| `CreateIoCompletionPort` | `pub fn CreateIoCompletionPort( file_handle: HANDLE, existing_completion_port: ?HANDLE, completion_key: usize, concurrent_thread_count: DWORD, ) CreateIoCompletionPortError!HANDLE` |
| `PostQueuedCompletionStatus` | `pub fn PostQueuedCompletionStatus( completion_port: HANDLE, bytes_transferred_count: DWORD, completion_key: usize, lpOverlapped: ?*OVERLAPPED, ) PostQueuedCompletionStatusError!void` |
| `GetQueuedCompletionStatus` | `pub fn GetQueuedCompletionStatus( completion_port: HANDLE, bytes_transferred_count: *DWORD, lpCompletionKey: *usize, lpOverlapped: *?*OVERLAPPED, dwMilliseconds: DWORD, ) GetQueuedCompletionStatusResult` |
| `GetQueuedCompletionStatusEx` | `pub fn GetQueuedCompletionStatusEx( completion_port: HANDLE, completion_port_entries: []OVERLAPPED_ENTRY, timeout_ms: ?DWORD, alertable: bool, ) GetQueuedCompletionStatusError!u32` |
| `CloseHandle` | `pub fn CloseHandle(hObject: HANDLE) void` |
| `FindClose` | `pub fn FindClose(hFindFile: HANDLE) void` |
| `ReadFile` | `pub fn ReadFile(in_hFile: HANDLE, buffer: []u8, offset: ?u64, io_mode: std.io.ModeOverride) ReadFileError!usize` |
| `WriteFile` | `pub fn WriteFile( handle: HANDLE, bytes: []const u8, offset: ?u64, io_mode: std.io.ModeOverride, ) WriteFileError!usize` |
| `SetCurrentDirectory` | `pub fn SetCurrentDirectory(path_name: []const u16) SetCurrentDirectoryError!void` |
| `GetCurrentDirectory` | `pub fn GetCurrentDirectory(buffer: []u8) GetCurrentDirectoryError![]u8` |
| `CreateSymbolicLink` | `pub fn CreateSymbolicLink( dir: ?HANDLE, sym_link_path: []const u16, target_path: []const u16, is_directory: bool, ) CreateSymbolicLinkError!void` |
| `ReadLink` | `pub fn ReadLink(dir: ?HANDLE, sub_path_w: []const u16, out_buffer: []u8) ReadLinkError![]u8` |
| `DeleteFile` | `pub fn DeleteFile(sub_path_w: []const u16, options: DeleteFileOptions) DeleteFileError!void` |
| `MoveFileEx` | `pub fn MoveFileEx(old_path: []const u8, new_path: []const u8, flags: DWORD) MoveFileError!void` |
| `MoveFileExW` | `pub fn MoveFileExW(old_path: [*:0]const u16, new_path: [*:0]const u16, flags: DWORD) MoveFileError!void` |
| `GetStdHandle` | `pub fn GetStdHandle(handle_id: DWORD) GetStdHandleError!HANDLE` |
| `SetFilePointerEx_BEGIN` | `pub fn SetFilePointerEx_BEGIN(handle: HANDLE, offset: u64) SetFilePointerError!void` |
| `SetFilePointerEx_CURRENT` | `pub fn SetFilePointerEx_CURRENT(handle: HANDLE, offset: i64) SetFilePointerError!void` |
| `SetFilePointerEx_END` | `pub fn SetFilePointerEx_END(handle: HANDLE, offset: i64) SetFilePointerError!void` |
| `SetFilePointerEx_CURRENT_get` | `pub fn SetFilePointerEx_CURRENT_get(handle: HANDLE) SetFilePointerError!u64` |
| `QueryObjectName` | `pub fn QueryObjectName( handle: HANDLE, out_buffer: []u16, ) ![]u16` |
| `GetFinalPathNameByHandle` | `pub fn GetFinalPathNameByHandle( hFile: HANDLE, fmt: GetFinalPathNameByHandleFormat, out_buffer: []u16, ) GetFinalPathNameByHandleError![]u16` |
| `QueryInformationFile` | `pub fn QueryInformationFile( handle: HANDLE, info_class: FILE_INFORMATION_CLASS, out_buffer: []u8, ) QueryInformationFileError!void` |
| `GetFileSizeEx` | `pub fn GetFileSizeEx(hFile: HANDLE) GetFileSizeError!u64` |
| `GetFileAttributes` | `pub fn GetFileAttributes(filename: []const u8) GetFileAttributesError!DWORD` |
| `GetFileAttributesW` | `pub fn GetFileAttributesW(lpFileName: [*:0]const u16) GetFileAttributesError!DWORD` |
| `WSAStartup` | `pub fn WSAStartup(majorVersion: u8, minorVersion: u8) !ws2_32.WSADATA` |
| `WSACleanup` | `pub fn WSACleanup() !void` |
| `WSASocketW` | `pub fn WSASocketW( af: i32, socket_type: i32, protocol: i32, protocolInfo: ?*ws2_32.WSAPROTOCOL_INFOW, g: ws2_32.GROUP, dwFlags: DWORD, ) !ws2_32.SOCKET` |
| `bind` | `pub fn bind(s: ws2_32.SOCKET, name: *const ws2_32.sockaddr, namelen: ws2_32.socklen_t) i32` |
| `listen` | `pub fn listen(s: ws2_32.SOCKET, backlog: u31) i32` |
| `closesocket` | `pub fn closesocket(s: ws2_32.SOCKET) !void` |
| `accept` | `pub fn accept(s: ws2_32.SOCKET, name: ?*ws2_32.sockaddr, namelen: ?*ws2_32.socklen_t) ws2_32.SOCKET` |
| `getsockname` | `pub fn getsockname(s: ws2_32.SOCKET, name: *ws2_32.sockaddr, namelen: *ws2_32.socklen_t) i32` |
| `getpeername` | `pub fn getpeername(s: ws2_32.SOCKET, name: *ws2_32.sockaddr, namelen: *ws2_32.socklen_t) i32` |
| `sendmsg` | `pub fn sendmsg( s: ws2_32.SOCKET, msg: *const ws2_32.WSAMSG, flags: u32, ) i32` |
| `sendto` | `pub fn sendto(s: ws2_32.SOCKET, buf: [*]const u8, len: usize, flags: u32, to: ?*const ws2_32.sockaddr, to_len: ws2_32.socklen_t) i32` |
| `recvfrom` | `pub fn recvfrom(s: ws2_32.SOCKET, buf: [*]u8, len: usize, flags: u32, from: ?*ws2_32.sockaddr, from_len: ?*ws2_32.socklen_t) i32` |
| `poll` | `pub fn poll(fds: [*]ws2_32.pollfd, n: c_ulong, timeout: i32) i32` |
| `WSAIoctl` | `pub fn WSAIoctl( s: ws2_32.SOCKET, dwIoControlCode: DWORD, inBuffer: ?[]const u8, outBuffer: []u8, overlapped: ?*OVERLAPPED, completionRoutine: ?ws2_32.LPWSAOVERLAPPED_COMPLETION_ROUTINE, ) !DWORD` |
| `GetModuleFileNameW` | `pub fn GetModuleFileNameW(hModule: ?HMODULE, buf_ptr: [*]u16, buf_len: DWORD) GetModuleFileNameError![:0]u16` |
| `TerminateProcess` | `pub fn TerminateProcess(hProcess: HANDLE, uExitCode: UINT) TerminateProcessError!void` |
| `VirtualAlloc` | `pub fn VirtualAlloc(addr: ?LPVOID, size: usize, alloc_type: DWORD, flProtect: DWORD) VirtualAllocError!LPVOID` |
| `VirtualFree` | `pub fn VirtualFree(lpAddress: ?LPVOID, dwSize: usize, dwFreeType: DWORD) void` |
| `VirtualQuery` | `pub fn VirtualQuery(lpAddress: ?LPVOID, lpBuffer: PMEMORY_BASIC_INFORMATION, dwLength: SIZE_T) VirtualQuerryError!SIZE_T` |
| `SetConsoleTextAttribute` | `pub fn SetConsoleTextAttribute(hConsoleOutput: HANDLE, wAttributes: WORD) SetConsoleTextAttributeError!void` |
| `SetConsoleCtrlHandler` | `pub fn SetConsoleCtrlHandler(handler_routine: ?HANDLER_ROUTINE, add: bool) !void` |
| `SetFileCompletionNotificationModes` | `pub fn SetFileCompletionNotificationModes(handle: HANDLE, flags: UCHAR) !void` |
| `GetEnvironmentStringsW` | `pub fn GetEnvironmentStringsW() GetEnvironmentStringsError![*:0]u16` |
| `FreeEnvironmentStringsW` | `pub fn FreeEnvironmentStringsW(penv: [*:0]u16) void` |
| `GetEnvironmentVariableW` | `pub fn GetEnvironmentVariableW(lpName: LPWSTR, lpBuffer: [*]u16, nSize: DWORD) GetEnvironmentVariableError!DWORD` |
| `CreateProcessW` | `pub fn CreateProcessW( lpApplicationName: ?LPWSTR, lpCommandLine: LPWSTR, lpProcessAttributes: ?*SECURITY_ATTRIBUTES, lpThreadAttributes: ?*SECURITY_ATTRIBUTES, bInheritHandles: BOOL, dwCreationFlags: DWORD, lpEnvironment: ?*anyopaque, lpCurrentDirectory: ?LPWSTR, lpStartupInfo: *STARTUPINFOW, lpProcessInformation: *PROCESS_INFORMATION, ) CreateProcessError!void` |
| `LoadLibraryW` | `pub fn LoadLibraryW(lpLibFileName: [*:0]const u16) LoadLibraryError!HMODULE` |
| `FreeLibrary` | `pub fn FreeLibrary(hModule: HMODULE) void` |
| `QueryPerformanceFrequency` | `pub fn QueryPerformanceFrequency() u64` |
| `QueryPerformanceCounter` | `pub fn QueryPerformanceCounter() u64` |
| `InitOnceExecuteOnce` | `pub fn InitOnceExecuteOnce(InitOnce: *INIT_ONCE, InitFn: INIT_ONCE_FN, Parameter: ?*anyopaque, Context: ?*anyopaque) void` |
| `HeapFree` | `pub fn HeapFree(hHeap: HANDLE, dwFlags: DWORD, lpMem: *anyopaque) void` |
| `HeapDestroy` | `pub fn HeapDestroy(hHeap: HANDLE) void` |
| `LocalFree` | `pub fn LocalFree(hMem: HLOCAL) void` |
| `GetFileInformationByHandle` | `pub fn GetFileInformationByHandle( hFile: HANDLE, ) GetFileInformationByHandleError!BY_HANDLE_FILE_INFORMATION` |
| `SetFileTime` | `pub fn SetFileTime( hFile: HANDLE, lpCreationTime: ?*const FILETIME, lpLastAccessTime: ?*const FILETIME, lpLastWriteTime: ?*const FILETIME, ) SetFileTimeError!void` |
| `LockFile` | `pub fn LockFile( FileHandle: HANDLE, Event: ?HANDLE, ApcRoutine: ?*IO_APC_ROUTINE, ApcContext: ?*anyopaque, IoStatusBlock: *IO_STATUS_BLOCK, ByteOffset: *const LARGE_INTEGER, Length: *const LARGE_INTEGER, Key: ?*ULONG, FailImmediately: BOOLEAN, ExclusiveLock: BOOLEAN, ) !void` |
| `UnlockFile` | `pub fn UnlockFile( FileHandle: HANDLE, IoStatusBlock: *IO_STATUS_BLOCK, ByteOffset: *const LARGE_INTEGER, Length: *const LARGE_INTEGER, Key: ?*ULONG, ) !void` |
| `teb` | `pub fn teb() *TEB` |
| `peb` | `pub fn peb() *PEB` |
| `fromSysTime` | `pub fn fromSysTime(hns: i64) i128` |
| `toSysTime` | `pub fn toSysTime(ns: i128) i64` |
| `fileTimeToNanoSeconds` | `pub fn fileTimeToNanoSeconds(ft: FILETIME) i128` |
| `nanoSecondsToFileTime` | `pub fn nanoSecondsToFileTime(ns: i128) FILETIME` |
| `span` | `pub fn span(self: *const PathSpace) [:0]const u16` |
| `removeDotDirsSanitized` | `pub fn removeDotDirsSanitized(comptime T: type, path: []T) RemoveDotDirsError!usize` |
| `normalizePath` | `pub fn normalizePath(comptime T: type, path: []T) RemoveDotDirsError!usize` |
| `cStrToPrefixedFileW` | `pub fn cStrToPrefixedFileW(s: [*:0]const u8) !PathSpace` |
| `sliceToPrefixedFileW` | `pub fn sliceToPrefixedFileW(s: []const u8) !PathSpace` |
| `wToPrefixedFileW` | `pub fn wToPrefixedFileW(s: []const u16) !PathSpace` |
| `loadWinsockExtensionFunction` | `pub fn loadWinsockExtensionFunction(comptime T: type, sock: ws2_32.SOCKET, guid: GUID) !T` |
| `unexpectedError` | `pub fn unexpectedError(err: Win32Error) std.os.UnexpectedError` |
| `unexpectedWSAError` | `pub fn unexpectedWSAError(err: ws2_32.WinsockError) std.os.UnexpectedError` |
| `unexpectedStatus` | `pub fn unexpectedStatus(status: NTSTATUS) std.os.UnexpectedError` |
| `CTL_CODE` | `pub fn CTL_CODE(deviceType: u16, function: u12, method: TransferType, access: u2) DWORD` |
| `parse` | `pub fn parse(s: []const u8) GUID` |
| `parseNoBraces` | `pub fn parseNoBraces(s: []const u8) !GUID` |
| `getRegs` | `pub fn getRegs(ctx: *const CONTEXT) struct` |
| `getRegs` | `pub fn getRegs(ctx: *const CONTEXT) struct` |
| `getRegs` | `pub fn getRegs(ctx: *const CONTEXT) struct` |
| `IsProcessorFeaturePresent` | `pub fn IsProcessorFeaturePresent(feature: PF) bool` |

## os / windows / user32

| Function | Signature |
|----------|-----------|
| `getMessageA` | `pub fn getMessageA(lpMsg: *MSG, hWnd: ?HWND, wMsgFilterMin: u32, wMsgFilterMax: u32) !void` |
| `getMessageW` | `pub fn getMessageW(lpMsg: *MSG, hWnd: ?HWND, wMsgFilterMin: u32, wMsgFilterMax: u32) !void` |
| `peekMessageA` | `pub fn peekMessageA(lpMsg: *MSG, hWnd: ?HWND, wMsgFilterMin: u32, wMsgFilterMax: u32, wRemoveMsg: u32) !bool` |
| `peekMessageW` | `pub fn peekMessageW(lpMsg: *MSG, hWnd: ?HWND, wMsgFilterMin: u32, wMsgFilterMax: u32, wRemoveMsg: u32) !bool` |
| `translateMessage` | `pub fn translateMessage(lpMsg: *const MSG) bool` |
| `dispatchMessageA` | `pub fn dispatchMessageA(lpMsg: *const MSG) LRESULT` |
| `dispatchMessageW` | `pub fn dispatchMessageW(lpMsg: *const MSG) LRESULT` |
| `postQuitMessage` | `pub fn postQuitMessage(nExitCode: i32) void` |
| `defWindowProcA` | `pub fn defWindowProcA(hWnd: HWND, Msg: UINT, wParam: WPARAM, lParam: LPARAM) LRESULT` |
| `defWindowProcW` | `pub fn defWindowProcW(hWnd: HWND, Msg: UINT, wParam: WPARAM, lParam: LPARAM) LRESULT` |
| `registerClassExA` | `pub fn registerClassExA(window_class: *const WNDCLASSEXA) !ATOM` |
| `registerClassExW` | `pub fn registerClassExW(window_class: *const WNDCLASSEXW) !ATOM` |
| `unregisterClassA` | `pub fn unregisterClassA(lpClassName: [*:0]const u8, hInstance: HINSTANCE) !void` |
| `unregisterClassW` | `pub fn unregisterClassW(lpClassName: [*:0]const u16, hInstance: HINSTANCE) !void` |
| `createWindowExA` | `pub fn createWindowExA(dwExStyle: u32, lpClassName: [*:0]const u8, lpWindowName: [*:0]const u8, dwStyle: u32, X: i32, Y: i32, nWidth: i32, nHeight: i32, hWindParent: ?HWND, hMenu: ?HMENU, hInstance: HINSTANCE, lpParam: ?*anyopaque) !HWND` |
| `createWindowExW` | `pub fn createWindowExW(dwExStyle: u32, lpClassName: [*:0]const u16, lpWindowName: [*:0]const u16, dwStyle: u32, X: i32, Y: i32, nWidth: i32, nHeight: i32, hWindParent: ?HWND, hMenu: ?HMENU, hInstance: HINSTANCE, lpParam: ?*anyopaque) !HWND` |
| `destroyWindow` | `pub fn destroyWindow(hWnd: HWND) !void` |
| `showWindow` | `pub fn showWindow(hWnd: HWND, nCmdShow: i32) bool` |
| `updateWindow` | `pub fn updateWindow(hWnd: HWND) !void` |
| `adjustWindowRectEx` | `pub fn adjustWindowRectEx(lpRect: *RECT, dwStyle: u32, bMenu: bool, dwExStyle: u32) !void` |
| `getWindowLongA` | `pub fn getWindowLongA(hWnd: HWND, nIndex: i32) !i32` |
| `getWindowLongW` | `pub fn getWindowLongW(hWnd: HWND, nIndex: i32) !i32` |
| `getWindowLongPtrA` | `pub fn getWindowLongPtrA(hWnd: HWND, nIndex: i32) !isize` |
| `getWindowLongPtrW` | `pub fn getWindowLongPtrW(hWnd: HWND, nIndex: i32) !isize` |
| `setWindowLongA` | `pub fn setWindowLongA(hWnd: HWND, nIndex: i32, dwNewLong: i32) !i32` |
| `setWindowLongW` | `pub fn setWindowLongW(hWnd: HWND, nIndex: i32, dwNewLong: i32) !i32` |
| `setWindowLongPtrA` | `pub fn setWindowLongPtrA(hWnd: HWND, nIndex: i32, dwNewLong: isize) !isize` |
| `setWindowLongPtrW` | `pub fn setWindowLongPtrW(hWnd: HWND, nIndex: i32, dwNewLong: isize) !isize` |
| `getDC` | `pub fn getDC(hWnd: ?HWND) !HDC` |
| `releaseDC` | `pub fn releaseDC(hWnd: ?HWND, hDC: HDC) bool` |
| `messageBoxA` | `pub fn messageBoxA(hWnd: ?HWND, lpText: [*:0]const u8, lpCaption: [*:0]const u8, uType: u32) !i32` |
| `messageBoxW` | `pub fn messageBoxW(hWnd: ?HWND, lpText: [*:0]const u16, lpCaption: [*:0]const u16, uType: u32) !i32` |

## packed_int_array

| Function | Signature |
|----------|-----------|
| `PackedIntIo` | `pub fn PackedIntIo(comptime Int: type, comptime endian: Endian) type` |
| `get` | `pub fn get(bytes: []const u8, index: usize, bit_offset: u7) Int` |
| `set` | `pub fn set(bytes: []u8, index: usize, bit_offset: u3, int: Int) void` |
| `slice` | `pub fn slice(bytes: []u8, bit_offset: u3, start: usize, end: usize) PackedIntSliceEndian(Int, endian)` |
| `sliceCast` | `pub fn sliceCast(bytes: []u8, comptime NewInt: type, comptime new_endian: Endian, bit_offset: u3, old_len: usize) PackedIntSliceEndian(NewInt, new_endian)` |
| `PackedIntArray` | `pub fn PackedIntArray(comptime Int: type, comptime int_count: usize) type` |
| `PackedIntArrayEndian` | `pub fn PackedIntArrayEndian(comptime Int: type, comptime endian: Endian, comptime int_count: usize) type` |
| `init` | `pub fn init(ints: [int_count]Int) Self` |
| `initAllTo` | `pub fn initAllTo(int: Int) Self` |
| `get` | `pub fn get(self: Self, index: usize) Int` |
| `set` | `pub fn set(self: *Self, index: usize, int: Int) void` |
| `setAll` | `pub fn setAll(self: *Self, int: Int) void` |
| `slice` | `pub fn slice(self: *Self, start: usize, end: usize) PackedIntSliceEndian(Int, endian)` |
| `sliceCast` | `pub fn sliceCast(self: *Self, comptime NewInt: type) PackedIntSlice(NewInt)` |
| `sliceCastEndian` | `pub fn sliceCastEndian(self: *Self, comptime NewInt: type, comptime new_endian: Endian) PackedIntSliceEndian(NewInt, new_endian)` |
| `PackedIntSlice` | `pub fn PackedIntSlice(comptime Int: type) type` |
| `PackedIntSliceEndian` | `pub fn PackedIntSliceEndian(comptime Int: type, comptime endian: Endian) type` |
| `bytesRequired` | `pub fn bytesRequired(int_count: usize) usize` |
| `init` | `pub fn init(bytes: []u8, int_count: usize) Self` |
| `get` | `pub fn get(self: Self, index: usize) Int` |
| `set` | `pub fn set(self: *Self, index: usize, int: Int) void` |
| `slice` | `pub fn slice(self: Self, start: usize, end: usize) PackedIntSliceEndian(Int, endian)` |
| `sliceCast` | `pub fn sliceCast(self: Self, comptime NewInt: type) PackedIntSliceEndian(NewInt, endian)` |
| `sliceCastEndian` | `pub fn sliceCastEndian(self: Self, comptime NewInt: type, comptime new_endian: Endian) PackedIntSliceEndian(NewInt, new_endian)` |

## pdb

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(self: *Module, allocator: mem.Allocator) void` |
| `init` | `pub fn init(allocator: mem.Allocator, path: []const u8) !Pdb` |
| `deinit` | `pub fn deinit(self: *Pdb) void` |
| `parseDbiStream` | `pub fn parseDbiStream(self: *Pdb) !void` |
| `parseInfoStream` | `pub fn parseInfoStream(self: *Pdb) !void` |
| `getSymbolName` | `pub fn getSymbolName(self: *Pdb, module: *Module, address: u64) ?[]const u8` |
| `getLineNumberInfo` | `pub fn getLineNumberInfo(self: *Pdb, module: *Module, address: u64) !debug.LineInfo` |
| `getModule` | `pub fn getModule(self: *Pdb, index: usize) !?*Module` |
| `getStreamById` | `pub fn getStreamById(self: *Pdb, id: u32) ?*MsfStream` |
| `getStream` | `pub fn getStream(self: *Pdb, stream: StreamType) ?*MsfStream` |
| `seekBy` | `pub fn seekBy(self: *MsfStream, len: i64) !void` |
| `seekTo` | `pub fn seekTo(self: *MsfStream, len: u64) !void` |
| `reader` | `pub fn reader(self: *MsfStream) std.io.Reader(*MsfStream, Error, read)` |

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
| `removeMinOrNull` | `pub fn removeMinOrNull(self: *Self) ?T` |
| `removeMin` | `pub fn removeMin(self: *Self) T` |
| `removeMaxOrNull` | `pub fn removeMaxOrNull(self: *Self) ?T` |
| `removeMax` | `pub fn removeMax(self: *Self) T` |
| `removeIndex` | `pub fn removeIndex(self: *Self, index: usize) T` |
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
| `removeOrNull` | `pub fn removeOrNull(self: *Self) ?T` |
| `remove` | `pub fn remove(self: *Self) T` |
| `removeIndex` | `pub fn removeIndex(self: *Self, index: usize) T` |
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

## process

| Function | Signature |
|----------|-----------|
| `getCwd` | `pub fn getCwd(out_buffer: []u8) ![]u8` |
| `getCwdAlloc` | `pub fn getCwdAlloc(allocator: Allocator) ![]u8` |
| `hash` | `pub fn hash(self: @This(), s: []const u8) u64` |
| `eql` | `pub fn eql(self: @This(), a: []const u8, b: []const u8) bool` |
| `init` | `pub fn init(allocator: Allocator) EnvMap` |
| `deinit` | `pub fn deinit(self: *EnvMap) void` |
| `putMove` | `pub fn putMove(self: *EnvMap, key: []u8, value: []u8) !void` |
| `put` | `pub fn put(self: *EnvMap, key: []const u8, value: []const u8) !void` |
| `getPtr` | `pub fn getPtr(self: EnvMap, key: []const u8) ?*[]const u8` |
| `get` | `pub fn get(self: EnvMap, key: []const u8) ?[]const u8` |
| `remove` | `pub fn remove(self: *EnvMap, key: []const u8) void` |
| `count` | `pub fn count(self: EnvMap) HashMap.Size` |
| `iterator` | `pub fn iterator(self: *const EnvMap) HashMap.Iterator` |
| `getEnvMap` | `pub fn getEnvMap(allocator: Allocator) !EnvMap` |
| `getEnvVarOwned` | `pub fn getEnvVarOwned(allocator: mem.Allocator, key: []const u8) GetEnvVarOwnedError![]u8` |
| `hasEnvVarConstant` | `pub fn hasEnvVarConstant(comptime key: []const u8) bool` |
| `hasEnvVar` | `pub fn hasEnvVar(allocator: Allocator, key: []const u8) error` |
| `init` | `pub fn init() ArgIteratorPosix` |
| `next` | `pub fn next(self: *ArgIteratorPosix) ?[:0]const u8` |
| `skip` | `pub fn skip(self: *ArgIteratorPosix) bool` |
| `init` | `pub fn init(allocator: mem.Allocator) InitError!ArgIteratorWasi` |
| `next` | `pub fn next(self: *ArgIteratorWasi) ?[:0]const u8` |
| `skip` | `pub fn skip(self: *ArgIteratorWasi) bool` |
| `deinit` | `pub fn deinit(self: *ArgIteratorWasi) void` |
| `ArgIteratorGeneral` | `pub fn ArgIteratorGeneral(comptime options: ArgIteratorGeneralOptions) type` |
| `init` | `pub fn init(allocator: Allocator, cmd_line_utf8: []const u8) InitError!Self` |
| `initTakeOwnership` | `pub fn initTakeOwnership(allocator: Allocator, cmd_line_utf8: []const u8) InitError!Self` |
| `initUtf16le` | `pub fn initUtf16le(allocator: Allocator, cmd_line_utf16le: [*:0]const u16) InitUtf16leError!Self` |
| `skip` | `pub fn skip(self: *Self) bool` |
| `next` | `pub fn next(self: *Self) ?[:0]const u8` |
| `deinit` | `pub fn deinit(self: *Self) void` |
| `init` | `pub fn init() ArgIterator` |
| `initWithAllocator` | `pub fn initWithAllocator(allocator: mem.Allocator) InitError!ArgIterator` |
| `next` | `pub fn next(self: *ArgIterator) ?([:0]const u8)` |
| `skip` | `pub fn skip(self: *ArgIterator) bool` |
| `deinit` | `pub fn deinit(self: *ArgIterator) void` |
| `args` | `pub fn args() ArgIterator` |
| `argsWithAllocator` | `pub fn argsWithAllocator(allocator: mem.Allocator) ArgIterator.InitError!ArgIterator` |
| `argsAlloc` | `pub fn argsAlloc(allocator: mem.Allocator) ![][:0]u8` |
| `argsFree` | `pub fn argsFree(allocator: mem.Allocator, args_alloc: []const [:0]u8) void` |
| `getUserInfo` | `pub fn getUserInfo(name: []const u8) !UserInfo` |
| `posixGetUserInfo` | `pub fn posixGetUserInfo(name: []const u8) !UserInfo` |
| `getBaseAddress` | `pub fn getBaseAddress() usize` |
| `getSelfExeSharedLibPaths` | `pub fn getSelfExeSharedLibPaths(allocator: Allocator) error` |
| `execv` | `pub fn execv(allocator: mem.Allocator, argv: []const []const u8) ExecvError` |
| `execve` | `pub fn execve( allocator: mem.Allocator, argv: []const []const u8, env_map: ?*const EnvMap, ) ExecvError` |

## Progress

| Function | Signature |
|----------|-----------|
| `start` | `pub fn start(self: *Node, name: []const u8, estimated_total_items: usize) Node` |
| `completeOne` | `pub fn completeOne(self: *Node) void` |
| `end` | `pub fn end(self: *Node) void` |
| `activate` | `pub fn activate(self: *Node) void` |
| `setEstimatedTotalItems` | `pub fn setEstimatedTotalItems(self: *Node, count: usize) void` |
| `setCompletedItems` | `pub fn setCompletedItems(self: *Node, completed_items: usize) void` |
| `start` | `pub fn start(self: *Progress, name: []const u8, estimated_total_items: usize) *Node` |
| `maybeRefresh` | `pub fn maybeRefresh(self: *Progress) void` |
| `refresh` | `pub fn refresh(self: *Progress) void` |
| `log` | `pub fn log(self: *Progress, comptime format: []const u8, args: anytype) void` |

## rand

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(pointer: anytype, comptime fillFn: fn (ptr: @TypeOf(pointer), buf: []u8) void) Random` |
| `bytes` | `pub fn bytes(r: Random, buf: []u8) void` |
| `boolean` | `pub fn boolean(r: Random) bool` |
| `enumValue` | `pub fn enumValue(r: Random, comptime EnumType: type) EnumType` |
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
| `weightedIndex` | `pub fn weightedIndex(r: std.rand.Random, comptime T: type, proportions: []const T) usize` |
| `limitRangeBiased` | `pub fn limitRangeBiased(comptime T: type, random_int: T, less_than: T) T` |
| `init` | `pub fn init(seed: u64) SplitMix64` |
| `next` | `pub fn next(self: *SplitMix64) u64` |

## rand / Gimli

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(secret_seed: [secret_seed_length]u8) Gimli` |
| `random` | `pub fn random(self: *Gimli) Random` |
| `fill` | `pub fn fill(self: *Gimli, buf: []u8) void` |

## rand / Isaac64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Isaac64` |
| `random` | `pub fn random(self: *Isaac64) Random` |
| `fill` | `pub fn fill(self: *Isaac64, buf: []u8) void` |

## rand / Pcg

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Pcg` |
| `random` | `pub fn random(self: *Pcg) Random` |
| `fill` | `pub fn fill(self: *Pcg, buf: []u8) void` |

## rand / RomuTrio

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) RomuTrio` |
| `random` | `pub fn random(self: *RomuTrio) Random` |
| `seedWithBuf` | `pub fn seedWithBuf(self: *RomuTrio, buf: [24]u8) void` |
| `seed` | `pub fn seed(self: *RomuTrio, init_s: u64) void` |
| `fill` | `pub fn fill(self: *RomuTrio, buf: []u8) void` |

## rand / Sfc64

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Sfc64` |
| `random` | `pub fn random(self: *Sfc64) Random` |
| `fill` | `pub fn fill(self: *Sfc64, buf: []u8) void` |

## rand / Xoodoo

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(secret_seed: [secret_seed_length]u8) Xoodoo` |
| `random` | `pub fn random(self: *Xoodoo) Random` |
| `fill` | `pub fn fill(self: *Xoodoo, buf: []u8) void` |

## rand / Xoroshiro128

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Xoroshiro128` |
| `random` | `pub fn random(self: *Xoroshiro128) Random` |
| `seed` | `pub fn seed(self: *Xoroshiro128, init_s: u64) void` |
| `fill` | `pub fn fill(self: *Xoroshiro128, buf: []u8) void` |

## rand / Xoshiro256

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(init_s: u64) Xoshiro256` |
| `random` | `pub fn random(self: *Xoshiro256) Random` |
| `seed` | `pub fn seed(self: *Xoshiro256, init_s: u64) void` |
| `fill` | `pub fn fill(self: *Xoshiro256, buf: []u8) void` |

## rand / ziggurat

| Function | Signature |
|----------|-----------|
| `next_f64` | `pub fn next_f64(random: Random, comptime tables: ZigTable) f64` |

## segmented_list

| Function | Signature |
|----------|-----------|
| `SegmentedList` | `pub fn SegmentedList(comptime T: type, comptime prealloc_item_count: usize) type` |
| `deinit` | `pub fn deinit(self: *Self, allocator: Allocator) void` |
| `at` | `pub fn at(self: anytype, i: usize) AtType(@TypeOf(self))` |
| `count` | `pub fn count(self: Self) usize` |
| `append` | `pub fn append(self: *Self, allocator: Allocator, item: T) Allocator.Error!void` |
| `appendSlice` | `pub fn appendSlice(self: *Self, allocator: Allocator, items: []const T) Allocator.Error!void` |
| `pop` | `pub fn pop(self: *Self) ?T` |
| `addOne` | `pub fn addOne(self: *Self, allocator: Allocator) Allocator.Error!*T` |
| `shrinkRetainingCapacity` | `pub fn shrinkRetainingCapacity(self: *Self, new_len: usize) void` |
| `clearRetainingCapacity` | `pub fn clearRetainingCapacity(self: *Self) void` |
| `clearAndFree` | `pub fn clearAndFree(self: *Self, allocator: Allocator) void` |
| `setCapacity` | `pub fn setCapacity(self: *Self, allocator: Allocator, new_capacity: usize) Allocator.Error!void` |
| `growCapacity` | `pub fn growCapacity(self: *Self, allocator: Allocator, new_capacity: usize) Allocator.Error!void` |
| `shrinkCapacity` | `pub fn shrinkCapacity(self: *Self, allocator: Allocator, new_capacity: usize) void` |
| `shrink` | `pub fn shrink(self: *Self, new_len: usize) void` |
| `writeToSlice` | `pub fn writeToSlice(self: *Self, dest: []T, start: usize) void` |
| `uncheckedAt` | `pub fn uncheckedAt(self: anytype, index: usize) AtType(@TypeOf(self))` |
| `next` | `pub fn next(it: *@This()) ?ElementPtr` |
| `prev` | `pub fn prev(it: *@This()) ?ElementPtr` |
| `peek` | `pub fn peek(it: *@This()) ?ElementPtr` |
| `set` | `pub fn set(it: *@This(), index: usize) void` |
| `iterator` | `pub fn iterator(self: *Self, start_index: usize) Iterator` |
| `constIterator` | `pub fn constIterator(self: *const Self, start_index: usize) ConstIterator` |

## SemanticVersion

| Function | Signature |
|----------|-----------|
| `includesVersion` | `pub fn includesVersion(self: Range, ver: Version) bool` |
| `isAtLeast` | `pub fn isAtLeast(self: Range, ver: Version) ?bool` |
| `order` | `pub fn order(lhs: Version, rhs: Version) std.math.Order` |
| `parse` | `pub fn parse(text: []const u8) !Version` |
| `format` | `pub fn format( self: Version, comptime fmt: []const u8, options: std.fmt.FormatOptions, out_stream: anytype, ) !void` |

## simd

| Function | Signature |
|----------|-----------|
| `suggestVectorSizeForCpu` | `pub fn suggestVectorSizeForCpu(comptime T: type, comptime cpu: std.Target.Cpu) ?usize` |
| `suggestVectorSize` | `pub fn suggestVectorSize(comptime T: type) ?usize` |
| `VectorIndex` | `pub fn VectorIndex(comptime VectorType: type) type` |
| `VectorCount` | `pub fn VectorCount(comptime VectorType: type) type` |
| `iota` | `pub fn iota(comptime T: type, comptime len: usize) @Vector(len, T)` |
| `repeat` | `pub fn repeat(comptime len: usize, vec: anytype) @Vector(len, std.meta.Child(@TypeOf(vec)))` |
| `join` | `pub fn join(a: anytype, b: anytype) @Vector(vectorLength(@TypeOf(a)) + vectorLength(@TypeOf(b)), std.meta.Child(@TypeOf(a)))` |
| `interlace` | `pub fn interlace(vecs: anytype) @Vector(vectorLength(@TypeOf(vecs[0])) * vecs.len, std.meta.Child(@TypeOf(vecs[0])))` |
| `deinterlace` | `pub fn deinterlace( comptime vec_count: usize, interlaced: anytype, ) [vec_count]@Vector( vectorLength(@TypeOf(interlaced)) / vec_count, std.meta.Child(@TypeOf(interlaced)), )` |
| `extract` | `pub fn extract( vec: anytype, comptime first: VectorIndex(@TypeOf(vec)), comptime count: VectorCount(@TypeOf(vec)), ) @Vector(count, std.meta.Child(@TypeOf(vec)))` |
| `mergeShift` | `pub fn mergeShift(a: anytype, b: anytype, comptime shift: VectorCount(@TypeOf(a, b))) @TypeOf(a, b)` |
| `shiftElementsRight` | `pub fn shiftElementsRight(vec: anytype, comptime amount: VectorCount(@TypeOf(vec)), shift_in: std.meta.Child(@TypeOf(vec))) @TypeOf(vec)` |
| `shiftElementsLeft` | `pub fn shiftElementsLeft(vec: anytype, comptime amount: VectorCount(@TypeOf(vec)), shift_in: std.meta.Child(@TypeOf(vec))) @TypeOf(vec)` |
| `rotateElementsLeft` | `pub fn rotateElementsLeft(vec: anytype, comptime amount: VectorCount(@TypeOf(vec))) @TypeOf(vec)` |
| `rotateElementsRight` | `pub fn rotateElementsRight(vec: anytype, comptime amount: VectorCount(@TypeOf(vec))) @TypeOf(vec)` |
| `reverseOrder` | `pub fn reverseOrder(vec: anytype) @TypeOf(vec)` |
| `firstTrue` | `pub fn firstTrue(vec: anytype) ?VectorIndex(@TypeOf(vec))` |
| `lastTrue` | `pub fn lastTrue(vec: anytype) ?VectorIndex(@TypeOf(vec))` |
| `countTrues` | `pub fn countTrues(vec: anytype) VectorCount(@TypeOf(vec))` |
| `firstIndexOfValue` | `pub fn firstIndexOfValue(vec: anytype, value: std.meta.Child(@TypeOf(vec))) ?VectorIndex(@TypeOf(vec))` |
| `lastIndexOfValue` | `pub fn lastIndexOfValue(vec: anytype, value: std.meta.Child(@TypeOf(vec))) ?VectorIndex(@TypeOf(vec))` |
| `countElementsWithValue` | `pub fn countElementsWithValue(vec: anytype, value: std.meta.Child(@TypeOf(vec))) VectorCount(@TypeOf(vec))` |
| `prefixScanWithFunc` | `pub fn prefixScanWithFunc( comptime hop: isize, vec: anytype, /// The error type that `func` might return. Set this to `void` if `func` doesn't return an error union. comptime ErrorType: type, comptime func: fn (@TypeOf(vec), @TypeOf(vec)) if (ErrorType == void) @TypeOf(vec) else ErrorType!@TypeOf(vec), /// When one operand of the operation performed by `func` is this value, the result must equal the other operand. /// For example, this should be 0 for addition or 1 for multiplication. comptime identity: std.meta.Child(@TypeOf(vec)), ) if (ErrorType == void) @TypeOf(vec) else ErrorType!@TypeOf(vec) { // I haven't debugged this, but it might be a cousin of sorts to what's going on with interlace. comptime if (builtin.cpu.arch.isMIPS()) @compileError("TODO: Find out why prefixScan doesn't work on MIPS"); const len = vectorLength(@TypeOf(vec)); if (hop == 0) @compileError("hop can not be 0; you'd be going nowhere forever!"); const abs_hop = if (hop < 0) -hop else hop; var acc = vec; comptime var i = 0; inline while ((abs_hop << i) < len) : (i += 1) { const shifted = if (hop < 0) shiftElementsLeft(acc, abs_hop << i, identity) else shiftElementsRight(acc, abs_hop << i, identity); acc = if (ErrorType == void) func(acc, shifted) else try func(acc, shifted); } return acc; } /// Returns a vector whose elements are the result of performing the specified operation on the corresponding /// element of the input vector and every hop'th element that came before it (or after, if hop is negative). /// Supports the same operations as the @reduce() builtin. Takes O(logN) to compute. /// The scan is not linear, which may affect floating point errors. This may affect the determinism of /// algorithms that use this function. pub fn prefixScan(comptime op: std.builtin.ReduceOp, comptime hop: isize, vec: anytype) @TypeOf(vec) { const VecType = @TypeOf(vec); const Child = std.meta.Child(VecType); const len = vectorLength(VecType); const identity = comptime switch (@typeInfo(Child)) { .Bool => switch (op) { .Or, .Xor => false, .And => true, else => @compileError("Invalid prefixScan operation " ++ @tagName(op) ++ " for vector of booleans."), }, .Int => switch (op) { .Max => std.math.minInt(Child), .Add, .Or, .Xor => 0, .Mul => 1, .And, .Min => std.math.maxInt(Child), }, .Float => switch (op) { .Max => -std.math.inf(Child), .Add => 0, .Mul => 1, .Min => std.math.inf(Child), else => @compileError("Invalid prefixScan operation " ++ @tagName(op) ++ " for vector of floats."), }, else => @compileError("Invalid type " ++ @typeName(VecType) ++ " for prefixScan."), }; const fn_container = struct { fn opFn(a: VecType, b: VecType) VecType { return if (Child == bool) switch (op) { .And => @select(bool, a, b, @splat(len, false)), .Or => @select(bool, a, @splat(len, true), b), .Xor => a != b, else => unreachable, } else switch (op) { .And => a & b, .Or => a | b, .Xor => a ^ b, .Add => a + b, .Mul => a * b, .Min => @min(a, b), .Max => @max(a, b), }; } }; return prefixScanWithFunc(hop, vec, void, fn_container.opFn, identity); } test "vector prefix scan" { if (comptime builtin.cpu.arch.isMIPS()) { return error.SkipZigTest; } if (builtin.zig_backend == .stage1 or builtin.zig_backend == .stage2_llvm) { // Regressed in LLVM 14: // https://github.com/llvm/llvm-project/issues/55522 return error.SkipZigTest; } const int_base = @Vector(4, i32){ 11, 23, 9, -21 }; const float_base = @Vector(4, f32){ 2, 0.5, -10, 6.54321 }; const bool_base = @Vector(4, bool){ true, false, true, false }; try std.testing.expectEqual(iota(u8, 32) + @splat(32, @as(u8, 1)), prefixScan(.Add, 1, @splat(32, @as(u8, 1)))); try std.testing.expectEqual(@Vector(4, i32){ 11, 3, 1, 1 }, prefixScan(.And, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 31, 31, -1 }, prefixScan(.Or, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 28, 21, -2 }, prefixScan(.Xor, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 34, 43, 22 }, prefixScan(.Add, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 253, 2277, -47817 }, prefixScan(.Mul, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 11, 9, -21 }, prefixScan(.Min, 1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 23, 23, 23 }, prefixScan(.Max, 1, int_base)); // Trying to predict all inaccuracies when adding and multiplying floats with prefixScans would be a mess, so we don't test those. try std.testing.expectEqual(@Vector(4, f32){ 2, 0.5, -10, -10 }, prefixScan(.Min, 1, float_base)); try std.testing.expectEqual(@Vector(4, f32){ 2, 2, 2, 6.54321 }, prefixScan(.Max, 1, float_base)); try std.testing.expectEqual(@Vector(4, bool){ true, true, false, false }, prefixScan(.Xor, 1, bool_base)); try std.testing.expectEqual(@Vector(4, bool){ true, true, true, true }, prefixScan(.Or, 1, bool_base)); try std.testing.expectEqual(@Vector(4, bool){ true, false, false, false }, prefixScan(.And, 1, bool_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 23, 20, 2 }, prefixScan(.Add, 2, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 22, 11, -12, -21 }, prefixScan(.Add, -1, int_base)); try std.testing.expectEqual(@Vector(4, i32){ 11, 23, 9, -10 }, prefixScan(.Add, 3, int_base)); }` |

## sort

| Function | Signature |
|----------|-----------|
| `binarySearch` | `pub fn binarySearch( comptime T: type, key: T, items: []const T, context: anytype, comptime compareFn: fn (context: @TypeOf(context), lhs: T, rhs: T) math.Order, ) ?usize` |
| `insertionSort` | `pub fn insertionSort( comptime T: type, items: []T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) void` |
| `insertionSortContext` | `pub fn insertionSortContext(len: usize, context: anytype) void` |
| `sort` | `pub fn sort( comptime T: type, items: []T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) void` |
| `sortContext` | `pub fn sortContext(len: usize, context: anytype) void` |
| `asc` | `pub fn asc(comptime T: type) fn (void, T, T) bool` |
| `desc` | `pub fn desc(comptime T: type) fn (void, T, T) bool` |
| `argMin` | `pub fn argMin( comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (@TypeOf(context), lhs: T, rhs: T) bool, ) ?usize` |
| `min` | `pub fn min( comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) ?T` |
| `argMax` | `pub fn argMax( comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) ?usize` |
| `max` | `pub fn max( comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) ?T` |
| `isSorted` | `pub fn isSorted( comptime T: type, items: []const T, context: anytype, comptime lessThan: fn (context: @TypeOf(context), lhs: T, rhs: T) bool, ) bool` |

## start

| Function | Signature |
|----------|-----------|
| `callMain` | `pub fn callMain() u8` |
| `call_wWinMain` | `pub fn call_wWinMain() std.os.windows.INT` |

## target

| Function | Signature |
|----------|-----------|
| `isDarwin` | `pub fn isDarwin(tag: Tag) bool` |
| `isBSD` | `pub fn isBSD(tag: Tag) bool` |
| `dynamicLibSuffix` | `pub fn dynamicLibSuffix(tag: Tag) [:0]const u8` |
| `defaultVersionRange` | `pub fn defaultVersionRange(tag: Tag, arch: Cpu.Arch) Os` |
| `isAtLeast` | `pub fn isAtLeast(self: WindowsVersion, ver: WindowsVersion) bool` |
| `includesVersion` | `pub fn includesVersion(self: Range, ver: WindowsVersion) bool` |
| `isAtLeast` | `pub fn isAtLeast(self: Range, ver: WindowsVersion) ?bool` |
| `format` | `pub fn format( self: WindowsVersion, comptime fmt: []const u8, _: std.fmt.FormatOptions, out_stream: anytype, ) !void` |
| `includesVersion` | `pub fn includesVersion(self: LinuxVersionRange, ver: Version) bool` |
| `isAtLeast` | `pub fn isAtLeast(self: LinuxVersionRange, ver: Version) ?bool` |
| `default` | `pub fn default(tag: Tag, arch: Cpu.Arch) VersionRange` |
| `getVersionRange` | `pub fn getVersionRange(self: Os) TaggedVersionRange` |
| `isAtLeast` | `pub fn isAtLeast(self: Os, comptime tag: Tag, version: anytype) ?bool` |
| `requiresLibC` | `pub fn requiresLibC(os: Os) bool` |
| `default` | `pub fn default(arch: Cpu.Arch, target_os: Os) Abi` |
| `isGnu` | `pub fn isGnu(abi: Abi) bool` |
| `isMusl` | `pub fn isMusl(abi: Abi) bool` |
| `floatAbi` | `pub fn floatAbi(abi: Abi) FloatAbi` |
| `fileExt` | `pub fn fileExt(of: ObjectFormat, cpu_arch: Cpu.Arch) [:0]const u8` |
| `default` | `pub fn default(os_tag: Os.Tag, cpu_arch: Cpu.Arch) ObjectFormat` |
| `empty_workaround` | `pub fn empty_workaround() Set` |
| `isEmpty` | `pub fn isEmpty(set: Set) bool` |
| `isEnabled` | `pub fn isEnabled(set: Set, arch_feature_index: Index) bool` |
| `addFeature` | `pub fn addFeature(set: *Set, arch_feature_index: Index) void` |
| `addFeatureSet` | `pub fn addFeatureSet(set: *Set, other_set: Set) void` |
| `removeFeature` | `pub fn removeFeature(set: *Set, arch_feature_index: Index) void` |
| `removeFeatureSet` | `pub fn removeFeatureSet(set: *Set, other_set: Set) void` |
| `populateDependencies` | `pub fn populateDependencies(set: *Set, all_features_list: []const Cpu.Feature) void` |
| `asBytes` | `pub fn asBytes(set: *const Set) *const [byte_count]u8` |
| `eql` | `pub fn eql(set: Set, other_set: Set) bool` |
| `isSuperSetOf` | `pub fn isSuperSetOf(set: Set, other_set: Set) bool` |
| `feature_set_fns` | `pub fn feature_set_fns(comptime F: type) type` |
| `featureSet` | `pub fn featureSet(features: []const F) Set` |
| `featureSetHas` | `pub fn featureSetHas(set: Set, feature: F) bool` |
| `featureSetHasAny` | `pub fn featureSetHasAny(set: Set, features: anytype) bool` |
| `featureSetHasAll` | `pub fn featureSetHasAll(set: Set, features: anytype) bool` |
| `isX86` | `pub fn isX86(arch: Arch) bool` |
| `isARM` | `pub fn isARM(arch: Arch) bool` |
| `isAARCH64` | `pub fn isAARCH64(arch: Arch) bool` |
| `isThumb` | `pub fn isThumb(arch: Arch) bool` |
| `isWasm` | `pub fn isWasm(arch: Arch) bool` |
| `isRISCV` | `pub fn isRISCV(arch: Arch) bool` |
| `isMIPS` | `pub fn isMIPS(arch: Arch) bool` |
| `isPPC` | `pub fn isPPC(arch: Arch) bool` |
| `isPPC64` | `pub fn isPPC64(arch: Arch) bool` |
| `isSPARC` | `pub fn isSPARC(arch: Arch) bool` |
| `isSPIRV` | `pub fn isSPIRV(arch: Arch) bool` |
| `isBpf` | `pub fn isBpf(arch: Arch) bool` |
| `isNvptx` | `pub fn isNvptx(arch: Arch) bool` |
| `parseCpuModel` | `pub fn parseCpuModel(arch: Arch, cpu_name: []const u8) !*const Cpu.Model` |
| `toElfMachine` | `pub fn toElfMachine(arch: Arch) std.elf.EM` |
| `toCoffMachine` | `pub fn toCoffMachine(arch: Arch) std.coff.MachineType` |
| `endian` | `pub fn endian(arch: Arch) std.builtin.Endian` |
| `supportsAddressSpace` | `pub fn supportsAddressSpace(arch: Arch, address_space: std.builtin.AddressSpace) bool` |
| `ptrBitWidth` | `pub fn ptrBitWidth(arch: Arch) u16` |
| `genericName` | `pub fn genericName(arch: Arch) []const u8` |
| `allFeaturesList` | `pub fn allFeaturesList(arch: Arch) []const Cpu.Feature` |
| `allCpuModels` | `pub fn allCpuModels(arch: Arch) []const *const Cpu.Model` |
| `toCpu` | `pub fn toCpu(model: *const Model, arch: Arch) Cpu` |
| `generic` | `pub fn generic(arch: Arch) *const Model` |
| `baseline` | `pub fn baseline(arch: Arch) *const Model` |
| `baseline` | `pub fn baseline(arch: Arch) Cpu` |
| `zigTriple` | `pub fn zigTriple(self: Target, allocator: mem.Allocator) ![]u8` |
| `linuxTripleSimple` | `pub fn linuxTripleSimple(allocator: mem.Allocator, cpu_arch: Cpu.Arch, os_tag: Os.Tag, abi: Abi) ![]u8` |
| `linuxTriple` | `pub fn linuxTriple(self: Target, allocator: mem.Allocator) ![]u8` |
| `exeFileExtSimple` | `pub fn exeFileExtSimple(cpu_arch: Cpu.Arch, os_tag: Os.Tag) [:0]const u8` |
| `exeFileExt` | `pub fn exeFileExt(self: Target) [:0]const u8` |
| `staticLibSuffix_os_abi` | `pub fn staticLibSuffix_os_abi(os_tag: Os.Tag, abi: Abi) [:0]const u8` |
| `staticLibSuffix` | `pub fn staticLibSuffix(self: Target) [:0]const u8` |
| `dynamicLibSuffix` | `pub fn dynamicLibSuffix(self: Target) [:0]const u8` |
| `libPrefix_os_abi` | `pub fn libPrefix_os_abi(os_tag: Os.Tag, abi: Abi) [:0]const u8` |
| `libPrefix` | `pub fn libPrefix(self: Target) [:0]const u8` |
| `isMinGW` | `pub fn isMinGW(self: Target) bool` |
| `isGnu` | `pub fn isGnu(self: Target) bool` |
| `isMusl` | `pub fn isMusl(self: Target) bool` |
| `isAndroid` | `pub fn isAndroid(self: Target) bool` |
| `isWasm` | `pub fn isWasm(self: Target) bool` |
| `isDarwin` | `pub fn isDarwin(self: Target) bool` |
| `isBSD` | `pub fn isBSD(self: Target) bool` |
| `isBpfFreestanding` | `pub fn isBpfFreestanding(self: Target) bool` |
| `isGnuLibC_os_tag_abi` | `pub fn isGnuLibC_os_tag_abi(os_tag: Os.Tag, abi: Abi) bool` |
| `isGnuLibC` | `pub fn isGnuLibC(self: Target) bool` |
| `supportsNewStackCall` | `pub fn supportsNewStackCall(self: Target) bool` |
| `getFloatAbi` | `pub fn getFloatAbi(self: Target) FloatAbi` |
| `hasDynamicLinker` | `pub fn hasDynamicLinker(self: Target) bool` |
| `init` | `pub fn init(dl_or_null: ?[]const u8) DynamicLinker` |
| `get` | `pub fn get(self: *const DynamicLinker) ?[]const u8` |
| `set` | `pub fn set(self: *DynamicLinker, dl_or_null: ?[]const u8) void` |
| `standardDynamicLinkerPath` | `pub fn standardDynamicLinkerPath(self: Target) DynamicLinker` |
| `plan9Ext` | `pub fn plan9Ext(cpu_arch: Cpu.Arch) [:0]const u8` |
| `maxIntAlignment` | `pub inline fn maxIntAlignment(target: Target) u16` |

## testing

| Function | Signature |
|----------|-----------|
| `expectError` | `pub fn expectError(expected_error: anyerror, actual_error_union: anytype) !void` |
| `expectEqual` | `pub fn expectEqual(expected: anytype, actual: @TypeOf(expected)) !void` |
| `expectFmt` | `pub fn expectFmt(expected: []const u8, comptime template: []const u8, args: anytype) !void` |
| `expectApproxEqAbs` | `pub fn expectApproxEqAbs(expected: anytype, actual: @TypeOf(expected), tolerance: @TypeOf(expected)) !void` |
| `expectApproxEqRel` | `pub fn expectApproxEqRel(expected: anytype, actual: @TypeOf(expected), tolerance: @TypeOf(expected)) !void` |
| `expectEqualSlices` | `pub fn expectEqualSlices(comptime T: type, expected: []const T, actual: []const T) !void` |
| `expectEqualSentinel` | `pub fn expectEqualSentinel(comptime T: type, comptime sentinel: T, expected: [:sentinel]const T, actual: [:sentinel]const T) !void` |
| `expect` | `pub fn expect(ok: bool) !void` |
| `cleanup` | `pub fn cleanup(self: *TmpDir) void` |
| `cleanup` | `pub fn cleanup(self: *TmpIterableDir) void` |
| `tmpDir` | `pub fn tmpDir(opts: std.fs.Dir.OpenDirOptions) TmpDir` |
| `tmpIterableDir` | `pub fn tmpIterableDir(opts: std.fs.Dir.OpenDirOptions) TmpIterableDir` |
| `expectEqualStrings` | `pub fn expectEqualStrings(expected: []const u8, actual: []const u8) !void` |
| `expectStringStartsWith` | `pub fn expectStringStartsWith(actual: []const u8, expected_starts_with: []const u8) !void` |
| `expectStringEndsWith` | `pub fn expectStringEndsWith(actual: []const u8, expected_ends_with: []const u8) !void` |
| `checkAllAllocationFailures` | `pub fn checkAllAllocationFailures(backing_allocator: std.mem.Allocator, comptime test_fn: anytype, extra_args: anytype) !void` |
| `refAllDecls` | `pub fn refAllDecls(comptime T: type) void` |
| `refAllDeclsRecursive` | `pub fn refAllDeclsRecursive(comptime T: type) void` |

## testing / failing_allocator

| Function | Signature |
|----------|-----------|
| `init` | `pub fn init(internal_allocator: mem.Allocator, fail_index: usize) FailingAllocator` |
| `allocator` | `pub fn allocator(self: *FailingAllocator) mem.Allocator` |
| `getStackTrace` | `pub fn getStackTrace(self: *FailingAllocator) std.builtin.StackTrace` |

## Thread

| Function | Signature |
|----------|-----------|
| `setName` | `pub fn setName(self: Thread, name: []const u8) SetNameError!void` |
| `getName` | `pub fn getName(self: Thread, buffer_ptr: *[max_name_len:0]u8) GetNameError!?[]const u8` |
| `getCurrentId` | `pub fn getCurrentId() Id` |
| `getCpuCount` | `pub fn getCpuCount() CpuCountError!usize` |
| `spawn` | `pub fn spawn(config: SpawnConfig, comptime function: anytype, args: anytype) SpawnError!Thread` |
| `getHandle` | `pub fn getHandle(self: Thread) Handle` |
| `detach` | `pub fn detach(self: Thread) void` |
| `join` | `pub fn join(self: Thread) void` |
| `yield` | `pub fn yield() YieldError!void` |
| `run` | `pub fn run(ctx: *@This()) !void` |

## Thread / Condition

| Function | Signature |
|----------|-----------|
| `wait` | `pub fn wait(self: *Condition, mutex: *Mutex) void` |
| `timedWait` | `pub fn timedWait(self: *Condition, mutex: *Mutex, timeout_ns: u64) error` |
| `signal` | `pub fn signal(self: *Condition) void` |
| `broadcast` | `pub fn broadcast(self: *Condition) void` |

## Thread / Futex

| Function | Signature |
|----------|-----------|
| `wait` | `pub fn wait(ptr: *const Atomic(u32), expect: u32) void` |
| `timedWait` | `pub fn timedWait(ptr: *const Atomic(u32), expect: u32, timeout_ns: u64) error` |
| `wake` | `pub fn wake(ptr: *const Atomic(u32), max_waiters: u32) void` |
| `init` | `pub fn init(expires_in_ns: ?u64) Deadline` |
| `wait` | `pub fn wait(self: *Deadline, ptr: *const Atomic(u32), expect: u32) error` |

## Thread / Mutex

| Function | Signature |
|----------|-----------|
| `tryLock` | `pub fn tryLock(self: *Mutex) bool` |
| `lock` | `pub fn lock(self: *Mutex) void` |
| `unlock` | `pub fn unlock(self: *Mutex) void` |

## Thread / ResetEvent

| Function | Signature |
|----------|-----------|
| `isSet` | `pub fn isSet(self: *const ResetEvent) bool` |
| `wait` | `pub fn wait(self: *ResetEvent) void` |
| `timedWait` | `pub fn timedWait(self: *ResetEvent, timeout_ns: u64) error` |
| `set` | `pub fn set(self: *ResetEvent) void` |
| `reset` | `pub fn reset(self: *ResetEvent) void` |

## Thread / RwLock

| Function | Signature |
|----------|-----------|
| `tryLock` | `pub fn tryLock(rwl: *RwLock) bool` |
| `lock` | `pub fn lock(rwl: *RwLock) void` |
| `unlock` | `pub fn unlock(rwl: *RwLock) void` |
| `tryLockShared` | `pub fn tryLockShared(rwl: *RwLock) bool` |
| `lockShared` | `pub fn lockShared(rwl: *RwLock) void` |
| `unlockShared` | `pub fn unlockShared(rwl: *RwLock) void` |
| `tryLock` | `pub fn tryLock(rwl: *SingleThreadedRwLock) bool` |
| `lock` | `pub fn lock(rwl: *SingleThreadedRwLock) void` |
| `unlock` | `pub fn unlock(rwl: *SingleThreadedRwLock) void` |
| `tryLockShared` | `pub fn tryLockShared(rwl: *SingleThreadedRwLock) bool` |
| `lockShared` | `pub fn lockShared(rwl: *SingleThreadedRwLock) void` |
| `unlockShared` | `pub fn unlockShared(rwl: *SingleThreadedRwLock) void` |
| `tryLock` | `pub fn tryLock(rwl: *PthreadRwLock) bool` |
| `lock` | `pub fn lock(rwl: *PthreadRwLock) void` |
| `unlock` | `pub fn unlock(rwl: *PthreadRwLock) void` |
| `tryLockShared` | `pub fn tryLockShared(rwl: *PthreadRwLock) bool` |
| `lockShared` | `pub fn lockShared(rwl: *PthreadRwLock) void` |
| `unlockShared` | `pub fn unlockShared(rwl: *PthreadRwLock) void` |
| `tryLock` | `pub fn tryLock(rwl: *DefaultRwLock) bool` |
| `lock` | `pub fn lock(rwl: *DefaultRwLock) void` |
| `unlock` | `pub fn unlock(rwl: *DefaultRwLock) void` |
| `tryLockShared` | `pub fn tryLockShared(rwl: *DefaultRwLock) bool` |
| `lockShared` | `pub fn lockShared(rwl: *DefaultRwLock) void` |
| `unlockShared` | `pub fn unlockShared(rwl: *DefaultRwLock) void` |

## Thread / Semaphore

| Function | Signature |
|----------|-----------|
| `wait` | `pub fn wait(sem: *Semaphore) void` |
| `post` | `pub fn post(sem: *Semaphore) void` |

## time

| Function | Signature |
|----------|-----------|
| `sleep` | `pub fn sleep(nanoseconds: u64) void` |
| `timestamp` | `pub fn timestamp() i64` |
| `milliTimestamp` | `pub fn milliTimestamp() i64` |
| `nanoTimestamp` | `pub fn nanoTimestamp() i128` |
| `now` | `pub fn now() error` |
| `order` | `pub fn order(self: Instant, other: Instant) std.math.Order` |
| `since` | `pub fn since(self: Instant, earlier: Instant) u64` |
| `start` | `pub fn start() Error!Timer` |
| `read` | `pub fn read(self: *Timer) u64` |
| `reset` | `pub fn reset(self: *Timer) void` |
| `lap` | `pub fn lap(self: *Timer) u64` |

## time / epoch

| Function | Signature |
|----------|-----------|
| `isLeapYear` | `pub fn isLeapYear(year: Year) bool` |
| `getDaysInYear` | `pub fn getDaysInYear(year: Year) u9` |
| `numeric` | `pub fn numeric(self: Month) u4` |
| `getDaysInMonth` | `pub fn getDaysInMonth(leap_year: YearLeapKind, month: Month) u5` |
| `calculateMonthDay` | `pub fn calculateMonthDay(self: YearAndDay) MonthAndDay` |
| `calculateYearDay` | `pub fn calculateYearDay(self: EpochDay) YearAndDay` |
| `getHoursIntoDay` | `pub fn getHoursIntoDay(self: DaySeconds) u5` |
| `getMinutesIntoHour` | `pub fn getMinutesIntoHour(self: DaySeconds) u6` |
| `getSecondsIntoMinute` | `pub fn getSecondsIntoMinute(self: DaySeconds) u6` |
| `getEpochDay` | `pub fn getEpochDay(self: EpochSeconds) EpochDay` |
| `getDaySeconds` | `pub fn getDaySeconds(self: EpochSeconds) DaySeconds` |

## treap

| Function | Signature |
|----------|-----------|
| `Treap` | `pub fn Treap(comptime Key: type, comptime compareFn: anytype) type` |
| `getMin` | `pub fn getMin(self: Self) ?*Node` |
| `getMax` | `pub fn getMax(self: Self) ?*Node` |
| `getEntryFor` | `pub fn getEntryFor(self: *Self, key: Key) Entry` |
| `getEntryForExisting` | `pub fn getEntryForExisting(self: *Self, node: *Node) Entry` |
| `set` | `pub fn set(self: *Entry, new_node: ?*Node) void` |
| `init` | `pub fn init(slice: []T, rng: std.rand.Random) Self` |
| `reset` | `pub fn reset(self: *Self) void` |
| `next` | `pub fn next(self: *Self) ?*T` |

## tz

| Function | Signature |
|----------|-----------|
| `name` | `pub fn name(self: *const Timetype) [:0]const u8` |
| `isDst` | `pub fn isDst(self: Timetype) bool` |
| `standardTimeIndicator` | `pub fn standardTimeIndicator(self: Timetype) bool` |
| `utIndicator` | `pub fn utIndicator(self: Timetype) bool` |
| `parse` | `pub fn parse(allocator: std.mem.Allocator, reader: anytype) !Tz` |
| `deinit` | `pub fn deinit(self: *Tz) void` |

## unicode

| Function | Signature |
|----------|-----------|
| `utf8CodepointSequenceLength` | `pub fn utf8CodepointSequenceLength(c: u21) !u3` |
| `utf8ByteSequenceLength` | `pub fn utf8ByteSequenceLength(first_byte: u8) !u3` |
| `utf8Encode` | `pub fn utf8Encode(c: u21, out: []u8) !u3` |
| `utf8Decode` | `pub fn utf8Decode(bytes: []const u8) Utf8DecodeError!u21` |
| `utf8Decode2` | `pub fn utf8Decode2(bytes: []const u8) Utf8Decode2Error!u21` |
| `utf8Decode3` | `pub fn utf8Decode3(bytes: []const u8) Utf8Decode3Error!u21` |
| `utf8Decode4` | `pub fn utf8Decode4(bytes: []const u8) Utf8Decode4Error!u21` |
| `utf8ValidCodepoint` | `pub fn utf8ValidCodepoint(value: u21) bool` |
| `utf8CountCodepoints` | `pub fn utf8CountCodepoints(s: []const u8) !usize` |
| `utf8ValidateSlice` | `pub fn utf8ValidateSlice(s: []const u8) bool` |
| `init` | `pub fn init(s: []const u8) !Utf8View` |
| `initUnchecked` | `pub fn initUnchecked(s: []const u8) Utf8View` |
| `initComptime` | `pub fn initComptime(comptime s: []const u8) Utf8View` |
| `iterator` | `pub fn iterator(s: Utf8View) Utf8Iterator` |
| `nextCodepointSlice` | `pub fn nextCodepointSlice(it: *Utf8Iterator) ?[]const u8` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Utf8Iterator) ?u21` |
| `peek` | `pub fn peek(it: *Utf8Iterator, n: usize) []const u8` |
| `init` | `pub fn init(s: []const u16) Utf16LeIterator` |
| `nextCodepoint` | `pub fn nextCodepoint(it: *Utf16LeIterator) !?u21` |
| `utf16CountCodepoints` | `pub fn utf16CountCodepoints(utf16le: []const u16) !usize` |
| `utf16leToUtf8Alloc` | `pub fn utf16leToUtf8Alloc(allocator: mem.Allocator, utf16le: []const u16) ![]u8` |
| `utf16leToUtf8AllocZ` | `pub fn utf16leToUtf8AllocZ(allocator: mem.Allocator, utf16le: []const u16) ![:0]u8` |
| `utf16leToUtf8` | `pub fn utf16leToUtf8(utf8: []u8, utf16le: []const u16) !usize` |
| `utf8ToUtf16LeWithNull` | `pub fn utf8ToUtf16LeWithNull(allocator: mem.Allocator, utf8: []const u8) ![:0]u16` |
| `utf8ToUtf16Le` | `pub fn utf8ToUtf16Le(utf16le: []u16, utf8: []const u8) !usize` |
| `utf8ToUtf16LeStringLiteral` | `pub fn utf8ToUtf16LeStringLiteral(comptime utf8: []const u8) *const [calcUtf16LeLen(utf8) catch unreachable:0]u16` |
| `calcUtf16LeLen` | `pub fn calcUtf16LeLen(utf8: []const u8) CalcUtf16LeLenError!usize` |
| `fmtUtf16le` | `pub fn fmtUtf16le(utf16le: []const u16) std.fmt.Formatter(formatUtf16le)` |

## valgrind

| Function | Signature |
|----------|-----------|
| `doClientRequest` | `pub fn doClientRequest(default: usize, request: usize, a1: usize, a2: usize, a3: usize, a4: usize, a5: usize) usize` |
| `ToolBase` | `pub fn ToolBase(base: [2]u8) u32` |
| `IsTool` | `pub fn IsTool(base: [2]u8, code: usize) bool` |
| `runningOnValgrind` | `pub fn runningOnValgrind() usize` |
| `discardTranslations` | `pub fn discardTranslations(qzz: []const u8) void` |
| `innerThreads` | `pub fn innerThreads(qzz: [*]u8) void` |
| `nonSIMDCall0` | `pub fn nonSIMDCall0(func: fn (usize) usize) usize` |
| `nonSIMDCall1` | `pub fn nonSIMDCall1(func: fn (usize, usize) usize, a1: usize) usize` |
| `nonSIMDCall2` | `pub fn nonSIMDCall2(func: fn (usize, usize, usize) usize, a1: usize, a2: usize) usize` |
| `nonSIMDCall3` | `pub fn nonSIMDCall3(func: fn (usize, usize, usize, usize) usize, a1: usize, a2: usize, a3: usize) usize` |
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

## valgrind / callgrind

| Function | Signature |
|----------|-----------|
| `dumpStats` | `pub fn dumpStats() void` |
| `dumpStatsAt` | `pub fn dumpStatsAt(pos_str: [*]u8) void` |
| `zeroStats` | `pub fn zeroStats() void` |
| `toggleCollect` | `pub fn toggleCollect() void` |
| `startInstrumentation` | `pub fn startInstrumentation() void` |
| `stopInstrumentation` | `pub fn stopInstrumentation() void` |

## valgrind / memcheck

| Function | Signature |
|----------|-----------|
| `makeMemNoAccess` | `pub fn makeMemNoAccess(qzz: []u8) i1` |
| `makeMemUndefined` | `pub fn makeMemUndefined(qzz: []u8) i1` |
| `makeMemDefined` | `pub fn makeMemDefined(qzz: []u8) i1` |
| `makeMemDefinedIfAddressable` | `pub fn makeMemDefinedIfAddressable(qzz: []u8) i1` |
| `createBlock` | `pub fn createBlock(qzz: []u8, desc: [*]u8) usize` |
| `discard` | `pub fn discard(blkindex: usize) bool` |
| `checkMemIsAddressable` | `pub fn checkMemIsAddressable(qzz: []u8) usize` |
| `checkMemIsDefined` | `pub fn checkMemIsDefined(qzz: []u8) usize` |
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

## wasm

| Function | Signature |
|----------|-----------|
| `opcode` | `pub fn opcode(op: Opcode) u8` |
| `valtype` | `pub fn valtype(value: Valtype) u8` |
| `reftype` | `pub fn reftype(value: RefType) u8` |
| `format` | `pub fn format(self: Type, comptime fmt: []const u8, opt: std.fmt.FormatOptions, writer: anytype) !void` |
| `eql` | `pub fn eql(self: Type, other: Type) bool` |
| `deinit` | `pub fn deinit(self: *Type, gpa: std.mem.Allocator) void` |
| `section` | `pub fn section(val: Section) u8` |
| `externalKind` | `pub fn externalKind(val: ExternalKind) u8` |

## x / net / bpf

| Function | Signature |
|----------|-----------|
| `format` | `pub fn format( self: Insn, comptime layout: []const u8, opts: std.fmt.FormatOptions, writer: anytype, ) !void` |
| `ld_imm` | `pub fn ld_imm(value: u32) Insn` |
| `ld_abs` | `pub fn ld_abs(size: Size, offset: u32) Insn` |
| `ld_ind` | `pub fn ld_ind(size: Size, offset: u32) Insn` |
| `ld_mem` | `pub fn ld_mem(reg: Scratch) Insn` |
| `ld_len` | `pub fn ld_len() Insn` |
| `ld_rnd` | `pub fn ld_rnd() Insn` |
| `ldx_imm` | `pub fn ldx_imm(value: u32) Insn` |
| `ldx_mem` | `pub fn ldx_mem(reg: Scratch) Insn` |
| `ldx_len` | `pub fn ldx_len() Insn` |
| `ldx_msh` | `pub fn ldx_msh(offset: u32) Insn` |
| `st` | `pub fn st(reg: Scratch) Insn` |
| `stx` | `pub fn stx(reg: Scratch) Insn` |
| `alu_neg` | `pub fn alu_neg() Insn` |
| `alu` | `pub fn alu(op: AluOp, source: KOrX) Insn` |
| `jmp_ja` | `pub fn jmp_ja(location: u32) Insn` |
| `jmp` | `pub fn jmp(op: JmpOp, source: KOrX, jt: u8, jf: u8) Insn` |
| `ret` | `pub fn ret(verdict: KOrA) Insn` |
| `tax` | `pub fn tax() Insn` |
| `txa` | `pub fn txa() Insn` |
| `simulate` | `pub fn simulate( packet: []const u8, filter: []const Insn, byte_order: std.builtin.Endian, ) Error!u32` |

## x / net / ip

| Function | Signature |
|----------|-----------|
| `initIPv4` | `pub fn initIPv4(host: IPv4, port: u16) Address` |
| `initIPv6` | `pub fn initIPv6(host: IPv6, port: u16) Address` |
| `from` | `pub fn from(address: Socket.Address) ip.Address` |
| `into` | `pub fn into(self: ip.Address) Socket.Address` |
| `format` | `pub fn format( self: ip.Address, comptime layout: []const u8, opts: fmt.FormatOptions, writer: anytype, ) !void` |

## x / net / tcp

| Function | Signature |
|----------|-----------|
| `from` | `pub fn from(conn: Socket.Connection) tcp.Connection` |
| `into` | `pub fn into(self: tcp.Connection) Socket.Connection` |
| `deinit` | `pub fn deinit(self: tcp.Connection) void` |
| `read` | `pub fn read(self: Client.Reader, buffer: []u8) !usize` |
| `write` | `pub fn write(self: Client.Writer, buffer: []const u8) !usize` |
| `init` | `pub fn init(domain: tcp.Domain, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Client` |
| `from` | `pub fn from(socket: Socket) Client` |
| `deinit` | `pub fn deinit(self: Client) void` |
| `shutdown` | `pub fn shutdown(self: Client, how: os.ShutdownHow) !void` |
| `connect` | `pub fn connect(self: Client, address: ip.Address) !void` |
| `reader` | `pub fn reader(self: Client, flags: u32) io.Reader(Client.Reader, ErrorSetOf(Client.Reader.read), Client.Reader.read)` |
| `writer` | `pub fn writer(self: Client, flags: u32) io.Writer(Client.Writer, ErrorSetOf(Client.Writer.write), Client.Writer.write)` |
| `read` | `pub fn read(self: Client, buf: []u8, flags: u32) !usize` |
| `write` | `pub fn write(self: Client, buf: []const u8, flags: u32) !usize` |
| `writeMessage` | `pub fn writeMessage(self: Client, msg: Socket.Message, flags: u32) !usize` |
| `readMessage` | `pub fn readMessage(self: Client, msg: *Socket.Message, flags: u32) !usize` |
| `getError` | `pub fn getError(self: Client) !void` |
| `getReadBufferSize` | `pub fn getReadBufferSize(self: Client) !u32` |
| `getWriteBufferSize` | `pub fn getWriteBufferSize(self: Client) !u32` |
| `getLocalAddress` | `pub fn getLocalAddress(self: Client) !ip.Address` |
| `getRemoteAddress` | `pub fn getRemoteAddress(self: Client) !ip.Address` |
| `setLinger` | `pub fn setLinger(self: Client, timeout_seconds: ?u16) !void` |
| `setKeepAlive` | `pub fn setKeepAlive(self: Client, enabled: bool) !void` |
| `setNoDelay` | `pub fn setNoDelay(self: Client, enabled: bool) !void` |
| `setQuickACK` | `pub fn setQuickACK(self: Client, enabled: bool) !void` |
| `setWriteBufferSize` | `pub fn setWriteBufferSize(self: Client, size: u32) !void` |
| `setReadBufferSize` | `pub fn setReadBufferSize(self: Client, size: u32) !void` |
| `setWriteTimeout` | `pub fn setWriteTimeout(self: Client, milliseconds: u32) !void` |
| `setReadTimeout` | `pub fn setReadTimeout(self: Client, milliseconds: u32) !void` |
| `init` | `pub fn init(domain: tcp.Domain, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Listener` |
| `deinit` | `pub fn deinit(self: Listener) void` |
| `shutdown` | `pub fn shutdown(self: Listener) !void` |
| `bind` | `pub fn bind(self: Listener, address: ip.Address) !void` |
| `listen` | `pub fn listen(self: Listener, max_backlog_size: u31) !void` |
| `accept` | `pub fn accept(self: Listener, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !tcp.Connection` |
| `getError` | `pub fn getError(self: Client) !void` |
| `getLocalAddress` | `pub fn getLocalAddress(self: Listener) !ip.Address` |
| `setReuseAddress` | `pub fn setReuseAddress(self: Listener, enabled: bool) !void` |
| `setReusePort` | `pub fn setReusePort(self: Listener, enabled: bool) !void` |
| `setFastOpen` | `pub fn setFastOpen(self: Listener, enabled: bool) !void` |
| `setAcceptTimeout` | `pub fn setAcceptTimeout(self: Listener, milliseconds: usize) !void` |

## x / os / io

| Function | Signature |
|----------|-----------|
| `from` | `pub fn from(slice: []const u8) Buffer` |
| `into` | `pub fn into(self: Buffer) []const u8` |
| `intoMutable` | `pub fn intoMutable(self: Buffer) []u8` |
| `from` | `pub fn from(slice: []const u8) Buffer` |
| `into` | `pub fn into(self: Buffer) []const u8` |
| `intoMutable` | `pub fn intoMutable(self: Buffer) []u8` |
| `init` | `pub fn init(flags: std.enums.EnumFieldStruct(Reactor.InitFlags, bool, false)) !Reactor` |
| `deinit` | `pub fn deinit(self: Reactor) void` |
| `update` | `pub fn update(self: Reactor, fd: os.fd_t, identifier: usize, interest: Reactor.Interest) !void` |
| `poll` | `pub fn poll(self: Reactor, comptime max_num_events: comptime_int, closure: anytype, timeout_milliseconds: ?u64) !void` |

## x / os / net

| Function | Signature |
|----------|-----------|
| `resolveScopeId` | `pub fn resolveScopeId(name: []const u8) ResolveScopeIdError!u32` |
| `cmp` | `pub fn cmp(self: IPv4, other: IPv4) math.Order` |
| `eql` | `pub fn eql(self: IPv4, other: IPv4) bool` |
| `isLoopback` | `pub fn isLoopback(self: IPv4) bool` |
| `isUnspecified` | `pub fn isUnspecified(self: IPv4) bool` |
| `isPrivate` | `pub fn isPrivate(self: IPv4) bool` |
| `isLinkLocal` | `pub fn isLinkLocal(self: IPv4) bool` |
| `isMulticast` | `pub fn isMulticast(self: IPv4) bool` |
| `isBroadcast` | `pub fn isBroadcast(self: IPv4) bool` |
| `isDocumentation` | `pub fn isDocumentation(self: IPv4) bool` |
| `format` | `pub fn format( self: IPv4, comptime layout: []const u8, opts: fmt.FormatOptions, writer: anytype, ) !void` |
| `parse` | `pub fn parse(buf: []const u8) ParseError!IPv4` |
| `mapToIPv6` | `pub fn mapToIPv6(self: IPv4) IPv6` |
| `toIPv6` | `pub fn toIPv6(self: IPv4) IPv6` |
| `cmp` | `pub fn cmp(self: IPv6, other: IPv6) math.Order` |
| `eql` | `pub fn eql(self: IPv6, other: IPv6) bool` |
| `isUnspecified` | `pub fn isUnspecified(self: IPv6) bool` |
| `isLoopback` | `pub fn isLoopback(self: IPv6) bool` |
| `mapsToIPv4` | `pub fn mapsToIPv4(self: IPv6) bool` |
| `toIPv4` | `pub fn toIPv4(self: IPv6) ?IPv4` |
| `isMulticast` | `pub fn isMulticast(self: IPv6) bool` |
| `isLinkLocal` | `pub fn isLinkLocal(self: IPv6) bool` |
| `isSiteLocal` | `pub fn isSiteLocal(self: IPv6) bool` |
| `scope` | `pub fn scope(self: IPv6) Scope` |
| `format` | `pub fn format( self: IPv6, comptime layout: []const u8, opts: fmt.FormatOptions, writer: anytype, ) !void` |
| `parse` | `pub fn parse(buf: []const u8) ParseError!IPv6` |
| `parseWithScopeID` | `pub fn parseWithScopeID(buf: []const u8, scope_id: u32) ParseError!IPv6` |

## x / os / socket

| Function | Signature |
|----------|-----------|
| `from` | `pub fn from(socket: Socket, address: Socket.Address) Socket.Connection` |
| `initIPv4` | `pub fn initIPv4(host: net.IPv4, port: u16) Socket.Address` |
| `initIPv6` | `pub fn initIPv6(host: net.IPv6, port: u16) Socket.Address` |
| `fromNative` | `pub fn fromNative(address: *align(4) const os.sockaddr) Socket.Address` |
| `toNative` | `pub fn toNative(self: Socket.Address) extern union` |
| `getNativeSize` | `pub fn getNativeSize(self: Socket.Address) u32` |
| `format` | `pub fn format( self: Socket.Address, comptime layout: []const u8, opts: fmt.FormatOptions, writer: anytype, ) !void` |
| `fromBuffers` | `pub fn fromBuffers(buffers: []const Buffer) Self` |
| `setName` | `pub fn setName(self: *Self, name: []const u8) void` |
| `setBuffers` | `pub fn setBuffers(self: *Self, buffers: []const Buffer) void` |
| `setControl` | `pub fn setControl(self: *Self, control: []const u8) void` |
| `setFlags` | `pub fn setFlags(self: *Self, flags: u32) void` |
| `getName` | `pub fn getName(self: Self) []const u8` |
| `getBuffers` | `pub fn getBuffers(self: Self) []const Buffer` |
| `getControl` | `pub fn getControl(self: Self) []const u8` |
| `getFlags` | `pub fn getFlags(self: Self) u32` |
| `init` | `pub fn init(timeout_seconds: ?u16) Socket.Linger` |
| `from` | `pub fn from(fd: os.socket_t) Socket` |

## x / os / socket_posix

| Function | Signature |
|----------|-----------|
| `Mixin` | `pub fn Mixin(comptime Socket: type) type` |
| `init` | `pub fn init(domain: u32, socket_type: u32, protocol: u32, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Socket` |
| `deinit` | `pub fn deinit(self: Socket) void` |
| `shutdown` | `pub fn shutdown(self: Socket, how: os.ShutdownHow) !void` |
| `bind` | `pub fn bind(self: Socket, address: Socket.Address) !void` |
| `listen` | `pub fn listen(self: Socket, max_backlog_size: u31) !void` |
| `connect` | `pub fn connect(self: Socket, address: Socket.Address) !void` |
| `accept` | `pub fn accept(self: Socket, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Socket.Connection` |
| `read` | `pub fn read(self: Socket, buf: []u8, flags: u32) !usize` |
| `write` | `pub fn write(self: Socket, buf: []const u8, flags: u32) !usize` |
| `writeMessage` | `pub fn writeMessage(self: Socket, msg: Socket.Message, flags: u32) !usize` |
| `readMessage` | `pub fn readMessage(self: Socket, msg: *Socket.Message, flags: u32) !usize` |
| `getLocalAddress` | `pub fn getLocalAddress(self: Socket) !Socket.Address` |
| `getRemoteAddress` | `pub fn getRemoteAddress(self: Socket) !Socket.Address` |
| `getError` | `pub fn getError(self: Socket) !void` |
| `getReadBufferSize` | `pub fn getReadBufferSize(self: Socket) !u32` |
| `getWriteBufferSize` | `pub fn getWriteBufferSize(self: Socket) !u32` |
| `setOption` | `pub fn setOption(self: Socket, level: u32, code: u32, value: []const u8) !void` |
| `setLinger` | `pub fn setLinger(self: Socket, timeout_seconds: ?u16) !void` |
| `setKeepAlive` | `pub fn setKeepAlive(self: Socket, enabled: bool) !void` |
| `setReuseAddress` | `pub fn setReuseAddress(self: Socket, enabled: bool) !void` |
| `setReusePort` | `pub fn setReusePort(self: Socket, enabled: bool) !void` |
| `setWriteBufferSize` | `pub fn setWriteBufferSize(self: Socket, size: u32) !void` |
| `setReadBufferSize` | `pub fn setReadBufferSize(self: Socket, size: u32) !void` |
| `setWriteTimeout` | `pub fn setWriteTimeout(self: Socket, milliseconds: usize) !void` |
| `setReadTimeout` | `pub fn setReadTimeout(self: Socket, milliseconds: usize) !void` |

## x / os / socket_windows

| Function | Signature |
|----------|-----------|
| `Mixin` | `pub fn Mixin(comptime Socket: type) type` |
| `init` | `pub fn init(domain: u32, socket_type: u32, protocol: u32, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Socket` |
| `deinit` | `pub fn deinit(self: Socket) void` |
| `shutdown` | `pub fn shutdown(self: Socket, how: os.ShutdownHow) !void` |
| `bind` | `pub fn bind(self: Socket, address: Socket.Address) !void` |
| `listen` | `pub fn listen(self: Socket, max_backlog_size: u31) !void` |
| `connect` | `pub fn connect(self: Socket, address: Socket.Address) !void` |
| `accept` | `pub fn accept(self: Socket, flags: std.enums.EnumFieldStruct(Socket.InitFlags, bool, false)) !Socket.Connection` |
| `read` | `pub fn read(self: Socket, buf: []u8, flags: u32) !usize` |
| `write` | `pub fn write(self: Socket, buf: []const u8, flags: u32) !usize` |
| `writeMessage` | `pub fn writeMessage(self: Socket, msg: Socket.Message, flags: u32) !usize` |
| `readMessage` | `pub fn readMessage(self: Socket, msg: *Socket.Message, flags: u32) !usize` |
| `getLocalAddress` | `pub fn getLocalAddress(self: Socket) !Socket.Address` |
| `getRemoteAddress` | `pub fn getRemoteAddress(self: Socket) !Socket.Address` |
| `getError` | `pub fn getError(self: Socket) !void` |
| `getReadBufferSize` | `pub fn getReadBufferSize(self: Socket) !u32` |
| `getWriteBufferSize` | `pub fn getWriteBufferSize(self: Socket) !u32` |
| `setOption` | `pub fn setOption(self: Socket, level: u32, code: u32, value: []const u8) !void` |
| `setLinger` | `pub fn setLinger(self: Socket, timeout_seconds: ?u16) !void` |
| `setKeepAlive` | `pub fn setKeepAlive(self: Socket, enabled: bool) !void` |
| `setReuseAddress` | `pub fn setReuseAddress(self: Socket, enabled: bool) !void` |
| `setReusePort` | `pub fn setReusePort(self: Socket, enabled: bool) !void` |
| `setWriteBufferSize` | `pub fn setWriteBufferSize(self: Socket, size: u32) !void` |
| `setReadBufferSize` | `pub fn setReadBufferSize(self: Socket, size: u32) !void` |
| `setWriteTimeout` | `pub fn setWriteTimeout(self: Socket, milliseconds: u32) !void` |
| `setReadTimeout` | `pub fn setReadTimeout(self: Socket, milliseconds: u32) !void` |

## zig / Ast

| Function | Signature |
|----------|-----------|
| `deinit` | `pub fn deinit(tree: *Ast, gpa: mem.Allocator) void` |
| `render` | `pub fn render(tree: Ast, gpa: mem.Allocator) RenderError![]u8` |
| `renderToArrayList` | `pub fn renderToArrayList(tree: Ast, buffer: *std.ArrayList(u8)) RenderError!void` |
| `errorOffset` | `pub fn errorOffset(tree: Ast, parse_error: Error) u32` |
| `tokenLocation` | `pub fn tokenLocation(self: Ast, start_offset: ByteOffset, token_index: TokenIndex) Location` |
| `tokenSlice` | `pub fn tokenSlice(tree: Ast, token_index: TokenIndex) []const u8` |
| `extraData` | `pub fn extraData(tree: Ast, index: usize, comptime T: type) T` |
| `rootDecls` | `pub fn rootDecls(tree: Ast) []const Node.Index` |
| `renderError` | `pub fn renderError(tree: Ast, parse_error: Error, stream: anytype) !void` |
| `firstToken` | `pub fn firstToken(tree: Ast, node: Node.Index) TokenIndex` |
| `lastToken` | `pub fn lastToken(tree: Ast, node: Node.Index) TokenIndex` |
| `tokensOnSameLine` | `pub fn tokensOnSameLine(tree: Ast, token1: TokenIndex, token2: TokenIndex) bool` |
| `getNodeSource` | `pub fn getNodeSource(tree: Ast, node: Node.Index) []const u8` |
| `globalVarDecl` | `pub fn globalVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `localVarDecl` | `pub fn localVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `simpleVarDecl` | `pub fn simpleVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
| `alignedVarDecl` | `pub fn alignedVarDecl(tree: Ast, node: Node.Index) full.VarDecl` |
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
| `switchCaseOne` | `pub fn switchCaseOne(tree: Ast, node: Node.Index) full.SwitchCase` |
| `switchCase` | `pub fn switchCase(tree: Ast, node: Node.Index) full.SwitchCase` |
| `asmSimple` | `pub fn asmSimple(tree: Ast, node: Node.Index) full.Asm` |
| `asmFull` | `pub fn asmFull(tree: Ast, node: Node.Index) full.Asm` |
| `whileSimple` | `pub fn whileSimple(tree: Ast, node: Node.Index) full.While` |
| `whileCont` | `pub fn whileCont(tree: Ast, node: Node.Index) full.While` |
| `whileFull` | `pub fn whileFull(tree: Ast, node: Node.Index) full.While` |
| `forSimple` | `pub fn forSimple(tree: Ast, node: Node.Index) full.While` |
| `forFull` | `pub fn forFull(tree: Ast, node: Node.Index) full.While` |
| `callOne` | `pub fn callOne(tree: Ast, buffer: *[1]Node.Index, node: Node.Index) full.Call` |
| `callFull` | `pub fn callFull(tree: Ast, node: Node.Index) full.Call` |
| `firstToken` | `pub fn firstToken(var_decl: VarDecl) TokenIndex` |
| `firstToken` | `pub fn firstToken(cf: ContainerField) TokenIndex` |
| `firstToken` | `pub fn firstToken(fn_proto: FnProto) TokenIndex` |
| `next` | `pub fn next(it: *Iterator) ?Param` |
| `iterate` | `pub fn iterate(fn_proto: *const FnProto, tree: *const Ast) Iterator` |
| `isContainerField` | `pub fn isContainerField(tag: Tag) bool` |

## zig / c_builtins

| Function | Signature |
|----------|-----------|
| `__builtin_bswap16` | `pub inline fn __builtin_bswap16(val: u16) u16` |
| `__builtin_bswap32` | `pub inline fn __builtin_bswap32(val: u32) u32` |
| `__builtin_bswap64` | `pub inline fn __builtin_bswap64(val: u64) u64` |
| `__builtin_signbit` | `pub inline fn __builtin_signbit(val: f64) c_int` |
| `__builtin_signbitf` | `pub inline fn __builtin_signbitf(val: f32) c_int` |
| `__builtin_popcount` | `pub inline fn __builtin_popcount(val: c_uint) c_int` |
| `__builtin_ctz` | `pub inline fn __builtin_ctz(val: c_uint) c_int` |
| `__builtin_clz` | `pub inline fn __builtin_clz(val: c_uint) c_int` |
| `__builtin_sqrt` | `pub inline fn __builtin_sqrt(val: f64) f64` |
| `__builtin_sqrtf` | `pub inline fn __builtin_sqrtf(val: f32) f32` |
| `__builtin_sin` | `pub inline fn __builtin_sin(val: f64) f64` |
| `__builtin_sinf` | `pub inline fn __builtin_sinf(val: f32) f32` |
| `__builtin_cos` | `pub inline fn __builtin_cos(val: f64) f64` |
| `__builtin_cosf` | `pub inline fn __builtin_cosf(val: f32) f32` |
| `__builtin_exp` | `pub inline fn __builtin_exp(val: f64) f64` |
| `__builtin_expf` | `pub inline fn __builtin_expf(val: f32) f32` |
| `__builtin_exp2` | `pub inline fn __builtin_exp2(val: f64) f64` |
| `__builtin_exp2f` | `pub inline fn __builtin_exp2f(val: f32) f32` |
| `__builtin_log` | `pub inline fn __builtin_log(val: f64) f64` |
| `__builtin_logf` | `pub inline fn __builtin_logf(val: f32) f32` |
| `__builtin_log2` | `pub inline fn __builtin_log2(val: f64) f64` |
| `__builtin_log2f` | `pub inline fn __builtin_log2f(val: f32) f32` |
| `__builtin_log10` | `pub inline fn __builtin_log10(val: f64) f64` |
| `__builtin_log10f` | `pub inline fn __builtin_log10f(val: f32) f32` |
| `__builtin_abs` | `pub inline fn __builtin_abs(val: c_int) c_int` |
| `__builtin_fabs` | `pub inline fn __builtin_fabs(val: f64) f64` |
| `__builtin_fabsf` | `pub inline fn __builtin_fabsf(val: f32) f32` |
| `__builtin_floor` | `pub inline fn __builtin_floor(val: f64) f64` |
| `__builtin_floorf` | `pub inline fn __builtin_floorf(val: f32) f32` |
| `__builtin_ceil` | `pub inline fn __builtin_ceil(val: f64) f64` |
| `__builtin_ceilf` | `pub inline fn __builtin_ceilf(val: f32) f32` |
| `__builtin_trunc` | `pub inline fn __builtin_trunc(val: f64) f64` |
| `__builtin_truncf` | `pub inline fn __builtin_truncf(val: f32) f32` |
| `__builtin_round` | `pub inline fn __builtin_round(val: f64) f64` |
| `__builtin_roundf` | `pub inline fn __builtin_roundf(val: f32) f32` |
| `__builtin_strlen` | `pub inline fn __builtin_strlen(s: [*c]const u8) usize` |
| `__builtin_strcmp` | `pub inline fn __builtin_strcmp(s1: [*c]const u8, s2: [*c]const u8) c_int` |
| `__builtin_object_size` | `pub inline fn __builtin_object_size(ptr: ?*const anyopaque, ty: c_int) usize` |
| `__builtin___memset_chk` | `pub inline fn __builtin___memset_chk( dst: ?*anyopaque, val: c_int, len: usize, remaining: usize, ) ?*anyopaque` |
| `__builtin_memset` | `pub inline fn __builtin_memset(dst: ?*anyopaque, val: c_int, len: usize) ?*anyopaque` |
| `__builtin___memcpy_chk` | `pub inline fn __builtin___memcpy_chk( noalias dst: ?*anyopaque, noalias src: ?*const anyopaque, len: usize, remaining: usize, ) ?*anyopaque` |
| `__builtin_memcpy` | `pub inline fn __builtin_memcpy( noalias dst: ?*anyopaque, noalias src: ?*const anyopaque, len: usize, ) ?*anyopaque` |
| `__builtin_expect` | `pub inline fn __builtin_expect(expr: c_long, c: c_long) c_long` |
| `__builtin_nanf` | `pub inline fn __builtin_nanf(tagp: []const u8) f32` |
| `__builtin_huge_valf` | `pub inline fn __builtin_huge_valf() f32` |
| `__builtin_inff` | `pub inline fn __builtin_inff() f32` |
| `__builtin_isnan` | `pub inline fn __builtin_isnan(x: anytype) c_int` |
| `__builtin_isinf` | `pub inline fn __builtin_isinf(x: anytype) c_int` |
| `__builtin_isinf_sign` | `pub inline fn __builtin_isinf_sign(x: anytype) c_int` |
| `__has_builtin` | `pub inline fn __has_builtin(func: anytype) c_int` |
| `__builtin_assume` | `pub inline fn __builtin_assume(cond: bool) void` |
| `__builtin_unreachable` | `pub inline fn __builtin_unreachable() noreturn` |
| `__builtin_constant_p` | `pub inline fn __builtin_constant_p(expr: anytype) c_int` |
| `__builtin_mul_overflow` | `pub fn __builtin_mul_overflow(a: anytype, b: anytype, result: *@TypeOf(a, b)) c_int` |
| `__builtin_alloca_with_align` | `pub fn __builtin_alloca_with_align(size: usize, alignment: usize) callconv(.Inline) *anyopaque` |

## zig / c_translation

| Function | Signature |
|----------|-----------|
| `cast` | `pub fn cast(comptime DestType: type, target: anytype) DestType` |
| `sizeof` | `pub fn sizeof(target: anytype) usize` |
| `promoteIntLiteral` | `pub fn promoteIntLiteral( comptime SuffixType: type, comptime number: comptime_int, comptime radix: CIntLiteralRadix, ) PromoteIntLiteralReturnType(SuffixType, number, radix)` |
| `shuffleVectorIndex` | `pub fn shuffleVectorIndex(comptime this_index: c_int, comptime source_vector_len: usize) i32` |
| `FlexibleArrayType` | `pub fn FlexibleArrayType(comptime SelfType: type, comptime ElementType: type) type` |
| `signedRemainder` | `pub fn signedRemainder(numerator: anytype, denominator: anytype) @TypeOf(numerator, denominator)` |
| `U_SUFFIX` | `pub fn U_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_uint, n, .decimal))` |
| `L_SUFFIX` | `pub fn L_SUFFIX(comptime number: anytype) L_SUFFIX_ReturnType(number)` |
| `UL_SUFFIX` | `pub fn UL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_ulong, n, .decimal))` |
| `LL_SUFFIX` | `pub fn LL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_longlong, n, .decimal))` |
| `ULL_SUFFIX` | `pub fn ULL_SUFFIX(comptime n: comptime_int) @TypeOf(promoteIntLiteral(c_ulonglong, n, .decimal))` |
| `F_SUFFIX` | `pub fn F_SUFFIX(comptime f: comptime_float) f32` |
| `WL_CONTAINER_OF` | `pub fn WL_CONTAINER_OF(ptr: anytype, sample: anytype, comptime member: []const u8) @TypeOf(sample)` |
| `CAST_OR_CALL` | `pub fn CAST_OR_CALL(a: anytype, b: anytype) switch (@typeInfo(@TypeOf(a)))` |
| `DISCARD` | `pub inline fn DISCARD(x: anytype) void` |
| `div` | `pub fn div(a: anytype, b: anytype) ArithmeticConversion(@TypeOf(a), @TypeOf(b))` |
| `rem` | `pub fn rem(a: anytype, b: anytype) ArithmeticConversion(@TypeOf(a), @TypeOf(b))` |

## zig / CrossTarget

| Function | Signature |
|----------|-----------|
| `fromTarget` | `pub fn fromTarget(target: Target) CrossTarget` |
| `toTarget` | `pub fn toTarget(self: CrossTarget) Target` |
| `parse` | `pub fn parse(args: ParseOptions) !CrossTarget` |
| `parseCpuArch` | `pub fn parseCpuArch(args: ParseOptions) ?Target.Cpu.Arch` |
| `getCpu` | `pub fn getCpu(self: CrossTarget) Target.Cpu` |
| `getCpuArch` | `pub fn getCpuArch(self: CrossTarget) Target.Cpu.Arch` |
| `getCpuModel` | `pub fn getCpuModel(self: CrossTarget) *const Target.Cpu.Model` |
| `getCpuFeatures` | `pub fn getCpuFeatures(self: CrossTarget) Target.Cpu.Feature.Set` |
| `getOs` | `pub fn getOs(self: CrossTarget) Target.Os` |
| `getOsTag` | `pub fn getOsTag(self: CrossTarget) Target.Os.Tag` |
| `getOsVersionMin` | `pub fn getOsVersionMin(self: CrossTarget) OsVersion` |
| `getOsVersionMax` | `pub fn getOsVersionMax(self: CrossTarget) OsVersion` |
| `getAbi` | `pub fn getAbi(self: CrossTarget) Target.Abi` |
| `isFreeBSD` | `pub fn isFreeBSD(self: CrossTarget) bool` |
| `isDarwin` | `pub fn isDarwin(self: CrossTarget) bool` |
| `isNetBSD` | `pub fn isNetBSD(self: CrossTarget) bool` |
| `isOpenBSD` | `pub fn isOpenBSD(self: CrossTarget) bool` |
| `isUefi` | `pub fn isUefi(self: CrossTarget) bool` |
| `isDragonFlyBSD` | `pub fn isDragonFlyBSD(self: CrossTarget) bool` |
| `isLinux` | `pub fn isLinux(self: CrossTarget) bool` |
| `isWindows` | `pub fn isWindows(self: CrossTarget) bool` |
| `exeFileExt` | `pub fn exeFileExt(self: CrossTarget) [:0]const u8` |
| `staticLibSuffix` | `pub fn staticLibSuffix(self: CrossTarget) [:0]const u8` |
| `dynamicLibSuffix` | `pub fn dynamicLibSuffix(self: CrossTarget) [:0]const u8` |
| `libPrefix` | `pub fn libPrefix(self: CrossTarget) [:0]const u8` |
| `isNativeCpu` | `pub fn isNativeCpu(self: CrossTarget) bool` |
| `isNativeOs` | `pub fn isNativeOs(self: CrossTarget) bool` |
| `isNativeAbi` | `pub fn isNativeAbi(self: CrossTarget) bool` |
| `isNative` | `pub fn isNative(self: CrossTarget) bool` |
| `zigTriple` | `pub fn zigTriple(self: CrossTarget, allocator: mem.Allocator) error` |
| `allocDescription` | `pub fn allocDescription(self: CrossTarget, allocator: mem.Allocator) ![]u8` |
| `linuxTriple` | `pub fn linuxTriple(self: CrossTarget, allocator: mem.Allocator) ![]u8` |
| `wantSharedLibSymLinks` | `pub fn wantSharedLibSymLinks(self: CrossTarget) bool` |
| `vcpkgTriplet` | `pub fn vcpkgTriplet(self: CrossTarget, allocator: mem.Allocator, linkage: VcpkgLinkage) ![]u8` |
| `isGnuLibC` | `pub fn isGnuLibC(self: CrossTarget) bool` |
| `setGnuLibCVersion` | `pub fn setGnuLibCVersion(self: *CrossTarget, major: u32, minor: u32, patch: u32) void` |
| `getObjectFormat` | `pub fn getObjectFormat(self: CrossTarget) Target.ObjectFormat` |
| `updateCpuFeatures` | `pub fn updateCpuFeatures(self: CrossTarget, set: *Target.Cpu.Feature.Set) void` |

## zig / fmt

| Function | Signature |
|----------|-----------|
| `fmtId` | `pub fn fmtId(bytes: []const u8) std.fmt.Formatter(formatId)` |
| `isValidId` | `pub fn isValidId(bytes: []const u8) bool` |
| `fmtEscapes` | `pub fn fmtEscapes(bytes: []const u8) std.fmt.Formatter(formatEscapes)` |

## zig / number_literal

| Function | Signature |
|----------|-----------|
| `parseNumberLiteral` | `pub fn parseNumberLiteral(bytes: []const u8) Result` |

## zig / parse

| Function | Signature |
|----------|-----------|
| `parse` | `pub fn parse(gpa: Allocator, source: [:0]const u8) Allocator.Error!Ast` |

## zig / render

| Function | Signature |
|----------|-----------|
| `renderTree` | `pub fn renderTree(buffer: *std.ArrayList(u8), tree: Ast) Error!void` |
| `writer` | `pub fn writer(self: *Self) Writer` |
| `write` | `pub fn write(self: *Self, bytes: []const u8) WriteError!usize` |
| `setIndentDelta` | `pub fn setIndentDelta(self: *Self, new_indent_delta: usize) void` |
| `insertNewline` | `pub fn insertNewline(self: *Self) WriteError!void` |
| `maybeInsertNewline` | `pub fn maybeInsertNewline(self: *Self) WriteError!void` |
| `pushIndent` | `pub fn pushIndent(self: *Self) void` |
| `pushIndentOneShot` | `pub fn pushIndentOneShot(self: *Self) void` |
| `lockOneShotIndent` | `pub fn lockOneShotIndent(self: *Self) usize` |
| `pushIndentNextLine` | `pub fn pushIndentNextLine(self: *Self) void` |
| `popIndent` | `pub fn popIndent(self: *Self) void` |
| `isLineOverIndented` | `pub fn isLineOverIndented(self: *Self) bool` |

## zig / string_literal

| Function | Signature |
|----------|-----------|
| `parseCharLiteral` | `pub fn parseCharLiteral(slice: []const u8) ParsedCharLiteral` |
| `parseAppend` | `pub fn parseAppend(buf: *std.ArrayList(u8), bytes: []const u8) error` |
| `parseAlloc` | `pub fn parseAlloc(allocator: std.mem.Allocator, bytes: []const u8) ParseError![]u8` |

## zig / system / arm

| Function | Signature |
|----------|-----------|
| `isKnown` | `pub fn isKnown(core: CoreInfo, is_64bit: bool) ?*const Target.Cpu.Model` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(arch: Target.Cpu.Arch, registers: [12]u64) ?Target.Cpu` |

## zig / system / darwin

| Function | Signature |
|----------|-----------|
| `isDarwinSDKInstalled` | `pub fn isDarwinSDKInstalled(allocator: Allocator) bool` |
| `getDarwinSDK` | `pub fn getDarwinSDK(allocator: Allocator, target: Target) ?DarwinSDK` |
| `deinit` | `pub fn deinit(self: DarwinSDK, allocator: Allocator) void` |

## zig / system / darwin / macos

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(target_os: *Target.Os) !void` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures() ?Target.Cpu` |

## zig / system / linux

| Function | Signature |
|----------|-----------|
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures() ?Target.Cpu` |

## zig / system / NativePaths

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(allocator: Allocator, native_info: NativeTargetInfo) !NativePaths` |
| `deinit` | `pub fn deinit(self: *NativePaths) void` |
| `addIncludeDir` | `pub fn addIncludeDir(self: *NativePaths, s: []const u8) !void` |
| `addIncludeDirFmt` | `pub fn addIncludeDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addLibDir` | `pub fn addLibDir(self: *NativePaths, s: []const u8) !void` |
| `addLibDirFmt` | `pub fn addLibDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addWarning` | `pub fn addWarning(self: *NativePaths, s: []const u8) !void` |
| `addFrameworkDir` | `pub fn addFrameworkDir(self: *NativePaths, s: []const u8) !void` |
| `addFrameworkDirFmt` | `pub fn addFrameworkDirFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addWarningFmt` | `pub fn addWarningFmt(self: *NativePaths, comptime fmt: []const u8, args: anytype) !void` |
| `addRPath` | `pub fn addRPath(self: *NativePaths, s: []const u8) !void` |

## zig / system / NativeTargetInfo

| Function | Signature |
|----------|-----------|
| `detect` | `pub fn detect(cross_target: CrossTarget) DetectError!NativeTargetInfo` |
| `abiAndDynamicLinkerFromFile` | `pub fn abiAndDynamicLinkerFromFile( file: fs.File, cpu: Target.Cpu, os: Target.Os, ld_info_list: []const LdInfo, cross_target: CrossTarget, ) AbiAndDynamicLinkerFromFileError!NativeTargetInfo` |
| `elfInt` | `pub fn elfInt(is_64: bool, need_bswap: bool, int_32: anytype, int_64: anytype) @TypeOf(int_64)` |
| `getExternalExecutor` | `pub fn getExternalExecutor( host: NativeTargetInfo, candidate: NativeTargetInfo, options: GetExternalExecutorOptions, ) Executor` |

## zig / system / windows

| Function | Signature |
|----------|-----------|
| `detectRuntimeVersion` | `pub fn detectRuntimeVersion() WindowsVersion` |
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures() ?Target.Cpu` |

## zig / system / x86

| Function | Signature |
|----------|-----------|
| `detectNativeCpuAndFeatures` | `pub fn detectNativeCpuAndFeatures(arch: Target.Cpu.Arch, os: Target.Os, cross_target: CrossTarget) Target.Cpu` |

## zig / tokenizer

| Function | Signature |
|----------|-----------|
| `getKeyword` | `pub fn getKeyword(bytes: []const u8) ?Tag` |
| `lexeme` | `pub fn lexeme(tag: Tag) ?[]const u8` |
| `symbol` | `pub fn symbol(tag: Tag) []const u8` |
| `dump` | `pub fn dump(self: *Tokenizer, token: *const Token) void` |
| `init` | `pub fn init(buffer: [:0]const u8) Tokenizer` |
| `next` | `pub fn next(self: *Tokenizer) Token` |
