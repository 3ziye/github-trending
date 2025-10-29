# MarkItDown Java

[![Java](https://img.shields.io/badge/Java-11+-orange.svg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]
[![Maven](https://img.shields.io/badge/Maven-3.6+-red.svg)

> **中国网络空间安全协会2025年开源安全奖励项目 - 重写赛道**
>
> 本项目是对微软开源项目 MarkItDown 的完整Java重写版本，旨在为中文用户提供更好的文档转换体验

微软 MarkItDown 的 Java 重写版本 - 将各种文档格式转换为 Markdown

## 📋 项目简介

MarkItDown Java 是一个功能强大的文档转换工具，支持将多种文档格式转换为 Markdown 格式。这是对微软开源项目 MarkItDown 的 Java 语言重写版本，专门针对中文环境和安全合规要求进行了优化。

### 🎯 主要特性

- **多格式支持**: PDF, DOCX, PPTX, XLSX, HTML, 图片, 音频, 文本等
- **OCR 文字识别**: 支持图片文字提取（需要 Tesseract）
- **表格处理**: 智能识别和转换表格
- **元数据提取**: 保留文档元信息
- **命令行界面**: 简单易用的 CLI 工具
- **独立Markdown引擎**: 内置独立的Java对象到Markdown转换引擎
- **高性能**: 基于 Java 11+ 优化，支持并发处理
- **中文优化**: 针对中文文档处理和显示进行优化

### 🏆 项目背景

- **参赛赛道**: 中国网络空间安全协会 2025年开源安全奖励 - 重写赛道
- **技术目标**: 将微软的 Python 原版 MarkItDown 完整重写为 Java 版本
- **安全考虑**: 在重写过程中遵循安全编码规范，确保代码质量和安全性
- **开源承诺**: 遵循 MIT 许可证，促进开源生态发展

### 📁 支持的文件格式

| 格式 | 扩展名 | 状态 | 备注 |
|------|--------|------|------|
| PDF | .pdf | ✅ 完全支持 | 支持文本和图片提取 |
| Microsoft Word | .docx, .doc | ✅ 完全支持 | 支持格式化文本和表格 |
| Microsoft PowerPoint | .pptx, .ppt | ✅ 完全支持 | 支持幻灯片文本和备注 |
| Microsoft Excel | .xlsx, .xls | ✅ 完全支持 | 支持多工作表处理 |
| HTML | .html, .htm | ✅ 完全支持 | 保持原有格式 |
| 图片 (OCR) | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp | ✅ 完全支持 | 中英文OCR识别 |
| 音频文件 | .mp3, .wav, .ogg, .flac, .m4a, .aac | ✅ 基础支持 | 提取音频元数据 |
| 文本文件 | .txt, .csv, .json, .xml, .md, .log | ✅ 完全支持 | 多种编码支持 |

## 🚀 快速开始

### 环境要求

- Java 11 或更高版本
- Maven 3.6+
- 可选: Tesseract OCR (用于图片文字识别)

### 安装使用

1. **下载 JAR 包**
   ```bash
   # 下载最新的可执行 JAR 包
   wget https://github.com/DuanYan007/markitdown-java/releases/download/v1.0.0/markitdown-java-1.0.0-SNAPSHOT.jar
   ```

2. **基本使用**
   ```bash
   # 转换单个文件
   java -jar markitdown-java-1.0.0-SNAPSHOT.jar document.pdf

   # 指定输出文件
   java -jar markitdown-java-1.0.0-SNAPSHOT.jar document.docx -o output.md

   # 批量转换所有PDF文件
   java -jar markitdown-java-1.0.0-SNAPSHOT.jar *.pdf
   ```

### 命令行选项

```bash
Usage: markitdown [OPTIONS] INPUT_FILES...

选项:
  -o, --output <FILE>          输出文件或目录
  --include-images            包含图片 (默认: true)
  --no-images                 排除图片
  --include-tables            包含表格 (默认: true)
  --no-tables                 排除表格
  --include-metadata          包含元数据 (默认: true)
  --no-metadata               排除元数据
  --ocr                       使用 OCR 文字识别
  --language <LANG>           OCR 语言 (默认: auto)
  --table-format <FORMAT>     表格格式: github, markdown, pipe (默认: github)
  --image-format <FORMAT>     图片格式: markdown, html, base64 (默认: markdown)
  --max-file-size <SIZE>      最大文件大小 (默认: 50MB)
  --temp-dir <DIR>            临时目录
  -v, --verbose               详细输出
  -q, --quiet                 静默模式
  -h, --help                  显示帮助
  -V, --version               显示版本信息
```

## 🔧 开发信息

### 项目结构

```
MarkItDown Java/
├── src/main/java/com/markitdown/
│   ├── api/                    # API 接口定义
│   ├── cli/                    # 命令行界面
│   ├── config/                  # 配置管理
│   ├── converter/               # 文档转换器
│   ├── core/                   # 核心引擎
│   │   └── markdown/          # 独立Markdown引擎
│   ├── exception/               # 异常处理
│   └── utils/                   # 工具类
├── src/main/java/com/markdown/engine/  # 独立Markdown引擎
│   ├── config/                 # Markdown引擎配置
│   ├── context/                # 渲染上下文
│   ├── renderer/               # 类型渲染器
│   └── impl/                   # 引擎实现
└── src/test/                      # 单元测试
```

### 技术栈

- **核心框架**: Java 11+
- **命令行**: PicoCLI 4.7.5
- **PDF 处理**: Apache PDFBox 3.0.1
- **Office 文档**: Apache POI 5.2.5
- **HTML 解析**: jsoup 1.17.2
- **OCR**: Tess4J 5.8.0
- **音频处理**: Apache Tika 2.9.1
- **JSON/XML**: Jackson 2.16.1
- **日志**: SLF4J + Logback
- **构建工具**: Maven 3.6+

### 独立Markdown引擎特性

除了文档转换功能，本项目还包含一个完全独立的Markdown引擎：

- **Java对象转Markdown**: 支持任意Java对象转换为Markdown格式
- **智能渲染**: 根据对象类型自动选择最佳渲染方式
- **可扩展架构**: 支持自定义渲染器和配置
- **流式构建**: 提供MarkdownBuilder用于程序化文档构建
- **线程安全**: 支持多线程并发使用

```java
// 使用独立Markdown引擎
MarkdownEngine engine = MarkdownEngineFactory.createEngine();
MarkdownConfig config = MarkdownConfig.builder()
    .includeTables(true)
    .tableFormat("github")
    .customOption("useEmoji", true)
    .build();

// 转换复杂Java对象
Map<String, Object> data = Map.of(
    "姓名", "张三",
    "年龄", 25,
    "技能", Arrays.asList("Java", "Python", "数据分析")
);
String markdown = engine.convertWithMetadata(data, metadata, config);
```

## 📊 性能特性

- **文件大小限制**: 默认 50MB，可配置
- **内存优化**: 流式处理大文件
- **并发支持**: 多文件并行处理
- **错误恢复**: 优雅的错误处理机制
- **中文支持**: 专门的中文OCR和文本处理

## 🧪 测试

项目包含完整的单元测试套件:

- **测试文件数**: 6个主要测试类
- **测试代码行数**: 1,800+ 行
- **测试用例数**: 130+ 个
- **覆盖率**: 核心功能 95%+ 覆盖

运行测试:
```bash
mvn test
```

## 🔨 构建

### 从源码构建

```bash
# 克隆项目
git clone https://github.com/DuanYan007/markitdown-java.git
cd markitdown-java

# 编译打包
mvn clean package -DskipTests

# JAR 文件位置
target/markitdown-java-1.0.0-SNAPSHOT.jar
```

### 开发环境设置

```bash
# 1. 安装依赖
mvn clean install

# 2. 运行测试
mvn test

# 3. 生成测试报告
mvn jacoco:report
