from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from esfigram.types.user import User


class BusinessConnection(BaseObject):
    def __init__(
        self,
        id: str,
        user: User,
        user_chat_id: int,
        date: int,
        can_reply: bool,
        is_enabled: bool
    ) -> None:
        self.id = id
        self.user = user
        self.user_chat_id = user_chat_id
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled
        super().__init__(
            id=self.id,
            user=self.user,
            user_chat_id=self.user_chat_id,
            date=self.date,
            can_reply=self.can_reply,
            is_enabled=self.is_enabled
        )