<div align="center">

<img src="public/brand/folkbench-logo-only.svg" width="64" height="64" alt="Folkbench">

# Folkbench

中转站实测评测，与 Folkbench Switch。

[![Release](https://img.shields.io/github/v/release/Folkbench/folkbench?include_prereleases&label=release&color=7624f4&style=for-the-badge)](https://github.com/Folkbench/folkbench/releases) [![Stars](https://img.shields.io/github/stars/Folkbench/folkbench?color=f5a623&logo=github&style=for-the-badge)](https://github.com/Folkbench/folkbench/stargazers) [![folkbench.com](https://img.shields.io/badge/folkbench.com-533afd?style=for-the-badge&logo=googlechrome&logoColor=white)](https://folkbench.com/?utm_source=github&utm_campaign=readme_badge) [![Telegram](https://img.shields.io/badge/Telegram-2BA2E0?logo=telegram&logoColor=white&style=for-the-badge)](https://t.me/+-h3yj4eOYmw0ZTNl) [![Group](https://img.shields.io/badge/Group-12B7F5?logo=qq&logoColor=white&style=for-the-badge)](https://qm.qq.com/q/71NzSTrPVK)

[🌐 在线评测大盘](https://folkbench.com/rankings/board?utm_source=github&utm_campaign=readme) · [⚡ Switch 客户端](#folkbench-switch) · [📦 下载安装](https://github.com/Folkbench/folkbench/releases) · [🔥 热门模型](#热门模型) · [💬 交流群 (TG)](https://t.me/+-h3yj4eOYmw0ZTNl) · [💬 QQ 群](https://qm.qq.com/q/71NzSTrPVK) · [English](README.en.md) · [日本語](README.ja.md) · [Español](README.es.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/hero-dark.png">
  <img src="docs/images/hero-light.png" width="100%" alt="Folkbench 中转站榜单与 Switch 客户端">
</picture>

</div>

<br>

[folkbench.com](https://folkbench.com/?utm_source=github&utm_campaign=readme) 持续测试各家 AI 中转站，公开可用率、响应耗时和价格。本仓库是配套桌面客户端 **Folkbench Switch** 的代码，用来把选好的线路写入 Claude Code、Codex 等工具的配置。

---

## 赞助商

以下中转站支持 Folkbench 的持续评测。[成为赞助商 →](https://folkbench.com/vendor/login?utm_source=github&utm_campaign=readme)

<!-- 顶级赞助位预留：确定档位后在此放置单独一行大 Logo / Reserved for a top-tier sponsor once tiers exist -->

<!-- /go 跳转上线前的原始链接 / Original links before /go went live:
     Modelflare: https://modelflare.dev/sign-up?partner=TDN1QM6KKYX9&utm_source=folkbench&utm_medium=referral&utm_campaign=folkbench-blog-readme
     CheapAI: https://cheapai.info/sign-up?aff=TkeF&utm_source=folkbench&utm_medium=referral&utm_campaign=folkbench-blog-readme
     IKunCode: https://api.ikuncode.cc/sign-up?aff=QgPu&utm_source=folkbench&utm_medium=referral&utm_campaign=folkbench-blog-readme
     智流 FluxLane: https://folkbench.com/services/fluxlane?utm_source=github&utm_campaign=readme
-->

<table>
<tr>
<td width="200" align="center"><a href="https://folkbench.com/go/modelflare?source=readme"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/sponsors/modelflare-dark.png"><img src="docs/images/sponsors/modelflare-light.png" alt="Modelflare" width="180"></picture></a></td>
<td><a href="https://folkbench.com/go/modelflare?source=readme"><b>Modelflare</b></a><br>Modelflare站点是由美国 Havenbyte LLC 运营，支持 GPT、Claude、Gemini、Grok 等主流模型和常用兼容协议，同时也支持 40 多种图片及视频模型。API Key 可以配置有序回退，一把 API Key 可以调用多个模型，Key 还可以设置备用分组，并且从请求日志里能看到状态、延迟、Token 和实际费用。<br><br>缓存补偿是这个站的另一个亮点：部分 OpenAI 价格优先、稳定和高级分组分别提供每日 65%、75%、85% 的缓存命中率保障，对于符合条件的api请求如果未达到缓存命中率，平台会给予对应补充。<br><br>站点目前也有首次充值解锁特惠分组的活动，单笔充值 US$20 后可解锁 GPT 特惠分组，解锁后 GPT-5.6-Sol 的价格大约是 ¥0.51（输入）/ ¥3.01（输出）/每百万 Token，并且没有使用上限限制。单笔充值 US$50 后可解锁 Claude 特惠分组。</td>
</tr>
<tr>
<td width="200" align="center"><a href="https://folkbench.com/go/cheapai?source=readme"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/sponsors/cheapai-dark.png"><img src="docs/images/sponsors/cheapai-light.png" alt="CheapAI" width="180"></picture></a></td>
<td><a href="https://folkbench.com/go/cheapai?source=readme"><b>CheapAI</b></a><br>CheapAI字如其名，主打一个便宜，可以重点看特惠分组，价格确实压得很低。而且还有一个很有意思的动态倍率分组。按客服的介绍，这个分组会根据实时号池情况调整倍率。资源充足的时候价格可以更低，资源紧张时则会相应调整，在价格和可用性之间实时做一个平衡。<br><br>对于追求性价比的用户可以选择它们家折扣倍率较好的特惠分组，而对于追求稳定的用户可以选择稳定分组或 Pro 分组，站点也提供官 key 分组，能够覆盖不同使用需求。</td>
</tr>
<tr>
<td width="200" align="center"><a href="https://folkbench.com/go/ikuncode?source=readme"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/sponsors/ikuncode-dark.png"><img src="docs/images/sponsors/ikuncode-light.png" alt="IKunCode" width="180"></picture></a></td>
<td><a href="https://folkbench.com/go/ikuncode?source=readme"><b>IKunCode</b></a><br>IKunCode对于各个编程工具接入的支持比较好，Claude Code、Codex 和 Gemini CLI 都有单独支持，售后以及咨询渠道渠道做得比较全，官网公开了客服邮箱、QQ 群和 Telegram，人工客服服务贴心，很适合新手上路。</td>
</tr>
<tr>
<td width="200" align="center"><a href="https://folkbench.com/go/fluxlane?source=readme"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/images/sponsors/fluxlane-dark.png"><img src="docs/images/sponsors/fluxlane-light.png" alt="智流 FluxLane" width="180"></picture></a></td>
<td><a href="https://folkbench.com/go/fluxlane?source=readme"><b>智流 FluxLane</b></a><br>智流 FluxLane 的模型和线路比较多，国内外模型都有，接入方式也比较统一，直接兼容 OpenAI SDK。除了模型和线路比较全，它还把路由、用量、成本和延迟这些东西都做进了平台里，比较适合开发者和团队长期接入。对于企业和高校采购这方面是比较明显的优势，可以提供发票、合同、采购单。</td>
</tr>
</table>

---