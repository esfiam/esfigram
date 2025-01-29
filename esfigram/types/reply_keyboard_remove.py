from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class ReplyKeyboardRemove(BaseObject):
    def __init__(
        self,
        remove_keyboard: bool,
        selective: Optional[bool] = None,
    ) -> None:
        self.remove_keyboard = remove_keyboard
        self.selective = selective
        super().__init__(
            remove_keyboard=remove_keyboard,
            selective=selective,
        )