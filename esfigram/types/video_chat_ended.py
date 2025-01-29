from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class VideoChatEnded(BaseObject):
    def __init__(self, duration: int, **kwargs) -> None:
        self.duration = duration
        super().__init__(duration=duration, **kwargs)