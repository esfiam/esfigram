from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, List
    from esfigram.types.message_entity import MessageEntity


class TextQuote(BaseObject):
    def __init__(
        self,
        text: str,
        position: int,
        entities: Optional[List[MessageEntity]] = None,
        is_manual: Optional[bool] = None,
        **kwargs,
    ) -> None:
        self.text = text
        self.position = position
        self.entities = entities
        self.is_manual = is_manual
        super().__init__(
            text=text,
            position=position,
            entities=entities,
            is_manual=is_manual,
            **kwargs,
        )