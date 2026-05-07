# `context/`

这里是整个 demo 的组装层。

## 文件树

```text
context/
├─ demo_context.py
└─ README.md
```

## `demo_context.py`

### 类: `DemoKeyboardEventEnum`

```python
class DemoKeyboardEventEnum(Enum):
    PRESS = "demo_keyboard_press"
```

这只是一个事件名常量。
它的作用是给 `ContextEventBus` 一个统一的事件 ID。

### 类: `DemoContext`

这个类继承了 `ContextEventBus`，所以它天然拥有：

1. `dispatch_event()`
2. `listen_event()`
3. `unlisten_event()`

这就是 OneDragon 风格里“上下文既是容器，也是事件中心”的做法。

### 代码段 1: 组装依赖

```python
self.config = TaygedoDemoConfig()
self.controller = DemoPcController(window_title=self.config.window_title)
self.analyzer = ScreenAnalyzeService(self.config)
self.auto_battle = AutoBattleService(...)
```

这段是关键：

1. `config` 提供参数。
2. `controller` 提供窗口、截图和输入。
3. `analyzer` 提供图像识别。
4. `auto_battle` 提供自动循环。

### 代码段 2: 键盘监听器

```python
self._btn_listener = PcButtonListener(
    on_button_tap=self._on_key_press,
    listen_keyboard=True,
    listen_mouse=False,
)
```

这里复用了 OneDragon 的监听器。
它会把全局按键事件转成字符串回调，例如 `f9`、`f10`。

### 代码段 3: `init()`

```python
self.controller.init_before_context_run()
self._btn_listener.start()
```

这段做初始化：

1. 先让控制器准备好窗口和截图环境。
2. 再启动键盘监听。

### 代码段 4: `shutdown()`

```python
self.auto_battle.shutdown()
self._btn_listener.stop()
```

这段做收尾：

1. 停止自动战斗线程。
2. 停止键盘监听。

### 代码段 5: `_on_key_press()`

```python
if key == self.config.key_start_running:
    if self.auto_battle.is_running:
        self.auto_battle.pause()
    else:
        self.auto_battle.start()
elif key == self.config.key_stop_running:
    self.auto_battle.pause()
```

这是整个 demo 的入口逻辑：

1. `F9` 在启动和暂停之间切换。
2. `F10` 强制暂停。
3. 其余按键只是透传事件，不影响主流程。

### 设计原因

1. `Context` 只负责“把东西连起来”。
2. 业务状态不写在 UI 里。
3. 后续要加更多按键、状态机、识别器时，只需要继续往这里挂对象和事件。
