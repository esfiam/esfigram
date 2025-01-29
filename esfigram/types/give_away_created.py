from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional


class GiveawayCreated(BaseObject):
    def __init__(self, prize_star_count: Optional[int] = None) -> None:
        self.prize_star_count: Optional[int] = prize_star_count
        super().__init__(prize_star_count=prize_star_count)