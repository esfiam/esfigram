from __future__ import annotations
from esfigram.types.base_object import BaseObject


class BotName(BaseObject):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name=self.name)