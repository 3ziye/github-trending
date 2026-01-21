[![GitHub release (latest by date)](https://img.shields.io/github/v/release/darkfiv/DouSql?style=flat-square&logo=github)](https://github.com/darkfiv/DouSql/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/darkfiv/DouSql?style=flat-square&logo=github)](https://github.com/darkfiv/DouSql/stargazers)
[![GitHub downloads](https://img.shields.io/github/downloads/darkfiv/DouSql/total?style=flat-square&logo=github)](https://github.com/darkfiv/DouSql/releases)
[![Burp Suite](https://img.shields.io/badge/Burp%20Suite-2024.6+-orange?style=flat-square&logo=portswigger)](https://portswigger.net/burp)


## 插件简介

**DouSql** 是基于Xia Sql二次开发的高度自定义化SQL注入检测插件，专为安全研究人员和渗透测试工程师打造。


## 主要功能
<img width="3012" height="1628" alt="image" src="https://github.com/user-attachments/assets/936e5d1b-9103-40b3-8286-cc91d60eb4ca" />
<img width="2992" height="1602" alt="image" src="https://github.com/user-attachments/assets/94cc3688-22af-4d64-b5bb-47e1970bf07b" />


### 核心检测功能
- **多种SQL注入检测**：支持报错注入、时间盲注、布尔盲注等多种检测方式
- **智能payload管理**：内置7个payload组，包含Mysql、Mssql、Oracle等。
- **实时响应分析**：自动分析响应长度、时间、状态码等关键指标
- **全面的报错信息识别**：内置33种数据库和框架的错误信息模式，支持MySQL、Oracle、PostgreSQL、SQL Server、SQLite等
- **增强JSON处理**：使用Burp Suite内置API处理复杂嵌套JSON结构，支持任意深度的对象、数组和混合数据类型


### 高级配置选项
- **参数过滤系统**：支持白名单/黑名单模式，精确控制测试范围
- **URL黑名单过滤**：可配置黑名单URL，跳过不需要测试的路径
- **静态文件过滤**：自动跳过图片、样式、脚本等静态资源文件（支持30+种文件类型）
- **响应时间阈值**：可自定义时间盲注检测阈值
- **长度差异阈值**：可配置响应长度差异检测敏感度
- **自定义延时发包**：支持固定延时和随机延时，可配置延时区间（默认1-5秒）
- **自定义追加参数**：支持为请求自动追加多个指定参数，兼容URL、POST、JSON等格式
- **智能参数测试控制**：追加参数可选择是否参与payload测试，提供灵活的测试策略

### 最新功能亮点
- **完全修复中文参数编码问题**：支持UTF-8、GBK、GB2312等多种编码格式
- **智能编码检测与修复**：自动识别并修复参数传递过程中的编码损坏
- **增强JSON处理能力**：完美支持复杂嵌套JSON结构的中文参数
- **优化默认payload**：更新18个高质量SQL注入检测payload
- **payload管理优化**：分离保存和加载功能，操作更直观
- **自定义延时发包**：支持三种延时模式，可配置固定或随机延时，避免WAF检测
- **智能追加参数**：支持URL、POST、JSON三种格式的多参数自动追加，每个参数可独立控制测试开关

### 用户界面特性
- **双面板设计**：左侧显示扫描结果，右侧显示参数测试详情
- **实时状态更新**：支持报错标记(err)、时间超时标记(time)、长度差异标记(diff)等状态显示
- **停止测试功能**：右键点击扫描结果中的URL，可选择停止该URL的测试
- **删除测试结果**：右键点击扫描结果，可删除单个结果；清空所有结果可使用控制面板的"清空列表"按钮
- **配置持久化**：所有配置自动保存，重启后自动恢复
- **Windows系统优化**：针对Windows系统进行UI布局优化，确保所有按钮和组件完整显示

### 工具集成
- **智能右键菜单**：支持payload组选择、停止测试、删除结果等多种操作
- **选择性监控**：默认只监控Proxy和Repeater的流量，需要手动启用对应的监控选项
- **自动检测**：通过右键菜单发送的请求会自动进行检测
- **多格式参数支持**：支持URL参数、POST参数、JSON参数、XML参数、Cookie参数等
- **灵活测试策略**：可根据不同场景选择合适的payload组，如盲注场景使用blind-injection-fuzz组，登录场景使用login-password-injection-fuzz组，WAF绕过使用union-select-bypass组

### 监控模式说明
- **Proxy监控**：启用后自动检测通过Proxy的所有HTTP流量
- **Repeater监控**：启用后自动检测Repeater发送的请求
- **Scanner/Intruder**：默认不自动监控，可通过右键菜单手动发送到插件
- **右键发送**：所有工具都支持通过右键菜单发送请求到插件进行检测
  - **使用当前组**：使用插件界面当前选中的payload组进行测试
  - **指定payload组**：可选择特定的payload组（如default、blind-injection-fuzz、login-password-injection-fuzz、union-select-bypass等）进行针对性测试

### 配置目录位置

**默认配置目录（推荐）：**
```bash
# Windows
C:\Users\[用户名]\dousql\

# macOS
/Users/[用户名]/dousql/

# Linux  
/home/[用户名]/dousql/
```

**配置文件结构：**
```
~/dousql/
├── xia_SQL_diy_payload_default.ini                    # default payload配置
├── xia_SQL_payload_orderby.ini                        # order测试组payload配置
├── xia_SQL_payload_blind-injection-fuzz.ini           # 盲注专用payload配置
├── xia_SQL_payload_login-password-injection-fuzz.ini  # 登录绕过payload配置
├── xia_SQL_payload_mssql-payloads-fuzz.ini            # MSSQL专用payload配置
├── xia_SQL_payload_oracle-payloads-fuzz.ini           # Oracle专用payload配置
├── xia_SQL_payload_union-select-bypass.ini            # UNION绕过payload配置
├── xia_SQL_diy_error_default.ini                      # 自定义报错关键字
├── xia_SQL_response_time_threshold.ini                # 响应时间阈值配置
├── xia_SQL_length_diff_threshold.ini                  # 长度差异阈值配置
├── xia_SQL_blacklist_urls.ini                         # 黑名单URL配置
├── xia_SQL_whitelist.ini                              # 白名单参数配置
├── xia_SQL_blacklist.ini                              # 黑名单参数配置
└── xia_SQL_param_filter_mode.ini                      # 参数过滤模式配置
```

**特殊情况（jar包同级）：**
```
/path/to/extensions/
├── DouSql-6.jar          # 插件jar包
└── dousql/                   # 配置文件目录
    ├── xia_SQL_diy_payload.ini
    ├── xia_SQL_payload_timebased.ini
    └── ...
```

**配置目录检测日志示例：**
```
ProtectionDomain路径: /var/folders/.../tmp/burp.../20
使用用户主目录: /Users/username
hello DouSQL!
你好 欢迎使用 DouSQL!
version:3.0. (Montoya API)
jar包目录: /Users/username
配置文件目录: /Users/username/dousql
```

## 快速开始

### 方式一：直接下载
从 [Releases](https://github.com/darkfiv/DouSql/releases) 页面下载最新版本的jar文件

### 方式二：从源码编译
```bash
git clone https://github.com/darkfiv/DouSql.git
cd DouSql
mvn clean package
```

### 加载到Burp Suite
1. 打开Burp Suite
2. 进入 Extensions → Installed
3. 点击 Add 按钮
4. 选择编译生成的jar文件
5. 插件加载成功后，会在标签页看到"DouSQL"

## 使用方法

### 编译插件

**环境要求：**
- Java 11+
- Maven 3.x

**编译步骤：**
```bash
# 克隆项目
git clone https://github.com/darkfiv/DouSql.git
cd DouSql

# 编译打包
mvn clean package

# 编译完成后，jar文件位于：
# target/DouSql-3.0.6.jar
```

### 安装使用

1. 将编译生成的jar文件加载到Burp Suite
2. 在Extensions标签页中找到"DouSQL"插件
3. 配置相关检测参数和阈值
4. 通过右键菜单或监控模式发送请求进行检测
5. 查看扫描结果和参数测试详情