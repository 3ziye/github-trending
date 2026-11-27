<p align="center"><img src="assets/logo.svg" alt="WinRust" width="140"></p>

<h1 align="center">WinRust</h1>

<p align="center"><b>Your Windows, minus the bloat.</b><br>The taskbar, File Explorer, file search and Task Manager rebuilt in Rust: native, tiny and fast.</p>

<p align="center">
  <a href="https://github.com/Lemxy/WinRust/releases/latest"><b>⬇ Download WinRust.exe</b></a> ·
  <a href="#install">Install</a> ·
  <a href="#what-gets-installed">What's inside</a> ·
  <a href="#community">Community</a>
</p>

<p align="center">English | <a href="README.ru.md">Русский</a> | <a href="README.ja.md">日本語</a> | <a href="README.pt-BR.md">Português (Brasil)</a> | <a href="README.zh.md">简体中文</a></p>

![The WinRust bar with its settings menu, Ruby theme](docs/screenshots/taskbar.webp)

> **Read this first.** WinRust turns off Windows Search, hides the taskbar and can turn off Explorer as the shell. The exe is not code-signed, so SmartScreen will warn you. A restore point is created before install, but try it on a spare machine or a VM first.

## Why WinRust

- **Fast.** A folder window opens in 60 ms instead of 420 ms, a search over the whole C: drive takes 45 ms ([measurements](#benchmark)).
- **Light.** The whole shell takes 46 MB of memory, explorer.exe took 366 MB.
- **Native.** Small Win32 programs: no .NET, no Electron.
- **Reversible.** Every value is saved before it is changed and put back on uninstall. One button removes everything.
- **Yours.** Eight styles (Ruby, Terminal, Floating dock, Windows 98 and more), any colour, the bar on any edge, English, Русский, 日本語 or Português.

## See it

| Run (Win+R) | File manager |
|---|---|
| ![Run box with recent commands](docs/screenshots/run.webp) | ![rust-explorer, Ruby theme](docs/screenshots/explorer.webp) |

**Task Manager** (Russian UI)

![Task Manager](docs/screenshots/task-manager.webp)

## Install

1. Download `WinRust.exe` from the [latest release](https://github.com/Lemxy/WinRust/releases/latest) (Windows 10/11, x64).
2. Run it as administrator.
3. Pick **Express (recommended)** and press **Install**: search, Task Manager, the bar, Settings, disk analysis and the photo viewer, nothing removed and Explorer left in place. Or pick **Custom (advanced)** to tick the components yourself, including `rust-explorer` (replaces the Windows Explorer shell; also the **Replace Explorer** switch behind the gear on the topbar row) and the extras. They are installed in the right order; one that fails or is skipped does not stop the others, and the last page lists each component with its result.

Windows Search is optional: on a stripped Windows (for example a debloated LTSC image without the Windows Search service) that step is skipped with a warning instead of failing the install.

If UAC asks for **another administrator's** password, the per-user settings (startup entries, scheduled tasks, PowerShell profile, search permissions) still go to the user who is signed in, not to the administrator you typed. If the installer cannot tell who that is, it stops before changing anything.

**Automatic updates:** after the first install, a `WinRust-update` scheduled task (runs as SYSTEM, no UAC prompt) checks the latest release at boot and once a day. It downloads the new `WinRust.exe` (and any program a release ships on its own), checks each file against a manifest signed with the project's key (a tampered or unsigned release is refused); the new `WinRust.exe` then replaces the installed programs that differ from the ones it carries. Only files that are already installed are replaced. A running program switches to the new version the next time it starts (sign-in or reboot). Log: `%ProgramData%\plugin-launcher\install.log` (`autoupdate:` lines). To turn it off, disable the `WinRust-update` task in Task Scheduler; **Remove WinRust** deletes it.

**Manual update:** download the new `WinRust.exe` from the releases page, run it as administrator and press **Update** on the Express card (it reinstalls what is installed and adds what is missing), or use Custom. An existing `rust-explorer` stays ticked. Your settings and the saved original Windows values stay.

The installer is in English. Its corner holds a language drop-down — English, Русский, 日本語, Português (Brasil), 简体中文; the same list sits behind the gear on the bar (**Bar settings → Language**), and rust-settings has it on its Personalization page (**Interface language**). The choice is stored in `%ProgramData%\WinRust\lang.txt` (`en`, `ru`, `ja`, `pt`, `zh`); the program you switch in repaints at once, the other programs read it when they start, so restart them (or sign out) after a change.

## Remove

- **Remove WinRust** on the installer's first page undoes everything: Windows Search, the taskbar, Explorer and the services come back.
- Without the installer (for example, antivirus deleted it): **Settings → Apps → Installed apps → WinRust → Uninstall** does the same as Remove WinRust.
- One plugin at a time: `plugin-launcher un