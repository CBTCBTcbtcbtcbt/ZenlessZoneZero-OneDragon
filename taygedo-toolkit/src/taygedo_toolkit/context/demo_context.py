from __future__ import annotations

import threading
from enum import Enum

from one_dragon.base.operation.context_event_bus import ContextEventBus
from one_dragon.utils.log_utils import log
from taygedo_toolkit.config.demo_config import TaygedoDemoConfig
from taygedo_toolkit.service.screen_analyze_service import ScreenAnalyzeService


class DemoKeyboardEventEnum(Enum):
    PRESS = "demo_keyboard_press"


class DemoContext(ContextEventBus):
    """Minimal context that mirrors OneDragon key-listen + dispatch pattern."""

    def __init__(self) -> None:
        super().__init__()

        self.config = TaygedoDemoConfig()
        try:
            from taygedo_toolkit.controller.demo_pc_controller import DemoPcController
        except ModuleNotFoundError as exc:
            log.error(
                "Missing dependency: %s. Install project dependencies first (for example: `uv sync`).",
                exc.name,
            )
            raise

        self.controller = DemoPcController(window_title=self.config.window_title)
        self.analyzer = ScreenAnalyzeService(self.config)
        from taygedo_toolkit.service.auto_battle_service import AutoBattleService

        self.auto_battle = AutoBattleService(self.config, self.controller, self.analyzer)

        self._lock = threading.Lock()
        self._ready = False

        from one_dragon.base.controller.pc_button.pc_button_listener import PcButtonListener

        self._btn_listener = PcButtonListener(
            on_button_tap=self._on_key_press,
            listen_keyboard=True,
            listen_mouse=False,
        )

    def init(self) -> None:
        with self._lock:
            if self._ready:
                return

            self.controller.init_before_context_run()
            if not self.controller.is_game_window_ready:
                log.warning(
                    "Target window not found by title '%s'; running anyway and waiting for it",
                    self.config.window_title,
                )

            self._btn_listener.start()
            self._ready = True
            log.info("Demo context initialized")

    def shutdown(self) -> None:
        with self._lock:
            if not self._ready:
                return

            self.auto_battle.shutdown()
            self._btn_listener.stop()
            self._ready = False
            log.info("Demo context shutdown")

    def _on_key_press(self, key: str) -> None:
        try:
            if key == self.config.key_start_running:
                if self.auto_battle.is_running:
                    self.auto_battle.pause()
                else:
                    self.auto_battle.start()
            elif key == self.config.key_stop_running:
                self.auto_battle.pause()

            self.dispatch_event(DemoKeyboardEventEnum.PRESS.value, key)
        except Exception:
            log.error("Key event handling failed", exc_info=True)
