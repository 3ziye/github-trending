# 欧加耳机音质助手

`MelodyCodecTweaker` 是一个面向 OPPO / OnePlus「无线耳机」App 的 LSPosed 模块。它不会替换系统文件，也不会修改「无线耳机」App 安装包，而是在运行时注入音质控制项，让部分原本藏在系统蓝牙栈里的编解码器、播放质量、采样率和 LE Audio 状态可以直接在耳机控制面板里操作。

模块主要服务于 ColorOS / OPlus 系设备上的 `com.oplus.melody`，同时配合 `com.android.bluetooth` 和 `com.oplus.wirelesssettings` 作用域完成更稳定的状态读取和写入。

## 主要功能

- 在「无线耳机」主面板 `DetailMainActivity` 注入蓝牙音质区域。
- 在 OneSpace 快捷面板 `OneSpaceDetailActivity` 注入同一套控制项。
- 显示当前协议：SBC、AAC、LDAC、LHDC、LC3 等。
- 支持播放质量切换，例如 LHDC 的连接优先、均衡、音质优先，以及 LDAC 的 330 / 660 / 990 kbps。
- 支持采样率切换，根据当前耳机和协议动态显示 44.1 / 48 / 96 / 192 kHz 等可选项。
- 播放质量和采样率会做联动修正，尽量避免写入蓝牙栈不接受的组合。
- 支持按耳机记忆选择，重新连接后自动应用上次设置。
- 支持 LE Audio 开关：开启后进入 LC3，并隐藏经典 A2DP 下的播放质量和采样率选项；关闭后恢复经典蓝牙音频状态。
- 耳机未连接、当前协议不可控、耳机不支持 Hi-Res 或 LE Audio 时，会隐藏或置灰对应选项，尽量贴近官方控件表现。
- 提供模块内置诊断页，可以查看作用域加载、页面 Hook、蓝牙桥接、无线设置桥接、native 补丁、记忆重放等状态，并可按需隐藏桌面图标。
- 提供「开始记录问题 + 生成反馈包」的复现记录流程，便于排查不同手机、系统版本、耳机型号和「无线耳机」版本带来的差异。

## 使用要求

- Android 12 及以上。
- 支持 libxposed API 101 的框架，例如新版 LSPosed。
- OPPO / OnePlus / ColorOS 系统上的「无线耳机」App：`com.oplus.melody`。
- 建议启用全部四个 LSPosed 作用域：
  - `com.oplus.melody`
  - `com.android.bluetooth`
  - `com.oplus.wirelesssettings`
  - `com.android.settings`

`com.oplus.melody` 负责页面注入和用户交互，`com.android.bluetooth` 负责更稳定地读写 A2DP 编解码器状态，`com.oplus.wirelesssettings` 负责调用系统侧 LE Audio 能力，`com.android.settings` 只用于收敛开发者选项里 LHDC V5 扩展值造成的无害日志噪音。少开作用域可能仍能部分工作，但实时切换、状态回读、LE Audio 和系统设置侧日志降噪会更容易失效。

## 安装与启用

1. 安装模块 APK。
2. 在 LSPosed 中启用模块。
3. 勾选上面四个作用域。
4. 强制停止「无线耳机」、蓝牙相关进程和无线设置，或者直接重启手机。
5. 打开「无线耳机」App，进入耳机主面板或 OneSpace 面板查看注入项。

如果只想临时停用模块，可以打开桌面图标「欧加耳机音质助手」，关闭模块总开关。关闭后需要重启「无线耳机」进程，宿主页才会完全恢复原状。

桌面图标默认显示。若不希望启动器里出现模块图标，可以在诊断页打开「隐藏桌面图标」开关；这个开关只控制 launcher alias，不会禁用模块，也不会影响 LSPosed 作用域加载或 LSPosed 管理器里的模块 UI 入口。

## 内置诊断页

模块桌面入口是内置诊断页，主要包含：

- 模块总开关。
- 隐藏桌面图标开关。
- 模块版本、手机型号、Android 版本和相关包版本。
- 「无线耳机」作用域、页面 Hook、主面板 / OneSpace 注入状态。
- 蓝牙作用域、A2DP Bridge、无线设置作用域和 LE Audio bridge 状态。
- LHDC V5 native 内存补丁、最近写入、记忆写入和重连重放状态。
- 「开始记录问题」和「生成反馈包」两个反馈操作。
- 最近结构化事件时间线。

如果出现「页面没有注入」「切换失败」「LE Audio 状态不刷新」「重连后记忆没有恢复」这类问题，建议先点「开始记录问题」，复现一次问题，再点「生成反馈包」。诊断页截图也仍然有用，可以快速判断是作用域没生效、页面 Hook 丢了、蓝牙桥没收到、native 补丁没命中，还是无线设置桥没工作。

## 一键反馈包

诊断页里的「生成反馈包」会生成：

```text
OPlusHeadsetAudioHelper-feedback-YYYYMMDD-HHMMSS.zip
```

优先保存到：

```text
/storage/emulated/0/
```

如果系统不允许直接写入根目录，会降级保存到：

```text
/storage/emulated/0/Download/
```

建议反馈前按这个流程操作，普通用户按顺序做即可：

