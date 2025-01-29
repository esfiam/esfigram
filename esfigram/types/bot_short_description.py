from __future__ import annotations
from esfigram.types.base_object import BaseObject


class BotShortDescription(BaseObject):
    def __init__(self, short_description: str) -> None:
        self.short_description = short_description
        super().__init__(short_description=self.short_description)