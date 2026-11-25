<p align="center">
  <img src="docs/readme/banner.png" alt="ASoftware iOS for Android: iOS 26 running in the app on a Galaxy S25 Ultra, with watchOS on a watch beside it" width="100%">
</p>

<p align="center">
  <a href="https://github.com/alpersamur3/asoft-ios-android/releases/latest"><b>Download the app</b></a>
  &nbsp;·&nbsp; <a href="DEVICES.md">Tested phones</a>
  &nbsp;·&nbsp; <a href="#if-something-goes-wrong">If something goes wrong</a>
  &nbsp;·&nbsp; <a href="https://github.com/alpersamur3/asoft-ios">Windows version</a>
</p>

Real iOS in an Android app. iOS 16 runs on most 64-bit phones; iOS 26 and watchOS run on phones whose
GPU passes the app's check, which today means most Snapdragon phones (Adreno). A normal phone is
enough: no root, no unlocked bootloader, no Termux and no PC. The app downloads iOS from Apple's own
servers and builds it on the phone.

It is a research preview: slow next to a real iPhone, a setup takes hours, and some phones hit
problems that are not solved yet (listed below). The app and this repository contain no Apple files.

## Will it run on my phone?

| | What the phone needs | Free space while it installs | Space it keeps |
|---|---|---|---|
| **iOS 16** | 64-bit Android 10 or newer. No GPU needed. 6 GB of RAM or more is comfortable; 4 GB phones run it, slowly. | about 26.5 GB | about 6.5 GB, and about 4 GB for its save |
| **iOS 26** | the same, plus a GPU that passes the app's GPU check, and 7 GB of RAM or more (12 GB is comfortable) | about 46 GB | about 12 GB |
| **watchOS** | the same GPU check as iOS 26, and 5 GB of RAM or more | about 20 GB | about 4 GB |

- The GPU check runs before anything is downloaded and takes about 10 seconds. It says plainly whether
  iOS 26 and watchOS will run on your phone, will never run on it, or are not supported on it yet.
- Adreno GPUs (Snapdragon) run through the Turnip driver that comes with the app. Some of them (for
  example the Adreno 750 and the 6xx series) run in a compatibility mode that can stop after long use;
  the app saves before that when it can.
- Mali (most Exynos, MediaTek and Tensor phones), Xclipse and PowerVR GPUs do not run iOS 26 or
  watchOS yet. iOS 16 runs on them, because it draws on the CPU.
- Newer CPUs are much faster. iOS's code runs natively only on cores with the ARMv8.2 features listed
  further down (most phones from 2019 on); on older cores (Cortex-A73, A53) everything is emulated and
  several times slower.
- [DEVICES.md](DEVICES.md) lists the phones people have run it on, with the speed they saw. After iOS
  has run for ten minutes on a phone that is not on the list, the app offers to add it.

## Install

1. Download `ASoftware-iOS-Android-<version>.apk` (about 110 MB) from
   [Releases](https://github.com/alpersamur3/asoft-ios-android/releases/latest) and install it. Android
   asks once to allow installs from your browser or file manager.
2. Open the app, tap **Set up**, and start iOS 16, iOS 26 or watchOS.
3. Leave the phone on its charger and on Wi-Fi, with the app open. If it waits for you, tap **Resume**:
   what is done stays done.
4. When it is done, tap the system on the home screen to start it.

How long it takes depends on the phone. On a Galaxy S25 Ultra, iOS 16 takes about 1.5 hours from
Apple, watchOS about an hour and iOS 26 a few hours. On reporters' phones iOS 16 alone has taken
from about an hour to more than 16 hours.

## While it installs

These are the things that stop most setups, from the reports we get:

- **Android closes the app.** Some phones (Xiaomi, OPPO, realme, vivo, Tecno, Samsung's sleeping
  apps) end long-running apps. Lock ASoftware in the recent apps (hold its card, tap the lock), set
  its battery use to *No restrictions*, and do not press *Clear all*. When Android closes it for low
  memory, the next try of that step uses less memory.
- **Not enough room.** The numbers in the table are what the build needs at its biggest moment. The
  app checks before each step and says how much is missing.
- **The battery.** Below 15 % and not on the charger, the setup waits for the charger.
- **Heat.** When Android reports the phone's heat as *severe* or worse, the setup pauses until Android
  says it has cooled down. Some phones report *severe* while only warm on the charger.
- **iOS 26's second boot.** The last big step, *Second boot: DataMigration*, is iOS setting itself
  up. It takes about an hour on a fast phone and longer on others. The bar stops at 85 % after an hour;
  the minutes in the text are the real progress. On some phones it never finishes: that is
  [#16](https://github.com/alpersamur3/asoft-ios-android/issues/16), still open.

## Using it

- A side bar on the right edge has Home, the side button, a touch lock, screen pinning and saves.
  Tap its handle to show or hide it, drag it to move it. A long press on a button says what it does.
- The phone's volume keys are iOS's, Android's back gesture is iOS's edge swipe, and turning the
  phone's screen off