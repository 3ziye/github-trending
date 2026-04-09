# FLARE Learning Hub
![FLARE Learning Hub Logo](./.github/logo.png)

The FLARE Learning Hub freely distributes quality reverse engineering and malware analysis educational content from the [FLARE team](https://cloud.google.com/security/flare).

The FLARE Learning Hub modules are hosted as web-published Google Docs, which are linked in the respective descriptions below. This repository contains all corresponding artifacts for each module, including lab exercise and demonstration binaries, disassembler databases, and scripts.

Refinements to existing modules and new modules will be published on an ongoing basis.

## Available Modules
* [Malware Analysis Crash Course](#malware-analysis-crash-course)
* [The Go Reverse Engineering Reference](#the-go-reverse-engineering-reference)
* [An Introduction to Time Travel Debugging](#an-introduction-to-time-travel-debugging)

## Getting Started
To start working on a module, we **strongly recommend** setting up a safely isolated virtual machine (VM) environment using [FLARE-VM](https://github.com/mandiant/flare-vm), which provides the tools necessary to complete the lab exercises and demonstrations. We also recommend using a virtualization product that supports snapshots, which allows you to record the VM in a clean state and revert to that state when starting a new analysis. All modules currently only support Intel x86-64 environments.

### Working with Distributed Binaries
While all distributed binaries and scripts are crafted for the sole purpose of hands-on exercise and demonstration, they may be flagged as malicious by automated systems as some exhibit malware-like behavior. **This project is not responsible for any damage or loss resulting from executing the binaries and scripts outside of a secured, isolated virtual machine environment.**

The password for any password-protected ZIPs in this repository is `flare`.

## [Malware Analysis Crash Course](https://docs.google.com/document/d/1I83PHeEImWacuQut02VBlkJ2-CJcuTYmt6mxa_xGqlA)
**Authors: Jae Young Kim and Nick Harbour**

**Module Link: [Malware Analysis Crash Course](https://docs.google.com/document/d/1I83PHeEImWacuQut02VBlkJ2-CJcuTYmt6mxa_xGqlA)**

**Module Directory**: `/macc`

As static analysis tools and sandbox products continue to progress, they provide increasingly valuable information about malware binaries. However, when reliability and accuracy are critical, making definitive statements about a malware sample still necessitates a comprehensive understanding of the program through manual reverse engineering.

This is a crash course on reading, interpreting, and manipulating assembly code, which remains the cornerstone of a reverse engineer’s skill set. By the end of this training, you will have developed the practical skills necessary to begin analyzing typical Windows malware samples.

The course starts with the basics of x86 assembly and gradually introduces higher-level programming constructs. It also includes the essential Windows knowledge required to begin reversing Windows-based malware.

Emphasizing a learn-by-doing approach, the course progression weaves in numerous assembly hacking exercises. We believe the repetition of writing assembly and debugging the results is the most effective way to quickly master the fundamentals needed to reverse larger, complex programs. The course also features flash quizzes as well as multiple labs with detailed solutions.

## [The Go Reverse Engineering Reference](https://docs.google.com/document/d/1AG76FBur7aagm36o-hNbny1X1Q3_IGHEjbP-JDsrJH4)
**Authors: Jae Young Kim**

**Module Link: [The Go Reverse Engineering Reference](https://docs.google.com/document/d/1AG76FBur7aagm36o-hNbny1X1Q3_IGHEjbP-JDsrJH4)**

The Go Reverse Engineering Reference is a comprehensive reference for reverse engineering Go executables. The reference consists of three sections:

* **Language Reference**: The Language Reference section breaks down each Go language feature and examines how the compiler implements it at the assembly level.  
* **Runtime Reference**: The Runtime Reference section covers key Go runtime topics (including program initialization, runtime type descriptors, and write barriers) and provides an exhaustive list of compiler-emitted runtime functions with contextual explanations.  
* **Executable Reference**: The Executable Reference section covers the structure and layout of a Windows Go executable with the goal of identifying and contextualizing every type of data and metadata in a binary.

All material in this reference is currently restricted to Windows AMD64 executables compiled with [Go version 1.24.0](https://github.com/golang/go/tree/go1.24.0).

## [An Introduction to Time Travel Debugging](https://docs.google.com/document/d/15gbXsTtWyxlUr5bxWO0wvWNHDZqxqh_LEqLanyZpdyw)
**Authors: Josh Stroschein and Jae Young Kim**

**Module Link: [An Introduction to Time Travel Debugging](https://docs.google.com/document/d/15gbXsTtWyxlUr5bxWO0wvWNHDZqxqh_LEqLanyZpdyw)**

**Modu