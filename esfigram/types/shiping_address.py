from __future__ import annotations
from esfigram.types.base_object import BaseObject


class ShippingAddress(BaseObject):
    def __init__(
        self,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str,
        **kwargs,
    ) -> None:
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code
        super().__init__(
            country_code=country_code,
            state=state,
            city=city,
            street_line1=street_line1,
            street_line2=street_line2,
            post_code=post_code,
            **kwargs,
        )