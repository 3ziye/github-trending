# Unofficial App Store Connect CLI

<p align="center">
  <img src="https://img.shields.io/badge/Go-1.24+-00ADD8?style=for-the-badge&logo=go" alt="Go Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Homebrew-compatible-blue?style=for-the-badge" alt="Homebrew">
</p>

A **fast**, **lightweight**, and **scriptable** CLI for App Store Connect. Automate your iOS app workflows from your IDE/terminal.

## Why ASC?

| Problem | Solution |
|---------|----------|
| Manual App Store Connect work | Automate everything from CLI |
| Slow, heavy tooling | Single Go binary, instant startup |
| Poor scripting support | JSON output, explicit flags, clean exit codes |

## Table of Contents

- [Why ASC?](#why-asc)
- [Quick Start](#quick-start)
  - [Install](#install)
  - [Authenticate](#authenticate)
- [Commands](#commands)
  - [Scripting Tips](#scripting-tips)
  - [TestFlight](#testflight)
  - [Beta Groups](#beta-groups)
  - [Beta Testers](#beta-testers)
  - [Devices](#devices)
  - [App Store](#app-store)
  - [App Tags](#app-tags)
  - [App Events](#app-events)
  - [Alternative Distribution](#alternative-distribution)
  - [Analytics & Sales](#analytics--sales)
  - [Finance Reports](#finance-reports)
  - [Sandbox Testers](#sandbox-testers)
  - [Xcode Cloud](#xcode-cloud)
  - [Game Center](#game-center)
  - [Apps & Builds](#apps--builds)
- [App Setup](#app-setup)
  - [Categories](#categories)
  - [Versions](#versions)
  - [App Info](#app-info)
  - [Pre-Release Versions](#pre-release-versions)
  - [Localizations](#localizations)
  - [Build Localizations](#build-localizations)
  - [Migrate (Fastlane Compatibility)](#migrate-fastlane-compatibility)
  - [Submit](#submit)
  - [Utilities](#utilities)
  - [Output Formats](#output-formats)
  - [Authentication](#authentication)
- [Design Philosophy](#design-philosophy)
  - [Explicit Over Cryptic](#explicit-over-cryptic)
  - [JSON-First Output](#json-first-output)
  - [No Interactive Prompts](#no-interactive-prompts)
- [Installation](#installation)
- [Documentation](#documentation)
- [How to test in <10 minutes](#how-to-test-in-10-minutes)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Star History](#star-history)

## Quick Start

### Install

```bash
# Via Homebrew (recommended)
brew tap rudrankriyam/tap
brew install rudrankriyam/tap/asc

# Install script (macOS/Linux)
curl -fsSL https://raw.githubusercontent.com/rudrankriyam/App-Store-Connect-CLI/main/install.sh | bash

# Installs to ~/.local/bin by default (ensure it's on your PATH)

# Or build from source
git clone https://github.com/rudrankriyam/App-Store-Connect-CLI.git
cd App-Store-Connect-CLI
make build
./asc --help
```

### Updates

`asc` checks for updates on startup and auto-updates when installed via the GitHub release install script. Homebrew installs will show a `brew upgrade` hint instead. Disable update checks with `--no-update` or `ASC_NO_UPDATE=1`.

### Authenticate

```bash
# Register your App Store Connect API key
asc auth login \
  --name "MyApp" \
  --key-id "ABC123" \
  --issuer-id "DEF456" \
  --private-key /path/to/AuthKey.p8

# Validate credentials via network during login
asc auth login \
  --network \
  --name "MyApp" \
  --key-id "ABC123" \
  --issuer-id "DEF456" \
  --private-key /path/to/AuthKey.p8

# Skip JWT + network validation (useful in CI)
asc auth login \
  --skip-validation \
  --name "MyApp" \
  --key-id "ABC123" \
  --issuer-id "DEF456" \
  --private-key /path/to/AuthKey.p8

# Add another profile and switch defaults
asc auth login \
  --name "ClientApp" \
  --key-id "XYZ789" \
  --issuer-id "LMN000" \
  --private-key /path/to/ClientAuthKey.p8

asc auth switch --name "ClientApp"

# Use a profile for a single command
asc --profile "ClientApp" apps list

# Fail if credentials resolve from mixed sources
asc --strict-auth apps list

# Create a template config.json (global, no secrets)
asc auth init

# Create a repo-local config.json
asc auth init --local

# Store credentials in global config.json (bypass keychain)
asc auth login \
  --bypass-keychain \
  --name "MyApp" \
  --key-id "ABC123" \
  --issuer-id "DEF456" \
  --private-key /path/to/AuthKey.p8

# Store credentials in repo-local config.json
asc auth login \
  --bypass-keychain \
  --local \
  --name "MyApp" \
  --key-id "ABC123" \
  --issuer-id "DEF456" \
  --private-key /path/to/AuthKey.p8
```

Generate API keys at: https://appstoreconnect.apple.com/access/integrations/api

Open the API keys page in your browser:
```bash
asc auth init --open
```

Credentials are stored in the system keychain when available, with a config fallback
at `~/.asc/config.json` (restricted permissions). A repo-local `./.asc/config.json`
takes precedence when present. Override with `ASC_CONFIG_PATH`. When
`ASC_BYPASS_KEYCHAIN` is set and environment credentials are fully provided, the
environment values take precedence ov