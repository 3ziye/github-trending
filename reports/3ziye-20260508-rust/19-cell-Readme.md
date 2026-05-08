# cell

A terminal spreadsheet editor with Vim keybindings, written in Rust.

![cell screenshot](assets/cell.png)

## Install

From [crates.io](https://crates.io/crates/cell-sheet-tui):

```sh
cargo install cell-sheet-tui
```

Pre-built binaries for Linux, macOS, and Windows are available on the [GitHub Releases](https://github.com/garritfra/cell/releases) page.

### Build from source

```sh
git clone https://github.com/garritfra/cell.git
cd cell
cargo build --release
# Binary at target/release/cell
```

## Usage

```sh
cell                          # empty sheet
cell data.csv                 # open CSV
cell data.tsv                 # open TSV
cell sheet.cell               # open native format
cell data.psv --delimiter '|' # open with a custom field delimiter
cat data.csv | cell           # read from stdin (pipe input)
```

To explore an example sheet with formulas, ranges, and IF logic:

```sh
cell examples/demo.cell
```

The CSV/TSV delimiter is auto-detected from file content; pass
`--delimiter` to override. The native `.cell` format is auto-detected
via its `# cell v` magic header.

## Headless mode

For shell pipelines, Makefiles, and CI, `cell` can read from and write to a
file without launching the TUI:

```sh
cell sales.cell --read A1                 # print one cell's computed value
cell sales.cell --read B1:B10             # print a range as TSV
cell sales.cell --eval '=SUM(B1:B10)'     # evaluate a formula (no save)
cell sales.cell --write A1 42             # set a cell, recalc, save in place
cell sales.cell --write A1 42 --write B1 7 # batch multiple writes into one save
cell sales.cell --write Total '=SUM(B:B)' --read Total  # write a formula, then print it
cat data.csv | cell --read A1             # read from stdin
cell data.psv --delimiter '|' --read A1   # custom delimiter
```

- Cell references are 1-indexed and Excel-style (`A1`, `AA10`, `A1:B3`).
- The `=` prefix on `--eval` is optional.
- Writes whose value starts with `=` are stored as formulas; others are auto-typed (number vs text).
- Operations apply in a fixed order per invocation: writes → save → reads → evals.
- Errors print to stderr; the process exits non-zero on bad refs, parse errors, or missing files.
- Stdin input supports CSV, TSV, and the native `.cell` format. The delimiter
  is auto-detected; pass `--delimiter` to override (CSV/TSV only). `--write`
  requires a file argument when reading from stdin.

## Keybindings

If you know Vim, you know cell.

All motions and operators accept a `[count]` prefix (`5j`, `10G`, `3dd`,
`4yy`, `2w`). Counts also work between an operator and its motion (`d3j`,
`y2k`); outer and inner counts multiply (`5d2j` clears 10 rows). The
in-progress count and operator render in the status line as you type.

### Normal Mode

#### Motion

| Key                  | Action                                 |
| -------------------- | -------------------------------------- |
| `h` `j` `k` `l`      | Move cursor (one cell)                 |
| `gg`                 | First row (or row N with `[count]gg`)  |
| `G`                  | Last row (or row N with `[count]G`)    |
| `0`                  | First column                           |
| `$`                  | Last column                            |
| `w` / `b`            | Next / previous non-empty cell in row  |
| `Ctrl-D` / `Ctrl-U`  | Half-page down / up                    |
| `Ctrl-F` / `Ctrl-B`  | Full page down / up                    |
| `{` / `}`            | Previous / next block boundary in column |
| `H` / `M` / `L`      | Cursor to top / middle / bottom of viewport |
| `zz` / `zt` / `zb`   | Recenter / scroll-to-top / scroll-to-bottom around cursor |
| `Ctrl-e` / `Ctrl-y`  | Scroll viewport one row without moving cursor |
| `Ctrl-o` / `Ctrl-i` (or Tab) | Jump back / forward in jump list |

#### Marks

| Key            | Action                              |
| -------------- | ----------------------------------- |
| `m{a-z}`       | Set mark at cursor                  |
| `'{a-z}`       | Jump to marked row (column 0)       |
| `` `{a-z} ``   | Jump to exact marked cell           |

#### Editing

| Key                  | Action                                 |
| -------------------- | -------------------------------------- |
| `i` / `a` / `Enter`  | Edit cell (Insert mode)                |
| `x`                  | Clear cell                             |
| `dd`                 | Delete row (`[count]dd` for N rows)    |
| `d{motion}`          | Clear cells along motion (`dj`, `d3l`, `dh`, `dk`) |
| `yy`                 | Yank row (`[count]yy` for N rows)      |
| `y{motion}`          | Yank cells along motion (`yj`, `y3l`, `yh`, `yk`) |
| `p` / `P`            | Paste below / above                    |
| `Ctrl-A` / `Ctrl-X`  | Increment / decrement number in cell (`[count]` accepted) |
| `~`                  | Toggle case of first character, advance cursor |
| `guu` / `gUU`        | Lowercase / uppercase entire cell      |
| `g~~`                |