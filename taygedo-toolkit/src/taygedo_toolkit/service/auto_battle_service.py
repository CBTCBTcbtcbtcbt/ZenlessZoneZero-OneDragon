from __future__ import annotations

import threading
import time

from one_dragon.utils.log_utils import log
from taygedo_toolkit.config.demo_config import TaygedoDemoConfig
from taygedo_toolkit.controller.demo_pc_controller import DemoPcController
from taygedo_toolkit.service.screen_analyze_service import ScreenAnalyzeService


class AutoBattleService:
    """Minimal auto-battle loop service."""

    def __init__(
        self,
        config: TaygedoDemoConfig,
        controller: DemoPcController,
        analyzer: ScreenAnalyzeService,
    ) -> None:
        self.config = config
        self.controller = controller
        self.analyzer = analyzer

        self._running = False
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None
        self._last_right_click_ts = 0.0

    @property
    def is_running(self) -> bool:
        return self._running

    def start(self) -> None:
        if self._running:
            return

        self._stop_event.clear()
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, name="taygedo_auto_battle", daemon=True)
        self._thread.start()
        log.info("Auto-battle started")

    def pause(self) -> None:
        if not self._running:
            return

        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=1.0)
        self._thread = None
        self._running = False
        log.info("Auto-battle paused")

    def shutdown(self) -> None:
        self.pause()

    def _run_loop(self) -> None:
        left_interval = max(0.01, self.config.left_click_interval)
        screenshot_interval = max(0.01, self.config.screenshot_interval)

        next_left_click_ts = time.time()
        next_capture_ts = time.time()

        while not self._stop_event.is_set():
            now = time.time()

            if now >= next_left_click_ts:
                self.controller.left_click()
                next_left_click_ts = now + left_interval

            if now >= next_capture_ts:
                _, screen = self.controller.screenshot(independent=False)
                if screen is not None:
                    result = self.analyzer.analyze(screen)
                    if result.red_flash_detected:
                        self._handle_red_flash(result.red_ratio)
                next_capture_ts = now + screenshot_interval

            time.sleep(0.002)

    def _handle_red_flash(self, red_ratio: float) -> None:
        now = time.time()
        if now - self._last_right_click_ts < self.config.right_click_cooldown:
            return

        self.controller.right_click()
        self._last_right_click_ts = now
        log.info("Red flash detected (ratio=%.4f), right click triggered", red_ratio)
