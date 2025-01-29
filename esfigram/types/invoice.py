from __future__ import annotations
from esfigram.types.base_object import BaseObject


class Invoice(BaseObject):
    def __init__(
            self,
            title: str,
            description: str,
            start_parameter: str,
            currency: str,
            total_amount: int,
    ) -> None:
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount
        super().__init__(
            title=title,
            description=description,
            start_parameter=start_parameter,
            currency=currency,
            total_amount=total_amount,
        )