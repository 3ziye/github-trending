# 多交易所策略自动化系统

**Multi-Exchange Strategy Automation System**

## 🎯 项目简介

这是一个企业级的多交易所加密货币自动化交易系统，提供高性能、高可靠性的网格交易、刷量交易、套利监控和市场监控功能。系统采用严格的分层架构设计，支持 Hyperliquid、Backpack、Lighter、Binance、OKX、EdgeX 等多个交易所的完整适配。

## 🏗️ 核心系统架构

### 系统组件

```
多交易所策略自动化系统
├── 📊 网格交易系统 (Grid Trading)
│   ├── 普通网格              # 固定价格区间网格
│   ├── 马丁网格              # 马丁格尔递增策略
│   ├── 价格移动网格          # 动态跟随价格
│   ├── 剥头皮模式            # 快速止损策略
│   ├── 智能剥头皮            # 多次深跌检测
│   ├── 本金保护模式          # 自动止损保护
│   ├── 止盈模式              # 到达目标自动平仓
│   └── 现货预留管理          # 现货币种预留
├── 🔍 网格波动率扫描器 (Grid Volatility Scanner)
│   ├── 虚拟网格模拟          # 无需实际下单的模拟网格
│   ├── 实时APR计算           # 准确预测年化收益率
│   ├── 代币排行榜            # 按波动率和APR排序
│   ├── 智能评级系统          # S/A/B/C/D等级评估
│   └── 终端 UI              # Rich 实时监控界面
├── 💹 刷量交易系统 (Volume Maker)
│   ├── 挂单模式              # 限价单刷量（Backpack）
│   └── 市价模式              # 市价单快速刷量（Lighter）
├── 🔄 套利监控系统 (Arbitrage Monitor)
│   ├── 价格监控              # 实时价格差监控
│   ├── 资金费率监控          # 跨交易所费率差异
│   ├── 套利机会识别          # 价差和费率套利
│   ├── 终端 UI              # Rich 实时监控界面
│   └── 交易对自动发现        # 多交易所交易对匹配
├── 🔔 价格提醒系统 (Price Alert)
│   ├── 价格突破监控          # 价格触及目标提醒
│   ├── 多交易所支持          # 支持所有接入的交易所
│   ├── 终端 UI              # 实时价格显示
│   └── 声音提醒              # 突破时声音通知
├── 🔗 交易所适配层 (Exchange Adapters)
│   ├── Hyperliquid 适配器    # 永续合约 + 现货
│   ├── Backpack 适配器       # 永续合约
│   ├── Lighter 适配器        # 永续合约（低手续费）
│   ├── Binance 适配器        # 现货 + 永续合约
│   ├── OKX 适配器            # 现货 + 永续合约
│   ├── EdgeX 适配器          # 永续合约
│   └── 统一接口标准          # 标准化 API 接口
└── 🏛️ 基础设施层 (Infrastructure)
    ├── 依赖注入容器          # DI 容器管理
    ├── 事件系统              # 事件驱动架构
    ├── 日志系统              # 结构化日志
    ├── 配置管理              # YAML 配置系统
    └── 数据聚合器            # 多交易所数据聚合
```

## 🚀 快速开始

### 系统要求

- Python 3.8+
- 支持的操作系统：Linux、macOS、Windows
- 可选：tmux（用于多进程管理）

### 安装依赖

```bash
# 安装 Python 依赖
pip install -r requirements.txt
```

### 配置 API 密钥

在 `config/exchanges/` 目录下配置对应交易所的 API 密钥：

```bash
config/exchanges/
├── hyperliquid_config.yaml   # Hyperliquid 配置
├── backpack_config.yaml       # Backpack 配置
├── lighter_config.yaml        # Lighter 配置
├── binance_config.yaml        # Binance 配置
├── okx_config.yaml            # OKX 配置
└── edgex_config.yaml          # EdgeX 配置
```

### 快速启动各系统

