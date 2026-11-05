<p align="center">
  <img src=".github/assets/icon.png" width="112" alt="TwinDesk icon">
</p>

<h1 align="center"><a href="https://twin-desk.vercel.app">TwinDesk</a></h1>

<p align="center">
  <b>Your Mac, your PC, your Linux box and your Android phone, working as one desk.</b><br>
  One mouse and keyboard for all of them. Their screens, apps, files, clipboard, cameras, calls and texts, shared.<br>
  Free and open source. No account, no cloud, no shared network needed.
</p>

<p align="center">
  <a href="#download"><b>⬇️ Download 2.5</b></a> ·
  <a href="https://twin-desk.vercel.app"><b>Website</b></a> ·
  <a href="#new-in-25"><b>What's new</b></a> ·
  <a href="#what-it-does"><b>What it does</b></a> ·
  <a href="#get-started"><b>Get started</b></a>
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/github/v/release/InukaAsith/TwinDesk?label=version&color=4b8bff">
  <img alt="macOS 13+" src="https://img.shields.io/badge/macOS-13%2B-black">
  <img alt="Windows 10/11" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078d4">
  <img alt="Linux X11 and Wayland" src="https://img.shields.io/badge/Linux-X11%20%7C%20Wayland-f0a30a">
  <img alt="Android 10+" src="https://img.shields.io/badge/Android-10%2B-3ddc84">
  <img alt="License: GPL-3.0" src="https://img.shields.io/badge/license-GPL--3.0-blue">
  <a href="https://github.com/inukaasith/twindesk/releases"><img src="https://img.shields.io/github/downloads/inukaasith/twindesk/total" alt="Downloads"></a>
</p>

<p align="center">
  <img src=".github/assets/v25-hero-desks.jpg" alt="TwinDesk on a Mac over its desktop wallpaper, on a Windows PC over its wallpaper, and on an Android phone, all connected" width="100%">
</p>


## What is TwinDesk?

You probably own more than one computer. A work laptop and a gaming PC. A MacBook and the Windows
machine you can't give up. A Linux box under the desk. And a phone that's never more than a metre
away. Each one is great on its own. Together they're a mess: two keyboards, files emailed to
yourself, a phone you keep picking up, the same tab opened three times.

**TwinDesk turns all of them into one desk.**

Push the mouse off the edge of your Mac's screen and it carries on onto the PC, keyboard and all.
Copy on one, paste on the other. Drag a file across the edge and drop it there. Open the PC's apps
in windows on your Mac. Turn a tablet or an old laptop into a second screen. Answer your phone's
calls and texts from the computer, use its camera in your video calls, and drive the computer from
the couch with it. And when you walk from one device to another, **ReZume** brings the tab, the
video or the document you were on with you.

It's one app on every platform, so a Mac and a PC pair exactly like two Macs, and a phone is a full
peer instead of a notification mirror.

<table>
<tr>
<td width="25%" valign="top">

**🔀 Any combination**<br>
Mac ↔ Windows, Mac ↔ Mac, PC ↔ PC, Linux ↔ anything, Android ↔ any computer. Or [all of them at once](#mesh).

</td>
<td width="25%" valign="top">

**📡 Anywhere**<br>
Same Wi-Fi, a USB cable, or no shared network at all: Bluetooth and a direct Wi-Fi link of their own.

</td>
<td width="25%" valign="top">

**🔒 Yours alone**<br>
No account, no cloud, no telemetry. Devices talk only to each other, end-to-end encrypted.

</td>
<td width="25%" valign="top">

**⚡ Built for speed**<br>
A native Rust input lane over UDP, a parallel file engine, hardware video. [How](#speed).

</td>
</tr>
</table>

<table>
<tr>
<td width="50%" align="center" valign="top">

**💻 Computer to computer**<br>
<img src=".github/assets/v25-overview-pc.gif" alt="The Mac switching to a connected Linux PC: its Overview with Ring, Lock, Sleep, volume, clipboard and a drop zone for files, then the File Sharing and Clipboard pages" width="100%">

</td>
<td width="50%" align="center" valign="top">

**📱 Computer to phone**<br>
<img src=".github/assets/v25-overview-phone.gif" alt="An Android phone taking over the Mac's link: the phone's Overview with its battery, network and quick actions, then its Photos" width="100%">

</td>
</tr>
</table>

<a name="download"></a>

## ⬇️ Download

<table>
<tr>
<td width="25%" align="center" valign="top">

**🍎 macOS**<br><sub>13 Ventura or later</sub>

<a href="https://github.com/InukaAsith/TwinDesk/releases/download/v2.5.2/TwinDesk-2.5.2-arm64.dmg"><img src="https://img.shields.io/badge/Apple_Silicon-.dmg-000000?style=for-the-badge" alt="macOS, Apple Silicon"></a><br>
<a href="https://github.com/InukaAsith/TwinDesk/releases/download/v2.5.2/TwinDesk-2.5.2-x64_Intel.dmg"><img src="https://img.shields.io/badge/Intel-.dmg-555555?style=for-the-badge" alt="macOS, Intel"></a>

</td>
<td width="25%" align="center" valign="top">

**🪟 Windows**<br><sub>10 and 11</sub>

<a href="https://github.com/InukaAsith/TwinDesk/releases/download/v2.5.2/TwinDesk-Setup-2.5.2.exe"><img src="https://img.shields.io/badge/x64-Installer-0078d4?style=for-the-badge" alt="Windows, x64"></a><br>
<a href="htt