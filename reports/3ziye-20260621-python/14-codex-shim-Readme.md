# codex-shim

Run **Codex Desktop** against any BYOK model you can describe in
`~/.codex-shim/models.json`, plus an optional passthrough to your **ChatGPT
subscription's Codex model** — without rebuilding Codex.

The shim is a local Python/aiohttp server that exposes an OpenAI
Responses-compatible endpoint on loopback. Codex points at the shim; the shim
routes each request to the matching upstream (OpenAI chat completions,
Anthropic Messages, a generic OpenAI-shaped chat endpoint, or ChatGPT Codex
passthrough), then translates streaming responses back into the shape Codex
expects.

> Tested on Codex Desktop **0.133.0-alpha.1** for macOS arm64. The shim server
> and routing layer are plain Python/aiohttp and work on Windows, macOS, Linux,
> WSL, and Git Bash. The only macOS-specific piece is the optional Desktop picker
> ASAR patch, needed when Codex hides custom catalog entries.

---

## What this gives you

Codex Desktop only shows models allowed by its server-side config. If you have
OpenAI / Anthropic / Z.ai / DeepSeek / Gemini / OpenRouter / local proxy models
you want as first-class picker entries, this wires them in locally.

The practical win is that Codex keeps its native UX while model routing moves
local:

- **BYOK models in the normal Codex picker.** No Codex rebuild, no request
  replay workflow.
- **Native Codex agent loops stay intact.** Function calls, tool outputs,
  reasoning blocks, image-capable models, shell-command metadata, and streaming
  SSE are translated instead of flattened into plain text.
- **ChatGPT/Codex passthrough.** If `~/.codex/auth.json` has a valid Codex
  access token, the shim can route Codex's native `/v1/responses` traffic to
  ChatGPT's Codex backend under the `gpt-5.5` slug used by current Codex builds.
- **Cursor/Composer passthrough.** If `cursor-agent login` is active, the shim
  exposes `composer-2-5` and routes through your Cursor subscription — no
  Dashboard API key (`crsr_…`) required. See
  [`docs/subscription-integration.md`](docs/subscription-integration.md).
- **Auto Router (optional).** Add an `Auto (smart routing)` picker entry that
  uses a cheap classifier model to route each task to the cheapest configured
  model that can handle it — trivial turns stay cheap, hard turns escalate. See
  [`docs/AUTO_ROUTER.md`](docs/AUTO_ROUTER.md).
- **Prompt-catching/proxy-friendly architecture.** Put a local proxy in front
  of the shim to dedupe boilerplate, inject stable instructions, repair
  pseudo-tool text, or route prompts by policy before they hit an upstream.
- **Maintainer-side wins on real coding-agent runs.** In the maintainer's
  internal Codex tasks, ChatGPT passthrough plus a prompt-catching proxy in
  front of the shim has produced multi-x reductions in billed input tokens
  and noticeably faster wall time vs. the baseline route. No reproducible
  benchmark script ships with the repo yet, so treat that as anecdata — the
  benchmark section below explains how to measure your own setup against
  an explicit oracle before quoting numbers.

---

## Requirements

- Python 3.11+.
- Codex CLI/Desktop installed and authenticated.
- One of:
  - `~/.codex-shim/models.json` with configured BYOK/upstream models;
  - a compatible JSON file passed with `--settings`;
  - `~/.codex/auth.json` containing `tokens.access_token` for ChatGPT/Codex
    passthrough-only use.
- Windows: PowerShell/cmd works when installed via the Python package entry
  point; WSL or Git Bash is needed only for the optional `bin/` shell wrappers.
- macOS only: `npx` and `codesign` if you need the optional Desktop picker
  patch.

---

## Install

Recommended on macOS/Linux/WSL/Git Bash (installs the `codex-shim` entry
point from `pyproject.toml`):

```bash
git clone https://github.com/0xSero/codex-shim ~/codex-shim
cd ~/codex-shim
python3 -m pip install --user -e .
```

Recommended on native Windows PowerShell/cmd:

```powershell
git clone https://github.com/0xSero/codex-shim $HOME\codex-shim
cd $HOME\codex-shim
py -3.11 -m pip install --user -e .
```

That pulls in `aiohttp` and installs the portable Python console command
`codex-shim`. On POSIX-like shells, the optional `codex-app` and `codex-model`
shortcuts live in `bin/`; symlink them if you want them on `PATH` too:

```bash
mkdir -p ~/.local/bin
ln -sf "$PWD/bin/codex-app" ~/.local/bin/codex-app
ln -sf "$PWD/bin/codex-model" ~/.local/bin/codex-model
```

If you move the checkout, recreate those symlinks; `codex-shim app` launches
`codex app` through the installed Python entry point and does not need them.

Alternative on macOS/Linux/WSL/Git Bash (no install, run straight from the
checkout):

```bash
git clone https://github.com/0xSero/codex-shim ~/codex-shim
cd ~/codex-shim
python3 -m pip install --user aiohttp
mkdir -p ~/.local/bin
ln -sf "$PWD/bin/codex-shim" ~/.local/bin/codex-shim
ln -sf "$PWD/bin/codex-app" ~/.local/bin/codex-app
ln -sf "$PWD/bin/codex-model" ~/.local/bin/codex-model
```

For running the test suite:

```bash
py