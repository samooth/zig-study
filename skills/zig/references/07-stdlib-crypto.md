# Crypto Reference

Cryptographic primitives in Zig 0.16+/0.17+.

## AEAD (Authenticated Encryption)

```zig
const std = @import("std");

// AES-GCM
const key: [32]u8 = ...; // 256-bit key
const nonce: [12]u8 = ...;
const ad = "associated data";
const plaintext = "secret message";

var ciphertext: [plaintext.len]u8 = undefined;
var tag: [16]u8 = undefined;
std.crypto.aead.aes_gcm.Aes256Gcm.encrypt(&ciphertext, &tag, plaintext, ad, nonce, key);

// ChaCha20-Poly1305
std.crypto.aead.chacha_poly.ChaCha20Poly1305.encrypt(&ciphertext, &tag, plaintext, ad, nonce, key);
```

## Hashing

```zig
// SHA-256
var hash: [32]u8 = undefined;
std.crypto.hash.sha2.Sha256.hash(data, &hash, .{});

// SHA-512
var hash512: [64]u8 = undefined;
std.crypto.hash.sha2.Sha512.hash(data, &hash512, .{});

// BLAKE3
var b3: [32]u8 = undefined;
std.crypto.hash.blake3.Blake3.hash(data, &b3, .{});

// BLAKE2b
var b2: [32]u8 = undefined;
std.crypto.hash.blake2.Blake2b256.hash(data, &b2, .{});
```

## HMAC

```zig
var mac: [32]u8 = undefined;
std.crypto.auth.hmac.HmacSha256.create(&mac, data, key);
```

## KDF

```zig
// HKDF
const okm = try std.crypto.kdf.hkdf.HkdfSha256.expand(prk, info, output_len, salt);

// PBKDF2
const key = try std.crypto.kdf.pbkdf2.pbkdf2(allocator, password, salt, iterations, key_len);
```

## Password Hashing

```zig
// Argon2
const hash = try std.crypto.pwhash.argon2.strHash(password, .{
    .allocator = allocator,
    .params = .{ .ops_limit = 2, .mem_limit = 65536 },
});

// Verify
const result = try std.crypto.pwhash.argon2.strVerify(hash, password);
```

## Post-Quantum (0.16+)

```zig
// ML-KEM (Key Encapsulation) — std.crypto.kem.ml_kem
const kp = try std.crypto.kem.ml_kem.MLKem768.KeyPair.generate(io);
const enc = std.crypto.kem.ml_kem.MLKem768.encaps(kp.public_key, io);
const shared = try std.crypto.kem.ml_kem.MLKem768.decaps(kp.secret_key, enc.ciphertext);

// ML-DSA (Digital Signature) — std.crypto.sign.mldsa
const kp2 = try std.crypto.sign.mldsa.MLDsa65.KeyPair.generate(io);
const sig = try kp2.sign(msg, null);
try sig.verify(msg, kp2.public_key);
```

## Random

```zig
// Via Io (recommended)
var buf: [32]u8 = undefined;
io.random(&buf);

// Direct (still works)
std.crypto.random.bytes(&buf);
```

## TLS

```zig
const client = std.http.Client{ .allocator = allocator };
var request = try client.request(.GET, uri, .{});
defer request.deinit();
```

## Common Types

| Type | Size | Purpose |
|------|------|---------|
| `[32]u8` | 256-bit | AES-256 key, SHA-256 hash |
| `[16]u8` | 128-bit | AES-128 key, AES-GCM tag |
| `[12]u8` | 96-bit | AES-GCM nonce |
| `[24]u8` | 192-bit | ChaCha20 nonce |
