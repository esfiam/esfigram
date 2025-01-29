from __future__ import annotations
from esfigram.types.base_object import BaseObject


class MessageId(BaseObject):
    def __init__(self, message_id: int) -> None:
        self.message_id = message_id
        super().__init__(message_id=message_id)