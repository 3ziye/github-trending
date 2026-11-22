# google-pro

简体中文 | [English](README.en.md)

> **更新**：新增傻瓜式向导，Mac 双击 `start.command`、Windows 双击 `start.bat` 即可，主开 **AI Pro 5TB**（入口 `pro.py`）；没有安卓手机可以用 MuMu 模拟器。Ultra 目前开不出来（offer 已下架 / 账号被判地区不支持）。

Google One 的 **AI Pro（5 TB）** 有一批免费试用 offer，任何页面上都看不到，只存在于 Play 结算库（BillingClient）的返回值里。这个脚本把「查 offer → 拉起 Play 收银台 → 确认 0 元 → 开通」串成一条命令。

原理是借 Google One 自己的进程调 BillingClient，不需要 Xposed，不需要改 APK。

## 能拿到什么

~~拿到的是 **Ultra 5x，20TB，12 个月 $0**，到期前取消就不用付钱。开通后 Play 订阅页会写「即将扣款 2027-11-17 US$99.99/月」，这是试用结束后的价格，不是现在扣。~~

~~30TB 那档（20x）也查得到 offer，但 Play 结算时会二次校验，大部分号会弹「您不符合免费试用条件」。这个脚本不会去点它。~~

（Ultra 的试用 offer 已下架，脚本保留但暂时开不出来）

当前有效的是 **AI Pro 5TB，12 个月 $0**，到期前取消就不用付钱。

```
商品  g1.2tb.ai.subs_variant
offer 12months-eft
首期  0 元 / P1Y
之后  US$19.99/月
```

12 个月那条在某些号上会被判「已订阅」（这个 SKU 是历史映射），脚本会自动退到三个月那条：

```
商品  g1.play.2tb.ai
offer eft-3mo
首期  0 元 / P3M
```

两条都拿不到，就是号不符合资格，换号。

### 商品与 offer 对照

| 档位 | 商品 | offer | 首期 | 之后 |
|---|---|---|---|---|
| ~~Ultra 20TB~~ | ~~g1.play.20tb~~ | ~~eft-12month~~ | ~~0 / P1Y~~ | ~~US$99.99/月~~ |
| ~~Ultra 30TB~~ | ~~g1.play.ai.pro~~ | ~~eft-12mo~~ | ~~0 / P1Y~~ | ~~—~~ |
| **AI Pro 5TB** | g1.2tb.ai.subs_variant | 12months-eft | 0 / P1Y | US$19.99/月 |
| **AI Pro 5TB** | g1.play.2tb.ai | eft-3mo | 0 / P3M | US$19.99/月 |

Ultra 两行已下架，仅保留备用；脚本默认只开 AI Pro。

## 三个硬条件

试过几十个号，能开的号必须同时满足：

| 条件 | 不满足会怎样 |
|---|---|
| Play 国家已设置（美国） | Google One 直接打不开，提示「此账号无法使用 Google One」 |
| 已绑付款方式 | 收银台拉不起来 |
| 从没订阅过任何 Google One 方案 | 弹「您已订阅」，即使订阅页是空的 |

第三条最坑：Play 记的是历史，不是当前状态。用过的号永久失去资格。

## 两个版本

**简单版**：一个网页，双击 `web/index.html` 打开，登录 → 绑卡 → 点一下，完事。不用装 Python，不用 root，不用数据线。

**脚本版**：`pro.py`，要一台 root 手机和 frida。优点是 offer 从真实客户端取，不依赖浏览器指纹。

先试简单版，不行再上脚本。

## 需要什么

一台 root 过的安卓手机，USB 连着电脑。Magisk、KernelSU、APatch 都行。

**没有手机就用 MuMu 模拟器。** Windows 装 MuMu Player 12，Mac 装 MuMu Pro（需 Apple Silicon），在设置里打开「ROOT 权限」并重启。向导会自动用 adb 连上它，frida-server 按模拟器架构自动选（MuMu-Windows 是 x86_64，MuMu-Mac 是 arm64），后面的流程和真机一样。

电脑上要 Python 3.9 以上，外加两个包：

```bash
pip3 install frida
```

adb 用 Android SDK 里的 platform-tools。装好后 `adb devices` 能看到手机就行。没装过的话，Mac 上 `brew install android-platform-tools`，Windows 去下 platform-tools 压缩包，解压后把目录加进 PATH。

手机上要开「开发者选项 → USB 调试」，插上后在弹窗里点允许。

## 用法

### 最简单：双击启动（不碰命令行）

Mac 双击 `start.command`，Windows 双击 `start.bat`，会打开一个向导：自动检查环境 → 粘账号 → 逐个开通 → 终端里出一张结果表格，最后打印报告目录。没有安卓手机也行，向导第一步会带你连 MuMu 模拟器。向导菜单最后一项（或 `--advanced`）退回下面的命令行用法。

### 简单版怎么用

