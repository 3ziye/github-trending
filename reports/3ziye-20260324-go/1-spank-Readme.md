<p align="center">
  <img src="doc/logo.png" alt="spank logo" width="200">
</p>

# spank

**English** | [简体中文][readme-zh-link]

Slap your MacBook, it yells back.

> "this is the most amazing thing i've ever seen" — [@kenwheeler](https://x.com/kenwheeler)

> "I just ran sexy mode with my wife sitting next to me...We died laughing" — [@duncanthedev](https://x.com/duncanthedev)

> "peak engineering" — [@tylertaewook](https://x.com/tylertaewook)

Uses the Apple Silicon accelerometer (Bosch BMI286 IMU via IOKit HID) to detect physical hits on your laptop and plays audio responses. Single binary, no dependencies.

## Requirements

- macOS on Apple Silicon (M2+)
- `sudo` (for IOKit HID accelerometer access)
- Go 1.26+ (if building from source)

## Install

Download from the [latest release](https://github.com/taigrr/spank/releases/latest).

Or build from source:

```bash
go install github.com/taigrr/spank@latest
```

> **Note:** `go install` places the binary in `$GOBIN` (if set) or `$(go env GOPATH)/bin` (which defaults to `~/go/bin`). Copy it to a system path so `sudo spank` works. For example, with the default Go settings:
>
> ```bash
> sudo cp "$(go env GOPATH)/bin/spank" /usr/local/bin/spank
> ```

## Usage

```bash
# Normal mode — says "ow!" when slapped
sudo spank

# Sexy mode — escalating responses based on slap frequency
sudo spank --sexy

# Halo mode — plays Halo death sounds when slapped
sudo spank --halo

# Fast mode — faster polling and shorter cooldown
sudo spank --fast
sudo spank --sexy --fast

# Custom mode — plays your own MP3 files from a directory
sudo spank --custom /path/to/mp3s

# Adjust sensitivity with amplitude threshold (lower = more sensitive)
sudo spank --min-amplitude 0.1   # more sensitive
sudo spank --min-amplitude 0.25  # less sensitive
sudo spank --sexy --min-amplitude 0.2

# Set cooldown period in millisecond (default: 750)
sudo spank --cooldown 600

# Set playback speed multiplier (default: 1.0)
sudo spank --speed 0.7   # slower and deeper
sudo spank --speed 1.5   # faster
sudo spank --sexy --speed 0.6
```

### Modes

**Pain mode** (default): Randomly plays from 10 pain/protest audio clips when a slap is detected.

**Sexy mode** (`--sexy`): Tracks slaps within a rolling 5-minute window. The more you slap, the more intense the audio response. 60 levels of escalation.

**Halo mode** (`--halo`): Randomly plays from death sound effects from the Halo video game series when a slap is detected.

**Custom mode** (`--custom`): Randomly plays MP3 files from a custom directory you specify.

### Detection tuning

Use `--fast` for a more responsive profile with faster polling (4ms vs 10ms), shorter cooldown (350ms vs 750ms), higher sensitivity (0.18 vs 0.05 threshold), and larger sample batch (320 vs 200).

You can still override individual values with `--min-amplitude` and `--cooldown` when needed.

### Sensitivity

Control detection sensitivity with `--min-amplitude` (default: `0.05`):

- Lower values (e.g., 0.05-0.10): Very sensitive, detects light taps
- Medium values (e.g., 0.15-0.30): Balanced sensitivity
- Higher values (e.g., 0.30-0.50): Only strong impacts trigger sounds

The value represents the minimum acceleration amplitude (in g-force) required to trigger a sound.

## Running as a Service

To have spank start automatically at boot, create a launchd plist. Pick your mode:

<details>
<summary>Pain mode (default)</summary>

```bash
sudo tee /Library/LaunchDaemons/com.taigrr.spank.plist > /dev/null << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.taigrr.spank</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/spank</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/spank.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/spank.err</string>
</dict>
</plist>
EOF
```

</details>

<details>
<summary>Sexy mode</summary>

```bash
sudo tee /Library/LaunchDaemons/com.taigrr.spank.plist > /dev/null << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.taigrr.spank</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/spank</string>
        <string>--sexy</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/spank.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/spank.err</string>
</dict>
</plist>
EOF
```

</details>

<details>
<summary>Halo mode</summary>

```bash
sudo tee /Library/LaunchDaemons/com.taigrr.spank.plist > /dev/null << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBL