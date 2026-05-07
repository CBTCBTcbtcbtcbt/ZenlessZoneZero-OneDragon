from __future__ import annotations

from pathlib import Path
import shutil
from typing import Any, Optional

from one_dragon.base.config.yaml_config import YamlConfig
from one_dragon.utils.log_utils import log


class TaygedoDemoConfig(YamlConfig):
    """Minimal demo config, aligned with OneDragon YamlConfig style."""

    def __init__(self) -> None:
        self._ensure_demo_config_exists()
        super().__init__(module_name="taygedo_demo", sample=False, copy_from_sample=False)

    def _ensure_demo_config_exists(self) -> None:
        root = Path.cwd()
        config_dir = root / "config"
        config_dir.mkdir(parents=True, exist_ok=True)

        target = config_dir / "taygedo_demo.yml"
        sample = root / "taygedo-toolkit" / "config" / "taygedo_demo.sample.yml"

        if target.exists():
            return

        if sample.exists():
            shutil.copyfile(sample, target)
            log.info("Created demo config from sample: %s", target)
            return

        target.write_text(
            "window_title: \"ZenlessZoneZero\"\n"
            "key_start_running: \"f9\"\n"
            "key_stop_running: \"f10\"\n"
            "left_click_interval: 0.08\n"
            "right_click_cooldown: 0.20\n"
            "screenshot_interval: 0.05\n"
            "red_detect_roi: [560, 220, 1360, 860]\n"
            "red_hsv_lower: [0, 120, 120]\n"
            "red_hsv_upper: [12, 255, 255]\n"
            "red_pixel_ratio_threshold: 0.006\n"
            "ocr_probe_roi: null\n"
            "log_ocr_text: false\n",
            encoding="utf-8",
        )
        log.info("Created default demo config: %s", target)

    @property
    def window_title(self) -> str:
        return self.get("window_title", "ZenlessZoneZero")

    @property
    def key_start_running(self) -> str:
        return self.get("key_start_running", "f9")

    @property
    def key_stop_running(self) -> str:
        return self.get("key_stop_running", "f10")

    @property
    def left_click_interval(self) -> float:
        return float(self.get("left_click_interval", 0.08))

    @property
    def right_click_cooldown(self) -> float:
        return float(self.get("right_click_cooldown", 0.20))

    @property
    def screenshot_interval(self) -> float:
        return float(self.get("screenshot_interval", 0.05))

    @property
    def red_detect_roi(self) -> list[int]:
        return self._normalize_roi(self.get("red_detect_roi", [560, 220, 1360, 860]))

    @property
    def red_hsv_lower(self) -> list[int]:
        return self._normalize_hsv(self.get("red_hsv_lower", [0, 120, 120]))

    @property
    def red_hsv_upper(self) -> list[int]:
        return self._normalize_hsv(self.get("red_hsv_upper", [12, 255, 255]))

    @property
    def red_pixel_ratio_threshold(self) -> float:
        return float(self.get("red_pixel_ratio_threshold", 0.006))

    @property
    def ocr_probe_roi(self) -> Optional[list[int]]:
        value: Any = self.get("ocr_probe_roi", None)
        if value is None:
            return None
        return self._normalize_roi(value)

    @property
    def log_ocr_text(self) -> bool:
        return bool(self.get("log_ocr_text", False))

    @staticmethod
    def _normalize_roi(value: Any) -> list[int]:
        if not isinstance(value, list) or len(value) != 4:
            return [560, 220, 1360, 860]

        x1, y1, x2, y2 = [int(v) for v in value]
        if x2 <= x1:
            x2 = x1 + 1
        if y2 <= y1:
            y2 = y1 + 1
        return [x1, y1, x2, y2]

    @staticmethod
    def _normalize_hsv(value: Any) -> list[int]:
        if not isinstance(value, list) or len(value) != 3:
            return [0, 120, 120]
        return [int(value[0]), int(value[1]), int(value[2])]
