# Concord

<img width="1613" height="848" alt="concord - a feature-rich TUI client for
  Discord" src="./docs/example.png" />

Concord is a feature-rich TUI (terminal user interface) client for Discord, written in Rust with ratatui. Full Discord experience, right in your terminal.

## Table of contents

- [Installation](#installation)
- [Features](#features)
- [Configuration](#configuration)
- [Performance](#performance)
- [FAQ](#faq)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Homebrew

```sh
brew install chojs23/tap/concord
```

### Cargo

Install native audio dependencies first. On macOS with Homebrew:

```sh
brew install opus pkg-config
```

On Fedora:

```sh
sudo dnf install opus-devel alsa-lib-devel pkgconf-pkg-config
```

On Debian or Ubuntu:

```sh
sudo apt install libopus-dev libasound2-dev pkg-config
```

On macOS with Homebrew:

```sh
brew install opus pkg-config
```

```sh
cargo install concord
```

To install without local voice playback and microphone support:

```sh
cargo install concord --no-default-features
```

To install the latest unreleased version directly from the Git repository:

```sh
cargo install --git https://github.com/chojs23/concord
```

### Nix

Run without installing (requires flakes enabled):

```sh
nix run github:chojs23/concord
```

Install into your profile:

```sh
nix profile install github:chojs23/concord
```

Or add the flake as an input in your own `flake.nix`:

```nix
{
  inputs.concord.url = "github:chojs23/concord";
}
```

### GitHub Release installer

Install the latest release with the cargo-dist shell installer:

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/chojs23/concord/releases/latest/download/concord-installer.sh | sh
```

On Windows, use the PowerShell installer instead:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://github.com/chojs23/concord/releases/latest/download/concord-installer.ps1 | iex"
```

The installer places `concord` under `$CARGO_HOME/bin`, which is usually
`~/.cargo/bin` on Unix and `%USERPROFILE%\.cargo\bin` on Windows.

### Build from source

You need the Rust stable toolchain, Cargo, and the native dependencies listed in
the Cargo install section.

```sh
git clone https://github.com/chojs23/concord.git
cd concord
cargo build --release
```

The release binary is produced at:

```sh
target/release/concord
```

To build without local voice playback and microphone support, disable default features:

```sh
cargo build --release --no-default-features
```

On WSLg, audio is usually exposed through PulseAudio instead of a real ALSA
sound card. If playback does not start, check that PulseAudio and ALSA routing
work before debugging Discord voice itself:

```sh
pactl info
paplay /usr/share/sounds/alsa/Front_Center.wav
aplay -D pulse /usr/share/sounds/alsa/Front_Center.wav
```

## Features

### Authentication

- **Token** : paste an existing Discord token.
- **Email / Password** : login with credentials. MFA (TOTP, SMS) is fully supported.
- **QR Code** : scan the code from the Discord mobile app.

Email and QR code logins may trigger a CAPTCHA challenge on Discord's side. We cannot solve that, so I strongly recommend using token authentication.

Tokens are saved under Concord's config directory in plain text. See the Security section below for details.

### Guilds & Channels

- Browse servers with guild folder grouping
- Navigate text channels, threads, and forum channels
- View and filter forum posts (active / archived)
- Load pinned messages per channel
- Open channel actions for pinned messages, thread lists, and mark-as-read
- Join and leave voice channels
- Highlight active voice speakers in voice channel participant rows
- Track unread messages and mention counts per channel
- Mute and unmute channels and servers
- Leave the selected server after confirmation

### Messaging

- Send, edit, and delete messages
- Upload / Download attachments
- Search messages with filters with `/`
- Use @mention autocomplete
- Use custom emoji from other servers when your account supports it
- Send custom emoji your account cannot use directly as image links when enabled
- View full message history
- Rich content display (embeds, attachments, stickers, and mentions)
- Detect URLs in message bodies and markdown links, then open them in your default browser
- Direct message shortcuts for copy, reply, edit, delete, reactions, URL opening,
  and image viewing. More message actions are available from the action menu.

#### Markdown Rendering

![Markdown rendering example](./docs/markdown-example.png)

Concord renders a practical subset of Discord-style Markdown in message bodies:

- Headings: `# H1`, `## H2`, `### H3`
- Quotes: `> quoted text`
- Bullets: `- item` and `* item`
- Inline styles: `**bold**`, `*italic*`, and `` `inline code` ``
- Fenced code blocks with optional language labels, rendered as compact boxes
- Raw URLs and markdown link destinations are underlined