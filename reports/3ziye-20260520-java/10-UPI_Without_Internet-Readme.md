# UPI Offline Mesh — Demo

A Spring Boot backend that demonstrates **offline UPI payments routed through a Bluetooth-style mesh network**. You're in a basement with zero connectivity. You send your friend ₹500. Your phone encrypts the payment, broadcasts it to nearby phones, and the packet hops device-to-device until *some* phone walks outside, gets 4G, and silently uploads it to this backend. The backend decrypts, deduplicates, and settles.

This repo is the **server side** of that system, plus a software simulator of the mesh so you can demo the whole flow on a single laptop without any real Bluetooth hardware.

---

## Table of Contents

1. [What this demo proves](#what-this-demo-proves)
2. [How to run it](#how-to-run-it)
3. [The demo flow (step by step)](#the-demo-flow-step-by-step)
4. [Architecture](#architecture)
5. [The three hard problems and how they're solved](#the-three-hard-problems-and-how-theyre-solved)
6. [File-by-file walkthrough](#file-by-file-walkthrough)
7. [API reference](#api-reference)
8. [Tests](#tests)
9. [What's NOT real (and what would change for production)](#whats-not-real-and-what-would-change-for-production)
10. [Honest limitations of the concept](#honest-limitations-of-the-concept)

---

## What this demo proves

The system shows three things working end to end:

1. **A payment can travel from sender to backend through untrusted intermediaries** without any of them being able to read or tamper with it. (Hybrid RSA + AES-GCM encryption.)
2. **Even if the same payment reaches the backend simultaneously through multiple bridge nodes, it settles exactly once.** (Idempotency via atomic compare-and-set on the ciphertext hash.)
3. **A tampered or replayed packet is rejected** before it touches the ledger.

You'll see all three in the dashboard.

---

## How to run it

### Prerequisites

- **JDK 17 or newer** installed and on PATH (or `JAVA_HOME` set). Check with `java -version`.
- That's it. No database, no Redis, no Maven (the wrapper handles it). Just Java.

### Run on Windows

Open a terminal in the project folder and run:

```cmd
mvnw.cmd spring-boot:run
```

The first run downloads Maven (~10 MB) and all dependencies (~80 MB) — give it a couple of minutes. Subsequent runs start in a few seconds.

### Run on Mac/Linux

```bash
./mvnw spring-boot:run
```

### Open the dashboard

Once you see `Started UpiMeshApplication in X.XXX seconds`, open:

**http://localhost:8080**

You'll get a dark dashboard with everything you need to drive the demo.

### Stop the server

`Ctrl+C` in the terminal.

### Run the tests

```cmd
mvnw.cmd test
```

The interesting one is `IdempotencyConcurrencyTest` — it fires three threads delivering the same packet simultaneously and asserts that exactly one settles.

---

## The demo flow (step by step)

The dashboard has four buttons that walk through the full pipeline. The intended sequence:

### Step 1 — Compose a payment

Choose sender, receiver, amount, PIN. Click **"📤 Inject into Mesh"**.

**What actually happens on the backend:**
- The server pretends to be the sender's phone.
- It builds a `PaymentInstruction` with a unique nonce and current timestamp.
- It encrypts that with the server's RSA public key (using hybrid encryption — see below).
- It wraps the ciphertext in a `MeshPacket` with a TTL of 5.
- It hands the packet to `phone-alice`, an offline virtual device.

You'll see `phone-alice` now holds 1 packet.

### Step 2 — Run gossip rounds

Click **"🔄 Run Gossip Round"**. Then click it again.

Each round, every device that holds a packet broadcasts it to every other device within "Bluetooth range" (which, in our simulator, means everyone). TTL decrements per hop.

After 1 round: every device holds the packet. After 2 rounds: still every device — TTL is just lower.

In the real system this would happen organically as people walk past each other in the basement.

### Step 3 — Bridge node walks outside

Click **"📡 Bridges Upload to Backend"**.

`phone-bridge` is the only device with `hasInternet=true`. The dashboard simulates that phone walking outside and getting 4G. It POSTs every packet it holds to `/api/bridge/ingest`.

The backend pipeline runs:
1. Hash the ciphertext (`SHA-256`).
2. Try to claim the hash in the idempotency cache.
3. If claimed: decrypt with the server's RSA private key.
4. Verify freshness (signedAt within 24 hours).
5. Run the debit/credit in a single DB transaction.

Watch the **Account Balances** table — money has moved. Watch the **Transaction Ledger** — a new row appears.

### Step 4 — Demonstrate idempotency (the killer feature)

Reset the mesh. Inject a single packet. Run gossip 2 times. Now **all 5 devices hold the same packet, including multiple bridges in a more complex setup**.

To really see idempotency in action, modify `MeshSimulatorService.java` to seed multiple bridge devices, or just:

1. Click "Inject" once.
2. Click "Gossip" twice.
3. Click "Flush Bridges" — only `phone-bridge` is a bridge in the default seed