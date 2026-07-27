# ChimeraBLE

A multi-headed BLE security & reverse-engineering tool for the ESP32 - named for
the chimera because it's one beast made of many parts, and because it speaks BLE
in all three roles: **Host** (central - scan, connect, enumerate, decode),
**Peripheral** (clone/emulate a device), and **MITM** (both at once - proxy
between a real device and its host). Enumerate a full GATT tree, read/write/
subscribe to characteristics, decode advertising data, parse HID report maps,
clone a device, direction-find it, or sit in the middle and log the traffic -
from a serial command line or the on-device Cardputer UI.

Built on [NimBLE-Arduino](https://github.com/h2zero/NimBLE-Arduino) 2.x.

> ⚠️ **Responsible use.** ChimeraBLE is a dual-use security research tool: it can
> impersonate/clone devices, man-in-the-middle connections, run a honeypot, and
> sniff HID/notification traffic. Use it **only** on devices you own or are
> explicitly authorized to test. You are responsible for complying with all
> applicable laws. Provided with **no warranty** (see LICENSE).

### Supported boards

| Env | Board | MCU | Front-end |
|---|---|---|---|
| `esp32dev` | ESP32 WROOM | classic Xtensa dual-core | serial CLI |
| `xiao_esp32c5` | Seeed Studio XIAO ESP32-C5 | RISC-V single-core | serial CLI |
| `cardputer` | M5Stack Cardputer ADV | ESP32-S3 (Stamp-S3A) | on-device M5 UI |

All targets use the [pioarduino](https://github.com/pioarduino/platform-espressif32)
platform (Arduino-ESP32 3.x / ESP-IDF 5.5) and **share the same BLE engine**
(`scanner`, `connection`, `gatt`, `adv_parser`, `uuid_db`, `hid_parser`, `oui_db`,
`fingerprint`, `clone`). `build_src_filter` swaps only the front-end: the serial
targets use `main.cpp` + `cli.cpp`; the Cardputer uses [`src/ui/`](src/ui/) (an
M5 menu UI in `App`/`UI`) and runs the engine natively on its own S3 radio - no
companion device. The XIAO ESP32-C5 board def lives in
[`boards/seeed_xiao_esp32c5.json`](boards/seeed_xiao_esp32c5.json).

---

## Build & flash

```sh
cd ChimeraBLE

# build both targets
pio run

# pick a target
pio run -e esp32dev
pio run -e xiao_esp32c5

# flash + monitor a specific target
pio run -e xiao_esp32c5 -t upload
pio device monitor -e xiao_esp32c5    # serial console @ 115200

# one-time: flash the OUI vendor database to the device filesystem (LittleFS).
# Needed for OUI-based vendor identification; also (re)formats LittleFS, so do
# this BEFORE saving clone profiles you want to keep.
pio run -e xiao_esp32c5 -t uploadfs
```

After flashing, open the monitor. You'll get a `ble>` prompt (it changes to
`ble-connected>` while a device is connected). Type `help` for the command list,
or just start with `scan`.

### Cardputer ADV (on-device UI)

```sh
pio run -e cardputer -t upload      # flash firmware
pio run -e cardputer -t uploadfs    # one-time: OUI DB onto LittleFS
```

No serial console needed - the UI is on the screen. Keyboard navigation:

| Key | Action |
|---|---|
| `;` / `.` | move selection up / down (scroll in Logs) |
| `/` or Enter | open / activate |
| `,` or Del | back (stops a fox hunt) |
| `'` | command mode - type any CLI command (e.g. `secure mitm iocap=display_yesno`, `clone save x`) and Enter |

Screens: **Main** → Scan / Devices / GATT / Command / Logs. **Devices** lists
scan results (RSSI + name or `~fingerprint`); select one for **Device Detail**
(Connect+dump, or Foxhunt). **Foxhunt** shows a live signal bar. Anything the
serial CLI can do is reachable from command mode, since both share the same
dispatch (`cli::execute`).

---

## Quick start

```
ble> scan 10                 # scan 10 seconds
ble> list                    # see what was found
ble> info 3                  # inspect device #3's advertising data
ble> connect 3               # connect to it
ble> secure                  # encrypt/bond (needed for many characteristics)
ble> dump                    # enumerate everything + auto-parse HID if present
ble> sub 0x002d              # subscribe to a notify characteristic
   ... press buttons / trigger the device, watch notifications stream ...
ble> disconnect
```

---

## Command reference

### Scanning & discovery

| Command | What it does |
|---|---|
| `scan [secs]` | Active scan for nearby devices (default 10s). Results are deduped by MAC. |
| `stop` | Stop an in-progress scan early. |
| `list` | Show the last scan's results, **sorted by signal strength (strongest/nearest first)** with indices renumbered 0..N to match: index, MAC, RSSI, adv byte count, and **name + fingerprint guess**. No-name devices show `~guess` (e.g. `~Apple (Nearby)`, `~BTHome sensor`). Named devices show `name \| guess` when the guess adds something (e.g. `Vertuo_DV6_… \| company 0x…`), since many self-reported names are cryptic. RPA/random addresses are tagged `[RPA]`/`[rand]`. |
| `info <idx>` | Full advertising payload for a device, hex + decoded AD records (flags, UUID lists, name, Tx power, appearance, service data, manufacturer data with Apple/Microsoft/Goog