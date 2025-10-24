# 🔐 fnox

**Fort Knox for your secrets.**

[![CI](https://github.com/jdx/fnox/actions/workflows/ci.yml/badge.svg)](https://github.com/jdx/fnox/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is fnox?

Secrets are done in 2 ways:

1. In git, encrypted (hopefully)
2. Remote, typically a cloud provider like AWS KMS

fnox works with either—or both! They've got their pros and cons. Either way, fnox gives you a
nice front-end to manage secrets and make them easy to work with in dev/ci/prod.

fnox's config file, `fnox.toml`, will either contain the encrypted secrets, or a reference to a secret in a cloud provider. You can either use `fnox exec -- <command>` to run a command with the secrets, or you can use the [shell integration](#shell-integration) to automatically load the secrets into your shell environment when you `cd` into a directory with a `fnox.toml` file.

## Supported Providers

fnox works with all the things:

### 🔐 Encryption (secrets in git, encrypted)

- `age` - Modern encryption (works with SSH keys!)
- `aws-kms` - AWS Key Management Service
- `azure-kms` - Azure Key Vault encryption
- `gcp-kms` - Google Cloud KMS

### ☁️ Cloud Secret Storage (remote, centralized)

- `aws-sm` - AWS Secrets Manager
- `azure-sm` - Azure Key Vault Secrets
- `gcp-sm` - Google Cloud Secret Manager
- `vault` - HashiCorp Vault

### 🔑 Password Managers

- `1password` - 1Password CLI
- `bitwarden` - Bitwarden/Vaultwarden

### 💻 Local Storage

- `keychain` - OS Keychain (macOS/Windows/Linux)
- `plain` - Plain text (for defaults only!)

## Installation

### Using mise (recommended)

The easiest way to install fnox is with [mise](https://mise.jdx.dev):

```bash
mise use -g fnox
```

### Using Cargo

```bash
cargo install fnox
```

### From Source

```bash
git clone https://github.com/jdx/fnox
cd fnox
cargo install --path .
```

## Quick Start

```bash
# Initialize fnox in your project
fnox init

# Set a secret (stores it encrypted in fnox.toml)
fnox set DATABASE_URL

# Get a secret
fnox get DATABASE_URL

# Run commands with secrets loaded as env vars
fnox exec -- npm start

# Enable shell integration (auto-load secrets on cd)
eval "$(fnox activate bash)"  # or zsh, fish
```

## How It Works

fnox uses a simple TOML config file (`fnox.toml`) that you check into git. Secrets are either:

1. **Encrypted inline** - The encrypted ciphertext lives in the config file
2. **Remote references** - The config contains a reference (like "my-db-password") that points to a secret in AWS/1Password/etc.

You configure providers (encryption methods or cloud services), then assign each secret to a provider. fnox handles the rest.

```toml
# fnox.toml
[providers.age]
type = "age"
recipients = ["age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p"]

[secrets.DATABASE_URL]
provider = "age"
value = "YWdlLWVuY3J5cHRpb24uLi4="  # ← encrypted ciphertext, safe to commit

[secrets.API_KEY]
default = "dev-key-12345"  # ← plain default value for local dev
```

When you run `fnox get DATABASE_URL`, it decrypts the value using your age key. When you run `fnox exec`, all secrets are loaded as environment variables.

## Shell Integration

fnox can automatically load secrets when you `cd` into directories with a `fnox.toml` file:

```bash
# Enable it once
eval "$(fnox activate bash)"  # or zsh, fish

# Add to your shell config for persistence
echo 'eval "$(fnox activate bash)"' >> ~/.bashrc
```

Now secrets auto-load on directory changes:

```bash
~/projects $ cd my-app
fnox: +3 DATABASE_URL, API_KEY, JWT_SECRET
~/projects/my-app $ cd ..
fnox: -3 DATABASE_URL, API_KEY, JWT_SECRET
```

Control the output with `FNOX_SHELL_OUTPUT`:

- `export FNOX_SHELL_OUTPUT=none` - Silent mode
- `export FNOX_SHELL_OUTPUT=normal` - Show count and keys (default)
- `export FNOX_SHELL_OUTPUT=debug` - Verbose debugging

Use profiles for different environments:

```bash
export FNOX_PROFILE=production
cd my-app  # Loads production secrets
```

## Why is this a standalone CLI and not part of mise?

mise has support for [encrypted secrets](https://mise.jdx.dev/environments/secrets/) but mise's design makes it a poor fit for remote secrets. mise reloads
its environment too frequently—whenever a directory is changed, `mise x` is run, a shim is called, etc. Any other use-case like this mise leverages caching
but secrets are an area where caching is a bad idea for obvious reasons. It might be possible to change mise's design to retain its environment in part to
better support something like this but that's a huge challenge.

Basically it's just too hard to get remote secrets to work effectively with mise so I made this a standalone tool.

---

## Providers: Complete Getting Started Guides

Each provider below is a complete standalone guide. Choose the ones that fit your workflow.

### Age Encryption

**Use age when:** You want secrets in git, encrypted, with minimal setup. Perfect for d