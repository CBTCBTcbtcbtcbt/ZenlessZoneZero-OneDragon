from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class ScreenAnalyzeResult:
    red_flash_detected: bool
    red_ratio: float
    ocr_text: str


@dataclass(slots=True)
class OCRProbeResult:
    text: str
    ok: bool
    error: Optional[str] = None
