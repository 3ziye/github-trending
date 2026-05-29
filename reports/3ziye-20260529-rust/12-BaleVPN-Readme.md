# Bale VPN

> 🟢 **Simplest start — two Android phones.** A peer-to-peer VPN over Bale messenger: one phone shares its working internet with the other, with no third-party server, no signup, and no command line. Install the APK on both, sign in with your Bale account in the app, flip one to **Server** and the other to **Client**.
>
> **→ [Android setup guide](docs/android-en.md)**

A peer-to-peer VPN that tunnels IP traffic over the voice-call infrastructure of [**Bale**](https://bale.ai/), the national Iranian messaging app. One device runs as the *server* (provides internet); another as the *client* (consumes it). To Bale's servers the link looks like a long voice call between two contacts.

The point: when one person has a working / uncensored connection and the other doesn't, the second person can route their traffic through the first — without any extra server, account, payment, or signup. Just install the app on two phones (or a laptop on the server side), make sure the two accounts have each other in their contact list, and connect.

There is no commercial relationship with Bale.

<div dir="rtl">

## دربارهٔ پروژه

> 🟢 **ساده‌ترین شروع — دو گوشی اندرویدی.** یک VPN نقطه‌به‌نقطه روی پیام‌رسان بله: یک گوشی، اینترنت سالمش را با گوشی دیگر به اشتراک می‌گذارد؛ بدون سرور خارجی، بدون ثبت‌نام، بدون خط فرمان. APK را روی هر دو نصب کنید، با حساب بلهٔ خودتان در اپ وارد شوید، یکی را روی **سرور** و دیگری را روی **کلاینت** بگذارید.
>
> **← [راهنمای نصب اندروید](docs/android-fa.md)**

این پروژه یک VPN نقطه‌به‌نقطه است که ترافیک IP را روی زیرساخت تماس صوتی [**بله**](https://bale.ai/)، پیام‌رسان ملی ایران، عبور می‌دهد. یک دستگاه نقش *سرور* را دارد (اینترنت می‌دهد) و دستگاه دیگر نقش *کلاینت* را (اینترنت می‌گیرد). برای سرورهای بله این ارتباط شبیه یک تماس صوتی طولانی بین دو مخاطب به نظر می‌رسد.

هدف: وقتی یک نفر اینترنت سالم دارد و نفر دیگر نه، نفر دوم بدون هیچ سرور یا اشتراک اضافه‌ای می‌تواند ترافیکش را از طریق نفر اول رد کند. فقط کافی است هر دو طرف، هم در بله ثبت‌نام کرده باشند و هم یکدیگر را در فهرست مخاطبین داشته باشند.

این پروژه هیچ ارتباط تجاری‌ای با بله ندارد.

</div>

---

## ⚠️ Privacy & encryption

The LiveKit data channel is encrypted with **DTLS**, so traffic is opaque to passive observers on the network and to ISP middleboxes. **However, Bale's LiveKit server is the SFU/TURN node and has access to the plaintext of the data flowing through the call.** That means:

- Bale can see **who relays for whom** — every tunnel session is a Bale voice call between two accounts, so Bale's call records reveal the social graph (which account uses which relay, when, for how long).
- Bale can see **which destinations you connect to** (IP and port, plus the hostname embedded in the TLS SNI of any HTTPS request).
- Bale can read the **contents of any traffic that isn't itself end-to-end encrypted**. If you only browse `https://` sites, the payload is opaque to them; if you access plaintext HTTP / DNS / FTP / etc. through the tunnel, they can read it.

**SOCKS5 mode (QUIC) note.** When you use SOCKS5 instead of full VPN, the tunnel carries client↔server traffic inside a QUIC channel that adds its own TLS-1.3 encryption on top of the LK data channel. **This is end-to-end encrypted between the two BaleVPN peers** and would in principle shield the contents from Bale's SFU. **But there is no certificate authority** — both ends generate self-signed certificates at startup and accept whatever the peer presents. Anyone who can inject themselves into the QUIC handshake path (which includes whoever operates the SFU you're routing through — Bale) can perform a transparent MITM by handing each side their own cert. The QUIC layer protects against passive eavesdropping by other tenants on the SFU; it does **not** protect against an active adversary at the relay. Treat the threat model as identical to the VPN-mode case above: rely on app-level TLS (HTTPS, etc.) for actual confidentiality, not on the QUIC layer.

Treat this tunnel like a corporate VPN whose operator you don't fully trust — fine for IP-level reachability (uncensoring), **not adequate as an anonymity or end-to-end privacy layer**. Use TLS at the application level (HTTPS, encrypted DNS, etc.).

### 📌 Recommendation from the author

Register the Bale account used with this tool on a **virtual phone number** rather than your primary one, so the call metadata above can't be tied back to your real identity.

**Bale accepts non-Iranian numbers** — and for those, **Bale's verification code is delivered through Telegram**, not by SMS. (Iranian SMS gateways often can't reliably deliver to international numbers, so Bale uses Telegram as the OTP channel for them.) Step-by-step:

1. Get a virtual phone number that can receive SMS. [Sonetel](https://app.sonetel.com/) works well; other reliable options include [JMP.chat](https://jmp.chat/) (with XMPP), [MySudo](https://mysudo.com/), [Hushed](https://hushed.com/), or [Twilio](https://www.twilio.com/) if you're comfortable with their dashboard. 