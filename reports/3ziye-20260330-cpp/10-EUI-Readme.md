# EUI-NEO

EUI-NEO 是一个基于 OpenGL + GLFW 的声明式 2D GUI 框架。

- 组件放在 `src/components`，尽量一个组件一个 `.h`

<p align="center">
  <img src="./docs/1.jpg" alt="EUI-NEO Preview 1" width="49%" />
  <img src="./docs/2.jpg" alt="EUI-NEO Preview 2" width="49%" />
  <img src="./docs/3.jpg" alt="EUI-NEO Preview 3" width="49%" />
  <img src="./docs/4.jpg" alt="EUI-NEO Preview 4" width="49%" />
</p>

## 目录

```text
EUI-NEO/
├─ main.cpp
├─ README.md
├─ app/
│  ├─ basic_demo.cpp
│  ├─ calculator_demo.cpp
│  ├─ calculator_logic.h
|  └─ calculator_demo.h
├─ docs/
│  ├─ ui_dsl_analysis.md
│  └─ gpui_full_redraw_optimization.md
├─ src/
│  ├─ EUINEO.h
│  ├─ EUINEO.cpp
│  ├─ app/
│  │  └─ DslAppRuntime.h
│  ├─ components/
│  │  ├─ Button.h
│  │  ├─ ComboBox.h
│  │  ├─ CustomNodeTemplate.h
│  │  ├─ InputBox.h
│  │  ├─ Label.h
│  │  ├─ Panel.h
│  │  ├─ Polygon.h
│  │  ├─ ProgressBar.h
│  │  ├─ ScrollArea.h
│  │  ├─ SegmentedControl.h
│  │  ├─ Sidebar.h
│  │  └─ Slider.h
│  ├─ pages/
│  │  ├─ AnimationPage.h
│  │  ├─ HomePage.h
│  │  ├─ LayoutPage.h
│  │  ├─ MainPage.h
│  │  └─ TypographyPage.h
│  ├─ ui/
│  │  ├─ UIBuilder.h
│  │  ├─ UIComponents.def
│  │  ├─ UIContext.cpp
│  │  ├─ UIContext.h
│  │  ├─ UINode.h
│  │  ├─ UIPrimitive.cpp
│  │  └─ UIPrimitive.h
│  └─ font/
│     ├─ Font Awesome 7 Free-Solid-900.otf
│     └─ YouSheBiaoTiHei-2.ttf
└─ CMakeLists.txt
```

## 当前演示页面

- `Home`
  - 基础控件页
  - 顶部按钮区 + 下方两列表单区
  - `Outline` 按钮会随机切换主题主色

- `Animation`
  - 自定义 `AnimationCardNode`
  - 演示 `Color / scale / rotation / gradient / queue` 动画轨道

- `Layout`
  - `row() / column() / flex()` 最小示例页
  - 一个滑条控制左右 `flex` 比例
  - 用来测试底层布局 DSL

- `Typography`
  - SDF 文本预览页
  - 展示不同字号、混排文本和图标字体效果

## 编译

```bash
cmake -B build -G Ninja
cmake --build build --config Release
```

## 运行

入口在 `main.cpp`。主循环是事件驱动重绘：

```cpp
EUINEO::MainPage mainPage{};

while (!glfwWindowShouldClose(window)) {
    if (EUINEO::State.needsRepaint ||
        EUINEO::State.animationTimeLeft > 0.0f ||
        mainPage.WantsContinuousUpdate()) {
        mainPage.Update();
    }

    if (EUINEO::Renderer::ShouldRepaint()) {
        EUINEO::Renderer::BeginFrame();
        mainPage.Draw();
    }
}
```

## app 目录说明

`app/` 是业务开发目录，给使用者放自己的页面入口和逻辑代码，不是框架底层目录。

- `app/*.cpp`：一个文件对应一个可执行入口（一个 demo / 一个应用入口）
- `app/*.h`：页面逻辑、状态、业务函数
- `src/`：框架源码（组件、渲染、布局、运行时）

当前示例：

- `app/basic_demo.cpp`
- `app/calculator_demo.cpp`
- `app/calculator_logic.h`

