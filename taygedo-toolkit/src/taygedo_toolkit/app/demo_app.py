from __future__ import annotations

import signal
import threading
import time

from one_dragon.utils.log_utils import log
from taygedo_toolkit.context.demo_context import DemoContext


class TaygedoDemoApp:
    """Headless demo app lifecycle."""

    def __init__(self) -> None:
        self.ctx = DemoContext()
        self._stop_event = threading.Event()

    def run(self) -> None:
        self.ctx.init()
        self._register_signal_handlers()

        log.info("Press %s to start/pause auto battle", self.ctx.config.key_start_running)
        log.info("Press %s to force pause", self.ctx.config.key_stop_running)

        try:
            while not self._stop_event.is_set():
                time.sleep(0.2)
        finally:
            self.ctx.shutdown()

    def stop(self) -> None:
        self._stop_event.set()

    def _register_signal_handlers(self) -> None:
        def _handle_signal(signum, frame):
            log.info("Signal %s received, exiting", signum)
            self.stop()

        signal.signal(signal.SIGINT, _handle_signal)
        signal.signal(signal.SIGTERM, _handle_signal)
