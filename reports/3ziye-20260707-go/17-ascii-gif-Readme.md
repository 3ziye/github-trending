# ascii-gif

[![CI](https://github.com/tamnd/ascii-gif/actions/workflows/ci.yml/badge.svg)](https://github.com/tamnd/ascii-gif/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/tamnd/ascii-gif)](https://github.com/tamnd/ascii-gif/releases/latest)
[![Go Reference](https://pkg.go.dev/badge/github.com/tamnd/ascii-gif.svg)](https://pkg.go.dev/github.com/tamnd/ascii-gif)
[![License](https://img.shields.io/github/license/tamnd/ascii-gif)](./LICENSE)

Turn a terminal session into a good-looking animated GIF. You write the action,
`ascii-gif` supplies the window chrome, theme, and framing.

It wraps [vhs](https://github.com/tamnd/vhs) as a Go library and prepends an
attractive default look, so a tape only carries the part you care about: the
commands, the typing, the pauses.

[Install](#install) • [Quickstart](#quickstart) • [Tapes](#tapes) • [Library](#library)

## Install

```bash
go install github.com/tamnd/ascii-gif/cmd/ascii-gif@latest
```

`ascii-gif` drives two runtime tools the way vhs does: `ttyd` runs your commands
in a real terminal and `ffmpeg` encodes the frames. Install both, then check:

```bash
# macOS
brew install ttyd ffmpeg

ascii-gif doctor
```

## Quickstart

```bash
ascii-gif init demo          # write demo.tape you can edit
ascii-gif render demo.tape   # render demo.gif
```

A tape is a small script of terminal actions. The starter looks like this:

```tape
# A tape is a script. ascii-gif prepends the look, you write the action.
Type "echo hello from ascii-gif"
Enter
Sleep 2s
```

Render it to a GIF, choosing the output path:

```bash
ascii-gif render demo.tape -o out/hello.gif
```

## Tapes

A tape uses the vhs tape language: `Type`, `Enter`, `Sleep`, `Hide`/`Show`, and
more. See the [vhs command reference](https://github.com/tamnd/vhs#vhs) for the
full set. `ascii-gif` adds the look for you, so you do not write the `Set`
header. The default look is a colored margin, a window bar, a rounded border,
and a readable theme and font.

Two flags change how the look is applied:

```
-o, --output     GIF path to write (default: the tape name with .gif)
    --no-preset  do not prepend the look; the tape stands on its own
-q, --quiet      suppress vhs progress output
```

Pass `--no-preset` when a tape carries its own `Set` header and you want full
control.

Read a tape from stdin with `-`:

```bash
echo 'Type "date"; Enter; Sleep 1s' | ascii-gif render -
```

## Library

The renderer is a small package you can call from Go. Give it a tape body and it
composes the look, runs vhs, and writes the GIF:

```go
import "github.com/tamnd/ascii-gif/asciigif"

err := asciigif.Render(ctx, `Type "echo hi"
Enter
Sleep 1s
`, asciigif.Options{Output: "hi.gif"})
```

`asciigif.CheckDeps` reports whether `ttyd` and `ffmpeg` are on PATH, which is
what `ascii-gif doctor` calls.

## Credit

The heavy lifting is [vhs](https://github.com/charmbracelet/vhs) by Charm.
`ascii-gif` is a thin wrapper over a [library-ized fork](https://github.com/tamnd/vhs)
of it that adds a default look and a smaller surface.

## License

MIT. See [LICENSE](LICENSE).
