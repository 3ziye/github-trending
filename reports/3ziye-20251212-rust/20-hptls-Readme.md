# HPTLS - High-Performance TLS Library

[![CI](https://github.com/seceq/hptls/workflows/CI/badge.svg)](https://github.com/seceq/hptls/actions/workflows/ci.yml)
[![Security Audit](https://github.com/seceq/hptls/workflows/Security%20Audit/badge.svg)](https://github.com/seceq/hptls/actions/workflows/security.yml)
[![codecov](https://codecov.io/gh/seceq/hptls/branch/master/graph/badge.svg)](https://codecov.io/gh/seceq/hptls)
[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](LICENSE)
[![Rust Version](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org)

A modern, high-performance TLS 1.3 library written in Rust with post-quantum cryptography support and FIPS-validated implementations.

## Overview

HPTLS is a production-ready TLS library designed for security, performance, and modern cryptographic standards. It provides complete TLS 1.3 client and server implementations with optional TLS 1.2 backward compatibility, post-quantum cryptography (PQC), and hardware acceleration support.

### Key Features

- **TLS 1.3** - Full RFC 8446 implementation with all cipher suites
- **TLS 1.2** - Backward compatibility for legacy systems
- **Post-Quantum Cryptography** - ML-KEM, ML-DSA, SLH-DSA (FIPS 203-205)
- **Hybrid KEX** - X25519+ML-KEM-768 for quantum-resistant security
- **FIPS 140-3** - FIPS-validated cryptographic implementations
- **Zero-Copy I/O** - Optimized for high-throughput applications
- **Memory Safe** - Written in pure Rust with no unsafe code in core logic
- **Pluggable Crypto** - Abstract crypto provider interface

## Architecture

### Layered Design

```
┌─────────────────────────────────────────────────────────┐
│                        hptls                            │
│         (High-level API - Client/Server builders)       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                     hptls-core                          │
│    (Protocol implementation - State machines, I/O)      │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                    hptls-crypto                         │
│          (Abstract crypto trait definitions)            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│               hptls-crypto-hpcrypt                      │
│     (FIPS-validated crypto using HPCrypt)                │
└─────────────────────────────────────────────────────────┘
```

### Crypto Abstraction

HPTLS uses a pluggable crypto provider architecture:

- **hptls-crypto** - Defines traits for all cryptographic operations
- **hptls-crypto-hpcrypt** - Production implementation using HPCrypt (FIPS 140-3 validated)
- Custom providers can be implemented by third parties

## Supported Features

### TLS Protocol Support

| Feature | Status | RFC |
|---------|--------|-----|
| TLS 1.3 | Complete | RFC 8446 |
| TLS 1.2 | Complete | RFC 5246 |
| DTLS 1.3 | Complete | RFC 9147 |
| QUIC Integration | Complete | RFC 9001 |

### Cipher Suites

**TLS 1.3:**
- TLS_AES_128_GCM_SHA256
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256

**TLS 1.2:**
- TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
- TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
- TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
- TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
- TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
- TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256

### Key Exchange

**Classical:**
- X25519 (Curve25519)
- secp256r1 (P-256)
- secp384r1 (P-384)

**Post-Quantum:**
- ML-KEM-768 (FIPS 203)
- ML-KEM-1024 (FIPS 203)

**Hybrid:**
- X25519+ML-KEM-768 (Recommended)
- P-256+ML-KEM-768

### Signature Algorithms

**Classical:**
- ECDSA (P-256, P-384, P-521)
- Ed25519 (EdDSA)
- RSA-PSS (2048, 3072, 4096 bits)

**Post-Quantum:**
- ML-DSA-65 (FIPS 204)
- ML-DSA-87 (FIPS 204)
- SLH-DSA (FIPS 205)

### Extensions

- Server Name Indication (SNI)
- Application-Layer Protocol Negotiation (ALPN)
- Supported Groups
- Signature Algorithms
- Key Share
- Pre-Shared Key (PSK)
- Early Data (0-RTT)
- Session Tickets
- Encrypted Client Hello (ECH) - Core cryptography complete
- GREASE (RFC 8701)

## Quick Start

### Client Example

```rust
use hptls::{ClientConfig, TlsConnector};
use std::net::TcpStream;
use std::io::{Read, Write};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create client configuration
    let config = ClientConfig::builder()
        .with_cipher_suites(vec![
            CipherSuite::Aes128GcmSha256,
            CipherSuite::ChaCha20Poly1305Sha256,
        ])
        .with_key_exchange(vec![
            KeyExchange::X25519,
            KeyExchange::Secp256r1,
        ])
        .build()?;

    // Connect to server
    let stream = TcpStream::connect("example.com:443"