# FastCtx

**English** | [简体中文](./README.zh-CN.md)

### Fast, context-efficient repository tools for AI agents.

FastCtx is a local Rust tool runtime. It provides file reading, content search, file discovery, batch replacement, and Bash command execution through MCP.

Repository operations run in a persistent process with stable input schemas and output formats. The model can gather the context it needs in fewer steps and spend more attention on understanding code, planning changes, and verifying results.

```console
npm install --global fastctx
fastctx
```

The `fastctx` command opens the control terminal. Review the proposed changes, select **Apply**, then start a new ChatGPT / Codex session.

FastCtx currently provides first-class setup for ChatGPT App and Codex CLI. Any MCP client can also register `fastctx serve` directly.

## What FastCtx solves

Coding agents often assemble shell commands on the fly when they access a repository. They have to handle quotes, escaping, paths, and platform differences, then extract the useful information from terminal output. A simple file read or symbol search can take several tool calls just to confirm that the command is correct and the result is complete.

This work consumes context and reasoning. The model tracks the code problem and the tool mechanics at the same time: whether the PowerShell syntax is correct, whether a path was escaped correctly, whether the encoding produced mojibake, and whether the host truncated a long result. More tool overhead leaves less room for the repository itself.

FastCtx turns common repository operations into structured input and output. The model provides parameters such as a path, pattern, range, and mode. The Rust runtime handles command construction, directory traversal, encoding, pagination, and output boundaries.

The tools cover the main parts of a coding task:

- `read` reads text, images, PDFs, and raw bytes;
- `grep` searches file contents;
- `glob` finds files;
- `replace` performs mechanical batch replacement;
- `run`, `run_background`, `job_output`, `job_kill`, and `job_list` execute Bash commands and manage persistent long-running jobs.

This greatly reduces the attention the model spends on tool mechanics, such as checking whether a PowerShell command is correct. It improves context efficiency and helps tasks finish faster with better results.

## Installation

### Install with npm

Requires Node.js 18 or later:

```console
npm install --global fastctx
fastctx
```

The first launch opens the full-screen control terminal. The interface supports 17 languages and provides these main actions:

1. Adjust the output tier;
2. Keep grep/glob on automatic CPU parallelism or set an explicit core limit;
3. Enable **Bash terminal** when needed;
4. Set current-user background-job storage, concurrency, and AI list page limits;
5. Inspect every currently running job across FastCtx sessions, follow its output, and stop it on the **Jobs** screen;
6. Reset all user preferences to factory defaults through a confirmation screen;
7. Review every host configuration change on the Apply screen, apply it, and restart the ChatGPT / Codex session.

Apply copies the current binary to `~/.fastctx/bin/` and points the host configuration at that stable path. The applied setup keeps working after npm cache cleanup or upgrades.

The full-screen terminal opens immediately while FastCtx checks its launch channel in a background thread. Successful results are cached for 24 hours in machine-private storage outside `~/.fastctx`. npm launches query the exact launcher package through a fresh isolated cache with `--prefer-online`; direct GitHub Release executables read the stable tag from GitHub's `releases/latest` web redirect. Available updates remain visible from the main menu and open a dedicated screen with **Update & restart** and **Continue**.

If GitHub has published a release but npm has not exposed the matching version yet, FastCtx shows a propagation screen instead of trusting stale metadata. **Retry** always uses another isolated cache; it never clears or mutates the user's normal npm cache. Transient network or rate-limit failures stay quiet and are recorded under **Status**; malformed publication metadata produces one warning. Status also offers a manual check that bypasses the 24-hour TTL. An accepted npm update installs the exact version with lifecycle scripts disabled. A GitHub Release update downloads this repository's platform archive and aggregate `SHA256SUMS`, verifies the archive before safely extracting the binary, probes the downloaded version, replaces the executable atomically, and rolls back when restart health fails. A failed npm update restores the exact previous package version; every failed update reopens the previous TUI with a warning. After a successful restart, an owned `~/.fastctx/bin/` Apply copy is synchronized; externally changed copies are left untouched.

`cargo install` builds and the internal `~/.fastctx/bin/` runt