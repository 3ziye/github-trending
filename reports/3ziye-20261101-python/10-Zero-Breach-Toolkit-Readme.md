# Zero Breach Toolkit

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

## Step-by-step guide (no technical experience needed)

You do not need a GitHub account or any technical knowledge. You need a Windows or Mac
computer and about 20 minutes. Phones are checked by connecting them to the computer.

**What do you want to check?**
[This Windows computer](#windows) ·
[This Mac](#mac) ·
[An Android phone](#android-phone) ·
[An iPhone](#iphone)

### Windows

**Set up (only the first time)**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the yellow
   **Download Python** button. Open the downloaded file.
2. On the first screen of the installer, **tick "Add python.exe to PATH"** at the bottom,
   then click **Install Now**. Wait until it says "Setup was successful".
3. On this page, click the green **Code** button near the top, then **Download ZIP**.
4. Open your **Downloads** folder, right-click **Zero-Breach-Toolkit-main.zip** and choose
   **Extract All**, then **Extract**.

**Run the check**

5. Close your web browsers and chat apps (Chrome, Edge, WhatsApp, Signal…).
6. Open the **Zero-Breach-Toolkit-main** folder (if there is another folder with the same name
   inside, open that one too), then the **scan** folder, and double-click **run-scan.cmd**.
   If Windows shows a warning, click **Run** (or **More info**, then **Run anyway**).
7. A menu appears. Type the number next to **Update the indicator lists** and press Enter,
   then type `y` and press Enter. When it finishes, press Enter.
8. Press Enter again to start **This computer - standard check**. It takes about 15 minutes.
9. Read the result at the end (see [What the result means](#what-the-result-means)). A copy
   is saved in the **findings** folder inside Zero-Breach-Toolkit-main.

### Mac

**Set up (only the first time)**

1. Go to [python.org/downloads](https://www.python.org/downloads/), click **Download Python**,
   open the downloaded file and follow the installer. When it finishes, open **Finder →
   Applications → Python 3** and double-click **Install Certificates.command** (without it,
   updating the indicator lists fails).
2. On this page, click the green **Code** button, then **Download ZIP**. It appears in your
   **Downloads** folder as **Zero-Breach-Toolkit-main** (if it is still a .zip file,
   double-click it).
3. Open **System Settings → Privacy & Security → Full Disk Access**, click **+**, choose
   **Applications → Utilities → Terminal**, and turn it on. Without this, macOS hides
   Safari's records from the check.

**Run the check**

4. Close your web browsers and chat apps.
5. Open **Terminal** (press Cmd+Space, type `Terminal`, press Enter). Copy this line, paste it
   into Terminal and press Enter:
   ```
   cd ~/Downloads/Zero-Breach-Toolkit-main && python3 -X utf8 scan/zero-breach-toolkit.py
   ```
6. A menu appears. Type the number next to **Update the indicator lists** and press Enter,
   then type `y` and press Enter. When it finishes, press Enter.
7. Press Enter again to start **This computer - standard check**. It takes about 15 minutes.
8. To keep a copy of the result, type `3` and press Enter, then type `.` (a full stop) and
   press Enter. It is saved in the Zero-Breach-Toolkit-main folder with the date and time in
   its name, so every check gets its own file. Type `0` to finish.

### Linux

**Set up (only the first time)**

1. Open a terminal (on most desktops, press Ctrl+Alt+T). Python 3 is usually already
   installed; check with `python3 --version`. If it is missing, install it with your
   package manager, for example `sudo dnf install python3` (Fedora),
   `sudo apt install python3` (Ubuntu, Debian, Mint) or `sudo pacman -S python` (Arch).
2. On this page, click the green **Code** button, then **Download