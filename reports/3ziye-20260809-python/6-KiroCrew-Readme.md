<p align="center">
  <img src="assets/banner.svg" alt="Kiro Crew. Keep work moving. Runs on your hardware, remembers across sessions, keeps working unattended.">
</p>

<h1 align="center">Kiro Crew</h1>

<p align="center">
  <strong>A persistent workspace for development work that self-improves and continues beyond one session.</strong>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/103032" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/103032/daily?language=Python" alt="Kiro Crew on Trendshift" width="250" height="55"></a>
</p>

<p align="center">
  Kiro Crew is an open source development workspace that runs locally or remotely on
  your hardware. It is persistent, self-learning, and self-evolving. Work with it
  from the desktop app, web dashboard, and CLI, or continue the same work through
  connection tools like Slack and Discord.
  Your multi-step tasks can run unattended, recurring jobs run on your schedule,
  and heartbeats monitor systems until something needs attention. Kiro Crew Apps
  tailor that experience to a specific job, combining a purpose-built interface
  with agents, skills, schedules, integrations, and backend services.
</p>

<p align="center">
  <a href="https://github.com/kirodotdev/KiroCrew/releases"><img src="https://img.shields.io/badge/Download-macOS%20%7C%20Linux-2f6feb?style=flat-square" alt="Download Kiro Crew for macOS or Linux"></a>
  <a href="docs/README.md"><img src="https://img.shields.io/badge/Documentation-1f6feb?style=flat-square" alt="Read the documentation"></a>
  <a href="docs/guides/install.md"><img src="https://img.shields.io/badge/Install%20guide-macOS%20%7C%20Linux%20%7C%20Windows-6e7781?style=flat-square" alt="Install guide for macOS, Linux, and Windows"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Contributing-238636?style=flat-square" alt="Contributing guide"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/Security-8250df?style=flat-square" alt="Security policy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-656d76?style=flat-square" alt="Apache 2.0 license"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#build-from-source">Build from source</a> ·
  <a href="#why-kiro-crew">Why Kiro Crew</a> ·
  <a href="#what-kiro-crew-does">Capabilities</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#security-and-control">Security</a> ·
  <a href="#install-configure-and-operate">Install</a> ·
  <a href="#anonymous-usage-telemetry">Telemetry</a> ·
  <a href="#docs-and-contributing">Docs</a>
</p>

## Quick start

You choose how to run Kiro Crew: the desktop app with automatic updates, a
one-line install on your machine or a remote host, the Docker image for
always-on servers, or a build from source. Every path runs on `kiro-cli`
underneath, so the first launch installs it if needed and guides Kiro
device-code sign-in.

### App downloads

The desktop app starts a bundled Gateway when no local Gateway is already
running, updates itself on the channel you download, and can connect to a
remote Gateway over an SSH tunnel. See the
[desktop app guide](docs/build/desktop-app.md).

- **macOS**: [Stable](https://download.crew.kiro.dev/desktop/stable/latest/KiroCrew.dmg) | [Insider](https://download.crew.kiro.dev/desktop/insider/latest/KiroCrew.dmg) | [Nightly](https://download.crew.kiro.dev/desktop/nightly/latest/KiroCrew.dmg)
- **Linux**: [Stable](https://download.crew.kiro.dev/desktop/stable/latest/KiroCrew-x86_64.AppImage) | [Insider](https://download.crew.kiro.dev/desktop/insider/latest/KiroCrew-x86_64.AppImage) | [Nightly](https://download.crew.kiro.dev/desktop/nightly/latest/KiroCrew-x86_64.AppImage)
- **Windows**: no desktop build yet, so run the Gateway from a [source install](#build-from-source) and open the dashboard in your browser

Take Stable unless you have a reason not to — the table below says who each
channel is for.

### Release channels

Every install path — desktop app, CLI, Docker image — offers the same three
channels. Pick by how much churn you can absorb, not by version number:

| Channel | Who it's for | Built from | Cadence |
|---------|--------------|------------|---------|
| **Stable** | Everyone. The default on every install path. | The Insider build that baked long enough to be promoted | On promotion, no calendar commitment |
| **Insider** | Power users who want features days to weeks early and accept the new bugs that come with them | Release-branch release-candidate tags | Every RC |
| **Nightly** | Us and contributors. Untested `main` HEAD — expect breakage. | `main`, 06:00 UTC daily | Daily |

Stable and Insider are two update lanes of the **same** app. The desktop app
switches between them in Settings → About, a CLI install switches by re-running
the installer with `--channel`, and a container switches by pulling a different
tag. Eith