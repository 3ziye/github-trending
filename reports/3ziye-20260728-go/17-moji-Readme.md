<div align="center">

<img src=".github/assets/moji-logo.svg" alt="moji" width="280">

<h1>moji</h1>

<p>
  <a href="https://www.npmjs.com/package/@microck/moji"><img src="https://img.shields.io/npm/v/@microck/moji?style=flat-square&color=000000" alt="npm version badge"></a>
  <img src="https://img.shields.io/npm/dt/@microck/moji?style=flat-square&color=000000" alt="npm total downloads badge">
  <a href="https://github.com/Microck/moji/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Microck/moji/ci.yml?branch=main&style=flat-square&label=ci&color=000000" alt="ci badge"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-000000?style=flat-square" alt="MIT license badge"></a>
</p>


https://github.com/user-attachments/assets/33fafa72-7974-4fb1-b107-98bfef03194a



</div>

---

ask for a font and get the file you actually meant. `moji` searches across font
sources, ranks candidates by family and filename, and downloads the best match.
browse interactively with Bubble Tea, pipe a stable table into shell workflows,
or request JSON for programmatic use.

## quick start

install with the package manager you already use:

```bash
npm install -g @microck/moji
pnpm add -g @microck/moji
bun add -g @microck/moji
```

search for a family:

```bash
moji
# or jump straight to results
moji "Futura"
```

bare `moji` opens the home TUI so you can type a query. pass a query to jump
straight to the live result list. redirect or pipe a queried command to get a
stable table instead.

```bash
moji "Futura" --format otf,ttf
moji "Futura" --format woff2 --json
```

download the best match, preview the choice first, or ask for the whole family:

```bash
moji get "Futura bold" --dry-run
moji get "Futura bold"
moji get "Futura entire family" --download-dir ~/Downloads/moji
```

convert a local desktop font to WOFF2, or restore a WOFF2 font to the TTF or
OTF flavor stored inside it:

```bash
moji convert Inter.ttf
moji convert Inter.woff2
moji convert Inter.otf --to woff2 --output build/Inter.woff2
```

conversion detects the input from its content and never replaces an existing
output file. it changes the font container without changing TrueType or CFF
glyph outlines.

inspect a downloaded TTF, OTF, or WOFF2 font before using it:

```bash
moji inspect Inter.ttf
moji inspect Inter.woff2 --json
```

inspection reads the font's character map and reports exact Unicode script
coverage counts. This answers whether a font includes Cyrillic, Arabic, Han,
or another script without relying on its filename.

## providers

the default GetFonts and registry providers work without an account. GitHub's
repository, tree, and release search also uses its small unauthenticated
allowance. Moji automatically uses an existing authenticated `gh` session when
GitHub CLI is installed. `GITHUB_TOKEN` and `github_token` take precedence and
also enable Code Search and higher limits. the TUI points this out when GitHub
search is limited.

the `websearch` provider automatically uses
[`kagi-cli`](https://github.com/Microck/kagi-cli) when it is installed. Run
`kagi auth` once. Ordinary web pages are ignored. direct CSS font URLs and
bounded ZIP or TAR archive members can become results. configured source
plugins pass through the same HTTPS, format, and download validation boundary.
Direct binary responses with missing or misleading extensions can also be
recognized as ZIP, TAR, or compressed TAR archives by signature; webpages and
interactive download flows remain excluded.

```bash
export GITHUB_TOKEN=github_pat_example
moji "Futura" --provider github
```

do not pass tokens as command-line flags. use `--token-stdin` when a token only
needs to exist for one invocation.

the same `websearch` provider also uses SearXNG when an instance URL is
configured.

## commands

| command | purpose |
| --- | --- |
| `moji` | open the home TUI and type a font query |
| `moji <query>` | search interactively or print a table when piped |
| `moji get <query>` | rank results and download the best match |
| `moji convert <input>` | convert TTF/OTF to WOFF2 or restore WOFF2 |
| `moji inspect <input>` | report Unicode script coverage for a local font |
| `moji config` | create the default config when needed and open `$EDITOR` |
| `moji config show` | print the current config with its token redacted |
| `moji cache clear` | remove cached provider results |

run `moji --help` for the complete flag and example reference.

## download safety

downloads use HTTPS by default and stop at 50 MiB. before the final file appears,
`moji` validates its font magic bytes, sanitizes its filename, writes to a
temporary path, and renames it atomically. SHA-256 hashes prevent duplicate
files from being saved twice.

If the first ranked link returns invalid font bytes, `moji get` remembers that
URL and tries the next candidate. Whole-family downloads validate one coherent
same-source group in staging, so a broken member cannot leave a part