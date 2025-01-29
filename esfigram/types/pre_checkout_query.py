from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.user import User
    from esfigram.types.order_info import OrderInfo
    from typing import Optional


class PreCheckoutQuery(BaseObject):
    def __init__(
        self,
        id: str,
        from_user: User,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None,
    ) -> None:
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        super().__init__(
            id=id,
            from_user=from_user,
            currency=currency,
            total_amount=total_amount,
            invoice_payload=invoice_payload,
            shipping_option_id=shipping_option_id,
            order_info=order_info,
        )