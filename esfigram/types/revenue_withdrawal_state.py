from __future__ import annotations
from esfigram.types.base_object import BaseObject


class RevenueWithdrawalState(BaseObject):
    def __init__(self, state_type: str, **kwargs) -> None:
        self.state_type = state_type
        super().__init__(type=state_type, **kwargs)


class RevenueWithdrawalStatePending(RevenueWithdrawalState):
    def __init__(self, **kwargs) -> None:
        super().__init__(state_type="pending", **kwargs)


class RevenueWithdrawalStateSucceeded(RevenueWithdrawalState):
    def __init__(self, date: int, url: str, **kwargs) -> None:
        self.date = date
        self.url = url
        super().__init__(state_type="succeeded", date=date, url=url, **kwargs)


class RevenueWithdrawalStateFailed(RevenueWithdrawalState):
    def __init__(self, **kwargs) -> None:
        super().__init__(state_type="failed", **kwargs)