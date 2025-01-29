from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Literal


class MaskPosition(BaseObject):
    def __init__(
        self,
        point: Literal["forehead", "eyes", "mouth", "chin"],
        x_shift: float,
        y_shift: float,
        scale: float,
    ) -> None:
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale
        super().__init__(
            point=point,
            x_shift=x_shift,
            y_shift=y_shift,
            scale=scale,
        )