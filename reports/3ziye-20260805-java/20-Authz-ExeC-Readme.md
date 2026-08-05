# 🔐 Authz-ExeC

**A Burp Suite extension for cross-identity / cross-tenant access-control testing — BAC, IDOR, BOLA, and privilege escalation.**

![Java](https://img.shields.io/badge/Java-17%2B-orange)
![Burp](https://img.shields.io/badge/Burp-Montoya%20API-ff6633)
![Platform](https://img.shields.io/badge/Burp-Pro%20%7C%20Community-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Authz-ExeC replays every request you make as a **privileged user** using each **identity** you
configure (a low-privilege user, a second tenant, unauthenticated), compares each response against
the privileged one, and shows a live colour matrix of where access control **held**, **broke**, or
**needs review**. Think Autorize / AuthMatrix — rebuilt on the modern Montoya API, hardened against
false positives, with first-class **multi-tenant** and **GraphQL** support.

## 🎬 Demo

<p align="center">
  <img src="docs/screenshot.png" alt="Authz-ExeC results matrix" width="900">
</p>

## ✨ Features

**⚡ Core**

- 🧮 **Matrix view** — rows are endpoints, columns are identities. Each cell is a colour-coded verdict
  (BYPASSED / ENFORCED / REVIEW / NO-AUTH / WAF).
- 📥 **Two ways to feed it:** one-click **Import Proxy History (in scope)**, or arm **LIVE** and browse.
- 🎭 **Identities** — swap `Cookie`, `Authorization` (JWT), and arbitrary headers (`X-Tenant-Id`,
  `X-Api-Key`, …), strip all auth (unauthenticated), or apply regex **ID-rewrite** rules for BOLA.
- 🔎 **Request/response viewer** per identity, colour count chips that double as **click-to-filter**, a
  free-text/time filter, CSV export, and a **JWT decoder** (`alg:none` / strip-signature helpers).

**🎯 Accuracy (low false-positive)**

- 🧠 **Three-state model** (privileged A / identity B / unauthenticated C) — a real bypass needs
  *B looks like A* **and** *C was refused*. If C also succeeds the endpoint is simply **public**.
- 🧹 **Body normalisation** — strips timestamps, UUIDs, CSRF/nonce tokens, and trace-ids before diffing.
- 📊 **JSON key-set** similarity, weighted-token similarity, and length tolerance.
- 🐤 **Canary markers** — tag a string unique to each tenant; a foreign marker appearing in another
  identity's response is near-proof of a cross-tenant leak.
- 🛡️ Guards for **WAF / rate-limit** blocks, **soft errors** (`200` + "access denied"), **empty
  results** (row-level filtering), and **login redirects**. Per-verdict **confidence score**.

**🧩 Coverage**

- 📡 **GraphQL** — auto-tests POST queries (even with POST off); mutations gated behind a write method.
- 🗂️ **API mode** — tests JSON, files/images (IDOR objects), XML, and empty/`204`/header-based
  responses; skips only rendered HTML pages.
- 🔁 **Value-aware de-dup** — same path with different parameter **values** (or different GraphQL
  queries) are each tested, while identical requests are never re-sent (persisted per project).
- 🙈 **Skips your identities' own browsing** — a request carrying a configured identity's session token
  is ignored, so browsing *as* the low-priv user doesn't create low-priv base rows.

**🧰 Workflow**

- 💾 **Presets** — save/load all identities + config to a portable `.properties` file.
- ♻️ **Retest** selected/all rows, **Send to Authz-ExeC** context-menu action, per-project persistence.

## 🧠 How detection works

For each captured request the engine sends and compares three responses:

| State | What it is                                                                        |
| ----- | --------------------------------------------------------------------------------- |
| **A** | the **privileged** response you captured (the "full access" template)             |
| **B** | the same request replayed with the **identity under test**'s auth                 |
| **C** | the same request with **all auth stripped** (the "denied / no-identity" template) |

A real access-control bypass requires **B ≈ A** *and* **C ≠ A** (unauthenticated was refused). If C
also equals A, the endpoint never had a control — it's simply public.

| Verdict      | Colour    | Meaning                                                                      |
| ------------ | --------- | ---------------------------------------------------------------------------- |
| **BYPASSED** | 🔴 red    | The identity got access it should not have (privilege / cross-tenant break). |
| **ENFORCED** | 🟢 green  | Properly denied, empty-filtered, or silently rescoped to its own data.       |
| **REVIEW**   | 🟠 orange | Ambiguous — inspect manually.                                                |
| **NO-AUTH**  | 🔵 blue   | Served even without any session (public / missing authentication).           |
| **WAF/RL**   | 🟣 purple | WAF or rate-limit block — infrastructure, not app authz.                     |

## 📋 Requirements

- 🧷 **Burp Suite** Professional **or** Community (the Montoya API is bundled — no download needed).
- ☕ To build from source: a **JDK 17 or newer**. No Gradle/Maven required.

## 🚀 Installation

### 📦 Option