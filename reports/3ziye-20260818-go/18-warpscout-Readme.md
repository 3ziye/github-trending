<h1 align="center">WARPSCOUT</h1>

![WARPSCOUT multi-node](.github/assets/warpscout-multi-node.png)

<p align="center">Find Cloudflare WARP endpoints that work from your network, and see where they come out.</p>

<p align="center">
  <a href="https://github.com/vernette/warpscout/releases"><img src="https://img.shields.io/github/release/vernette/warpscout.svg" alt="GitHub Release"></a>
  <a href="https://github.com/vernette/warpscout/actions/workflows/release.yaml"><img src="https://img.shields.io/github/actions/workflow/status/vernette/warpscout/release.yaml" alt="Build Status"></a>
  <a href="https://github.com/vernette/warpscout/actions/workflows/test.yaml"><img src="https://img.shields.io/github/actions/workflow/status/vernette/warpscout/test.yaml?label=tests" alt="Tests"></a>
  <a href="https://github.com/vernette/warpscout/releases"><img src="https://img.shields.io/github/downloads/vernette/warpscout/total" alt="GitHub Downloads"></a>
  <a href="https://hub.docker.com/r/vernette/warpscout"><img src="https://img.shields.io/docker/pulls/vernette/warpscout?logo=docker" alt="Docker Pulls"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT"></a>
</p>

<p align="center">Documentation: 🇬🇧 English &middot; <a href="README_RU.md">🇷🇺 Русский</a></p>

## Table of contents

- [What it is](#what-it-is)
- [How it works](#how-it-works)
- [Install](#install)
- [Usage](#usage)
- [Scripting](#scripting)
- [SOCKS](#socks)
- [AmneziaWG obfuscation](#amneziawg-obfuscation)
- [MASQUE](#masque)
- [WARP-in-WARP](#warp-in-warp)
- [Docker](#docker-1)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)
- [Support the author](#support-the-author)

## What it is

Cloudflare WARP hands out thousands of endpoint addresses, and there is no built-in way to choose where your tunnel comes out. WARPSCOUT tries those addresses one by one and, for each of them, shows which country the traffic appears to come from and which Cloudflare edge node the tunnel landed on. Latency and packet loss are measured along the way, so among the well-placed endpoints you can also pick a fast one.

Three protocols are supported: plain WireGuard (`wg`), AmneziaWG (`awg`) - an obfuscated version of WireGuard that gets through networks where plain WireGuard is filtered - and MASQUE (`masque`, CONNECT-IP over QUIC, plus its TCP fallback `masque-h2`), Cloudflare's own second transport.

- One static binary
- No root and no TUN device - the tunnel runs in userspace
- Linux, macOS, Windows, Android (Termux) and Docker, on `amd64` and `arm64`
- Live table while it scans, plus a report file that is easy to process (with `awk`, for example)

### Why the edge node matters

Choosing the node is what this tool was written for. Since April 2026, traffic going through the Moscow node (`DME`) is filtered by DPI inside Russia: some sites and services simply do not load through it, even though WARP itself connects fine. The same config, pointed at an endpoint with a different node, works without that problem.

There is no such setting in the official WARP client. The node depends both on where you are and on the endpoint address you connect to, so there is only one way to choose it: test addresses from your own connection and look at where they land. That is what WARPSCOUT does, and what `-node` and `-country` exist for: scan, keep only the endpoints that miss the unwanted node, export a config for the best of them.

### Checking what region a server gets

The other common case is a VPS. WARP determines the region from the address a connection comes from, and the GeoIP databases behind that decision are often wrong: a machine physically standing in the Netherlands can be filed as Indian, and every site the tunnel reaches will treat it that way.

A scan on the server answers that question right away, with the `SEEN AS` column. There is no need to set WARP up and find out afterwards that half your services have moved to another country.

How much the result tells you depends on where the server sits. On most European providers every address lands on the same node with the same region, and the scan fits on one screen:

![WARPSCOUT single node](.github/assets/warpscout-single-node.png)

Russian providers are less predictable: one machine gives you `ARN`, another `HEL`, and some hand out four locations or more across the pools, where there is an actual choice to make:

![WARPSCOUT multi-node](.github/assets/warpscout-multi-node2.png)

## How it works

A scan runs in two phases.

**Phase 1 - which ports get through.** WARP endpoints listen on several UDP ports and stay silent in response to everything except a valid WireGuard handshake. A completed handshake is therefore the only reliable test of whether a port is reachable. WARPSCOUT takes a few addresses and finds out which ports the network lets out. The common ones are tried first, and only if none of them get through are the rest swept. Phase 2 then walks that list per