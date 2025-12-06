<div align="center">
  <a href="https://github.com/mixedbread-ai/mgrep">
    <img src="public/logo_mb.svg" alt="mgrep" width="96" height="96" />
  </a>
  <h1>mgrep</h1>
  <p><em>A calm, CLI-native way to semantically grep everything, like code, images, pdfs and more.</em></p>
  <a href="https://www.npmjs.com/package/@mixedbread/mgrep"><img src="https://badge.fury.io/js/@mixedbread%2Fcli.svg" alt="npm version" /></a>
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0" /></a><br>
  <a href="https://demo.mgrep.mixedbread.com"><img src="https://img.shields.io/badge/Playground-Try%20it%20now-brightgreen" alt="Playground: Try it now" /></a>

  <br>

  <p align="center">
    <video src="https://github.com/user-attachments/assets/7cb6d2ab-f96b-4092-9088-abbca85b0d52" controls="controls" style="max-width: 730px;">
      Your browser does not support the video tag.
    </video>
  </p>
</div>

## Why mgrep?
- Natural-language search that feels as immediate as `grep`.
- Semantic, multilingual & multimodal (audio, video support coming soon!)
- Smooth background indexing via `mgrep watch`, designed to detect and keep up-to-date everything that matters inside any git repository.
- Friendly device-login flow and first-class coding agent integrations.
- Built for agents and humans alike, and **designed to be a helpful tool**, not a restrictive harness: quiet output, thoughtful defaults, and escape hatches everywhere.
- Reduces the token usage of your agent by 2x while maintaining superior performance

```bash
# index once
mgrep watch

# then ask your repo things in natural language
mgrep "where do we set up auth?"
```

## Quick Start

1. **Install**
   ```bash
   npm install -g @mixedbread/mgrep    # or pnpm / bun
   ```

2. **Sign in once**
   ```bash
   mgrep login
   ```
   A browser window (or verification URL) guides you through Mixedbread authentication.

   **Alternative: API Key Authentication**
   For CI/CD or headless environments, set the `MXBAI_API_KEY` environment variable:
   ```bash
   export MXBAI_API_KEY=your_api_key_here
   ```
   This bypasses the browser login flow entirely.

3. **Index a project**
   ```bash
   cd path/to/repo
   mgrep watch
   ```
   `watch` performs an initial sync, respects `.gitignore`, then keeps the Mixedbread store updated as files change.

4. **Search anything**
   ```bash
   mgrep "where do we set up auth?" src/lib
   mgrep -m 25 "store schema"
   ```
   Searches default to the current working directory unless you pass a path.

**Today, `mgrep` works great on:** code, text, PDFs, images.  
**Coming soon:** audio & video.

## Using it with Coding Agents

`mgrep` supports assisted installation commands for many agents:
- `mgrep install-claude-code` for Claude Code
- `mgrep install-opencode` for OpenCode
- `mgrep install-codex` for Codex
- `mgrep install-droid` for Factory Droid

These commands sign you in (if needed) and add Mixedbread `mgrep` support to the
agent. After that you only have to start the agent in your project folder, thats
it.

### More Agents Coming Soon

More agents (Cursor, Windsurf, etc.) are on the way—this section will grow as soon as each integration lands.

## Making your agent smarter

We plugged `mgrep` into Claude Code and ran a benchmark of 50 QA tasks to evaluate the economics of `mgrep` against `grep`.

![mgrep benchmark](public/bench.jpg)

In our 50-task benchmark, `mgrep`+Claude Code used ~2x fewer tokens than grep-based workflows at similar or better judged quality.

`mgrep` finds the relevant snippets in a few semantic queries first, and the model spends its capacity on reasoning instead of scanning through irrelevant code from endless `grep` attempts. You can [Try it yourself](http://demo.mgrep.mixedbread.com).

*Note: Win Rate (%) was calculated by using an LLM as a judge.*

## Why we built mgrep

`grep` is an amazing tool. It's lightweight, compatible with just about every machine on the planet, and will reliably surface any potential match within any target folder.

But grep is **from 1973**, and it carries the limitations of its era: you need exact patterns and it slows down considerably in the cases where you need it most, on large codebases.

Worst of all, if you're looking for deeply-buried critical business logic, you cannot describe it: you have to be able to accurately guess what kind of naming patterns would have been used by the previous generations of engineers at your workplace for `grep` to find it. This will often result in watching a coding agent desperately try hundreds of patterns, filling its token window, and your upcoming invoice, with thousands of tokens. 

But it doesn't have to be this way. Everything else in our toolkit is increasingly tailored to understand us, and so should our search tools. `mgrep` is our way to bring `grep` to 2025, integrating all of the advances in semantic understanding and code-search, without sacri