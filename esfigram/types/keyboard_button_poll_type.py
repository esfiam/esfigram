from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class KeyboardButtonPollType(BaseObject):
    def __init__(self, type: Optional[str] = None) -> None:
        self.type = type
        super().__init__(type=type)