#### 网格交易系统
```bash
python3 run_grid_trading.py config/grid/lighter-long-perp-btc.yaml
```

#### 刷量交易系统（Backpack挂单模式）
```bash
python3 run_volume_maker.py config/volume_maker/backpack_btc_volume_maker.yaml
```

#### 刷量交易系统（Lighter市价模式）
```bash
python3 run_lighter_volume_maker.py config/volume_maker/lighter_volume_maker.yaml
```

#### 套利监控系统
```bash
python3 run_arbitrage_monitor.py
```

#### 价格提醒系统
```bash
python3 run_price_alert.py config/price_alert/binance_alert.yaml
```

#### 网格波动率扫描器
```bash
python3 grid_volatility_scanner/run_scanner.py
```

## 📋 核心功能详解

### 1️⃣ 网格交易系统

#### 功能特性

- **多种网格模式**：普通网格、马丁网格、价格移动网格
- **智能策略**：剥头皮、智能剥头皮、本金保护、止盈模式
- **健康检查**：自动订单校验和修复机制
- **终端 UI**：实时监控界面，显示持仓、盈亏、网格状态
- **现货支持**：现货预留管理（自动维持币种余额）
- **多交易所**：支持 Hyperliquid、Backpack、Lighter

#### 配置文件位置

```
config/grid/
├── lighter_btc_perp_long.yaml              # Lighter BTC 做多
├── lighter_btc_perp_short.yaml             # Lighter BTC 做空
├── hyperliquid_btc_perp_long.yaml          # Hyperliquid BTC 做多
├── hyperliquid_btc_perp_short.yaml         # Hyperliquid BTC 做空
├── hyperliquid_btc_spot_long.yaml          # Hyperliquid 现货做多
├── backpack_capital_protection_long_btc.yaml   # Backpack BTC 本金保护
├── backpack_capital_protection_long_eth.yaml   # Backpack ETH 本金保护
├── backpack_capital_protection_long_sol.yaml   # Backpack SOL 本金保护
├── backpack_capital_protection_long_bnb.yaml   # Backpack BNB 本金保护
└── backpack_capital_protection_long_hype.yaml  # Backpack HYPE 本金保护
```

#### 启动方式

```bash
# 方式1：直接启动（推荐）
python3 run_grid_trading.py config/grid/lighter_btc_perp_long.yaml
python3 run_grid_trading.py config/grid/lighter_eth_perp_long.yaml

# 方式2：DEBUG 模式启动（查看详细日志）
python3 run_grid_trading.py config/grid/lighter_btc_perp_long.yaml --debug

# 方式3：使用 Shell 脚本批量启动（tmux）
./scripts/start_all_grids.sh
```

#### 核心文件

| 文件路径 | 说明 |
|---------|------|
| `run_grid_trading.py` | 网格交易系统主启动脚本 |
| `core/services/grid/coordinator/grid_coordinator.py` | 网格系统协调器（核心逻辑） |
| `core/services/grid/implementations/grid_engine_impl.py` | 网格执行引擎 |
| `core/services/grid/implementations/grid_strategy_impl.py` | 网格策略实现 |
| `core/services/grid/implementations/position_tracker_impl.py` | 持仓跟踪器 |
| `core/services/grid/implementations/order_health_checker.py` | 订单健康检查器 |
| `core/services/grid/scalping/scalping_manager.py` | 剥头皮管理器 |
| `core/services/grid/scalping/smart_scalping_tracker.py` | 智能剥头皮追踪器 |
| `core/services/grid/capital_protection/capital_protection_manager.py` | 本金保护管理器 |
| `core/services/grid/terminal_ui.py` | 终端 UI 界面 |

### 2️⃣ 刷量交易系统

#### 功能特性

- **双交易模式**：挂单模式（Backpack）、市价模式（Lighter）
- **信号源支持**：Backpack REST API、Hyperliquid WebSocket
- **智能判断**：买卖单数量对比、价格变动监控
- **实时统计**：成交量、