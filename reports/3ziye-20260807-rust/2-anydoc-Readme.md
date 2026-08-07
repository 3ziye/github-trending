# anydoc

[![Crates.io](https://img.shields.io/crates/v/anydoc.svg)](https://crates.io/crates/anydoc)
[![npm](https://img.shields.io/npm/v/@firecrawl/anydoc.svg)](https://www.npmjs.com/package/@firecrawl/anydoc)
[![PyPI](https://img.shields.io/pypi/v/firecrawl-anydoc.svg)](https://pypi.org/project/firecrawl-anydoc/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/firecrawl/anydoc)](https://skills.sh/firecrawl/anydoc)

Fast Rust library that converts documents (Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF) into clean GitHub-Flavored Markdown. Includes bindings for [Node.js](node/README.md), [Python](python/README.md), and the [browser](wasm/README.md) (WebAssembly).

Built by [Firecrawl](https://firecrawl.dev) to turn any office document into LLM-ready Markdown in single-digit milliseconds, with one consistent output no matter which format goes in. It powers [Firecrawl Parse](https://firecrawl.dev/parse), so if you'd rather not run it yourself, the hosted API gives you the same conversion plus our OCR models for the scanned pages anydoc can't read on its own.

**[Try it in your browser](https://firecrawl.github.io/anydoc/)**: the demo page runs the library as WebAssembly, so files are converted locally and never leave your machine.

## Quick start

### Agent skill

anydoc ships as an [Agent Skill](https://agentskills.io), so your agent can read any document it runs into:

```bash
npx skills add firecrawl/anydoc
```

The [skill](skills/convert-documents-to-markdown/SKILL.md) teaches the agent to convert documents with the anydoc CLI. Works with [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex/), [Cursor](https://cursor.com), [OpenCode](https://opencode.ai), and any other [compatible agent](https://agentskills.io/clients).

### CLI

```bash
npx @firecrawl/anydoc report.docx               # Markdown to stdout
npx @firecrawl/anydoc slides.pptx -o slides.md  # or to a file
npx @firecrawl/anydoc - --format csv < data.csv # read stdin
```

`npx` downloads the prebuilt binary for your platform on first run. For a permanent `anydoc` command, install globally with `npm install -g @firecrawl/anydoc`. Run `anydoc --help` for all options.

### Node.js

```bash
npm install @firecrawl/anydoc
```

```js
import { toDocument, toMarkdown, toMarkdownBytes } from '@firecrawl/anydoc';

// From a file path:
const markdown = await toMarkdown('report.docx');

// From bytes, with the format detected from the content:
const fromBytes = await toMarkdownBytes(bytes);

// Or name it, which signature-less formats (CSV) need:
const fromCsv = await toMarkdownBytes(bytes, 'csv');

// Or stop at the document model, which also carries embedded assets:
const document = await toDocument(bytes);
```

> Full API reference: [node/README.md](node/README.md)

### Python

```bash
pip install firecrawl-anydoc
```

```python
import anydoc

# From a file path:
markdown = anydoc.to_markdown("report.docx")

# From bytes, with the format detected from the content:
markdown = anydoc.to_markdown_bytes(data)

# Or name it, which signature-less formats (CSV) need:
markdown = anydoc.to_markdown_bytes(data, "csv")

# Or stop at the document model, which also carries embedded assets:
document = anydoc.to_document(data)
```

> Full API reference: [python/README.md](python/README.md)

### Browser (WebAssembly)

```bash
npm install @firecrawl/anydoc-wasm
```

```js
import init, { toMarkdownBytes, toDocument } from '@firecrawl/anydoc-wasm';

await init();

// From bytes, with the format detected from the content:
const markdown = toMarkdownBytes(bytes);

// Or name it, which signature-less formats (CSV) need:
const fromCsv = toMarkdownBytes(bytes, 'csv');

// Or stop at the document model, which also carries embedded assets:
const document = toDocument(bytes);
```

> Full API reference: [wasm/README.md](wasm/README.md)

### Rust

```bash
cargo add anydoc
```

```rust
// From a file path:
let markdown = anydoc::to_markdown("report.docx")?;

// From bytes, with the format detected from the content:
let markdown = anydoc::to_markdown_bytes(&bytes, None)?;

// Or name it, which signature-less formats (CSV) need:
let markdown = anydoc::to_markdown_bytes(&bytes, anydoc::Format::Csv)?;

// Or stop at the document model, which also carries embedded assets:
let document = anydoc::to_document(&bytes, None)?;
```

## Features

- **One output for every format.** Each format parses into a shared document model and renders through a single Markdown serializer, so escaping, tables, heading anchors, and footnotes behave identically whether the input was a `.doc` from 2003 or a `.pptx` from yesterday.
- **Full document structure.** Headings with anchors, bold/italic/strikethrough, inline code and code blocks, links and internal cross-references, bulleted/numbered/nested/task lists with the source's own numbering, tables with merged cells and header rows, block quotes, footnotes and