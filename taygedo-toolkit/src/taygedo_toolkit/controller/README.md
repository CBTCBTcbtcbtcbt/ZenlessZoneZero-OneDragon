# `controller/`

这里是输入输出控制层。

## 文件树

```text
controller/
├─ demo_pc_controller.py
└─ README.md
```

## `demo_pc_controller.py`

### 类: `DemoPcController`

它是一个很薄的包装器，直接继承 `PcControllerBase`。

### 代码段 1: 构造函数

```python
super().__init__(
    win_title=window_title,
    standard_width=standard_width,
    standard_height=standard_height,
)
```

这一步把窗口标题和标准分辨率交给 OneDragon 的控制器基类。
真正的窗口查找、截图、缩放、激活都在基类里完成。

### 代码段 2: 左键

```python
def left_click(self) -> None:
    self.btn_controller.tap("mouse_left")
```

这表示“让当前按钮控制器点击左键”。
`btn_controller` 默认是键鼠控制器，后续也可以切成手柄控制器。

### 代码段 3: 右键

```python
def right_click(self) -> None:
    self.btn_controller.tap("mouse_right")
```

和左键同理，只是按钮换成了右键。

## 依赖的 OneDragon 基类做了什么

`PcControllerBase` 负责的不是 demo 本身，而是通用控制能力：

1. `init_before_context_run()` 初始化截图环境。
2. `is_game_window_ready` 判断窗口是否存在。
3. `screenshot()` 获取当前窗口画面。
4. `btn_controller.tap()` 执行键鼠输入。

所以这个文件之所以短，是因为真正重活已经被基类承担了。

## 为什么这里仍然要保留一层 wrapper

1. 以后要换成别的游戏，只要改这个类。
2. 以后要加更多输入方法，也只改这一层。
3. 上层 `service` 不需要知道具体输入实现。
