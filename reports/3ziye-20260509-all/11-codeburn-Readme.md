<p align="center">
  <img src="https://raw.githubusercontent.com/getagentseal/codeburn/main/assets/providers.png" alt="CodeBurn" width="520" />
</p>

<p align="center"><strong>See where your AI coding tokens go.</strong></p>

<p align="center">                                                                                                                                                                          
    <a href="https://www.npmjs.com/package/codeburn"><img src="https://img.shields.io/npm/v/codeburn.svg" alt="npm version" /></a>
    <a href="https://www.npmjs.com/package/codeburn"><img src="https://img.shields.io/npm/dt/codeburn.svg" alt="total downloads" /></a>                                                       
    <a href="https://github.com/getagentseal/codeburn/blob/main/LICENSE"><img src="https://img.shields.io/npm/l/codeburn.svg" alt="license" /></a>                                            
    <a href="https://github.com/getagentseal/codeburn"><img src="https://img.shields.io/badge/node-%3E%3D20-brightgreen.svg" alt="node version" /></a>                                        
    <a href="https://discord.gg/pJ2DMWvtAx"><img src="https://img.shields.io/badge/discord-join-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>                                     
    <a href="https://github.com/sponsors/iamtoruk"><img src="https://img.shields.io/badge/sponsor-♥-ea4aaa?logo=github" alt="Sponsor" /></a>                                                  
  </p> 

CodeBurn tracks token usage, cost, and performance across **18 AI coding tools**. It breaks down spending by task type, model, tool, project, and provider so you can see exactly where your budget goes.

Everything runs locally. No wrapper, no proxy, no API keys. CodeBurn reads session data directly from disk and prices every call using [LiteLLM](https://github.com/BerriAI/litellm).

<table>
<tr>
<td align="center"><strong>Dashboard</strong></td>
<td align="center"><strong>Menu Bar</strong></td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/getagentseal/codeburn/main/assets/dashboard.jpg" alt="CodeBurn TUI dashboard" width="440" /></td>
<td><img src="https://cdn.jsdelivr.net/gh/getagentseal/codeburn@main/assets/menubar-0.8.0.png" alt="CodeBurn macOS menubar" width="440" /></td>
</tr>
<tr>
<td align="center"><strong>Optimize</strong></td>
<td align="center"><strong>Compare</strong></td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/getagentseal/codeburn/main/assets/optimize.jpg" alt="CodeBurn optimize" width="440" /></td>
<td><img src="https://raw.githubusercontent.com/getagentseal/codeburn/main/assets/compare.jpg" alt="CodeBurn compare" width="440" /></td>
</tr>
</table>

## Requirements

- Node.js 20+
- At least one supported AI coding tool with session data on disk
- For Cursor and OpenCode support, `better-sqlite3` is installed automatically as an optional dependency

## Install

```bash
npm install -g codeburn
```

Or with Homebrew:

```bash
brew tap getagentseal/codeburn
brew install codeburn
```

Or run directly without installing:

```bash
npx codeburn
bunx codeburn
dx codeburn
```

## Usage

```bash
codeburn                        # interactive dashboard (default: 7 days)
codeburn today                  # today's usage
codeburn month                  # this month's usage
codeburn report -p 30days       # rolling 30-day window
codeburn report -p all          # every recorded session
codeburn report --from 2026-04-01 --to 2026-04-10  # exact date range
codeburn report --format json   # full dashboard data as JSON
codeburn report --refresh 60    # auto-refresh every 60s (default: 30s)
codeburn status                 # compact one-liner (today + month)
codeburn status --format json
codeburn export                 # CSV with today, 7 days, 30 days
codeburn export -f json         # JSON export
codeburn optimize               # find waste, get copy-paste fixes
codeburn optimize -p week       # scope the scan to last 7 days
codeburn compare                # side-by-side model comparison
codeburn yield                  # track productive vs reverted/abandoned spend
codeburn yield -p 30days        # yield analysis for last 30 days
```

Arrow keys switch between Today, 7 Days, 30 Days, Month, and 6 Months (use `--from` / `--to` for an exact historical window). Press `q` to quit, `1` `2` `3` `4` `5` as shortcuts, `c` to open model comparison, `o` to open optimize. The dashboard auto-refreshes every 30 seconds by default (`--refresh 0` to disable). It also shows average cost per session and the five most expensive sessions across all projects.

## Supported Providers

| Provider | Data Location | Supported |
|----------|--------------|-----------|
| Claude Code | `~/.claude/projects/` | Yes |
| Claude Desktop | `~/Library/Application Support/Claude/local-agent-mode-sessions/` | Yes |
| Codex (OpenAI) | `~/.codex/sessions/` | Yes |
| Cursor | `~/Library/Application Support/Cursor/User/globalStorage/state.vsc