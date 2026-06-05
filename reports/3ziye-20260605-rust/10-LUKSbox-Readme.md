<!-- markdownlint-disable MD041 -->

<p align="center">
  <a href="https://luksbox.penthertz.com/">
    <img src="assets/luksbox-logo.png" alt="LUKSbox" width="180">
  </a>
</p>

<h1 align="center">LUKSbox</h1>

<p align="center">
  <strong>Encrypted vaults that survive the next decade.</strong><br>
  Open-source, FIDO2 + TPM 2.0 native, post-quantum-ready.<br>
  <em>Store sensitive files in the cloud or on shared media without trusting the host.</em>
</p>

<p align="center">
  <a href="https://penthertz.com" title="By Penthertz">
    Built by
    <img src="assets/penthertz-logo.png" alt="Penthertz" height="22" valign="middle">
  </a>
</p>

<p align="center">
  <a href="https://luksbox.penthertz.com/"><strong>Website</strong></a> |
  <a href="https://luksbox.penthertz.com/docs/"><strong>Docs</strong></a> |
  <a href="https://luksbox.penthertz.com/docs/security/architecture/"><strong>Security</strong></a> |
  <a href="https://luksbox.penthertz.com/docs/security/tests/"><strong>Fuzzing</strong></a> |
  <a href="https://luksbox.penthertz.com/compare/"><strong>Compare</strong></a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>
  <a href="https://www.rust-lang.org/"><img alt="Made with Rust" src="https://img.shields.io/badge/made%20with-Rust-orange.svg"></a>
  <img alt="Status: pre-1.0" src="https://img.shields.io/badge/status-pre--1.0-yellow.svg">
</p>

---

## What it solves

You probably already store sensitive files where you don't fully
control the storage: cloud sync (iCloud, Drive, Dropbox, OneDrive,
S3, Backblaze), NAS units, USB sticks that travel, backup tapes that
end up at a recycler. The provider promises encryption-at-rest "with
their keys." LUKSbox encrypts the file before it ever leaves your
machine, under **your** keys, in a single container that is opaque to
the provider and tamper-evident on the way back.

A LUKSbox vault is one file (`.lbx`), optionally with a separate
header (`.hdr`) and post-quantum sidecar (`.kyber`) that you keep on
different storage. Drop it on any cloud or shared medium. The
provider sees one indistinguishable-from-random blob and cannot
decrypt it even under legal compulsion. Mount it locally as a real
drive when you need to use it.

| Concern | Plain cloud upload | Cloud + provider encryption | LUKSbox vault on cloud |
|---|---|---|---|
| Provider can read your files | Yes | Yes (they hold the key) | **No** |
| Government request to provider exposes data | Yes | Yes | **No** |
| Silent file tamper detected | No | Sometimes (TLS in transit only) | **Yes** (per-chunk AEAD) |
| Whole-vault rollback detected | No | No | **Yes** (anchor sidecar) |
| "Harvest now, decrypt later" (post-quantum) | Vulnerable | Vulnerable | **ML-KEM-768/1024 hybrid slot** |
| Hardware-key requirement to open | N/A | Provider-specific | **FIDO2 / TPM / Windows Hello** |
| Vault file looks like random data | No | No | **Yes** (with detached header) |
| Source you can audit | No | No | **Yes** (Apache-2.0) |

The full per-tool comparison (vs LUKS2 / VeraCrypt / age / gocryptfs /
Cryptomator / BitLocker / FileVault) lives at
<https://luksbox.penthertz.com/compare/>.

> **A LUKSbox vault is a *travelling* copy, not a *master* copy.**
> Use it for the cloud, a USB stick, a vault you share with a
> colleague or client, anywhere you would not put plaintext. Like
> every encrypted container it is a single point of failure: if the
> `.lbx` file is corrupted or every keyslot becomes inaccessible,
> the data is gone. The forensic toolkit (`header-backup`, `check`,
> `extract --tolerate-errors`) helps in many damage scenarios but
> cannot recover bytes that are no longer on disk or no longer
> AEAD-tagged. Always keep an unencrypted copy somewhere you trust
> for any file you cannot afford to lose.

---

## Status

This is a **pre-1.0** release. The on-disk format is locked, the
cryptographic primitives are NIST/RFC standards built on RustCrypto,
and 9 internal audit rounds have shipped. External paid audit and
broader real-world deployment are the next milestones. The
cloud-storage threat model, provider can't read your data even under
subpoena, is what LUKSbox is built for and what it does today.

| Surface | State |
|---|---|
| `cargo test --workspace` | 200+ passing, 0 failing, 0 ignored |
| `cargo audit` (Linux/macOS) | 0 vulns / 0 unsound / 0 unmaintained |
| `cargo audit` (Windows) | 1 unmaintained (`registry`, transitive via WinFsp) |
| Internal audit rounds | 9 documented at <https://luksbox.penthertz.com/docs/security/audit/> (per-round details kept internal) |
| Third-party audit | not yet performed; engagement scope package available on request to `security@penthertz.com` |
| Fuzz iterations across 10 libFuzzer harnesses | 30M+ |

---

## How a vault is opened

```mermaid
flowchart LR
    User[User knowledge<br/>passphrase or PIN] --> Unlock[Unlock material]
    FIDO[FIDO2 authenticator<br/>hmac-se