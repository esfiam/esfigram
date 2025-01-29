from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.sticker import Sticker


class BusinessIntro(BaseObject):
    def __init__(
        self,
        title: Optional[str] = None,
        message: Optional[str] = None,
        sticker: Optional[Sticker] = None
    ) -> None:
        self.title = title
        self.message = message
        self.sticker = sticker
        super().__init__(title=self.title, message=self.message, sticker=self.sticker)