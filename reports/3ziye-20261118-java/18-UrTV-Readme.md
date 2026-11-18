<p align="center"><img src=".github/brand/hero.png" alt="تلفزيونك · UrTV" width="100%"></p>

<h1 align="center">تلفزيونك · UrTV</h1>

<p align="center" dir="rtl">واجهة رئيسية عربية وشاشة توقف سعودية لتلفزيونات Android TV و Google TV، وتسريع آمن للتلفزيون.<br>تركّبها من التلفزيون نفسه بزر واحد، أو من جوالك أو كمبيوترك.</p>

<p align="center">An Arabic home screen and a Saudi screensaver for Android TV / Google TV, and a safe speed-up.<br>Set it up from the TV itself with one button, or from your phone or computer.</p>

<p align="center">
  <a href="https://github.com/tshi-dev/UrTV/releases/latest"><img src="https://img.shields.io/badge/Download-APK-2ea043?style=for-the-badge&logo=android&logoColor=white" alt="Download APK" height="40"></a>
  &nbsp;
  <img src="https://img.shields.io/badge/Downloader_code-9378345-c9a227?style=for-the-badge" alt="Downloader code 9378345" height="40">
</p>

<p align="center">
  <a href="https://github.com/tshi-dev/UrTV/releases/latest"><img src="https://img.shields.io/github/v/release/tshi-dev/UrTV?display_name=release&label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/tshi-dev/UrTV" alt="MIT licence"></a>
  <a href="https://github.com/tshi-dev/UrTV/stargazers"><img src="https://img.shields.io/github/stars/tshi-dev/UrTV?style=flat" alt="Stars"></a>
  <img src="https://img.shields.io/badge/Android_TV-8%2B-3ddc84?logo=android&logoColor=white" alt="Android TV 8 and newer">
</p>

<p align="center"><a href="#التثبيت-اختر-طريقة">العربية</a> | <a href="#install-pick-a-way">English</a></p>

<p align="center"><img src=".github/screens/before-after-home.jpg" alt="Before: Google TV home. After: the تلفزيونك home screen" width="100%"></p>
<p align="center"><img src=".github/screens/before-after-screensaver.jpg" alt="Before: the Google screensaver. After: شاشة تلفزيونك" width="100%"></p>

<div dir="rtl">

## التثبيت: اختر طريقة

| الطريقة | تحتاج | المدة |
|---|---|---|
| **① التلفزيون وحده** (الأسهل) | التلفزيون والريموت | ١٠–٢٠ دقيقة |
| **② من جوال** أندرويد أو آيفون | جوال على نفس الواي فاي | مثل الكمبيوتر (الآيفون أبطأ) |
| **③ من كمبيوتر** | كمبيوتر على نفس الواي فاي ومساعد ذكي | ٤٠ دقيقة |

> **مهم:** تثبيت التطبيق وحده **ما يخلّيه الشاشة الرئيسية**. اللي يحوّل التلفزيون ويسرّعه هو **الإعداد** («جهّز كل شي» أو الأوامر)، وتقدر ترجع كل شي مثل ما كان بأي وقت.

### ① التلفزيون وحده
1. **فعّل التصحيح:** الإعدادات ← تفضيلات الجهاز ← حول ← اضغط OK على **Build** سبع مرات، ثم **خيارات المطوّر** ← شغّل **تصحيح USB**.
2. **ثبّت تطبيق Downloader** من متجر التلفزيون، واكتب فيه الرمز **9378345** ← **تثبيت** (اسمح له بتثبيت التطبيقات لو سألك).
3. **افتح «إعداد تلفزيوني»** من صف التطبيقات ← اضغط **«جهّز كل شي»**.
4. التلفزيون يسألك «السماح بتصحيح USB؟» ← **السماح دائماً**. تطلع لك الخطة بأرقام تلفزيونك قبل أي تغيير ← **«ابدأ»**، وخلّه يكمل (يعيد التشغيل مرتين ويكمل وحده).

| الشاشة الأولى | الخطة قبل أي تغيير | النهاية |
|---|---|---|
| <img src="docs/shots/setup/after/glass-ar-start.png" alt="«جهّز كل شي»" width="260"> | <img src="docs/shots/setup/after/glass-ar-plan.png" alt="الخطة" width="260"> | <img src="docs/shots/setup/after/glass-ar-done.png" alt="تم" width="260"> |

### ② من جوال أندرويد أو آيفون
- **التلفزيون:** فعّل التصحيح مثل الخطوة ١ فوق.
- **أندرويد:** ثبّت **Termux** وشغّل نفس أوامر الكمبيوتر من الجوال.
- **آيفون / آيباد:** ثبّت **iSH** (أبطأ).
- الخطوات كاملة: [`docs/PHONE-SETUP.md`](docs/PHONE-SETUP.md).

### ③ من كمبيوتر (مع مساعد ذكي)
1. **التلفزيون:** فعّل التصحيح مثل الخطوة ١ فوق.
2. **الكمبيوتر**، على نفس الواي فاي، وعليه واحد من هذي:

| **Codex** (OpenAI) | **Claude Code** (Anthropic) |
|---|---|
| مجاني بحساب ChatGPT | يحتاج اشتراك Claude Pro (20$ بالشهر) |
| حمّل تطبيق Codex | حمّل تطبيق Claude ← تبويب **Code** |
| الموافقات: اختر **«Approve for me»** | الموافقات: **Allow** للمهمة كلها |

<sub>ويندوز: ركّب Git وPython أول (`winget install --source winget Git.Git Python.Python.3.12`). Gemini CLI مجاني وناس قالوا يشتغل؛ ما جرّبناه.</sub>

3. **الصق هذا:**

> ركّب تلفزيوني من https://github.com/tshi-dev/UrTV: انسخ المستودع واتبع `docs/SETUP-PROMPT.md` خطوة بخطوة. أنت على كمبيوتر متصل بنفس شبكة الواي فاي حقت التلفزيون.

### بعد التثبيت
- **وش يصير بعد اللصق؟** يسألك عن مدينتك وأنديتك، والتلفزيون يسألك «السماح» مرة، وبعدها خلّه يشتغل.
- **بترجعه مثل ما كان؟** نعم بأي وقت: زر «تراجع» في «إعداد تلفزيوني»، أو `optimize/reset.sh`.
- **نزلت نسخة جديدة؟** «تحديث تلفزيوني» من التلفزيون (ضغطة طويلة على أي تطبيق)، وإعداداتك باقية.
- **تحديث للنظام وقف تطبيقنا؟** أعد الإعداد: «جهّز كل شي» أو `optimize/run.sh again`.

## وش فيه
- **الشاشة الرئيسية «تلفزيونك»:** عربية ونظيفة، مفضلتك، المهام، تلاوة وأذان، والمباريات.
- **شاشة التوقف:** الساعة والهجري ومواقيت الصلاة والإقامة، ومبارياتك، والطقس، والأسواق، وصور سعودية أو صورك.
- **تلاوة وأذان:** ٤٢ قارئاً، والإذاعات، والأذان بتوقيت أم القرى (٢١ أذاناً).
- **«تلفزيونك»:** افتح التطبيق وتدخل الأسواق أو المباريات أو الألعاب أو الإعدادات بضغطة.
- **ثماني ألعاب عائلية:** «الأسرع» من الجوالات،