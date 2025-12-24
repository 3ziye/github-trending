# Jsync by Fizzed

[![Maven Central](https://img.shields.io/maven-central/v/com.fizzed/jsync?style=flat-square)](https://mvnrepository.com/artifact/com.fizzed/jsync)

## Automated Testing

The following Java versions and platforms are tested using GitHub workflows:

[![Java 8](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java8.yaml?branch=master&label=Java%208&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java8.yaml)
[![Java 11](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java11.yaml?branch=master&label=Java%2011&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java11.yaml)
[![Java 17](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java17.yaml?branch=master&label=Java%2017&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java17.yaml)
[![Java 21](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java21.yaml?branch=master&label=Java%2021&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java21.yaml)
[![Java 25](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java25.yaml?branch=master&label=Java%2025&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java25.yaml)

[![Linux x64](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/linux-java8.yaml?branch=master&label=Linux%20x64&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/linux-java8.yaml)
[![MacOS arm64](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/macos-arm64.yaml?branch=master&label=MacOS%20arm64&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/macos-arm64.yaml)
[![Windows x64](https://img.shields.io/github/actions/workflow/status/fizzed/jsync/windows-x64.yaml?branch=master&label=Windows%20x64&style=flat-square)](https://github.com/fizzed/jsync/actions/workflows/windows-x64.yaml)

The following platforms are tested using the [Fizzed, Inc.](http://fizzed.com) build system:

[![Alpine x64](https://img.shields.io/badge/Alpine_x64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![Alpine arm64](https://img.shields.io/badge/Alpine_arm64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![Alpine riscv64](https://img.shields.io/badge/Alpine_riscv64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![FreeBSD x64](https://img.shields.io/badge/FreeBSD_x64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![FreeBSD arm64](https://img.shields.io/badge/FreeBSD_arm64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![Linux arm64](https://img.shields.io/badge/Linux_arm64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![Linux riscv64](https://img.shields.io/badge/Linux_riscv64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![MacOS x64](https://img.shields.io/badge/MacOS_x64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![NetBSD x64](https://img.shields.io/badge/MacOS_x64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![OpenBSD x64](https://img.shields.io/badge/OpenBSD_x64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![OpenBSD arm64](https://img.shields.io/badge/OpenBSD_arm64-passing-brightgreen?style=flat-square)](buildx-results.txt)
[![Windows arm64](https://img.shields.io/badge/Windows_arm64-passing-brightgreen?style=flat-square)](buildx-results.txt)

## Overview

Pure Java library (8, 11, 17, 21, 25, etc.) for providing rsync-like efficient file synchronization between two directories
or files either locally or remotely via SSH/SFTP. Requires no native dependencies, works on all major platforms including Windows,
and requires no special executables present on the remote system.

## Features
 - Supports all platforms that Java can run on, including Windows
 - Diff-based Syncing: Only transfers files that have changed (based on size, modification time, or checksum).
 - Local: Sync between local directories.
 - SSH/SFTP: Sync between local and remote servers (via SSH/SFTP).
 - Zero-Dependency Core: The core logic is separated from protocol implementations to keep the footprint small.
 - Builder API: Fluent, easy-to-use Java API for configuring sync jobs.
 - Supports syncing file and directory permissions
 - Does NOT require rsync to be installed on either system, uses SFTP for file operations on the remote system,
along with using SSH for checksums if needed.
 - Leverages the excellent [Jsch](https://github.com/mwiede/jsch) library for SSH/SFTP support (but designed to pluggable
and support other SSH/SFTP implementations in the future)

## Command-Line Tool / Example

This library is optimized primarily for programmatic use, but if you'd like to simply use it from the command-line,
or to quickly give it a try, we suggest trying it out from within the [Blaze Script System](https://github.com/fizzed/blaze)