源码在 `web/index.html`，单文件，下载后双击就能用，浏览器会打开一个页面：

1. 点「去登录」，用要开的谷歌账号登进去
2. 点「去绑卡」，绑一张卡，卡里留 1 美元就行，试用期间不扣
3. 回页面，点对应的套餐卡片

跳到 Google 的结算页之后，确认金额是 0，点订阅即可。

### 脚本版怎么用

先自检一遍环境，它会检查设备、root、frida-server、推送计费模块，还会顺手关掉会拦截 Play 网络的代理和 Clash：

```bash
python3 pro.py --check
```

全绿就可以跑号了。

账号写成一个文本文件，一行一个，字段用四个短横线隔开：

```
邮箱----密码----辅助邮箱----2FA密钥----卡号----有效期----CVC----持卡人----邮编
```

后面几项留空也行。刚买的新号一般没有 2FA，那就留空：

```
abc123@gmail.com----mypassword----
```

带卡的话：

```
abc123@gmail.com----mypassword--------4242424242424242----10/29----326----ZHANG SAN----97201
```

地址不填会默认用 `123 Main St, Portland, OR 97201`，俄勒冈免消费税。

跑：

```bash
python3 pro.py accounts.txt
```

单个号也可以：

```bash
python3 pro.py --account "abc@gmail.com:密码:2FA密钥"
```

`ultra0.py` 是同一套代码，参数一致；`pro.py` 只是把 `--plan pro` 设成默认。

想看结果，开订阅页确认一下：

```
Play 商店 → 头像 → 付款和订阅 → 订阅
```

## 它内部干了什么

1. 把账号加到手机（没有就加，有就跳过）
2. 切 Play 账号。切完一定从头像面板读回来核对，对不上直接退出，不会跑到别的号上
3. 启动 Google One，用 Frida 挂进去，`DexClassLoader` 加载计费模块
4. `queryProductDetailsAsync` 查 `g1.2tb.ai.subs_variant`、`g1.play.2tb.ai`、`g1.2tb.ai` 三个商品
5. 挑免费期最长的那个（`12months-eft`，P1Y），在主线程调 `launchBillingFlow`
6. 盯着收银台。看到价格是 0 或者「免费试用 12 个月」才点订阅；看到「不符合免费试用条件」就关掉，绝不点
7. Play 有时会要求重新输密码，脚本自己填
8. 打开订阅页核对，结果写进 `ultra0-report/`

## 失败的时候是什么情况

**账号不符合资格。** Play 会说「您不符合免费试用条件，尽管如此，您仍能订阅」。一个号基本只有一次机会：试用一旦发起过，哪怕没确认，offer 也会消失。所以别拿主力号试。

**没有付款方式。** 订阅必须有卡。Play 的加卡页是 WebView，adb 填不进去，脚本会停下来提示你在手机上填完再按回车。每台设备手动绑一次，之后所有号共用这张卡。

**Play 账号没切过来。** 脚本会打印当前实际登录的是哪个号，然后退出。这时手动在 Play 里切一下，加上 `--no-switch` 重跑，让它只做校验不再尝试切换：

```bash
python3 pro.py accounts.txt --no-switch
```

**收银台没弹出来。** 重跑一次。连续两次都不弹，检查一下设备的网络：`settings get global http_proxy`，不是 `null` 就清掉；Clash 这类 VPN 会劫持 DNS，也会让 Play 连不上。

## 一些参数

```bash
--plan pro     # 默认，只查 AI Pro 5TB
--plan 5x      # 查 Ultra 20TB（已下架，仅备用）
--plan 20x     # 查 Ultra 30TB（已下架，仅备用）
--no-add       # 账号已经在手机上，跳过加号
--no-switch    # 不自动切账号，只校验当前账号
```

## 几个说明

试完之后记得去 Play 里取消订阅，不然到期会扣 $99.99。

脚本只在本地跑，账号密码和卡号不联网，也不上传任何地方。报告文件在 `ultra0-report/`，里面有 offer 明细和每步结果。

这段代码只对 Play 结算流程里「客户端能拿到试用 offer」这件事做了利用，没有改任何服务端数据。

## 交流

技术讨论群，随便进一个。**进群前先看[群规则](RULES.md)：禁止一切广告，违者移出。**

<table>
<tr>
<td align="center"><b>11 群</b><br><img src="assets/wechat-group11.jpg" width="220" alt="11 群"></td>
<td align="center"><b>12 群</b><br><img src="assets/wechat-group12.png" width="220" alt="12 群"></td>
<td align="center"><b>13 群</b><br><img src="assets/wechat-group13.png" width="220" alt="13 群"></td>
</tr>
<tr>
<td align="center"><b>14 群</b><br><img src="assets/wechat-group14.png" width="220" alt="14 群"></td>
<td align="center"><b>15 群</b><br><img src="assets/wechat-group