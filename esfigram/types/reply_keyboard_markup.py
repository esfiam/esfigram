from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.keyboard_button import KeyboardButton


class ReplyKeyboardMarkup(BaseObject):
    def __init__(
        self,
        keyboard: List[List[KeyboardButton]],
        is_persistent: Optional[bool] = False,
        resize_keyboard: Optional[bool] = False,
        one_time_keyboard: Optional[bool] = False,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = False,
    ) -> None:
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
        super().__init__(
            keyboard=keyboard,
            is_persistent=is_persistent,
            resize_keyboard=resize_keyboard,
            one_time_keyboard=one_time_keyboard,
            input_field_placeholder=input_field_placeholder,
            selective=selective,
        )