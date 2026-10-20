<div align="center">

<a href="https://jactionlint.jdx.dev"><img src="https://jactionlint.jdx.dev/logo.svg" alt="" width="88" height="88"></a>

# jactionlint

**Catch broken and insecure GitHub Actions workflows before they run.**

[![CI status](https://github.com/jdx/jactionlint/actions/workflows/ci.yaml/badge.svg)](https://github.com/jdx/jactionlint/actions/workflows/ci.yaml)
[![Latest release](https://img.shields.io/github/v/release/jdx/jactionlint?label=release&color=0f766e)](https://github.com/jdx/jactionlint/releases/latest)
[![Go reference](https://pkg.go.dev/badge/github.com/jdx/jactionlint/v2.svg)](https://pkg.go.dev/github.com/jdx/jactionlint/v2)

[Documentation](https://jactionlint.jdx.dev) · [Playground](https://jactionlint.jdx.dev/playground) · [Rules](https://jactionlint.jdx.dev/rules) · [Changelog](https://github.com/jdx/jactionlint/blob/main/CHANGELOG.md)

</div>

jactionlint is a static checker for GitHub Actions. It reads your workflows, composite actions and `dependabot.yml` and reports two kinds of problems: the mistakes that make a run fail or misbehave, and the patterns that let an outsider run code in your repository or steal its token. It started as a fork of [actionlint](https://github.com/rhysd/actionlint) and covers its checks, and its security rules follow the audits of [zizmor](https://github.com/zizmorcore/zizmor).

- **Correctness.** Unknown keys and events, type errors in `${{ }}` expressions, wrong inputs of actions and reusable workflows, and broken `needs:`, cron and glob patterns. [shellcheck](https://github.com/koalaman/shellcheck) and [pyflakes](https://github.com/PyCQA/pyflakes) check the scripts of `run:` steps.
- **Security.** Script injection, excessive token permissions, dangerous triggers such as `pull_request_target`, cache poisoning, credentials left in the checkout and AI agent actions that outsiders can steer.
- **Policy.** Actions used by a tag instead of a commit, and workflows without `permissions:`, a job timeout or a concurrency group.
- **Fixes.** `jactionlint --fix` repairs what has a mechanical fix, and `--diff` shows the change first.
- **Gradual adoption.** Profiles choose how much is checked, and a baseline fails the build only on new findings.
- **No network unless you ask.** The [online checks](https://jactionlint.jdx.dev/online), which ask GitHub about archived repositories, impostor commits and published advisories, run only with `--online`.

Try it without installing anything in the [playground](https://jactionlint.jdx.dev/playground), which runs jactionlint in your browser.

<a id="quick-start"></a>
## Quick start

Install jactionlint with [mise](https://mise.jdx.dev) and run it at the root of a repository:

```sh
mise use -g jactionlint
jactionlint
```

With no arguments, jactionlint checks the workflows, composite actions, `dependabot.yml` and Actions lock file of the repository. Pass file names to check only those, or `-` to read standard input. It exits with status 1 when a finding of level `error` is left.

Other ways to install it:

- **Homebrew:** `brew tap jdx/jactionlint https://github.com/jdx/jactionlint`, then `brew install --cask jdx/jactionlint/jactionlint`.
- **PyPI:** `uvx jactionlint` runs it without installing it, and `pipx install jactionlint` or `uv tool install jactionlint` installs it.
- **Docker:** the image `ghcr.io/jdx/jactionlint` also holds shellcheck and pyflakes. [Run the image](https://jactionlint.jdx.dev/ci#run-the-image) shows the command.
- **Go:** `go install github.com/jdx/jactionlint/v2/cmd/jactionlint@latest`.
- **Release archives:** download the archive for your platform from the [releases](https://github.com/jdx/jactionlint/releases) and [verify it](https://jactionlint.jdx.dev/install#verify-the-download).

Packages named `actionlint`, as in Homebrew core, install the original project, not this fork. [Installation](https://jactionlint.jdx.dev/install) covers every method.

## Example

This workflow has a typo in a trigger, untrusted input in a script and an undefined matrix property. It also uses an action by tag and sets no permissions, timeout or concurrency group. Save it as `test.yaml`:

<!-- demo:input -->
```yaml
on:
  push:
    branch: main
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "${{ github.event.head_commit.message }}"
      - run: echo "${{ matrix.os }}"
```

`jactionlint test.yaml` prints each finding with its position, a message, the line it points at and, in brackets, the ID of its rule:

<!-- demo:output -->
```
test.yaml:1:1: workflow has no "concurrency:", so every run of it executes at the same time even when a newer run supersedes the older ones. add a top-level "concurrency:" with a "group:" and "cancel-in-progress: true" [concurrency-limits]
  |
1 | on:
  | ^~~
test.yaml:3:5: unexpected key "branch" for "push" section. expected one of "branches", "branches-ignore", "paths", "paths-ignore", "tags", "tags-ignore", "types", "w