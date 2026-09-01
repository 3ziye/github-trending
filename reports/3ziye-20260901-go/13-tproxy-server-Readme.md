# tproxy-server

`tproxy-server` is the hosted half of a proof-of-concept WEB proxy type for
Telegram. A Telegram app keeps its normal MTProxy framing and encryption, but sends
all of its proxy TCP connections through one app-owned WebView transport. The
WebView carries a multiplexed session over a server-selected same-origin HTTPS or
WebSocket carrier.
The relay separates the logical streams again and connects each one to a stock
official MTProxy on the server.

The design is not tied to one Telegram client or operating system. Any Telegram
app that can host a WebView and connect its MTProxy sockets to a small local adapter
can implement the client side. The current proof-of-concept work includes a
Telegram Desktop implementation, an experimental Android client described in
[`ANDROID.md`](ANDROID.md), and an iOS client plan in [`IOS.md`](IOS.md). All use
the same bridge page, carrier selection, shared frame format, and server deployment.

The configured hostname remains a regular HTTPS website. A capability derived from
the hostname and MTProxy secret selects a one-shot bridge page; every other normal
request receives the public site.

## How it works

```text
Telegram app
  MTProto connections with the normal MTProxy transform
          |
          v
  local WEB proxy adapter
  one logical stream per app connection
          |
          v
  one WebView transport and authenticated relay session
  multiplexed frames in the selected HTTPS/WebSocket carrier
          |
          v
  tproxy-server -> one local TCP connection per stream -> official MTProxy
```

The app configures only a hostname and an MTProxy secret. It derives the bridge
capability locally and never exposes the raw secret to JavaScript. The WebView
opens the bridge, exchanges a short-lived bootstrap token for a relay session, and
runs the carrier mode selected by the matching server profile. `OPEN`, `DATA`,
`WINDOW`, and `CLOSE` frames multiplex every app connection through that session.
The relay treats DATA as opaque bytes: it cannot choose a Telegram destination or
decrypt the MTProxy stream.

“One WebView transport” means one logical carrier and relay session for the app,
not one HTTP request or backend connection. The profile may use the original
serialized HTTPS carrier, independent HTTPS request lanes per Telegram logical
session, one multiplexed WebSocket, or an independent WebSocket per logical
session.

See [`PROTOCOL.md`](PROTOCOL.md) for the normative wire contract and
[`PLAN.md`](PLAN.md) for the architecture, limits, implementation rationale, and
remaining proof-of-concept work. [`PUBLIC_SITE.md`](PUBLIC_SITE.md) defines the
operator-owned website extension points.

The reference deployment layout is:

```text
Internet :80/:443 -> Caddy -> 127.0.0.1:8080 tproxy-server -> operator site
                                              |                (memory or loopback app)
                                              \-> 127.0.0.1:2398 official MTProxy
```

Only Caddy listens on external interfaces. The relay, its admin endpoints, the
official MTProxy client port, and MTProxy statistics remain local. The relay never
receives a client-selected backend address and never decrypts the MTProxy stream.

Caddy proxies **every** path to the relay. In static mode the relay serves the
whole site from memory through one code path and one header set. In application
mode it delegates ordinary and unauthenticated requests to one private loopback
web application. A request that proves knowledge of a bridge or session token is
intercepted before that application. In either mode there is no separately hosted
relay path for an unauthenticated prober to compare with the public site, and only
`GET /?bridge=<valid capability>` reveals the bridge. Restart the relay after
changing files under `public_dir`; the static site is read once at start-up.

## What you need

- a dedicated lowercase hostname such as `proxy.example.com` that you control;
- an **x86_64** Linux server with a public IPv4 address, SSH access, systemd, and
  either Ubuntu 22.04+ or Debian 12+;
- root or passwordless `sudo` on that server;
- public inbound TCP 80 and 443;
- one random 16-byte secret; and
- an operator-owned static site or a web application bound to a private loopback
  port.

The automated installer is intended for a clean server on which Caddy may own ports
80/443. It backs up an existing `/etc/caddy/Caddyfile`, but it then replaces the
active Caddy configuration. If the server already hosts other sites, use the manual
integration section instead.

## 1. Choose the hostname and secret

At your DNS provider, add an `A` record:

```text
proxy.example.com -> YOUR_SERVER_PUBLIC_IPV4
```

Add an `AAAA` record only when the server really has working public IPv6. Do not put
a CDN or HTTP proxy in front of this first deployment. Publish the hostname to
users in its ACE (`xn--…`) form if it is an internationalised name: the desktop
client stores and derives the capability from