from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.message_entity import MessageEntity


class PollOption(BaseObject):
    def __init__(
        self,
        text: str,
        voter_count: int,
        text_entities: Optional[List[MessageEntity]] = None,
    ) -> None:
        self.text = text
        self.voter_count = voter_count
        self.text_entities = text_entities
        super().__init__(
            text=text,
            voter_count=voter_count,
            text_entities=text_entities,
        )