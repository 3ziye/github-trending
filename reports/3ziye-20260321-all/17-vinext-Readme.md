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
npm install -D vinext vite @vitejs/plugin-react
```

If you're using the App Router, also install:

```bash
npm install -D @vitejs/plugin-rsc react-server-dom-webpack
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

| Command         | Description                                                             |
| --------------- | ----------------------------------------------------------------------- |
| `vinext dev`    | Start dev server with HMR                                               |
| `vinext build`  | Production build (multi-environment for App Router: RSC + SSR + client) |
| `vinext start`  | Start local production server for testing                               |
| `vinext deploy` | Build and deploy to Cloudflare Workers                                  |
| `vinext init`   | Migrate a Next.js project to run under vinext                           |
| `vinext check`  | Scan your Next.js app for compatibility issues before migrating         |
| `vinext lint`   | Delegate to eslint or oxlint                                            |

Options: `-p / --port <port>`, `-H / --hostname <host>`, `--turbopack` (accepted, no-op).

`vinext deploy` options: `--preview`, `--env <name>`, `--name <name>`, `--skip-build`, `--dry-run`, `--experimental-tpr`.

`vinext init` options: `--port <port>` (default: 3001), `--skip-check`, `--force`.

### Starting a new vinext project

Run `npm create next-app@latest` to create a new Next.js project, and then follow these instructions to migrate it to vinext.

In the future, we will have a proper `npm create vinext` new project workflow.

### Migrating an existing Next.js project

`vinext init` automates the migration in one command:

```bash
npx vinext init
```

This will:

1. Run `vinext check` to scan for compatibility issues
2. Install `vite`, `@vitejs/plugin-react`, and App Router-only deps (`@vitejs/plugin-rsc`, `react-server-dom-webpack`) as devDependencies
3. Rename CJS config files (e.g. `postcss.config.js` -> `.cjs`) to avoid ESM conflicts
4. Add `"type": "module"` to `package.json`
5. Add `dev:vinext` and `build:vinext` scripts to `package.json`
6. Generate a minimal `vite.config.ts`

The migration is non-destructive -- your existing Next.js setup continues to work alongside vinext. It does not modify `next.config`, `tsconfig.json`, or any source files, and it does not remove Next.js dependencies.

vinext supports both Vite 7 and Vite 8. If you bring custom Vite config or plugins from an older setup, note that Vite 8 now defaults to Rolldown, Oxc, Lightning CSS, and a newer browser baseline. Prefer `oxc`, `optimizeDeps.rolldownOptions`, and `build.rolldownOptions` over older `esbuild` and `build.rollupOptions` knobs, and override `build.target` if you still need older browsers. If a dependency only breaks on Vite 8 because of stricter CommonJS default import handling, fix the import or use `legacy.inconsistentCjsInterop: true` as a temporary escape hatch. See the [Vite 8 migration guide](https://vite.dev/guide/migration).

```bash
npm run dev:vinext