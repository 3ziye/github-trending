<div align="center">

<img src="https://bountyyfi.s3.eu-north-1.amazonaws.com/lonkero.png" alt="Lonkero Logo" width="200"/>

### Wraps around your attack surface

Professional-grade scanner for real penetration testing. Fast. Modular. Rust.

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Proprietary-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-green.svg)](https://github.com/bountyyfi/lonkero)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/bountyyfi/lonkero)
[![Coverage](https://img.shields.io/badge/coverage-95%25-success.svg)](https://github.com/bountyyfi/lonkero)

**90+ Advanced Scanners** | **16 Premium Features** | **Smart AI Filtering** | **5% False Positives**

**[Official Website](https://lonkero.bountyy.fi/en)** | [Features](#core-capabilities) · [Installation](#installation) · [Quick Start](#quick-start) · [Architecture](#architecture)

---

</div>

## What is Lonkero?

Lonkero is a production-grade web security scanner designed for professional security testing:

- Near-zero false positives (5% vs industry 20-30%)
- Intelligent testing - Skips framework internals, focuses on real vulnerabilities
- Modern stack coverage - Next.js, React, GraphQL, gRPC, WebSocket, HTTP/3
- 80% faster scans - Smart parameter filtering eliminates noise
- Advanced blind vulnerability detection techniques

Unlike generic scanners that spam thousands of useless payloads, Lonkero uses context-aware filtering to test only what matters.

---

## Core Capabilities

### 91 Security Scanners

| Category | Scanners | Focus Areas |
|----------|----------|-------------|
| **Injection** | 25 scanners | SQLi, XSS, XXE, NoSQL, Command, LDAP, XPath, SSRF, Template, HTML |
| **Authentication** | 18 scanners | JWT, OAuth, SAML, MFA, Session, Auth Bypass, IDOR, Privilege Escalation |
| **API Security** | 14 scanners | GraphQL, gRPC, REST, WebSocket, Rate Limiting, CORS, HTTP/3 |
| **Frameworks** | 11 scanners | Next.js, React, Django, Laravel, WordPress, Drupal, Express |
| **Configuration** | 13 scanners | Headers, SSL/TLS, Cloud, Containers, WAF Bypass, CSRF |
| **Business Logic** | 6 scanners | Race Conditions, Payment Bypass, Workflow Manipulation |
| **Info Disclosure** | 8 scanners | Sensitive Data, Debug Leaks, Source Code, JS Secrets |
| **Specialized** | 6 scanners | CVE Detection, Version Mapping, ReDoS |

### Smart Scanning Features

- **Parameter Filtering** - Skips framework internals, prioritizes user input (80% faster scans)
- **Blind Detection** - Time-based, error-based, boolean-based techniques
- **Context-Aware** - Adapts testing based on detected technology stack

### Enterprise Integration

- **Compliance** - OWASP Top 10 2025, PCI DSS, GDPR, NIS2, DORA
- **CI/CD** - GitHub Actions, GitLab SAST, SARIF output
- **Reporting** - PDF, HTML, JSON, XLSX, CSV, SARIF, Markdown formats with detailed remediation

---

## Architecture

### Scanning Pipeline

```mermaid
graph TB
    Start([Target URL]) --> Recon[Phase 0: Reconnaissance<br/>Tech Detection, Endpoint Discovery]

    Recon --> Filter{Smart Filter}
    Filter -->|Skip| Skip[Framework Internals]
    Filter -->|Test| Priority[Prioritized Parameters]

    Priority --> Injection[Phase 1: Injection<br/>SQLi, XSS, XXE, NoSQL<br/>Command, LDAP, XPath<br/>SSRF, Template, HTML]

    Injection --> Auth[Phase 2: Authentication<br/>JWT, OAuth, SAML<br/>Session, Cookie<br/>MFA, Password Reset]

    Auth --> AuthZ[Phase 3: Authorization<br/>IDOR, Privilege Escalation<br/>Client-side Route Bypass<br/>Mass Assignment]

    AuthZ --> Logic[Phase 4: Business Logic<br/>Race Conditions<br/>Payment/Discount Bypass<br/>Workflow Manipulation]

    Logic --> API[Phase 5: API Security<br/>GraphQL, gRPC, REST<br/>WebSocket, Rate Limiting<br/>CORS, Cache Poisoning]

    API --> Framework[Phase 6: Framework-Specific<br/>Next.js, React, Vue<br/>Laravel, Django, Rails<br/>WordPress, Drupal]

    Framework --> Config[Phase 7: Configuration<br/>Security Headers, SSL/TLS<br/>Debug Mode, Directory Listing<br/>Backup Files, Git Exposure]

    Config --> Info[Phase 8: Information Disclosure<br/>Sensitive Data Exposure<br/>Error Messages<br/>Source Code Leaks]

    Info --> Report[Generate Report<br/>JSON/HTML/SARIF]

    Report --> End([Scan Complete])

    style Filter fill:#ff6b6b
    style Injection fill:#e74c3c
    style Auth fill:#3498db
    style AuthZ fill:#9b59b6
    style Logic fill:#e67e22
    style API fill:#1abc9c
```

---

## Smart Parameter Filtering

### The Problem

Traditional scanners waste 95% of resources testing framework internals:

```
Testing: __react_state, _nextData, csrfToken, sessionId, timestamp, buildId...
Result: 2,800 requests, 0 vulnerabilities, 28 seconds
```

### The Solution

```mermaid
sequenceDiagram
    participant Scanner
    participant Filter as Smart Filter
    participant Target

    Scanner->>Fil