# 🤖 `sidekick.nvim`

**sidekick.nvim** is your Neovim AI sidekick that integrates Copilot LSP's
"Next Edit Suggestions" with a built-in terminal for any AI CLI.
Review and apply diffs, chat with AI assistants, and streamline your coding,
without leaving your editor.

<img width="2311" height="1396" alt="image" src="https://github.com/user-attachments/assets/63a33610-9a8e-45e2-bbd0-b7e3a4fde621" />

## ✨ Features

- **🤖 Next Edit Suggestions (NES) powered by Copilot LSP**
  - 🪄 **Automatic Suggestions**: Fetches suggestions automatically when you pause typing or move the cursor.
  - 🎨 **Rich Diffs**: Visualizes changes with inline and block-level diffs, featuring Treesitter-based syntax highlighting with granular diffing down to the word or character level.
  - 🧭 **Hunk-by-Hunk Navigation**: Jump through edits to review them one by one before applying.
  - 📊 **Statusline Integration**: Shows Copilot LSP's status, request progress, and preview text in your statusline.

- **💬 Integrated AI CLI Terminal**
  - 🚀 **Direct Access to AI CLIs**: Interact with your favorite AI command-line tools without leaving Neovim.
  - 📦 **Pre-configured for Popular Tools**: Out-of-the-box support for Claude, Gemini, Grok, Codex, Copilot CLI, and more.
  - ✨ **Context-Aware Prompts**: Automatically include file content, cursor position, and diagnostics in your prompts.
  - 📝 **Prompt Library**: A library of pre-defined prompts for common tasks like explaining code, fixing issues, or writing tests.
  - 🔄 **Session Persistence**: Keep your CLI sessions alive with `tmux` and `zellij` integration.
  - 📂 **Automatic File Watching**: Automatically reloads files in Neovim when they are modified by AI tools.

- **🔌 Extensible and Customizable**
  - ⚙️ **Flexible Configuration**: Fine-tune every aspect of the plugin to your liking.
  - 🧩 **Plugin-Friendly API**: A rich API for integrating with other plugins and building custom workflows.
  - 🎨 **Customizable UI**: Change the appearance of diffs, signs, and more.

## 📋 Requirements

- **Neovim** `>= 0.11.2` or newer
- The official [copilot-language-server](https://github.com/github/copilot-language-server-release) LSP server,
  enabled with `vim.lsp.enable`. Can be installed in multiple ways:
  1. install using `npm` or your OS's package manager
  2. install with [mason-lspconfig.nvim](https://github.com/mason-org/mason-lspconfig.nvim)
  3. [copilot.lua](https://github.com/zbirenbaum/copilot.lua) and [copilot.vim](https://github.com/github/copilot.vim)
     both bundle the LSP Server in their plugin.
- A working `lsp/copilot.lua` configuration.
  - **TIP:** Included in [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)
- [snacks.nvim](https://github.com/folke/snacks.nvim) for better prompt/tool selection **_(optional)_**
- [nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) **_(`main` branch)_** for `{function}` and `{class}` context variables **_(optional)_**
- AI cli tools, such as Codex, Claude, Copilot, Gemini, … **_(optional)_**
  see the [🤖 AI CLI Integration](#-ai-cli-integration) section for details.

## 🚀 Quick Start

1. **Install** the plugin with your package manager (see below)
2. **Configure Copilot LSP** - must be enabled with `vim.lsp.enable`
3. **Check health**: `:checkhealth sidekick`
4. **Sign in to Copilot**: `:LspCopilotSignIn`
5. **Try it out**:
   - Type some code and pause - watch for Next Edit Suggestions appearing
   - Press `<Tab>` to navigate through or apply suggestions
   - Use `<leader>aa` to open AI CLI tools

> [!NOTE]
> **New to Next Edit Suggestions?** Unlike inline completions, NES suggests entire refactorings or multi-line changes anywhere in your file - think of it as Copilot's "big picture" suggestions.

## 📦 Installation

Install with your favorite manager. With [lazy.nvim](https://github.com/folke/lazy.nvim):

<!-- setup_base:start -->

```lua
{
  "folke/sidekick.nvim",
  opts = {
    -- add any options here
    cli = {
      mux = {
        backend = "zellij",
        enabled = true,
      },
    },
  },
  -- stylua: ignore
  keys = {
    {
      "<tab>",
      function()
        -- if there is a next edit, jump to it, otherwise apply it if any
        if not require("sidekick").nes_jump_or_apply() then
          return "<Tab>" -- fallback to normal tab
        end
      end,
      expr = true,
      desc = "Goto/Apply Next Edit Suggestion",
    },
    {
      "<leader>aa",
      function() require("sidekick.cli").toggle() end,
      desc = "Sidekick Toggle CLI",
    },
    {
      "<leader>as",
      function() require("sidekick.cli").select() end,
      -- Or to select only installed tools:
      -- require("sidekick.cli").select({ filter = { installed = true } })
      desc = "Select CLI",
    },
    {
      "<leader>at",
      function() require("sidekick.cli").send({ msg = "{this}" }) end,
      mode = { "x", "n" },
      desc = "Send This",
    },
    {
      "<leader>av",
      function() requ