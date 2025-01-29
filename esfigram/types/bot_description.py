from __future__ import annotations
from esfigram.types.base_object import BaseObject


class BotDescription(BaseObject):
    def __init__(self, description: str) -> None:
        self.description = description
        super().__init__(description=self.description)