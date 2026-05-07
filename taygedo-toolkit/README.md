# Taygedo Toolkit

这是一个最小可行的自动战斗 demo，结构刻意模仿 OneDragon 的分层方式，但去掉了前端，只保留后端流程。

## 综述

目标很单纯：

1. 按 `F9` 进入自动战斗，再按一次暂停。
2. 自动战斗期间持续左键点击。
3. 每轮截图，在指定 ROI 内识别红光。
4. 检测到红光时点击右键。
5. 同时执行一次轻量 OCR 探测，作为后续扩展的接口位。

## 技术栈

| 层 | 技术 | 作用 |
| --- | --- | --- |
| 语言 | Python 3.11 | demo 主体语言 |
| 框架复用 | `one_dragon` | Context、EventBus、Controller 基类 |
| 监听输入 | `pynput` | 监控键盘输入 |
| 模拟输入 | `pyautogui` + `pynput` | 左右键点击、窗口激活 |
| 截图 | `mss` / `pyautogui` | 获取目标窗口画面 |
| 图像处理 | `opencv-python` + `numpy` | 红光区域检测 |
| OCR | `onnxocr` / `onnxruntime` | 轻量文字探测 |
| 配置 | `PyYAML` + `YamlConfig` | sample 配置与运行配置 |

## Framework

这个 demo 的核心框架是 OneDragon 风格的“启动器 -> 应用 -> 上下文 -> 服务 -> 控制器”链路：

```text
run_demo.py
  -> launcher/cli.py
    -> TaygedoDemoApp
      -> DemoContext
        -> DemoPcController
        -> ScreenAnalyzeService
        -> AutoBattleService
        -> PcButtonListener
```

每一层只做一件事：

1. `launcher` 只负责启动。
2. `app` 只负责生命周期。
3. `context` 只负责组装依赖和分发按键事件。
4. `controller` 只负责窗口、截图、键鼠输出。
5. `service` 只负责识别和战斗循环。
6. `config` 只负责参数。

## 项目树

```text
taygedo-toolkit/
├─ README.md
├─ run_demo.py
├─ config/
│  ├─ README.md
│  └─ taygedo_demo.sample.yml
└─ src/taygedo_toolkit/
   ├─ README.md
   ├─ app/
   │  └─ README.md
   ├─ config/
   │  └─ README.md
   ├─ context/
   │  └─ README.md
   ├─ controller/
   │  └─ README.md
   ├─ launcher/
   │  └─ README.md
   └─ service/
      └─ README.md
```

## 关键运行流程

### 1. 启动入口

`run_demo.py` 负责把 `src/one_dragon` 和 `taygedo-toolkit/src` 加进 `PYTHONPATH`，再把命令行参数转发给真正的入口 `taygedo_toolkit.launcher.cli`。

### 2. 命令行入口

`src/taygedo_toolkit/launcher/cli.py` 只做参数解析和 app 启动；`--version` 会提前返回，不需要初始化任何游戏相关对象。

### 3. 应用生命周期

`src/taygedo_toolkit/app/demo_app.py` 创建 `DemoContext`，然后进入一个很轻的保活循环。真正的业务跑在后台线程里。

### 4. 上下文组装

`src/taygedo_toolkit/context/demo_context.py` 组装 `config`、`controller`、`analyzer`、`auto_battle`，并启动全局键盘监听。

### 5. 自动战斗循环

`src/taygedo_toolkit/service/auto_battle_service.py` 负责持续左键点击、定期截图、调用 `ScreenAnalyzeService` 检测红光、触发右键。

### 6. 屏幕分析

`src/taygedo_toolkit/service/screen_analyze_service.py` 先裁剪 ROI，再做 HSV 红色阈值检测，同时做一次 OCR 探测。

### 7. 控制器输出

`src/taygedo_toolkit/controller/demo_pc_controller.py` 只是对 OneDragon 的 `PcControllerBase` 再包一层，保留可替换性。

## 阅读路线

1. [launcher README](src/taygedo_toolkit/launcher/README.md)
2. [app README](src/taygedo_toolkit/app/README.md)
3. [context README](src/taygedo_toolkit/context/README.md)
4. [service README](src/taygedo_toolkit/service/README.md)
5. [controller README](src/taygedo_toolkit/controller/README.md)
6. [config README](src/taygedo_toolkit/config/README.md)
7. [root config README](config/README.md)

## 运行前提

这个 demo 不是独立安装包，它直接复用仓库根目录的 `src/one_dragon` 代码，所以运行前要满足两件事：

1. 在仓库根目录执行。
2. 依赖已安装，至少包括 `pyautogui`、`pynput`、`opencv-python`。

## 配置流

首次启动时，`TaygedoDemoConfig` 会尝试把 `config/taygedo_demo.sample.yml` 复制成 `config/taygedo_demo.yml`。
所以真正运行时读的是根目录下的 `config/taygedo_demo.yml`。

## 扩展点

1. 想换成别的游戏，只改 `window_title` 和 ROI。
2. 想把“红光识别”换成模板/YOLO，替换 `ScreenAnalyzeService` 即可。
3. 想加更多按键和状态，往 `DemoContext` 和 `AutoBattleService` 里加事件即可。
