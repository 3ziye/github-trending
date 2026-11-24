<p align="center"><img src="docs/images/logo.svg" width="72" height="72" alt="Hatamoto"></p>

<h1 align="center">Hatamoto</h1>

<p align="center"><strong>Stand close. Serve well.</strong></p>

<p align="center">
The batteries-included CMS for the agentic era: builder, SEO, caching, forms, redirects,
AI analytics, auto linking, entities, schema, Media optimizer and MCP in one Go binary plus Postgres.<br>
Open source, no plugin stack, no PHP, no Node, install stats on by default, one switch to turn them off.
</p>

<p align="center">
  <a href="https://github.com/Zen-Labs-Corp/hatamoto/actions/workflows/ci.yml"><img src="https://github.com/Zen-Labs-Corp/hatamoto/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/Zen-Labs-Corp/hatamoto/releases/latest"><img src="https://img.shields.io/github/v/release/Zen-Labs-Corp/hatamoto?sort=semver&label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/licence-Apache--2.0-blue" alt="Licence: Apache-2.0"></a>
</p>

<p align="center">
  <a href="https://hatamoto.dev">Website</a> ·
  <a href="https://hatamoto.dev/docs">Docs</a> ·
  <a href="docs/README.md">Docs in this repo</a> ·
  <a href="docs/site/getting-started/index.md">Get started</a> ·
  <a href="https://hatamoto.dev/plugins">Plugins</a> ·
  <a href="https://hatamoto.dev/themes">Themes</a> ·
  <a href="docs/ROADMAP.md">Roadmap</a> ·
  <a href="SECURITY.md">Security</a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/builder-dark.webp">
    <img src="docs/images/builder.webp" width="900" alt="The visual page builder: the layers of the home page on the left, the page on a canvas with desktop, tablet and phone sizes, and the selected headline's settings on the right.">
  </picture>
</p>

## Get started

**Docker** (starts Postgres too):

```sh
git clone https://github.com/Zen-Labs-Corp/hatamoto.git && cd hatamoto
docker compose up
```

**Or the binary** (Linux or macOS, Intel or ARM), pointed at your own Postgres:

```sh
OS=$(uname -s | tr A-Z a-z); ARCH=$(uname -m | sed 's/x86_64/amd64/; s/aarch64/arm64/')
curl -fL "https://github.com/Zen-Labs-Corp/hatamoto/releases/latest/download/hatamoto-$OS-$ARCH.tar.gz" | tar -xz --strip-components=1 "hatamoto-$OS-$ARCH/hatamoto"
DATABASE_URL=postgres://user:pw@localhost:5432/hatamoto?sslmode=disable ./hatamoto serve
```

The server prints a setup address in its log (`docker compose logs hatamoto`). Open it to create
your account and site. The admin lives at a private address of its own, which `hatamoto admin-url`
prints at any time. More: [Install with Docker](docs/site/getting-started/install-docker.md),
[Install the binary](docs/site/getting-started/install-binary.md), [First run](docs/site/getting-started/first-run.md),
[Trust and signing](docs/site/updates/trust-and-signing.md).

> **Status: v1, plugin SDK v0.** It runs [hatamoto.dev](https://hatamoto.dev) in production. The plugin SDK
> can still change between its minor versions. What stays stable, and for how long: [STABILITY.md](STABILITY.md).

## A look around

Every screenshot below is a real Hatamoto server with a seeded demo site, captured by
[`scripts/homepage-shots`](scripts/homepage-shots/README.md) (`SHOTS_SET=readme`), so they are regenerated
when the admin changes.

### Write and build pages

Posts get a writing editor with SEO checks, scheduling and suggested internal links. Pages get the visual
builder above: sections and blocks you rearrange on a canvas, previewed at desktop, tablet and phone sizes,
with undo, history and keyboard shortcuts. [Page editor](docs/site/admin/page-editor.md),
[Builder reference](docs/site/admin/builder-reference.md)

![The post editor: a post with a heading selected and the formatting toolbar, and the publish, schedule, slug and featured image settings in the side panel](docs/images/editor.webp)

### See who reads your site, people and AI

The overview shows what changed this week and what needs a review. Analytics are cookieless and count AI
assistants as a channel of their own. The crawler report shows which AI agents fetch which pages, checks that
each one is who it claims to be, and lets you allow or block a whole purpose (training, search, user fetches).
[AI and SEO](docs/site/ai-seo/index.md), [Crawler analytics](docs/site/ai-seo/crawler-analytics.md)

<table>
  <tr>
    <td width="50%"><img src="docs/images/overview.webp" alt="The admin overview: published pages, drafts, new form submissions, AI-referred visits and missing pages, then site health and the pages AI crawlers fetch most."></td>
    <td width="50%"><img src="docs/images/ai-analytics.webp" alt="AI analytics overview: AI fetches, AI-referred visits and AI share of traffic, with both plotted per day."></td>
  </tr>
</table>

![AI crawlers: fetches by purpose and every agent with its verification status and an Allow or Block switch per purpose](docs/images/ai-crawlers.webp)

#