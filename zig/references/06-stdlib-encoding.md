# Encoding Reference

String formatting, JSON, compression, and encoding in Zig 0.16+/0.17+.

## String Formatting (std.fmt)

```zig
const std = @import("std");

// Print to stderr
std.debug.print("value: {}, string: {s}\n", .{ 42, "hello" });

// Format to buffer
var buf: [100]u8 = undefined;
const result = try std.fmt.bufPrint(&buf, "x={d}", .{42});

// Format specifiers
// {}   — default format
// {s}  — string
// {d}  — decimal integer
// {x}  — hex
// {X}  — hex uppercase
// {o}  — octal
// {b}  — binary
// {e}  — scientific float
// {f}  — decimal float
// {d:.2} — float with 2 decimal places
// {c}  — character
```

## JSON (std.json)

### Parse

```zig
const Config = struct {
    name: []const u8,
    version: u32,
    tags: []const []const u8,
};

const parsed = try std.json.parseFromSlice(Config, allocator, json_bytes, .{});
defer parsed.deinit();
const config = parsed.value;
```

### Stringify

```zig
const config = Config{ .name = "myapp", .version = 1, .tags = &.{"zig"} };
const json = try std.json.stringifyAlloc(allocator, config, .{});
defer allocator.free(json);
```

### Dynamic Parsing

```zig
const parsed = try std.json.parseFromSlice(std.json.Value, allocator, bytes, .{});
defer parsed.deinit();

if (parsed.value == .object) |obj| {
    if (obj.get("key")) |val| {
        if (val == .string) |s| { _ = s; }
    }
}
```

## Base64

```zig
const std = @import("std");

// Encode
const encoded = try std.base64.standard.Encoder.encode(allocator, data);
defer allocator.free(encoded);

// Decode
const decoded = try std.base64.standard.Decoder.decode(allocator, encoded);
defer allocator.free(decoded);
```

## Compression

### Gzip / Zlib (via flate)

```zig
var buf: [8192]u8 = undefined;
var decomp = std.compress.flate.Decompress.init(&reader, .gzip, &buf);
const data = try decomp.reader.readAllAlloc(allocator, max_size);
defer allocator.free(data);
```

### Zstandard (0.16+)

```zig
var buf: [8192]u8 = undefined;
var decomp = std.compress.zstd.Decompress.init(&reader, &buf, .{});
const data = try decomp.reader.readAllAlloc(allocator, max_size);
defer allocator.free(data);
```

## Tar

```zig
var tar_reader = std.tar.reader(allocator, comp_reader);
while (try tar_reader.next()) |entry| {
    // entry.name, entry.kind
    const data = try tar_reader.readAllAlloc(allocator, max_size);
    defer allocator.free(data);
}
```

## LEB128

```zig
// Read
const value = try std.leb.readUleb128(u32, reader);

// Write
try std.leb.writeUleb128(writer, value);
```

## URI

```zig
const uri = try std.Uri.parse("https://example.com/path?q=1");
// uri.host, uri.path, uri.query
```

## Unicode

```zig
// Decode UTF-8
const cp = try std.unicode.utf8Decode("€");

// Encode UTF-8
var buf: [4]u8 = undefined;
const len = try std.unicode.utf8Encode(cp, &buf);
```
