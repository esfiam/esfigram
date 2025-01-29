from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional


class ForumTopicEdited(BaseObject):
    def __init__(self, name: Optional[str] = None, icon_custom_emoji_id: Optional[str] = None) -> None:
        self.name = name
        self.icon_custom_emoji_id = icon_custom_emoji_id
        super().__init__(
            name=name,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )