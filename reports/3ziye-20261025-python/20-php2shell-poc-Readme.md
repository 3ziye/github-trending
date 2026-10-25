<p align="center">
  <img src="docs/cover.png" alt="php2shell" width="700">
</p>

<h1 align="center">php2shell</h1>
<p align="center">
  <strong>CVE-2026-109618 & CVE-2026-109619 — PHP Pre-Auth RCE Exploit & Detection Toolkit</strong>
</p>
<p align="center">
  <a href="https://github.com/ikow/php2shell-poc/stargazers"><img src="https://img.shields.io/github/stars/ikow/php2shell-poc?style=flat-square" alt="Stars"></a>
  <img src="https://img.shields.io/badge/CVSS-9.2%20Critical-red?style=flat-square" alt="CVSS 9.2">
  <img src="https://img.shields.io/badge/PHP-5.4%E2%80%938.5-orange?style=flat-square" alt="Affected Versions">
  <img src="https://img.shields.io/badge/Fixed-8.2.35%20%7C%208.3.36%20%7C%208.4.27%20%7C%208.5.12-green?style=flat-square" alt="Fixed Versions">
  <img src="https://img.shields.io/badge/Exploits-3%20public%20%7C%202%20paid-blue?style=flat-square" alt="Exploits">
</p>

<p align="center">
  <a href="#exploits">Exploits</a> · <a href="#detection-rules">Detection</a> · <a href="#quick-start">Lab</a> · <a href="https://qideng.substack.com/p/php2shell-dissecting-phps-critical">Writeup</a>
</p>

---

Five independent RCE chains exploiting PHP's `session.upload_progress` and the Zend engine's OOM bailout. **14 years of vulnerable code** — PHP 5.4.0 (2012) through 8.5.11. Pre-auth. No application vulnerability required for some chains.

Impacts **78% of all websites** — including WordPress (43%), Joomla, Drupal, Laravel, Magento, and every default PHP installation.

**Author:** [Qi Deng](https://github.com/ikow) &nbsp;|&nbsp; **Writeup:** [Substack](https://qideng.substack.com/p/php2shell-dissecting-phps-critical) &nbsp;|&nbsp; **Date:** 2026-10-21

## CVE Details

| CVE | GHSA | CVSS | Description |
|-----|------|------|-------------|
| CVE-2026-109618 | [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) | 9.2 | OOM → `longjmp()` leaves Zend engine state invalid → RCE |
| CVE-2026-109619 | [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) | 9.2 | Stale global state across FPM worker requests → UAF → RCE |

**Patch:** [Commit 3584a98](https://github.com/php/php-src/commit/3584a98bda) — 300 files changed across the Zend engine.

## Attack Chains

| Chain | Vector | Pre-auth | Conditions | SAPI |
|-------|--------|:--------:|------------|------|
| **A** | Session injection + LFI | Yes | App has any LFI sink | All |
| **B** | var_destroy UAF → handler overwrite | No | App calls `unserialize()` | All |
| **C** | Handler mismatch → `__destruct` | Yes | Two dirs with different serialize_handler | FPM |
| **D** | OOM corruption → stale `EG()` | Yes | **None** — any endpoint | mod_php |
| **E** | FPM session OOM → stale `BG()` | Yes | Producer: any `session_start()` endpoint; Consumer: **any** endpoint | FPM |

Chain D is the most critical: **zero-dependency pre-auth RCE** against any Apache mod_php installation.

Chain E is nearly as broad on FPM: the producer needs any endpoint that calls `session_start()` (near-universal — WordPress, Laravel, Joomla, Drupal all do), and the **consumer can be any PHP endpoint** — the `rfc1867` upload_progress handler runs during SAPI startup before application code. Verified: `nosession.php` (no `session_start()` in code) triggers 502 crash when consuming stale `BG(unserialize)` state.

## Exploits

Three RCE exploits (Chains A, B, C) are included in [`exploit/`](exploit/):

| File | Chain | What It Does |
|------|-------|-------------|
| `chain_a_session_lfi.py` | A | Injects PHP code via upload filename → LFI includes session file → RCE |
| `chain_b_uaf_rce.php` | B | var_destroy UAF → discovers `zif_system` via EG() → overwrites `var_dump` handler via `/proc/self/mem` → RCE |
| `chain_c_mismatch_rce.py` | C | Pollutes FPM worker `PS(serializer)` → injects serialized object via filename → `__destruct` fires on decode failure → RCE |

Chains D and E exploits are available to [paid subscribers](https://qideng.substack.com/p/php2shell-dissecting-phps-critical).

```bash
# Chain A: Session injection + LFI → RCE
python3 exploit/chain_a_session_lfi.py --host TARGET --port 80 --command 'id'

# Chain B: var_destroy UAF → RCE (run on target or via uploaded webshell)
php exploit/chain_b_uaf_rce.php

# Chain C: Handler mismatch → __destruct → RCE
python3 exploit/chain_c_mismatch_rce.py --host TARGET --port 80 --command 'id'
```

## Detection Rules

Pre-built IDS / WAF / SIEM rules in [`detection/`](detection/):

| File | Format | Signatures |
|------|--------|-----------|
| `php2shell.rules` | Suricata / Snort | 13 rules — request, response, and recon |
| `php2shell.yaml` | Sigma | 5 rules — web logs, process creation, file events |
| `modsecurity.conf` | ModSecurity v2/v3 | 7 rules — drop-in for Apache/Nginx |
| `php2shell.lua` | OpenResty Lua | Lightweight reverse proxy module |

**Fastest mitigation:** block `PHP_SESSION_UPLOAD_PROGRESS` in multipart POST bodies. Near-zero legitimate use