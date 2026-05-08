![](media/dockerfile-image.png)

![](media/screenshot-1.png)

![](media/screenshot-2.png)

![](media/screenshot-3.png)

# droast

a dockerfile linter that actually has opinions. it catches bad practices and tells you about them in the least diplomatic way possible.

think of it as code review from a senior dev who's seen too many prod incidents and has stopped being polite about it.

## vs code extension

install from the marketplace and get inline squiggles as you type:

![VS Code](https://img.shields.io/badge/VSCode-007ACC?logo=visualstudiocode&logoColor=white&style=flat)

**[droast — Dockerfile Linter](https://marketplace.visualstudio.com/items?itemName=ImmanuelTikhonov.droast)**

```bash
code --install-extension ImmanuelTikhonov.droast
```

the binary is bundled — no separate install needed. findings appear in real time with roast messages on hover.

## install

**one-liner** (macOS and Linux, detects Homebrew automatically):

```bash
curl -fsL ewry.net/droast/install.sh | sh
```

**Homebrew** (macOS and Linux):

```bash
brew tap immanuwell/droast https://github.com/immanuwell/homebrew-droast.git
brew install immanuwell/droast/droast
```

**from source:**

```bash
cargo install dockerfile-roast
```

or grab a prebuilt binary from the releases page if you'd rather not wait for the rust compiler to do its thing.

## usage

```bash
# the basics
droast Dockerfile

# lint an entire project
droast **/Dockerfile

# boring mode (no roasts, just facts)
droast --no-roast Dockerfile

# only care about real problems
droast --min-severity warning Dockerfile

# disagree with a rule? valid, we respect it
droast --skip DF001,DF012 Dockerfile

# ci-friendly output
droast --format github Dockerfile    # github actions annotations
droast --format json Dockerfile      # machine-readable
droast --format compact Dockerfile   # one line per finding
droast --format sarif Dockerfile     # SARIF 2.1.0 for GitHub Advanced Security / IDEs
```

## configuration

droast works out of the box with zero configuration. for teams that want to commit project-level defaults, drop a `droast.toml` in the repo root:

```toml
# droast.toml — all fields optional
skip        = ["DF012", "DF022"]  # rules to suppress project-wide
min-severity = "warning"          # hide info-level findings
no-roast    = false               # true = technical output only
no-fail     = false               # true = never block CI
format      = "terminal"          # terminal | json | github | compact
```

droast searches for `droast.toml` starting from the current directory, walking up to the nearest `.git` root. CLI flags always take precedence over the file — the file just sets the defaults so you don't repeat yourself.

`skip` is the most useful field for CI pipelines: add rules your team has consciously accepted (e.g. you ship without HEALTHCHECK by design) so developers don't drown in noise they can't act on.

## github action

add droast to any repo in 5 lines:

```yaml
- uses: immanuwell/dockerfile-roast@1.3.0
```

full example (`.github/workflows/lint.yml`):

```yaml
name: Lint Dockerfiles

on: [push, pull_request]

jobs:
  droast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: immanuwell/dockerfile-roast@1.3.0
```

findings show up as inline annotations on the PR diff. no configuration required.

available inputs (all optional):

| input | default | description |
|-------|---------|-------------|
| `files` | `Dockerfile` | file(s) or glob to lint |
| `min-severity` | `info` | `info`, `warning`, or `error` |
| `skip` | — | comma-separated rule IDs to ignore |
| `no-roast` | `false` | technical output only, no jokes |
| `no-fail` | `false` | advisory mode — never blocks the build |
| `image-tag` | `latest` | pin to a specific droast release, e.g. `1.3.0` |

example with options:

```yaml
- uses: immanuwell/dockerfile-roast@1.3.0
  with:
    files: '**/Dockerfile'
    min-severity: warning
    skip: DF012,DF022
    no-fail: true        # report findings but don't block the PR
```

## docker

pull from ghcr and use immediately, no install needed:

```bash
# lint a Dockerfile in the current directory
docker run --rm -v "$(pwd)/Dockerfile":/Dockerfile ghcr.io/immanuwell/droast /Dockerfile

# lint any file, anywhere
docker run --rm -v /path/to/your/Dockerfile:/Dockerfile ghcr.io/immanuwell/droast /Dockerfile

# pass flags as usual
docker run --rm -v "$(pwd)/Dockerfile":/Dockerfile ghcr.io/immanuwell/droast \
    --no-roast --min-severity warning /Dockerfile
```

or build locally from source:

```bash
docker build -t droast .
docker run --rm -v "$(pwd)/Dockerfile":/Dockerfile droast /Dockerfile
```

the image is published automatically to `ghcr.io/immanuwell/droast` on every release tag.

## shell completions

add this once, never mistype `--min-severity` again:

```bash
# bash — add to .bashrc
source <(droast completion bash)

# zsh — add to .zshrc
droast completion zsh > ~/.zfunc/_droast

# fish — add to config.fish
droast co