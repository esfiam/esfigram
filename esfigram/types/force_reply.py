from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class ForceReply(BaseObject):
    def __init__(
        self,
        force_reply: bool,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None,
    ) -> None:
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
        super().__init__(
            force_reply=force_reply,
            input_field_placeholder=input_field_placeholder,
            selective=selective,
        )