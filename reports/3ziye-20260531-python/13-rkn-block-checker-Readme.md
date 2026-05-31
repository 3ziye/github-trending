# RKN Block Checker

[![PyPI version](https://img.shields.io/pypi/v/rkn-block-checker.svg)](https://pypi.org/project/rkn-block-checker/)
[![CI](https://github.com/MayersScott/rkn-block-checker/actions/workflows/ci.yml/badge.svg)](https://github.com/MayersScott/rkn-block-checker/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A small CLI that figures out whether the connection you're sitting on is in
an RKN/TSPU-blocked zone - and, more usefully, **what kind** of block it is
(DNS poisoning, TCP reset, TLS DPI on SNI, or an ISP stub page).

The point isn't "site X doesn't open." Browsers already tell you that. The
point is to look at each layer of the stack independently and report
*where* it broke. That tells you a lot more about your situation than a
generic "this site can't be reached" page.

## Quick start

```bash
pip install rkn-block-checker
rkn-check
```

That's it. The tool probes a built-in list of sites, classifies each
failure by layer, and prints a verdict. No config, no setup, nothing to
edit.

## Example output

```text
======================================================================
  RKN Block Checker
======================================================================
  IP:       95.165.xxx.xxx
  ISP:      AS12389 Rostelecom
  Location: Moscow, Moscow, RU
----------------------------------------------------------------------

Whitelist (should always work)
  name          verdict                    TCP     TLS     PLT  status
  --------------------------------------------------------------------
  gosuslugi     ✓ OK                      18ms    42ms   380ms  200
  yandex        ✓ OK                       8ms    25ms    95ms  200
  sberbank      ✓ OK                      12ms    38ms   250ms  200
  vk            ✓ OK                       9ms    28ms   180ms  200
  ...

Blacklist (RKN-restricted)
  name          verdict                    TCP     TLS     PLT  status
  --------------------------------------------------------------------
  instagram     ~ LIKELY TLS DPI          22ms       -       -  -
    └ TLS reset right after ClientHello - consistent with SNI-based DPI
  twitter/x     ~ LIKELY TLS DPI          24ms       -       -  -
    └ TLS handshake silently dropped - consistent with DPI filtering
  rutracker     ✗ HTTP STUB               18ms    45ms   120ms  200
    └ response body matches a known ISP stub-page marker
  protonvpn     ✗ DNS                        -       -       -  -
    └ system DNS doesn't resolve, DoH does - consistent with DNS poisoning

======================================================================
  Summary
----------------------------------------------------------------------
  Whitelist: 21/21 working
  Blacklist: 3/15 open, 12/15 blocked

  → Likely in an RKN-blocked zone (medium confidence).
    Most blacklist failures match censorship patterns (TLS DPI, TCP RST),
    but those signals can also be caused by server-side issues. A control
    vantage point would confirm.

  Block types in the blacklist:
    ~ LIKELY TLS DPI: 8
    ✗ DNS: 2
    ✗ HTTP STUB: 2
======================================================================
```

Verdict labels are **calibrated by confidence**: `✗` means a high-confidence
diagnosis (e.g. DNS poisoning confirmed by DoH, HTTP 451, a known stub-page
marker), `~ LIKELY` means a known censorship pattern matched but a single
signal can't rule out a server-side issue, and `?` means the symptom is
ambiguous. The summary line says so plainly - "high confidence", "medium
confidence", or "inconclusive" - and never claims more certainty than the
underlying signals support.

## Why this exists

If a site doesn't open, your browser tells you that. But if you want to
*do* something about it - pick the right circumvention tool, file a useful
bug report, or just understand what's happening to your traffic - you need
to know which part of the network stack is actually being interfered with.

Different censorship mechanisms leave different fingerprints:

- **DNS poisoning** is the cheapest and oldest. The ISP's resolver lies
  about a domain.
- **TCP reset** is IP-level blackholing. Rare in practice - most ISPs
  don't bother.
- **TLS DPI on SNI** is the modern TSPU/RKN signature. The middlebox
  watches for the SNI extension in the TLS ClientHello and tears the
  connection down once it sees a blocked hostname.
- **HTTP stub pages** are the polite kind: an ISP-controlled page served
  back with a "blocked by RKN" body, often with status 200 or the
  rarer-but-explicit 451.

`rkn-check` walks DNS → TCP → TLS → HTTP for each target and stops at the
first thing that fails. Whichever layer broke becomes the verdict.

## Common scenarios

### Just diagnose the connection you're on

```bash
rkn-check
```

Probes the built-in lists (~21 control sites, ~15 RKN-restricted), prints
a 