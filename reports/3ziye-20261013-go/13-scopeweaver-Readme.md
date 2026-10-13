<div align="center">

# ScopeWeaver

An LLM multi-agent autonomous penetration-testing system (Go backend + Next.js frontend)

English · [한국어](README.ko.md)

</div>

---

> **About this project.** ScopeWeaver is a derivative of [Autumn-27/ARTEX](https://github.com/Autumn-27/ARTEX),
> rebranded and translated into English and Korean. It is built from upstream commit `160fe13`.

Modification date: **2026-10-02**. See [provenance and changes](docs/PROVENANCE.md); this is not a release tag.

[Verification status and known limitations](docs/VERIFICATION.md).

> The code and architecture originate in ARTEX. This standalone derivative changes the product
> name, English/Korean interface and messages, documentation, and distribution targets. See [Provenance and changes](#provenance-and-changes)
> for the full list of what differs from upstream, and [License and disclaimer](#license-and-disclaimer)
> for the terms, which are unchanged (AGPL-3.0).
>
> **Authorization.** This is a security-testing tool. Use it only against systems you own or are
> explicitly authorized to test. The upstream usage restrictions still apply — read them below.

---

## Language

English is the default. Select English or Korean in the interface. The server's durable default is
`language` in system settings; `SCOPEWEAVER_LANGUAGE` (or `ARTEX_LANGUAGE`) supplies the environment
fallback. Operating-system `LANG` does not select the application language.

Requests prefer `lang`, then supported `Accept-Language` preferences, then the `scopeweaver_locale`
cookie, then the server default. New HTTP-created tasks retain their language across queues and
restarts; older tasks without saved language use the server default. Built-in agent guidance and
output instructions use the run language; user-edited templates and stored evidence remain intact.
Report/CSV/ZIP labels use the export request's language. [Full documentation](docs/README.md) and
[Korean references](docs/ko/README.md) include the bundled skill guidance.

## Screenshots

These captures show ScopeWeaver's English interface with the included fictional demo data.
They do not represent scans of live targets. See the [Korean screenshots](README.ko.md#스크린샷)
and [mobile view](screenshots/en/mobile.png).

| Dashboard | Tasks |
| :---: | :---: |
| ![English dashboard](screenshots/en/dashboard.png) | ![English task list](screenshots/en/tasks.png) |
| Findings | Settings |
| ![English findings](screenshots/en/findings.png) | ![English settings](screenshots/en/settings.png) |

Original Chinese screenshots remain in [the screenshots directory](screenshots), credited to
[upstream ARTEX](https://github.com/Autumn-27/ARTEX/tree/160fe13c243be361eeac5408c40a96e824fa842c/screenshots).

---

## Approval records

The global "Approval records" view, the in-task "Interception approval" panel, and the approval
cards shown inside conversations all expand to show full detail. The presentation follows the
[approval-detail component from AegisHook](https://github.com/RuoJi6/AegisHook/blob/main/web/src/components/CallDetail.vue),
reusing the upstream component and theme.

## Asset sync (ScopeSentry)

You can sync asset data directly from [ScopeSentry](https://github.com/Autumn-27/ScopeSentry),
which saves you from collecting the same data twice:

- On the **Asset sync** page, enter your ScopeSentry address and API key to connect the data source.
- Choose what to sync by **project** or by **task**, and pick the asset types (domain / subdomain /
  IP / port / site / endpoint …).
- Import in one click. Assets are merged into the company asset scope and go straight into the
  asset graph for agents to explore.

---

## Installation

### GLM and other model providers

The **LLM → New** form includes GLM-5.3 configuration templates for Z.ai's General API and a
separately labeled Coding Plan reference. Add your own API key; template selection does not save,
activate, or contact a provider. Coding Plan use is restricted to officially supported tools, and
ScopeWeaver is not listed. See [provider setup and support limits](docs/llm-providers.md).

> Requires a **PostgreSQL** database. Exploration needs an **LLM** configured
> (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, or set it in the UI).

### Option 1: one-click install script (recommended)

```bash
git clone https://github.com/cskwork/scopeweaver.git
cd scopeweaver
./install.sh
```

The script detects (and optionally installs) Docker, then lets you choose **① all-in-Docker** or
**② build and run locally**:

- **① All-in-Docker**: enter one Postgres password (press Enter for a random one) → it writes
  `.env` → `docker compose up -d`.
- **② Local**: pick a database (connect to an existing one, or start one with Docker) → it
  generates `config.json` → `go` compiles a single binary with the frontend embedded → start.

Once it is up, open **http://localhost:8787** (the first visit lands on `/setup` to set the admin
password).

> The scripts speak English by default. For Korean p