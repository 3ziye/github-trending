# dumbtv

Your TV should do what you paid for: your apps, your HDMI inputs, and nothing
else. No ads from the TV itself, no watch tracking, no update you did not ask
for. dumbtv applies that over ADB from another machine — **no root**, nothing
written to `/system`, every step reversible with one script.

The same idea, told to whichever TV will listen:

| TV | Debloat | Own home screen | On-device DNS filter |
|---|---|---|---|
| **Fire OS** (Fire TV sticks, Fire TV Edition TVs) | yes | yes | yes |
| **Android TV / Google TV** (Sony, TCL, Philips, Hisense, Xiaomi, Shield) | yes | yes, by disabling the stock launcher | yes |
| **Samsung, LG, Roku, VIDAA, Vizio, Panasonic, Philips Saphi** | no shell, no path | no | no — block it at the router, or boot the TV straight into HDMI |

Tested end to end on a Fire TV Edition television running Fire OS 7.7.1.7
(Android 9). Fire OS 6 and 8 differ in small ways; Android TV needs a different
package list and a different launcher trick. Fire OS 6 (Android 7.1, e.g. the 2018
Fire TV Stick 4K) uses its own lists in `data/fireos6/`, picked up from the device,
and the launcher holds HOME there with a small foreground service instead of the
accessibility hook Amazon refuses on 6.7. The ones that cannot be opened, and the
honest reason for each, are in `docs/OTHER-TVS.md` — along with what we are
working on to reach them.

**What it will not do:** replace the operating system, unlock a bootloader, or
survive a factory reset. Every current TV has a signed boot chain and a verified
system partition, so there is no honest way around it. Pretending otherwise is
how people brick their TVs. See `docs/WHY-NOT-REPLACE-OS.md`.

## Add your TV to the catalog

At the end of a session — or any time something surprised you — record it:

```sh
./scripts/contribute.sh
```

It reads the model, OS build and kernel from the TV, then asks only what a robot
cannot know: how developer mode was enabled, where the IP address was shown,
which dialogs blocked automation and what dismissed each one. It writes
`catalog/devices/<id>.yaml`, validates it, and prints the `git` / `gh` commands
for a pull request. No git? `.github/ISSUE_TEMPLATE/device-report.yml` asks the
same questions in a browser.

That file is the part this repo cannot generate: per-model knowledge. Code is
cheap; someone's evening is not.

## It asks what you want to keep

Nothing is decided for you:

```sh
./scripts/configure.sh
```

It goes through the apps this repo would remove (`data/fireos/user-apps.txt`,
with readable names from `data/apps.txt`) and asks, one by one, whether to remove
each. Answer "no" and that app is never touched. It also asks whether you watch
Prime Video — Prime stays installed either way, but if you say yes its video CDN
is left out of the blocklist so playback keeps working — and whether you want the
launcher replaced and the DNS filter installed.

The answers go into `dumbtv.conf` (git-ignored). Re-run it any time to change
your mind; the scripts read that file, so nothing has to be edited by hand.

Ads, telemetry, experiments and Alexa are removed regardless. This step is only
about apps a person might actually watch.

## Reversibility

`scripts/restore.sh` puts back package state, app-ops, network rules and every
setting the pass touched — using the snapshot `preflight.sh` took first, so the
values are the ones this TV actually had, not generic defaults. The snapshot is
taken once: run `preflight.sh` before the first pass, and a later run cannot
overwrite the originals.

Two things are not reversible:

1. **Apps that live in `/data`.** The streaming apps the pass uninstalls (JioHotstar,
   Zee5, JioCinema, SonyLIV, Discovery+, Aaj Tak, Twitch, FastScreen, MX Player)
   have their APKs deleted; they come back from the store, not from a script. The
   keep-list in `configure.sh` exists so you only lose what you agreed to lose.
2. **Anything uninstalled after the fact.** `restore.sh` restores the lists in
   `data/`, so an app removed by hand is still gone.

Everything else — the ~65 disabled packages, the launcher, the DNS filter, the
settings — is undoable, and a factory reset also undoes it (including this repo's
work).

## What it changes

| Layer | Result |
|---|---|
| Packages | ~65 disabled: ACR (screen fingerprinting), ad-ID service, sponsored rows, watch-time analytics, A/B experiment engines, Alexa/mic app, promo screensaver, OTA helpers. Ad-funded streaming apps uninstalled. YouTube and VLC kept. |
| Protected packages | The handful Amazon refuses to disable get their background execution and background data removed instead. |
| Settings | Ad tracking limited, interest-based ads off, app/device usage reporting off, wake word and voice off, promo autoplay off. |
| DNS | personalDNSfilter runs on the TV: Amazon telemetry, Alexa endpoints and the OTA servers answer `127.0.0.1`. YouTube and the app store still resolve. |
| Launcher | [dumbtv home](launcher/README.md), this repo's own launcher, replac