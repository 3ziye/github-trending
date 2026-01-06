# witr (why-is-this-running)

<img width="631" height="445" alt="witr" src="https://github.com/user-attachments/assets/e51cace3-0070-4200-9d1f-c4c9fbc81b8d" />

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Goals](#2-goals)
- [3. Core Concept](#3-core-concept)
- [4. Supported Targets](#4-supported-targets)
- [5. Output Behavior](#5-output-behavior)
- [6. Flags & Options](#6-flags--options)
- [7. Example Outputs](#7-example-outputs)
- [8. Installation](#8-installation)
  - [8.1 Script Installation (Recommended)](#81-script-installation-recommended)
  - [8.2 Homebrew (macOS & Linux)](#82-homebrew-macos--linux)
  - [8.3 Conda (macOS & Linux)](#83-conda-macos--linux)
  - [8.4 Arch Linux (AUR)](#84-arch-linux-aur)
  - [8.5 Prebuilt Packages (deb, rpm, apk)](#85-prebuilt-packages-deb-rpm-apk)
  - [8.6 Go (cross-platform)](#86-go-cross-platform)
  - [8.7 Manual Installation](#87-manual-installation)
  - [8.8 Verify Installation](#88-verify-installation)
  - [8.9 Uninstallation](#89-uninstallation)
  - [8.10 Run Without Installation](#810-run-without-installation)
- [9. Platform Support](#9-platform-support)
- [10. Success Criteria](#10-success-criteria)

---

## 1. Purpose

**witr** exists to answer a single question:

> **Why is this running?**

When something is running on a system—whether it is a process, a service, or something bound to a port—there is always a cause. That cause is often indirect, non-obvious, or spread across multiple layers such as supervisors, containers, services, or shells.

Existing tools (`ps`, `top`, `lsof`, `ss`, `systemctl`, `docker ps`) expose state and metadata. They show _what_ is running, but leave the user to infer _why_ by manually correlating outputs across tools.

**witr** makes that causality explicit.

It explains **where a running thing came from**, **how it was started**, and **what chain of systems is responsible for it existing right now**, in a single, human-readable output.

---

## 2. Goals

### Primary goals

- Explain **why a process exists**, not just that it exists
- Reduce time‑to‑understanding during debugging and outages
- Work with zero configuration
- Be safe, read‑only, and non‑destructive
- Prefer clarity over completeness

### Non‑goals

- Not a monitoring tool
- Not a performance profiler
- Not a replacement for systemd/docker tooling
- Not a remediation or auto‑fix tool

---

## 3. Core Concept

witr treats **everything as a process question**.

Ports, services, containers, and commands all eventually map to **PIDs**. Once a PID is identified, witr builds a causal chain explaining _why that PID exists_.

At its core, witr answers:

1. What is running?
2. How did it start?
3. What is keeping it running?
4. What context does it belong to?

---

## 4. Supported Targets

witr supports multiple entry points that converge to PID analysis.

---

### 4.1 Name (process or service)

```bash
witr node
witr nginx
```

A single positional argument (without flags) is treated as a process or service name. If multiple matches are found, witr will prompt for disambiguation by PID.

---

### 4.2 PID

```bash
witr --pid 14233
```

Explains why a specific process exists.

---

### 4.3 Port

```bash
witr --port 5000
```

Explains the process(es) listening on a port.

---

## 5. Output Behavior

### 5.1 Output Principles

- Single screen by default (best effort)
- Deterministic ordering
- Narrative-style explanation
- Best-effort detection with explicit uncertainty

---

### 5.2 Standard Output Sections

#### Target

What the user asked about.

#### Process

Executable, PID, user, command, start time and restart count.

#### Why It Exists

A causal ancestry chain showing how the process came to exist.
This is the core value of witr.

#### Source

The primary system responsible for starting or supervising the process (best effort).

Examples:

- systemd unit (Linux)
- launchd service (macOS)
- docker container
- pm2
- cron
- interactive shell

Only **one primary source** is selected.

#### Context (best effort)

- Working directory
- Git repository name and branch
- Container name / image (docker, podman, kubernetes, colima, containerd)
- Public vs private bind

#### Warnings

Non‑blocking observations such as:

- Process is running as root
- Process is listening on a public interface (0.0.0.0 / ::)
- Restarted multiple times (warning only if above threshold)
- Process is using high memory (>1GB RSS)
- Process has been running for over 90 days

---

## 6. Flags & Options

```
--pid <n>         Explain a specific PID
--port <n>        Explain port usage
--short           One-line summary
--tree            Show full process ancestry tree
--json            Output result as JSON
--warnings        Show only warnings
--no-color        Disable colorized output
--env             Show only environment variables for the process
--help            Show this help message
--verbose         Show extended process information
```

A single positional argument (without flags) is 