# CursorLight

[English](#cursorlight-english)

一个基于 **ESP32-C3 SuperMini + BLE 蓝牙** 的桌面状态灯项目，用红绿灯挂件直观显示 Cursor Agent / AI 编程过程中的状态，例如思考中、执行中、成功、失败、等待用户操作等。

> A BLE-powered status light for Cursor Agent, using ESP32-C3 to visualize AI coding states.

---

## 1. 项目简介

CursorLight 将一个普通的红绿灯挂件改造成可由电脑控制的桌面状态灯。

核心思路：

- 使用 **ESP32-C3 SuperMini** 作为主控。
- 复用红绿灯挂件内部原有三色灯板。
- 通过 **BLE 蓝牙** 接收电脑端脚本发送的状态指令。
- 结合 Cursor Hooks，让 Cursor Agent 的工作状态自动映射到灯效。

本项目不依赖 Wi-Fi，电脑可以继续连接 5GHz 网络。ESP32-C3 只负责 BLE 通信和灯效控制。

---

## 2. 效果预览

典型状态映射：

| 场景 | 模式 | 灯效 |
|---|---|---|
| 开机展示 | `demo` | 自动展示多种灯效 |
| AI 正在分析 | `thinking` | 连贯跑马灯 |
| AI 正在生成 | `ai` | 柔和慢速跑马灯 |
| 正在执行命令 | `busy` | 黄灯慢闪 |
| 任务成功 | `success` | 绿灯常亮 |
| 任务失败 | `error` | 红灯快闪 |
| 严重异常 / 阻塞 | `alarm` | 红黄交替警灯 |
| 展示模式 | `traffic` | 模拟红绿灯 |
| 关闭 | `off` | 全灭 |

---

## 3. 硬件清单

| 类别 | 物料 | 数量 | 说明 |
|---|---|---:|---|
| 主体 | 红绿灯挂件 / 玩具交通信号灯模型 | 1 个 | 淘宝 / 1688 搜“红绿灯挂件”“交通信号灯挂件” |
| 主控 | ESP32-C3 SuperMini 开发板 | 1 块 | 建议购买已焊针版本，USB-C 更方便 |
| 限流 | 220Ω 1/4w 电阻 | 3 只 | 建议买 10 只装备用 |
| 连线 | 细导线 / 飞线 | 若干 | 推荐 30AWG 硅胶线或漆包线 |
| 供电 | USB-C 数据线 | 1 条 | 必须支持数据传输 |
| 绝缘 | 热缩管 / 绝缘胶带 | 少量 | 用于保护焊点 |
| 工具 | 电烙铁、焊锡丝、镊子、剪线钳 | 若干 | 需要基础焊接工具 |
| 检测 | 万用表 | 可选 | 推荐用于确认焊点和短路 |

说明：

- 本方案复用原玩具灯板，不需要额外购买红、黄、绿三颗 LED。
- 改装后建议使用 USB 供电，不建议继续使用纽扣电池。
- 每路灯建议串联 220Ω 电阻，用于保护 ESP32-C3 和原灯板。

---

## 4. 硬件接线

本项目当前适配的是 **公共正极灯板**。

实测灯位：

| 灯位 | 实际颜色 | ESP32 引脚 |
|---|---|---|
| L1 | 绿灯 | IO2 |
| L2 | 黄灯 | IO3 |
| L3 | 红灯 | IO4 |

接线方式：

```text
ESP32 3.3V  -> 原灯板 + / 原电池正极
ESP32 IO2   -> 220Ω -> L1 控制点 = 绿灯
ESP32 IO3   -> 220Ω -> L2 控制点 = 黄灯
ESP32 IO4   -> 220Ω -> L3 控制点 = 红灯

原灯板 - / 原电池负极：第一版先不要接
```

公共正极逻辑：

```text
GPIO LOW  = 灯亮
GPIO HIGH = 灯灭
```

固件中已经处理了反相输出，正常使用时不需要手动关心高低电平。

注意事项：

- 只焊接在露出的金属焊盘、元件焊脚或电阻焊点上。
- 不要焊在绿色阻焊层表面。
- 焊接完成后，先用万用表检查是否短路，再接入电脑 USB 供电。
- 如果用于成品交付，建议用热熔胶或 UV 胶固定飞线，避免拉断焊点。

---

## 5. 固件说明

固件文件：

```text
ESP32_C3_ToyBoard_CommonAnode_BLE_Enhanced_CursorLight.ino
```

固件特性：

- BLE 广播名：`CursorLight`
- 通信方式：BLE GATT 写入字符串
- 默认开机模式：`demo`
- 支持多种状态灯效
- 内置自动超时，避免灯长时间高亮

BLE 参数：

```text
Device Name: CursorLight
Service UUID: b8b7e001-7a6b-4f4f-9a8b-11c0ffee0001
Mode Characteristic UUID: b8b7e002-7a6b-4f4f-9a8b-11c0ffee0001
```

---

## 6. 烧录固件

### 6.1 安装 Arduino IDE

前往 Arduino 官方页面下载 Arduino IDE 2.x：

```text
https://www.arduino.cc/en/software
```

macOS：

1. 下载 macOS 版本。
2. 打开 `.dmg`。
3. 将 Arduino IDE 拖入 Applications。
4. 首次打开如有安全提示，按系统提示允许。

Windows：

1. 下载 Windows 安装包。
2. 按安装向导完成安装。
3. 如果系统提示安装驱动或允许网络访问，按需允许。

---

### 6.2 安装 ESP32 开发板包

打开 Arduino IDE 后：

1. 进入左侧 **Boards Manager**。
2. 搜索 `esp32`。
3. 安装 **esp32 by Espressif Systems**。
4. 安装完成后重启 Arduino IDE。

注意：不要把 **Arduino ESP32 Boards by Arduino** 作为本项目的主要板包。

---

### 6.3 选择开发板和端口

连接 ESP32-C3 SuperMini 后，在 Arduino IDE 中选择：

```text
Board: ESP32C3 Dev Module
Port: 选择带 USB 标识的串口
```

常见端口：

| 系统 | 端口示例 |
|---|---|
| macOS | `/dev/cu.usbmodemxxxx Serial Port (USB)` |
| Windows | `COM3` / `COM5` 等 |

推荐设置：

| 设置项 | 建议值 |
|---|---|
| USB CDC On Boot | Enabled |
| Upload Speed | 921600 或默认值 |
| Flash Size | 4MB 或默认值 |

如果串口监视器没有输出，优先确认 `USB CDC On Boot` 是否已设为 `Enabled`，然后重新上传固件。

---

### 6.4 上传固件

1. 用 Arduino IDE 打开 `.ino` 文件。
2. 确认 Board 和 Port。
3. 点击左上角 **Upload** 按钮。
4. 上传成功时，Output 区域通常会看到：

```text
Writing at ... 100%
Hash of data verified.
Hard resetting via RTS pin...
```

如果出现 `Connecting...` 后失败，可尝试：

```text
按住 BOOT -> 点击 Upload -> 开始 Writing 后松开 BOOT
```

---

### 6.5 串口检查

打开 Serial Monitor，波特率选择：

```text
115200
```

按一下开发板 `RST`，正常会看到类似日志：

```text
Power on. Default mode: demo
Common anode BLE enhanced version.
BLE device name: CursorLight
BLE advertising started.
Supported modes:
demo / thinking / ai / busy / success / error / alarm / traffic / off / red / yellow / green
```

---

## 7. BLE 控制脚本

电脑端通过 Python 脚本控制灯效：

```text
cursor_light_ble_enhanced.py
```

### 7.1 安装依赖

macOS：

```bash
python3 -m pip install bleak
```

Windows：

```powershell
py -3 -m pip install bleak
```

macOS 如果提示 `Bluetooth device is turned off`，但系统蓝牙已经打开，请到：

```text
系统设置 -> 隐私与安全性 -> 蓝牙
```

给 Terminal、iTerm、Cursor 或当前终端应用授权。

---

### 7.2 手动测试

macOS：

```bash
python3 cursor_light_ble_enhanced.py demo
python3 cursor_light_ble_enhanced.py thinking
python3 cursor_light_ble_enhanced.py ai
python3 cursor_light_ble_enhanced.py busy
python3 cursor_light_ble_enhanced.py success
python3 cursor_light_ble_enhanced.py error
python3 cursor_light_ble_enhanced.py alarm
python3 cursor_light_ble_enhanced.py traffic
python3 cursor_light_ble_enhanced.py off
```

Windows：

```powershell
py -3 cursor_light_ble_enhanced.py demo
py -3 cursor_light_ble_enhanced.py thinking
py -3 cursor_light_ble_enhanced.py ai
py -3 cursor_light_ble_enhanced.py busy
py -3 cursor_light_ble_enhanced.py success
py -3 cursor_light_ble_enhanced.py error
py -3 cursor_light_ble_enhanced.py alarm
py -3 cursor_light_ble_enhanced.py traffic
py -3 cursor_light_ble_enhanced.py off
```

---

## 8. 固件模式

| mode | 灯效说明 | 典型用途 |
|---|---|---|
| `demo` | 默认开机展示，循环展示多种灯效