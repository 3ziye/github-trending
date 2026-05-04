# RSVP Nano

RSVP Nano is an open-source ESP32-S3 reading device for showing text one word at a time with RSVP (Rapid Serial Visual Presentation). The firmware is built around stable anchor-letter rendering, readable typography, tunable pacing, SD card storage, and a web-first book conversion workflow.

## Highlights

- One-word RSVP reader with stable anchor alignment.
- Optional page-scroll reading mode that keeps the same pacing/book-position mechanics without the RSVP anchor.
- Hold to read, double-tap to lock autoplay, tap to stop locked autoplay, and pause on sentence boundaries.
- Horizontal scrub preview with hold-to-scroll text browsing, then tap to return to RSVP.
- Adjustable typeface, font size, typography, anchor guides, pacing, and phantom words.
- Menu language selection for English, Spanish, French, German, Romanian, and Polish.
- Chapter and paragraph-aware navigation.
- SD card library under `/books`.
- Web-first book conversion and SD-card library sync from the browser flasher.
- Optional GitHub Release OTA updates over Wi-Fi with on-device network setup and touch keyboard entry.
- USB mass-storage mode for copying books to the SD card.
- Browser-based firmware installation plus in-browser library conversion, sidecar cleanup, and SD-card sync.

## Getting Started

### Flash From The Browser

The easiest way to install the firmware is the web flasher:

<https://ionutdecebal.github.io/rsvpnano/>

Use Chrome or Edge on desktop, connect the device over USB, and follow the installer prompts.
The hosted flasher installs the latest published GitHub Release rather than unreleased `main`
commits.

The browser flasher uses ESP Web Tools and Web Serial, so it must be opened over HTTPS or localhost.
It also includes a browser-side Library Workspace for importing supported books, converting them
into `.rsvp`, downloading a `.zip` of the results, cleaning interrupted sidecar files, and syncing
the converted outputs back into the SD card's `/books` folder.

On the device, you can switch the menu language in `Settings -> Display -> Language`.
You can also switch between anchored RSVP and the page scroller in `Settings -> Display ->
Reading mode`.
While paused in RSVP mode, swipe left or right to open the larger scrub preview, hold and move
your finger vertically to browse smoothly through the text, and tap to return to the anchored
word view.

The browser workflow currently accepts:

- `.epub`
- `.txt`
- `.md` / `.markdown`
- `.html` / `.htm` / `.xhtml`

The browser page automatically writes `.rsvp` output that preserves common accented, Baltic,
Sami, and other extended-Latin letters while staying compatible with the current firmware.
It is currently the best-supported conversion path and the recommended way to prepare books.

### Add Books

The easiest workflow is to use the Library Workspace on the browser flasher page, then sync the
converted files directly into the SD card's `/books` folder.

If you want to manage files manually, create a `books` folder at the root of the SD card:

```text
/books
  my-book.epub
  another-book.rsvp
```

The device library scans `/books` for `.rsvp`, `.txt`, and `.epub` files, but the recommended
workflow is to put browser-converted `.rsvp` files there whenever possible.

Current text support is best for ASCII plus a curated set of accented and extended-Latin letters
used in many European languages. That includes the usual Germanic and Nordic letters plus common
extras such as `OE`/`oe` ligatures, Polish `L`-slash style letters, Romanian comma-accent letters,
several Central European and Turkish forms, the Czech and Hungarian letters used outside Latin-1,
and the Baltic/Sami letters used in Latvian, Lithuanian, and Sami text. Common book punctuation
such as curly quotes, guillemets, and bracket variants is normalized into readable ASCII wrappers.
The Standard serif reader font renders that wider Latin set directly. In the other reader fonts
and in the tiny UI font, unsupported letters currently fall back to the closest plain ASCII letter
in the selected font instead of switching fonts.
More complex scripts still need additional renderer and font work.

The firmware prioritizes `.rsvp` files. If a matching `.rsvp` file does not exist yet, an EPUB
can still be converted locally the first time it is opened, and the converted `.rsvp` file is then
reused on future launches. That on-device path is best treated as a fallback; the browser converter
currently has the best compatibility and library-management flow.

If a conversion is interrupted, you may see sidecar files such as:

```text
.rsvp.tmp
.rsvp.converting
.rsvp.failed
```

### OTA Updates

The firmware can optionally check GitHub Releases over Wi-Fi and install a newer app build without
erasing your reader settings or saved reading progress. Settings and progress are stored in ESP32
`Preferences`, so a normal OTA update keeps them intact.

To enable OTA on the device:

1. Open `Settings -> Wi-Fi`.
2. Tap `Choose netw