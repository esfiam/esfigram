from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.chat import Chat


class Giveaway(BaseObject):
    def __init__(
        self,
        chats: List[Chat],
        winners_selection_date: int,
        winner_count: int,
        only_new_members: Optional[bool] = None,
        has_public_winners: Optional[bool] = None,
        prize_description: Optional[str] = None,
        country_codes: Optional[List[str]] = None,
        prize_star_count: Optional[int] = None,
        premium_subscription_month_count: Optional[int] = None,
    ) -> None:
        self.chats: List[Chat] = chats
        self.winners_selection_date: int = winners_selection_date
        self.winner_count: int = winner_count
        self.only_new_members: Optional[bool] = only_new_members
        self.has_public_winners: Optional[bool] = has_public_winners
        self.prize_description: Optional[str] = prize_description
        self.country_codes: Optional[List[str]] = country_codes
        self.prize_star_count: Optional[int] = prize_star_count
        self.premium_subscription_month_count: Optional[int] = premium_subscription_month_count
        super().__init__(
            chats=chats,
            winners_selection_date=winners_selection_date,
            winner_count=winner_count,
            only_new_members=only_new_members,
            has_public_winners=has_public_winners,
            prize_description=prize_description,
            country_codes=country_codes,
            prize_star_count=prize_star_count,
            premium_subscription_month_count=premium_subscription_month_count,
        )