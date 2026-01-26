```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   ██████╗  ██████╗  ██████╗██╗  ██╗███████╗████████╗                 ║
║   ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝                 ║
║   ██████╔╝██║   ██║██║     █████╔╝ █████╗     ██║                    ║
║   ██╔═══╝ ██║   ██║██║     ██╔═██╗ ██╔══╝     ██║                    ║
║   ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗   ██║                    ║
║   ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝                    ║
║                                                                      ║
║    ███████╗███████╗██╗  ██╗    ████████╗███████╗██████╗ ███╗   ███╗  ║
║    ██╔════╝██╔════╝██║  ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║  ║
║    ███████╗███████╗███████║       ██║   █████╗  ██████╔╝██╔████╔██║  ║
║    ╚════██║╚════██║██╔══██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║  ║
║    ███████║███████║██║  ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║  ║
║    ╚══════╝╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

# PocketSSH

A portable SSH terminal client for the ESP32-S3 T-Deck Plus, featuring a hardware keyboard, trackball navigation, and touch gesture controls. Connect to remote servers, execute commands, and navigate your terminal with ease on this compact handheld device.

![PocketSSH Screenshot](misc/screenshot_01.jpeg)

## Version History

### v1.1.0 (January 14, 2026)
- **Fixed**: Boot loop issue on quick power cycles caused by GPIO4 (strapping pin) ADC initialization
  - Added 100ms delay before ADC initialization to allow GPIO4 to settle after boot
  - Prevents residual voltage from interfering with boot strapping sequence
  - Device now boots reliably regardless of power cycle timing
- **Added**: Touch-to-position cursor functionality
  - Tap anywhere on input text to move cursor to that position
  - Improves text editing experience with precise cursor control
- **Improved**: System stability on rapid power on/off cycles

### v1.0.0 (Initial Release)
- Full SSH2 terminal with PTY support
- Hardware keyboard and trackball navigation
- Touch gesture controls
- Battery voltage monitoring
- Command history with NVS storage

## Key Features

### SSH Terminal
- Full SSH2 protocol support with password authentication
- PTY terminal emulation (vt100) for proper shell interaction
- Real-time command execution and output display
- Handles large data transfers without freezing

### Hardware Controls
- **Physical Keyboard**: Full typing capability via C3 keyboard module
- **Trackball Navigation**: 
  - Up/Down: Navigate through command history
  - Click: Select/execute (when applicable)
- **Touch Screen Gestures**:
  - Swipe right-to-left: Show special keys panel
  - Swipe left-to-right: Hide special keys panel

### Special Keys Panel
Quick access to commonly used control sequences:
- **Ctrl+C**: Interrupt running process
- **Ctrl+Z**: Suspend process
- **Ctrl+D**: EOF signal / logout
- **Ctrl+L**: Clear screen
- **Tab**: Command completion
- **Esc**: Escape key
- **Exit SSH**: Close SSH session
- **Clear**: Clear terminal display

### Display Features
- 320x240 color LCD with LVGL graphics
- Real-time byte counter for data transfer monitoring
- Battery voltage indicator
- Connection status icons (WiFi, SSH)
- Non-blocking display updates prioritize rendering over input

## Hardware Requirements

- **ESP32-S3 T-Deck Plus**
  - ST7789 LCD Display (320x240)
  - GT911 Touch Controller
  - C3 Keyboard Module
  - Trackball (GPIO 1,2,3,15)
  - Battery monitoring (GPIO 4)

## Quick Start

### Prerequisites
- ESP-IDF v5.5.1
- ESP32-S3 T-Deck/T-Deck Plus

### First-Time Setup

1. **Connect to WiFi**:
   ```
   connect <SSID> <PASSWORD>
   ```
   Example: `connect MyNetwork MyPassword123`

2. **Connect to SSH Server**:
   ```
   ssh <HOST> <PORT> <USER> <PASSWORD>
   ```
   Example: `ssh 192.168.1.100 22 pi raspberry`

3. **Use Interactive Shell**:
   Once connected, any command you type is sent to the remote server:
   ```
   ls -la
   cd /home
   top
   vim myfile.txt
   ```

4. **Disconnect**:
   - Type `disconnect` command, or
   - Use Disconnect button in special keys panel

### Available Local Commands

These commands are executed locally on the device (not sent to SSH):
- `help` - Display available commands and usage
- `clear` - Clear the terminal display
- `disconnect` - Close WiFi connection
- `exit` - Close SSH connection
- `connect <SSID> <PASS>` - Connect to WiFi network
- `ssh <HOST> <PORT> <USER> <PASS>` - Establish SSH connection

## Architecture

### Framework & Libraries
- **ESP-IDF**: v5.5.1 - Official Espressif IoT Development Framework
- **LVGL**: v9.x - Graphics library with thread-safe display locking (`bsp_display_lock/unlock`)
- **libssh2**: SSH2 protocol implementation (see d