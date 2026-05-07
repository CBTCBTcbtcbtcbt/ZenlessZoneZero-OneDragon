from __future__ import annotations

from one_dragon.base.controller.pc_controller_base import PcControllerBase


class DemoPcController(PcControllerBase):
    """Thin wrapper over OneDragon PC controller for demo use."""

    def __init__(self, window_title: str, standard_width: int = 1920, standard_height: int = 1080):
        super().__init__(
            win_title=window_title,
            standard_width=standard_width,
            standard_height=standard_height,
        )

    def left_click(self) -> None:
        self.btn_controller.tap("mouse_left")

    def right_click(self) -> None:
        self.btn_controller.tap("mouse_right")
