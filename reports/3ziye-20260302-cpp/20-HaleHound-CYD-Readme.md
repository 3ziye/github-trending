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

Version **v3.1.0 CYD Edition** | By [JesseCHale](https://github.com/JesseCHale)

---

## Overview

HaleHound-CYD is a multi-protocol offensive security toolkit built for the ESP32-2432S028 "Cheap Yellow Display" (CYD) platform. It ports the full ESP32-DIV HaleHound v2.5.0 firmware to the CYD's 2.8" touchscreen form factor, adding external CC1101 SubGHz, NRF24L01+PA+LNA 2.4GHz, and GPS radios via the CYD's breakout pins.

Every attack module from the original ESP32-DIV is present, plus CYD-exclusive features: full touchscreen navigation, EAPOL/PMKID capture, Karma attacks, wardriving with GPS logging, UART serial monitor for hardware hacking, and OTA firmware updates from SD card.

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

### Base Board

| Component | Specification |
|-----------|--------------|
| Board | ESP32-2432S028 (CYD 2.8") |
| MCU | ESP32-WROOM-32 or ESP32-WROOM-32UE |
| Display | 2.8" ILI9341 320x240 TFT |
| Touch | XPT2046 Resistive (separate SPI bus) |
| Flash | 4MB minimum (16MB recommended) |
| USB | CH340C USB-Serial (Micro-USB or USB-C) |
| SD Card | Built-in MicroSD slot (VSPI bus) |
| Power | 5V USB or LiPo + boost converter |

### External Modul