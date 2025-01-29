from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.chat import Chat
    from esfigram.types.user import User


class AffiliateInfo(BaseObject):
    def __init__(
            self,
            affiliate_user: Optional[User] = None,
            affiliate_chat: Optional[Chat] = None,
            commission_per_mille: int = 0,
            amount: int = 0,
            nanostar_amount: Optional[int] = None,
    ) -> None:
        self.affiliate_user = affiliate_user
        self.affiliate_chat = affiliate_chat
        self.commission_per_mille = commission_per_mille
        self.amount = amount
        self.nanostar_amount = nanostar_amount
        super().__init__(
            affiliate_user=affiliate_user,
            affiliate_chat=affiliate_chat,
            commission_per_mille=commission_per_mille,
            amount=amount,
            nanostar_amount=nanostar_amount,
        )