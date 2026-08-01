<p align="center">
  <a href="https://bento.page" title="bento.page — try it in your browser">
    <img src="docs/assets/bento-logo.svg" alt="Bento" width="96" height="96">
  </a>
</p>

# [Bento — the office suite that fits in a file](https://bento.page/)

**This PowerPoint alternative is a single HTML file.** A Bento deck carries
its own viewer, presenter, and editor inside the document — open it in any
browser, edit it, present it, send it. The person you send it to needs
nothing: the file *is* the software.

**Try it in 10 seconds:** open [bento.page/slides](https://bento.page/slides)
— that's the entire app, running on a starter deck that doubles as the
feature tour. Or grab a designed template from the
[gallery](https://bento.page/) and make it yours.

**Download the app:** grab the single `Bento_Slides.bento.html` from the
[GitHub Releases](https://github.com/nyblnet/bento/releases) page or straight
from [bento.page](https://bento.page/releases/slides/Bento_Slides.bento.html)
(~560 KB, no account, no installer). Open it in any modern browser and it *is*
the editor. Save, and it rewrites itself with your deck inside.

## Why this exists

Office documents used to be things you *had*. Now they're things you rent —
locked in someone's cloud, behind someone's login, readable only while a
company keeps its servers on. Bento takes the other path:

- **One file, forever.** Deck, fonts, images, charts, animations, and the
  full editor travel together. A copy from 2026 will open in 2036.
- **View-source honest.** Your data sits in a plain, readable JSON block at
  the top of the file. No binary formats, no lock-in, no archaeology.
- **It saves itself.** The file rewrites its own data block on save (File
  System Access API, with a download fallback). No app to install, ever.
- **Local-first, provably.** Flip on Offline mode and nothing leaves your
  machine — updates and collaboration are hard-blocked, and the app says so.

## What's inside

| Feature | Description |
|---|---|
| **Morph presenting** | Elements that share an id animate between slides — position, size, color, even gradients. Duplicate a slide, rearrange, and the motion designs itself. |
| **Live collaboration** | E2EE (AES-GCM) with keys that live in your file, never on a server. The file itself is the invitation: anyone who opens a copy joins. Offline edits merge back precisely — our own CRDT, character-level text merging included. |
| **A blind relay** | The optional sync relay ([`server/sync-worker/`](server/sync-worker/)) stores ciphertext and learns nothing. Read the source; it's about one file. |
| **Charts, built in** | Bar / line / pie / scatter drawn by our own dependency-free engine, live during presentations: tooltips, zoom, and data that morphs when a bar chart becomes a pie. |
| **Designed for AI** | The document is plain JSON in the file, so agents edit `.bento.html` files in place and chatbots round-trip the JSON (`window.bento.loadDoc`). See [docs/agents.md](docs/agents.md). |
| **Signed self-updates** | Releases are ECDSA-signed and offered in-app. Updating writes a *new* file — the old one stays as your rollback. No server ever touches your documents. |
| **Everything else** | Speaker view, comments, layouts, hidden interactive states, hover reveals, motion paths, PDF export, page sizes, 8 UI languages — in a ~560 KB shell. |

## Use it with AI

Because the document is plain JSON living in one plaintext block near the top
of the file, any assistant that can read and write a file can edit your deck —
no plugin, no API. Two ways in:

- **File harnesses** edit the `#bento-doc` JSON in place:
  [Claude Code](https://claude.com/claude-code), Cursor, Aider, or any agent
  with filesystem access. Claude Code users get a packaged `bento-slides`
  skill (installable from this repo's plugin marketplace: `/plugin marketplace
  add nyblnet/bento`) that even downloads the latest Bento app by itself.
- **Chat round-trip** for any chatbot: copy the document JSON out (*Save →
  Copy document JSON*), let the assistant rewrite it, paste it back.

**It works fully offline with local open-weight models** — point
[Ollama](https://ollama.com), llama.cpp, or LM Studio at the deck and nothing
leaves your machine. The agent guide is a single page you can drop into any
model's context: [bento.page/agents.md](https://bento.page/agents.md) (also in
this repo at [docs/agents.md](docs/agents.md)).

## Architecture in one paragraph

`slides/src/model.ts` defines the JSON document model; one renderer
(`render.ts`) draws it for the editor canvas, thumbnails, and present mode
(Reveal.js drives navigation; morphs are computed from the model, not the
DOM). Animation is an in-house engine (`anim.ts`), charts are in-house
(`charts.ts`), collaboration is an in-house CRDT (`sync/crdt.ts` — pure
data, fuzz-tested by `scripts/test-sync.ts` across hundreds of thousands of
convergence checks). The shell compresses to ~560 KB with the document block
left as plaintext so o