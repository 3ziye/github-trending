<p align="center">
  <img src="assets/plumber.svg" alt="Plumber">
</p>


<p align="center">
  <b>CI/CD compliance scanner for GitLab pipelines</b>
</p>

<p align="center">
  <a href="https://github.com/getplumber/plumber/actions"><img src="https://img.shields.io/github/actions/workflow/status/getplumber/plumber/release.yml?label=Build" alt="Build Status"></a>
  <a href="https://github.com/getplumber/plumber/releases"><img src="https://img.shields.io/github/v/release/getplumber/plumber" alt="Latest Release"></a>
  <img src="https://img.shields.io/github/go-mod/go-version/getplumber/plumber" alt="Go Version">
  <a href="https://github.com/getplumber/plumber/releases"><img src="https://img.shields.io/github/downloads/getplumber/plumber/total?label=Downloads" alt="GitHub Downloads"></a>
  <a href="https://hub.docker.com/r/getplumber/plumber"><img src="https://img.shields.io/docker/pulls/getplumber/plumber" alt="Docker Pulls"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MPL--2.0-blue" alt="License"></a>
</p>

<p align="center">
  <a href="https://getplumber.io">Website</a> •
  <a href="https://discord.gg/932xkSU24f">Discord</a> •
  <a href="https://github.com/getplumber/plumber/issues">Issues</a>
</p>

---

## 🤔 What is Plumber?

Plumber is a compliance scanner for GitLab. It reads your `.gitlab-ci.yml` and repository settings, then checks for security and compliance issues like:

- Container images using mutable tags (`latest`, `dev`)
- Container images from untrusted registries
- Unprotected branches
- Hardcoded jobs not from includes/components
- Outdated includes/templates
- Forbidden version patterns (e.g., `main`, `HEAD`)
- Missing required components or templates

**How does it work?** Plumber connects to your GitLab instance via API, analyzes your pipeline configuration, and reports any issues it finds. You define what's allowed in a config file (`.plumber.yaml`), and Plumber tells you if your project complies.

<p align="center">
  <img src="assets/component.gif" alt="Plumber Demo" width="700">
</p>

> 💡 **Want to see it in action?** Check out our example projects:
> - [go-build-test-compliant](https://gitlab.com/getplumber/examples/go-build-test-compliant/-/pipelines) - A compliant project passing all checks
> - [go-build-test-non-compliant](https://gitlab.com/getplumber/examples/go-build-test-non-compliant/-/pipelines) - A non-compliant project showing detected issues

## 🚀 Two Ways to Use Plumber

Choose **one** of these methods. You don't need both:

| Method | Best for | How it works |
|--------|----------|--------------|
| **[CLI](#option-1-cli)** | Quick evaluation, local testing, one-off scans | Install binary and run from terminal |
| **[GitLab CI Component](#option-2-gitlab-ci-component)** | Automated checks on every pipeline run | Add 2 lines to your `.gitlab-ci.yml` |

---

## 📖 Table of Contents

- [What is Plumber?](#-what-is-plumber)
- [CLI](#option-1-cli)
- [GitLab CI Component](#option-2-gitlab-ci-component)
- [Configuration](#%EF%B8%8F-configuration)
  - [Available Controls](#available-controls)
  - [Outputs](#outputs)
    - [Example Output](#example-output)
- [Installation](#-installation)
- [CLI Reference](#-cli-reference)
- [Self-Hosted GitLab](#%EF%B8%8F-self-hosted-gitlab)
- [Troubleshooting](#-troubleshooting)


---

## Option 1: CLI

**Try Plumber in 2 minutes!** No commits, no CI changes, just run it.

### Step 1: Install

Choose **one** of the following:

#### Homebrew

```bash
brew tap getplumber/plumber
brew install plumber
```

#### Mise

```bash
mise use -g github:getplumber/plumber
```

> Requires [mise activation](https://mise.jdx.dev/getting-started.html#activate-mise) in your shell, or run with `mise exec -- plumber`.

#### Direct Download

```bash
# For Linux/MacOs
curl -LO "https://github.com/getplumber/plumber/releases/latest/download/plumber-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')"
chmod +x plumber-* && sudo mv plumber-* /usr/local/bin/plumber
```

> 📦 See [Installation](#-installation) for Windows, Docker, or building from source.

### Step 2: Generate a Config File

```bash
plumber config generate
```

This creates `.plumber.yaml` with [default](./.plumber.yaml) compliance rules. You can customize it later.

### Step 3: Create & Set Your Token

1. In GitLab, go to **User Settings → Access Tokens** ([direct link](https://gitlab.com/-/user_settings/personal_access_tokens))
2. Create a Personal Access Token with `read_api` + `read_repository` scopes
3. Export it in your terminal:

> ⚠️ **Important:** The token must belong to a user with **Maintainer** role (or higher) on the project to access branch protection settings and other project configurations.

```bash
export GITLAB_TOKEN=glpat-xxxx
```

### Step 4: Run Analysis

Plumber auto-detects the GitLab URL and project from your git remote but requires the remote to be set to 'origin'. 
```bash
# if in git remote with remote = o