1. 确认 LSPosed 里已经启用模块，并勾选 `com.oplus.melody`、`com.android.bluetooth`、`com.oplus.wirelesssettings`、`com.android.settings` 四个作用域。
2. 在 KernelSU / Magisk / APatch 等 root 管理器里给「欧加耳机音质助手」授权 root；没有 root 授权时也能生成反馈包，但会缺少最关键的蓝牙栈日志。
3. 打开「欧加耳机音质助手」诊断页，点击「开始记录问题」。如果弹出 root 授权请求，请选择允许。
4. 回到「无线耳机」页面复现一次问题，例如切换 LHDC 质量 / 采样率、切换 AAC / SBC / LHDC、断开重连耳机、开关 LE Audio，或等待出现「未适配，请联系开发者反馈」。
5. 再回到诊断页，点击「生成反馈包」。
6. 把生成的 `OPlusHeadsetAudioHelper-feedback-YYYYMMDD-HHMMSS.zip` 发给开发者即可。

如果是为了适配 LHDC V5 native 内存补丁，请同时提供手机型号、系统版本，以及当前系统的 `/system/lib64/libbluetooth_jni.so`。这个文件可以通过 root 文件管理器复制，也可以在电脑上用 adb 尝试导出：

```bash
adb pull /system/lib64/libbluetooth_jni.so
```

反馈包包含设备信息、模块版本、相关包版本、诊断状态、最近模块事件时间线、结构化事件 JSONL、状态快照、模块偏好、`scope.list`、`module.prop` 和模块 logcat。若设备已授权 root，还会额外尝试抓取并过滤蓝牙栈相关 logcat，便于确认 `quality_mode`、`target bit rate`、`codec_specific_1`、native patch 和记忆重放情况。它不会主动打包用户文件，但 logcat 里可能包含系统日志，请反馈前自行确认是否介意。

常见文件包括：

- `summary.txt`：设备、系统、模块和相关包版本概览。
- `diagnostics.txt`：诊断页状态汇总。
- `timeline.txt`：模块事件时间线，适合直接阅读。
- `events.jsonl`：结构化事件，适合后续筛选分析。
- `state.json`：当前诊断状态快照。
- `prefs.txt`：模块偏好和诊断偏好。
- `logcat-module.txt`：模块相关 logcat。
- `logcat-bluetooth-root.txt`：root 可用时抓取的蓝牙栈相关日志。

## LE Audio 说明

LE Audio 开关只会在模块判断当前设备支持时显示。判断来源包括「无线耳机」自身状态、系统蓝牙 UUID、蓝牙侧桥接回传和无线设置侧状态，避免出现「手机支持 LE Audio，但当前耳机不支持」时误显示。

开启流程：

1. 用户在「无线耳机」主面板或 OneSpace 面板点击 LE Audio。
2. 模块在当前 Melody Activity 内弹出确认对话框。
3. 用户确认后，模块再向系统侧作用域发送请求。
4. `com.oplus.wirelesssettings` 或蓝牙侧桥接调用系统 `LeAudioProfile.setEnabled(device, true)`。
5. 蓝牙栈完成切换后回传状态，页面显示 `蓝牙音质: LC3`。
6. 经典 A2DP 的播放质量和采样率行隐藏。

关闭 LE Audio 时，耳机通常会短暂断开并重新连回经典蓝牙音频。模块会延迟刷新 A2DP 状态，期间页面可能短暂显示等待状态，这是蓝牙栈重新协商造成的。

## 播放质量与采样率

模块优先读取系统蓝牙栈中的实时能力，而不是硬编码所有耳机档位：

- 当前协议来自 `BluetoothA2dp.getCodecStatus()`。
- 播放质量来自 `codecSpecific1` 能力。
- 采样率来自 `sampleRate` bitmask。
- 写入优先使用 `setCodecConfigPreference()` 并等待系统广播确认。

写入路径会按能力降级：

1. Melody 进程内直接反射 A2DP 隐藏 API。
2. 通过 `com.android.bluetooth` 中注册的 AIDL bridge 写入。
3. 对 LDAC / 采样率尝试写入开发者选项 `Settings.Global`。
4. 最后尝试 root shell fallback。

LHDC 的实时切换更依赖厂商蓝牙栈。模块会直接写入目标播放质量 / 采样率组合，避免一次切换里额外触发 A2DP 重配置。如果蓝牙栈拒绝当前组合，模块会尽量自动选择兼容采样率，例如从「均衡 / 48 kHz」切换到「音质优先」时先提升到可用采样率。

## 兼容策略

「无线耳机」App 经常经过 R8 混淆，直接绑定单个类名非常容易在更新后失效。当前模块做了这些兜底：

- 优先 Hook Manifest 中相对稳定的 Activity，例如 `DetailMainActivity` 和 `OneSpaceDetailActivity`。
- 同时 Hook Melody / COUI / AndroidX 的 PreferenceFragment 形态。
- 运行时扫描 FragmentManager，查找带有目标 PreferenceScreen 标记的页面。
- 通过 Preference key、页面结构和可见分类兜底寻找注入点。
- 从 Intent、Fragment / Activity 字段以及当前 active A2DP 设备解析当前耳机，兼容从系统设置跳转进 DetailMain 的路径。
- 对没有 Hi-Res、没有 LE Audio、没有对应协议能力的设备做隐藏或禁用处理。
- 系统侧蓝牙和无线设置也做了多点 Hook，降低系统更新后单点失效概率。

这些策略能覆盖同一大版本内较多小版本更新，但模块仍然依赖厂商私有页面结构和隐藏 API，不是公开 