<p align="center">
<img src="httpcloak.png" alt="httpcloak" width="600">
</p>

<p align="center">
  <a href="https://pkg.go.dev/github.com/sardanioss/httpcloak"><img src="https://pkg.go.dev/badge/github.com/sardanioss/httpcloak.svg" alt="Go Reference"></a>
  <a href="https://pypi.org/project/httpcloak/"><img src="https://img.shields.io/pypi/v/httpcloak" alt="PyPI"></a>
  <a href="https://www.npmjs.com/package/httpcloak"><img src="https://img.shields.io/npm/v/httpcloak" alt="npm"></a>
  <a href="https://www.nuget.org/packages/HttpCloak"><img src="https://img.shields.io/nuget/v/HttpCloak" alt="NuGet"></a>
</p>

<p align="center">
<i>Every Byte of your Request Indistinguishable from Chrome.</i>
</p>

<br>

---

## The Problem

Bot detection doesn't just check your User-Agent anymore.

It fingerprints your **TLS handshake**. Your **HTTP/2 frames**. Your **QUIC parameters**. The order of your headers. Whether your SNI is encrypted.

One mismatch = blocked.

## The Solution

```python
import httpcloak

r = httpcloak.get("https://target.com", preset="chrome-143")
```

That's it. Full browser transport layer fingerprint.

---

## What Gets Emulated

<table>
<tr>
<td width="33%" valign="top">

### 🔐 TLS Layer

- JA3 / JA4 fingerprints
- GREASE randomization
- Post-quantum X25519MLKEM768
- ECH (Encrypted Client Hello)

</td>
<td width="33%" valign="top">

### 🚀 Transport Layer

- HTTP/2 SETTINGS frames
- WINDOW_UPDATE values
- Stream priorities (HPACK)
- QUIC transport parameters
- HTTP/3 GREASE frames

</td>
<td width="33%" valign="top">

### 🧠 Header Layer

- Sec-Fetch-* coherence
- Client Hints (Sec-Ch-UA)
- Accept / Accept-Language
- Header ordering
- Cookie persistence

</td>
</tr>
</table>

---

## Results

```
┌─────────────────────────────────┐
│  ECH (Encrypted Client Hello)   │
├─────────────────────────────────┤
│  WITHOUT:  sni=plaintext        │
│  WITH:     sni=encrypted   +    │
└─────────────────────────────────┘
```

```
┌─────────────────────────────────┐
│  HTTP/3 Fingerprint Match       │
├─────────────────────────────────┤
│  Protocol:        h3       +    │
│  QUIC Version:    1        +    │
│  Transport Params:         +    │
│  GREASE Frames:            +    │
└─────────────────────────────────┘
```

---

## vs curl_cffi

```
┌────────────────────────────────┬────────────────────────────────┐
│        BOTH LIBRARIES          │       HTTPCLOAK ONLY           │
├────────────────────────────────┼────────────────────────────────┤
│                                │                                │
│  + TLS fingerprint (JA3/JA4)   │  + HTTP/3 fingerprinting       │
│  + HTTP/2 fingerprint          │  + ECH (encrypted SNI)         │
│  + Post-quantum TLS            │  + MASQUE proxy                │
│  + Bot score: 99               │  + Domain fronting             │
│                                │  + Certificate pinning         │
│                                │  + Go, Python, Node.js, C#     │
│                                │                                │
└────────────────────────────────┴────────────────────────────────┘
```

---

## Install

```bash
pip install httpcloak        # Python
npm install httpcloak        # Node.js
go get github.com/sardanioss/httpcloak   # Go
dotnet add package HttpCloak # C#
```

---

## Quick Start

### Python

```python
import httpcloak

# Simple request
r = httpcloak.get("https://example.com", preset="chrome-143")
print(r.status_code, r.protocol)

# POST with JSON
r = httpcloak.post("https://httpbin.org/post",
    json={"key": "value"},
    preset="chrome-143"
)

# Custom headers
r = httpcloak.get("https://httpbin.org/headers",
    headers={"X-Custom": "value"},
    preset="chrome-143"
)
```

### Go

```go
import (
    "context"
    "github.com/sardanioss/httpcloak/client"
)

// Simple request
c := client.NewClient("chrome-143")
defer c.Close()

resp, _ := c.Get(ctx, "https://example.com", nil)
body, _ := resp.Text()
fmt.Println(resp.StatusCode, resp.Protocol)

// POST with JSON
jsonBody := []byte(`{"key": "value"}`)
resp, _ = c.Post(ctx, "https://httpbin.org/post",
    bytes.NewReader(jsonBody),
    map[string][]string{"Content-Type": {"application/json"}},
)

// Custom headers
resp, _ = c.Get(ctx, "https://httpbin.org/headers", map[string][]string{
    "X-Custom": {"value"},
})
```

### Node.js

```javascript
import httpcloak from "httpcloak";

// Simple request
const session = new httpcloak.Session({ preset: "chrome-143" });
const r = await session.get("https://example.com");
console.log(r.statusCode, r.protocol);

// POST with JSON
const r = await session.post("https://httpbin.org/post", {
    json: { key: "value" }
});

// Custom headers
const r = await session.get("https://httpbin.org/headers", {
    headers: { "X-Custom": "value" }
});

session.close();
```

### C#

```csharp
using HttpCloak;

// Simple request
using var session = new Session(preset: Presets.Chrome143);
var r = session.Get("https://example.com");
Console.WriteLine($"{r.StatusCode} 