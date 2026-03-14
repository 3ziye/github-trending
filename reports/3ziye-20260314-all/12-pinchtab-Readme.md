<p align="center">
  <img src="assets/pinchtab-headless.png" alt="PinchTab" width="200"/>
</p>

<p align="center">
  <strong>PinchTab</strong><br/>
  <strong>Browser control for AI agents</strong><br/>
  12MB Go binary • HTTP API • Token-efficient
</p>


<table align="center">
  <tr>
    <td align="center" valign="middle">
      <a href="https://pinchtab.com/docs"><img src="assets/docs-no-background-256.png" alt="Full Documentation" width="92"/></a>
    </td>
    <td align="left" valign="middle">
      <a href="https://github.com/pinchtab/pinchtab/releases/latest"><img src="https://img.shields.io/github/v/release/pinchtab/pinchtab?style=flat-square&color=FFD700" alt="Release"/></a><br/>
      <a href="https://github.com/pinchtab/pinchtab/actions/workflows/go-verify.yml"><img src="https://img.shields.io/github/actions/workflow/status/pinchtab/pinchtab/go-verify.yml?branch=main&style=flat-square&label=Build" alt="Build"/></a><br/>
      <img src="https://img.shields.io/badge/Go-1.25+-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go 1.25+"/><br/>
      <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License"/></a>
    </td>
  </tr>
</table>

---

## What is PinchTab?

PinchTab is a **standalone HTTP server** that gives AI agents direct control over Chrome.

For day-to-day local use, the server is typically installed as a user-level daemon, allowing agent tools to reuse the same browser control plane running in the background.

```bash
curl -fsSL https://pinchtab.com/install.sh | bash
# or
pinchtab daemon install
```

This installs the control-plane server and starts a default headless Chrome instance, ready to accept requests from agents or manual API calls.


If you prefer not to run a daemon, or if you're on Windows, you can instead run:

`pinchtab server` — runs the control-plane server directly
`pinchtab bridge` — runs a single browser instance as a lightweight runtime

PinchTab also provides a CLI with an interactive entry point for local setup and common tasks:

`pinchtab`

## Security

PinchTab defaults to a **local-first security posture**:

- `server.bind = 127.0.0.1`
- sensitive endpoint families are disabled by default
- `attach` is disabled by default
- IDPI is enabled with a **local-only website allowlist**

> [!CAUTION]
> By default, IDPI restricts browsing to **locally hosted websites only**.
> This prevents agents from navigating the public internet until you explicitly allow it.
> The restriction exists to make the security implications of browser automation clear before enabling wider access.

See the full guide: [docs/guides/security.md](docs/guides/security.md)

## What can you use it for

### Headless navigation

With the daemon installed and an agent skill configured, an agent can execute tasks like:

```
"What are the main news about trump on news.com?"
```

PinchTab exposes browser tools that allow agents to navigate pages, extract structured content, and interact with the DOM without wasting tokens on raw HTML or images.

### Headed navigation

In addition to headless automation, PinchTab supports headed Chrome profiles.

You can create profiles configured with authentication, cookies, extensions, or specific environments. Each profile can have a name and description.

For example, an agent request like:

```
"Log into my work profile and download the weekly report"
```

can automatically select the appropriate profile and perform the action.

### Local container isolation

If you prefer stronger isolation, PinchTab can run inside Docker.

This allows agents to control browsers in a sandboxed environment, reducing risk when running automation tasks locally.

### Distributed automation

PinchTab can manage multiple Chrome instances (headless or headed) across containers or remote machines.

Typical use cases include:

- QA automation
- testing environments
- distributed browsing tasks
- development tooling

You can connect to multiple PinchTab servers, or attach to Chrome instances running in remote debug mode.

## Process Model

PinchTab is server-first:
1. install the daemon or run `pinchtab server` for the full control plane
2. let the server manage profiles and instances
3. let each managed instance run behind a lightweight `pinchtab bridge` runtime

In practice:
- Server — the main product entry point and control plane
- Bridge — the runtime that manages a single browser instance
- Attach — an advanced mode for registering externally managed Chrome instances

### Primary Usage

The primary user journey is:

1. install Pinchtab
2. install and start the daemon with `pinchtab daemon install`
3. point your agent or tool at `http://localhost:9867`
4. let PinchTab act as your local browser service

That is the default “replace the browser runtime” scenario.
Most users should not need to think about `pinchtab bridge` directly, and only need `pinchtab` when they want the local interactive menu.

### Key Features

- **CLI o