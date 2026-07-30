# Draw.io Scientific Illustrator

[中文说明](#中文说明) · [English guide](#english-guide) · [MIT License](LICENSE)

A Codex plugin that lets an AI agent draw scientific figures **live inside the visible draw.io desktop canvas**. You can watch shapes, labels, arrows, styling, and layout appear step by step. The live workflow calls draw.io's own graph API through a localhost-only MCP server; it does not automate the operating-system mouse or keyboard and does not create XML first and merely open it afterward.

> Status: Windows is tested. macOS and Linux executable discovery is included, but live behavior can vary with draw.io/Electron packaging. Reports and pull requests are welcome.

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
Install the public Codex plugin from https://github.com/icebird1998/drawio-scientific-illustrator.
Clone it locally, register its repository root as a Codex marketplace, install
drawio-scientific-illustrator@drawio-scientific-tools, then tell me when to restart Codex.
```

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

On PowerShell, replace `"$(pwd)"` with `(Get-Location).Path`:

```powershell
git clone https://github.com/icebird1998/drawio-scientific-illustrator.git
Set-Location drawio-scientific-illustrator
codex plugin marketplace add (Get-Location).Path
codex plugin add drawio-scientific-illustrator@drawio-scientific-tools
```

### How to use it

1. Restart Codex after installation and create a new task.
2. Attach a PNG, JPEG, SVG, or a rendered PDF page as the reference.
3. Mention **Draw.io Scientific Illustrator** or select the plugin in the composer.
4. State the desired pacing and output formats.

> **Recommended Codex configuration for complex scientific redraws:** choose **GPT-5.6 Sol** and set reasoning effort to **Max**. In Codex settings, enable the six-level reasoning selector first; the default five-level selector does not show the Max option. This setting can increase response time and token use.

Recommended prompt:

```text
Use Draw.io Scientific Illustrator. Launch the live draw.io canvas and recreate this
reference scientific figure step by step with a 100 ms delay. Control only draw.io's
own graph API; do not use OS mouse/keyboard automation and do not generate XML first.
Keep all labels, arrows, panels, and legends editable. Visually inspect and refine each
section, then save the final .drawio file and export a 2000 px PNG preview.
```

Chinese prompts work equally well:

```text
使用 Draw.io Scientific Illustrator。启动实时 draw.io，以 100 ms 的步骤间隔重绘
这张参考图。必须直接控制 draw.io 画布，不要使用系统鼠标键盘控制，也不要先生成
XML。文字、箭头、分区和图例都要可编辑；完成后保存 .drawio 并导出 2000 px PNG。
```

### Live tool workflow

The agent normally uses the tools in this order:

1. `drawio_live_launch` — launch or connect to a visible draw.io editor.
2. `drawio_live_status` — confirm that the 