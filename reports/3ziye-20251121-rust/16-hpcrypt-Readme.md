# HPCrypt

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%2FApache--2.0-blue)](LICENSE-MIT)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)
[![no_std compatible](https://img.shields.io/badge/no__std-compatible-success)](https://docs.rust-embedded.org/book/intro/no-std.html)

A comprehensive, high-performance cryptography library written in pure Rust, providing production-ready implementations of modern cryptographic primitives with a focus on security, performance, and usability.

## Features

- **100% Safe Rust** - Zero unsafe code, memory-safe by design
- **no_std Compatible** - Runs in embedded and constrained environments
- **Standards Compliant** - Full RFC and NIST FIPS compliance
- **Post-Quantum Ready** - ML-DSA, ML-KEM, SLH-DSA implementations
- **Comprehensive Testing** - Validated against official test vectors including Wycheproof
- **Constant-Time Operations** - Protection against timing side-channel attacks
- **Modular Design** - Use only what you need

## Crates Overview

The library is organized into focused, composable crates:

### Core Primitives

| Crate | Description | Standards |
|-------|-------------|-----------|
| **hpcrypt-core** | Core utilities, error types, traits | - |
| **hpcrypt-hash** | Hash functions (SHA-2, SHA-3, BLAKE2/3) | FIPS 180-4, FIPS 202, RFC 7693 |
| **hpcrypt-cipher** | Block ciphers (AES, ChaCha20) and modes (CBC, CTR, XTS) | NIST SP 800-38A/E |
| **hpcrypt-mac** | MACs (HMAC, CMAC, KMAC, GMAC, Poly1305) and universal hashes (GHASH, Polyval) | FIPS 198-1, RFC 2104, RFC 4493 |
| **hpcrypt-aead** | Authenticated encryption (AES-GCM, ChaCha20-Poly1305, Ascon) | RFC 5116, RFC 7539, RFC 5297 |
| **hpcrypt-kdf** | Key derivation (HKDF, PBKDF2, Argon2, scrypt, TLS/QUIC KDF) | RFC 5869, RFC 2898, RFC 9106 |
| **hpcrypt-rng** | Cryptographically secure random generation | - |

### Elliptic Curve Cryptography

| Crate | Description | Standards |
|-------|-------------|-----------|
| **hpcrypt-curves** | Elliptic curves (Curve25519, P-256, P-384, P-521, secp256k1) | RFC 7748, RFC 8032, FIPS 186-4, SEC 2 |
| **hpcrypt-signatures** | Digital signatures (Ed25519, Ed448, ECDSA, Schnorr) | RFC 8032, FIPS 186-4, BIP-340 |
| **hpcrypt-ecies** | Hybrid encryption scheme | ISO/IEC 18033-2 |

### Post-Quantum Cryptography

| Crate | Description | Standards |
|-------|-------------|-----------|
| **hpcrypt-mlkem** | ML-KEM (Kyber) key encapsulation | FIPS 203 |
| **hpcrypt-mldsa** | ML-DSA (Dilithium) signatures | FIPS 204 |
| **hpcrypt-slhdsa** | SLH-DSA (SPHINCS+) signatures | FIPS 205 |

### High-Level Protocols

| Crate | Description | Standards |
|-------|-------------|-----------|
| **hpcrypt-rsa** | RSA encryption and signatures (OAEP, PSS, PKCS#1) | RFC 8017 |
| **hpcrypt-hpke** | Hybrid Public Key Encryption | RFC 9180 |
| **hpcrypt-pake** | Password-authenticated key exchange (OPAQUE) | RFC 9497 |
| **hpcrypt-srp** | Secure Remote Password protocol | RFC 2945, RFC 5054 |
| **hpcrypt-fpe** | Format-preserving encryption (FF1) | NIST SP 800-38G |
| **hpcrypt-threshold** | Threshold cryptography (Shamir secret sharing) | - |

## Quick Start

Add to your `Cargo.toml`:

```toml
[dependencies]
hpcrypt = { version = "0.1", features = ["curves", "aead", "hash"] }
```

### AES-GCM Authenticated Encryption

```rust
use hpcrypt::aead::{Aes256Gcm, Aead};
use hpcrypt::rng::OsRng;

// Generate random key and nonce
let key = OsRng::generate_bytes::<32>();
let nonce = OsRng::generate_bytes::<12>();

// Encrypt
let cipher = Aes256Gcm::new(&key);
let plaintext = b"Secret message";
let ciphertext = cipher.encrypt(&nonce, plaintext, &[])?;

// Decrypt
let recovered = cipher.decrypt(&nonce, &ciphertext, &[])?;
assert_eq!(recovered, plaintext);
```

### Ed25519 Digital Signatures

```rust
use hpcrypt::curves::Ed25519;
use hpcrypt::rng::OsRng;

// Generate keypair
let private_key = OsRng::generate_bytes::<32>();
let public_key = Ed25519::public_key(&private_key);

// Sign message
let message = b"Important message";
let signature = Ed25519::sign(&private_key, message);

// Verify signature
assert!(Ed25519::verify(&public_key, message, &signature));
```

### ML-DSA Post-Quantum Signatures

```rust
use hpcrypt_mldsa::{MlDsa65, keygen::keygen};

// Generate post-quantum keypair
let (pk, sk) = keygen::<MlDsa65>();

// Sign message
let message = b"Future-proof signature";
let signature = sk.sign(message)?;

// Verify signature
assert!(pk.verify(message, &signature));
```

### Password Hashing with Argon2

```rust
use hpcrypt::kdf::Argon2id;

let password = b"user_password";
let salt = b"unique_salt_16bt";

// Hash password
let params = Argon2id::default_params();
let mut output = [0u8; 32];
Argon2id::hash(password, salt, &params, &mut output)?;

// Verify password
let mut verify = [0u8; 32];
Argon2id::hash(password, salt, &params, &mut verify)?;
assert_eq!(output, verify);
```

## Supported Algorithms

### Hash Functions

- **SHA-2 Fam