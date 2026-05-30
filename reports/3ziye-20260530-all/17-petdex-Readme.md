<div align="center">

<img src="public/brand/petdex-desktop-icon.png" alt="Petdex" width="120" />

<h1>Petdex</h1>

<p>
  The public gallery of animated companions for Codex.
  <br />
  Browse, install, and submit pets with one command.
</p>

<p>
  <a href="https://petdex.crafter.run"><strong>petdex.crafter.run</strong></a>
  &nbsp;·&nbsp;
  <a href="https://petdex.crafter.run/built-with">Built with Petdex</a>
  &nbsp;·&nbsp;
  <a href="https://discord.gg/byhubdyBTe">Discord</a>
  &nbsp;·&nbsp;
  <a href="https://www.npmjs.com/package/petdex">npm</a>
</p>

<p>
  <a href="https://www.npmjs.com/package/petdex"><img src="https://img.shields.io/npm/v/petdex?style=flat-square&label=cli&color=000000" alt="npm version" /></a>
  <a href="https://github.com/crafter-station/petdex/stargazers"><img src="https://img.shields.io/github/stars/crafter-station/petdex?style=flat-square&color=000000" alt="GitHub stars" /></a>
  <a href="https://github.com/crafter-station/petdex/blob/main/LICENSE"><img src="https://img.shields.io/github/license/crafter-station/petdex?style=flat-square&color=000000" alt="MIT license" /></a>
  <a href="https://github.com/crafter-station/petdex/issues"><img src="https://img.shields.io/github/issues/crafter-station/petdex?style=flat-square&color=000000" alt="GitHub issues" /></a>
</p>

</div>

---

## What is Petdex

Petdex is three things working together:

1. **A web gallery** at [petdex.crafter.run](https://petdex.crafter.run) where the community submits, reviews, and showcases animated pets in the Codex sprite format.
2. **A CLI** that installs any pet on your machine with one command and ships them straight into Codex.
3. **A desktop app** that floats a pet on your screen and reacts to your coding agent's activity in real time.

Every pet is a folder. Every folder is a Pokédex entry. Every entry is one `npx petdex install` away.

## Quick start

```sh
# Pick a pet. Install it. Your Codex desktop app picks it up automatically.
npx petdex install boba

# Or run the full Petdex desktop app with bubble UI and agent hooks.
npx petdex init
```

Open Codex, go to **Settings → Appearance → Pets**, and pick the one you just installed.

## For users

| You want to... | Do this |
| --- | --- |
| Browse pets | Visit [petdex.crafter.run](https://petdex.crafter.run) |
| Install a pet | `npx petdex install <slug>` |
| Run the desktop floater | `npx petdex init` (downloads the `.dmg` and wires Codex/Claude Code hooks) |
| Make a pet | Use the `hatch-pet` skill inside Codex, or build one with the [Petdex creator tools](https://petdex.crafter.run/create) |
| Submit a pet | `npx petdex submit ./my-pet/` or drop it through the web submitter |
| Join the community | [Discord](https://discord.gg/byhubdyBTe) |

Full CLI reference: [`packages/petdex-cli/README.md`](./packages/petdex-cli/README.md).

## For builders

If you want to build on top of Petdex (a desktop client, a wearable, an SDK, a Discord bot, anything), you have two stable surfaces:

- **The HTTP API.** `petdex.crafter.run/api/manifest` returns every approved pet with its slug, spritesheet URL, animation states, and metadata.
- **The pet package format.** Every pet is a `pet.json` plus a `spritesheet.{webp,png}` rendered as an 8×9 grid of 192×208 frames.

13 open-source projects already build on these. See [petdex.crafter.run/built-with](https://petdex.crafter.run/built-with) for the catalog, then [submit yours via the issue template](https://github.com/crafter-station/petdex/issues/new?template=built-with.yml).

## Architecture

```text
crafter-station/petdex
├── src/
│   ├── app/[locale]/          Public site: gallery, /pets/<slug>, /collections, /built-with, /community, /create, /download, /submit, /u/<handle>, ...
│   ├── app/api/cli/           CLI endpoints: OAuth config, submit (zip → presigned R2), dedup check, register
│   ├── app/api/manifest/      Public manifest: every approved pet with its spritesheet URL
│   ├── app/api/admin/         Admin review surface for submissions, edits, collection requests
│   └── lib/db/schema.ts       Drizzle schema (Postgres)
├── packages/
│   ├── petdex-cli/            npm `petdex` (auth, list, install, submit, hooks, init)
│   ├── petdex-desktop/        Zig + WebKit floating mascot for macOS
│   └── discord-bot/           Discord.js bot for the Petdex server
├── public/built-with/         Screenshots for the community page
├── public/brand/              Logos, OS icons, Discord icon
└── drizzle/                   SQL migrations (Postgres schema history)
```

**Web stack**: Next.js 16, React 19, Tailwind, Drizzle, Postgres, Redis, Clerk, R2.<br />
**CLI**: Bun + TypeScript, ships as a single npm binary. Auth via Clerk OAuth + PKCE.<br />
**Desktop**: Zig on a fork of [`vercel-labs/zero-native`](https://github.com/vercel-labs/zero-native), HTTP sidecar in Node for agent hooks.

## Develop locally

Three paths, pick the one that matches what you want to change.

| Goal | Command | Setup |
| --- | --- | --- |
| U