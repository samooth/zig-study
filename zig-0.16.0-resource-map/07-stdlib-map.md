# Zig 0.16.0 — Standard Library File Map

Complete directory listing of `<zig-install-dir>/lib/std/`

## Top-Level Files

```
std.zig              — Root namespace, re-exports everything
start.zig            — Program startup/linking logic
builtin.zig          — Compile-time build configuration
```

## Top-Level Modules (single files)

```
Io.zig               — ★ NEW: Central I/O abstraction
process.zig          — Process management, Init (Juicy Main)
mem.zig              — Allocator interface, Alignment, byte utilities
meta.zig             — Compile-time type reflection
math.zig             — Math utilities
fmt.zig              — String formatting
json.zig             — JSON parser/serializer
zon.zig              — ZON parser/serializer
hash.zig             — Hash functions
hash_map.zig         — HashMap implementation
array_hash_map.zig   — ArrayHashMap (ordered)
array_list.zig       — ArrayList (growable array)
multi_array_list.zig — MultiArrayList (SoA layout)
compress.zig         — Compression algorithms
http.zig             — HTTP client/server
crypto.zig           — Cryptography
testing.zig          — Test utilities
debug.zig            — Debugging, stack traces
posix.zig            — Cross-platform POSIX abstraction
os.zig               — OS-specific low-level APIs
base64.zig           — Base64 encoding/decoding
sort.zig             — Sorting algorithms
simd.zig             — SIMD utilities
atomic.zig           — Atomic operations
log.zig              — Logging infrastructure
tar.zig              — Tar archive handling
zip.zig              — ZIP archive handling
unicode.zig          — Unicode utilities
elf.zig              — ELF format parsing
coff.zig             — COFF format parsing
macho.zig            — Mach-O format parsing
pdb.zig              — PDB format parsing
dwarf.zig            — DWARF debug info
wasm.zig             — WebAssembly support
gpu.zig              — GPU interface
leb128.zig           — LEB128 encoding
bit_set.zig          — Bit set types
BitStack.zig         — Nested boolean state stack
buf_map.zig          — Buffer map
buf_set.zig          — Buffer set
deque.zig            — Double-ended queue
DoublyLinkedList.zig — Doubly linked list
SinglyLinkedList.zig — Singly linked list
enums.zig            — EnumArray, EnumMap, EnumSet
static_string_map.zig — Comptime string maps
priority_queue.zig   — Priority queue
priority_dequeue.zig — Priority deque
treap.zig            — Treap data structure
SemanticVersion.zig  — Semantic versioning
Uri.zig              — URI parsing
dynamic_library.zig  — Dynamic library loading
valgrind.zig         — Valgrind client requests
pie.zig              — Position-independent executables
Thread.zig           — OS thread abstraction
Random.zig           — Random number generation
Target.zig           — Target triple resolution
Progress.zig         — Progress bar/reporting
Build.zig            — Build system API (~3000+ lines)
```

## Io/ Subdirectory

```
Io/
├── Dir.zig           — Directory operations (open, create, delete, walk)
├── File.zig          — File handle operations
├── File/
│   ├── Atomic.zig    — Atomic file writes
│   ├── MemoryMap.zig — mmap abstraction
│   ├── MultiReader.zig — Multi-stream reader
│   ├── Reader.zig    — File reading
│   └── Writer.zig    — File writing
├── Reader.zig        — Generic reader interface
├── Reader/
│   └── Limited.zig   — Bounded reader
├── Writer.zig        — Generic writer interface
├── IoUring.zig       — Linux io_uring backend
├── Kqueue.zig        — BSD/macOS kqueue backend
├── Threaded.zig      — Thread-pool based Io (~19K lines)
├── Threaded/
│   └── test.zig
├── net.zig           — Networking (TCP/UDP/Unix/DNS)
├── net/
│   ├── HostName.zig
│   └── test.zig
├── Terminal.zig      — Terminal handling / ANSI codes
├── RwLock.zig        — Reader-writer lock
├── Semaphore.zig     — Semaphore primitive
└── test.zig
```

## process/ Subdirectory

```
process/
├── Args.zig          — CLI argument parsing (Windows/POSIX/WASI)
├── Child.zig         — Child process handle
├── Environ.zig       — Environment variable management
└── Preopens.zig      — WASI preopened directories
```

## heap/ Subdirectory

```
heap/
├── arena_allocator.zig      — ArenaAllocator (bump allocator)
├── debug_allocator.zig      — DebugAllocator (renamed from GPA)
├── FixedBufferAllocator.zig — Stack/buffer allocator
├── PageAllocator.zig        — OS page allocator
├── SmpAllocator.zig         — SMP-optimized allocator (new)
├── sbrk_allocator.zig       — sbrk-based allocator
├── memory_pool.zig          — Single-type memory pool
├── ThreadSafeAllocator.zig  — Thread-safe wrapper
└── WasmAllocator.zig        — WebAssembly allocator
```

## Build/ Subdirectory

