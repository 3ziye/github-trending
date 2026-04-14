**English** | [中文](README_zh.md)

# sage-wiki

An implementation of [Andrej Karpathy's idea](https://x.com/karpathy/status/2039805659525644595) for an LLM-compiled personal knowledge base. Developed using [Sage Framework](https://github.com/xoai/sage).

Some lessons learned after building sage-wiki [here](https://x.com/xoai/status/2040936964799795503).

Drop in your papers, articles, and notes. sage-wiki compiles them into a structured, interlinked wiki — with concepts extracted, cross-references discovered, and everything searchable.

- **Your sources in, a wiki out.** Add documents to a folder. The LLM reads, summarizes, extracts concepts, and writes interconnected articles.
- **Compounding knowledge.** Every new source enriches existing articles. The wiki gets smarter as it grows.
- **Works with your tools.** Opens natively in Obsidian. Connects to any LLM agent via MCP. Runs as a single binary — nothing to install beyond the API key.
- **Ask your wiki questions.** Enhanced search with chunk-level indexing, LLM query expansion, and re-ranking. Ask natural language questions and get cited answers.

https://github.com/user-attachments/assets/c35ee202-e9df-4ccd-b520-8f057163ff26

_Dots on the outer boundary represent summaries of all documents in the knowledge base, while dots in the inner circle represent concepts extracted from the knowledge base, with links showing how those concepts connect to one another._

## Install

```bash
# CLI only (no web UI)
go install github.com/xoai/sage-wiki/cmd/sage-wiki@latest

# With web UI (requires Node.js for building frontend assets)
git clone https://github.com/xoai/sage-wiki.git && cd sage-wiki
cd web && npm install && npm run build && cd ..
go build -tags webui -o sage-wiki ./cmd/sage-wiki/
```

## Supported Source Formats

| Format      | Extensions                              | What gets extracted                                         |
| ----------- | --------------------------------------- | ----------------------------------------------------------- |
| Markdown    | `.md`                                   | Body text with frontmatter parsed separately                |
| PDF         | `.pdf`                                  | Full text via pure-Go extraction                            |
| Word        | `.docx`                                 | Document text from XML                                      |
| Excel       | `.xlsx`                                 | Cell values and sheet data                                  |
| PowerPoint  | `.pptx`                                 | Slide text content                                          |
| CSV         | `.csv`                                  | Headers + rows (up to 1000 rows)                            |
| EPUB        | `.epub`                                 | Chapter text from XHTML                                     |
| Email       | `.eml`                                  | Headers (from/to/subject/date) + body                       |
| Plain text  | `.txt`, `.log`                          | Raw content                                                 |
| Transcripts | `.vtt`, `.srt`                          | Raw content                                                 |
| Images      | `.png`, `.jpg`, `.gif`, `.webp`, `.svg` | Description via vision LLM (caption, content, visible text) |
| Code        | `.go`, `.py`, `.js`, `.ts`, `.rs`, etc. | Source code                                                 |

Just drop files into your source folder — sage-wiki detects the format automatically. Images require a vision-capable LLM (Gemini, Claude, GPT-4o).

## Quickstart

![Compiler Pipeline](sage-wiki-compiler-pipeline.png)

### Greenfield (new project)

```bash
mkdir my-wiki && cd my-wiki
sage-wiki init
# Add sources to raw/
cp ~/papers/*.pdf raw/papers/
cp ~/articles/*.md raw/articles/
# Edit config.yaml to add api key, and pick LLMs
# First Compile
sage-wiki compile
# Search
sage-wiki search "attention mechanism"
# Ask questions
sage-wiki query "How does flash attention optimize memory?"
# Interactive terminal dashboard
sage-wiki tui
# Browse in the browser (requires -tags webui build)
sage-wiki serve --ui
# Watch folder
sage-wiki compile --watch
```

### Vault Overlay (existing Obsidian vault)

```bash
cd ~/Documents/MyVault
sage-wiki init --vault
# Edit config.yaml to set source/ignore folders, add api key, pick LLMs
# First Compile
sage-wiki compile
# Watch the vault
sage-wiki compile --watch
```

### Docker

```bash
# Pull from GitHub Container Registry
docker pull ghcr.io/xoai/sage-wiki:latest

# Or from Docker Hub
docker pull xoai/sage-wiki:latest

# Run with your wiki directory mounted
docker run -d -p 3333:3333 -v ./my-wiki:/wiki -e GEMINI_API_KEY=... ghcr.io/xoai/sage-wiki

# Or build from source
docker build -t sage-wiki .
docker run -d -p 3333:3333 -v ./my-wiki:/wiki -e GEMINI_API_KEY=... sage-wiki
```

Available tags: `:latest` (main branch), `:v1.0.0` (releases), `:sha-abc1234` (specific