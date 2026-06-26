# Encrypted Collaboration Spaces

A cryptographic framework for building collaborative applications over an
untrusted server, and a working prototype implementation.

The cryptographic design is described in full in the
[whitepaper](https://encryptedspaces.org/whitepapers/encrypted-spaces.pdf). For a
high-level overview of the project, see
[encryptedspaces.org](https://encryptedspaces.org).

## ⚠️⚠️⚠️ DO NOT USE IN PRODUCTION ⚠️⚠️⚠️

This is experimental code published for research purposes.

The implementation remains under active development and has not yet undergone the level of security review, testing, auditing, and hardening required for production deployment. The issues tracked in this repository are not a complete accounting of security limitations, known issues, or remaining risks.

***This code MUST NOT be used to protect sensitive data or in security-critical applications.***

For example:
- **Authentication is a placeholder.** The reference server accepts a
  client-asserted identity on connection and does not yet verify it. Security
  rests on the cryptographic verification each client performs on server
  responses, *not* on server-enforced access control.
- **Fast-forward proofs require `--features real-proofs`.** Default builds run
  RISC Zero in dev mode (`RISC0_DEV_MODE=1`), which accepts non-cryptographic
  "fake" receipts for fast iteration. Builds intended to rely on succinct
  fast-forward proofs must enable the `real-proofs` feature.
- **DoS hardening is incomplete.** Some deserialization paths are not yet
  depth-bounded, so malformed input can exhaust resources. The insider-DoS
  resistance described in the design goals below is a target, not a hardened
  guarantee in this prototype.

## What is this?

Most collaboration software stores shared application state on servers in
plaintext, requiring users to trust those servers (and any integrated
services) with the contents of their documents, chats, and databases.
End-to-end encryption addresses messaging but does not directly generalize
to applications where participants must read, modify, and verify long-lived
structured state.

An *Encrypted Collaboration Space* is a shared, mutable application state
with dynamic membership, shared cryptographic key material, an authenticated
history of operations, and a verifiable database representing current
contents. The server holds only ciphertexts and proof material; clients
verify every server response locally with cryptographic proofs.

The design targets four security properties:

- **Verifiable history.** Members can confirm that the membership list and
  shared data are the correct result of all previous operations.
- **Selective data retention.** Members can delete shared data items and
  give new members access to the non-deleted older data.
- **Insider robustness.** Malicious insiders cannot compromise security of
  communications occurring before or after their membership, or cause
  denial of service for other members.
- **Deniable sender authentication.** Members can authenticate the author
  of each data object without producing publicly-verifiable cryptographic
  evidence of user relationships.

## Architecture at a glance

- **Changelog.** Append-only, hash-chained log of operations. The
  authenticated history of a Space.
- **Verifiable database.** Current state exposed via Merkle search trees;
  clients check the database commitment against the latest changelog
  commitment on every response.
- **Tables, lists, text.** Relational rows with primary-key and
  secondary-index search trees; ordered lists via keyless
  order-statistic trees; collaborative text layered on lists.
- **Membership.** A members table tracks who can participate. Existing
  members invite new ones by issuing provisional keys; removal triggers a
  rekey of the remaining members, without requiring re-encryption of data.
- **Access control.** Per-table rules constrain which members can write or
  delete which rows, enforced cryptographically rather than by
  server policy.
- **Retention.** Members can grant new joiners access to historic data, or
  selectively delete data before a chosen point so neither the server nor
  future members can read it, without re-encrypting the entire Space.
- **Fast-forward proofs.** Succinct zero-knowledge proofs that let clients
  skip ahead in the changelog without replaying every operation.

## Repository layout

| Path           | Contents                                                |
| -------------- | ------------------------------------------------------- |
| `sdk/`         | Client SDK and verifiable database API (start here)     |
| `crypto/`      | Core cryptographic primitives                           |
| `zkp/`         | Zero-knowledge proof system                             |
| `ffproof/`     | Fast-forward changelog proofs                           |
| `retention/`   | Selective data retention construction                   |
| `key_manager/` | Group key sta