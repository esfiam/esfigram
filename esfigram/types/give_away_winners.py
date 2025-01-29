from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.chat import Chat
    from esfigram.types.user import User


class GiveawayWinners(BaseObject):
    def __init__(
        self,
        chat: Chat,
        giveaway_message_id: int,
        winners_selection_date: int,
        winner_count: int,
        winners: List[User],
        additional_chat_count: Optional[int] = None,
        prize_star_count: Optional[int] = None,
        premium_subscription_month_count: Optional[int] = None,
        unclaimed_prize_count: Optional[int] = None,
        only_new_members: Optional[bool] = None,
        was_refunded: Optional[bool] = None,
        prize_description: Optional[str] = None,
    ) -> None:
        self.chat: Chat = chat
        self.giveaway_message_id: int = giveaway_message_id
        self.winners_selection_date: int = winners_selection_date
        self.winner_count: int = winner_count
        self.winners: List[User] = winners
        self.additional_chat_count: Optional[int] = additional_chat_count
        self.prize_star_count: Optional[int] = prize_star_count
        self.premium_subscription_month_count: Optional[int] = premium_subscription_month_count
        self.unclaimed_prize_count: Optional[int] = unclaimed_prize_count
        self.only_new_members: Optional[bool] = only_new_members
        self.was_refunded: Optional[bool] = was_refunded
        self.prize_description: Optional[str] = prize_description
        super().__init__(
            chat=chat,
            giveaway_message_id=giveaway_message_id,
            winners_selection_date=winners_selection_date,
            winner_count=winner_count,
            winners=winners,
            additional_chat_count=additional_chat_count,
            prize_star_count=prize_star_count,
            premium_subscription_month_count=premium_subscription_month_count,
            unclaimed_prize_count=unclaimed_prize_count,
            only_new_members=only_new_members,
            was_refunded=was_refunded,
            prize_description=prize_description,
        )