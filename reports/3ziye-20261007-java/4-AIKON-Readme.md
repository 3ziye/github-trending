<h1><img src="docs/images/wordmark.png" alt="AIKON" width="420"></h1>

> **Formerly Claude S40.** The project was called *Claude S40* up to phone
> app 0.10.x / server 0.7.x, while it only talked to Claude. Since it also
> speaks to OpenAI, Gemini and Grok it is called **AIKON** (Nokia spelled
> backwards). The repository moved from `emir/claude-s40` to `emir/AIKON`
> (GitHub redirects the old address); the Java package and server names
> keep the old name.

![AIKON: today's AI on a 2007 Nokia](docs/images/cover.png)

**Today's AI on a 2007 Nokia.** AIKON is an AI chat client for
Nokia Series 40 and Symbian S60 phones (Java ME, CLDC 1.1 / MIDP 2.0), plus
the small Go server it talks to. Pick a model per chat (Claude, OpenAI, Gemini or Grok),
type on the keypad, get the answer on a 240x320 screen: with today's news,
weather and exchange rates from web search, long answers you can page
through, and a UI in Turkish, English, Spanish, Portuguese, French, German, Russian or
Indonesian. Tested on the Nokia 6300 (S40) and
the Nokia E63 (S60 QWERTY).

**Video** (still as Claude S40): [on a Nokia 6300, on X](https://x.com/EmirKarsiyakali/status/2104183718483018026)

## Features

**On the phone**

- **Pick the model per chat**: first the provider (Claude, OpenAI, Gemini,
  Grok), then one of the models the server offers; switch in the middle of
  a chat with Options > Model. Every reply is labelled with its model.
- **Chat**: your messages in bubbles, replies full width, day headings
  ("Today", "Yesterday"), and a typing indicator that counts the seconds.
  Replies keep their paragraphs and lists (dots, numbers, hanging indent);
  an unsent draft waits in the input bar.
- **Web search** for news, weather, rates: the model searches on the server
  with its provider's search tool; the phone's 2007 browser is not involved. Sources are listed under the
  reply.
- **Reading mode** (key 7): one reply full width, page by page, whole lines
  only, page number and progress line. It keeps its place when you change
  the text size (key 9) or load the rest.
- **Long replies in parts**: "0 · Show the rest" fetches the next part
  from the server for free; the model is not asked again.
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
  it before you send it.
- **Photos**: take one with the camera or pick one from the phone and ask
  about it ("what is this?", "translate this sign", "read this label");
  follow-up questions in the same chat still see it.
- **Your notes for the AI** (Settings): "I'm Emir, I live in Istanbul, keep
  it short" is sent with every message.
- **Data usage**: requests and approximate kilobytes today and in total.
- **20 quick prompts** (search the web, weather, translate, reply to a
  message, add to my calendar, summarize, fix my writing, ...).
- **Short notes, details on request**: info and errors are one line; select
  one (1/3) and press the centre key for the explanation; setup and settings
  screens keep theirs under Options > Info.
- **Setup wizard** on first start: server address, connection test,
  pairing with a 6-digit code (no long code to type); the language follows
  the phone. A build that names its server skips to the pairing.
- **Keypad-first**: every screen works with the keypad (on QWERTY phones
  like the E63, the digits printed on the letter keys); a Shortcuts screen
  lists every key. Retry after an error is one key and never charges twice.
- **Eight languages**: English, Türkçe, Español, Português, Français,
  Deutsch, Русский and Bahasa Indonesia. The app opens in the phone's
  language (English for any other) and changes under Settings > Language.
  The replies follow the language you write in, whatever the menus say.
- **Look and feel**: every screen except text entry is drawn by the app:
  line icons with smooth edges, lists with two-line rows, settings with
  switches that save at once, full screen. Light, dark or automatic (dark
  in the evening) look, three text sizes, start-up animation and jingle,
  reply chime, vibration and ba