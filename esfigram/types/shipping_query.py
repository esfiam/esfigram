from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from esfigram.types.user import User
    from esfigram.types.shiping_address import ShippingAddress


class ShippingQuery(BaseObject):
    def __init__(
            self,
            id: str,
            from_user: User,
            invoice_payload: str,
            shipping_address: ShippingAddress,
            **kwargs
    ) -> None:
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address
        super().__init__(
            id=id,
            from_user=from_user,
            invoice_payload=invoice_payload,
            shipping_address=shipping_address,
            **kwargs
        )