from __future__ import annotations
from esfigram.types.base_object import BaseObject


class MessageAutoDeleteTimerChanged(BaseObject):
    def __init__(self, message_auto_delete_time: int) -> None:
        self.message_auto_delete_time = message_auto_delete_time
        super().__init__(message_auto_delete_time=message_auto_delete_time)