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
  <img src="https://img.shields.io/badge/runtime-stock%20workerd-f38020" alt="stock workerd" />
  <img src="https://img.shields.io/badge/API%20surface-2%2C097%20members-success" alt="2097 members" />
  <img src="https://img.shields.io/badge/rust-1.98-orange" alt="Rust 1.98" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey" alt="macOS | Linux" />
</p>

<p align="center">
  <a href="https://open-compute.dev">Website</a>
  · <a href="docs/README.md">Docs</a>
  · <a href="packages/docs">Operator site</a>
  · <a href="docs/implemented/open-compute-workerd-platform.md">Architecture</a>
</p>

<p align="center">
  English · <a href="README.zh.md">简体中文</a>
</p>

---

## The Workers platform, running on your hardware

You already know how to write Cloudflare Workers. **open-compute runs them unchanged** — the same module workers, the same bindings, the same APIs — on a single machine you own.

**One binary. One data directory. One object authority.** Local filesystem is the default; S3-compatible storage is optional.

No Kubernetes. No Redis. No service mesh. No control plane to babysit. No vendor.

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
- **Fast because it's workerd.** Your code runs on stock workerd, Cloudflare's open-source V8 runtime. Isolates start in **milliseconds** and idle in **megabytes** — not containers, not gigabytes, not per-request process spawns.
- **Nothing else to run.** SQLite owns platform metadata and direct Local storage owns object bytes by default. You can select one S3-compatible authority instead; neither mode needs a sidecar.
- **Pinned and verified.** The current release pin uses stock workerd. Native limits and Loader development uses the [`elliothux/workerd` submodule](docs/workerd/README.md) at `third_party/workerd`; adopting a fork binary requires a coordinated pin update and validation.
- **Yours completely.** Your code, your data, your machines, fully offline. No account, no egress, no telemetry, no bill.

## Proof, not promises

Compatibility here is measured, not asserted. The same fixtures run against open-compute **and** real Cloudflare — and if the results differ, it does not ship.

|           |                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| **2,097** | stable API members implemented across the Workers runtime and every product binding — **zero gaps**                  |
| **7 / 7** | product surfaces verified byte-for-byte against real Cloudflare: Workers, Cache, KV, D1, R2, Durable Objects, Queues |
| **1 : 1** | a production Next.js 16 build runs identically on Cloudflare and on open-compute — same artifact, same behavior      |
| **90%+**  | enforced line coverage, with real processes, real SQLite, and real workerd in every acceptance run                   |

## Compatibility

Write standard module workers (`export default { fetch }`) with the bindings you already know.

### Runtime & bindings

| Module                | Status             |
| --------------------- | ------------------ |
| Workers               | ██████████ 100% ✅ |
| KV                    | ██████████ 100% ✅ |
| R2                    | ██████████ 100% ✅ |
| 