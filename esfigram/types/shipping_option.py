from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.labeled_price import LabeledPrice


class ShippingOption(BaseObject):
    def __init__(self, id: str, title: str, prices: List[LabeledPrice], **kwargs) -> None:
        self.id = id
        self.title = title
        self.prices = prices
        super().__init__(id=id, title=title, prices=prices, **kwargs)