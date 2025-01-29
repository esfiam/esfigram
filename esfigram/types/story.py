from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.chat import Chat


class Story(BaseObject):
    def __init__(self, chat: Chat, id: int, **kwargs) -> None:
        self.chat = chat
        self.id = id
        super().__init__(chat=chat, id=id, **kwargs)