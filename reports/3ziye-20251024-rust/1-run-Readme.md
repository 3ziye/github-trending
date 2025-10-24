<h1 align="center">run</h1>

<p align="center">
	<strong>Polyglot command runner & smart REPL that lets you script, compile, and iterate in 25+ languages without touching another CLI.</strong>
</p>

<p align="center">
  <!-- Release -->
  <a href="https://github.com/Esubaalew/run/releases/latest">
    <img src="https://img.shields.io/github/v/release/Esubaalew/run?style=flat-square&color=orange&logo=github" alt="Latest release" />
  </a>

  <!-- Release status -->
  <img src="https://img.shields.io/badge/release-passing-brightgreen?style=flat-square" alt="Release passing" />

  <!-- Docs -->
  <a href="https://docs.rs/run-kit">
    <img src="https://img.shields.io/badge/docs-passing-brightgreen?style=flat-square&logo=rust" alt="Docs passing" />
  </a>

  <!-- Crates.io -->
  <a href="https://crates.io/crates/run-kit">
    <img src="https://img.shields.io/crates/v/run-kit.svg?style=flat-square&logo=rust&color=red" alt="crates.io" />
  </a>

  <!-- Downloads -->
  <a href="https://github.com/Esubaalew/run/releases">
    <img src="https://img.shields.io/github/downloads/Esubaalew/run/total?style=flat-square&color=blue" alt="Downloads" />
  </a>

  <!-- Stars -->
  <a href="https://github.com/Esubaalew/run/stargazers">
    <img src="https://img.shields.io/github/stars/Esubaalew/run?style=flat-square&color=yellow" alt="GitHub stars" />
  </a>

  <!-- Platforms -->
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square" alt="Platform support" />

  <!-- License -->
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License" />
  </a>
</p>

<p align="center">
	<a href="https://run.esubalew.et/">Website</a>
	•
	<a href="https://run.esubalew.et/docs/overview">Docs Overview</a>
</p>

> Built in Rust for developers who live in multiple runtimes. `run` gives you a consistent CLI, persistent REPLs, and batteries-included examples for your favorite languages.

---

<details>
<summary><strong>Table of contents</strong></summary>

- [Website and Docs](#website-and-docs)
- [Overview](#overview---universal-multi-language-runner)
  - [What is run?](#what-is-run)
  - [Who is this for?](#who-is-this-for)
  - [Why was run created?](#why-was-run-created)
  - [Why Rust?](#why-rust)
- [Highlights](#-highlights)
- [Quickstart](#-quickstart)
- [Installation](#-installation)
- [How it works](#-how-it-works)
- [Supported languages](#-supported-languages)
  - [Complete Language Aliases Reference](#complete-language-aliases-reference)
- [Command Variations - Flexible Syntax](#command-variations---flexible-syntax)
- [Command-Line Flags Reference](#command-line-flags-reference)
- [⚠️ When to Use --lang (Important!)](#️-when-to-use---lang-important)
- [Main Function Flexibility](#main-function-flexibility)
- [Examples](#-examples)
- [REPL](#-repl)
  - [Interactive REPL - Line by Line or Paste All](#interactive-repl---line-by-line-or-paste-all)
  - [Variable Persistence & Language Switching](#variable-persistence--language-switching)
  - [REPL Commands](#repl-commands)
- [Stdin Piping Examples](#stdin-piping-examples)
- [Language-Specific Notes](#language-specific-notes)
- [📄 License](#-license)

</details>

---

# Website and Docs

The official website and full documentation are available here:

- Website: https://run.esubalew.et/
- Docs Overview: https://run.esubalew.et/docs/overview

Use these links to explore features, language guides, and detailed examples.

---

# Overview - Universal Multi-Language Runner

A powerful command-line tool for executing code in 25 programming languages

## What is run?

run is a universal multi-language runner and smart REPL (Read-Eval-Print Loop) written in Rust. It provides a unified interface for executing code across 25 programming languages without the hassle of managing multiple compilers, interpreters, or build tools.

Whether you're a beginner learning your first programming language or an experienced polyglot developer, run streamlines your workflow by providing consistent commands and behavior across all supported languages.

## Who is this for?

• Beginners: Learn programming without worrying about complex setup procedures. Just install run and start coding in any language.

• Students: Quickly test code snippets and experiment with different programming paradigms across multiple languages.

• Developers: Prototype ideas rapidly, test algorithms, and switch between languages seamlessly without context switching.

• DevOps Engineers: Write and test automation scripts in various languages from a single tool.

• Educators: Teach programming concepts across multiple languages with a consistent interface.

## Why was run created?

Traditional development workflows require installing and configuring separate tools for each programming language. This creates several problems:

• Time-consuming setup: Installing compilers, interpreters, package managers, and configuring environments 