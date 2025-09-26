# ck - Semantic Code Search

**ck (seek)** finds code by meaning, not just keywords. It's grep that understands what you're looking for — search for "error handling" and find try/catch blocks, error returns, and exception handling code even when those exact words aren't present.

## 🚀 Quick Start

```bash
# Install from crates.io
cargo install ck-search

# Just search — ck builds and updates indexes automatically
ck --sem "error handling" src/
ck --sem "authentication logic" src/
ck --sem "database connection pooling" src/

# Traditional grep-compatible search still works
ck -n "TODO" *.rs
ck -R "TODO|FIXME" .

# Combine both: semantic relevance + keyword filtering
ck --hybrid "connection timeout" src/
```

## ✨ Headline Features

### 🤖 **AI Agent Integration (MCP Server)**
Connect ck directly to Claude Desktop, Cursor, or any MCP-compatible AI client for seamless code search integration:

```bash
# Start MCP server for AI agent integration
ck --serve
```

**Claude Desktop Setup:**

```bash
# Install via Claude Code CLI (recommended)
claude mcp add ck-search -s user -- ck --serve

# Note: You may need to restart Claude Code after installation
# Verify installation with:
claude mcp list  # or use /mcp in Claude Code
```

**Manual Configuration (alternative):**
```json
{
  "mcpServers": {
    "ck": {
      "command": "ck",
      "args": ["--serve"],
      "cwd": "/path/to/your/codebase"
    }
  }
}
```

**Tool Permissions:** When prompted by Claude Code, approve permissions for ck-search tools (semantic_search, regex_search, hybrid_search, etc.)

**Available MCP Tools:**
- `semantic_search` - Find code by meaning using embeddings
- `regex_search` - Traditional grep-style pattern matching
- `hybrid_search` - Combined semantic and keyword search
- `index_status` - Check indexing status and metadata
- `reindex` - Force rebuild of search index
- `health_check` - Server status and diagnostics

**Built-in Pagination:** Handles large result sets gracefully with page_size controls, cursors, and snippet length management.

### 🔍 **Semantic Search**
Find code by concept, not keywords. Understands synonyms, related terms, and conceptual similarity:

```bash
# These find related code even without exact keywords:
ck --sem "retry logic"           # finds backoff, circuit breakers
ck --sem "user authentication"   # finds login, auth, credentials
ck --sem "data validation"       # finds sanitization, type checking

# Get complete functions/classes containing matches
ck --sem --full-section "error handling"  # returns entire functions
```

### ⚡ **Drop-in grep Compatibility**
All your muscle memory works. Same flags, same behavior, same output format:

```bash
ck -i "warning" *.log              # Case-insensitive
ck -n -A 3 -B 1 "error" src/       # Line numbers + context
ck -l "error" src/                  # List files with matches only
ck -L "TODO" src/                   # List files without matches
ck -R --exclude "*.test.js" "bug"  # Recursive with exclusions
```

### 🎯 **Hybrid Search**
Combine keyword precision with semantic understanding using Reciprocal Rank Fusion:

```bash
ck --hybrid "async timeout" src/    # Best of both worlds
ck --hybrid --scores "cache" src/   # Show relevance scores with color highlighting
ck --hybrid --threshold 0.02 query  # Filter by minimum relevance
```

### ⚙️ **Automatic Delta Indexing**
Semantic and hybrid searches transparently create and refresh their indexes before running. The first search builds what it needs; subsequent searches only touch files that changed.

### 📁 **Smart File Filtering**
Automatically excludes cache directories, build artifacts, and respects `.gitignore` files:

```bash
ck "pattern" .                           # Follows .gitignore rules
ck --no-ignore "pattern" .               # Search all files including ignored ones
ck --exclude "dist" --exclude "logs" .   # Add custom exclusions

# Exclusion patterns use .gitignore syntax:
ck --exclude "node_modules" .            # Exclude directory and all contents
ck --exclude "*.test.js" .                # Exclude files matching pattern
ck --exclude "build/" --exclude "*.log" . # Multiple exclusions
# Note: Patterns are relative to the search root
```

## 🛠 Advanced Usage

### AI Agent Integration

#### MCP Server (Recommended)
```python
# Example usage in AI agents
response = await client.call_tool("semantic_search", {
    "query": "authentication logic",
    "path": "/path/to/code",
    "page_size": 25,
    "top_k": 50,           # Limit total results (default: 100 for MCP)
    "snippet_length": 200
})

# Handle pagination
if response["pagination"]["next_cursor"]:
    next_response = await client.call_tool("semantic_search", {
        "query": "authentication logic",
        "path": "/path/to/code",
        "cursor": response["pagination"]["next_cursor"]
    })
```

#### JSONL Output (Custom Workflows)
Perfect structured output for LLMs, scripts, and automation:

```bash
# JSONL format - one JSON object per line (recom