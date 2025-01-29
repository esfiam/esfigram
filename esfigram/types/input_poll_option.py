from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional, List
    from esfigram.types.message_entity import MessageEntity


class InputPollOption(BaseObject):
    def __init__(
            self,
            text: str,
            text_parse_mode: Optional[str] = None,
            text_entities: Optional[List[MessageEntity]] = None,
    ) -> None:
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities
        super().__init__(
            text=text,
            text_parse_mode=text_parse_mode,
            text_entities=text_entities,
        )