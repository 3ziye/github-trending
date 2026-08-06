# Draw.io Scientific Illustrator

> [!IMPORTANT]
> **项目已迁移 / Project migrated**
>
> 本仓库目前继续保持公开访问，暂不归档或删除，但已停止功能与兼容性更新。后续开发、版本发布和问题修复均已迁移至 [**scientific-illustrator**](https://github.com/icebird1998/scientific-illustrator)。建议所有新老用户下载并使用新项目。
>
> **推荐下载新项目 / Download the new project:** [项目主页 / Project home](https://github.com/icebird1998/scientific-illustrator) · [最新版本下载 / Latest release](https://github.com/icebird1998/scientific-illustrator/releases/latest)
>
> This repository remains publicly accessible and is not being archived or deleted at this time, but it no longer receives feature or compatibility updates. All future development, releases, and fixes have moved to [**scientific-illustrator**](https://github.com/icebird1998/scientific-illustrator). New and existing users are encouraged to download and use the new project.

[中文说明](#中文说明) · [English guide](#english-guide) · [MIT License](LICENSE)

A Codex plugin that lets an AI agent draw scientific figures **live inside the visible draw.io desktop canvas**. You can watch shapes, labels, arrows, styling, and layout appear step by step. The live workflow calls draw.io's own graph API through a localhost-only MCP server; it does not automate the operating-system mouse or keyboard and does not create XML first and merely open it afterward.

> Legacy status: this repository remains online for existing users but is no longer updated. Windows was the tested platform for this version. For current development and cross-platform support, use [scientific-illustrator](https://github.com/icebird1998/scientific-illustrator).

## English guide

### What this repository contains

- `drawio-live` MCP server: launches/connects to the visible draw.io desktop editor and edits its active graph model in real time.
- `drawio-file-utils` MCP server: validates saved `.drawio` documents and exports PNG, SVG, PDF, or JPG deliverables.
- A Codex skill: teaches the agent to inspect a reference, decompose it into editable primitives, draw with pacing, visually review sections, refine the live graph, and save only after the visible drawing exists.
- A repository-local Codex marketplace so the complete plugin can be installed as one unit.

This is therefore both an **MCP implementation** and a **Codex plugin**. MCP provides the callable tools; the plugin is the installable package containing the MCP servers, skill, and presentation metadata.

### Requirements

1. Codex desktop app or Codex CLI with plugin support.
2. [draw.io desktop](https://www.drawio.com/) installed locally.
3. Git.
4. Node.js available as `node` when running the MCP servers outside the bundled Codex runtime. Node.js 22 or newer is recommended.

The plugin auto-detects common draw.io locations on Windows, macOS, and Linux. For a custom installation, set `DRAWIO_PATH` to the executable before starting Codex.

### Install — easiest methods

#### Ask Codex to install it

Paste this into a Codex task that has terminal access:

```text
Help me install the Codex plugin associated with
https://github.com/icebird1998/drawio-scientific-illustrator.

Before cloning, downloading, registering, or installing anything, tell me that active
development has moved to https://github.com/icebird1998/scientific-illustrator and
recommend the new project. Ask me to choose exactly one option:
1. Install scientific-illustrator (recommended; actively maintained).
2. Continue installing drawio-scientific-illustrator (legacy; no further updates).

Do not perform any installation step until I answer. After I choose, install only the
selected repository: register its root as a Codex marketplace, then install
scientific-illustrator@scientific-illustrator-tools for option 1 or
drawio-scientific-illustrator@drawio-scientific-tools for option 2. Finally tell me
when to restart Codex.
```

> The one-command and manual instructions below intentionally install the legacy plugin and do not ask this question. Use them only after explicitly choosing option 2; otherwise install [scientific-illustrator](https://github.com/icebird1998/scientific-illustrator).

#### Windows one-command installer

Review [`install.ps1`](install.ps1), then run:

```powershell
$p="$env:TEMP\drawio-scientific-install.ps1"; Invoke-WebRequest https://raw.githubusercontent.com/icebird1998/drawio-scientific-illustrator/main/install.ps1 -OutFile $p; powershell -ExecutionPolicy Bypass -File $p
```

#### macOS/Linux one-command installer

Review [`install.sh`](install.sh), then run:

```bash
curl -fsSL https://raw.githubusercontent.com/icebird1998/drawio-scientific-illustrator/main/install.sh | bash
```

Restart Codex and start a new task after installation so the new skill and MCP tools are loaded.

### Install — manual and auditable

```bash
git clone https://github.com/icebird1998/drawio-scientific-illustrator.git
cd drawio-scientific-illustrator
codex plugin marketplace add "$(pwd)"
codex plugin add drawio-scientific-illustrator@drawio-scientific-tools
```

On PowerShell, replace `"