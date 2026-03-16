```
              _                                                   _
         .k$$$$$g,                                           ,g$$$$$k.
      .k$$$$$$$$$$$a.                                     .a$$$$$$$$$$$k.
    .J$$$$$?'   `?$?^?,                                 ,?^?$?`   `?$$$$$L.
   JS$$SI!a,  _.JS$   ?,                               ,?   $SL._  ,a$!IS$$SL
  k$$$SI!:?$$$$$$$$$xu$$j                              j$$ux$$$$$$$$$?:!IS$$$k
 :I$$SI:J$$?*"$$$$4^?*?:                               :?*?^4$$$$"*?$$L:iIS$$I:
 :IS$$SiJ?`  _.'$?`/'   ':                           :'    '/'?$'._  `?LiS$$SI:
  ?ISSik? _        ',    `                              .    ,'       _ ?kiSSI?
    ?i$?` _   k$        .                               :.        $k   _ `?$i?
      '?I:-?z$$I   _._.'                                  ._._   I$$z?-:I?'
     '*?- '?$$a louSxuS?                               ?xuSxuol a$$?' -?*'
           i$$$$$$$$$$$S                               S$$$$$$$$$$$i
              ?$$$?-                                       -?$$$?

     ██░ ██  ▄▄▄       ██▓    ▓█████  ██░ ██  ▒█████   █    ██  ███▄    █ ▓█████▄
    ▓██░ ██▒▒████▄    ▓██▒    ▓█   ▀ ▓██░ ██▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌
    ▒██▀▀██░▒██  ▀█▄  ▒██░    ▒███   ▒██▀▀██░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌
    ░▓█ ░██ ░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ░▓█ ░██ ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌
    ░▓█▒░██▓ ▓█   ▓██▒░██████▒░▒████▒░▓█▒░██▓░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓
     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒
     ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒
     ░  ░░ ░  ░   ▒     ░ ░      ░    ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░
     ░  ░  ░      ░  ░    ░  ░   ░  ░ ░  ░  ░    ░ ░     ░              ░    ░

              _                                                   _
         .k$$$$$g,                                           ,g$$$$$k.
      .k$$$$$$$$$$$a.                                     .a$$$$$$$$$$$k.
    .J$$$$$?'   `?$?^?,                                 ,?^?$?`   `?$$$$$L.
   JS$$SI!a,  _.JS$   ?,                               ,?   $SL._  ,a$!IS$$SL
  k$$$SI!:?$$$$$$$$$xu$$j                              j$$ux$$$$$$$$$?:!IS$$$k
 :I$$SI:J$$?*"$$$$4^?*?:                              :?*?^4$$$$"*?$$L:iIS$$I:
 :IS$$SiJ?`  _.'$?`/'  ':                            :'    '/'?$'._  `?LiS$$SI:
  ?ISSik? _        ',  .                                .    ,'       _ ?kiSSI?
    ?i$?` _  k$        .:                              :.        $k   _ `?$i?
      '?I:-?z$$I   _._.'                                  ._._   I$$z?-:I?'
     '*?- '?$$a louSxuS?                               ?xuSxuol a$$?' -?*'
           i$$$$$$$$$$$S                               S$$$$$$$$$$$i
              ?$$$?-                                       -?$$$?
```

# HaleHound-CYD

**ESP32-DIV HaleHound Edition for Cheap Yellow Display**

Version **v3.4.0 CYD Edition** | By [JesseCHale](https://github.com/JesseCHale) | [HaleHound.com](https://halehound.com)

---

## Overview

HaleHound-CYD is a multi-protocol offensive security toolkit built for the ESP32 "Cheap Yellow Display" (CYD) platform. Supports the 2.8" (ESP32-2432S028), QDtech E32R28T (2.8"), and QDtech E32R35T (3.5") boards. External CC1101 SubGHz, NRF24L01+PA+LNA 2.4GHz, PN532 NFC/RFID, and GPS modules connect via the CYD's breakout pins.

Every attack module from the original ESP32-DIV is present, plus CYD-exclusive features: full touchscreen navigation, EAPOL/PMKID capture, Karma attacks, wardriving with GPS logging, PN532 RFID card scanning/cloning/brute force, defensive jam detection, NRF24 promiscuous sniffer with MouseJack keystroke injection, AirTag attack suite (Phantom Flood, AirTag Replay, Find You), BLE HID keyboard injection (BLE Ducky), UART serial monitor for hardware hacking, and OTA firmware updates from SD card.

All radios transmit at maximum power. No safety nets.

---

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Supported Boards](#supported-boards)
- [Complete Wiring Guide](#complete-wiring-guide)
- [Menu Tree](#menu-tree)
- [Attack Modules - Detailed](#attack-modules---detailed)
  - [WiFi Attacks](#wifi-attacks)
  - [Bluetooth Attacks](#bluetooth-attacks)
  - [2.4GHz NRF24 Attacks](#24ghz-nrf24-attacks)
  - [SubGHz CC1101 Attacks](#subghz-cc1101-attacks)
  - [SIGINT Operations](#sigint-operations)
  - [Tools](#tools)
  - [Settings](#settings)
- [Touch Navigation](#touch-navigation)
- [TX Power Configuration](#tx-power-configuration)
- [SD Card Structure](#sd-card-structure)
- [Build and Flash](#build-and-flash)
- [Pin Reference Table](#pin-reference-table)
- [SPI Bus Sharing](#spi-bus-sharing)
- [Known Issues](#known-issues)
- [Project Structure](#project-structure)

---

## Hardware Requirements

### Base Board (Any One)

| Component | CYD 2.8" (ESP32-2432S028) | E32R35T (QDtech E32R35T) |
|-----------|---------------------------|---------------------------|
| M