from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class SentWebAppMessage(BaseObject):
    def __init__(self, inline_message_id: Optional[str] = None, **kwargs) -> None:
        self.inline_message_id = inline_message_id
        super().__init__(inline_message_id=inline_message_id, **kwargs)