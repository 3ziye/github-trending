# UnknownAuto

[![Download APK](https://img.shields.io/github/v/release/GitMag/UnknownAuto?label=download%20APK&logo=android&color=success)](https://github.com/GitMag/UnknownAuto/releases/latest)
[![Support on Ko-fi](https://img.shields.io/badge/support-Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/forsblomdev)

An open, offline tool that lets a **self‑built or sideloaded Android Auto app** actually
run in the car. It installs an APK the way Android Auto requires — as if it came from
Google Play — **entirely on the phone, no computer** (Android 11+). No internet, no account,
no payment, no analytics. A free, open alternative to the proprietary *AA Enabler*.

<p align="center"><img src="docs/screenshot.png" alt="UnknownAuto" width="300"></p>

## Why it's needed

Android Auto won't run an app built with its Car App Library unless Android thinks the app
was **installed from Google Play**. The developer "Unknown sources" switch doesn't change
that. A normal sideload — `adb install`, a file manager, or Shizuku — is recorded as *not*
from Play, so Android Auto quietly refuses the app. UnknownAuto fixes that record so the
car accepts it.

## How it works

Android remembers who installed each app, and that "installed from Google Play" mark can
only be set **when the app is installed** — you can't change it afterwards, and a plain
sideload can't set it at all.

UnknownAuto uses **Shizuku** — which runs with the phone's "shell" privileges, the same
ones a connected computer's `adb` has — to drive Android's own package installer and mark
the install as coming from Google Play. The car then treats it as a real Play install. It's
the same trick the proprietary AA Enabler uses, done openly and for free.

Some Android 17 builds do it the other way round: they keep the mark only when UnknownAuto
starts the installer itself. When an install comes out without the mark, UnknownAuto tries
once more the other way (one more tap on **Update**) and remembers which way works on that
phone. Start Shizuku so both ways are available.

Android 14 and older also check the app that asked for the install, and refuse the shell
itself. There Shizuku starts the installer on UnknownAuto's behalf, so UnknownAuto needs the
**install unknown apps** permission for this too.

If the install doesn't go through at all, for example a newer version or one signed with
another key is already installed, UnknownAuto says so, and **Show details** includes the
installer's own log lines, which is the most useful thing to paste into an issue.

## Install UnknownAuto

Grab **UnknownAuto‑1.3.apk** from the [latest release](https://github.com/GitMag/UnknownAuto/releases/latest)
and open it on the phone — or build it yourself with plain Android SDK tools, no Gradle:

```
./build.sh            # build unknownauto.apk
./build.sh install    # build, then install and open it
```

On first use, allow it to **install unknown apps** (it opens that settings screen for you).

## Set up Shizuku (once)

UnknownAuto needs [Shizuku](https://shizuku.rikka.app/) running. Shizuku gets the same
access a computer gets through USB debugging, but on Android 11+ the phone gives it that
access itself, over **Wireless debugging**. So when Shizuku asks you to pair, you pair the
phone **with itself**: there is no computer or second device involved.

Wireless debugging only works while the phone is **connected to Wi‑Fi** (any network; it
doesn't use the internet).

1. **Install Shizuku.** Tap **Install Shizuku** in UnknownAuto (it downloads the official
   app), or get Shizuku from Google Play.
2. **Turn on Developer options.** Settings → About phone → tap **Build number** seven times.
   (Samsung: About phone → Software information → Build number. Xiaomi: About phone → OS
   version or MIUI version.)
3. **Start pairing in Shizuku.** Open Shizuku and, under *Start via Wireless debugging*,
   tap **Pairing**. Allow notifications if it asks: you'll type the pairing code into a
   Shizuku notification. The notification says *Searching for pairing service*.
4. **Get a pairing code.** Open Developer options → **Wireless debugging** (usually Settings
   → System → Developer options; or search Settings for "Wireless debugging"). Turn on
   **Use wireless debugging** and allow it on this network, then tap **Pair device with
   pairing code**. A six‑digit code appears. **Leave this dialog open.**
5. **Type the code into the notification.** Pull down the notifications: Shizuku's
   notification now says *Pairing service found*. Tap **Enter pairing code**, type the six
   digits and send. It changes to **Pairing successful**.
6. **Start Shizuku.** Go back to Shizuku and tap **Start** (the button next to Pairing). A
   black screen with text opens for a moment and closes by itself; that's normal. Shizuku's
   main screen now says **Shizuku is running**.

The first time you tap **Install** in UnknownAuto, Shizuku asks whether to allow
UnknownAuto: choose **Allow all the time**.

**After