# iris

<img width="1448" height="1086" alt="ChatGPT Image Aug 18, 2026, 12_50_00 PM" src="https://github.com/user-attachments/assets/9acb5597-afea-41ed-b4a1-63195c2ce662" />

A camera for coding agents. One fast command or MCP tool call produces one trustworthy image.

```
iris example.com                        # 1440×900 @2x → example.com.png
iris --full --dark tailwindcss.com      # full page, dark color scheme
iris --size iphone stripe.com           # 390×844 @3x with a mobile UA
iris --selector '#hero' --padding 24 app.dev # first matching element, tightly framed
iris -o shots/ a.com b.com c.com        # batch, captured concurrently
cat urls.txt | iris - -o shots/         # batch from stdin (# comments ok)
iris -o hero.jpg --wait-for 'h1' app.dev
iris --selector 'h1' --json app.dev      # machine-readable JSON Lines
```

`iris --full bridger.to` →

![Full-page capture of bridger.to, taken by iris](.github/demo.png)

## Install

```
curl -fsSL https://raw.githubusercontent.com/brijr/iris/main/install.sh | sh
```

Or with a Rust toolchain:

```
cargo install iris-screenshot
```

The crates.io package is named `iris-screenshot`; the installed command is `iris`.

The only runtime dependency is an installed Chrome-family browser (Chrome, Chromium, Edge, or Brave).
Building from source requires Rust 1.88 or newer.

## Give your coding agent eyes

Iris includes a local stdio MCP server in the same binary. Add it to Codex:

```
codex mcp add iris -- iris mcp
```

Or use the equivalent configuration in another MCP client:

```json
{
  "mcpServers": {
    "iris": {
      "command": "iris",
      "args": ["mcp"]
    }
  }
}
```

The server exposes one tool, `capture`, which returns the image inline with structured metadata. It writes nothing by default; pass `output` when the agent also needs a file.

```json
{
  "url": "localhost:3000",
  "selector": "#pricing-card",
  "padding": 24,
  "size": "desktop",
  "dark": false,
  "format": "png",
  "timeout_seconds": 30,
  "output": "/tmp/pricing-card.png"
}
```

Bare localhost, `.localhost`, and loopback addresses use HTTP automatically. Other bare hosts use HTTPS. Run `iris mcp --help` to select a Chrome binary for the server.

MCP clients may need a fresh agent task before the newly registered `capture` tool appears.

## Setup Prompt

Give this setup prompt to your coding agent:

```text
Set up Iris as your visual camera in this coding environment.

Goal: install Iris, connect its local MCP server to this agent client, and prove
both the CLI and MCP paths work. Do not modify the application repository.

1. Check for an installed Chrome-family browser, `iris --version`, and an
   existing Iris MCP configuration.
2. If Iris is missing or outdated, install it with:

   curl -fsSL https://raw.githubusercontent.com/brijr/iris/main/install.sh | sh

   Or, when Rust is available:

   cargo install iris-screenshot

   Make sure the resulting `iris` command is on PATH.
3. Register the stdio MCP server without duplicating an existing entry.

   For Codex:

   codex mcp add iris -- iris mcp
   codex mcp get iris

   For another MCP client, configure command `iris` with args `["mcp"]`.
4. Prove the CLI works:

   iris https://example.com --selector h1 --padding 8 --scale 1 --json \
     -o /tmp/iris-smoke.png

   Confirm `status: ok` and a readable, non-empty PNG.
5. Reload the MCP configuration or start a fresh agent task if required. Call
   Iris's `capture` tool once for `https://example.com`, selecting the first
   `h1` with 8px padding and scale 1. Confirm an inline PNG and structured
   dimensions are returned.
6. Report the installed Iris version, MCP configuration, CLI smoke result, MCP
   smoke result, and any remaining blocker.

Do not claim MCP success from the CLI test alone. Do not add browser automation,
interaction scripting, or review tooling; use Iris only as the camera.
```

## What it does for you

- Renders with your real installed Chrome, driven over the DevTools Protocol
- Waits for fonts, image loads, entrance animations, and — on `--full` — scroll-triggers lazy-loaded content before capturing
- Captures the first matching element with `--selector`, automatically scrolling it into view and settling newly visible content before framing it
- Serves the same capture engine to coding agents with `iris mcp`, returning pixels inline instead of making the agent locate a file
- Retina `@2x` output by default; full pages taller than Chrome's ~16k px render limit fall back to `@1x` automatically (the report tells you which you got)
- Image format from the `-o` extension or `--format`: `png` (default), `jpg`, `webp` (JPEG/WebP encode at quality 90)
- One browser process, concurrent tabs; a failed URL prints `✗` and never kills the batch (exit code 1 if anything failed)
- Batch filenames derive from the URL (`example.com-pricing.png`); collisions get `-2`, `-3` suffixes
- `--json` writes one JSON object per completed capture to stdout, in concurrent completion order