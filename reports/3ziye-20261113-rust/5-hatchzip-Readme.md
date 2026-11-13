<h1 align="center">HatchZip</h1>

<p align="center">
  Extract huge archives in place. The archive shrinks as your files hatch,<br>
  so you only need free space for the output, not for the output <em>and</em> the archive.
</p>

<h4 align="center">
  <a href="https://hatchzip.dev">hatchzip.dev</a> |
  <a href="#installation">Installation</a> |
  <a href="#usage">Usage</a> |
  <a href="#is-hatchzip-safe">Safety</a> |
  <a href="docs/how-it-works.md">How it works</a> |
  <a href="CONTRIBUTING.md">Contributing</a>
</h4>

<p align="center">
  <a href="https://github.com/xevrion/hatchzip/actions/workflows/ci.yml"><img src="https://github.com/xevrion/hatchzip/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/xevrion/hatchzip"><img src="https://api.scorecard.dev/projects/github.com/xevrion/hatchzip/badge" alt="OpenSSF Scorecard" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg" alt="MIT or Apache-2.0 licensed" /></a>
  <img src="https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-blue.svg" alt="Linux, Windows and macOS" />
</p>

<p align="center">
  <img src="docs/media/hatchzip.gif" width="720" alt="HatchZip extracts the last part of the archive, then cuts it off the archive file, so the disk never holds the archive and all the files at once" />
</p>

HatchZip is a free, open-source archive extractor for Windows, macOS and Linux, with a desktop app and a command line tool. It extracts ZIP, 7z, RAR, tar and split archives in place, for when there is not enough disk space to extract an archive next to itself, such as a large game download on a nearly full disk. Download it from [hatchzip.dev](https://hatchzip.dev).

A 180 GB game download that unpacks to 200 GB needs 380 GB of disk with WinRAR, 7-Zip or `unzip`, because the archive and everything extracted from it have to exist at the same time. HatchZip needs a little over 200 GB. It extracts the archive from the end and cuts each finished part off the archive file as it goes, so the space the archive gives back is reused for the next files.

It checks that the extraction will fit before it changes anything, keeps a safety margin of free space the whole way through, and can be stopped or crash at any moment and pick up where it left off. It reads ZIP, 7z, tar, `.tar.gz`, `.tar.bz2`, `.tar.xz`, RAR volume sets and split archives.

### Get it

> [!IMPORTANT]
> HatchZip is only distributed from this repository's [releases](https://github.com/xevrion/hatchzip/releases) and its site, [hatchzip.dev](https://hatchzip.dev). Other sites using the name, such as hatchzip.com, are not affiliated with this project.

No coding needed. **[Download for Windows](https://github.com/xevrion/hatchzip/releases/latest/download/HatchZip-x64-setup.exe)** (Windows 10 and 11), or for [macOS (Apple Silicon)](https://github.com/xevrion/hatchzip/releases/latest/download/HatchZip-aarch64.dmg), [macOS (Intel)](https://github.com/xevrion/hatchzip/releases/latest/download/HatchZip-x86_64.dmg) and [Linux](#installation).

1. Run the installer. Windows may show "Windows protected your PC" because HatchZip is not code-signed yet: choose **More info**, then **Run anyway**.
2. Right-click the archive, choose **HatchZip**, then **Extract here**. On Windows 11 the menu is under **Show more options**. To pick the destination folder first, choose **Extract files…** instead.
3. Or open HatchZip from the Start menu, open the archive, and choose **Extract**.

HatchZip shows whether the files will fit before it changes anything. The archive is used up as the files come out, so when it finishes, only the extracted files are left.

**Extract here** puts an archive with one folder or one file at its top next to the archive. An archive with several files or folders at its top goes into a new folder named after it, so its files never mix with what is already there. The progress window closes when the extraction completes; to keep it open, clear **Close the progress window when extraction completes** in the app's Settings menu.

To keep the archive when there is room for both, choose **Extract here (keep archive)** in the right-click menu. To always keep archives, as other extractors do, clear **Remove the archive during extraction** in the app's Settings menu; every right-click entry then keeps the archive too. That is a normal extraction: the archive is not changed, and space is required for all extracted files.

## When there is not enough disk space to extract

The same 200 MB of game data (21 files), packed by the real tools, extracted on a 220 MiB disk with about 50 MB free:

| Archive | `unzip` / 7-Zip | HatchZip |
|---|---|---|
| ZIP, 180 MB | `unzip` ran out of space at file 6 of 21 | Finished, every file byte-identical |
| 7z from 7-Zip 25.01, `-ms=20m` (10 solid blocks) | Needs 380 MB | Finished in 0.64 s, every file byte-identical |
| 7z split into 5 volumes of 40 MB 