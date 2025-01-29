from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional


class Birthdate(BaseObject):
    def __init__(self, day: int, month: int, year: Optional[int] = None) -> None:
        self.day = day
        self.month = month
        self.year = year
        super().__init__(day=day, month=month, year=year)