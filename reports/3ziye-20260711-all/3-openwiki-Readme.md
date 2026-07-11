# OpenWiki

OpenWiki is a CLI that writes and maintains agent wikis for codebases or purpose memory. It's built specifically for agents, can ingest local knowledge sources through built-in connectors or git repositories and synthesize them into a local wiki.

![OpenWiki](https://raw.githubusercontent.com/langchain-ai/openwiki/main/static/openwiki.png)

## Install

```sh
npm install -g openwiki
```

On Windows, prefer installing OpenWiki with Node.js package managers such as
`npm` or `pnpm`:

```sh
npm install -g openwiki
# or
pnpm add -g openwiki
```

`bun install -g openwiki` can fall back to compiling OpenWiki's `better-sqlite3`
checkpointing dependency. Before using that path, install Visual Studio Build
Tools with the Desktop development with C++ workload. Bun does not run lifecycle
scripts from installed packages by default, so it cannot display a package-level
warning before that native dependency build starts.

## Quick Start

Initialize OpenWiki, configure your model and API key, then generate documentation

```sh
# Personal brain mode
openwiki personal --init

# Code brain mode
openwiki code --init
```

OpenWiki has two modes:

- **Personal mode** builds a local personal brain wiki in `~/.openwiki/wiki` from
  configured sources like local repositories, Gmail, Notion, Web Search, Hacker
  News, and X/Twitter.
- **Code mode** builds repository documentation in `openwiki/` for the current
  codebase.

Choose `openwiki personal --init` for a local personal brain wiki or
`openwiki code --init` for repository documentation.

Then to ensure your documentation stays up-to-date, add the CI workflow for your Git provider to automatically open a PR or merge request with documentation updates:

- GitHub Actions: copy [openwiki-update.yml](./examples/openwiki-update.yml) into `.github/workflows/openwiki-update.yml`.
- GitLab CI: copy [openwiki-update.gitlab-ci.yml](./examples/openwiki-update.gitlab-ci.yml) into `.gitlab-ci.yml` or include it from your existing GitLab pipeline.

For repository documentation in GitHub Actions, use
`openwiki code --update --print`. You do not need to run `--init` in CI:
`--update` will create the initial `openwiki/` docs if they do not exist yet, as
long as the workflow provides the required provider and model environment
variables.

## Usage

Start the interactive CLI:

```sh
openwiki
```

Start OpenWiki with an initial request:

```sh
openwiki "Please generate documentation for this repository"
```

Run a single command and exit:

```sh
openwiki -p "Summarize what you can do"
```

Initialize OpenWiki:

```sh
openwiki personal --init
```

Initialize repository code documentation:

```sh
openwiki code --init
```

Update existing documentation:

```sh
openwiki --update
```

Update repository code documentation:

```sh
openwiki code --update
```

Run an update that can ingest configured local connectors first:

```sh
openwiki --update "Refresh the wiki from configured connectors"
```

Show help:

```sh
openwiki --help
```

In chat, use `/api-key` to update the current provider API key and
`/langsmith-key` to update or clear LangSmith tracing credentials. Both commands
use masked prompts.

Authenticate a connector provider:

```sh
openwiki auth slack
openwiki auth gmail
openwiki auth x
openwiki auth notion
```

Start an ngrok tunnel for Slack OAuth:

```sh
openwiki ngrok start
```

This starts ngrok with a random HTTPS forwarding URL. OpenWiki reads ngrok's
local inspection API, appends `/callback`, and saves
`OPENWIKI_HTTPS_OAUTH_REDIRECT_URI` automatically. Register the printed callback
URL in Slack. If you have a fixed ngrok domain, run
`openwiki ngrok start https://<your-ngrok-domain>`. X/Twitter and Gmail auth
ignore that HTTPS override and keep using the local loopback callback,
`http://127.0.0.1:53682/callback`.

`openwiki` creates initial repository documentation in `openwiki/` when no wiki exists. Source ingestion runs and scheduled connector updates maintain the local general-purpose wiki in `~/.openwiki/wiki/`. By default, the CLI stays open after each run so you can send follow-up messages. Use `-p` or `--print` for a one-shot non-interactive run that prints the final assistant output.

Use `openwiki personal --init` for the local personal brain wiki or `openwiki code --init` for repository documentation. Bare `openwiki --init` is no longer supported because init needs an explicit mode. `openwiki --update` defaults to personal mode unless you pass `code`, `personal`, or `--mode`.

On each `code` run, `openwiki` maintains both an `AGENTS.md` and a `CLAUDE.md` at the repository root, adding prompting that instructs your coding agent to reference the wiki when searching for context. Each file is created if it does not already exist. If a file is present, OpenWiki only rewrites its own `<!-- OPENWIKI:START -->…<!-- OPENWIKI:END -->` block and leaves the rest of your content untouched (appending the block the first time). The scheduled GitHub Actions workflow includes these f