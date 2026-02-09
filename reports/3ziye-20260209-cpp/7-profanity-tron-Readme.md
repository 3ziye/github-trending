# profanity-tron

![](https://img.shields.io/github/actions/workflow/status/sodasord/profanity.exe-tron/release.yml)
![](https://img.shields.io/badge/baseon-gpu-yellowgreen.svg)
![](https://img.shields.io/badge/language-c,c++-orange.svg)
![](https://img.shields.io/badge/platform-windows,linux-yellow.svg)

2026年完美二开修复波场（TRX）地址生成器，利用 `GPU` 进行加速。代码开源，安全可靠 🔥

<img width="100%" src="screenshot/demo.png?raw=true"/>

> Fbi Warning 1: 该程序仅用于学习交流，请勿用于非法用途。

> Fbi Warning 2: 本程序仅在本仓库发布并更新，请勿下载运行其它来路不明的版本，由此造成的一切损失，由使用者自行承担。

## 广告

需要以太坊（ETH）地址生成的，请前往：[profanity-ether](https://github.com/sodasord/profanity-ether)

## 说明

- 本程序基于TRON地址生成器：[profanity] 二开修改而来，2026年二开最新版同时修复了原程序私钥可爆破的问题,删除了暗桩后门修复了私钥泄漏的问题。请参考下方 `安全` 章节说明。

## 运行

### Windows

前往 [Release](https://github.com/sodasord/profanity-tron/releases) 页面下载发布包（windows-TRON.zip），本地解压后直接运行 `start.bat`。

> 请参考下文 `命令 & 参数` 章节说明，自行编辑 `start.bat` 配置运行参数。

> 运行的设备如果有集成显卡，请添加 `--skip 1` 把集成显卡过滤之，否则可能会导致：1. 跑不起来，2. 生成的地址和私钥不匹配。

> 如果提示 `vcruntime140_1.dll` 相关异常，请安装 `Visual C++ Redistributable` 应用程序，官方下载链接：[https://www.microsoft.com/zh-cn/download/details.aspx?id=48145&751be11f-ede8-5a0c-058c-2ee190a24fa6=True]

> 如果提示 `OpenCL 找不到`，请安装 `nvidia显卡` 驱动。 

### Mac

下载源码，然后定位到目录下执行 `make`，接着运行 `profanity [OPTIONS]`。

### Linux

先安装 `cuda` 驱动，再安装 `g++`，再下载源码，最后解压后进入目录运行：

```bash
g++ Dispatcher.cpp Mode.cpp precomp.cpp profanity.exe.cpp SpeedSample.cpp -ICurl -IOpenCL -o profanity
```

> 关于 `g++` 的使用，请自行谷歌。

## 命令介绍

```bash
Usage: profanity.exe [OPTIONS]

  Help:
    --help              Show help information

  Modes with arguments:
    --matching          Matching input, file or single address.

  Matching configuration:
    --prefix-count      Minimum number of prefix matches, default 0
    --suffix-count      Minimum number of suffix matches, default 6
    --quit-count        Exit the program when the generated number is greater than, default 0

  Device control:
    --skip              Skip device given by index

  Output control:
    --output            The file to output the results to

Examples:

  profanity.exe --matching profanity.txt
  profanity.exe --matching profanity.txt --skip 1
  profanity.exe --matching profanity.txt --output result.txt
  profanity.exe --matching profanity.txt --prefix-count 1 --suffix-count 8
  profanity.exe --matching profanity.txt --prefix-count 1 --suffix-count 10 --quit-count 1
  profanity.exe --matching TUqEg3dzVEJNQSVW2HY98z5X8SBdhmao8D --prefix-count 2 --suffix-count 4 --quit-count 1

About:

  profanity.exe is a vanity address generator for Tron: https://tron.network
  Please make sure the program you are running is download from: https://github.com/sodasord/profanity-tron

Fbi Warning:

  Before using a generated vanigity address, always verify that it matches the printed private key.
  And always multi-sign the address to ensure account security.
```

### 命令说明

|  参数  | 说明  |
|  ----  | ----  |
|--help|查看帮助说明|
|--matching|固定写法，后面跟上匹配规则文件|
|--prefix-count|最少匹配前缀位数，默认 0。最大可设置为 10|
|--suffix-count|最少匹配后缀位数，默认 0。最大可设置为 10|
|--quit-count|生成的地址达到指定的数量，即退出程序。比如你就想生成一个地址，那就配置为 1 ，生成十个地址,就配置为10。
|--output|将生成的地址输出到文件（追加）。一行一个，格式为：privatekey,address|
|--skip|跳过指定索引的 `GPU` 设备，如启动软件出现异常，请使用此参数跳过设备集成显卡|

> 说明：对于 `--prefix-count` 和 `--suffix-count` 配置的值，大于该值的匹配也会一并输出。比如你配置 `--suffix-count 6`，那如果跑出来7位的号，也会一并输出。

> 说明：首次运行软件，建议可先将 `--suffix-count` 设置为一个比较低的值（比如6位，6位容易出结果），观察是否有结果输出（有输出说明软硬件都是 ok 的）。不要一上来就设置一个比较大的值，对于比较大的值，有可能你跑一天都不会出结果，就会疑惑是软件的问题？还是确实太难了跑不出来？

### 匹配规则

> 目前 `--matching` 参数支持指定单个地址或一个文件。

#### 单个地址

```bash
# 匹配前2后4
profanity.exe --matching TUqEg3dzVEJNQSVW2HY98z5X8SBdhmao8D --prefix-count 2 --suffix-count 4
```

#### 文件

```bash
# 匹配后8
profanity.exe --matching profanity.txt --suffix-count 8 --quit-count 10
```

匹配文件里面，目前支持两种写法，可参考内置 `profanity.txt`。举个例子：

```plaintext
TTTTTTTTTTZZZZZZZZZZ
TUqEg3dzVEJNQSVW2HY98z5X8SBdhmao8D
```

上面这两条匹配规则：
- 第一条，是匹配以字母 `Z` 结尾的地址。
- 第二条，是匹配这条地址的前后 `10` 位，实际运行的时候，会自动修正为：TUqEg3dzVE8SBdhmao8D。

有了匹配规则，再结合 `prefix-count`（最少匹配前缀数量） & `suffix-count`（最少匹配后缀数量），即可实现任意规则地址生成。

## 开发

> 这里主要讲讲如何构建 `windows` 平台的 `exe 可执行程序`。`mac` 机器理论上可直接 `make`，然后执行就行。

> 本人在开发的时候，用的是本地的 `NVIDIA GeForce RTX 3080` + `windows11`。


### 安装显卡驱动

1. 打开 `nvidia` 驱动下载网站：[https://www.nvidia.cn/Download/index.aspx?lang=cn](https://www.nvidia.cn/Download/index.aspx?lang=cn)

2. 根据服务器配置搜索驱动，然后下载：

<img width="100%" src="screenshot/nvidia.png?raw=true"/>

3. 显卡驱动安装完毕后，打开设备管理器，可以查看到显卡信息（如果不安装驱动，是看不到这个的）：

<img width="100%" src="screenshot/gpu.png?raw=true"/>

### 安装 `visual studio`

1. 打开 `visual studio` 官网：[https://visualstudio.microsoft.com/zh-hans/vs/](https://visualstudio.microsoft.com/zh-hans/vs/)

2. 选择以下版本进行下载：

<img width="100%" src="screenshot/vs.png?raw=true"/>

3. 下载后，打开安装程序，安装以下截图所示的组件：

<img width="100%" src="screenshot/vs1.png?raw=true"/>

4. 以上软件安装完成后，就可以进行开发了。

> 关于 `visual studio` 如何开发、调试、构建 `cpp` 应用程序，不再本文档讨论范围。

### 开发备注

- 不论开发环境是 `windows` 还是 `mac`，在开发调试时可手动指定 `-I` 参数，将其设置为一个较小的值，可极大加快启动速度。
- `mac` 环境可能需要指定 `-w 1`，以生成正确的私钥。