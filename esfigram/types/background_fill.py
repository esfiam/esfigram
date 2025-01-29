from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List


class BackgroundFill(BaseObject):
    def __init__(self, type: str) -> None:
        self.type = type
        super().__init__(type=type)


class BackgroundFillSolid(BackgroundFill):
    def __init__(self, color: int) -> None:
        self.color = color
        super().__init__(type="solid")


class BackgroundFillGradient(BackgroundFill):
    def __init__(self, top_color: int, bottom_color: int, rotation_angle: int) -> None:
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle
        super().__init__(type="gradient")


class BackgroundFillFreeformGradient(BackgroundFill):
    def __init__(self, colors: List[int]) -> None:
        self.colors = colors
        super().__init__(type="freeform_gradient")