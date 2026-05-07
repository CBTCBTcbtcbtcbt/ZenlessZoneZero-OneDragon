# `app/`

这里是应用生命周期层。

## 文件树

```text
app/
├─ demo_app.py
└─ README.md
```

## `demo_app.py`

### 类: `TaygedoDemoApp`

这个类只做三件事：

1. 创建 `DemoContext`。
2. 持续保活。
3. 退出时统一清理资源。

### 代码段 1: 初始化

```python
def __init__(self) -> None:
    self.ctx = DemoContext()
    self._stop_event = threading.Event()
```

这段完成两个对象：

1. `DemoContext`，真正的运行上下文。
2. `_stop_event`，用于让主循环退出。

### 代码段 2: `run()`

```python
def run(self) -> None:
    self.ctx.init()
    self._register_signal_handlers()
```

先初始化上下文，再注册系统信号。
这样 Ctrl+C 或 SIGTERM 都能让程序平滑退出。

### 代码段 3: 保活循环

```python
try:
    while not self._stop_event.is_set():
        time.sleep(0.2)
finally:
    self.ctx.shutdown()
```

这个循环不做业务，只是让进程一直活着。
真正的业务在 `AutoBattleService` 的后台线程里。

### 代码段 4: 信号处理

```python
def _register_signal_handlers(self) -> None:
    def _handle_signal(signum, frame):
        self.stop()
```

它把系统退出信号转换成 `_stop_event.set()`。
这样 `finally` 会执行，资源会被统一释放。

## 结论

`app` 层不写业务，只写“怎么开始”和“怎么结束”。
