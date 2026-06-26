# glint

A fast, keyboard-driven terminal dashboard. Stocks, forex + crypto,
calendar, weather, news, email, notes, system resources, image gallery —
all in one grid you compose yourself. Written in Rust with
[ratatui](https://ratatui.rs).

https://github.com/user-attachments/assets/31f79aef-412c-44fb-bd72-c684e6aa9185

*A live capture — keyboard shortcuts driving focus, view changes, and
widget interaction across the dashboard.*

![Composed glint dashboard with clock, weather, calendar, news, stocks, resources, and gallery widgets in the tokyonight scheme](docs/screenshots/glint-demo1.png)

*A composed dashboard — clock + weather on the left, a calendar / email
/ notes stack and a stocks / forex / WSJ stack on the right, system
resources and a rotating gallery filling the rest. `tokyonight` scheme.*

![The same layout with the calendar rotated to week view, weather expanded to a 3-day forecast, and the WSJ news widget scrolling the latest articles](docs/screenshots/glint-demo2.png)

*Same layout, different views — calendar in week mode, weather showing
the 3-day forecast, the gallery rotating its next image, and the WSJ
feed scrolling the latest articles in the middle stack.*

![A different 5-pane layout in the chalktone scheme, focused on the WSJ widget with an NVDA stock chart open](docs/screenshots/glint-demo3.png)

*A different 5-pane layout in the `chalktone` scheme, focused on the
WSJ stack with an NVDA chart open in stocks on the right.*

Everything is opt-in, locally configured, and persists in plain TOML
under `~/.config/glint/` — no accounts, no telemetry, no cloud
component glint controls. The setup wizard generates a working
dashboard on first launch.

---

## Highlights

- **Ten widget kinds**, each independently configurable, with sensible
  built-in defaults — see the [widget catalogue](#widget-catalogue) below.
- **Composable layout**: a grid of cells; any cell can be a single
  widget or a **stack** of widgets you cycle between with `.` / `,`.
- **Multi-instance** — run the same widget kind in several panes
  (`stocks@watchlist1` + `stocks@watchlist2`, `clock@home` + `clock@office`).
- **Live config reload** — edit any widget's TOML and the dashboard
  picks it up without a restart.
- **Theming** — nine bundled colour schemes; per-widget colour overrides;
  add your own schemes by editing one TOML file. `:scheme nord` switches
  live.
- **Setup wizard** — `glint --setup` (or first launch with no config)
  walks you through layout, widget assignment, and credentials with
  copy-pasteable instructions for each external service.
- **Keyboard-first, mouse-friendly** — `Tab` cycles widgets,
  `Shift+<letter>` jumps to a widget by its shortcut letter, `:` opens
  a command bar, click anywhere to focus.
- **No cloud component**: every credential lives on disk under
  `~/.config/glint/credentials/` (0600 perms). API calls go directly
  from your machine to the upstream service.

---

## Install

### From source (only option for now)

You need a recent Rust toolchain (1.81+). Install via
[`rustup`](https://rustup.rs/) if you don't have one.

```sh
git clone https://github.com/ntrospect0/glint.git glint
cd glint

# Per-user install (no sudo, installs to ~/.local/bin):
make install PREFIX=~/.local

# Or system-wide (typically needs sudo):
sudo make install
```

If `~/.local/bin` isn't on your `$PATH`, add this to `~/.zshrc` or
`~/.bashrc`:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Verify:

```sh
glint --version
```

### Makefile targets

| target | what it does |
|---|---|
| `make` / `make release` | release build at `target/release/glint` |
| `make build` | debug build (faster compile, slower runtime) |
| `make install` | release build + copy to `$(PREFIX)/bin/glint` |
| `make uninstall` | remove `$(PREFIX)/bin/glint` |
| `make test` | run the test suite |
| `make clean` | `cargo clean` |

### Slim builds

Every widget compiles in only when its feature is enabled. The default
`widgets-all` umbrella turns them all on. For a smaller binary:

```sh
cargo install --path . --no-default-features \
  --features widget-clock,widget-weather,widget-stocks
```

Available features: `widget-clock`, `widget-weather`, `widget-calendar`,
`widget-news`, `widget-stocks`, `widget-forex`, `widget-email`,
`widget-resources`, `widget-gallery`, `widget-notes`.

### Updating

```sh
git pull
make install PREFIX=~/.local   # or sudo make install
```

---

## Quickstart

Launch with no existing config and you land in the setup wizard:

```sh
glint
# → "No config detected … launching the setup wizard."
```

The wizard walks you through:

1. **Global settings** — colour scheme, mouse-scroll direction, optional
   LLM provider and API key.
2. **Layout** — pick 1 to 8 panes and a layout preset.
3. **Widget assignment** — pick the widget kind that fills each pane,
   including the option to stack multiple widgets in a single cell.
4. **Per-widget setup** — timezone, location, RSS feeds, watchlist
   tickers, calendar provid