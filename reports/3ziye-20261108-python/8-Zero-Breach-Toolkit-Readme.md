# Zero Breach Toolkit

> **Version 2 is out:** now a double-click app for Windows, Mac and Linux, in 27 languages.
> [Download it from the latest release](https://github.com/interplains/Zero-Breach-Toolkit/releases/latest).

A free, open-source check for traces of known mercenary spyware (Pegasus, Predator,
Graphite, Candiru and others) on computers, Android phones and iPhone backups.

- **Read-only.** It does not modify source evidence or system settings. It writes only
  temporary database snapshots and the reports you ask for.
- **No network requests during a scan.** It never looks up spyware addresses and has no
  upload feature. Python network calls are blocked and redirected paths are refused. This
  is not an operating-system network sandbox; see [PRIVACY.md](PRIVACY.md).
- **States its limits.** Every report says what was found, how strong the evidence is, and
  what could not be checked. A clean result is never presented as proof that you are safe.

Made by archivegenocide. Built on [Zero Breach](https://github.com/interplains/zero-breach).

> **If you think you are being targeted right now, get expert help first.** You do not
> need to run this tool before asking. Journalists, activists, human-rights defenders and
> civil society can contact the
> [Access Now Digital Security Helpline](https://www.accessnow.org/help/) (free, 24/7,
> many languages) or [Amnesty International's Security Lab](https://securitylab.amnesty.org/get-help/).

---

## Easiest: download the program (no Python, no commands)

**You do not need to know anything technical to use this.** Download one file from the
[latest release](https://github.com/interplains/Zero-Breach-Toolkit/releases/latest), open it,
and follow the window. You do not need the source code on this page, and you do not need to
type any commands.

Once it is open: choose a check, press **Start check**, and read the result. It tells you in
plain words whether anything was found and what to do next. You can save the report if you
want to keep it or show it to someone helping you.

**Which check?** Use **Standard** unless you have a reason not to: it covers browsers, apps,
startup items, program files and out-of-date programs (usually 15 to 20 minutes). **Quick** looks
at browsers only (5 to 10 minutes). **Full** adds web caches and more file types (30 minutes or
more). You can press **Stop** at any time and keep what has been checked so far. To check a
phone, choose **A phone** in the window; the guides there explain what you need first.

**A green result is good news, not a guarantee.** It means this check found none of the published
traces it looks for, in the places it could read. It cannot find spyware nobody has published
traces of, and it does not prove a device is safe. If you think you are being targeted, ask a
digital-security helpline even if the result is green.

**Your antivirus may flag these programs.** Antivirus products often wrongly flag new programs that are not code-signed yet, and some flag these. If you downloaded the file from [the official release page](https://github.com/interplains/Zero-Breach-Toolkit/releases/latest), this is a false alarm and you can ignore it: the code is public, and each program has a public build record you can check. We have applied for free code signing and will report these false alarms to the antivirus companies. **If the file came from anywhere else, do not run it and trust the warning.**

### Windows

1. Download `zero-breach-toolkit-windows-x64.exe`.
2. Double-click it in your Downloads folder.
3. Windows may say it "protected your PC". Click **More info**, then **Run anyway**.

### Mac

1. Download `zero-breach-toolkit-macos-apple-silicon.dmg` for a newer Mac (M1, M2, M3, M4),
   or `zero-breach-toolkit-macos-intel.dmg` for an older Intel Mac. The Apple menu →
   **About This Mac** says which one you have.
2. Open it, drag **Zero Breach Toolkit** into Applications, then open it from Applications.
3. macOS will refuse the first time. Open **System Settings → Privacy & Security**, scroll
   down, click **Open Anyway**, then open the app again.

Open the app on the Mac itself, not through a remote or SSH session: it needs a desktop.

### Linux

1. Download `zero-breach-toolkit-linux-x64.tar.gz`.
2. Extract it (double-click it, or `tar -xzf zero-breach-toolkit-linux-x64.tar.gz`).
3. Run `./zero-breach-toolkit`, or right-click it and choose **Run in Terminal**.

The warnings appear because the programs are not signed by Microsoft or Apple yet. Each
program is built by GitHub from the published source, and you can check that before running it:
`gh attestation verify <file> --repo interplains/Zero-Breach-Toolkit` (see
[docs/VERIFYING.md](docs/VERIFYING.md)). Prefer to see exactly what runs? Use the Python
version in the guide below; it is the same check.

To let the check read Safari on a Mac, give **Zero Breach Toolkit** (or Terminal, for the Python
version) **Full Disk Access** in System Settings → Privacy & Secu