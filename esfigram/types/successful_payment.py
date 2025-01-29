from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.order_info import OrderInfo


class SuccessfulPayment(BaseObject):
    def __init__(
        self,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str,
        subscription_expiration_date: Optional[int] = None,
        is_recurring: Optional[bool] = None,
        is_first_recurring: Optional[bool] = None,
        shipping_option_id: Optional[str] = None,
        order_info: Optional[OrderInfo] = None,
        **kwargs,
    ) -> None:
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.subscription_expiration_date = subscription_expiration_date
        self.is_recurring = is_recurring
        self.is_first_recurring = is_first_recurring
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        super().__init__(
            currency=currency,
            total_amount=total_amount,
            invoice_payload=invoice_payload,
            telegram_payment_charge_id=telegram_payment_charge_id,
            provider_payment_charge_id=provider_payment_charge_id,
            subscription_expiration_date=subscription_expiration_date,
            is_recurring=is_recurring,
            is_first_recurring=is_first_recurring,
            shipping_option_id=shipping_option_id,
            order_info=order_info,
            **kwargs,
        )