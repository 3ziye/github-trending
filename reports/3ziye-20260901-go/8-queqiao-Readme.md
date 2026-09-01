<p align="center">
  <img src="assets/queqiao-icon.png" width="144" alt="Queqiao project icon">
</p>

<h1 align="center">Queqiao</h1>

<p align="center">
  <strong>Make difficult long-haul links feel local.</strong><br>
  An open-source, self-hosted transport for TCP and UDP across a long link you control both ends of.
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

### Not only client to gateway, but also inter-datacenter

The same problem turned up between two datacenter servers. This has been our own
pain point since 2023: the models run in the US and the clients are everywhere.
ASR sends a few hundred kilobytes of audio up and gets a sentence back.
TTS sends a sentence up and gets a few hundred kilobytes back, in one
burst once the model finishes. Each is a single transfer that has to finish
before anything else happens, which is the shape a long path is worst at.

Guiyang, China to a model in Irvine, US: a 355KB audio upload takes **1185ms**, of
which the ASR model only spends about 30ms.
In theory, the path's bandwidth could carry 355KB in about 9ms.
The rest is a handshake, a transfer starting at ten segments, and a window
thrown away between requests.
Queqiao approaches the limits of this 200ms RTT link, achieving **302ms** end-to-end
on a cold connection and **237ms** once warm, which is the floor. On a sustained
transfer it reaches **310 Mbit/s**, 93% of what the path itself carries, against
3.6 to 106 Mbit/s for direct TCP.
[Why this profile exists](docs/DESIGN-DC-PROFILE.md) walks through each request; [the
runbook](docs/DEPLOYING-DC-PROFILE.md) is how to deploy it.

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
- **Not all packet loss means congestion.** A path that erases packets
  independently of the sending rate is not an overloaded one, and backing off
  does not make an erasure channel drop less. So loss is not the congestion
  signal here: the brake is a delay bound, the round trip may not exceed twice
  the path's own minimum, and the measured erasure is what sizes the code and
  compensates the window instead. A policer, which drops without queueing, is
  the case this does not yet brake -- see the [known
  limitations](docs/KNOWN-LIMITATIONS.md).
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
shared WAN segment is the 