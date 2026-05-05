# Dexter

<img src="dexter-logo.png" width="200" height="200" alt="Dexter logo" />

A fast, full-featured Elixir LSP optimized for large Elixir codebases.

## Table of contents

- [Features](#features)
- [Quick start](#quick-start)
- [Editor setup](#editor-setup)
  - [VS Code / Cursor](#vs-code--cursor)
    - [Configuration](#configuration)
  - [Neovim (0.11+)](#neovim-011)
    - [Configuring format on save](#configuring-format-on-save)
  - [Neovim (with nvim-lspconfig — \< 0.11)](#neovim-with-nvim-lspconfig---011)
  - [Zed](#zed)
  - [Emacs](#emacs)
    - [Eglot](#eglot)
      - [Emacs version \>= 30](#emacs-version--30)
      - [Emacs version \<= 29](#emacs-version--29)
    - [lsp-mode](#lsp-mode)
  - [Helix](#helix)
- [Why build another LSP?](#why-build-another-lsp)
- [Performance](#performance)
- [CLI usage](#cli-usage)
  - [Index a project](#index-a-project)
  - [Look up definitions](#look-up-definitions)
  - [Find references](#find-references)
  - [Reindexing files manually](#reindexing-files-manually)
- [Hover documentation](#hover-documentation)
  - [Cursor-position-aware resolution](#cursor-position-aware-resolution)
- [Rename](#rename)
  - [Modules](#modules)
  - [Functions](#functions)
  - [Variables](#variables)
- [Lightning-fast formatting](#lightning-fast-formatting)
- [LSP options](#lsp-options)
- [Index database location (.dexter/)](#index-database-location-dexter)
- [Debugging](#debugging)
- [Development (building from source)](#development-building-from-source)
- [Releasing](#releasing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Fast indexing** — cold index completes in ~11s on a 57k-file Elixir monorepo, ~100ms on Oban, ~300ms on the Elixir standard library (measured on an M1 MacBook Pro). After your first index, incremental indexing makes sure that you never have to reindex the whole codebase again.
- **Go-to-definition** — jump to any module, function, type, or variable definition. Resolves aliases, imports, `defdelegate` chains, `use` injections, and the Elixir stdlib. Handles all definition forms: `def`, `defp`, `defmacro`, `defprotocol`, `defimpl`, `defstruct`, and more.
- **Go-to-references** — find all usages of a function or module across the codebase, including through `import`, `use` chains, and `defdelegate`.
- **Hover documentation** — `@doc`, `@moduledoc`, `@typedoc`, and `@spec` annotations rendered as Markdown when you hover over a symbol.
- **Autocompletion** — modules, functions, types, and variables with full snippet support. Resolves through aliases, imports, `use` injections, and the Elixir stdlib. Works for qualified calls (`MyApp.Accounts.|`), bare function calls, and module prefixes.
- **Rename** — rename modules, functions, and variables with automatic file renaming when the convention is followed.
- **No compilation required** — the index is built by parsing source files directly, not by compiling your project. Dexter works immediately on any codebase, even ones that don't compile.
- **Monorepo and umbrella support** — a single index at the repository root covers all apps and shared libraries. Go-to-definition, find references, and rename work cross-project out of the box.
- **Format on save** — formats `.ex`, `.exs`, and `.heex` files on save via a persistent Elixir process. Near-instant after the first save. Formatter plugins (Styler, Phoenix.LiveView.HTMLFormatter) are loaded from your project's `_build` — no install needed. Syntax errors are surfaced as diagnostics.
- **Elixir stdlib indexing** — jump to `Enum`, `String`, `Mix`, and other bundled modules by indexing your local Elixir installation sources.
- **Signature help** — parameter hints as you type function calls.
- **Workspace symbols** — search for any module or function across the entire codebase.
- **Call hierarchy** — navigate incoming and outgoing calls.
- **Code actions** — add missing aliases with a single action.
- **Document symbols** — outline view of all functions and modules in the current file.
- **Document highlight** — highlight all occurrences of the symbol under the cursor.
- **Variable support** — go-to-definition, rename, and completion for local variables via tree-sitter, with correct scoping across `case`, `with`, `for`, and other block constructs.
- **Git branch switch detection** — automatically reindexes when you switch branches.

<details>
<summary>More features</summary>

- **Delegate following** — `defdelegate fetch_user(id), to: MyApp.Accounts.Finders.FetchUser, as: :find` jumps to `MyApp.Accounts.Finders.FetchUser.find`, respecting `as:` renames.
- **Alias resolution** — `alias MyApp.Handlers.Foo`, `alias MyApp.Handlers.Foo, as: Cool`, `alias MyApp.Handlers.{Foo, Bar}`.
- **Import resolution** — bare function calls resolved through `import` declarations.
- **Type definitions** — `@type` and `@opaque` are indexed for go-to-definition and hover.
- **Folding ranges** — collapse functions and modules in your editor.
- **Monorepo-aware formatting** —