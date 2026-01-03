# Mistral Vibe

[![PyPI Version](https://img.shields.io/pypi/v/mistral-vibe)](https://pypi.org/project/mistral-vibe)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/release/python-3120/)
[![CI Status](https://github.com/mistralai/mistral-vibe/actions/workflows/ci.yml/badge.svg)](https://github.com/mistralai/mistral-vibe/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/mistralai/mistral-vibe)](https://github.com/mistralai/mistral-vibe/blob/main/LICENSE)

```
██████████████████░░
██████████████████░░
████  ██████  ████░░
████    ██    ████░░
████          ████░░
████  ██  ██  ████░░
██      ██      ██░░
██████████████████░░
██████████████████░░
```

**Mistral's open-source CLI coding assistant.**

Mistral Vibe is a command-line coding assistant powered by Mistral's models. It provides a conversational interface to your codebase, allowing you to use natural language to explore, modify, and interact with your projects through a powerful set of tools.

> [!WARNING]
> Mistral Vibe works on Windows, but we officially support and target UNIX environments.

### One-line install (recommended)

**Linux and macOS**

```bash
curl -LsSf https://mistral.ai/vibe/install.sh | bash
```

**Windows**

First, install uv
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then, use uv command below.

### Using uv

```bash
uv tool install mistral-vibe
```

### Using pip

```bash
pip install mistral-vibe
```

## Features

- **Interactive Chat**: A conversational AI agent that understands your requests and breaks down complex tasks.
- **Powerful Toolset**: A suite of tools for file manipulation, code searching, version control, and command execution, right from the chat prompt.
  - Read, write, and patch files (`read_file`, `write_file`, `search_replace`).
  - Execute shell commands in a stateful terminal (`bash`).
  - Recursively search code with `grep` (with `ripgrep` support).
  - Manage a `todo` list to track the agent's work.
- **Project-Aware Context**: Vibe automatically scans your project's file structure and Git status to provide relevant context to the agent, improving its understanding of your codebase.
- **Advanced CLI Experience**: Built with modern libraries for a smooth and efficient workflow.
  - Autocompletion for slash commands (`/`) and file paths (`@`).
  - Persistent command history.
  - Beautiful Themes.
- **Highly Configurable**: Customize models, providers, tool permissions, and UI preferences through a simple `config.toml` file.
- **Safety First**: Features tool execution approval.

## Quick Start

1. Navigate to your project's root directory:

   ```bash
   cd /path/to/your/project
   ```

2. Run Vibe:

   ```bash
   vibe
   ```

3. If this is your first time running Vibe, it will:

   - Create a default configuration file at `~/.vibe/config.toml`
   - Prompt you to enter your API key if it's not already configured
   - Save your API key to `~/.vibe/.env` for future use

4. Start interacting with the agent!

   ```
   > Can you find all instances of the word "TODO" in the project?

   🤖 The user wants to find all instances of "TODO". The `grep` tool is perfect for this. I will use it to search the current directory.

   > grep(pattern="TODO", path=".")

   ... (grep tool output) ...

   🤖 I found the following "TODO" comments in your project.
   ```

## Usage

### Interactive Mode

Simply run `vibe` to enter the interactive chat loop.

- **Multi-line Input**: Press `Ctrl+J` or `Shift+Enter` for select terminals to insert a newline.
- **File Paths**: Reference files in your prompt using the `@` symbol for smart autocompletion (e.g., `> Read the file @src/agent.py`).
- **Shell Commands**: Prefix any command with `!` to execute it directly in your shell, bypassing the agent (e.g., `> !ls -l`).

You can start Vibe with a prompt with the following command:

```bash
vibe "Refactor the main function in cli/main.py to be more modular."
```

**Note**: The `--auto-approve` flag automatically approves all tool executions without prompting. In interactive mode, you can also toggle auto-approve on/off using `Shift+Tab`.

### Programmatic Mode

You can run Vibe non-interactively by piping input or using the `--prompt` flag. This is useful for scripting.

```bash
vibe --prompt "Refactor the main function in cli/main.py to be more modular."
```

by default it will use `auto-approve` mode.

### Slash Commands

Use slash commands for meta-actions and configuration changes during a session.

## Configuration

Vibe is configured via a `config.toml` file. It looks for this file first in `./.vibe/config.toml` and then falls back to `~/.vibe/config.toml`.

### API Key Configuration

Vibe supports multiple ways to configure your API keys:

1. **Interactive Setup (Recommended for first-time users)**: When you run Vibe for the first time or if your API key is missing, Vibe will prompt you to enter it. The ke