如果你使用声明式 UI 运行时，入口函数是 `src/app/DslAppRuntime.h` 里的 `RunDslApp`。常见写法是：

```cpp
// app/xxx_demo.cpp
int main() {
    EUINEO::DslAppConfig config;
    // window / page / fps 配置
    return EUINEO::RunDslApp(config, composeFn);
}
```

```cpp
// app/xxx_logic.h
struct XxxLogic {
    // 状态、输入处理、计算逻辑
};
```

## DSL 运行配置

`DslAppConfig` 现在支持帧率配置：

```cpp
EUINEO::DslAppConfig config;
config.title = "EUI Demo";
config.width = 800;
config.height = 600;
config.pageId = "demo";
config.fps = 120;
```

- `config.fps <= 0`：默认垂直同步（VSync）
- `config.fps > 0`：关闭 VSync，按目标帧率限帧
- 不写 `fps` 时默认值是 `0`，等价于垂直同步

## 字体与回退

字体加载入口也在 `main.cpp`，当前主要配置是：

```cpp
constexpr const char* kUIFontFile = "YouSheBiaoTiHei-2.ttf";
constexpr const char* kIconFontFile = "Font Awesome 7 Free-Solid-900.otf";
constexpr float kUiSdfLoadSize = 72.0f;
constexpr float kIconSdfLoadSize = 96.0f;
constexpr float kCjkSdfLoadSize = 72.0f;
```

项目字体默认会从下面两个目录里找：

- `src/font/`
- `font/`

如果你要改主文本字体：

1. 把字体文件放到 `src/font/`
2. 修改 `main.cpp` 里的 `kUIFontFile`
3. 按需要调整 `kUiSdfLoadSize`

如果你要改图标字体：

1. 把图标字体放到 `src/font/`
2. 修改 `main.cpp` 里的 `kIconFontFile`
3. 按需要调整 `main.cpp` 里预加载的 icon codepoint

当前文本渲染约定：

- 普通文本走 SDF
- 图标字体走普通 bitmap alpha，不走 SDF

当前默认系统字体回退：

- 主 UI 字体文件如果加载失败，会按下面顺序回退：
  - `C:/Windows/Fonts/msyh.ttc`
  - `C:/Windows/Fonts/arial.ttf`
- 中文缺字回退使用：
  - `C:/Windows/Fonts/msyh.ttc`

当前中文缺字回退是延迟加载：

- 启动时不会直接把 `msyh.ttc` 整包读进内存
- 只有项目字体缺某个字时，才会加载 `msyh.ttc` 并生成对应 glyph

## 页面写法

页面层目标是只写布局和声明，不回流到组件内部实现。

```cpp
ui.begin("main");

ui.sidebar("sidebar")
    .position(sidebarX, sidebarY)
    .size(sidebarWidth, sidebarHeight)
    .width(60.0f, 86.0f)
    .brand("EUI", "NEO")
    .selectedIndex(static_cast<int>(currentView_))
    .item("\xEF\x80\x95", "Home", [this] { SwitchView(MainPageView::Home); })
    .item("\xEF\x81\x8B", "Animation", [this] { SwitchView(MainPageView::Animation); })
    .item("\xEF\x80\x89", "Layout", [this] { SwitchView(MainPageView::Layout); })
    .item("\xEF\x80\xB1", "Typography", [this] { SwitchView(MainPageView::Typography); })
    .themeToggle([this] { ToggleTheme(); })
    .build();

ComposeCurrentPage(PageBounds());

ui.end();
```

当前真实参考：

- `src/pages/MainPage.h`
- `src/pages/HomePage.h`
- `src/pages/AnimationPage.h`
- `src/pages/LayoutPage.h`
- `src/pages/TypographyPage.h`

## Row / Column / Flex

现在底层已经有三种布局写法：

- `ui.row()`
- `ui.column()`
- `ui.flex()`

其中：

- `row()` 是横向排布
- `column()` 是纵向排布
- `flex()` 是通用弹性容器，靠 `.direction(...)` 选横向或纵向
- 子项用 `.flex(n)` 吃剩余空间

最简单示例：

```cpp
ui.column()
    .position(bounds.x, bounds.y)
    .size(bounds.width, bounds.height)
   