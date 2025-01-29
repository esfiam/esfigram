from __future__ import annotations
from esfigram.types.base_object import BaseObject


class CopyTextButton(BaseObject):
    def __init__(self, text: str) -> None:
        if not (1 <= len(text) <= 256):
            raise ValueError("Text length must be between 1 and 256 characters.")
        self.text = text
        super().__init__(text=text)