```
Build/
├── Step.zig                 — Build step base type
├── Step/
│   ├── Compile.zig          — Compilation step
│   ├── Run.zig              — Run a built artifact
│   ├── WriteFile.zig        — File generation
│   ├── InstallArtifact.zig
│   ├── InstallDir.zig
│   ├── InstallFile.zig
│   ├── ConfigHeader.zig
│   ├── CheckFile.zig
│   ├── CheckObject.zig
│   ├── ObjCopy.zig
│   ├── Options.zig
│   ├── Fmt.zig
│   ├── TranslateC.zig
│   ├── UpdateSourceFiles.zig
│   └── Fail.zig
├── Module.zig               — Module definition
├── Cache.zig                — Content-addressable caching
├── Cache/
│   ├── DepTokenizer.zig
│   ├── Directory.zig
│   └── Path.zig
├── Watch.zig                — File system watching
├── Watch/
│   └── FsEvents.zig
├── Fuzz.zig                 — Fuzzing support
├── WebServer.zig            — Build runner web server
└── abi.zig
```

## crypto/ Subdirectory

```
crypto/
├── tls.zig / tls/           — TLS implementation
├── Certificate.zig          — Certificate handling
├── Certificate/
├── 25519/                   — Curve25519
├── pcurves/                 — Prime-field elliptic curves
├── aes.zig / aes/           — AES
├── aes_gcm.zig              — AES-GCM
├── aes_ccm.zig              — AES-CCM
├── aes_ocb.zig              — AES-OCB
├── aes_siv.zig              — AES-SIV (new)
├── aes_gcm_siv.zig          — AES-GCM-SIV (new)
├── chacha20.zig             — ChaCha20-Poly1305
├── blake2.zig               — BLAKE2
├── blake3.zig               — BLAKE3
├── sha2.zig                 — SHA-2 family
├── sha3.zig                 — SHA-3 family
├── Sha1.zig                 — SHA-1
├── argon2.zig               — Argon2 password hashing
├── scrypt.zig               — scrypt
├── bcrypt.zig               — bcrypt
├── ml_dsa.zig               — ML-DSA (post-quantum)
├── ml_kem.zig               — ML-KEM (post-quantum)
├── ascon.zig                — Ascon (NIST lightweight, new)
├── ff.zig                   — Finite field arithmetic
├── hmac.zig                 — HMAC
├── hkdf.zig                 — HKDF
├── pbkdf2.zig               — PBKDF2
├── x25519.zig               — X25519
├── ed25519.zig              — Ed25519
├── ecdh.zig                 — ECDH
├── ecdsa.zig                — ECDSA
└── ...
```

## os/ Subdirectory

```
os/
├── linux.zig / linux/       — Linux syscalls
├── windows.zig / windows/   — Windows API
├── wasi.zig                 — WASI interface
├── uefi.zig / uefi/         — UEFI firmware API
├── emscripten.zig           — Emscripten
└── plan9.zig / plan9/       — Plan 9
```

## math/ Subdirectory (43 files)

```
math/
├── big.zig / big/           — Arbitrary precision integers
├── complex.zig / complex/   — Complex number math
├── float.zig                — Float utilities
├── pow.zig, sqrt.zig, log.zig
├── sin.zig, cos.zig, tan.zig
├── asin.zig, acos.zig, atan.zig
├── exp.zig, ln.zig
├── root.zig, round.zig
├── order.zig
└── ...
```

## Other Subdirectories

```
zig/                 — Zig compiler internals (Tokenizer, AST, ZIR, etc.)
zig/
├── Ast.zig, AstGen.zig, Zir.zig, Zoir.zig, ZonGen.zig
├── tokenizer.zig, Server.zig, Client.zig
├── ErrorBundle.zig, primitives.zig
├── BuiltinFn.zig, system.zig, target.zig
└── LibCInstallation.zig, WindowsSdk.zig, ...

testing/
└── FailingAllocator.zig

sort/
├── block.zig        — Block sort
└── pdq.zig          — Pattern-defeating quicksort

compress/
├── flate.zig / flate/   — gzip/zlib/deflate
├── xz.zig / xz/         — XZ/LZMA
├── lzma.zig / lzma/
├── zstd.zig / zstd/     — Zstandard (new)
└── testdata/

http/
├── Client.zig       — HTTP client with TLS
├── Server.zig       — HTTP server
├── HeadParser.zig
├── ChunkParser.zig
└── HeaderIterator.zig

Random/
├── Xoshiro256.zig, ChaCha.zig, Isaac64.zig, Pcg.zig
├── Xoroshiro128.zig, Sfc64.zig, RomuTrio.zig, SplitMix64.zig
├── Ascon.zig, lcg.zig, ziggurat.zig
└── test.zig, benchmark.zig

debug/
├── Dwarf.zig, Pdb.zig
├── ElfFile.zig, MachOFile.zig
├── Info.zig, Coverage.zig
└── cpu_context.zig

time/
└── epoch.zig        — Unix epoch calculations

tz/                  — Timezone data
tar/                 — Tar archive internals
unicode/             — Unicode internals
```
