<p align="center">
  <b>Enjoying this project?</b> It is built and tested in my free time. A small
  donation helps buy test hardware and keeps the development going. Thank you! ❤️
  <br><br>
  <a href="https://www.paypal.com/donate/?business=VGY3ZM78NAL78&no_recurring=0&currency_code=EUR"><img src="https://img.shields.io/badge/Donate-PayPal-ff5e5b?style=for-the-badge&logo=paypal&logoColor=white" alt="Donate with PayPal"></a>
</p>

<p align="center">
  <a href="images/airplay-surround-dark.png"><img src="images/airplay-surround-dark.png" alt="ESP32 AirPlay 2 Surround 7.1" width="100%"></a>
</p>

# ESP32 AirPlay 2 Surround Gateway

**Wireless 5.1 / 7.1 surround sound from an Apple TV, built from low-cost
ESP32-S3 boards: one Gateway, and one board per speaker.**

The Apple TV sees **one AirPlay 2 speaker: the Gateway**. The Gateway takes
the complete surround stream and passes it on, unchanged, to up to **eight
speaker boards** over your Wi-Fi. Every speaker decodes **only its own
channel** (Front Left, Centre, Subwoofer, Rear Right, …) and plays it through
any amplifier and speaker you like. All speakers share one clock taken from
the Wi-Fi access point itself, so they play each sample at the same moment.
No cables between the speakers, no AV receiver, one web page for the whole
system.

- 🎬 **5.1 and 7.1 AAC** (Apple Music Dolby Atmos, films and series from the
  Apple TV apps).
- 🎵 **Stereo** too: ALAC 44.1 kHz/16-bit and **lossless 48 kHz/24-bit**, AAC
  44.1 / 48 kHz, from any AirPlay 2 sender. A stereo song plays on the front
  pair and the subwoofer, as on an AV receiver.
- 📡 **One AirPlay target.** You pick the Gateway, not eight speakers. Pairing,
  RTSP and the Apple TV's clock are handled once, by the Gateway.
- 🏠 **Apple Home (HomeKit)** pairing, artwork, playback and volume controls
  for the whole surround system as one speaker.
- ⏱️ **Microsecond clock alignment** between speakers through the access
  point's beacon timer (TSF). No extra hardware, no cables.
- 🎤 **Room calibration** with an optional INMP441 microphone on the
  Gateway: distance, delay and level of every speaker measured from your
  seat, applied with one click.
- 📈 **Room EQ** with the same microphone: each speaker's frequency
  response measured from your seat and corrected with its own EQ, with
  settings like REW's.
- 📻 **Web radio** on the Gateway: stations of your country, a search, your
  favourites or any stream address (MP3 or AAC over HTTP / HTTPS), played on
  all speakers like an AirPlay stream. AirPlay always takes over.
- 💾 **USB player** on the Gateway (experimental): FLAC,
  WAV, ALAC, AAC and MP3 from a USB drive, **bit for bit** to the speakers,
  5.1 / 7.1 files each channel on its own speaker, gapless, with tags,
  covers and m3u playlists ([USB player](#usb-player-experimental)).
- 🎛️ **One page for all speakers**: role, level and delay of every speaker,
  and a live view of what each one plays. Each speaker keeps its own
  2 × 24-band parametric EQ, mono or **bi-amp** (woofer + tweeter through a
  Linkwitz-Riley crossover), loudness and latency settings.
- 🔀 **Format changes on the fly**: the Apple TV can switch between stereo and
  surround from track to track; the speakers follow without reconnecting.
- ⚡ About **a third of one CPU core** per speaker for 7.1, thanks to a patched
  Fraunhofer FDK AAC decoder that synthesises just one channel.
- 🔗 **Speakers belong to the system**: a speaker is not an AirPlay
  receiver of its own and never shows up on an iPhone; it just follows the
  Gateway. (A board that is its own AirPlay receiver is the `standalone`
  branch.)

> [!NOTE]
> **The project is under active development.** A Gateway and five speakers
> (front pair, centre, side pair) play 5.1 and 7.1 from an Apple TV and
> stereo from an iPhone, each speaker its own channel, audibly in sync.
> Features, defaults and wiring may still change, and this README is updated
> with every change. See [Limitations](#limitations).

> [!IMPORTANT]
> **16 MB flash modules (ESP32-S3 N16R8).** The 8 MB flash of the N8R8
> boards is nearly full: the Gateway keeps a copy of the speaker firmware to
> update the speakers, and that copy has only about 117 KB of room left. A
> board with 16 MB can already use its full flash
> ([16 MB flash](#16-mb-flash)); new features will need it. **If you buy
> boards now, buy N16R8.** 8 MB boards build and update as before.
>
> **Planned:**
> - 🔊 **USB sound card** support.
> - 📺 **DLNA**: play to the system from DLNA / UPnP apps, not only AirPlay.

## Contents

- [Gallery](#gallery)
- [Apple Home (HomeKit)](#apple-home-homekit)
- [How it works](#how-it-works)
- [What you need](#what-you-need)
- [Assembly and wiring](#assembly-and-wiring)
- [Installation](#installation)
- [First start](#first-start)
- [Settings](#settings)
- [USB player (experimental)](#usb-player-experimental)
- [Technical details](#technical-details)
- [Measuring sync](#measuring-sync)
- [Limitations](#limitations)
- [Tro