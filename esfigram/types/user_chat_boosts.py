from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.chat_boost import ChatBoost


class UserChatBoosts(BaseObject):
    def __init__(self, boosts: List[ChatBoost], **kwargs) -> None:
        self.boosts = boosts
        super().__init__(boosts=boosts, **kwargs)