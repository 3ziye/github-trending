<p align="center">
  <img src="banner-dark.png" alt="Mole — a deep research agent in Go, exposed over MCP" width="820">
</p>

<p align="center">
  <em>A deep-research agent with an enforced budget, verified quotes, and a privacy
  boundary for local data.</em>
</p>

Ask a question. mole decomposes it, searches, reads sources, extracts claims,
checks each claim against the text it came from, looks for contradictions between
them, and writes an answer with citations. Every model call is reserved against a
budget before it happens and settled after, so the ceiling you set is the ceiling
it hits.

It runs as a single static binary on your machine, uses your own API keys, and
speaks MCP so a coding agent can drive it — either by handing mole a question and
collecting the answer, or, in **toolkit mode**, by doing the reasoning with its own
model while mole supplies the parts that are not model calls.

<p align="center">
  <img src="demo.svg" alt="mole researching a question: planning, 39 claims, two contradictions found, $0.0149 spent" width="900">
</p>

---

## Why mole

Three things mole does that a chat interface with web search does not.

**The budget is enforced, not estimated.** Every call is reserved before it is
made and settled after, against a ledger with non-negative constraints in the
database schema itself. `--usd 0.50` means the run stops at fifty cents. Measured
overshoot across the test corpus is 0%.

**Every claim carries a quote, checked against the source.** A claim whose quote
does not appear verbatim in the page it was mined from is discarded at extraction,
before it can reach an answer. Claims that survive can be re-read against their
source afterwards, and one that turns out not to be supported is marked as such in
the report rather than quietly dropped.

**Your local data stays local.** Point mole at a CSV or a folder and it will
analyse it without the contents leaving your machine: the model chooses a
hypothesis template and column names, mole renders and runs the SQL, and only
aggregates — counts, means, test results, buckets covering at least five records —
are allowed back. `mole crossings` shows you exactly what left.

---

## Install

**Script** — Linux and macOS, amd64 and arm64:

```sh
curl -fsSL https://raw.githubusercontent.com/lajosdeme/mole/main/install.sh | sh
```

Downloads the release archive for your platform, verifies its SHA-256 against the
checksums published with the release, and installs `mole` and `mole-mcp` into
`~/.local/bin` (or `/usr/local/bin` if that is writable). It uses `sudo` only if
the target directory needs it, and `--dry-run` shows what it would do. If piping a
script into a shell makes you uneasy — reasonable — read it first, or use one of
the paths below.

**Homebrew** — macOS and Linux:

```sh
brew install lajosdeme/mole/mole
```

Fully qualified, and it has to be: an unrelated `mole` (a macOS cleanup tool) is in
homebrew/core, so `brew install mole` will always mean that one. Both install a
binary called `mole`, so only one can be linked at a time.

**Arch Linux** — from the AUR:

```sh
yay -S mole-research-bin      # prebuilt release binaries
yay -S mole-research          # build from source
```

Not `mole`: that name and `mole-bin` on the AUR belong to an SSH tunnelling tool
that has held them since 2020. The package installs `/usr/bin/mole` and declares
the conflict, so pacman will tell you rather than overwrite anything.

**Debian and Ubuntu** — `.deb` from the [releases page](https://github.com/lajosdeme/mole/releases):

```sh
curl -fsSLO https://github.com/lajosdeme/mole/releases/latest/download/mole_amd64.deb
sudo dpkg -i mole_amd64.deb
```

An `.rpm` is published for the same platforms.

**From source** — needs Go 1.25+:

```sh
go install github.com/lajosdeme/mole/cmd/mole@latest
go install github.com/lajosdeme/mole/cmd/mole-mcp@latest
```

Or clone and `make install`, which stamps the version so `mole version` reports the
tag rather than `dev`.

Every path installs the same thing: two static binaries with no runtime
dependencies, built `CGO_ENABLED=0`. The database is SQLite, created on first use
under your XDG data directory.

### Configure

You need a search provider and a model provider. Keys live in
`~/.config/mole/config.json`, mode 0600 — never in environment variables that
leak into process listings, and never in `.mcp.json`.

```bash
mole config set search.provider tavily          # or: brave
mole config set search.tavily-key tvly-...

mole config set llm.provider anthropic          # or: openai-compatible
mole config set llm.api-key sk-...
mole config set llm.model claude-sonnet-5
mole config set llm.cheap-model claude-haiku-4-5

mole doctor                                     # verify everything above
```

Any OpenAI-compatible endpoint works — DeepSeek, Ollama, llama.cpp, vLLM, a proxy:

```bash
mole config set llm.provider openai-compatible
mole config set llm.base-url https://api.deepseek.com/v1
mole config set llm.model deepseek