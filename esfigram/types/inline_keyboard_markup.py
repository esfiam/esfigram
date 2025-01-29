from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.inline_keyboard_button import InlineKeyboardButton


class InlineKeyboardMarkup(BaseObject):
    def __init__(self, inline_keyboard: List[List[InlineKeyboardButton]]) -> None:
        self.inline_keyboard: List[List[InlineKeyboardButton]] = inline_keyboard
        super().__init__(inline_keyboard=inline_keyboard)