from __future__ import annotations
from esfigram.types.base_object import BaseObject


class LabeledPrice(BaseObject):
    def __init__(self, label: str, amount: int) -> None:
        self.label = label
        self.amount = amount
        super().__init__(label=label, amount=amount)