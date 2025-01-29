from __future__ import annotations
from esfigram.types.base_object import BaseObject


class VideoChatScheduled(BaseObject):
    def __init__(self, start_date: int, **kwargs) -> None:
        self.start_date = start_date
        super().__init__(start_date=start_date, **kwargs)