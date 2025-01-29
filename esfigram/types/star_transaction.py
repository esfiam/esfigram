from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.transaction_partner import TransactionPartner


class StarTransaction(BaseObject):
    def __init__(
        self,
        id: str,
        amount: int,
        date: int,
        nanostar_amount: Optional[int] = None,
        source: Optional[TransactionPartner] = None,
        receiver: Optional[TransactionPartner] = None,
        **kwargs
    ) -> None:
        self.id = id
        self.amount = amount
        self.date = date
        self.nanostar_amount = nanostar_amount
        self.source = source
        self.receiver = receiver
        super().__init__(
            id=id,
            amount=amount,
            date=date,
            nanostar_amount=nanostar_amount,
            source=source,
            receiver=receiver,
            **kwargs,
        )