from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.star_transaction import StarTransaction


class StarTransactions(BaseObject):
    def __init__(self, transactions: List[StarTransaction], **kwargs) -> None:
        self.transactions = transactions
        super().__init__(transactions=transactions, **kwargs)