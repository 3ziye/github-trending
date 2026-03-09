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

Version **v3.2.0 CYD Edition** | By [JesseCHale](https://github.com/JesseCHale)

---

## Overview

HaleHound-CYD is a multi-protocol offensive security toolkit built for the ESP32 "Cheap Yellow Display" (CYD) platform. Supports both the 2.8" (ESP32-2432S028) and 3.5" (ESP32-3248S035C) CYD boards. External CC1101 SubGHz, NRF24L01+PA+LNA 2.4GHz, PN532 NFC/RFID, and GPS modules connect via the CYD's breakout pins.

Every attack module from the original ESP32-DIV is present, plus CYD-exclusive features: full touchscreen navigation, EAPOL/PMKID capture, Karma attacks, wardriving with GPS logging, PN532 RFID card scanning/cloning/brute force, defensive jam detection, UART serial monitor for hardware hacking, and OTA firmware updates from SD card.

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

### Base Board (Either One)

| Component | CYD 2.8" (ESP32-2432S028) | CYD 3.5" (ESP32-3248S035C) |
|-----------|---------------------------|---------------------------|
| MCU | ESP32-WROOM-32 / 32UE | ESP32-WROOM-32 |
| Display | 2.8" ILI9341 240x320 | 3.5" ST7796 320x480 |
| Touch | XPT2046 Resistive (SPI) | GT911 Capacitive (I2C) |
| Flash | 4MB minimum (16MB recommended) | 4MB min