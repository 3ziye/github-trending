# NFCX

<p align="center"><img src="docs/images/nfcx-logo.png" alt="NFCX logo" width="144"></p>

<p align="center"><strong>A cross-platform, open-source, easy-to-use GUI desktop tool for NFC.</strong></p>

<p align="center"><a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a></p>

NFCX brings reader discovery, card information, reads, protected writes, raw dumps, key management, and recovery workflows into one desktop application for macOS, Windows, and Linux. It is for MIFARE Classic cards you own or are authorized to test.

NFCX is open source and uses a clear, direct GUI so NFC work does not depend on a collection of command-line tools.

Website: [nfcx.tools](https://nfcx.tools) · Downloads: [GitHub Releases](https://github.com/BennyThink/NFCX/releases)

# What NFCX can do

- Discover and connect NFC readers.
- Detect cards and show their UID, ATQA, SAK, and card type.
- Work with MIFARE Classic 1K: authenticate with Key A or Key B, read blocks, edit data, and write changes.
- Save and load compatible raw dumps (`.bin` / `.mfd`) with sidecar metadata; restore with capacity, BCC, access-bit, and per-block read-back checks.
- Scan common keys and manage a local key catalog.
- Run the integrated recovery sequence on a validated PN532 UART reader: common keys, Darkside, Nested, Hardnested, and read verification.
- Use the guarded 4-byte UID/block 0 workflow for supported CUID/Gen2 and Gen1A cards.

# Supported readers

| Reader | Connection / backend | Status | Platforms |
| --- | --- | --- | --- |
| PN532 + FT232RL | Serial, `pn532_uart` via libnfc | **Tested**: discovery, Classic read/write, dump/restore, and key recovery | macOS, Windows, Linux builds |
| Other PN532 UART adapters | Serial, `pn532_uart` via libnfc | **Expected compatible**; not hardware-tested by this project | Depends on adapter driver and serial permissions |
| ACR122U | USB / PC/SC or libnfc | **Unsupported in this release**: NFCX hardware validation and a release profile are not yet available | — |
| ACR1552U | USB / vendor PC/SC driver | **Unsupported in this release**: NFCX hardware validation and a release profile are not yet available | — |
| Other libnfc devices | Varies | **Unsupported** until an explicit NFCX validation profile exists | — |

# Drivers and runtime requirements

NFCX packages its NFC runtime. You do not need to install libnfc, mfoc, mfcuk, or separate command-line NFC tools.

- Linux: your account generally needs read/write serial access (commonly the `dialout` group). For example, run `sudo usermod -aG dialout $USER`, then sign out and back in. You can also run it with `sudo` if you understand the implications.
- macOS: an unsigned release can show a Gatekeeper warning. Use **System Settings → Privacy & Security** to allow it to open when prompted.
- Windows: starting NFCX may require the [FTDI virtual-COM/serial driver](https://ftdichip.com/drivers/).

# Download and install

1. Open [GitHub Releases](https://github.com/BennyThink/NFCX/releases).
2. Download the archive or installer for your operating system.
3. Install or unpack it, then install the reader driver if needed.
4. Connect the reader and start NFCX.

# Quick start

1. Connect an NFC reader and launch NFCX.
2. Refresh the reader list or enter the PN532 UART connection string.
3. Place an authorized card on the reader and select **Scan Card**.
4. Review the card information, then use **Key Recovery**, **Read Card**, or **Change UID** as needed.

UART/HSU config: 
![uart.jpeg](docs/images/uart.jpeg)

# FAQ

<details><summary>Do I still need a card reader?</summary>

Yes. NFCX communicates with physical NFC cards through a compatible external reader.
</details>

<details><summary>Which hardware is supported?</summary>

The tested combination is PN532 + FT232RL. Other serial adapters may work, but FT232RL is recommended. Set the PN532 to UART/HSU mode and cross the data lines (PN532 RX to the serial adapter’s TX). A soldered connection is recommended to avoid unreliable jumper wires.
</details>

<details><summary>Can I write an access card to an iPhone?</summary>

NFCX can work with physical access cards, but cards in an iPhone cannot be written like ordinary blank NFC cards. Consider using a writable NFC sticker and attaching it to the back of the phone.
</details>

<details><summary>Which cards do you recommend?</summary>

For authorized testing, CUID cards are a useful choice. They commonly support changing the UID, and their all-FF Key A and Key B are convenient for testing.
</details>

<details><summary>Can I clone an access card?</summary>

It depends on the card type and access-control system design. Only work with cards and systems you own or are explicitly authorized to test.
</details>

<details><summary>Why can’t NFCX find my reader?</summary>

Check the serial port, adapter driver, whether another program is using the device, and whether your current system account has permission to access the serial port.
</details>

<detail