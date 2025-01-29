from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from esfigram.types.affiliate_info import AffiliateInfo
    from esfigram.types.paid_media import PaidMedia
    from esfigram.types.user import User
    from esfigram.types.revenue_withdrawal_state import RevenueWithdrawalState
    from esfigram.types.gift import Gift


class TransactionPartner(BaseObject):
    def __init__(self, type: str, **kwargs) -> None:
        self.type = type
        super().__init__(type=type, **kwargs)


class TransactionPartnerUser(TransactionPartner):
    def __init__(
        self,
        user: User,
        affiliate: Optional[AffiliateInfo] = None,
        invoice_payload: Optional[str] = None,
        subscription_period: Optional[int] = None,
        paid_media: Optional[List[PaidMedia]] = None,
        paid_media_payload: Optional[str] = None,
        gift: Optional[Gift] = None,
        **kwargs,
    ) -> None:
        self.user = user
        self.affiliate = affiliate
        self.invoice_payload = invoice_payload
        self.subscription_period = subscription_period
        self.paid_media = paid_media
        self.paid_media_payload = paid_media_payload
        self.gift = gift
        super().__init__(
            type="user",
            user=user,
            affiliate=affiliate,
            invoice_payload=invoice_payload,
            subscription_period=subscription_period,
            paid_media=paid_media,
            paid_media_payload=paid_media_payload,
            gift=gift,
            **kwargs,
        )


class TransactionPartnerAffiliateProgram(TransactionPartner):
    def __init__(
        self,
        sponsor_user: Optional[User],
        commission_per_mille: int,
        **kwargs,
    ) -> None:
        self.sponsor_user = sponsor_user
        self.commission_per_mille = commission_per_mille
        super().__init__(
            type="affiliate_program",
            sponsor_user=sponsor_user,
            commission_per_mille=commission_per_mille,
            **kwargs,
        )


class TransactionPartnerFragment(TransactionPartner):
    def __init__(
        self,
        withdrawal_state: Optional[RevenueWithdrawalState] = None,
        **kwargs,
    ) -> None:
        self.withdrawal_state = withdrawal_state
        super().__init__(
            type="fragment",
            withdrawal_state=withdrawal_state,
            **kwargs,
        )


class TransactionPartnerTelegramAds(TransactionPartner):
    def __init__(self, **kwargs) -> None:
        super().__init__(type="telegram_ads", **kwargs)


class TransactionPartnerTelegramApi(TransactionPartner):
    def __init__(
        self,
        request_count: int,
        **kwargs,
    ) -> None:
        self.request_count = request_count
        super().__init__(
            type="telegram_api",
            request_count=request_count,
            **kwargs,
        )


class TransactionPartnerOther(TransactionPartner):
    def __init__(self, **kwargs) -> None:
        super().__init__(type="other", **kwargs)