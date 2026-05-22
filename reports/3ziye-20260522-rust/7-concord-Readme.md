# Concord

<img width="1613" height="848" alt="concord - a feature-rich TUI client for
  Discord" src="./docs/example.png" />

Concord is a feature-rich TUI (terminal user interface) client for Discord, written in Rust with ratatui. Full Discord experience, right in your terminal.

## Installation

### Homebrew

```sh
brew install chojs23/tap/concord
```

### Cargo

```sh
cargo install concord
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

Then reference it as `concord.packages.${system}.default` in your configuration.

A development shell with the pinned Rust toolchain and `rust-analyzer` is also
available:

```sh
nix develop github:chojs23/concord
```

### GitHub Release installer

Install the latest release with the cargo-dist shell installer:

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/chojs23/concord/releases/latest/download/concord-installer.sh | sh
```

The installer places `concord` under `$CARGO_HOME/bin`, which is usually
`~/.cargo/bin`. Make sure that directory is on your `PATH` before running
`concord`.

### Build from source

You need the Rust stable toolchain and Cargo.

```sh
git clone https://github.com/chojs23/concord.git
cd concord
cargo build --release
```

The release binary is produced at:

```sh
target/release/concord
```

By default, source builds can join voice channels and decode received voice
audio, but they do not open local audio input or output devices. To build with
voice playback and gated microphone transmit, enable the optional
`voice-playback` feature:

```sh
cargo build --release --features voice-playback
```

Linux playback uses the system audio stack through `cpal`. You may need ALSA
development files when building from source:

```sh
sudo apt install libasound2-dev
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

Concord can request joining and leaving Discord voice channels. Default builds
do not open local audio devices, while source builds with `--features
voice-playback` support voice playback and gated microphone transmit.

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
- Receive voice playback when built with `--features voice-playback`
- Transmit microphone audio when built with `--features voice-playback`, joined
  from this Concord session, explicitly allowed, and not self-muted
- Highlight active voice speakers in voice channel participant rows
- Track unread messages and mention counts per channel
- Mute and unmute channels and servers

### Messaging

- Send, edit, and delete messages
- Reply to specific messages
- Upload files by copying them from your file manager and pasting them into the composer
- Upload images copied directly to the system clipboard when the terminal forwards the paste key
- Use @mention autocomplete while composing messages
- View full message history with pagination
- Rich content display (embeds, attachments, stickers, and mentions)
- Detect URLs in message bodies and markdown links, then open them in your default browser
- Direct message shortcuts for copy, reply, edit, delete, pin/unpin, reactions,
  image viewing, and profile lookup

#### Markdown Rendering

![Markdown rendering example](./docs/markdown-example.png)

Concord renders a practical subset of Discord-style Markdown in message bodies:

- Headings: `# H1`, `## H2`, `### H3`
- Quotes: `> quoted text`
- Bullets: `- item` and `* item`
- Inline styles: `**bold**`, `*italic*`, and `` `inline code` ``
- Fenced code blocks with optional language labels, rendered as compact boxes
- Raw URLs and markdown link destinations are underlined and can be ope