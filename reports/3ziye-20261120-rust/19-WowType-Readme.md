<div align="center">

<img src="icons/hicolor/scalable/apps/wowtype.svg" width="112" alt="WowType 图标">

# WowType

**在 Linux 上打字，像微信输入法一样顺手。**

一个 fcitx5 拼音输入法：长句一次打完、打一半就有词、按错键也能认出来，越用越懂你。

[![CI](https://github.com/Gloridust/WowType/actions/workflows/ci.yml/badge.svg)](https://github.com/Gloridust/WowType/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Gloridust/WowType?include_prereleases&label=release)](https://github.com/Gloridust/WowType/releases)
![fcitx5](https://img.shields.io/badge/fcitx5-%E2%89%A5%205.0-blue)
![License](https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-green)

[安装](#安装) · [使用](#使用) · [设置](#设置) · [更多文档](#更多文档) · [常见问题](#常见问题) · [工作原理](#工作原理) · [参与开发](#参与开发)

[![加入 Telegram 交流群](https://img.shields.io/badge/%E5%8A%A0%E5%85%A5%20Telegram%20%E4%BA%A4%E6%B5%81%E7%BE%A4-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+Kxk-4VkXIS9lODM1)

<table>
<tr>
<td align="center" width="50%"><video src="https://github.com/user-attachments/assets/b9ee2854-3718-461b-a58c-0a0e72f78253" controls muted width="100%"></video></td>
<td align="center" width="50%"><video src="https://github.com/user-attachments/assets/9a6a6ea9-d3b3-4b7b-8d7b-fc5554c4a8c6" controls muted width="100%"></video></td>
</tr>
<tr>
<td align="center"><sub>介绍视频</sub></td>
<td align="center"><sub>v0.3.12：互译、语音输入、macOS 版、日期时间、候选更准……</sub></td>
</tr>
</table>

</div>

## 特性

<p align="center"><img src="docs/images/candidates.png" width="720" alt="在文本编辑器里打 hengxianghouxuanci：横排候选条，第一个是横向候选词，后面是横向、横向后选词……"><br>
<sub>候选横排，和微信输入法一样：整句只留几个，后面是词，最后是单字</sub></p>

- **整句输入**：`xiangquzijieshangban` 直接出「想去字节上班」；后面跟着句子的前半截，可以先上屏一段，剩下的拼音接着改。自带 WowType 自己训的整句增强模型（字级神经语言模型），长句的首选更准，开箱即用；也可以导入微信输入法的（[说明](docs/CONFIG.md#数据文件)）。
- **半成品也有词**：`zhongg` 就有「中国」，不用打全。打全了的拼音正好是个词时，它一定排第一。
- **按错键能认出来**：按成相邻键、两个键按反、多按或漏按一个键（`zhognguo` → 中国）。本来就打对的输入不受影响。
- **越用越懂你**：记住你选过的词和常连着用的词（选过一次「我们再讨论」，下次就不会出「我们在讨论」），30 天不用会慢慢淡掉。
- **简拼、省略韵母、中英混打**：`bjdx` → 北京大学；有的音节只打声母也行，`kyi` → 可以、`yongzwen` → 用中文；zh/ch/sh 可以当一个声母，`zhch`、`zhchi` → 支持；`github` → GitHub。
- **候选横排**，和微信输入法一样：整句只留几个，后面是词，最后是单字。
- **语音输入**：按住右 `Alt` 说话，松开就上屏；也可以点一下右 `Alt` 说，说完停一下自动结束。用微信输入法的离线识别模型，在本机识别，不上传录音。
- **Emoji**：打「开心」「点赞」「生日快乐」时，第三个候选就是对应的 emoji；按 `Super` + `.` 打开表情面板，打拼音或英文搜 emoji 和符号（`xiao` → 😂、`pizza` → 🍕、`youjiantou` → →）。
- **互译**：单按 `Shift` 切到「译」，照常打中文，停一下就翻成英文（或日、韩、法等 13 种语言），回车上屏；打外文就翻成中文。可以下载腾讯混元的 HY-MT 翻译模型离线翻，可以用哔哩哔哩免费的 Index-Translate（不用注册、不用 API Key），也可以填你自己的 OpenAI 格式接口（DeepSeek、通义千问、Ollama……）。
- **日期时间、计算器**：打 `riqi`（`rq`）、`shijian`（`sj`）、`xingqi`，首选后面就是今天的日期、现在的时间（`2026年11月10日`、`2026-11-10`、`15:52`……）；`v1+2*3` 直接出 `7`；只打一个数（`v12345.67`）出大写金额「壹万贰仟叁佰肆拾伍元陆角柒分」和「一万二千三百四十五点六七」。双拼时 `v` 是声母键，计算器用大写 `V`（`V1+2*3`）。
- **v + 空格工具栏**：只打一个 `v` 再按空格，选剪贴板历史（默认关，最近 20 条，只在内存里）、常用语（自定义词）、符号、表情。
- **中英文之间自动加空格**（默认关）：`你好Linux` → `你好 Linux`、`第5章` → `第 5 章`，字母和数字分别开关。
- **繁体、模糊音、双拼**：可切繁体输出；模糊音分 16 组单独开（z=zh、n=l、f=h、r=l、an=ang、un=ong、huang=wang……）；双拼支持自然码、小鹤、微软、搜狗、智能 ABC、紫光、拼音加加，双拼也有整句、句首词和分段选词，编辑区显示全拼。
- **五笔 86**：设置里「输入方案」选「五笔输入」。四码唯一自动上屏、第五码顶字、标点顶字、空码提示，候选后面显示还要打的码；不会打的字按 `z` 临时打拼音，候选后面就是它的五笔码。码表来自 [rime-wubi](https://github.com/rime/rime-wubi)，码位固定、不调频，见[五笔](#五笔)。
- **图形设置界面**：候选排列、模糊音、语音键都在「WowType 设置」里点一下就改，马上生效；还能加自定义词（人名、公司名、常用的长句、邮箱），加进去的词排第一，简拼也能打；编码可以是 `mail` 这类字母，词里能换行，可以导入导出。
- **打字统计**（默认关）：在设置的「统计」页打开后，看今天和累计的输入字数、活跃时长、速度、连续天数，以及每个键按了多少次（按键热力图）和候选命中位置。只在本机按天记计数，不记打的字、拼音、按键顺序和时刻，密码框里的不算；随时可以清除，见 [docs/CONFIG.md](docs/CONFIG.md#打字统计)。
- **快、全在本地**：完整的雾凇拼音词库，按一个键一般几毫秒内出候选；不联网，输入内容不离开你的电脑（语音模型在设置里下载一次；在线互译只在切到「译」时把那句话发给你选的服务）。

<table>
<tr>
<td align="center" width="50%">
<img src="docs/images/sentence-head.png" alt="打 xiangquzijieshangban 时的候选：想去字节上班、想去字节……"><br>
<b>长句一口气打完</b><br>
<sub>还能只上屏前半截「想去字节」，剩下的接着选</sub>
</td>
<td align="center" width="50%">
<img src="docs/images/typo.png" alt="打 weixni 时第一个候选是微信"><br>
<b>按错顺序，没关系</b><br>
<sub><code>weixni</code> 照样是「微信」</sub>
</td>
</tr>
<tr>
<td align="center">
<img src="docs/images/mixed-jianpin.png" alt="打 wanqky 时第一个候选是完全可以"><br>
<b>全简拼混打，也没问题</b><br>
<sub><code>wanqky</code> → 完全可以</sub>
</td>
<td align="center">
<img src="docs/images/english.png" alt="打 wechat 时第一个候选是 WeChat"><br>
<b>中英混打，不用切换</b><br>
<sub><code>wechat</code> → WeChat，大小写按词表来</sub>
</td>
</tr>
<tr>
<td align="center">
<img src="docs/images/emoji.png" alt="打 jintianhaokaixin 时第三个候选是开心😊"><br>
<b>打着字，顺手就有表情</b><br>
<sub>第三个候选是「开心😊」，选了上屏「今天好开心😊」</sub>
</td>
<td align="center">
<img src="docs/images/voice.png" alt="按住右 Alt 说话：光标变成声波，下面是正在听、离线和实时波形"><br>
<b>按住右 Alt 说话</b><br>
<sub>离线识别，录音不上传</sub>
</td>
</tr>
</table>

## 安装

### 系统要求

- Linux x86_64 或 arm64（aarch64），输入法框架 **fcitx5 5.0 或更新**。Arch 的安装包只有 x86_64
- 有现成安装包的发行版：**Ubuntu 22.04 / 24.04 / 26.04、Debian 13、deepin 23 / 25**（deb）、**Arch Linux** 及 EndeavourOS / Garuda / CachyOS（pkg.tar.zst）、**Fedora**（[rpm](#fedora)）、**NixOS**（[flake](#nixos--nix)）。其他发行版请[从源码构建](docs/INSTALL.md)
- Ubuntu 22.04 的 GNOME 是 42：绿色候选框主题和语音浮条（GNOME 扩展，要 GNOME 45+）用不了，见[安装说明](docs/I