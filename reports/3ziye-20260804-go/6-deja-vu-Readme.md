<p align="center"><img src="assets/logo.svg" width="340" alt="deja-vu"></p>

<p align="center"><strong>Your agents already solved this. deja finds it.</strong><br>Memory tools start empty and record forward. deja starts full: it indexes the sessions your coding agents already wrote to disk &mdash; months of history from before you installed it &mdash; searches 3.5&nbsp;GB in ~1.5&nbsp;ms, serves it back to any agent over MCP, and moves with you between machines over SSH. One zero-dependency binary, fully local.</p>

<p align="center"><strong>84.9% hit@1</strong> on LongMemEval-S retrieval &mdash; no LLM, no embeddings, no API key. <a href="https://vshulcz.github.io/deja-vu/guide/benchmarks.html">Harness in-repo, run it yourself.</a></p>

<p align="center"><a href="https://vshulcz.github.io/deja-vu/">vshulcz.github.io/deja-vu</a> &middot; <a href="https://vshulcz.github.io/deja-vu/guide/compare.html">how deja compares</a></p>

<p align="center">
  <a href="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml"><img src="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/vshulcz/deja-vu/releases"><img src="https://img.shields.io/github/v/release/vshulcz/deja-vu" alt="Release"></a>
  <a href="https://www.npmjs.com/package/@vshulcz/deja-vu"><img src="https://img.shields.io/npm/v/%40vshulcz%2Fdeja-vu?label=npm" alt="npm"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/vshulcz/deja-vu"><img src="https://api.scorecard.dev/projects/github.com/vshulcz/deja-vu/badge" alt="OpenSSF Scorecard"></a>
  <a href="https://mcptoplist.com/server/io.github.vshulcz%2Fdeja-vu"><img src="https://mcptoplist.com/badge/io.github.vshulcz%2Fdeja-vu.svg" alt="MCP Toplist"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
</p>

<p align="center"><img src="assets/demo.gif" alt="The same question asked twice in Claude Code: without deja the agent has no record of it, with deja it answers with the decision from eight months earlier"></p>

<p align="center"><em>Every line is quoted from two real Claude Code sessions &mdash; the same question, the same agent, once without memory and once with deja. Nobody searched anything: the agent called deja itself.</em></p>

<p align="center">
<b>84.9% hit@1</b> on LongMemEval-S &middot; <b>69.8%</b> on LoCoMo &middot; <b>zero</b> LLM calls, zero embeddings, zero API keys &middot; <b>~1.5&nbsp;ms</b> median search over 3.5&nbsp;GB<br>
<sub>Both harnesses ship in this repo and run on the public datasets in minutes — <a href="https://vshulcz.github.io/deja-vu/guide/benchmarks.html">check the numbers yourself</a>.</sub>
</p>

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/vshulcz/deja-vu/main/install.sh | sh
```

or:

```sh
go install github.com/vshulcz/deja-vu/cmd/deja@latest   # Go
npx @vshulcz/deja-vu "query"                            # npm, no install
brew install vshulcz/tap/deja-vu                        # Homebrew
```

For desktop apps that install MCP servers as bundles, every release ships an
`.mcpb` per platform — download it from the
[latest release](https://github.com/vshulcz/deja-vu/releases/latest) and open it.
The bundle carries the binary, so there is nothing else to install. Terminal
agents use `deja install` below instead.

### Shell completion

```sh
deja completion bash >> ~/.bashrc
deja completion zsh >> ~/.zshrc
deja completion fish > ~/.config/fish/completions/deja.fish
```

Wire it into the agents you use (edits config, keeps a `.bak`):

```sh
deja install --all     # MCP recall for every agent it finds on this machine
deja install --auto    # same, plus session-start auto-recall where supported
```

Install also builds the index from the histories it finds, so the first agent
session after it is instant rather than paying for the build. `--no-index`
skips that for scripted installs; running `deja` with nothing indexed builds it
too.

Claude Code users can skip that step and install everything as a plugin instead:

```sh
claude plugin marketplace add vshulcz/deja-vu
claude plugin install deja-vu@deja-vu
```

The plugin wires the same three hooks, the `/deja` command and the MCP server. It stands down on its own if `deja install` already wired them, so having both does not recall twice.

Codex, Cursor and Qwen read the same bundle from their own registries:

```sh
codex plugin marketplace add vshulcz/deja-vu && codex plugin add deja-vu@deja-vu
cursor-agent plugin marketplace add https://github.com/vshulcz/deja-vu
qwen extensions install https://github.com/vshulcz/deja-vu
```

Copilot CLI takes it too, and OpenClaw installs plugins from a path rather than a URL:

```sh
copilot plugin marketplace add vshulcz/deja-vu && copilot plugin install deja-vu@deja-vu
openclaw plugins install ./deja-vu/claude-plugin
```

Cursor, Qwen, OpenClaw and Copilot all read the Claude plugin format, so **one bundle installs into six harnesses**. Their