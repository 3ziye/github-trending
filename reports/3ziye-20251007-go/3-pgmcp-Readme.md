[![ci](https://github.com/subnetmarco/pgmcp/actions/workflows/ci.yml/badge.svg)](https://github.com/subnetmarco/pgmcp/actions/workflows/ci.yml)
[![Go Report Card](https://goreportcard.com/badge/github.com/subnetmarco/pgmcp)](https://goreportcard.com/report/github.com/subnetmarco/pgmcp)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# PGMCP - PostgreSQL Model Context Protocol Server

PGMCP connects AI assistants to **any PostgreSQL database** through natural language queries. Ask questions in plain English and get structured SQL results with automatic streaming and robust error handling.

**Works with**: Cursor, Claude Desktop, VS Code extensions, and any [MCP-compatible client](https://modelcontextprotocol.io/)

## Quick Start

PGMCP connects to **your existing PostgreSQL database** and makes it accessible to AI assistants through natural language queries.

### Prerequisites
- PostgreSQL database (existing database with your schema)
- OpenAI API key (optional, for AI-powered SQL generation)

### Basic Usage

```bash
# Set up environment variables
export DATABASE_URL="postgres://user:password@localhost:5432/your-existing-db"
export OPENAI_API_KEY="your-api-key"  # Optional

# Run server (using pre-compiled binary)
./pgmcp-server

# Test with client in another terminal
./pgmcp-client -ask "What tables do I have?" -format table
./pgmcp-client -ask "Who is the customer that has placed the most orders?" -format table
./pgmcp-client -search "john" -format table
```

Here is how it works:

```
👤 User / AI Assistant
         │
         │ "Who are the top customers?"
         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Any MCP Client                           │
│                                                             │
│  PGMCP CLI  │  Cursor  │  Claude Desktop  │  VS Code  │ ... │
│  JSON/CSV   │  Chat    │  AI Assistant    │  Editor   │     │
└─────────────────────────────────────────────────────────────┘
         │
         │ Streamable HTTP / MCP Protocol
         ▼
┌─────────────────────────────────────────────────────────────┐
│                    PGMCP Server                             │
│                                                             │
│  🔒 Security    🧠 AI Engine      🌊 Streaming               │
│  • Input Valid  • Schema Cache    • Auto-Pagination         │
│  • Audit Log    • OpenAI API      • Memory Management       │
│  • SQL Guard    • Error Recovery  • Connection Pool         │
└─────────────────────────────────────────────────────────────┘
         │
         │ Read-Only SQL Queries
         ▼
┌─────────────────────────────────────────────────────────────┐
│                Your PostgreSQL Database                     │
│                                                             │
│  Any Schema: E-commerce, Analytics, CRM, etc.               │
│  Tables • Views • Indexes • Functions                       │
└─────────────────────────────────────────────────────────────┘

External AI Services:
OpenAI API • Anthropic • Local LLMs (Ollama, etc.)

Key Benefits:
✅ Works with ANY PostgreSQL database (no assumptions about schema)
✅ No schema modifications required  
✅ Read-only access (100% safe)
✅ Automatic streaming for large results
✅ Intelligent query understanding (singular vs plural)
✅ Robust error handling (graceful AI failure recovery)
✅ PostgreSQL case sensitivity support (mixed-case tables)
✅ Production-ready security and performance
✅ Universal database compatibility
✅ Multiple output formats (table, JSON, CSV)
✅ Free-text search across all columns
✅ Authentication support
✅ Comprehensive testing suite
```

## Features

- **Natural Language to SQL**: Ask questions in plain English
- **Automatic Streaming**: Handles large result sets automatically  
- **Safe Read-Only Access**: Prevents any write operations
- **Text Search**: Search across all text columns
- **Multiple Output Formats**: Table, JSON, and CSV
- **PostgreSQL Case Sensitivity**: Handles mixed-case table names correctly
- **Universal Compatibility**: Works with any PostgreSQL database

### Environment Variables

**Required:**
- `DATABASE_URL`: PostgreSQL connection string to your existing database

**Optional:**
- `OPENAI_API_KEY`: OpenAI API key for AI-powered SQL generation
- `OPENAI_MODEL`: Model to use (default: "gpt-4o-mini")
- `HTTP_ADDR`: Server address (default: ":8080")
- `HTTP_PATH`: MCP endpoint path (default: "/mcp")
- `AUTH_BEARER`: Bearer token for authentication

## Installation

### Download Pre-compiled Binaries

1. Go to [GitHub Releases](https://github.com/subnetmarco/pgmcp/releases)
2. Download the binary for your platform (Linux, macOS, Windows)
3. Extract and run:

```bash
# Example for macOS/Linux
tar xzf pgmcp_*.tar.gz
cd pgmcp_*
./pgmcp-server
```

### Alternative Options

```bash
# Homebrew (macOS/Linux) - Available after first release
brew tap subnetmarco/homebrew-tap
brew inst