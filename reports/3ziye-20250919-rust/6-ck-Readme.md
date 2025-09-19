# ck - Semantic Grep by Embedding

**ck (seek)** finds code by meaning, not just keywords. It's a drop-in replacement for `grep` that understands what you're looking for — search for "error handling" and find try/catch blocks, error returns, and exception handling code even when those exact words aren't present.

## Quick Start

```bash
# Install from crates.io
cargo install ck-search

# Or build from source
git clone https://github.com/BeaconBay/ck
cd ck
cargo build --release
```

```bash
# Index your project for semantic search (one-time setup)
ck --index src/

# Search by meaning - automatically updates index for changed files
ck --sem "error handling" src/
ck --sem "authentication logic" src/
ck --sem "database connection pooling" src/

# Traditional grep-compatible search still works
ck -n "TODO" *.rs
ck -R "TODO|FIXME" .

# Combine both: semantic relevance + keyword filtering
ck --hybrid "connection timeout" src/
```

## Why ck?

**For Developers:** Stop hunting through thousands of regex false positives. Find the code you actually need by describing what it does.

**For AI Agents:** Get structured, semantic search results in JSONL format. Stream-friendly, error-resilient output perfect for LLM workflows, code analysis, documentation generation, and automated refactoring.





## Core Features

### 🔍 **Semantic Search**
Find code by concept, not keywords. Searches understand synonyms, related terms, and conceptual similarity.

```bash
# These find related code even without exact keywords:
ck --sem "retry logic"           # finds backoff, circuit breakers
ck --sem "user authentication"   # finds login, auth, credentials  
ck --sem "data validation"       # finds sanitization, type checking

# Get complete functions/classes containing matches (NEW!)
ck --sem --full-section "error handling"  # returns entire functions
ck --full-section "async def" src/        # works with regex too
```

### ⚡ **Drop-in grep Compatibility**
All your muscle memory works. Same flags, same behavior, same output format.

```bash
ck -i "warning" *.log              # Case-insensitive  
ck -n -A 3 -B 1 "error" src/       # Line numbers + context
ck --no-filename "TODO" src/        # Suppress filenames (grep -h equivalent)
ck -l "error" src/                  # List files with matches only (NEW!)
ck -L "TODO" src/                   # List files without matches (NEW!)
ck -R --exclude "*.test.js" "bug"  # Recursive with exclusions
ck "pattern" file1.txt file2.txt   # Multiple files
```

### 🎯 **Hybrid Search**  
Combine keyword precision with semantic understanding using Reciprocal Rank Fusion.

```bash
ck --hybrid "async timeout" src/    # Best of both worlds
ck --hybrid --scores "cache" src/   # Show relevance scores with color highlighting
ck --hybrid --threshold 0.02 query  # Filter by minimum relevance
ck -l --hybrid "database" src/      # List files using hybrid search
```

### 🤖 **Agent-Friendly Output**
Perfect structured output for LLMs, scripts, and automation. JSONL format provides superior parsing reliability for AI agents.

```bash
# JSONL format - one JSON object per line (recommended for agents)
ck --jsonl --sem "error handling" src/
ck --jsonl --no-snippet "function" .        # Metadata only
ck --jsonl --topk 5 --threshold 0.7 "auth"  # High-confidence results

# Traditional JSON (single array)
ck --json --sem "error handling" src/ | jq '.file'
ck --json --topk 5 "TODO" . | jq -r '.preview'
ck --json --full-section --sem "database" . | jq -r '.preview'  # Complete functions
```

**Why JSONL for AI agents?**
- ✅ **Streaming friendly**: Process results as they arrive, no waiting for complete response
- ✅ **Memory efficient**: Parse one result at a time, not entire array into memory
- ✅ **Error resilient**: One malformed line doesn't break entire response
- ✅ **Composable**: Works perfectly with Unix pipes and stream processing
- ✅ **Standard format**: Used by OpenAI API, Anthropic API, and modern ML pipelines

**JSONL Output Format:**
```json
{"path":"./src/auth.rs","span":{"byte_start":1203,"byte_end":1456,"line_start":42,"line_end":58},"language":"rust","snippet":"fn authenticate(user: User) -> Result<Token> { ... }","score":0.89}
{"path":"./src/error.rs","span":{"byte_start":234,"byte_end":678,"line_start":15,"line_end":25},"language":"rust","snippet":"impl Error for AuthError { ... }","score":0.76}
```

**Agent Processing Example:**
```python
# Stream-process JSONL results (memory efficient)
import json, subprocess

proc = subprocess.Popen(['ck', '--jsonl', '--sem', 'error handling', 'src/'], 
                       stdout=subprocess.PIPE, text=True)

for line in proc.stdout:
    result = json.loads(line)
    if result['score'] > 0.8:  # High-confidence matches only
        print(f"📍 {result['path']}:{result['span']['line_start']}")
        print(f"🔍 {result['snippet'][:100]}...")
```

### 📁 **Smart File Filtering**
Automatically excludes cache directories, build artifacts, and respects `.gitignore` files.

```bash