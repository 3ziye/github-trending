# openhongguo

[![Go Reference](https://pkg.go.dev/badge/github.com/beilunyang/openhongguo/sdk.svg)](https://pkg.go.dev/github.com/beilunyang/openhongguo/sdk)
[![npm](https://img.shields.io/npm/v/openhongguo)](https://www.npmjs.com/package/openhongguo)
[![npm react-native](https://img.shields.io/npm/v/react-native-openhongguo?label=npm%20react-native)](https://www.npmjs.com/package/react-native-openhongguo)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.beilunyang/openhongguo)](https://central.sonatype.com/artifact/io.github.beilunyang/openhongguo)
[![pub.dev](https://img.shields.io/pub/v/openhongguo)](https://pub.dev/packages/openhongguo)
[![CI](https://github.com/beilunyang/openhongguo/actions/workflows/ci.yml/badge.svg)](https://github.com/beilunyang/openhongguo/actions/workflows/ci.yml)

[![npm downloads](https://img.shields.io/npm/d18m/openhongguo?label=npm%20downloads)](https://www.npmjs.com/package/openhongguo)
[![react-native downloads](https://img.shields.io/npm/d18m/react-native-openhongguo?label=react-native%20downloads)](https://www.npmjs.com/package/react-native-openhongguo)
[![pub downloads](https://img.shields.io/pub/dm/openhongguo?label=pub%20downloads)](https://pub.dev/packages/openhongguo)
[![CLI downloads](https://img.shields.io/github/downloads/beilunyang/openhongguo/total?label=CLI%20downloads)](https://github.com/beilunyang/openhongguo/releases)

openhongguo 是红果短剧（Hongguo）的非官方 SDK，提供 Go、Node.js、Android、iOS、React Native 和 Flutter 版本。SDK 可以浏览短剧目录、搜索短剧、读取短剧和分集的详情与弹幕，并取得分集的播放地址和内容密钥。

SDK 用匿名设备发送所有请求，不需要登录。Go 以外的 SDK 都由 Go SDK 编译而成，所以各语言的行为相同。

> **免责声明**
>
> 请以学习为目的使用本仓库。
>
> 本仓库的所有内容仅供学习和参考之用，禁止用于商业用途。任何人或组织不得将本仓库的内容用于非法用途或侵犯他人合法权益。
>
> 本仓库所涉及的接口分析与调用技术仅用于学习和研究，不得用于对其他平台进行大规模数据采集或其他非法行为。
>
> 对于因使用本仓库内容而引起的任何法律责任，本仓库不承担任何责任。使用本仓库的内容即表示您同意本免责声明的所有条款和条件。
>
> 详细的免责声明见[文末](#免责声明)。

## 文档

| 文档 | 内容 |
|---|---|
| [类型参考](docs/types.md) | 所有返回值和查询参数的字段 |
| [Go 包文档](https://pkg.go.dev/github.com/beilunyang/openhongguo/sdk) | Go SDK 的完整 API |
| [命令行文档](docs/cli.md) | 命令行工具 openhongguo-cli（命令 `ohg`）的用法 |
| [开发说明](docs/development.md) | 接口契约检查和持续集成 |
| [发布手册](docs/release.md) | 发布新版本的步骤 |

## 安装

| 语言 | 包 | 安装 | 文档 |
|---|---|---|---|
| Go | [`github.com/beilunyang/openhongguo`](https://pkg.go.dev/github.com/beilunyang/openhongguo/sdk) | `go get github.com/beilunyang/openhongguo@latest` | 本文 |
| Node.js | [`openhongguo`](https://www.npmjs.com/package/openhongguo) | `npm install openhongguo` | [bindings/node](bindings/node/README.md) |
| Android（Kotlin） | [`io.github.beilunyang:openhongguo`](https://central.sonatype.com/artifact/io.github.beilunyang/openhongguo) | `implementation("io.github.beilunyang:openhongguo:0.3.0")` | [bindings/mobile](bindings/mobile/README.md) |
| iOS / macOS（Swift） | Swift Package | `.package(url: "https://github.com/beilunyang/openhongguo.git", from: "0.3.0")` | [bindings/mobile](bindings/mobile/README.md) |
| React Native | [`react-native-openhongguo`](https://www.npmjs.com/package/react-native-openhongguo) | `npx expo install react-native-openhongguo` | [bindings/react-native](bindings/react-native/README.md) |
| Flutter | [`openhongguo`](https://pub.dev/packages/openhongguo) | `flutter pub add openhongguo` | [bindings/flutter](bindings/flutter/README.md) |

## 要求

| 语言 | 最低版本 |
|---|---|
| Go | 1.22 |
| Node.js | 20 |
| Android | 5.0（API 21）；Flutter 是 7.0（API 24） |
| iOS | 13；React Native 是 15.1，Flutter 是 15 |
| macOS | 11 |

## 快速上手

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/beilunyang/openhongguo/adapters"
	"github.com/beilunyang/openhongguo/sdk"
)

func main() {
	ctx := context.Background()
	client, err := adapters.NewClient("anonymous.json", sdk.Options{})
	if err != nil {
		log.Fatal(err)
	}

	page, err := client.Search(ctx, "全球死考", sdk.SearchOptions{})
	if err != nil {
		log.Fatal(err)
	}
	episodes, err := client.ListEpisodes(ctx, page.Items[0].ID, sdk.EpisodeOptions{})
	if err != nil {
		log.Fatal(err)
	}
	pb, err := client.ResolvePlayback(ctx, episodes.Items[0].ID, sdk.PlaybackOptions{})
	if pb == nil {
		log.Fatal(err)
	}
	for _, s := range pb.Streams {
		fmt.Println(s.Definition, s.URL)
	}
}
```

第一次请求时，SDK 注册一台匿名设备，并把设备档案保存到 `anonymous.json`。以后的请求都使用这台匿名设备。

<details>
<summary>其他语言的写法</summary>

| 语言 | 创建客户端并搜索 |
|---|---|
| Node.js | `const client = await createClient();`<br>`const page = await client.search('全球死考');` |
| Kotlin | `val client = OpenhongguoClient.create(context)`<br>`val page = client.search("全球死考")` |
| Swift | `let client = try OpenhongguoClient.create()`<br>`let page = try await client.search("全球死考")` |
| React Native | `const client = await createClient();`<br>`const page = await client.search('全球死考');` |
| Dart | `final client = await OpenhongguoClient.create();`<br>`final page = await client.search('全球死考');` |

</details>

## 客户端选项

`adapters.NewClient` 用默认的实现创建客户端。`sdk.Options` 的字段都是可选的。

```go
client, err := adapters.NewClient("anonymous.json", sdk.Options{
	RetryAttempts: 5,
	Logger:      