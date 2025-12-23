# lockenv

Simple, CLI-friendly secret storage that lets you safely commit encrypted secrets to version control.

> For small teams who want something simpler than sops/git-crypt for .env and infra secrets.

## Overview

lockenv provides a secure way to store sensitive files (like `.env` files, configuration files, certificates) in an encrypted `.lockenv` file that can be safely committed to your repository. Files are encrypted using a password-derived key and can be easily extracted when needed.

## How is this different?

| Feature         | lockenv              | git-crypt                | sops                      |
|-----------------|----------------------|--------------------------|---------------------------|
| Format          | Single vault file    | Transparent per-file     | YAML/JSON native          |
| Auth            | Password + Keyring   | GPG keys                 | KMS/PGP                   |
| Git integration | Manual (lock/unlock) | Transparent (git filter) | Manual                    |
| Setup           | `lockenv init`       | GPG key exchange         | KMS/key config            |
| Best for        | Simple .env/config   | Large teams, many devs   | Cloud infra, key rotation |

## Installation

### Homebrew (macOS/Linux)

```bash
brew tap illarion/tap
brew install lockenv
```

### Debian/Ubuntu

Download the `.deb` file from the [latest release](https://github.com/illarion/lockenv/releases/latest):

```bash
sudo dpkg -i lockenv_*_linux_amd64.deb
```

### Fedora/RHEL

Download the `.rpm` file from the [latest release](https://github.com/illarion/lockenv/releases/latest):

```bash
sudo rpm -i lockenv_*_linux_amd64.rpm
```

### Binary Download

Download pre-built binaries from [GitHub Releases](https://github.com/illarion/lockenv/releases/latest).

Available for:
- Linux (amd64, arm64)
- macOS (amd64, arm64)
- Windows (amd64, arm64)

### Go Install

```bash
go install github.com/illarion/lockenv@latest
```

## Shell Completions

Shell completions are **automatically installed** when using Homebrew, deb, or rpm packages.

For manual installation (binary download or `go install`):

```bash
# Bash - add to ~/.bashrc
eval "$(lockenv completion bash)"

# Zsh - add to ~/.zshrc
eval "$(lockenv completion zsh)"

# Fish - add to ~/.config/fish/config.fish
lockenv completion fish | source

# PowerShell - add to $PROFILE
lockenv completion powershell | Out-String | Invoke-Expression
```

## Quick Start

```bash
# Initialize lockenv in your project
lockenv init

# Lock (encrypt and store) sensitive files
lockenv lock .env config/secrets.json

# Later, unlock (decrypt and restore) files with your password
lockenv unlock
```

## Git Integration

lockenv is designed for version control: ignore your sensitive files, commit only the encrypted `.lockenv` vault.

### Basic Setup

Add to your `.gitignore`:

```gitignore
# Sensitive files - these are stored encrypted in .lockenv
.env
.env.*
*.key
*.pem
secrets/

# Keep the encrypted vault (negation pattern)
!.lockenv
```

The `!.lockenv` negation ensures the vault is tracked even if broader patterns (like `.*`) would exclude it.

### Project-Specific Examples

**Some software project:**
```gitignore
.env
.env.local
.env.production
config/secrets.json
!.lockenv
```

**Terraform project:**
```gitignore
*.tfvars
terraform.tfstate
terraform.tfstate.backup
.terraform/
!.lockenv
```

## Commands

### `lockenv init`
Creates a `.lockenv` vault file in the current directory. Prompts for a password that will be used for encryption. The password is not stored anywhere - you must remember it.

```bash
$ lockenv init
Enter password:
Confirm password:
initialized: .lockenv
```

### `lockenv lock <file> [file...]`
Encrypts and stores files in the vault. Supports glob patterns for multiple files.

```bash
# Lock a single file
$ lockenv lock .env
Enter password:
locking: .env
encrypted: .env
locked: 1 files into .lockenv

# Lock multiple files with glob pattern
$ lockenv lock "config/*.env"
Enter password:
locking: config/dev.env
locking: config/prod.env
encrypted: config/dev.env
encrypted: config/prod.env
locked: 2 files into .lockenv
```

**Options:**
- `-r, --remove` - Remove original files after locking

```bash
$ lockenv lock .env --remove
Enter password:
locking: .env
encrypted: .env
removed: .env
locked: 1 files into .lockenv
```

### `lockenv unlock [file...]`
Decrypts and restores files from the vault with smart conflict resolution.

```bash
# Unlock all files
$ lockenv unlock
Enter password:
unlocked: .env
unlocked: config/database.yml

unlocked: 2 files

# Unlock specific file
$ lockenv unlock .env
Enter password:
unlocked: .env

unlocked: 1 files

# Unlock files matching pattern
$ lockenv unlock "config/*.env"
Enter password:
unlocked: config/dev.env
unlocked: config/prod.env

unlocked: 2 files
```

**Smart Conflict Resolution:**
When a file exists locally and differs from the vault version, you have multiple options:

**Interactive Mode (default):**
- `[l]` Keep lo