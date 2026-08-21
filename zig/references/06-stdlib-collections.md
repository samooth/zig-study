# Collections Reference

Data structures in Zig 0.16+/0.17+.

## ArrayList

Growable array, most common collection.

```zig
var list = std.ArrayList(u32).empty;
defer list.deinit(allocator);

try list.append(allocator, 42);
try list.appendSlice(allocator, &.{ 1, 2, 3 });
try list.insert(allocator, 0, 99);
_ = list.orderedRemove(0);
_ = list.swapRemove(0);

// Access
const item = list.items[i];
const len = list.items.len;

// Own the slice
const owned = try list.toOwnedSlice(allocator);
defer allocator.free(owned);
```

## HashMap

Hash map with string or custom keys.

```zig
// String-keyed
var map = std.StringHashMap(u32).empty;
defer map.deinit(allocator);

try map.put(allocator, "key", 42);
if (map.get("key")) |val| { _ = val; }
if (map.getPtr("key")) |ptr| { ptr.* = 100; }
_ = map.remove("key");

// Integer-keyed
var int_map = std.AutoHashMap(u32, bool).empty;
defer int_map.deinit(allocator);

try int_map.put(allocator, 42, true);

// Iterate
var iter = map.iterator();
while (iter.next()) |entry| {
    // entry.key_ptr, entry.value_ptr
}
```

## ArrayHashMap

Ordered hash map (preserves insertion order).

```zig
var map = std.ArrayHashMap([]const u8, u32, std.hash_map.StringContext, false).empty;
defer map.deinit(allocator);

try map.put(allocator, "key", 42);
```

## MultiArrayList

Struct-of-arrays layout for better cache performance.

```zig
const S = struct { x: u32, y: u32, z: f32 };
var list = std.MultiArrayList(S).empty;
defer list.deinit(allocator);

try list.append(allocator, .{ .x = 1, .y = 2, .z = 3.0 });

// Access by field
const x_vals = list.items(.x); // []u32
const y_vals = list.items(.y); // []u32
```

## SinglyLinkedList

```zig
const Node = struct {
    data: u32,
    next: ?*Node = null,
};

var list: std.SinglyLinkedList(Node) = .{};
const node = try allocator.create(Node);
node.* = .{ .data = 42 };
list.prepend(node);
```

## DoublyLinkedList

```zig
var list: std.DoublyLinkedList(u32) = .{};
const node = try list.createNode(allocator, 42);
list.append(node);
const removed = list.remove(node);
```

## PriorityQueue

```zig
fn lessThan(context: void, a: u32, b: u32) std.math.Order {
    _ = context;
    return std.math.order(a, b);
}

var queue = std.PriorityQueue(u32, void, lessThan).empty;
defer queue.deinit(allocator);

try queue.push(allocator, 42);
const min = queue.pop();
```

## PriorityDequeue

```zig
var dequeue = std.PriorityDequeue(u32, void, lessThan).empty;
defer dequeue.deinit(allocator);

try dequeue.push(allocator, 42);
const min = dequeue.popMin();
const max = dequeue.popMax();
```

## BitSet

```zig
// Static
var bits = std.bit_set.StaticBitSet(64).initEmpty();
bits.set(5);
const has = bits.isSet(5);

// Dynamic
var bits = std.bit_set.DynamicBitSet.initEmpty(allocator, 128);
defer bits.deinit();
bits.set(5);
```

## Treap

```zig
var treap = std.Treap(u32, std.math.order).empty;
try treap.insert(allocator, 42);
const found = treap.find(42);
```

## Deque

```zig
var deque = std.Deque(u32).empty;
defer deque.deinit(allocator);

try deque.pushBack(allocator, 42);
try deque.pushFront(allocator, 99);
const back = deque.popBack();
const front = deque.popFront();
```

## StaticStringMap

Compile-time string lookup.

```zig
const Command = enum { help, version, build };

const map = std.StaticStringMap(Command).initComptime(.{
    .{ "help", .help },
    .{ "version", .version },
    .{ "build", .build },
});

if (map.get("help")) |cmd| {
    // cmd == .help
}
```

## EnumMap / EnumSet / EnumArray

```zig
var em = std.EnumMap(MyEnum).initEmpty();
em.put(.key, value);
if (em.get(.key)) |v| { _ = v; }

var es = std.EnumSet(MyEnum).empty;
es.insert(.a);
es.insert(.b);
const has = es.contains(.a);

var ea = std.EnumArray(MyEnum, u32).initFill(0);
ea.set(.key, 42);
```

## Initialization Pattern (0.16+)

```zig
// ALL collections use .empty, not .{}
var list = std.ArrayList(u32).empty;
var map = std.StringHashMap(u32).empty;
var queue = std.PriorityQueue(u32, void, lessThan).empty;
var bits = std.bit_set.StaticBitSet(64).initEmpty();
```
