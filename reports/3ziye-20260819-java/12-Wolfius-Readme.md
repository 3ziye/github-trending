# Wolfius
**English** / [русский](README.ru.md) / [简体中文](README.zh.md)

Wolfius is a local TLS proxy for **Android 1.5+** that transparently upgrades TLS 1.0 connections to modern TLS 1.3. This restores access to the modern Internet on old Android devices.
* **Telegram channel for updates**: [@AppDataApps](https://t.me/AppDataApps)
* Join our **[Retro Android Group](https://t.me/retroandroidgroup)** on Telegram!
* Discord server: [Android Afterlife](https://discord.gg/2JqfEkQyck)

Wolfius utilizes the wolfSSL library to provide TLS 1.3 access system-wide across all applications, which resolves issues with modern certificates.

<img src="img/logo.png" alt="Modern SSL certificates for legacy Android" width="301"/>

<img src="img/scr1.png" alt="Screenshot" width="200"/> <img src="img/scr2.png" alt="Screenshot" width="200"/> <img src="img/scr3.png" alt="Screenshot" width="200"/> <img src="img/scr4.png" alt="Screenshot" width="200"/> <img src="img/scr5.png" alt="Screenshot" width="200"/>

> [!WARNING]  
> This project is at an early stage of development and may run slowly or be unstable. Please report any issues, attaching a full logcat report.

> [!IMPORTANT]  
> To set up the CA correctly and ensure that the TLS proxy operates system-wide, it is recommended that you obtain root privileges. However, this is not a prerequisite: even without root privileges, you will still be able to use TLS 1.3 in browsers.

> [!NOTE]  
> This project is intended for use with Android 1.5–4.4 only.

## 📥 Download
* [GitHub Releases](https://github.com/gohoski/Wolfius/releases)
* [4PDA](https://4pda.to/forum/index.php?showtopic=1124459)
* [MyIntCountry](http://myintcountry.ru/index.php?board=android&action=display&num=2350)
* [Oldpods](http://2012rs.oldpods.cn/app.php?id=1575)
* Telegram (link at the top of the README)

Simply install the APK and follow the on-screen instructions.

## Root CA installation
Sometimes, simply installing the root CA in the system is not enough—for example, the Opera browser has its own store of trusted certificates. In such applications, follow this link to install the root certificate authority: http://144.31.189.129/ca_cert.der

## Why and how
Today, the vast majority of modern websites enforce a minimum of TLS 1.2 or 1.3. This completely locks legacy Android devices out of the modern web, as early versions are natively restricted to TLS 1.0. 
While TLS 1.2 support technically exists in Android 4.1–4.3, it is explicitly dependent on Google Mobile Services (GMS). For old resource-constrained CPUs, running GMS background services introduces massive proprietary bloatware that makes the device painfully slow. Native, unmanaged TLS 1.2 support was only fully integrated into AOSP with the release of Android 5.0 Lollipop.

This gives an idea of inserting TLS 1.2 into old Android versions. However, solving this isn't as simple as swapping out the system's old OpenSSL library. Android enforces strict system library checks, and even if you bypass them, standard apps wouldn't automatically know how to use the updated library. The alternative would mean manually patching every single application for forcing the usage of TLS 1.2—an impossible task, especially since many apps bundle their own TLS libraries or reject custom certificate authorities. Modifying core system files like `core.jar` and `framework.jar` is equally problematic; these files vary wildly by device, meaning a system patch for one phone would completely break another. Ultimately, this will cause a lot of incompatibility.

However, this project does not do any of that. Wolfius avoids all of this friction by acting as a local, system-wide TLS 1.0 man-in-the-middle (MITM) proxy right on the device. When an app attempts to connect to a modern website, Wolfius intercepts the traffic locally. It then establishes a brand-new, secure TLS 1.3 connection to the remote server, fetches the data, and hands it back to the app over TLS 1.0 using a locally trusted root certificate. To the old app, the connection looks perfectly normal; to the modern web, the device looks like a secure, modern client. This achieves seamless, system-wide compatibility without modifying a single line of application or system code.
### Why Android 1.5? Why TLS 1.3?
This architecture is made possible by the wolfSSL library, which is highly optimized for embedded systems and environments that lack a modern C library. Because of its lightweight design, it compiles cleanly for Android 1.5 without hitting NDK compatibility roadblocks. Additionally, for some websites TLS 1.2 is not enough anymore; by leveraging wolfSSL, Wolfius completely skips the aging TLS 1.2 standard and jumps straight to full TLS 1.3 support, bringing modern cryptographic performance to hardware built long before these security standards were even conceived.
### Why so many connection methods?
Prior to version 4.2, Android didn't provide a proper interface to proxy traffic. Depending on the device, either iptables r