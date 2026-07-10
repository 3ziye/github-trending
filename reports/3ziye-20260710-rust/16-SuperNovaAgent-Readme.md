# SuperNova

<p align="center">
  <img src="desktop_shell/ui/public/supernova-icon.png" alt="SuperNova icon" width="112" />
</p>

<p align="center">
  <strong>A Windows-first desktop AI Workbench for truth-backed agent execution.</strong>
</p>

<p align="center">
  <a href="README.zh-CN.md">中文</a> · English
</p>

<p align="center">
  RC0 stabilization · Windows desktop candidate · Rust Process Kernel · Local Runtime Protocol · Not final release
</p>


## Desktop Preview

<p align="center">
  <img src="docs/assets/User%20Guide.png" alt="SuperNova Workbench guide and desktop workspace" width="920" />
</p>

<p align="center"><sub>Screenshot source: current desktop Workbench UI, 2026-06-27.</sub></p>

| Command flow | Source selection |
| --- | --- |
| <img src="docs/assets/Slash%20Command.png" alt="Slash command flyout for Chat, TASK, Model, and Context" width="420" /> | <img src="docs/assets/Source%20Config.png" alt="Source picker for workspace files, folders, Chat, and TASK history" width="420" /> |

| Model route | Context pack |
| --- | --- |
| <img src="docs/assets/Model%20Config.png" alt="Model configuration flyout with provider, model, thinking, reasoning effort, and output budget" width="420" /> | <img src="docs/assets/Context%20Config.png" alt="Context configuration flyout for recent Chat turns, TASK runs, summaries, and explicit context items" width="420" /> |

<p align="center"><sub>Screenshots are UI examples, not validation evidence for a release claim. See <a href="docs/validation.md">Validation</a> for current-state claims.</sub></p>

## What SuperNovaAgent Does

SuperNova is an AI Agent workbench for a local workspace. It brings project files, Chat, TASK execution, context, and output destinations into one surface so questions can become inspectable work results.

Use Chat to quickly understand project files, documents, and code.
Use TASK for longer work: read material, edit code, organize files, run time-limited commands, and generate reports or datasets.
Use containers to keep a work stream's context, history, sources, and output destination together.

### For everyday users

SuperNovaAgent has two user-visible modes. Chat is for reading, explaining, clarifying, and deciding whether a request needs a task. TASK is for controlled local execution with runtime state, receipts, artifacts, and completion evidence.

| What you want to do | What Chat can do first | What TASK can do next |
| --- | --- | --- |
| Understand a project or folder | Read files, directory trees, workspace inventory, hashes, diffs, datasets, Office text, PDF text, and sanitized local environment facts. | Run batch workspace analysis such as SourceSets, duplicate checks, recent-change scans, tree indexes, and performance inventories. |
| Work on code | Read source files, explain module relationships, inspect diffs, and identify likely issue areas. | Apply workspace-scoped file changes, create focused source outputs, copy/move/rename/delete/unzip files, and record what actually changed. |
| Run commands or dev services | Explain the command intent and when terminal execution is needed; Chat itself does not mutate or run task work. | Run bounded foreground commands, start/stop/check long-running services, and attach terminal results to the task timeline. |
| Work with documents and tables | Read DOCX text, workbook cells/text, PDF text, DOCX metadata, validation results, and document diff summaries. | Create DOCX files, rewrite DOCX copies, rewrite DOCX in place when requested, and validate the produced document. |
| Analyze datasets | Read CSV datasets, inspect paged dataset refs, and check coverage. | Export CSV or Markdown results, create temporary datasets, and preserve row counts, schema, and derivation facts in receipts. |
| Produce deliverables | Decide which visible files should be produced and inspect existing artifacts. | Write text artifacts such as Markdown, CSV, JSON, and TXT; copy selected source sets; verify typed artifacts; run coverage and quality checks. |
| Package outputs | Inspect the candidate file set and package shape. | Build zip packages with supporting manifest/checksum files and verify the package artifact. |
| Track what happened | Return an answer, ask for missing facts, or suggest switching to TASK. | Show the active run, task stream, status, artifact cards, completion statement, and evidence in the Workbench. |

### For developers

| Extension path | What you can build on |
| --- | --- |
| Agent workflows | Add TASK flows that observe context, call capabilities, and close with evidence. |
| Local tools | Add or adapt file, terminal, document, package, artifact, or environment capabilities. |
| Product surfaces | Build new Workbench views over the same Product Runtime streams and read models. |
| Runtime contracts | Extend typed protocol DTOs while keeping UI, Product Runtime, and Kernel boundaries explicit. |
| Verification loops | Add validation around the exact layer you changed instead of rely