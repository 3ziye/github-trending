<div align="center">

# TV Detox

<a href="https://www.skool.com/staffed-claude-code-ai-5304"><img src="https://img.shields.io/badge/Join_the_community_%E2%86%92-FFD400?style=for-the-badge" alt="Join the community" width="340"></a>

### Make an old, slow Android TV fast again.

Claude Code or Codex does the work. You just press OK on the remote.

[![Release](https://img.shields.io/github/v/release/Ansub/tv-detox?color=black)](https://github.com/Ansub/tv-detox/releases/latest)
[![Tests](https://img.shields.io/github/actions/workflow/status/Ansub/tv-detox/build.yml?branch=main&label=tests)](https://github.com/Ansub/tv-detox/actions)
[![License](https://img.shields.io/badge/license-MIT-black)](LICENSE)
[![YouTube](https://img.shields.io/badge/YouTube-@ansubkhan-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@ansubkhan)

**As seen on**

[![The Verge](https://img.shields.io/badge/The_Verge-5200FF?style=for-the-badge)](https://www.theverge.com/tech/1016116/vibe-coding-tv-os)
[![Android Authority](https://img.shields.io/badge/Android_Authority-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://www.androidauthority.com/android-tv-vibe-hacking-remove-ads-bloatware-3725338/)
[![Mashable](https://img.shields.io/badge/Mashable-00AEEF?style=for-the-badge)](https://mashable.com/tech/smart-tv-ads-claude-code-ai-cleanup)
[![t3n](https://img.shields.io/badge/t3n-E6007E?style=for-the-badge)](https://t3n.de/news/claude-alter-fernseher-android-tv-1768831/)
[![Tom's Guide](https://img.shields.io/badge/Tom's_Guide-E1261C?style=for-the-badge)](https://www.tomsguide.com/ai/people-are-using-ai-to-turn-their-smart-tvs-into-dumb-tvs-and-you-might-want-to-do-the-same)
[![Yahoo Tech](https://img.shields.io/badge/Yahoo_Tech-6001D2?style=for-the-badge)](https://tech.yahoo.com/ai/article/sick-of-seeing-ads-and-clutter-on-your-smart-tv-the-internet-says-ai-can-fix-that-181417392.html)
[![GIGA](https://img.shields.io/badge/GIGA-E2001A?style=for-the-badge)](https://www.giga.de/tech/ist-euer-smart-tv-zu-langsam-dieses-ki-tool-kann-helfen--01M5HH1C89TWAQX4FYXJBDBQAF)
[![Computer Hoy](https://img.shields.io/badge/Computer_Hoy-0A64A0?style=for-the-badge)](https://computerhoy.20minutos.es/dispositivos/tv-detox-app-gratis-elimina-obsolescencia-programada-tu-smart-tv-claude-hace-trabajo-tu-solo-tienes-que-pulsar-ok-mando-distancia_7050469_0.html)
[![AI Times](https://img.shields.io/badge/AI_Times-111111?style=for-the-badge)](https://www.aitimes.com/news/articleView.html?idxno=216547)

[All press coverage →](press.md)

<img src="docs/home-screen.png" alt="The TV Detox home screen" width="100%">

</div>

<table>
<tr>
<td width="33%" valign="top"><b>🧹 Removes the junk</b><br>Bloatware, ads and sponsored rows, gone.</td>
<td width="33%" valign="top"><b>📺 A calm home screen</b><br>Your apps, your HDMI inputs and a clock. Nothing else.</td>
<td width="33%" valign="top"><b>↩️ Undo anytime</b><br>Apps are turned off, never deleted.</td>
</tr>
</table>

## Watch it work

<a href="https://www.youtube.com/watch?v=fP2SGGVsaB0"><img src="https://img.youtube.com/vi/fP2SGGVsaB0/maxresdefault.jpg" alt="Watch: Claude Made My Old Android TV Feel Brand New" width="100%"></a>

**[▶ Claude Made My Old Android TV Feel Brand New](https://www.youtube.com/watch?v=fP2SGGVsaB0)** · the full setup on a real TV, in 4 minutes.

## Get started

**1. Turn on developer mode on the TV.**
Settings → Device Preferences → About → press **Build** 7 times. Then turn on **USB debugging** in **Developer options**. [Stuck?](#help)
Read the [notes and warnings](#notes-and-warnings) first.

**2. Open [Claude Code](https://claude.com/claude-code) or [Codex](https://openai.com/codex) on your laptop.**
The laptop and TV must be on the same Wi-Fi.

**3. Paste this in.**

```text
Help me clean up my Android TV and make it faster.
My TV is a <brand and model>.

1. Before you change anything, tell me in plain words:
   this turns off system apps, and that has some risk.
   A few TVs got stuck at the logo or kept restarting,
   and you're an AI, so you can make mistakes. undo.sh
   and your undo list turn everything back on. Ask me to
   confirm I want to go ahead.
2. Connect to my TV over Wi-Fi. Walk me through anything
   I need to tap on the TV.
3. Before changing anything, list every app in plain English:
   safe to turn off, needed by the TV, and apps I use.
   Check free memory.
4. Ask me before every change. Turn apps off instead of
   deleting them. Keep a list of what you changed and how
   to undo it.
5. Never turn off: Google Play services
   (com.google.android.gms), Google Play, Settings,
   System UI, setup apps, the keyboard, Bluetooth, my HDMI
   inputs, the TV's input and tuner framework, or anything
   else the TV needs to start. On Google TV or Chromecast,
   also never turn off Google TV's home screen
   (com.google.android.apps.tv.launcherx). If you're not
   sure, leave it on.
6. Install the home screen: download
   https://github.com/Ansub/tv-deto