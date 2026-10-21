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

[![The Verge](https://img.shields.io/badge/The_Verge-5200FF?style=for-the-badge)](https://www.theverge.com/ai-artificial-intelligence/1013505/maybe-claude-make-your-android-tv-less-crappy-too)
[![Android Authority](https://img.shields.io/badge/Android_Authority-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://www.androidauthority.com/android-tv-vibe-hacking-remove-ads-bloatware-3725338/)
[![Mashable](https://img.shields.io/badge/Mashable-00AEEF?style=for-the-badge)](https://mashable.com/tech/smart-tv-ads-claude-code-ai-cleanup)
[![t3n](https://img.shields.io/badge/t3n-E6007E?style=for-the-badge)](https://t3n.de/news/claude-alter-fernseher-android-tv-1768831/)
[![Tom's Guide](https://img.shields.io/badge/Tom's_Guide-E1261C?style=for-the-badge)](https://www.tomsguide.com/ai/people-are-using-ai-to-turn-their-smart-tvs-into-dumb-tvs-and-you-might-want-to-do-the-same)

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

> [!WARNING]
> **Google TV and Chromecast with Google TV:** don't turn off the TV's own home screen. On some of these devices that left them stuck restarting, and the only fix was a factory reset. Since v1.4.1, `install.sh` leaves it on for Google TV unless you opt in with `GOOGLE_TV=1`. The cleanup still works and makes the TV faster. You just keep Google TV's own home screen.

> [!WARNING]
> **OLED TVs:** keep the screensaver on. It stops a still picture from burning into the screen. Don't leave any home screen, this one included, on for hours.

**1. Turn on developer mode on the TV.**
Settings → Device Preferences → About → press **Build** 7 times. Then turn on **USB debugging** in **Developer options**. [Stuck?](#help)

**2. Open [Claude Code](https://claude.com/claude-code) or [Codex](https://openai.com/codex) on your laptop.**
The laptop and TV must be on the same Wi-Fi.

**3. Paste this in.**

```text
Help me clean up my Android TV and make it faster.
My TV is a <brand and model>.

1. Connect to my TV over Wi-Fi. Walk me through anything
   I need to tap on the TV.
2. Before changing anything, list every app in plain English:
   safe to turn off, needed by the TV, and apps I use.
   Check free memory.
3. Ask me before every change. Turn apps off instead of
   deleting them. Keep a list of what you changed and how
   to undo it.
4. Never turn off: Google Play services
   (com.google.android.gms), Google Play, Settings,
   System UI, setup apps, the keyboard, Bluetooth, my HDMI
   inputs, the TV's input and tuner framework, or anything
   else the TV needs to start. On Google TV or Chromecast,
   also never turn off Google TV's home screen
   (com.google.android.apps.tv.launcherx). If you're not
   sure, leave it on.
5. Install the home screen: download
   https://github.com/Ansub/tv-detox and run its
   install.sh with my TV and these apps: <your apps>.
6. Turn off animations and make the TV sleep after 5
   minutes. Then check the model name and ask me if the TV
   is OLED. Keep the screensaver on unless I say it's not
   OLED.
7. Wait 30 seconds after the last change, then restart the
   TV once and check it starts up normally before you say
   you're done. Show me free memory before
   and after.
```

That's it. It asks you before every change.

> [!NOTE]
> This is what worked for us, not professional advice. Use it at your own risk. You're responsible for your own TV, and I'm not l