from __future__ import annotations
from esfigram.types.base_object import BaseObject


class WebAppData(BaseObject):
    def __init__(self, data: str, button_text: str, **kwargs) -> None:
        self.data = data
        self.button_text = button_text
        super().__init__(data=data, button_text=button_text, **kwargs)