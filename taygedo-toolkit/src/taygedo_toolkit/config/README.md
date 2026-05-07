# `config/`

这里是配置层实现。

## 文件树

```text
config/
├─ demo_config.py
└─ README.md
```

## `demo_config.py`

### 类: `TaygedoDemoConfig`

它继承 `YamlConfig`，所以天然支持：

1. 读取 YAML。
2. 保存 YAML。
3. 缺失时自动创建默认配置文件。

### 代码段 1: `_ensure_demo_config_exists()`

```python
target = config_dir / "taygedo_demo.yml"
sample = root / "taygedo-toolkit" / "config" / "taygedo_demo.sample.yml"
```

这段在做路径约定：

1. 示例配置放在 `taygedo-toolkit/config/`。
2. 运行配置放在仓库根目录 `config/`。

如果目标文件不存在，它会优先复制 sample。

### 代码段 2: 兜底默认值

```python
target.write_text(
    "window_title: \"ZenlessZoneZero\"\n"
    ...
)
```

如果 sample 也不在，它就直接写一份默认值。
这样 demo 依然能启动，不会卡在配置缺失。

### 代码段 3: 属性访问

```python
@property
def red_detect_roi(self) -> list[int]:
    return self._normalize_roi(self.get("red_detect_roi", [560, 220, 1360, 860]))
```

这个模式的好处是：

1. 外部拿到的是类型稳定的数据。
2. 业务层不用每次都做 `dict.get()`。
3. 默认值集中管理。

### 代码段 4: `_normalize_roi()`

```python
if x2 <= x1:
    x2 = x1 + 1
if y2 <= y1:
    y2 = y1 + 1
```

这段是最小的健壮性保护：

1. 防止输入坐标写反。
2. 防止裁剪空区域。

### 代码段 5: `_normalize_hsv()`

```python
if not isinstance(value, list) or len(value) != 3:
    return [0, 120, 120]
```

这段保证 HSV 配置一定是 3 个整数。
只要配置格式错了，就回退到默认值。

## 这个配置层为什么重要

1. Demo 后续扩展时，只要加字段，不用改调用链。
2. ROI、阈值、窗口标题都可以热调。
3. 和 OneDragon 原仓库的 YAML 风格保持一致。
