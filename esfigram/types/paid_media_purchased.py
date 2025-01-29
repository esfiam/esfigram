from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.user import User


class PaidMediaPurchased(BaseObject):
    def __init__(self, from_user: User, paid_media_payload: str) -> None:
        self.from_user = from_user
        self.paid_media_payload = paid_media_payload
        super().__init__(from_user=from_user, paid_media_payload=paid_media_payload)