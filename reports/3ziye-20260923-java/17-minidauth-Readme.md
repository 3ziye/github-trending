<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo.svg" alt="minidauth" width="380">
  </picture>
</p>

<p align="center"><strong>Give your existing login a key that nobody holds.</strong></p>

<p align="center">
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-111.svg"></a>
  <img alt="Java 17+" src="https://img.shields.io/badge/java-17%2B-111.svg">
  <img alt="124 tests passing" src="https://img.shields.io/badge/tests-124%20passing-111.svg">
</p>

Your app can already tell who someone is. What it cannot do is stop itself reading their data. The
database holds the rows, the app holds the key, and taking the machine takes both.

minidauth moves the key out. It exists only as shares spread across the [Tide](https://tide.org)
network, and no single node can reconstruct it. That key signs every token, policy and role grant
your system issues, and decides who may decrypt, and none of those decisions are your server's to
make. Your login stays exactly where it is: Cognito, Better Auth, Keycloak, Auth.js, whatever you
already run.

> **A stolen copy of your database contains nothing readable, and no key to make it readable.**

![minidauth in a minute](examples/notes/docs/demo.gif)

That is the [notes demo](examples/notes). No password, no user table, roles granted by a quorum, and
a database holding nothing but ciphertext.

The same key signs as well as encrypts, and signing is the busier half. Every sign-in token, every
policy, every role grant is an EdDSA signature produced jointly by a threshold of nodes. Nothing is
signed locally, which is why owning the server does not let you forge a role or mint a token the
network will accept.

It also means the network can refuse. Ask it to sign a payment over the limit its policy allows and
fourteen nodes independently decline, somewhere your code does not run. That is
[in the demo too](examples/notes#signing-which-encryption-cannot-do).

**[Try it](#quick-start)** in two commands, or read on for whether it is for you.

## What you actually get

| | |
|---|---|
| **A key that is never assembled** | Not "stored in an HSM", not "held by a service". It exists as shares, and a threshold of independent nodes cooperate to use it. There is no moment where the whole key exists. |
| **Every signature is a joint one** | Sign-in tokens, policies, role grants. Nothing minidauth issues is signed on your server, so taking the server does not let you forge a role or mint a token the network accepts. |
| **Identity you did not have to hold** | Sign-in happens in the ORKs' own enclave. No password reaches your application or this service, so there is none to leak. |
| **Role grants that need more than one person** | A grant is filed, approved by administrators in their own enclaves, and only then does the network sign the attestations that make it real. |
| **Reads decided by policy, not by your code** | The ORKs check the caller's role against a signed policy before they will help decrypt. Your app cannot decide to read; it can only ask. |
| **Your auth system untouched** | Store one extra column, a `vuid`, and add one callback route. |

Encryption is the visible one, and the easiest to check, which is why the demo leads with it. It is
not the whole of what the key does.

**Signing is the half that decides what may happen at all.** A custom request has its payload read by
the policy's contract before the cohort will sign, so the network can decline. The
[demo](examples/notes#signing-which-encryption-cannot-do) signs `amount=250;to=alice` and refuses
`amount=5000;to=alice`, with fourteen nodes independently answering "over the limit this policy will
sign". That refusal happens where your code does not run, so owning your server does not produce the
signature anyway. Approving a release, authorising a refund, issuing a credential: same shape.

## Projects minidauth'd

Open source apps forked to seal their most sensitive data before it reaches Postgres, so the app and
its database only ever hold `ms1:` ciphertext and only a quorum-granted role can read it. Each is off
unless `MINIDAUTH_SEAL_URL` is set, so an unconfigured checkout behaves exactly like upstream. Full
write-ups, with how each is wired, at [dauth.me/projects](https://www.dauth.me/projects/).

| Project | What it is | What gets sealed |
|---|---|---|
| [Twenty](https://www.dauth.me/projects/twenty/) | CRM | Every personal field on a contact, decrypted in the browser so the server never sees plaintext |
| [Cal.diy](https://www.dauth.me/projects/cal/) ([fork](https://github.com/sashyo/cal.diy)) | Scheduling (Cal.com) | Attendee names and phone numbers, booking titles and descriptions |
| [Formbricks](https://www.dauth.me/projects/formbricks/) ([fork](https://github.com/sashyo/formbricks)) | Surveys | The answers people submit |
| [Documenso](https://www.dauth.me/projects/documenso/) ([fork](https://github.com/sa