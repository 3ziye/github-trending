<div align="center">
  <img src="https://raw.githubusercontent.com/IRNova/Nova-Proxy-App/main/logo.svg" width="120" height="120" alt="NovaProxy Logo">
  <h1>NovaProxy</h1>
  <p><strong>Cloudflare IP Shaper — Domain Fronting Proxy with MITM + GSA Relay Engines</strong></p>
  <p>عبور از فیلترینگ هوشمند با دامنه‌فرانتینگ مبتنی بر Google Apps Script و Cloudflare Worker</p>
</div>

<p align="center">
  <a href="https://github.com/IRNova/Nova-Proxy-App/blob/main/README.en.md">🇬🇧 English Version</a>
</p>

---

<a name="fa"></a>

## معرفی

NovaProxy یک پروکسی دسکتاپ (Wails v3 / Go) است که ترافیک اینترنت را از طریق زیرساخت Google و Cloudflare عبور می‌دهد. از دید سیستم DPI، همه ترافیک شبیه ارتباط عادی با `www.google.com` است، در حالی که درخواست واقعی به هر سایتی ارسال می‌شود.

دو هسته اصلی:

| هسته | وظیفه |
|------|--------|
| **MITM Engine** | خاتمه TLS، گواهی‌سازی داینامیک، SNI spoofing، fragmentation |
| **GSA Relay** | رله ترافیک از Google Apps Script → Cloudflare Worker با H2 multiplexing |

---




## MITM Engine

هسته MITM وظیفه **خاتمه TLS و بازرمزگذاری** را بر عهده دارد تا ترافیک HTTPS قابل بازرسی و مسیریابی باشد.

```
Client → CONNECT tunnel → TLS Termination (MITM Cert) → Upstream TLS (SNI spoofed) → Target
                            │
                     Dynamic Cert Generation
                     (ECDSA P256 signed by Root CA)
```

### معماری MITM

```
ProxyServer.handleConnect()
    │
    ├── direct        → TCP tunnel خام
    ├── transparent   → انتقال بایت‌های TLS بدون خاتمه
    ├── tls-rf        → تکه‌تکه کردن ClientHello + tunnel
    ├── quic          → MITM روی QUIC/HTTP3
    └── mitm          ──► handleMITM()
                            │
                    ┌───────▼────────┐
                    │  establishUpstreamConn()
                    │  - resolve candidates
                    │  - uTLS handshake (fingerprint randomization)
                    │  - ALPN negotiation (h2 / http/1.1)
                    │  - ECH support
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  makeMITMTLSConfig()
                    │  - generateCert(host, CA cert, CA key)
                    │  - ECDSA P256 per-host cert
                    │  - cache certs in memory
                    │  - serve to client via tls.Server()
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  directTunnel()
                    │  - bidirectional copy (pooled buffers)
                    │  - client ↔ upstream
                    └────────────────┘
```

### امکانات MITM

| قابلیت | توضیح |
|---------|---------|
| **گواهی‌سازی داینامیک** | تولید گواهی ECDSA P256 برای هر دامنه در لحظه، امضا شده توسط Root CA (RSA 2048) |
| **مدیریت Root CA** | ایجاد، نصب و مدیریت CA روی Windows / macOS / Linux / Firefox |
| **خاتمه TLS** | قطع اتصال TLS کلاینت، اتصال مجدد به سرور مقصد با SNI جعلی |
| **SNI Spoofing** | جایگزینی SNI واقعی با دامنهٔ جلویی (مثلاً `www.google.com`) |
| **uTLS Fingerprint** | تقلید اثر انگشت TLS مرورگر Chrome یا Firefox با `refraction-networking/utls` |
| **TLS Fragmentation** | تکه‌تکه کردن ClientHello به چند segment با تأخیر قابل تنظیم برای عبور از DPI |
| **QUIC/HTTP3 MITM** | پشتیبانی از MITM روی QUIC با `quic-go` |
| **ECG (Encrypted ClientHello)** | پشتیبانی از ECH برای مخفی‌سازی SNI |
| **تأیید گواهی پیشرفته** | حالت‌های `allow_names` (لیست سفید)، Custom CA pinning |

### فایل‌های MITM

```
cert/
├── cert.go           # تولید CA، بارگذاری، خروجی PEM، بازتولید
├── installer.go      # نصب/حذف/بررسی CA در سیستمعامل
└── exec_windows.go   # اجرای فرمان در ویندوز (hidden/elevated)

proxy/
├── proxy.go          # هندلر MITM، تونل CONNECT، کانفیگ TLS
├── tls_fragment.go   # fragmentation برای دور زدن DPI
├── cert_verify.go    # تأیید گواهی پیشرفته
└── cf_pool.go        # مخزن IP های کلودفلر
```

---

## GSA Relay Engine

هسته GSA ترافیک را از طریق **زیرساخت Google** با تکنیک Domain Fronting رله می‌کند. از دید فیلترینگ، همه ترافیک به نظر `www.google.com` می‌رسد.

```
Browser
    │
    ▼
GSA Proxy (127.0.0.1:8085)
    │  ← TLS Termination (MITM cert)
    ▼
H2 Connection → Google IP (SNI: www.google.com)
    │  ← از دید DPI: ترافیک عادی گوگل
    ▼
Google Apps Script (script.google.com)
    │  ← رله JSON داخل زیرساخت گوگل
    ▼
Cloudflare Worker
    │  ← خروج با IP کلودفلر
    ▼
Site Target
```

### معماری GSA

```
gsaProxyServer.start()
    │
    ├── acceptLoop() → handleHTTP(conn)
    │       │
    │       ├── CONNECT → handleCONNECT()
    │       │       ├── gsaShouldDirectConnect() → relayRawTCP()
    │       │       └── TLS: mitm.getCert() → TLS Server → relayHTTPOverTLS()
    │       │
    │       ├── OPTIONS + access-control-request → CORS Preflight
    │       │
    │       └── GET/POST → relayRequest()
    │           