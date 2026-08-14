# FastCtx

**English** | [简体中文](./README.zh-CN.md)

### Fast, context-efficient repository tools for AI agents.

FastCtx is a local Rust tool runtime. It provides file reading, content search, file discovery, batch replacement, and Bash command execution through MCP.

Repository operations run in a persistent process with stable input schemas and output formats. The model can gather the context it needs in fewer steps and spend more attention on understanding code, planning changes, and verifying results.

Each `fastctx serve` process is a thin stdio proxy. Proxies for the same user and FastCtx build share one private local control center, including its search executor and global admission limits, while every MCP connection keeps its own working directory, native environment, cancellation state, and background-output cursor. The control center never disconnects a live proxy; after the last proxy disconnects, it exits once ten minutes have passed with no active request and no running background job. If the private control center cannot start or accept a session, the proxy reports the problem and falls back to a complete standalone server before consuming MCP input.

```console
npm install --global fastctx
fastctx
```

The `fastctx` command opens the control terminal. Review the proposed changes, select **Connect to Codex**, then start a new ChatGPT / Codex session.

FastCtx currently provides first-class setup for ChatGPT App and Codex CLI. Any MCP client can also register `fastctx serve` directly.

## What FastCtx solves

Coding agents often assemble shell commands on the fly when they access a repository. They have to handle quotes, escaping, paths, and platform differences, then extract the useful information from terminal output. A simple file read or symbol search can take several tool calls just to confirm that the command is correct and the result is complete.

This work consumes context and reasoning. The model tracks the code problem and the tool mechanics at the same time: whether the PowerShell syntax is correct, whether a path was escaped correctly, whether the encoding produced mojibake, and whether the host truncated a long result. More tool overhead leaves less room for the repository itself.

FastCtx turns common repository operations into structured input and output. The model provides parameters such as a path, pattern, range, and mode. The Rust runtime handles command construction, directory traversal, encoding, pagination, and output boundaries.

The tools cover the main parts of a coding task:

- `inspect_local_file` reads text, images, PDFs, and raw bytes;
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

1. Adjust the output tier and provider-aware output protection;
2. Keep grep/glob on automatic CPU parallelism or set an explicit core limit;
3. Enable **Bash terminal** when needed;
4. Set current-user background-job storage, concurrency, and AI list page limits;
5. Inspect every currently running job across FastCtx sessions, follow its output, and stop it on the **Jobs** screen;
6. Reset all user preferences to factory defaults through a confirmation screen;
7. Review every host configuration change on the Connect to Codex screen, confirm it, and restart the ChatGPT / Codex session.

Connecting copies the current binary to `~/.fastctx/bin/` and points the host configuration at that stable path. The connected setup keeps working after npm cache cleanup or upgrades.

On launch, FastCtx checks its launch channel for updates before the main menu opens. A brief checking screen appears and the wait is strictly bounded: if the check cannot finish — offline, timeout, rate limiting — FastCtx enters silently, and the dedicated **Update** screen still offers a manual check at any time. When a newer version is installable, the update screen opens directly and asks whether to **Update & restart** or **Continue** into the current version. Successful results are cached for 24 hours in machine-private storage outside `~/.fastctx`, so most launches skip the network entirely. npm launches query the exact launcher package through a fresh isolated cache with `--prefer-online`; direct GitHub Release executables read the stable tag from GitHub's `releases/latest` web redirect.

If GitHub has published a release but npm has not exposed the matching version yet, FastCtx