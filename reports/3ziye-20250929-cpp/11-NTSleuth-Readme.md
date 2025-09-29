# 🔍 NTSleuth

<div align="center">

![NTSleuth Banner](https://img.shields.io/badge/NTSleuth-Windows%20Syscall%20Hunter-purple?style=for-the-badge&logo=windows&logoColor=white)

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](https://github.com/xaitax/NTSleuth/releases)
[![Platform](https://img.shields.io/badge/Platform-ARM64%20%7C%20x64%20%7C%20x86-orange?style=for-the-badge)](https://github.com/xaitax/NTSleuth)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-green?style=for-the-badge)](LICENSE)
[![C++](https://img.shields.io/badge/C++-20-red?style=for-the-badge&logo=cplusplus)](https://isocpp.org/)

**Comprehensive Windows Syscall Extraction & Analysis Framework**

*Discover every syscall. Resolve every parameter. Map the undocumented.*

If you find this research valuable, I'd appreciate a coffee:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M61EP5XL)

</div>

---

## ⚠️ Early Development Notice

> **Important**: This project is in early development. While functional and tested on multiple systems, it certainly has bugs and edge cases that haven't been discovered yet. I'm actively working on improvements and welcome feedback! Despite its early stage, I hope NTSleuth proves helpful for your Windows internals research and reverse engineering projects.
>
> Please report any issues you encounter - your feedback helps make this tool better for everyone!

## 🎯 What is NTSleuth?

NTSleuth is an advanced Windows syscall extraction and analysis framework that automatically discovers, documents, and analyzes system calls across all Windows architectures. It's a comprehensive reverse engineering tool that provides deep insights into Windows internals with high accuracy.

### 🚀 Key Achievements

- **2,400+ Syscalls Extracted** - Complete coverage of ntdll.dll and win32u.dll
- **1,100+ Function Signatures** - Integrated PHNT database from System Informer
- **3 Architectures Supported** - Native ARM64, x64, and x86 analysis
- **100% Automated** - From extraction to parameter resolution
- **< 4 Second Extraction** - Lightning-fast analysis engine

## ✨ Core Features

### 🔬 Syscall Extraction Engine
- **Multi-Architecture Disassembly** - ARM64 (SVC), x64 (SYSCALL), x86 (INT 2E/SYSENTER)
- **Complete Module Coverage** - ntdll.dll, win32u.dll, and WOW64 variants
- **Stub Analysis** - Extracts and analyzes syscall stub bytes
- **Alias Detection** - Identifies Nt/Zw function relationships
- **True Syscall Verification** - Distinguishes actual syscalls from regular exports

### 🧠 Advanced Parameter Resolution
- **PHNT Database Integration** - 1,100+ authoritative function signatures
- **SAL Annotation Support** - Complete _In_, _Out_, _Inout_, _opt_ preservation
- **Multi-Method Resolution**:
  - Primary: PHNT database lookup
  - Secondary: Pattern-based matching
  - Tertiary: Assembly code analysis
  - Quaternary: Heuristic inference
  - Quinary: Cross-reference learning
- **Confidence Scoring** - Reliability ratings for each resolution (0.0-1.0)

### 📊 Output Formats
- **JSON Export** - Structured data with complete metadata
- **C/C++ Headers** - Ready-to-use header files with prototypes
- **Interactive Lookup** - Query individual syscalls with rich formatting
- **Documentation Links** - Direct references to ntdoc.m417z.com

### 🛠️ Professional Features
- **Symbol Resolution** - Automatic PDB download from Microsoft Symbol Server
- **Local Caching** - Intelligent cache management for symbols and PHNT data
- **Offline Mode** - Works without internet after initial cache population

## 📸 Screenshots

```
    ███   ██ ████████ ███████ ██      ███████ ██   ██ ████████ ██  ██
    ████  ██    ██    ██      ██      ██      ██   ██    ██    ██  ██
    ██ ██ ██    ██    ███████ ██      █████   ██   ██    ██    ███████
    ██  ████    ██         ██ ██      ██      ██   ██    ██    ██  ██
    ██   ███    ██    ███████ ███████ ███████  ██████    ██    ██  ██


  +===================================================================+
  |  Windows Syscall Extraction & Automated Parameter Resolution Tool |
  |                 ARM64 | x64 | x86 Syscall Analysis                |
  |               v1.0.0 by Alexander Hagenah • @xaitax               |
  +===================================================================+

[*] INITIALIZATION

[+] Initializing NtSleuth Engine...
[+] Output directory: output
[+] Symbol cache: cache\symbols

[*] PARAMETER DATABASE

[+] Loading PHNT database for parameter resolution...
[+] PHNT database initialized with 1109 function signatures

[*] SYSCALL EXTRACTION

[+] Extracting syscalls from system modules...

[*] PARAMETER RESOLUTION

[+] Resolving parameters from PHNT database...
[+] Resolved parameters for 1103 syscalls from PHNT

[*] EXTRACTION RESULTS

> System Information
  * Target OS: 10.0.26220.5770 (ARM64)
  * Build: 26220.5770

> Syscall Statistics
  * Total syscalls found: 2461
    -> ntdll.dll: 978 total
    -> win32u