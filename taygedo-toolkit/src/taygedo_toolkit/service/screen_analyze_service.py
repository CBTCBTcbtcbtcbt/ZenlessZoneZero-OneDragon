from __future__ import annotations

from typing import Optional

import cv2
import numpy as np
from cv2.typing import MatLike

from one_dragon.base.matcher.ocr.onnx_ocr_matcher import OnnxOcrMatcher, OnnxOcrParam
from one_dragon.utils.log_utils import log
from taygedo_toolkit.config.demo_config import TaygedoDemoConfig
from taygedo_toolkit.service.types import OCRProbeResult, ScreenAnalyzeResult


class ScreenAnalyzeService:
    """Screen analysis pipeline: red flash detection + OCR probe."""

    def __init__(self, config: TaygedoDemoConfig) -> None:
        self.config = config
        self._ocr: Optional[OnnxOcrMatcher] = None
        self._ocr_ready = False
        self._init_ocr_once()

    def _init_ocr_once(self) -> None:
        self._ocr = OnnxOcrMatcher(
            OnnxOcrParam(
                use_gpu=False,
                det_limit_side_len=1920,
                use_angle_cls=False,
            )
        )

        try:
            self._ocr_ready = self._ocr.init_model(
                download_by_github=False,
                download_by_gitee=False,
                download_by_mirror_chan=False,
                skip_if_existed=True,
            )
            if self._ocr_ready:
                log.info("OCR initialized for taygedo demo")
            else:
                log.warning("OCR model not ready; demo will continue without OCR output")
        except Exception:
            self._ocr_ready = False
            log.warning("OCR init failed; demo will continue without OCR output", exc_info=True)

    def analyze(self, screen: MatLike) -> ScreenAnalyzeResult:
        red_detected, red_ratio = self._detect_red_flash(screen)
        ocr_result = self._probe_ocr(screen)

        if self.config.log_ocr_text and ocr_result.ok and ocr_result.text:
            log.info("OCR probe text: %s", ocr_result.text)

        return ScreenAnalyzeResult(
            red_flash_detected=red_detected,
            red_ratio=red_ratio,
            ocr_text=ocr_result.text,
        )

    def _detect_red_flash(self, screen: MatLike) -> tuple[bool, float]:
        roi = self._crop_roi(screen, self.config.red_detect_roi)
        if roi.size == 0:
            return False, 0.0

        hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)

        lower = np.array(self.config.red_hsv_lower, dtype=np.uint8)
        upper = np.array(self.config.red_hsv_upper, dtype=np.uint8)
        mask_main = cv2.inRange(hsv, lower, upper)

        # Include upper red hue range near 179 as fallback.
        lower_wrap = np.array([170, lower[1], lower[2]], dtype=np.uint8)
        upper_wrap = np.array([179, upper[1], upper[2]], dtype=np.uint8)
        mask_wrap = cv2.inRange(hsv, lower_wrap, upper_wrap)

        mask = cv2.bitwise_or(mask_main, mask_wrap)
        red_pixels = int(np.count_nonzero(mask))
        total_pixels = int(mask.size)
        ratio = (red_pixels / total_pixels) if total_pixels > 0 else 0.0

        detected = ratio >= self.config.red_pixel_ratio_threshold
        return detected, ratio

    def _probe_ocr(self, screen: MatLike) -> OCRProbeResult:
        if not self._ocr_ready or self._ocr is None:
            return OCRProbeResult(text="", ok=False, error="ocr_not_ready")

        roi_cfg = self.config.ocr_probe_roi or self.config.red_detect_roi
        roi = self._crop_roi(screen, roi_cfg)
        if roi.size == 0:
            return OCRProbeResult(text="", ok=False, error="roi_empty")

        try:
            text = self._ocr.run_ocr_single_line(roi, threshold=0.0, strict_one_line=False)
            return OCRProbeResult(text=text or "", ok=True)
        except Exception as exc:
            return OCRProbeResult(text="", ok=False, error=str(exc))

    @staticmethod
    def _crop_roi(screen: MatLike, roi: list[int]) -> MatLike:
        h, w = screen.shape[:2]
        x1, y1, x2, y2 = roi

        x1 = max(0, min(w - 1, x1))
        y1 = max(0, min(h - 1, y1))
        x2 = max(x1 + 1, min(w, x2))
        y2 = max(y1 + 1, min(h, y2))

        return screen[y1:y2, x1:x2]
