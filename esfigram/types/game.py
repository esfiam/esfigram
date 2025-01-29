from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.animation import Animation
    from esfigram.types.message_entity import MessageEntity
    from esfigram.types.photo_size import PhotoSize


class Game(BaseObject):
    def __init__(
        self,
        title: str,
        description: str,
        photo: List[PhotoSize],
        text: Optional[str] = None,
        text_entities: Optional[List[MessageEntity]] = None,
        animation: Optional[Animation] = None,
    ) -> None:
        self.title: str = title
        self.description: str = description
        self.photo: List[PhotoSize] = photo
        self.text: Optional[str] = text
        self.text_entities: Optional[List[MessageEntity]] = text_entities
        self.animation: Optional[Animation] = animation
        super().__init__(
            title=title,
            description=description,
            photo=photo,
            text=text,
            text_entities=text_entities,
            animation=animation,
        )