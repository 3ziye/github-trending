### 🚀[am-cf-tunnel-sub](https://github.com/amclubs/am-cf-tunnel-sub)
基于Vercel、Cloudflare部署该脚本，你可以方便地将Cloudflare Workers 和 Pages的 VLESS、Trojan 配置信息使用在线配置转换到 Clash、 Singbox 、Quantumult X等工具中订阅使用。Cloudflare Workers 和 Pages 生成VLESS、Trojan节点,实现一键订阅节点。分离节点与订阅框架,更好解决Cloudfare部署时出现1101、522的问题。 [最新视频教程](https://www.youtube.com/watch?v=i-XnnP-MptY&t=596s)、[🎬 YouTube](https://youtube.com/@am_clubs?sub_confirmation=1)、 [💬 Telegram](https://t.me/am_clubs)、[📂 GitHub](https://github.com/amclubs)、[🌐 Blog](https://amclubss.com)

### ⚙️结合Coudflare部署免费节点项目 [am-cf-tunnel](https://github.com/amclubs/am-cf-tunnel) 与教程使用 [视频教程](https://youtu.be/i-XnnP-MptY)
- 本频道订阅器转换地址：https://sub.amclubss.com

### 👉 后期计划
- 增加在线自动优先IP功能
- 增加其它更多免费容器部署

##
### 📝一、前期准备资料
<details>
<summary>点击展开/收起</summary>

### 1、注册免费**Vercel**帐号(GitHub方式连接就可以注册)
- 注册地址：https://vercel.com <a href="https://www.youtube.com/watch?v=ZxHLLlxuJyI&t=50s">[点击观看视频教程]</a>

### 2、注册**免费域名** [点击观看所有免费域名视频教程](https://www.youtube.com/playlist?list=PLGVQi7TjHKXZGODTvB8DEervrmHANQ1AR)

### 3、**订阅工具** [点击观看使用视频教程](https://youtu.be/xGOL57cmvaw)
👉 [点击加入TG群 数字套利｜交流群](https://t.me/AM_CLUBS)发送关键字 **工具** 获取下载

### 4、Cloudflare标准 **端口** 知识  [点击观看优选IP视频教程](https://youtu.be/pKrlfRRB0gU)
- 80系端口(HTTP)：80，8080，8880，2052，2082，2086，2095
- 443系端口(HTTPS)：443，2053，2083，2087，2096，8443
- [IP落地测试工具地址](https://ip.sb/)

### 4、结合loudflare部署免费节点项目与教程使用 [am-cf-tunnel](https://github.com/amclubs/am-cf-tunnel)

</details>

##
### ⚙️ 二、部署节点订阅器 [视频教程](https://www.youtube.com/watch?v=i-XnnP-MptY&t=596s)

<details>
<summary>点击展开/收起</summary>

#### `①` Vercel方式部署 [视频教程](https://www.youtube.com/watch?v=i-XnnP-MptY&t=596s)
1. Fork或克隆本仓库[am-cf-tunnel-sub](https://github.com/amclubs/am-cf-tunnel-sub)到您的 GitHub/GitLab 账户
2. 登录 [Vercel](https://vercel.com)，点击"New Project" <a href="https://www.youtube.com/watch?v=ZxHLLlxuJyI&t=28s">[点击观看注册视频教程]</a>
3. 导入您的仓库，使用默认设置
4. **⚠️ 重要：在"Settings" > "Environment Variables"中添加 `UUID` 和 `HOST` 变量（必须设置）**
5. 点击"Deploy"

访问 `http://部署域名` 即可。

#### `②` Cloudfare方式部署（Pages GitHub）
1. 部署 Cloudflare Pages：
   - 在 Github 上先 Fork 本项目[am-cf-tunnel-sub](https://github.com/amclubs/am-cf-tunnel-sub)，并点上 Star !!!
   - 在 CloudFlare主页的左边菜单的 `计算(Workers)` 选项卡 -> 点击 `Workers 和 Pages` -> 右上方点击 -> `创建应用程序` -> 选择 `Pages`里的 `导入现有 Git 存储库` 点击 `开始使用` -> 选择GitHub 点击`连接GitHub`根据提示授权GitHub和项目(此步已有可忽略)后 -> 选中 `am-cf-tunnel-sub`项目后 -> 点击 `开始设置` -> 可修改`项目名称`(此名称自己命名) 后 -> 右下方点击 `保存并部署`即可。
2. 设置节点UUID和HOST变量： 
   - 在 Pages控制台的 `设置` 选项卡 -> 点击 `设置` -> 左方点击 `变量和机密` -> 右方点击  `添加` -> 变量名称 填入 `UUID`(此名称固定不能变) ，值填入CF部署节点ID -> 再点击添加变量 填入 `HOST`(此名称固定不能变)，值填入CF部署的自定义域名 后 -> 右下方点击 `保存`。
   - 在 `设置` 选项卡，点击 `部署` -> 在所有部署 找到最新一条部署记录 ，在右边点击 3个点 `...` 选择 `重试部署` 即可。
3. 给 Pages绑定 CNAME自定义域：[无域名绑定Cloudflare部署视频教程]->[免费域名教程1](https://youtu.be/wHJ6TJiCF0s) [免费域名教程2](https://youtu.be/yEF1YoLVmig)  [免费域名教程3](https://www.youtube.com/watch?v=XS0EgqckUKo&t=320s)
   - 在 Pages控制台的 `自定义域`选项卡，下方点击 `设置自定义域`。
   - 填入你的自定义次级域名，注意不要使用你的根域名，例如：
     您分配到的域名是 `amclubss.com`，则添加自定义域填入 `sub.amclubss.com`即可，点击 `激活域`即可。    
4. 验证部署是否成功：
   - 访问 `https://[YOUR-WORKERS-URL]` 即可进入登录页面,登录成功就是完成部署(默认登录密码(UUID)是：ec872d8f-72b0-4a04-b612-0327d85e18ed)。
   - 例如 `https://sub.amclubss.com` 然后进入登录页面 -> 输入密码 `ec872d8f-72b0-4a04-b612-0327d85e18ed` -> 点击登录 -> 成功登录。 
5. 修改默认登录密码(ID)变量，(强烈要求修改，防止别人用你节点)： 
   - 在 Pages控制台的 `设置` 选项卡 -> 点击 `设置` -> 左方点击 `变量和机密` -> 右方点击  `添加` -> 变量名称 填入 `ID`(此名称固定不能变) ，自己设置复杂的密码 -> 右下方点击 `保存`。
   - 在 `设置` 选项卡，点击 `部署` -> 在所有部署 找到最新一条部署记录 ，在右边点击 3个点 `...` 选择 `重试部署` 即可。
   - 保存成功后，原登录密码(ID)已作废不能访问，用新登录密码(ID)登录访问即可。
6. 本频道订阅器转换地址：https://sub.amclubss.com

</details>

## 
### 🔧三、变量说明 [视频教程](https://www.youtube.com/watch?v=i-XnnP-MptY&t=596s)
| 变量名 | 示例 | 必填 | 备注 | YT |
|-----|-----|-----|-----|-----|
| ID   | ec872d8f-72b0-4a04-b612-0327d85e18ed（默认）|✅| 订阅器的登录密码 | |
| UUID | ec872d8f-72b0-4a04-b612-0327d85e18ed |✅| Cloudflare部署节点的ID变量值[在线获取UUID](https://1024tools.com/uuid)   |  |
| HOST | vless.amclubss.com |✅| Cloudflare部署节点的域名或自定域名 | |
| IP_URL           | [https://raw.github.../ipUrl.txt](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/ipUrl.txt)           |❌| （推荐）优选(ipv4、ipv6、域名、API)地址(支持多个之间`,`或 换行 作间隔)，支持文件连接后里带PROXYIP参数，可以实现不同区域优先IP使用不同的PROXYIP固定区域，解决IP乱跳问题  | [视频教程](https://www.youtube.com/watch?v=4fcyJjstFdg&t=349s)|
| PROXYIP          | proxyip.amclubs.kozow.com </br>或</br> [https://raw.github.../proxyip.txt](https://raw.githubusercontent.com/amclubs/am-cf-tunnel/main/proxyip.txt)  |❌| 访问CloudFlare的CDN代理节点(支持多PROXYIP, PROXYIP之间使用`,`或 换行 作间隔),支持端口设置默认443 如: proxyip.amclubs.kozow.com:2053 ，支持远程txt或csv文件| [视频教程](https://youtu.be/pKrlfRRB0gU) |
| SOCKS5           | user:password@127.0.0.1:1080         |❌| 优先作为访问CFCDN站点的SOCKS5代理                                                   | [视频教程](https://youtu.be/Bw82BH_ecC4) |
| NAT64           | true/false                           |❌| 默认false,是否开启nat做PROXYIP(反代IP)，开启后优选使用NAT64再用PROXYIP       | [视频教程](https://www.youtube.com/watch?v=nx80sGpVoBM&t=533s) |
| NAT64_PREFIX  | 2602:fc59