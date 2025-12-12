<p align="center">
<pre>
███    ██ ██    ██ ███    ███ ██████
████   ██ ██    ██ ████  ████ ██   ██
██ ██  ██ ██    ██ ██ ████ ██ ██████
██  ██ ██ ██    ██ ██  ██  ██ ██   ██
██   ████  ██████  ██      ██ ██   ██
</pre>
</p>

<p align="center">
  <a href="https://github.com/nasedkinpv/numr/actions/workflows/ci.yml"><img src="https://github.com/nasedkinpv/numr/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

A text calculator for natural language expressions with a vim-style TUI.

<p align="center">
  <img src="screenshots/numr_demo.gif" width="700" alt="numr TUI demo - calculations with variables, units, currencies, and continuation">
</p>

## Features

- **Natural language expressions**: `20% of 150`, `$100 in euros`, `2 hours + 30 min`
- **Variables**: `tax = 15%` then `100 + tax`
- **Unit conversions**: Length, weight, time, temperature, data sizes
- **Compound units**: `5 m * 10 m = 50 m²`, `100 km / 2 h = 50 km/h`
- **Currency conversions**: USD, EUR, GBP, JPY, CHF, CNY, CAD, AUD, INR, KRW, RUB, ILS, PLN, UAH + crypto (BTC, ETH, SOL, and more)
- **Live exchange rates**: Fetched automatically on startup
- **Vim-style editing**: Normal and Insert modes with familiar keybindings
- **Mouse support**: Scroll with mouse wheel or trackpad
- **File persistence**: Auto-saves to config directory, supports custom files
- **Syntax highlighting**: Numbers, operators, variables, units, and currencies
- **Comments**: Lines starting with `#` or `//` are treated as comments
- **Continuation**: Start a line with an operator (`+ 10`, `* 2`) to continue from the previous result
- **Wrap mode**: Toggle text wrapping with bottom-aligned results
- **Grouped totals**: Currencies and units summed separately in footer (respects exchange rates)

## Installation

### macOS (Homebrew)

```bash
brew tap nasedkinpv/tap
brew install numr
```

### Arch Linux (AUR)

```bash
# Using yay
yay -S numr

# Using paru
paru -S numr
```

### From source

```bash
# Install from source
cargo install --path crates/numr-tui

# Or build from source
cargo build --release

# Binary will be available at target/release/numr
```

## Usage

### TUI Mode

```bash
# Open default file (~/.config/numr/default.numr)
numr

# Open specific file
numr example.numr
```

### CLI Mode

```bash
# Single expression
numr-cli "20% of 150"

# Evaluate file
numr-cli -f example.numr

# Interactive REPL
numr-cli -i

# Pipe mode
echo "100 + 200" | numr-cli
```

### JSON-RPC Server Mode

Run numr as a backend for other tools (editors, launchers, scripts):

```bash
numr-cli --server
```

Send JSON-RPC 2.0 requests via stdin, receive responses via stdout:

```bash
echo '{"jsonrpc":"2.0","method":"eval","params":{"expr":"20% of 150"},"id":1}' | numr-cli --server
# {"jsonrpc":"2.0","result":{"type":"number","value":30.0,"display":"30"},"id":1}
```

**Available methods:**

| Method | Params | Description |
|--------|--------|-------------|
| `eval` | `{"expr": "..."}` | Evaluate expression |
| `eval_lines` | `{"lines": [...]}` | Evaluate multiple lines |
| `clear` | none | Clear state |
| `get_totals` | none | Get grouped totals |
| `get_variables` | none | List variables |
| `reload_rates` | none | Refresh exchange rates |

## Keybindings (TUI)

### Normal Mode

| Key | Action |
|-----|--------|
| `i` | Enter Insert mode |
| `a` | Enter Insert mode after cursor |
| `A` | Enter Insert mode at end of line |
| `o` | New line below and enter Insert mode |
| `h` / `←` | Move left |
| `j` / `↓` | Move down |
| `k` / `↑` | Move up |
| `l` / `→` | Move right |
| `PageUp` | Scroll page up |
| `PageDown` | Scroll page down |
| `0` / `Home` | Move to start of line |
| `$` / `End` | Move to end of line |
| `x` | Delete character under cursor |
| `dd` | Delete current line |
| `W` | Toggle wrap mode |
| `N` | Toggle line numbers |
| `H` | Toggle header (hidden by default) |
| `?` / `F1` | Toggle help popup |
| `q` | Quit |
| `Ctrl+s` | Save file |
| `Ctrl+r` | Refresh exchange rates |
| `F12` | Toggle debug mode |

### Insert Mode

| Key | Action |
|-----|--------|
| `Esc` | Return to Normal mode |
| `Enter` | New line |
| `Backspace` | Delete character before cursor |
| `Delete` | Delete character after cursor |
| `Arrows` | Move cursor |
| `PageUp/Down` | Scroll page |
| `Home/End` | Move to start/end of line |
| `Ctrl+s` | Save file |
| `F12` | Toggle debug mode |

## Supported Operations

### Arithmetic
```
10 + 20           → 30
100 - 25          → 75
6 * 7             → 42
100 / 4           → 25
2 ^ 8             → 256
```

### Percentages
```
20% of 150        → 30
100 + 15%         → 115
$50 - 10%         → $45
```

### Variables
```
price = $100
tax = 8%
price + tax       → $108
```

### Comments
```
# This is a comment
// This is also a comment
Groceries         $45.00
# Comments are dimmed and ignored in calculations
```

### Continuation
```
$100              → $100
+ $50             → $150 (continues from previous)
* 2               → $300
- 10%             → $270
total = _