# SemTools

> Semantic search and document parsing tools for the command line

A collection of high-performance CLI tools for document processing and semantic search, built with Rust for speed and reliability.

- **`parse`** - Parse documents (PDF, DOCX, etc.) using, by default, the LlamaParse API into markdown format
- **`search`** - Local semantic keyword search using multilingual embeddings with cosine similarity matching and per-line context matching
- **`workspace`** - Workspace management for accelerating search over large collections

**NOTE:** By default, `parse` uses LlamaParse as a backend. Get your API key today for free at [https://cloud.llamaindex.ai](https://cloud.llamaindex.ai). `search` remains local-only.

## Key Features

- **Fast semantic search** using model2vec embeddings from [minishlab/potion-multilingual-128M](https://huggingface.co/minishlab/potion-multilingual-128M)
- **Reliable document parsing** with caching and error handling  
- **Unix-friendly** design with proper stdin/stdout handling
- **Configurable** distance thresholds and returned chunk sizes
- **Multi-format support** for parsing documents (PDF, DOCX, PPTX, etc.)
- **Concurrent processing** for better parsing performance
- **Workspace management** for efficient document retrieval over large collections

## Installation

Prerequisites:

- For the `parse` tool: LlamaIndex Cloud API key

Install:

You can install `semtools` via npm:

```bash
npm i -g @llamaindex/semtools
```

Or via cargo:

```bash
# install entire crate
cargo install semtools

# install only parse
cargo install semtools --no-default-features --features=parse

# install only search
cargo install semtools --no-default-features --features=search
```

Note: Installing from npm builds the Rust binaries locally during install if a prebuilt binary is not available, which requires Rust and Cargo to be available in your environment. Install from `rustup` if needed: `https://www.rust-lang.org/tools/install`.

## Quick Start

Basic Usage:

```bash
# Parse some files
parse my_dir/*.pdf

# Search some (text-based) files
search "some keywords" *.txt --max-distance 0.3 --n-lines 5

# Combine parsing and search
parse my_docs/*.pdf | xargs search "API endpoints"
```

Advanced Usage:

```bash
# Combine with grep for exact-match pre-filtering and distance thresholding
parse *.pdf | xargs cat | grep -i "error" | search "network error" --max-distance 0.3

# Pipeline with content search (note the 'cat')
find . -name "*.md" | xargs parse | xargs search "installation"

# Combine with grep for filtering (grep could be before or after parse/search!)
parse docs/*.pdf | xargs search "API" | grep -A5 "authentication"

# Save search results
parse report.pdf | xargs cat | search "summary" > results.txt
```

Using Workspaces:

```bash
# Create or select a workspace
# Workspaces are stored in ~/.semtools/workspaces/
workspace use my-workspace
> Workspace 'my-workspace' configured.
> To activate it, run:
>   export SEMTOOLS_WORKSPACE=my-workspace
> 
> Or add this to your shell profile (.bashrc, .zshrc, etc.)

# Activate the workspace
export SEMTOOLS_WORKSPACE=my-workspace

# All search commands will now use the workspace for caching embeddings
# The initial command is used to initialize the workspace
search "some keywords" ./some_large_dir/*.txt --n-lines 5 --top-k 10

# If documents change, they are automatically re-embedded and cached
echo "some new content" > ./some_large_dir/some_file.txt
search "some keywords" ./some_large_dir/*.txt --n-lines 5 --top-k 10

# If documents are removed, you can run prune to clean up stale files
workspace prune

# You can see the stats of a workspace at any time
workspace status
> Active workspace: arxiv
> Root: /Users/loganmarkewich/.semtools/workspaces/arxiv
> Documents: 3000
> Index: Yes (IVF_PQ)
```

## CLI Help

```bash
$ parse --help
A CLI tool for parsing documents using various backends

Usage: parse [OPTIONS] <FILES>...

Arguments:
  <FILES>...  Files to parse

Options:
  -c, --parse-config <PARSE_CONFIG>  Path to the config file. Defaults to ~/.parse_config.json
  -b, --backend <BACKEND>            The backend type to use for parsing. Defaults to `llama-parse` [default: llama-parse]
  -v, --verbose                      Verbose output while parsing
  -h, --help                         Print help
  -V, --version                      Print version
```

```bash
$ search --help
A CLI tool for fast semantic keyword search

Usage: search [OPTIONS] <QUERY> [FILES]...

Arguments:
  <QUERY>     Query to search for (positional argument)
  [FILES]...  Files or directories to search

Options:
  -n, --n-lines <N_LINES>            How many lines before/after to return as context [default: 3]
      --top-k <TOP_K>                The top-k files or texts to return (ignored if max_distance is set) [default: 3]
  -m, --max-distance <MAX_DISTANCE>  Return all results with distance below this threshold (0.0+)
  -i, --ignore-case                  Perform case-insens