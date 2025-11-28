# never_jscore

基于 Deno Core (V8) 的高性能 Python JavaScript 执行引擎，**专为 JS 逆向工程优化**。

[![PyPI](https://img.shields.io/pypi/v/never-jscore)](https://pypi.org/project/never-jscore/)
[![Python](https://img.shields.io/pypi/pyversions/never-jscore)](https://pypi.org/project/never-jscore/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**警告**：仅供技术研究和学习，请勿用于违法用途，后果自负。

- **技术交流群**：加微信 xu970821582
- 提醒: 基于pyo3库的更新迭代情况,个人推荐使用python3.14版本来使用此库,可能会避免很多奇怪的报错

---

## 为什么选择 never_jscore？

### 核心优势

| 特性 | never_jscore | PyMiniRacer | PyExecJS |
|------|--------------|-------------|----------|
| **Promise/async** | ✅ 完整支持 | ❌ 不支持 | ❌ 不支持 |
| **Hook 拦截** | ✅ 双模式：`$return()` + `$terminate()` | ❌ | ❌ |
| **确定性随机数** | ✅ 种子控制 | ❌ | ❌ |
| **Web API** | ✅ 完整（require/fetch/localStorage） | ❌ | ❌ |
| **性能（1000次调用）** | **11ms** 🏆 | 38ms | 69473ms |
| **上下文隔离** | ✅ 独立 V8 Isolate | ✅ | ⚠️ 进程隔离 |
| **类型提示** | ✅ .pyi 文件 | ⚠️ 部分 | ❌ |

### 专为逆向工程设计

- 🎣 **双模式 Hook 拦截**：
  - `$return()` - 快速拦截，适合简单场景
  - `$terminate()` - **V8 强制终止，无法被 try-catch 捕获**（v2.4.3+ 新增）
- 🎲 **确定性调试**：固定随机数种子，轻松调试动态加密算法
- 🌐 **零配置补环境**：内置 800+ 行 polyfill，自动模拟浏览器/Node.js 环境
- ⚡ **极致性能**：Rust + V8 直接绑定，比 PyExecJS 快 100-300 倍
- 🔄 **现代 JS 支持**：完整的 Promise、async/await、fetch、localStorage

### 性能基准测试

![img.png](img.png)

| 测试项目 | never_jscore | PyMiniRacer | PyExecJS |
|---------|-------------|-------------|----------|
| 简单计算 | 0.007ms | 0.005ms | 2.3ms |
| 字符串操作 | **0.004ms** 🏆 | 0.008ms | 2.3ms |
| 数组操作 | **0.004ms** 🏆 | 0.006ms | 2.3ms |
| 复杂算法(1000次) | **0.0111s** 🏆 | 0.0383s | 69.4735s |
| Promise | **✅ 0.003ms** | ❌ 不支持 | ❌ 不支持 |

---

## 快速开始

### 安装

```bash
pip install never-jscore
```

**支持平台**：Windows、Linux、macOS | **Python 版本**：3.8+

### 基本用法

```python
import never_jscore

# 创建独立的 JavaScript 执行环境
ctx = never_jscore.Context()

# 方式 1: 编译代码到全局作用域
ctx.compile("""
    function encrypt(text, key) {
        // 你的加密逻辑
        return btoa(text + key);
    }
""")

# 调用已定义的函数
result = ctx.call("encrypt", ["hello", "secret"])
print(result)  # 'aGVsbG9zZWNyZXQ='

# 方式 2: 一次性求值（不污染全局）
result = ctx.evaluate("1 + 2 + 3")
print(result)  # 6
```

### Promise 和 async/await（自动等待）

```python
ctx = never_jscore.Context()

# 定义异步函数
ctx.compile("""
    async function fetchUserData(userId) {
        // 模拟异步操作
        return await Promise.resolve({
            id: userId,
            name: "User" + userId,
            token: Math.random().toString(36)
        });
    }
""")

# 自动等待 Promise 完成
user = ctx.call("fetchUserData", [12345])
print(user)  # {'id': 12345, 'name': 'User12345', 'token': '0.xyz...'}

# Promise 链式调用
result = ctx.evaluate("""
    Promise.resolve(10)
        .then(x => x * 2)
        .then(x => x + 5)
""")
print(result)  # 25
```

---

## 高级功能

### 🎣 Hook 拦截：提取加密数据

在 JS 逆向中，经常需要拦截某个函数的调用并提取参数或返回值。never_jscore 提供**两种 Hook 模式**：

#### 模式 1: `$return()` - 快速拦截（可被 try-catch 捕获）

```python
ctx = never_jscore.Context()

# 适合简单场景
encrypted_data = ctx.evaluate("""
    (async () => {
        const originalSend = XMLHttpRequest.prototype.send;
        XMLHttpRequest.prototype.send = function(data) {
            $return({
                url: this._url,
                encrypted: data
            });
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://api.example.com/login');
        xhr.send(encryptedPayload);
    })()
""")

print(f"拦截到的加密数据: {encrypted_data['encrypted']}")
```

#### 模式 2: `$terminate()` - 强制终止（**无法被 try-catch 捕获** ⭐ v2.4.3+ 新增）

**关键特性：** 使用 V8 `terminate_execution()`，绕过所有 try-catch 防护！

```python
import json

ctx = never_jscore.Context()
ctx.clear_hook_data()  # 清空之前的数据（可选，会自动清空）

# Hook XMLHttpRequest.send
ctx.compile("""
    XMLHttpRequest.prototype.send = function(data) {
        // ⚡ 使用 $terminate 强制终止，无法被 try-catch 捕获
        $terminate({
            url: this._url,
            method: this._method,
            encrypted: data
        });
    };
""")

# 执行目标代码（即使有 try-catch 也会被终止）
try:
    ctx.evaluate("""
        try {
            const xhr = new XMLHttpRequest();
            xhr.open('POST', 'https://api.example.com/login');
            xhr.send(encryptedPayload);
        } catch (e) {
            // ❌ 这里不会执行 - $terminate 无法被捕获！
            console.log("Will not execute");
        }
    """)
except Exception as e:
    # ✅ Python 端捕获到终止
    print(f"JS 被强制终止: {e}")

# 获取拦截的数据
hook_data = ctx.get_hook_data()
if hook_data:
    data = json.loads(hook_data)
    print(f"拦截到的加密数据: {data['encrypted']}")

# ⚠️ 注意：每次 evaluate()/call() 前会自动清空 hook 数据
# 如果需要保留上一次的数据，必须在下一次执行前先读取
```

**两种模式对比：**

| 特性 | `$return()` | `$terminate()` ⭐ |
|------|-------------|-------------------|
| 速度 | ✅ 快 | ✅ 快 |
| try-catch | ⚠️ 可被捕获 | ✅ **无法被捕获** |
| 适用场景 | 简单 Hook | 对抗加固代码 |
| 数据获取 | 直接返回值 | `ctx.get_hook_data()` |
| 多次执行 | ✅ 可复用 Context | ⚠️ 建议清理后复用 |

**Hook API 总览**：
- **模式 1：** `$return(value)`, `$exit(value)`, `__neverjscore_return__(value)`
- **模式 2：** `$terminate(value)`, `__saveAndTerminate__(value)` ⭐ 新增

**典型应用场