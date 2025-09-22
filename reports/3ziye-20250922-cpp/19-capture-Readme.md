# 高性能网络流量分析系统

## 系统概述
这是一个基于 PcapPlusPlus、PF_RING 和 ClickHouse 构建的高性能网络流量分析系统，专注于实时流量捕获、解析与存储。

## 核心特性
### 数据捕获能力
- ✨ 实时在线流量捕获和解析
- 📦 离线数据包文件解析支持
- 🚀 处理性能超过 2Gbps

### 流量分析引擎
- 🔄 维护动态流表（LUT）结构
- 🌐 支持网络层和传输层的统一流级表征
- 📊 提供基础流量统计分析功能

### 系统架构
- 💾 采用 ClickHouse 作为高性能数据仓库
- 🔌 集成 Python Socket 通信接口（端口 8888）
- 🛠️ 基于 PcapPlusPlus 和 PF_RING 的高效数据包处理

### 技术优势
- 高性能：突破 2Gbps 处理速率
- 灵活性：支持在线/离线双模式解析
- 可扩展：完整的数据存储与分析管道

这个系统完美结合了高性能网络数据捕获和现代数据仓库技术，为网络流量分析提供了一个强大而完整的解决方案。
# 编译和运行
可以直接在终端-执行任务，选择任务即可，也可以运行下列命令
```sh
# 编译
sudo cmake --build build/
# 运行
sudo ./bin/live_uni_pac_attr
# 如果没有加载pfring内核模块
sudo insmod /home/njust/program/PF_RING/kernel/pf_ring.ko
```
# sudo版本调试
在Vscode调试下使用Debug with sudo即可，配置已经在launch.json和tasks.json
# 常用命令参考指南
## 开发环境配置

### VSCode 相关
```bash
# root权限打开VScode
sudo code . --no-sandbox --user-data-dir='./usr-data/'

# 修改文件归属以解决提交commit、修改和打开vscode的权限问题
sudo chown njust:njust .
```
### 流量重放
```sh
apt install tcpreplay

sudo tcpreplay --topspeed -i enp7s0 "/home/njust/数据集/数据集调研/pcap/synthetic_attack/dataset/anonymized/full_anonymized/Sunday_2021-05-02_1206_adjusted.pcap"
```
###  列出pfring网卡
```sh
/home/njust/program/pfringPcapPlusPlus/PcapPlusPlus/build/examples_bin# ./PfRingTrafficFilter --list
    -> Name: enp7s0   Index: 3     MAC address: 14:d8:64:92:f0:cb   Available RX channels: 8   MTU: 1518
    -> Name: any      Index: N/A   MAC address: N/A                 Available RX channels: 0   MTU: 18
    -> Name: lo       Index: 1     MAC address: N/A                 Available RX channels: 1   MTU: 65554
    -> Name: eno1     Index: 2     MAC address: e8:9c:25:98:aa:2a   Available RX channels: 1   MTU: 1518
    -> Name: docker0  Index: 4     MAC address: 02:42:3a:d5:a3:68   Available RX channels: 1   MTU: 1518
    -> Name: br-e5358eb32785 Index: 5     MAC address: 02:42:a1:26:60:29   Available RX channels: 1   MTU: 1518
```


###  测试pfring
```sh
./PfRingTrafficFilter -n enp7s0
```

###  clickhouse
```sh
clickhouse-server
```
###  clickhouse的cpp通信库安装
```sh
git clone https://github.com/ClickHouse/clickhouse-cpp.git
cd clickhouse-cpp
git submodule update --init --recursive
cmake . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build
cd build 
make install
```
# 配置说明文档

## 1. 编译配置

### 使用libpcap版本
```bash
cmake -S . -B build -DPcapPlusPlus_ROOT=/home/njust/program/pcapplusplus-23.09-ubuntu-20.04-gcc-9.4.0-x86_64
```

### 使用PFRing版本
```bash
cmake -S . -B build -DPcapPlusPlus_ROOT=/home/njust/program/pfringPcapPlusPlus/LibPcapPlusPlus
```

## 2. 性能测试命令

### 程序执行与计时
```bash
# 基本计时命令
time ./bin/pcap2csv /home/njust/program/pcapplusplus-23.09-ubuntu-20.04-gcc-9.4.0-x86_64/backend-demo/data/traffic/数据集1/TrafficSets.txt /home/njust/program/pcapplusplus-23.09-ubuntu-20.04-gcc-9.4.0-x86_64/backend-demo/data/traffic/数据集1/FlowAttr.csv

# 详细计时（可选）
/usr/bin/time -v ./example-app "$1"

# 流量回放
tcpreplay --topspeed -i enp7s0 "/home/njust/数据集/数据集调研/pcap/synthetic_attack/dataset/anonymized/full_anonymized/Sunday_2021-05-02_1206_adjusted.pcap"
```

## 3. ClickHouse数据库操作

### 表操作
```sql
-- 创建数据包表
CREATE TABLE IF NOT EXISTS default.packets (
    insertTime DateTime DEFAULT now(),
    hashVal UInt32,
    packetLen Int32,
    tvSec UInt32,
    tvNsec UInt32,
    srcIp String,
    dstIp String,
    ttl UInt8,
    tos UInt8,
    id UInt16,
    offset UInt16,
    protocolIP UInt8,
    protocol UInt8,
    lenLoad UInt16,
    srcPort UInt16,
    dstPort UInt16,
    ackNum UInt32,
    seqNum UInt32,
    flag UInt16,
    window UInt16,
    lenUdp UInt16,
    icmpType UInt8,
    icmpCode UInt8
) 
ENGINE = MergeTree()
ORDER BY (insertTime,hashVal)

-- 删除表
DROP TABLE default.packets
DROP TABLE default.hashVal_summary
DROP TABLE default.protocol_hash_table
DROP TABLE default.src_ip_hash_table
```

### 查询操作
```sql
-- 查看表行数
SELECT count() FROM default.packets

-- 查看表大小
SELECT formatReadableSize(sum(data_compressed_bytes)) AS table_size
FROM system.parts
WHERE active AND database = 'default' AND table = 'numbers'

-- 统计分析
SELECT count(tvSec), min(tvSec), max(tvSec),
       avg(tvSec), stddevSamp(tvSec)
FROM default.packets;

-- 计算中位数
SELECT quantile(0.5)(tvSec) as median
FROM default.packets;
```

### 复杂查询示例
```sql
WITH filtered_hashVals AS (
    SELECT hashVal 
    FROM hashVal_summary 
    WHERE packet_count > 50 
          AND latest_insertTime < now() - INTERVAL 5 SECOND 
          AND packet_count - calculated_packet_count > 50
)
SELECT 
    hashVal,
    groupArray(ttl),
    groupArray(tos),
    groupArray(id),
    groupArray(offset),
    groupArray(packetLen),
    groupArray(tvNsec),
    groupArray(lenLoad),
    groupArray(ackNum),
    groupArray(seqNum),
    groupArray(flag),
    groupArray(window),
    groupArray(lenUdp),
    groupArray(icmpType),
    groupArray(icmpCode)
FROM packets
WHERE hashVal IN filtered_hashVals
GROUP BY hashVal;
```
## 查看版本和特定IP
```
query clickhouse version
SELECT version();
SELECT hashVal FROM default.src_ip_hash_table WHERE srcIp = '8.8.4.4';
```

##  列出所有的表和数据库
```
SHOW DATABASES;
SHOW TABLES;
```

