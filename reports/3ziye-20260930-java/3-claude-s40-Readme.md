# Claude S40

![Claude S40: chat with Claude on a 2007 Nokia](docs/images/cover.png)

**Chat with Claude on a 2007 Nokia.** Claude S40 is an unofficial Claude
client for Nokia Series 40 phones (Java ME, CLDC 1.1 / MIDP 2.0), plus the
small Go server it talks to. Type on the keypad, get Claude's answer on a
240x320 screen: with today's news, weather and exchange rates from web
search, long answers you can page through, and a UI in Turkish or English.

**Video:** [Claude S40 on a Nokia 6300, on X](https://x.com/EmirKarsiyakali/status/2104183718483018026)

## Features

**On the phone**

- **Chat** with bubbles, timestamps and a typing indicator that counts the
  seconds. Replies keep their paragraphs and lists (dots, numbers, hanging
  indent).
- **Web search** for news, weather, rates: Claude searches on the server,
  the phone's 2007 browser is not involved. Sources are listed under the
  reply.
- **Reading mode** (key 7): one reply full width, page by page, whole lines
  only, page number and progress line. It keeps its place when you change
  the text size (key 9) or load the rest, and keeps the backlight on.
- **Long replies in parts**: "0 · Show the rest" fetches the next part
  from the server for free; Claude is not asked again.
- **Message actions**: select a message with 1/3, press the centre key:
  shorten, explain more simply, translate, ask about it, open it in the
  editor. They only fill in the editor; nothing is sent until you press
  Send.
- **Earlier chats** from the server, continue any of them; **pin** the ones
  you want to keep at the top (kept until unpinned), **delete** or **search**
  all chats (no Turkish letters needed: "sise" finds "şişe"); optional
  offline copy of the last chat.
- **Save to phone**: a reply as a .txt file (memory card if there is one),
  readable later without the network under "Saved".
- **Calendar and to-do**: ask "add to my calendar: dentist tomorrow at 3"
  and the reply carries a ready entry; the centre key opens a prefilled
  form, and only your "Save" writes it to the phone's own calendar or to-do
  list. Works from any message too.
- **Voice messages**: press Dictate, speak up to 30 seconds; the server
  turns it into text, which opens in the editor so you can check and fix
  it before you send it to Claude.
- **Photos**: take one with the camera or pick one from the phone and ask
  about it ("what is this?", "translate this sign", "read this label");
  follow-up questions in the same chat still see it.
- **Your notes for Claude** (Settings): "I'm Emir, I live in Istanbul, keep
  it short" is sent with every message.
- **Data usage**: requests and approximate kilobytes today and in total.
- **20 quick prompts** (search the web, weather, translate, reply to a
  message, add to my calendar, summarize, fix my writing, ...).
- **Setup wizard** on first start: language, server address, connection
  test, pairing with a 6-digit code (no long code to type).
- **Keypad-first**: every screen works with the keypad; a Shortcuts screen
  lists every key. Retry after an error is one key and never charges twice.
- **Look and feel**: light and dark theme, three text sizes, start-up
  animation and jingle, reply chime, vibration and backlight. Texts are
  fitted to the screen and checked from 128x160 to 320x240.

**On the server**

- One Go binary / Docker image that speaks TLS 1.0 to the phone with a
  certificate from your own private CA, and modern HTTPS to the Claude API.
- Per-device access tokens through pairing, daily request, token,
  web-search, voice-message and photo limits, no automatic retries of paid
  calls.
- Optional speech-to-text for voice messages (OpenAI), with a minimal
  ffmpeg in the image for the phone's AMR recordings.
- SQLite for chats (30 days, pinned ones until unpinned), search over
  them, admin API on localhost only.

## Screens

| Home | Waiting for Claude | Lists and paragraphs | Reading mode |
|---|---|---|---|
| ![](docs/images/home.png) | ![](docs/images/typing.png) | ![](docs/images/lists.png) | ![](docs/images/reading.png) |
| **A calendar entry, selected** | **Message actions** | **Quick prompts** | **Dark theme, large text** |
| ![](docs/images/selected.png) | ![](docs/images/actions.png) | ![](docs/images/prompts.png) | ![](docs/images/dark.png) |

Screenshots are from the FreeJ2ME emulator in the app's test mode (the
"[Test mode]" replies are fake and cost nothing; the emulator reports no
calendar API, so the harness turns the calendar actions on for these
screens and never saves); the cover is a drawing.
Start-up animation: [docs/images/splash.gif](docs/images/splash.gif).

> Unofficial side project. Not made, endorsed or supported by Anthropic or
> Nokia. See [TRADEMARKS.md](TRADEMARKS.md).

Tested on a **Nokia 6300 (RM-217, firmware V06.60)**. Other Series 40
phones (CLDC 1.1 / MIDP 2.0, 240x320) may work but are untested.

## How it works

```
Nokia (Java ME app) --HTTPS: TLS 1.0, RSA, no SNI, cert from YOUR private CA--> c