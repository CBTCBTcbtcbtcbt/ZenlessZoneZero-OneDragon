# `service/`

这里是 demo 的业务核心。

## 文件树

```text
service/
├─ auto_battle_service.py
├─ screen_analyze_service.py
├─ types.py
└─ README.md
```

## `types.py`

### `ScreenAnalyzeResult`

```python
@dataclass(slots=True)
class ScreenAnalyzeResult:
    red_flash_detected: bool
    red_ratio: float
    ocr_text: str
```

这个结果对象把一次屏幕分析的三个输出打包起来：

1. 是否检测到红光。
2. 红色占比是多少。
3. OCR 识别出的文本是什么。

### `OCRProbeResult`

```python
@dataclass(slots=True)
class OCRProbeResult:
    text: str
    ok: bool
    error: Optional[str] = None
```

这个对象只描述 OCR 子任务本身：

1. `ok` 表示 OCR 是否真的可用。
2. `text` 是识别结果。
3. `error` 只在失败时记录原因。

## `screen_analyze_service.py`

### 类: `ScreenAnalyzeService`

这个类负责“看屏幕”。

### 代码段 1: 初始化 OCR

```python
self._ocr = OnnxOcrMatcher(OnnxOcrParam(...))
self._ocr_ready = self._ocr.init_model(...)
```

这里的设计意图是：

1. OCR 只初始化一次。
2. 如果模型不可用，demo 仍然能继续跑。
3. 不让 OCR 阻塞红光检测。

注意这里把下载开关关掉了，所以它不会在 demo 里主动联网拉模型。

### 代码段 2: `analyze()`

```python
red_detected, red_ratio = self._detect_red_flash(screen)
ocr_result = self._probe_ocr(screen)
```

一次分析分两条线并行思路：

1. 先做红光检测，这是主判定。
2. 再做 OCR 探测，这是扩展位。

### 代码段 3: `_detect_red_flash()`

```python
roi = self._crop_roi(screen, self.config.red_detect_roi)
hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
mask_main = cv2.inRange(hsv, lower, upper)
mask_wrap = cv2.inRange(hsv, lower_wrap, upper_wrap)
mask = cv2.bitwise_or(mask_main, mask_wrap)
```

这一段是红光识别的核心。

1. 先裁剪 ROI，减少计算量。
2. 再把 RGB 转成 HSV，方便做颜色阈值。
3. 红色在 HSV 里跨越 0 和 179，所以要补一个 `mask_wrap`。
4. 最后统计红色像素占比。

### 代码段 4: 红光判定

```python
detected = ratio >= self.config.red_pixel_ratio_threshold
```

这里不使用复杂模型，而是用像素比例阈值。
这样 demo 简单、快，也容易调。

### 代码段 5: `_probe_ocr()`

```python
text = self._ocr.run_ocr_single_line(roi, threshold=0.0, strict_one_line=False)
```

OCR 只做“探测”，不参与当前战斗判定。
如果模型不存在，函数会直接返回 `ocr_not_ready`。

### 代码段 6: `_crop_roi()`

```python
x1 = max(0, min(w - 1, x1))
y1 = max(0, min(h - 1, y1))
x2 = max(x1 + 1, min(w, x2))
y2 = max(y1 + 1, min(h, y2))
```

这段是坐标保护：

1. 防止 ROI 越界。
2. 防止 `x2 <= x1` / `y2 <= y1`。
3. 保证裁剪结果始终有效。

## `auto_battle_service.py`

### 类: `AutoBattleService`

这个类负责“怎么打”。

### 代码段 1: 运行状态

```python
self._running = False
self._stop_event = threading.Event()
self._thread = None
```

这三个变量表示：

1. 当前是否在跑。
2. 后台线程是否应该退出。
3. 线程对象本身。

### 代码段 2: `start()`

```python
self._stop_event.clear()
self._running = True
self._thread = threading.Thread(target=self._run_loop, ...)
```

启动时只做两件事：

1. 清除停止信号。
2. 拉起后台线程。

### 代码段 3: `pause()`

```python
self._stop_event.set()
if self._thread is not None:
    self._thread.join(timeout=1.0)
```

暂停时先发停止信号，再等线程收尾。
这比直接杀线程更安全。

### 代码段 4: `_run_loop()`

```python
if now >= next_left_click_ts:
    self.controller.left_click()

if now >= next_capture_ts:
    _, screen = self.controller.screenshot(independent=False)
    result = self.analyzer.analyze(screen)
```

这个循环把“点击”和“识别”分成两个独立节拍：

1. 左键节拍。
2. 截图节拍。

这样不会因为一次 OCR/识别变慢而把点击节奏拖死。

### 代码段 5: `_handle_red_flash()`

```python
if now - self._last_right_click_ts < self.config.right_click_cooldown:
    return
```

这段是右键冷却。
没有这个限制的话，红光出现时可能会连续右键多次。

### 这一层的扩展口

1. 想换成“红光 + 文字”双判定，改 `analyze()`。
2. 想加闪避键、技能键，往 `_run_loop()` 里加分支即可。
3. 想换成状态机，保留这个 service 作为最外层调度器。
