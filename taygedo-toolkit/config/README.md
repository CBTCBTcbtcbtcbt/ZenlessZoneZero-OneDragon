# `config/`

这里放 demo 的示例配置。

## 文件树

```text
config/
├─ taygedo_demo.sample.yml
└─ README.md
```

## `taygedo_demo.sample.yml`

这个文件是样板配置。程序第一次运行时，会把它复制到仓库根目录的 `config/taygedo_demo.yml`。

### 字段说明

1. `window_title`
   - 目标游戏窗口标题。
   - `PcGameWindow` 会根据这个标题找窗口。

2. `key_start_running`
   - 启动/暂停自动战斗的按键。
   - 默认 `F9`。

3. `key_stop_running`
   - 强制暂停按键。
   - 默认 `F10`。

4. `left_click_interval`
   - 连续左键的间隔。
   - 越小点击越密。

5. `right_click_cooldown`
   - 检测到红光后，右键的冷却时间。
   - 防止一帧红光触发很多次右键。

6. `screenshot_interval`
   - 截图频率。
   - 这个值越小，检测越快，但开销越高。

7. `red_detect_roi`
   - 红光检测区域，格式是 `[x1, y1, x2, y2]`。
   - 默认是 1920x1080 参考坐标。

8. `red_hsv_lower` / `red_hsv_upper`
   - 红色阈值范围。
   - `ScreenAnalyzeService` 会先把 ROI 转成 HSV，再做 `cv2.inRange()`。

9. `red_pixel_ratio_threshold`
   - 红色像素占比阈值。
   - 超过这个比例就认为“出现红光”。

10. `ocr_probe_roi`
    - OCR 探测区域。
    - 为空时，默认复用 `red_detect_roi`。

11. `log_ocr_text`
    - 是否把 OCR 结果打印到日志。
    - 只是调试辅助，不影响主循环。

## 这一层的代码逻辑

配置类在 `src/taygedo_toolkit/config/demo_config.py`。
它做了两件事：

1. 保证配置文件存在。
2. 把 YAML 中的原始值转换成类型稳定的 Python 属性。

## 使用建议

1. 先调整 `window_title`。
2. 再调 `red_detect_roi`。
3. 最后调 `red_pixel_ratio_threshold`。
