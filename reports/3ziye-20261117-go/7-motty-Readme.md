<div align="center">
  <p>English | <a href="README.zh-CN.md">简体中文</a> | <a href="README.ja.md">日本語</a></p>

  <p>
    <a href="assets/readme-hero.svg"><img src="assets/readme-hero.svg" width="100%" alt="Motty — a desktop SSH client: shell, files, tunnels, screens and an assistant in one window" /></a>
  </p>

  <p>
    <a href="https://qm.qq.com/cgi-bin/qm/qr?k=&group_code=1131573299"><img src="assets/badge-qq.svg" alt="QQ 群 1131573299" /></a>
    <a href="https://docs.qq.com/doc/DVXBGYnFFdm9UWkVP"><img src="assets/badge-wechat.svg" alt="微信群" /></a>
    <a href="https://discord.gg/6s5tn9H4p2"><img src="assets/badge-discord.svg" alt="Discord" /></a>
    <a href="https://linux.do/t/topic/3086528/1"><img src="assets/badge-linuxdo.svg" alt="LINUX DO Community" /></a>
  </p>

  <p>
    <a href="assets/readme-hero.png"><img src="assets/readme-hero.png" width="900" alt="Motty running a real session: the SFTP panel, a shell tailing a log, and the AI assistant's answer" /></a>
  </p>
  <p><sub>A real session: the file panel, a shell following a deploy log, and the assistant reading the same terminal.</sub></p>
</div>

Motty is a desktop SSH client. The terminal, the SFTP panel, port forwards,
remote desktops and an AI assistant share one window, so a session does not
need a second app for files or a browser tab for a screen.

The full documentation lives at <https://motty.page/en/docs>; this file covers
the project, the packages and how to build it.

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/readme-hosts.png"><img src="assets/readme-hosts.png" alt="Host list with groups, tags and colours" /></a>
    </td>
    <td width="50%" valign="top">
      <a href="assets/readme-sftp-light.png"><img src="assets/readme-sftp-light.png" alt="The SFTP file panel beside the shell, in the light appearance" /></a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/readme-forward-light.png"><img src="assets/readme-forward-light.png" alt="Port forwards as a table of rules, in the light appearance" /></a>
    </td>
    <td width="50%" valign="top">
      <a href="assets/readme-monitor.png"><img src="assets/readme-monitor.png" alt="A split terminal beside the resource monitor" /></a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="assets/readme-desktop.png"><img src="assets/readme-desktop.png" alt="A remote desktop over VNC" /></a>
    </td>
    <td width="50%" valign="top">
      <a href="assets/readme-settings-colors.png"><img src="assets/readme-settings-colors.png" alt="Terminal color schemes in Settings, in the light appearance" /></a>
    </td>
  </tr>
</table>

## Why Motty?

<table>
  <tr>
    <td width="50%" valign="top">
      <p><strong>Hosts stay organised.</strong> Groups, tags, colours and icons, importable from
      OpenSSH config, PuTTY, MobaXterm and five more. Passwords go to an
      AES-256-GCM vault; the key lives in the system secret store.</p>
    </td>
    <td width="50%" valign="top">
      <p><strong>A session you can watch.</strong> Split the pane, then read the host's
      CPU, memory, disk and network beside the shell that is using them.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <p><strong>Screens too, when you need them.</strong> VNC and RDP connect, and both can
      ride an SSH host when the server only listens on its own loopback.</p>
    </td>
    <td width="50%" valign="top">
      <p><strong>Tunnels you can see.</strong> Local, remote, SOCKS5 and HTTP CONNECT
      rules bind to loopback only, are saved, and start when you say so. A tunnel
      stops with the SSH tab that owns it.</p>
    </td>
  </tr>
</table>

**Keyboard first.** Tabs, splits, SFTP, forwarding and the assistant are
commands in the palette; the mouse is optional. **Mosh when the network
moves:** an SSH host can carry its terminal over Mosh, keeping the session
through Wi-Fi, hotspot and VPN changes and drawing slow-link typing before the
echo; [docs/mosh.md](docs/mosh.md) lists what such a session does not carry.
**Honest about limits:**
[docs/remote-desktop.md](docs/remote-desktop.md) lists what the VNC and RDP
implementations do not do, and the release notes say which platforms were
tested on real hardware. **Nothing phones home:** no analytics, and the update
check is off by default and asks GitHub Releases when you turn it on.

## Install

Download the package for your platform from the
[releases page](https://github.com/t8y2/motty/releases):

| Platform | Packages |
| --- | --- |
| macOS (arm64, amd64) | `.dmg`, `.zip` |
| Windows (amd64, arm64) | `.exe` installer, portable `.zip` (data kept in `motty-data` beside `motty.exe`) |
| Linux (amd64, arm64) | `.deb`, `.tar.gz` |

Windows packages require Windows 10 or Windows Server 2016 or later.

macOS builds are signed and notarized when the release has the credentials.
Windows builds are signed when a certificate is configured. Linux packages are
not signed. AUR and `.