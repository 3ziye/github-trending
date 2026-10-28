<p align="center"><img src=".github/brand/hero.png" alt="تلفزيونك · UrTV" width="100%"></p>

<h1 align="center">تلفزيونك · UrTV</h1>

<p align="center" dir="rtl">واجهة رئيسية عربية وشاشة توقف سعودية لتلفزيونات Android TV و Google TV، وتسريع آمن للتلفزيون.<br>يركّبها لك مساعد ذكاء اصطناعي بأمر واحد.</p>

<p align="center">An Arabic home screen and a Saudi screensaver for Android TV / Google TV, and a safe speed-up.<br>Your AI agent sets it all up.</p>

<p align="center"><img src=".github/screens/before-after-home.jpg" alt="Before: Google TV home. After: the تلفزيونك home screen" width="100%"></p>
<p align="center"><img src=".github/screens/before-after-screensaver.jpg" alt="Before: the Google screensaver. After: شاشة تلفزيونك" width="100%"></p>

<div dir="rtl">

## ركّبه في 3 خطوات

### ① التلفزيون
الإعدادات ← حول ← اضغط OK على **Build** سبع مرات. بعدها روح إلى **خيارات المطوّر** ← شغّل **USB debugging**.

### ② كمبيوتر على نفس الواي فاي، وعليه واحد من هذي

| **Codex** (OpenAI) | **Claude Code** (Anthropic) |
|---|---|
| مجاني بحساب ChatGPT | يحتاج اشتراك Claude Pro (20$ بالشهر) |
| حمّل تطبيق Codex | حمّل تطبيق Claude ← تبويب **Code** |
| الموافقات: اختر **«Approve for me»** | الموافقات: **Allow** للمهمة كلها |

<sub>ويندوز: ركّب Git وPython أول (`winget install --source winget Git.Git Python.Python.3.12`). Gemini CLI مجاني وناس قالوا يشتغل؛ ما جرّبناه.</sub>

### ③ الصق هذا

> ركّب تلفزيوني من https://github.com/tshi-dev/UrTV: انسخ المستودع واتبع `docs/SETUP-PROMPT.md` خطوة بخطوة. أنت على كمبيوتر متصل بنفس شبكة الواي فاي حقت التلفزيون.

#### وش يصير بعد اللصق؟
يسألك عن **مدينتك** و**أنديتك**، والتلفزيون يسألك **Allow** مرة وحدة، وبعدها خلّه يشتغل: 40 دقيقة وكم إعادة تشغيل.

#### بترجعه مثل ما كان؟
نعم، بأي وقت: تطبيقاتنا تنحذف، واللي أطفأناه يرجع، وشاشة التلفزيون الأصلية ترجع.
<sub>`optimize/reset.sh`</sub>

#### نزلت نسخة جديدة؟
حدّث التطبيقين وإعداداتك كلها باقية. الشاشة نفسها تتحدّث لحالها. آخر الإعدادات، تحت «تحديث الشاشة الآن»، ثلاثة أسطر: الإصدار الحالي، والإصدار المتاح، وطريقة التحديث.
<sub>`optimize/install.sh all`</sub>

#### نزل تحديث للنظام وقفل تطبيقنا؟
أعد الإعداد كله بأمر واحد، وإعداداتك باقية.
<sub>`optimize/run.sh again`</sub>

</div>

## Set it up in 3 steps

### ① The TV
Settings → About → press OK on **Build** 7 times. Then go to **Developer options** → turn on **USB debugging**.

### ② A computer on the same Wi-Fi, with one of these

| **Codex** (OpenAI) | **Claude Code** (Anthropic) |
|---|---|
| Free with a ChatGPT account | Needs Claude Pro ($20/month) |
| Download the Codex app | Download the Claude app → **Code** tab |
| Approvals: choose **«Approve for me»** | Approvals: **Allow** for the whole task |

<sub>Windows: install Git and Python first (`winget install --source winget Git.Git Python.Python.3.12`). Gemini CLI is free and reported to work; not tested by us.</sub>

### ③ Paste this

> Set up my TV with https://github.com/tshi-dev/UrTV: clone it and follow `docs/SETUP-PROMPT.md` step by step. You are on a computer on the same Wi-Fi as the TV.

#### What happens after pasting?
It asks your **city** and your **clubs**, the TV asks **Allow** once, then leave it: 40 minutes, a few restarts.

#### Can I put it back as it was?
Yes, anytime: our apps are removed, what we turned off comes back on, the TV's own screen returns.
<sub>`optimize/reset.sh`</sub>

#### A new version came out?
Update both apps; all your settings stay. The screen itself updates on its own. The settings row tells you when one exists.
<sub>`optimize/install.sh all`</sub>

#### The TV updated its system and locked our app out?
Redo the whole setup with one command, settings kept.
<sub>`optimize/run.sh again`</sub>

**Safe:** nothing is uninstalled; AirPlay, Chromecast and voice are never touched; a 5-minute safety switch puts the
stock home back if ours doesn't come up. The apps are built and signed by GitHub Actions from this repo (version
3.N = the build number). The full prompt: [docs/SETUP-PROMPT.md](docs/SETUP-PROMPT.md). To build a different
screen: [docs/RECREATE-PROMPT.md](docs/RECREATE-PROMPT.md).

## What you get

| | | |
|---|---|---|
| **شاشة تلفزيونك** · screensaver | Clock, Hijri date, prayer times and iqama, Ramadan, your teams' matches, weather, markets, and beside the clock your choice of new episodes, today's prayers, the 5-day forecast, all your teams' games, a stock watchlist, or a verse/hadith of the day, over Saudi landscapes | `urtv-screensaver.apk` |
| **تلفزيونك** · home screen | Clean Arabic launcher: favourites row (5–10 apps) arranged in «ترتيب المفضلة», all apps, inputs, Wi-Fi, settings; «المهام» (tasks, by voice too), optional card from the screensaver (off by default). The «تلاوة» pill opens the Quran and the radio, with the adhan at Umm al-Qura times. App names show in Arabic: the name the setup agent gave it on this TV (`optimize/dock.sh names` / `name`), else the app's own Arabic name, else the one in `res/values/app_names.xml`, else its own name | `urtv-home.apk` |
| **Two free