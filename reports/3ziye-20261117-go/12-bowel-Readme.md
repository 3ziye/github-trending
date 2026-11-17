<p align="center">
  <img src="site/icon.png" width="112" alt="bowel">
</p>

<h1 align="center">bowel</h1>

<p align="center">
bowel is a <a href="https://github.com/MetaCubeX/mihomo">mihomo</a> client for macOS, Windows, Linux and Android.
</p>

<p align="center">
  <a href="https://github.com/21stware/bowel/releases/latest"><b>Download</b></a> ·
  <a href="https://bowel.dev/en/">Website</a> ·
  <a href="https://t.me/+BI3KVgBn7SE3YjVh">Telegram</a> ·
  <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="site/shots/home-en-dark.webp">
    <img src="site/shots/home-en.webp" width="880" alt="bowel main window">
  </picture>
</p>

The desktop interface is built in Go and rendered directly via the GPU, with no WebView. The Android app is built with Flutter and has the same cards and skins.

## Features

The screenshots are from macOS.

### Routes
Route traffic by purpose, and select exit nodes manually or automatically by speed.

<img src="site/shots/routes-en.webp" width="880" alt="Routes">

### Connections
Inspect the app, destination, rule, exit, and speed for each connection, or reroute domains on the fly.

<img src="site/shots/activity-en.webp" width="880" alt="Connections log">

### Providers
Import subscription links, node URLs, YAML configs, or QR codes, with data usage and expiry shown for each source.

<img src="site/shots/providers-en.webp" width="880" alt="Providers">

### Menu bar
Toggle system proxy takeover, switch proxy modes, and pick the node for traffic no rule matches from the menu bar, or from the system tray on Windows and Linux. On Omarchy, pin bowel's icon in the bar's tray, or it stays folded in the tray's drawer.

<img src="site/shots/panel-en.webp" width="300" alt="Menu bar panel">

### Skins
Sixteen skins that change the look of the whole interface.

<table>
  <tr>
    <td><img src="site/shots/skin-broadsheet-en.webp" alt="Broadsheet"><br><sub>Broadsheet</sub></td>
    <td><img src="site/shots/skin-phosphor-en.webp" alt="Phosphor"><br><sub>Phosphor</sub></td>
    <td><img src="site/shots/skin-neon-en.webp" alt="Neon"><br><sub>Neon</sub></td>
  </tr>
  <tr>
    <td><img src="site/shots/skin-blueprint-en.webp" alt="Blueprint"><br><sub>Blueprint</sub></td>
    <td><img src="site/shots/skin-sakura-en.webp" alt="Sakura"><br><sub>Sakura</sub></td>
    <td><img src="site/shots/skin-paper-en.webp" alt="Paper"><br><sub>Paper (default)</sub></td>
  </tr>
  <tr>
    <td><img src="site/shots/skin-shanshui-en.webp" alt="Shanshui"><br><sub>Shanshui</sub></td>
    <td><img src="site/shots/skin-celadon-en.webp" alt="Celadon"><br><sub>Celadon</sub></td>
    <td><img src="site/shots/skin-dunhuang-en.webp" alt="Dunhuang"><br><sub>Dunhuang</sub></td>
  </tr>
  <tr>
    <td><img src="site/shots/skin-dusk-en.webp" alt="Dusk"><br><sub>Dusk</sub></td>
    <td><img src="site/shots/skin-aurora-en.webp" alt="Aurora"><br><sub>Aurora</sub></td>
    <td><img src="site/shots/skin-obsidian-en.webp" alt="Obsidian"><br><sub>Obsidian</sub></td>
  </tr>
  <tr>
    <td><img src="site/shots/skin-riso-en.webp" alt="Riso"><br><sub>Riso</sub></td>
    <td><img src="site/shots/skin-mrrobot-en.webp" alt="Mr. Robot"><br><sub>Mr. Robot</sub></td>
    <td><img src="site/shots/skin-machine-en.webp" alt="The Machine"><br><sub>The Machine</sub></td>
  </tr>
  <tr>
    <td><img src="site/shots/skin-samaritan-en.webp" alt="Samaritan"><br><sub>Samaritan</sub></td>
  </tr>
</table>

### Other
- **Custom rules**: Route specific domains, keywords, or IP ranges, and test where addresses go; on macOS, Windows and Linux, route by application too.
- **Measured exit locations**: Verify true exit locations through Cloudflare trace.
- **Gateway mode** (macOS, Linux): Turn this computer into a LAN gateway for devices like TVs and consoles. The full guide, for people and agents, is [docs/gateway.md](docs/gateway.md).
- **TUN** (macOS, Windows, Linux): Intercept traffic from applications that ignore system proxy settings.
- **Developer tools** (macOS, Linux): Docker, the terminal and Git ignore the system proxy. bowel lists which ones aren't connected, writes their own config in one click, and removes it cleanly when you undo.
- **Download sources**: Measures the official source and each mirror for npm, pip, Go and Cargo, and switches in one click. When the current source stops answering, one click moves you to the fastest one that does, or sends it through a node again.
- **Private networks**: Addresses on your LAN, Tailscale and company VPN go direct automatically, in global mode too.
- **MCP**: Built-in MCP server for Claude Code and other agents to read status and troubleshoot connections. It asks you before changing settings by default. The command below is for macOS; on Windows and Linux, use the path of the bowel program.
  ```bash
  claude mcp add --scope user bowel -- /Applications/bowel.app/Contents/MacOS/bowel mcp
  ```
- **Settings and languages**: Searchable 