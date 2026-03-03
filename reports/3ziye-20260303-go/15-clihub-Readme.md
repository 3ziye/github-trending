# clihub

<p align="center">
  <img src="assets/cli_vs_mcp.png" alt="MCP vs CLI" width="600">
</p>

Turn any [MCP server](https://modelcontextprotocol.io/) into a compiled CLI binary. One command. Designed for agents.

```
clihub generate --url https://mcp.linear.app/mcp
# → ./out/linear (6.5MB static binary, zero runtime dependencies)
```

Every tool the server exposes becomes a subcommand with flags derived from its JSON Schema. Auth is handled automatically — OAuth, bearer tokens, API keys, and more.

[Full blog post](https://kanyilmaz.me/2026/02/23/cli-vs-mcp.html)

## Install

```bash
go install github.com/thellimist/clihub@latest
```

If `clihub` is not found after install, run `export PATH="$(go env GOPATH)/bin:$PATH"` to add Go-installed binaries (usually `~/go/bin`) to your current shell `PATH`.

Or build from source:

```bash
git clone https://github.com/thellimist/clihub.git
cd clihub
go build -o clihub .
install -m 755 clihub ~/.local/bin/clihub
```

If you're contributing, run `bash scripts/install-hooks.sh` once after cloning.

If `~/.local/bin` is not in your `PATH`, add it in your shell config (for example `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Requires Go 1.24+.

## AI Usage

Add the following to your AGENTS.md

```
## Tools

- Check if tool exists in `bin`.
- If not, check if official CLI exists. If so, download it and add it to AGENTS.md
- If not, check official MCP exists. If so, use clihub `go run github.com/thellimist/clihub@latest <server>` (see `--help`). to create a CLI and move the executable to bin folder. Then add it to AGENTS.md
- If both failed, give suggestions to create a CLI using official docs and https://clig.dev/
```

## Quick Start

### HTTP MCP server

```bash
clihub generate --url https://mcp.linear.app/mcp
./out/linear list-teams
```

### HTTP server with OAuth

```bash
clihub generate --url https://mcp.notion.com/mcp --oauth
./out/notion notion-search --query "meeting notes"
```

### Stdio MCP server

```bash
clihub generate --stdio "npx @modelcontextprotocol/server-github" \
  --env GITHUB_TOKEN=$GITHUB_TOKEN
./out/github list-repos --owner octocat
```

### Cross-compile

```bash
clihub generate --url https://mcp.stripe.com \
  --platform linux/amd64,darwin/arm64,windows/amd64
```

### Pass tool input as JSON

Generated CLIs include a `--from-json` flag on each tool command. This lets you pass the full tool input object directly.

```bash
./out/linear create-issue --from-json '{"title":"Bug report","priority":"high"}'
```

Rules:

- `--from-json` bypasses typed tool flags.
- `--from-json` cannot be combined with typed flags in the same call.
- If a tool already has a `--from-json` flag from its schema, clihub uses `--clihub-from-json` for passthrough instead.

## How It Works

1. **Connect** to the MCP server (HTTP or stdio)
2. **Discover** all tools via `tools/list`
3. **Generate** a Go CLI with one subcommand per tool
4. **Compile** to a static binary for your target platform(s)

The generated binary is standalone — no runtime dependencies, no config files, no clihub needed.

## Authentication

Generated CLIs handle auth at runtime. For HTTP servers, the `auth` subcommand manages credentials:

```bash
# OAuth browser flow (auto-discovers endpoints via RFC 9728 / RFC 8414)
./out/linear auth

# Manual bearer token
./out/linear auth --token $TOKEN

# Check status
./out/linear auth status

# Logout
./out/linear auth logout
```

Some MCPs require generatin-time auth. Use

```bash
clihub generate --help-auth
```

Auth is resolved in this order:

1. `--auth-token` flag
2. `--auth-type` + related flags (`--auth-header-name`, `--auth-key-file`, etc.)
3. `CLIHUB_AUTH_TOKEN` environment variable
4. `~/.clihub/credentials.json` (persisted from previous auth)
5. Unauthenticated

### Supported Auth Types

| Type | Description |
|------|-------------|
| OAuth 2.0 | Browser flow with PKCE, auto-discovery, token refresh |
| Dynamic Client Registration | RFC 7591 — auto-registers OAuth clients |
| Bearer Token | Static `Authorization: Bearer <token>` |
| API Key | Custom header (e.g. `X-API-Key`) |
| Basic Auth | Username/password |
| S2S OAuth 2.0 | Client credentials grant (no browser) |
| Google Service Account | JWT signed with service account key |

## Flags

```
clihub generate [flags]

Connection:
  --url string              Streamable HTTP URL of an MCP server
  --stdio string            Shell command that spawns a stdio MCP server
  --timeout int             Connection timeout in ms (default 30000)
  --env strings             Environment variables for stdio servers (KEY=VALUE)

Output:
  --name string             Override the inferred binary name
  --output string           Output directory (default "./out/")
  --platform string         Target GOOS/GOARCH pairs or 'all' (default current platform)

Auth (shown via `--help-auth`):
  --oauth                   Use OAuth for authentication (browser flow)
  --auth-token string       Bearer token
  --auth