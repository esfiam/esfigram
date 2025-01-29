from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, Optional


if TYPE_CHECKING:
    from esfigram.types.shiping_address import ShippingAddress


class OrderInfo(BaseObject):
    def __init__(
        self,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        shipping_address: Optional[ShippingAddress] = None,
    ) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address
        super().__init__(
            name=name,
            phone_number=phone_number,
            email=email,
            shipping_address=shipping_address,
        )