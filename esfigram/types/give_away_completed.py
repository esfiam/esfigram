from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.maybe_inaccessible_message import Message


class GiveawayCompleted(BaseObject):
    def __init__(
        self,
        winner_count: int,
        unclaimed_prize_count: Optional[int] = None,
        giveaway_message: Optional[Message] = None,
        is_star_giveaway: Optional[bool] = None,
    ) -> None:
        self.winner_count: int = winner_count
        self.unclaimed_prize_count: Optional[int] = unclaimed_prize_count
        self.giveaway_message: Optional[Message] = giveaway_message
        self.is_star_giveaway: Optional[bool] = is_star_giveaway
        super().__init__(
            winner_count=winner_count,
            unclaimed_prize_count=unclaimed_prize_count,
            giveaway_message=giveaway_message,
            is_star_giveaway=is_star_giveaway,
        )