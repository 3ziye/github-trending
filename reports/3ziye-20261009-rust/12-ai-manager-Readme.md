<div align="center">

<img src="src/assets/spatial/models/v5/mark.png" alt="AI Manager" width="128" height="128">

# AI Manager

### A calm desktop manager for AI coding tools

</div>

AI Manager installs, updates, configures, and repairs AI coding command-line
tools on your own computer, so you never have to touch shell profiles, `PATH`,
or hand-edited configuration files. It is a local-first desktop application
built with Tauri 2 and React 18, released under the GNU AGPL-3.0-or-later.

> [!NOTE]
> Every installer on the
> [Releases page](https://github.com/OnlistTeam/ai-manager/releases) passes the
> signing and verification gates in the
> [release runbook](docs/development/RELEASE_RUNBOOK.md) before it is
> published. A local build is not a release and must not be redistributed as
> one.

## Who it is for

People who use Claude Code, Codex, or a similar tool every day and would
rather not manage npm ownership, configuration files, and API endpoints by
hand. One place to see which tools are installed, which AI service each one
is really using, and whether that setup still works.

## What it does

Seven destinations in a flat sidebar, with Settings in the footer.

**Home** summarises what is installed, what has an update, and what needs
attention. Quick Check is built from real local signals: it rechecks saved
service addresses only when you ask, and never claims a process is healthy
when no such signal exists.

**Software** detects, installs, updates, and repairs ten command-line tools
without crossing away from the npm, pnpm, bun, or Volta owner that already
manages them. It keeps a verified version history and shows bounded, redacted
process logs instead of raw shell output. Downloads are official-first, with
one process-scoped retry on a recoverable network failure and a local proxy
option in Settings. Desktop apps are detected separately; installing and
updating those stays with each vendor's signed channel.

**API Endpoints** connects a tool to an AI service from a reviewed preset
catalogue or a custom HTTPS endpoint, then shows the effective connection:
the endpoint the tool will really use, and why, including environment
variable overrides. Testing a service reads the models it actually serves,
sends one real request to the one you pick, and shows the reply or the
generated image, so a rejected key no longer reads as a healthy address. Your
shell environment is never edited. Local Routing and a 30 day local usage
overview are secondary tabs.

**Skills** scans every supported local scope in one overview, installs from
trusted GitHub catalogues or a local ZIP, copies a Skill to another tool, and
keeps recovery copies before removal.

**MCP** adds stdio, HTTP, and SSE connections without pasting JSON, and
enables or disables them per tool. Adoption of a tool's existing servers
never rewrites live configuration.

**Global Prompts** creates, edits, imports, and switches prompts without
opening a configuration file, and reveals where each one lives.

**Sessions** browses and searches local sessions. Content loads only after
selection, and supported sessions resume in a terminal through a command line
built in the backend.

**Settings** holds language and appearance, desktop behaviour, the local
download proxy, database backups, configuration import and export, and the
fail-closed signed updater.

## Supported tools

| Command-line tools     | Desktop apps   |
| ---------------------- | -------------- |
| Claude Code            | Codex App      |
| Codex                  | Claude Desktop |
| OpenCode               | Cursor         |
| Gemini CLI             | ZCode          |
| Grok Build             | Cherry Studio  |
| OpenClaw               |                |
| Hermes                 |                |
| Pi                     |                |
| Kimi Code              |                |
| DeepSeek Harness (DSH) |                |

Per-tool behaviour is driven by a capability registry rather than scattered
conditionals, so a tool that lacks a concept (for example a "current service")
simply does not show that control.

## Install

Download the installer for your platform from the
[Releases page](https://github.com/OnlistTeam/ai-manager/releases).

| Platform            | Installer                     | Automatic updates        |
| ------------------- | ----------------------------- | ------------------------ |
| macOS Apple Silicon | Signed, notarized DMG         | Signed app archive       |
| macOS Intel         | Signed, notarized DMG         | Signed app archive       |
| Windows x64         | MSI, verify the SHA-256       | Minisign-signed MSI      |
| Linux x64           | AppImage and deb with SHA-256 | Minisign-signed AppImage |

Windows installers are not Authenticode-signed, so SmartScreen shows an unknown
publisher warning on first run; check the published SHA-256 before installing.
Linux has no cross-distribution equivalent of platform signing either. On both,
the minisign signature on upda