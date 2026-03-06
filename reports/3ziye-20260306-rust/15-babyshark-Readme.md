# babyshark

**Wireshark made easy (in your terminal).**

Babyshark is a PCAP TUI that helps you answer:
- What’s using the network?
- What looks broken/weird?
- What should I select next?

**Status:** v0.3.0 (alpha).
- Offline `.pcap` / `.pcapng` viewing works without Wireshark
- Live capture requires `tshark` (Wireshark CLI)


### Overview
![DB99A3F0-4AB7-461C-A40F-496F9C950AFC](https://github.com/user-attachments/assets/8dfb277c-a081-4feb-987e-6fc404e39f7e)

**Overview is the “start here” dashboard.** It summarizes the capture and suggests what to do next.

- Shows quick totals (packets/flows), a traffic mix, and “top” tables (ports/hosts/flows).
- In live mode it shows capture status (pps + a last status/error line from `tshark`).

**How to use it:**
- Press `D` to jump to **Domains** (hostnames-first).
- Press `W` to jump to **What’s weird?** (curated detectors).
- Press `F` (or `f`) to jump to **Flows** (raw).
- Many rows are drill-down entry points: select a row and press **Enter**.

### Domains
![5E1633E3-0E53-4085-AE98-6656121EAF8B](https://github.com/user-attachments/assets/7f4691cb-b930-46c6-85d8-6facfe9acfcd)

**Domains groups traffic by hostname** so you can start from names instead of 5‑tuples.

- Shows per-domain rollups (connections/bytes + query/response/failure-style counters).
- The details pane shows “IP hints”. When DNS answers aren’t visible (DoH/DoT/caching), it can still show **Observed IPs (from flows)** using TLS SNI / HTTP Host hints.

**How to use it:**
- Select a domain and press **Enter** to drill into the relevant **Flows**.
- Press `s` to change the sort mode.
- Press `c` to clear an active subset filter.

### What's weird?
![B401B8AA-4EE7-42BE-A53A-DC4F6DFC562A](https://github.com/user-attachments/assets/bf8b8c1d-8c45-47a8-b9ec-17bc29a925d5)

**What’s weird? is a curated set of detectors** meant to answer “what looks broken/slow?” without needing deep Wireshark knowledge.

- Each detector includes a short “why it matters”.
- Pressing **Enter** on a detector filters down to the affected flows so you can drill into packets/streams.

**How to use it:**
- Select a detector (you can also press `1`–`9` to jump-select) and press **Enter**.
- Press `c` to clear an active subset filter.

### Expand
![Screenshot 2026-02-23 at 12 09 07 PM](https://github.com/user-attachments/assets/68cdf767-426b-41b0-85d4-b2e44fe12eac)

**Expand / Explain (`?`) gives plain-English context** for what you’re looking at.

- From **Flows**, press **Enter** to open **Packets**, then press `?` to open **Explain**.
- Explain is best-effort: it tries to classify the flow and show “why I think that” + “next steps”.

Tip: press `h` for help and `g` for glossary.


---

## Quickstart

### Download a release (recommended)

Grab a binary from GitHub Releases:
- https://github.com/vignesh07/babyshark/releases

### Or build from source

```bash
git clone https://github.com/vignesh07/babyshark
cd babyshark/rust
cargo install --path . --force
babyshark --help
```

---

## Features

- Offline: open `.pcap` / `.pcapng` and browse:
  - flows list → packets list → follow stream
  - stream search with highlighting + `n` / `N` navigation
- Live: capture and inspect traffic in the TUI:
  - list capture interfaces
  - live capture with optional display filter
  - optional write-to-file while capturing
- Per-flow analysis:
  - **Health badges** — colored dot (green/yellow/red) on each flow based on RST, incomplete handshakes, retransmissions
  - **Asymmetry labels** — `DL/UL` suffix in flow list + `download-heavy/upload-heavy/balanced` in details (falls back to `A>B/B>A` when local side is ambiguous)
  - **TCP timing** — handshake RTT, server think time, data transfer duration in the details pane
  - **TLS version display** — shows negotiated version from ServerHello when visible, flags deprecated versions (<= TLS 1.1)
- Weird detectors:
  - TCP resets, handshake-not-completed, DNS failures, retransmit/OOO hints, high-latency flows
  - **Deprecated TLS** — flags flows using TLS 1.0 or 1.1
  - **Chatty hosts** — flags ≥10 flows to the same destination within 60 seconds
- Timeline view (`T`):
  - **Gantt** — phase-colored horizontal bars (handshake / TLS / data / close) with hostname labels
  - **Scatter** — per-packet direction/retransmit dot plot
  - Color legends, pattern callouts, and plain-English narrative in details
- Notes/export:
  - bookmark flows
  - export markdown report (latest + timestamped copies)

---

## Install

### Option A: GitHub Release (recommended)

Download a prebuilt binary:
- https://github.com/vignesh07/babyshark/releases

### Option B: build from source

Prereqs:
- Rust toolchain (stable)
- (Live mode only) `tshark`

```bash
git clone https://github.com/vignesh07/babyshark
cd babyshark/rust
cargo install --path . --force
babyshark --help
```

### Option C: cargo install (dev-friendly)

```bash
cargo install --git https://github.com/vignesh07/babyshark --bin babyshark
```

---

## Install `tshark` (re