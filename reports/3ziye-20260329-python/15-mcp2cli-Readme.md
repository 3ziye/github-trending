<p align="center">
  <img src="https://raw.githubusercontent.com/knowsuchagency/mcp2cli/main/assets/hero.png" alt="mcp2cli — one CLI for every API" width="700">
</p>

<h1 align="center">mcp2cli</h1>

<p align="center">
  Turn any MCP server, OpenAPI spec, or GraphQL endpoint into a CLI — at runtime, with zero codegen.<br>
  <strong>Save 96–99% of the tokens wasted on tool schemas every turn.</strong><br><br>
  <a href="https://www.orangecountyai.com/blog/mcp2cli-one-cli-for-every-api-zero-wasted-tokens"><strong>Read the full writeup →</strong></a>
</p>

## Install

```bash
# Run directly without installing
uvx mcp2cli --help

# Or install globally
uv tool install mcp2cli
```

## AI Agent Skill

mcp2cli ships with an installable [skill](https://skills.sh) that teaches AI coding agents (Claude Code, Cursor, Codex) how to use it. Once installed, your agent can discover and call any MCP server or OpenAPI endpoint — and even generate new skills from APIs.

```bash
npx skills add knowsuchagency/mcp2cli --skill mcp2cli
```

After installing, try prompts like:
- `mcp2cli --mcp https://mcp.example.com/sse` — interact with an MCP server
- `mcp2cli create a skill for https://api.example.com/openapi.json` — generate a skill from an API

## Usage

### MCP HTTP/SSE mode

```bash
# Connect to an MCP server over HTTP
mcp2cli --mcp https://mcp.example.com/sse --list

# Call a tool
mcp2cli --mcp https://mcp.example.com/sse search --query "test"

# With auth header
mcp2cli --mcp https://mcp.example.com/sse --auth-header "x-api-key:sk-..." \
  query --sql "SELECT 1"

# Force a specific transport (skip streamable HTTP fallback dance)
mcp2cli --mcp https://mcp.example.com/sse --transport sse --list

# Search tools by name or description (case-insensitive substring match)
mcp2cli --mcp https://mcp.example.com/sse --search "task"
```

`--search` implies `--list` and works across all modes (`--mcp`, `--spec`, `--graphql`, `--mcp-stdio`).

### OAuth authentication

APIs that require OAuth are supported out of the box — across MCP, OpenAPI, and GraphQL modes.
mcp2cli handles token acquisition, caching, and refresh automatically.

```bash
# Authorization code + PKCE flow (opens browser for login)
mcp2cli --mcp https://mcp.example.com/sse --oauth --list
mcp2cli --spec https://api.example.com/openapi.json --oauth --list
mcp2cli --graphql https://api.example.com/graphql --oauth --list

# Client credentials flow (machine-to-machine, no browser)
mcp2cli --spec https://api.example.com/openapi.json \
  --oauth-client-id "my-client-id" \
  --oauth-client-secret "my-secret" \
  list-pets

# With specific scopes
mcp2cli --graphql https://api.example.com/graphql --oauth --oauth-scope "read write" users

# Local spec file — use --base-url for OAuth discovery
mcp2cli --spec ./openapi.json --base-url https://api.example.com --oauth --list
```

Tokens are persisted in `~/.cache/mcp2cli/oauth/` so subsequent calls reuse existing tokens
and refresh automatically when they expire.

### Secrets from environment or files

Sensitive values (`--auth-header` values, `--oauth-client-id`, `--oauth-client-secret`) support
`env:` and `file:` prefixes to avoid passing secrets as CLI arguments (which are visible in
process listings):

```bash
# Read from environment variable
mcp2cli --mcp https://mcp.example.com/sse \
  --auth-header "Authorization:env:MY_API_TOKEN" \
  --list

# Read from file
mcp2cli --mcp https://mcp.example.com/sse \
  --oauth-client-secret "file:/run/secrets/client_secret" \
  --oauth-client-id "my-client-id" \
  --list

# Works with secret managers that inject env vars
fnox exec -- mcp2cli --mcp https://mcp.example.com/sse \
  --oauth-client-id "env:OAUTH_CLIENT_ID" \
  --oauth-client-secret "env:OAUTH_CLIENT_SECRET" \
  --list
```

### MCP stdio mode

```bash
# List tools from an MCP server
mcp2cli --mcp-stdio "npx @modelcontextprotocol/server-filesystem /tmp" --list

# Call a tool
mcp2cli --mcp-stdio "npx @modelcontextprotocol/server-filesystem /tmp" \
  read-file --path /tmp/hello.txt

# Pass environment variables to the server process
mcp2cli --mcp-stdio "node server.js" --env API_KEY=sk-... --env DEBUG=1 \
  search --query "test"
```

### OpenAPI mode

```bash
# List all commands from a remote spec
mcp2cli --spec https://petstore3.swagger.io/api/v3/openapi.json --list

# Call an endpoint
mcp2cli --spec ./openapi.json --base-url https://api.example.com list-pets --status available

# With auth
mcp2cli --spec ./spec.json --auth-header "Authorization:Bearer tok_..." create-item --name "Test"

# POST with JSON body from stdin
echo '{"name": "Fido", "tag": "dog"}' | mcp2cli --spec ./spec.json create-pet --stdin

# Local YAML spec
mcp2cli --spec ./api.yaml --base-url http://localhost:8000 --list
```

### GraphQL mode

```bash
# List all queries and mutations from a GraphQL endpoint
mcp2cli --graphql https://api.example.com/graphql --list

# Call a query
mcp2cli --graphql https://api.example.com/graphql users --limit 10

# Call a mutation
mcp