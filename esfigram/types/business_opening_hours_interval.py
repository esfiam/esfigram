from __future__ import annotations
from esfigram.types.base_object import BaseObject


class BusinessOpeningHoursInterval(BaseObject):
    def __init__(self, opening_minute: int, closing_minute: int) -> None:
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute
        super().__init__(
            opening_minute=self.opening_minute,
            closing_minute=self.closing_minute,
        )