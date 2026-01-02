<div align="center">

<img src="https://bountyyfi.s3.eu-north-1.amazonaws.com/lonkero.png" alt="Lonkero Logo" width="200"/>

### Wraps around your attack surface

Professional-grade scanner for real penetration testing. Fast. Modular. Rust.

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Proprietary-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0-green.svg)](https://github.com/bountyyfi/lonkero)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/bountyyfi/lonkero)
[![Coverage](https://img.shields.io/badge/coverage-95%25-success.svg)](https://github.com/bountyyfi/lonkero)

**120+ Advanced Scanners** | **Intelligent Mode** | **ML Auto-Learning** | **Scanner Intelligence** | **5% False Positives**

**[Official Website](https://lonkero.bountyy.fi/en)** | [Features](#core-capabilities) · [Installation](#installation) · [Quick Start](#quick-start) · [ML Features](#machine-learning-features) · [Scanner Intelligence](#scanner-intelligence-system) · [Architecture](#architecture)

---

</div>

## What is Lonkero?

Lonkero is a production-grade web security scanner designed for professional security testing:

- **v3.0 Intelligent Mode** - Context-aware scanning with tech detection, endpoint deduplication, and per-parameter risk scoring
- **ML Auto-Learning** - Learns from every scan to reduce false positives over time (federated learning available)
- **Scanner Intelligence System** - Real-time scanner communication, Bayesian hypothesis testing, multi-step attack planning, and semantic response understanding
- Near-zero false positives (5% vs industry 20-30%)
- Intelligent testing - Skips framework internals, focuses on real vulnerabilities
- Modern stack coverage - Next.js, React, GraphQL, gRPC, WebSocket, HTTP/3
- 80% faster scans - Smart parameter filtering eliminates noise
- Advanced blind vulnerability detection techniques
- **When tech detection fails, we run MORE tests, not fewer** - fallback layer with 35+ scanners

Unlike generic scanners that spam thousands of useless payloads, Lonkero uses context-aware filtering to test only what matters.

---

## Core Capabilities

### v3.0 Intelligent Scanning Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: Universal Scanners (always run)                       │
│  CORS, Headers, SSL, OpenRedirect, HttpSmuggling, HostHeader    │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: Core Scanners (always run)                            │
│  XSS, SQLi, SSRF, CommandInjection, PathTraversal, IDOR, JWT    │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: Tech-Specific (when detected)                         │
│  NextJs, React, Django, Laravel, Express, WordPress...          │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: Fallback (when tech=Unknown → MORE tests)             │
│  35+ scanners: NoSQLi, XXE, Deserial, Log4j, Merlin, Cognito... │
└─────────────────────────────────────────────────────────────────┘
```

**Key insight**: When technology detection fails, the fallback layer runs MORE comprehensive tests to ensure nothing is missed.

### 120+ Security Scanners

| Category | Scanners | Focus Areas |
|----------|----------|-------------|
| **Injection** | 30 scanners | SQLi, XSS, DOM XSS, XXE, NoSQL, Command, LDAP, XPath, SSRF, Template, Prototype Pollution, Host Header, Log4j/JNDI, DOM Clobbering |
| **Authentication** | 26 scanners | JWT, OAuth, OIDC, SAML, MFA, 2FA Bypass, Session, Auth Bypass, IDOR, BOLA, Account Takeover, Password Reset Poisoning, Timing Attacks, Cognito Enum, Client Route Bypass |
| **API Security** | 20 scanners | GraphQL (advanced), GraphQL Batching, gRPC, REST, WebSocket, Rate Limiting, CORS, HTTP/3, Azure APIM, BFLA, API Versioning, OpenAPI Analyzer |
| **Frameworks** | 15 scanners | Next.js (route discovery), React, Django, Laravel, WordPress, Drupal, Joomla, Express, SvelteKit, Ruby on Rails, Spring Boot |
| **Configuration** | 17 scanners | Headers, CSP Bypass, SSL/TLS, Cloud, Containers, WAF Bypass, CSRF, DNS Security, Web Cache Deception, PostMessage Vulns |
| **Business Logic** | 8 scanners | Race Conditions, Payment Bypass, Workflow Manipulation, Mass Assignment (advanced), Timing Attacks |
| **Info Disclosure** | 11 scanners | Sensitive Data, Debug Leaks, Source Code, JS Secrets, Source Maps, Favicon Hash, HTML Injection |
| **Specialized** | 9 scanners | CVE Detection, Version Mapping, ReDoS, Google Dorking, Attack Surface Enum, Subdomain Takeover |

### Smart Scanning Features

- **Parameter Filtering** - Skips framework internals, prioritizes user input (80% faster scans)
- **Blind Detection** - Time-based, error-based, boolean-based techniques
- **Context-Aware** - Adapts testing based on detected technology stack
- **SPA Detection** - Id