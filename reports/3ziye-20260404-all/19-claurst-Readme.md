<div align="center">

<h1>CLAURST</h1>
<h3><em>Your Favorite Terminal Coding Agent, now in Rust</em></h3>
<img src="public/Rustle.png" alt="Rustle the Crab" width="150" />


  <p>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Built_with-Rust-CE4D2B?style=for-the-badge&logo=rust&logoColor=white" alt="Built with Rust"></a>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Tracking-None-2E8B57?style=for-the-badge" alt="No Tracking"></a>
    <a href="https://github.com/kuberwastaken/claurst"><img src="https://img.shields.io/badge/Experimental_Features-Unlocked-6A0DAD?style=for-the-badge" alt="Experimental Features Unlocked"></a>
  </p>

  <br />

  <img src="public/screenshot.png" alt="CLAURST in action" width="1080" />
</div>

---

> [!NOTE]
> **100% Coverage complete from original source** on the [`src-rust`](https://github.com/kuberwastaken/claurst/tree/main/src-rust) and it's already much more memory effecient than the original port, along with no tracking, experimental features unlocked and more. We're at a stage where I'm using Claurst to further build Claurst in <2 days and it's incredibly exciting.
>
> A huge revision with multi provider support, many more features and optimisations is actively being worked on and will be pushed ideally by tomorrow :) I would love to hear thoughts, help you set up or squash any bugs you encounter in the process, please don't refrain from [reaching out](https://x.com/kuberwastaken) or [repoting any issues.](https://github.com/Kuberwastaken/claurst/issues/new) Thank you for your support !

---

# IMPORTANT NOTICE

This repository does not hold a copy of the proprietary Claude Code typescript source code.
This is a clean-room Rust reimplementation of Claude Code's behavior.

The process was explicitly two-phase:

Specification [`spec/`](https://github.com/kuberwastaken/claude-code/tree/main/spec) - An AI agent analyzed the source and produced exhaustive behavioral specifications and improvements, deviated from the original: architecture, data flows, tool contracts, system designs. No source code was carried forward.

Implementation [`src-rust/`](https://github.com/kuberwastaken/claude-code/tree/main/src-rust)- A separate AI agent implemented from the spec alone, never referencing the original TypeScript. The output is idiomatic Rust that reproduces the behavior, not the expression.

This mirrors the legal precedent established by Phoenix Technologies v. IBM (1984) — clean-room engineering of the BIOS — and the principle from Baker v. Selden (1879) that copyright protects expression, not ideas or behavior.

The analysis below is commentary on publicly available software, protected under fair use (17 U.S.C. § 107). Code excerpts are quoted to illustrate technical points from a public source - no unauthorized access was involved in this process or research.

# Claude Code's Entire Source Code Got Leaked via a Sourcemap in npm, Let's Talk About It

## Technical Breakdown

>**PS:** I've also published this [breakdown on my blog](https://kuber.studio/blog/AI/Claude-Code's-Entire-Source-Code-Got-Leaked-via-a-Sourcemap-in-npm,-Let's-Talk-About-it) with a better reading experience and UX :)

Earlier today (March 31st, 2026) - Chaofan Shou on X discovered something that Anthropic probably didn't want the world to see: the **entire source code** of Claude Code, Anthropic's official AI coding CLI, was sitting in plain sight on the npm registry via a sourcemap file bundled into the published package.

[![The tweet announcing the leak](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/leak-tweet.png)](https://raw.githubusercontent.com/kuberwastaken/claude-code/main/public/leak-tweet.png)

This repository is a backup of that leaked source, and this README is a full breakdown of what's in it, how the leak happened and most importantly, the things we now know that were never meant to be public.

Let's get into it.

## How Did This Even Happen?

This is the part that honestly made me go "...really?"

When you publish a JavaScript/TypeScript package to npm, the build toolchain often generates **source map files** (`.map` files). These files are a bridge between the minified/bundled production code and the original source, they exist so that when something crashes in production the stack trace can point you to the *actual* line of code in the *original* file, not some unintelligible line 1, column 48293 of a minified blob.

But the fun part is **source maps contain the original source code**. The actual, literal, raw source code, embedded as strings inside a JSON file.

The structure of a `.map` file looks something like this:

```json
{
  "version": 3,
  "sources": ["../src/main.tsx", "../src/tools/BashTool.ts", "..."],
  "sourcesContent": ["// The ENTIRE original source code of each file", "..."],
  "mappings