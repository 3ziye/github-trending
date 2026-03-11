![AndroHunter](images/banner.png)

# AndroHunter

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android-brightgreen?style=for-the-badge&logo=android"/>
  <img src="https://img.shields.io/badge/Language-Kotlin-purple?style=for-the-badge&logo=kotlin"/>
  <img src="https://img.shields.io/badge/Min_SDK-29_(Android_10)-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Version-4.0-00FF88?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  <b>A comprehensive Android security research toolkit for bug bounty hunters and mobile penetration testers.</b><br/>
  Built with Jetpack Compose · Dark terminal UI · On-device analysis
</p>

---

## ⚠️ Legal Disclaimer

> **AndroHunter is intended for authorized security research, bug bounty programs, and educational purposes only.**
> You must have explicit permission from the application owner before testing any target.
> The developer assumes no responsibility for misuse. Always comply with your bug bounty program's scope and rules of engagement.

---

## Overview

AndroHunter is a native Android application that provides a full suite of mobile security testing tools — all running directly on the device without requiring a rooted phone for most features. It is designed for security researchers participating in bug bounty programs (HackerOne, Yes We Hack, Intigriti, etc.) who need to analyze Android applications quickly and efficiently.

The tool covers the entire Android attack surface: static analysis (APK, DEX, Manifest), dynamic testing (Intent fuzzing, ContentProvider probing, Broadcast injection), runtime analysis (Frida script generation, SSL bypass), and network interception (HTTP proxy).

---

## Features

### 📱 App Explorer
- Lists all installed applications with metadata (package name, version, permissions, target SDK)
- Filter by system/user apps
- Quick navigation to any analysis module from the app detail view

### 🔍 DEX Analyzer
- Extracts and analyzes `.dex` files from APKs
- Scans for hardcoded secrets: API keys, tokens, passwords, URLs, private keys
- String pattern matching with severity classification (`VULN` / `SUSP` / `SAFE`)
- Class and method enumeration with popup viewer
- Supports multi-dex APKs — each DEX file analyzed separately

### 📄 Manifest Viewer
- Parses `AndroidManifest.xml` directly from the APK (no decompiler needed)
- Three-tab view: **Components**, **Permissions**, **Raw XML**
- Highlights exported components, dangerous permissions, and deep link schemes
- Identifies potential attack surface (exported Activities, Services, Receivers, Providers)

### 🎯 Intent Fuzzer
- Lists all exported Activities, Services, and Broadcast Receivers of the target app
- Sends crafted Intents with custom extras, data URIs, and categories
- Supports path traversal payloads via Intent data (`file:///data/...`)
- Integrates with Payload Engine for automated testing

### 💥 Payload Engine
- Logcat-based real-time result monitoring
- Automated payload delivery to target components
- Visual result classification: `VULN` (red) / `SUSP` (yellow) / `SAFE` (green)
- Supports deeplink exploitation, OAuth redirect hijacking, file URI leaks

### 🗄️ Content Provider Fuzzer
- Enumerates all exported ContentProviders of the target application
- Tests 9 SQL injection payloads per provider (Error-based, Boolean, UNION, Time-based)
- Detects readable/writable providers and schema exposure
- One-tap navigation from APK Analyzer findings to Provider Fuzzer with pre-filled target

### 📁 FileProvider Path Analyzer
- Parses `res/xml/` configuration files from APK to extract FileProvider path definitions
- Risk classification per path type:
  - `root-path` with empty path → **CRITICAL** (full filesystem access)
  - `external-path` with empty path → **HIGH**
  - `cache-path` / `external-cache-path` → **MEDIUM**
- **Path Traversal Tester**: automated testing with 9 traversal payloads
- Attempts actual file reads via `ContentResolver` and reports file contents on success
- **ADB Commands tab**: ready-to-use `adb shell content read --uri '...'` commands

### 🏃 Activity Launcher
- Lists all Activities of any installed app with exported status badge
- One-tap launch with optional extra data / deep link injection
- ADB command generator: `adb shell am start -n pkg/activity --es data "payload"`
- Filter by exported-only for quick attack surface identification

### 📡 Broadcast Fuzzer
- 10 pre-built broadcast payloads across 6 categories:
  - **Auth**: Login bypass, Session hijack
  - **SQLi**: SQL injection via Intent extras
  - **LFI**: Path traversal via file path extras
  - **Redirect**: Open redirect, Deep link hijack
  - **PrivEsc**: Privilege escalation, Component enable
  - **Exfil**: Data exfiltration via backup intent
- Custom broadcast sender: specify action + key=value extras
- ADB command copy for each payload

### 🔑 Shared Preferences Reader
- Reads `shared_p