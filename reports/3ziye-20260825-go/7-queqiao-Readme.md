<p align="center">
  <img src="assets/queqiao-icon.png" width="144" alt="Queqiao project icon">
</p>

<h1 align="center">Queqiao</h1>

<p align="center">
  <strong>Make difficult long-haul links feel local.</strong><br>
  An open-source, self-hosted transport for TCP and UDP across a known WAN bottleneck.
</p>

<p align="center">
  <a href="docs/DEPLOYING.md">Deploy</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="docs/STATUS.md">Project status</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

During my internship at Microsoft Research Asia in 2013,
I used Microsoft's dedicated link from China and saw,
for the first time, how fast access to Google and YouTube could be.

Later, I built a detour gateway in Hong Kong to improve the China-US route when I'm back home.
It worked, but it added infrastructure, doubled the network bandwidth cost, and increased
latency. Is it possible to directly connect China to US while
enjoying the same latency and bandwidth with dedicated links?

Although I did networking research for 10 years, I did not have the time to build it.
It is finally possible with help from Kimi K3, Claude Opus 5 and GPT-5.6 Sol.
Today, Queqiao is a ready-to-use, self-hosted protocol for supported
client-to-gateway deployments. It carries TCP and UDP through a local proxy over
an authenticated transport, and keeps evolving as we measure more paths,
improve the transport, and learn from users.

## Why Queqiao?

Many transports make each connection learn and react on its own. That is a
reasonable default for the general Internet, but it leaves performance on the
table when many application flows share the same difficult client-to-gateway
segment.

The path that motivated Queqiao made the problem concrete: we measured roughly
42–45% downstream packet erasure even below the path's capacity knee, followed
by clustered loss when aggregate traffic exceeded that knee. Those two regimes
need different responses. Backing off does not remove independent erasure;
ignoring overload only makes it worse. See the full
[path characterization](docs/PATH-CHARACTER-20260813.md).

Queqiao is built around a few practical observations:

- **Flows sharing one bottleneck should share one model.** Flows to different final
  destinations can still share one client-to-gateway path, so Queqiao shares
  delivery, loss, RTT, pacing, and latency-reserve state across them.
- **Not all packet loss means congestion.** The controller distinguishes a measured
  erasure floor from loss caused by an overloaded bottleneck instead of treating
  every missing packet as congestion.
- **Choose recovery for the path.** On a long-RTT path, forward-error
  correction can recover a gap sooner than another round trip; as a flow grows,
  retransmission can become the more efficient choice.
- **Protect interactive traffic from bulk transfers.** Control and new interactive
  work must not wait behind a bulk transfer, so aggregate pacing, priority, and
  reactive isolation protect latency while the pipe is used.
- **Upstream and downstream are different.** Upstream and downstream can have very
  different capacity and loss behavior, so they are measured and controlled
  independently.

These are operating principles, not universal performance claims. Queqiao is a
good fit when the client and gateway are known, trusted endpoints and their
shared WAN segment is the dominant bottleneck. If the real bottleneck is
somewhere else, measure again before relying on the optimization.

## How it works

```mermaid
flowchart LR
    A[Applications<br/>Web · SSH · video · transfers] --> B[Local SOCKS5<br/>Queqiao client]
    B ==>|one coordinated long-haul path| C[Provider gateway]
    C --> D[Internet destinations]
```

Queqiao presents an ordinary local SOCKS5 proxy, including UDP ASSOCIATE. The
client and provider gateway form one authenticated transport session. Inside
that session, every flow uses the same logical framing, byte-offset recovery,
acknowledgement ranges, and scheduling machinery. QUIC streams and datagrams
are used when available, with authenticated TLS/TCP fallback for restrictive
networks.

The application does not have to choose a “short-flow,” “interactive,” or
“bulk” protocol. Queqiao observes how a flow behaves and adjusts policy inside
the same architecture. HTTPS remains end-to-end; the gateway sees the
destination and traffic shape, but Queqiao does not inspect application content.

## How Queqiao compares

| System | Shared path model | Recovery strategy | Bulk median | SSH p99 under bulk load |
| --- | --- | --- | ---: | ---: |
| **Queqiao** | Shared endpoint pair | Erasure-aware FEC + retransmission | **143.1 Mbit/s** | 940 ms |
| TUIC v5 | Usually per connection | QUIC recovery | 76.8 Mbit/s | **662 ms** |
| Hysteria 2 | Usually per connection | Protocol-specific UDP/QUIC recovery | 90.2 Mbit/s | **526 ms** |

These are representative results from a six-round real-path campaign. They
show why Queqiao's shared path model