# CSS MCP Server

An MCP (Model Context Protocol) server that provides up-to-date CSS documentation from MDN and comprehensive CSS code analysis.

## Features

**Documentation & Compatibility:**

- Official MDN Docs - Fetches documentation directly from MDN's API
- Browser Compatibility - Includes browser support data from MDN's BCD
- Simple API - Just pass CSS property names like `"grid"`, `"flexbox"`, or `":has"`
- Markdown Conversion - Converts HTML documentation to clean, readable markdown
- Auto-normalization - Supports both simple slugs (`"grid"`) and full paths (`"Web/CSS/grid"`)
- Smart Caching - SQLite-based cache with 7-day TTL for blazing-fast responses

**CSS Analysis:**

- 150+ Metrics - Comprehensive analysis of stylesheet quality and complexity
- Design Patterns - Detect color palettes, font sizes, spacing patterns
- Code Quality - Selector complexity, specificity analysis, property usage
- Performance Insights - Identify overly complex selectors and redundant code

## Installation

### For Claude Code

Install via the Claude Code CLI:

```bash
claude mcp add css -- npx -y css-mcp
```

### For VS Code 

One click install:

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=css&config=%7B%22name%22%3A%22css-mcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22css-mcp%22%5D%2C%22env%22%3A%7B%7D%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=css&config=%7B%22name%22%3A%22css%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22css-mcp%22%5D%2C%22env%22%3A%7B%7D%7D&quality=insiders)

Install via VS Code CLI:

```bash
code --add-mcp '{\"name\":\"css\",\"command\":\"npx\",\"args\":[\"-y\",\"css-mcp\"],\"env\":{}}'
```

### For MCP Clients (Claude Desktop, etc.)

Add to your MCP settings configuration:

```json
{
  "mcpServers": {
    "css": {
      "command": "npx",
      "args": ["-y", "css-mcp"]
    }
  }
}
```

### For Development

```bash
npm install -g css-mcp
```

Or use with npx:

```bash
npx css-mcp --self-test
```

## Requirements

- Node.js 20+
- Build tools for native modules (usually pre-installed on most systems)

## Usage

### Available Tools

#### `get_docs`

Fetch CSS documentation for any property, selector, function, or concept.

**Parameters:**

- `slug` (string) - CSS feature name or MDN path

**Examples:**

```javascript
// Simple slugs (auto-normalized)
get_docs({ slug: "grid" });
get_docs({ slug: ":has" });
get_docs({ slug: "flexbox" });
get_docs({ slug: "@media" });
get_docs({ slug: "::before" });

// Full MDN paths also work
get_docs({ slug: "Web/CSS/grid" });
get_docs({ slug: "en-US/docs/Web/CSS/border-radius" });
```

**Returns:**

```json
{
  "source": "mdn-doc",
  "slug": "/en-US/docs/Web/CSS/grid",
  "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/grid/index.json",
  "title": "grid",
  "mdn_url": "/en-US/docs/Web/CSS/grid",
  "summary": "The grid CSS property is a shorthand...",
  "body": [
    {
      "type": "prose",
      "title": "Syntax",
      "content": "The **`grid`** property is a shorthand..."
    }
  ]
}
```

#### `get_browser_compatibility`

Fetch browser compatibility data for CSS features.

**Parameters:**

- `bcd_id` (string) - Browser Compat Data ID (e.g., `"css.properties.grid"`)

**Example:**

```javascript
get_browser_compatibility({ bcd_id: "css.properties.grid" });
get_browser_compatibility({ bcd_id: "css.selectors.has" });
```

#### `analyze_css`

Analyze CSS code for quality, complexity, and design patterns. Returns **curated summary by default** (lightweight, ~1-2k tokens). Use `summaryOnly: false` for complete 150+ metrics (uses ~10k+ tokens).

**Parameters:**

- `css` (string, required) - CSS code to analyze
- `summaryOnly` (boolean, optional) - Return summary instead of full analysis. Default: `true`

**Examples:**

```javascript
// Summary mode (default, lightweight)
analyze_css({
  css: `
    .container {
      display: grid;
      color: #3b82f6;
    }
  `
});

// Full analysis with all 150+ metrics
analyze_css({
  css: "...",
  summaryOnly: false
});
```

**Returns (default summary):**

```json
{
  "analysis": {
    "stylesheet": {
      "sourceLinesOfCode": 5,
      "size": 72
    },
    "rules": { "total": 1 },
    "selectors": {
      "total": 1,
      "averageComplexity": 1.0,
      "maxComplexity": 1
    },
    "colors": {
      "unique": 1,
      "uniqueColors": ["#3b82f6"]
    }
  },
  "note": "Summary metrics only. Use summaryOnly: false for complete 150+ metrics."
}
```

#### `analyze_project_css`

Analyze all CSS files in a project. Finds CSS files recursively, combines them, and provides project-wide analysis. **Framework-agnostic** - works with built CSS from any framework (SvelteKit, React, Vue, 