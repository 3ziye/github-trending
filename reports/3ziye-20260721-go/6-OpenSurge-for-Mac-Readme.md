<div align="center">
  <img src="apps/menubar/Resources/OpenSurgeAppIcon.png" width="96" height="96" alt="OpenSurge for Mac App 图标">
  <h1>OpenSurge for Mac</h1>
  <p><strong>把 Mac 变成可导入规则、可按设备分流的全屋透明代理网关——支持 DHCP/DNS 自动接管</strong></p>
  <p>
    <a href="https://github.com/YTwsy/OpenSurge-for-Mac/releases"><img alt="最新版本" src="https://img.shields.io/github/v/release/YTwsy/OpenSurge-for-Mac?style=flat-square"></a>
    <img alt="macOS 13+" src="https://img.shields.io/badge/macOS-13%2B-000000?style=flat-square&amp;logo=apple">
    <img alt="提供 Apple Silicon 与 Intel 安装包" src="https://img.shields.io/badge/Apple%20Silicon%20%7C%20Intel-packages-6f42c1?style=flat-square&amp;logo=apple">
    <a href="LICENSE"><img alt="GPL-3.0-only" src="https://img.shields.io/badge/license-GPL--3.0--only-2ea44f?style=flat-square"></a>
  </p>
  <p>
    <strong>简体中文</strong> · <a href="README.en.md">English</a>
  </p>
  <p>
    <a href="https://github.com/YTwsy/OpenSurge-for-Mac/releases">下载</a> ·
    <a href="docs/app-user-guide.zh-CN.md">App 指南</a> ·
    <a href="#能力">能力</a> ·
    <a href="#每设备策略">每设备策略</a> ·
    <a href="#web-gui-与菜单栏-app">Web GUI</a> ·
    <a href="#ai-agent-友好工作区">Agent 工作区</a>
  </p>
  <table width="100%">
    <tr>
      <td width="66%" valign="top">
        <img src="docs/images/opensurge-dashboard.png" width="100%" alt="OpenSurge 全屋网关主界面">
      </td>
      <td width="34%" valign="top">
        <img src="docs/images/opensurge-policies.png" width="100%" alt="OpenSurge 策略与节点健康页面">
        <br>
        <img src="docs/images/opensurge-devices.png" width="100%" alt="OpenSurge 每设备策略页面">
      </td>
    </tr>
  </table>
</div>

OpenSurge for Mac 是一个开源的 Surge 风格 macOS 网关与控制面。它把 Mac 变成
整个局域网的代理出口：同一网络下的手机、电视、PS5、游戏机、VR 设备、虚拟机等终端，
都可以从 Mac 获取 DHCP/DNS，并共享由策略控制的网络连接；你也可以为每台设备
单独配置不同的出口策略：手机走代理、游戏机直连，设备啥都不用配。

- 能导入你现有的 mihomo 订阅，它只接管网关那部分，不抢你的节点和规则。
- 有 Web GUI 和菜单栏 app，哪个设备在跑多少流量、走的哪条出口链，一目了然。

底层由 dnsmasq 提供 DHCP/DNS，mihomo 作为代理引擎，macOS pf 与 IPv4
forwarding 提供原生网关路径。

