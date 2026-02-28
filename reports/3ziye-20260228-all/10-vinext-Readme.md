# vinext

The Next.js API surface, reimplemented on Vite.

> **Read the announcement:** [How we rebuilt Next.js with AI in one week](https://blog.cloudflare.com/vinext/)

> 🚧 **Experimental — under heavy development.** This project is an experiment in AI-driven software development. The vast majority of the code, tests, and documentation were written by AI (Claude Code). Humans direct architecture, priorities, and design decisions, but have not reviewed most of the code line-by-line. Treat this accordingly — there will be bugs, rough edges, and things that don't work. Use at your own risk.

## Quick start

vinext includes an [Agent Skill](https://agentskills.io/home) that handles migration for you. It works with Claude Code, OpenCode, Cursor, Codex, and dozens of other AI coding tools. Install it, open your Next.js project, and tell the AI to migrate:

```sh
npx skills add cloudflare/vinext
```

Then open your Next.js project in any supported tool and say:

```
migrate this project to vinext
```

The skill handles compatibility checking, dependency installation, config generation, and dev server startup. It knows what vinext supports and will flag anything that needs manual attention.

### Or do it manually

```bash
npm install vinext
```

Replace `next` with `vinext` in your scripts:

```json
{
  "scripts": {
    "dev": "vinext dev",
    "build": "vinext build",
    "start": "vinext start"
  }
}
```

```bash
vinext dev          # Development server with HMR
vinext build        # Production build
vinext deploy       # Build and deploy to Cloudflare Workers
```

vinext auto-detects your `app/` or `pages/` directory, loads `next.config.js`, and configures Vite automatically. No `vite.config.ts` required for basic usage.

Your existing `pages/`, `app/`, `next.config.js`, and `public/` directories work as-is. Run `vinext check` first to scan for known compatibility issues, or use `vinext init` to [automate the full migration](#migrating-an-existing-nextjs-project).

### CLI reference

| Command | Description |
|---------|-------------|
| `vinext dev` | Start dev server with HMR |
| `vinext build` | Production build (multi-environment for App Router: RSC + SSR + client) |
| `vinext start` | Start local production server for testing |
| `vinext deploy` | Build and deploy to Cloudflare Workers |
| `vinext init` | Migrate a Next.js project to run under vinext |
| `vinext check` | Scan your Next.js app for compatibility issues before migrating |
| `vinext lint` | Delegate to eslint or oxlint |

Options: `-p / --port <port>`, `-H / --hostname <host>`, `--turbopack` (accepted, no-op).

`vinext deploy` options: `--preview`, `--env <name>`, `--name <name>`, `--skip-build`, `--dry-run`, `--experimental-tpr`.

`vinext init` options: `--port <port>` (default: 3001), `--skip-check`, `--force`.

### Starting a new vinext project

Run `npm create next-app@latest` to create a new Next.js project, and then follow these instructions to migrate it to vinext.

In the future, we will havre a proper `npm create vinext` new project workflow. 

### Migrating an existing Next.js project

`vinext init` automates the migration in one command:

```bash
npx vinext init
```

This will:

1. Run `vinext check` to scan for compatibility issues
2. Install `vite` (and `@vitejs/plugin-rsc` for App Router projects) as devDependencies
3. Rename CJS config files (e.g. `postcss.config.js` -> `.cjs`) to avoid ESM conflicts
4. Add `"type": "module"` to `package.json`
5. Add `dev:vinext` and `build:vinext` scripts to `package.json`
6. Generate a minimal `vite.config.ts`

The migration is non-destructive -- your existing Next.js setup continues to work alongside vinext. It does not modify `next.config`, `tsconfig.json`, or any source files, and it does not remove Next.js dependencies.

```bash
npm run dev:vinext    # Start the vinext dev server (port 3001)
npm run dev           # Still runs Next.js as before
```

Use `--force` to overwrite an existing `vite.config.ts`, or `--skip-check` to skip the compatibility report.

## Why

Vite has become the default build tool for modern web frameworks — fast HMR, a clean plugin API, native ESM, and a growing ecosystem. With [`@vitejs/plugin-rsc`](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc) adding React Server Components support, it's now possible to build a full RSC framework on Vite.

vinext is an experiment: can we reimplement the Next.js API surface on Vite, so that existing Next.js applications can run on a completely different toolchain? The answer, so far, is mostly yes — about 94% of the API surface works.

The current deployment target is Cloudflare Workers — zero cold starts, global by default, integrated platform (KV, R2, D1, AI). The `vinext deploy` command handles the full build-and-deploy pipeline. Expanding to other deployment targets is something we'd like to explore.

**Alternatives worth knowing about:**
- **[OpenNext](https://opennext.js.org/)** — adapts `next buil