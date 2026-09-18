<p align="center">
  <a href="https://open-compute.dev">
    <img src="share/brand/open-compute.png" alt="open-compute" width="480" />
  </a>
</p>

<p align="center">
  <strong>High-performance Cloudflare Workers–compatible infrastructure in a single binary, deployed in one step.</strong><br/>
  Millisecond cold starts. MB-scale memory. Zero extra dependencies.
</p>

<p align="center">
  <a href="https://github.com/elliothux/open-compute/actions/workflows/ci.yml">
    <img src="https://github.com/elliothux/open-compute/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI" />
  </a>
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0" />
  <img src="https://img.shields.io/badge/runtime-verified%20workerd%20fork-f38020" alt="verified workerd fork" />
  <img src="https://img.shields.io/badge/API%20inventory-2%2C203%20members-success" alt="2203 stable members and overloads" />
  <img src="https://img.shields.io/badge/rust-1.98-orange" alt="Rust 1.98" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey" alt="macOS | Linux" />
</p>

<p align="center">
  <a href="https://open-compute.dev">Website</a>
  · <a href="https://open-compute.dev/docs/">Docs</a>
  · <a href="https://open-compute.dev/docs/platform/compatibility/">Compatibility</a>
  · <a href="https://open-compute.dev/docs/project/">Architecture</a>
</p>

<p align="center">
  English · <a href="README.zh.md">简体中文</a>
</p>

---

## The Workers platform, running on your hardware

You already know how to write Cloudflare Workers. **open-compute runs the compatible Workers programming model** — module workers, familiar bindings, and Wrangler workflows — on a single machine you own.

**One binary. One data directory. One object authority.** Local filesystem is the default; S3-compatible storage is optional.

No Kubernetes. No Redis. No service mesh. No distributed control plane to babysit. No vendor lock-in.

```
   Everyone else                        open-compute
   ─────────────                        ────────────
   gateway + router                     ┌──────────────┐
   control plane                        │              │
   scheduler service          ═══>      │  ocd (1 bin) │
   Redis / Valkey cluster               │              │
   Postgres                             └──────────────┘
   K8s + operators                       + SQLite + Local/S3 objects
```

## Why open-compute

**workerd is a runtime, not a platform.** It executes isolated Workers brilliantly — and stops there. No multi-tenant routing, no durable state, no scheduling, no deployment lifecycle, no control API. Everyone who wants Workers on their own infrastructure has to build that layer.

open-compute _is_ that layer — and it ships as **one file**.

- **One binary, everything inside.** Runtime, control plane, scheduler, and every product binding. Copy it to a host, point it at a directory, and you are serving traffic.
- **Fast because it's workerd.** Worker code runs on a pinned, checksum-verified workerd fork. Isolates start in milliseconds — not one process or container per request.
- **Nothing else to run.** SQLite owns platform metadata and Local storage owns object bytes by default. S3-compatible storage is optional; neither mode needs a database or cache sidecar.
- **Pinned and verified.** The runtime and its assets are fixed and verified at build and startup. Production startup stays offline.
- **Yours completely.** You own the code, data, and machines. External services are optional and explicitly configured.

## Proof, not promises

Compatibility here is measured, not asserted. The same fixtures run against open-compute and real Cloudflare wherever the hosted API permits direct comparison.

|           |                                                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| **2,203** | stable API members and overloads tracked across the Workers runtime and product bindings                        |
| **7 / 7** | core product surfaces checked against real Cloudflare: Workers, Cache, KV, D1, R2, Durable Objects, and Queues  |
| **1 : 1** | a production Next.js 16 build runs on Cloudflare and open-compute from the same project and deployment artifact |
| **90%+**  | required line coverage, with real processes, SQLite, and the pinned workerd runtime in acceptance tests         |

## Compatibility

Write standard module workers (`export default { fetch }`) with the bindings you already know. See the [compatibility guide](https://open-compute.dev/docs/platform/compatibility/) for exact behavior and single-node differences.

### Runtime & bindings

| Module                  | Status            |
| ----------------------- | ----------------- |
| Workers                 | █████████▉ 99% ✅ |
| Workers Standard limits | █████████▉ 99% ✅ |
| KV           