这个仓库也被有意设计成一个
[AI Agent 友好工作区](#ai-agent-友好工作区)：项目知识与代码一起版本化，高风险
网络行为有可执行的证据门槛，Virtual Lab 与真实设备产生的证据会回流到下一轮工程
循环。

## 能力

**友好的 App 体验**

- 通过 macOS 菜单栏 App 随时查看状态、接收网络恢复提醒并打开本地 Web GUI；
- 在一个控制面中完成订阅导入、网络设置、设备分流、节点健康、连通性检查与诊断；
- 使用恢复状态机引导同一 LAN DHCP 接管的启动、客户端验收、停止和网络恢复。

第一次使用请参阅 [OpenSurge for Mac App 使用指南](docs/app-user-guide.zh-CN.md)。

**网关与代理**

- 启停 DHCP/DNS、mihomo、pf NAT 与 IPv4 forwarding，并带 rollback；
- 通过 mihomo `mixed-port` 提供显式代理；
- 通过 mihomo TUN 提供 macOS 透明代理；
- DHCP 接管模式为登记设备生成 MAC 绑定的固定 IPv4 租约；同 LAN 手工网关模式
  使用主路由侧保持稳定的静态 IPv4，两者都可使用独立出口策略。

**可观测性**

- 把活跃会话流量归属到 DHCP 设备或同 LAN 的静态登记/当前观察设备，显示每设备
  连接数、实时上下行速率、累计字节与占主要流量的 mihomo 出口链；
- 集中检测代理节点可达性/延迟，并从健康视图切换已应用的 Selector；
- 通过 applied mihomo mixed-port 路径探测固定真实服务目录，展示三轮中位延迟、
  命中规则与实际出口链；
- 查看与切换策略组、查看 imported proxy/rule provider 状态、查看当前连接；
- 输出文本/JSON 形式的 status / doctor / logs / snapshot，并收集允许局部失败的
  JSON snapshot 供诊断与 UI 使用。

**安全与验证**

- 配置校验、TUN-only 透明代理、rollback 与明确的恢复契约；
- 在接触普通 LAN 前，先用隔离的虚拟 LAN lab 验证高风险网络行为。

## 每设备策略

一个 mihomo 进程可以对已登记的 LAN 设备应用独立策略。DHCP 接管模式会为每台设备
配置 MAC 绑定的固定 IPv4 租约；同 LAN 手工网关模式则使用主路由侧保持稳定的静态
IPv4，并从当前经过 Mac 的流量与 ARP 邻居观察辅助登记。两种模式都会生成每设备的
mihomo selector group 和 `SRC-IP-CIDR` 规则。可选 JSON 策略文件让每台设备要么跟随 Mac/全局规则，要么在
全局规则之前走设备专属 selector；它也支持 `REJECT` 这类设备专属动作，以及按
域名/IP/协议/端口/rule-provider 叠加的规则覆盖。dedicated 模式下，本地/私有目标
保持直连。

OpenSurge 有意不内置家庭模板或第三方规则列表；策略内容由操作者提供，空 starter
文件也是合法配置。JSON 模型、优先级、CLI 命令和验证边界见
[每设备策略覆盖](docs/device-policy.zh-CN.md)。

## Web GUI 与菜单栏 App

通过安装包使用 OpenSurge 时，请从
[OpenSurge for Mac App 使用指南](docs/app-user-guide.zh-CN.md)开始。

本地 Control API、React Web GUI 和只读 SwiftUI 菜单栏 launcher 已进入仓库。开发构建：

```sh
make web-install
make control-build
./bin/opensurge-control --config examples/config.example.yaml
make menubar-build
```

控制服务只监听 `127.0.0.1`，启动时会输出一次性 Web GUI 链接。菜单栏 App 显示
状态、恢复警报并打开 Web GUI，不提供网关 start/stop 或策略切换。它区分“只退出菜单栏
App”和“退出 OpenSurge”：后者只在网关数据面已经停止时退出菜单栏 App 与用户级
Control Service；系统 launchd 托管的 root Helper 保持空闲加载，下次打开无需再次授权。
架构、安全边界与构建说明见 [Web GUI 与菜单栏 App](docs/gui-architecture.zh-CN.md)。
Web GUI 内置 applied 网关策略路径的连通性页面，并提供 Net.Coffee 的独立浏览器本机
检测入口；两者都不会被描述成下游设备 DHCP/DNS/TUN 路径已经验收。

`make gui-installer` 会在取得真实 mihomo、dnsmasq 二进制后构建 macOS 安装包。
Developer ID 签名和 notarization 必须显式提供发布凭据。GitHub 正式发布同时提供文件名中
明确带有 `arm64-unsigned.pkg` 与 `x86_64-unsigned.pkg` 的架构专用构建，但不能把正式
Release 描述成已经签名、已经 notarize 或可被 Gatekeeper 直接放行的安装包。

### 安装 GitHub 未签名正式发布包

当前正式发布同时提供 Apple Silicon 与 Intel Mac 安装包。请从对应 GitHub Release 下载
`arm64-unsigned.pkg`（Apple Silicon）或 `x86_64-unsigned.pkg`（Intel），以及
`SHA256SUMS`。可运行 `shasum -a 256 -c SHA256SUMS` 核对已下载文件，并使用以下命令
验证所选安装包的 GitHub 构建来源：

```sh
gh attestation verify OpenSurge-for-Mac-*-arm64-unsigned.pkg \
  -R YTwsy/OpenSurge-for-Mac
gh attestation verify OpenSurge-for-Mac-*-x86_64-unsigned.pkg \
  -R YTwsy/OpenSurge-for-Mac
```

双击安装包。如果 Gatekeeper 阻止安装，进入**系统设置 → 隐私与安全性**，选择
**仍要打开**并完成身份验证，然后再次打开同一个安装包。不要全局关闭 Gatekeeper，
也不要递归删除 quarantine。使用管理员账户完成 Installer 后，从 `/Applications`
打开 **OpenSurge Menu Bar