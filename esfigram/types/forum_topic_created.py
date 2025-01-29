from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class ForumTopicCreated(BaseObject):
    def __init__(self, name: str, icon_color: int, icon_custom_emoji_id: Optional[str] = None) -> None:
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
        super().__init__(name=name, icon_color=icon_color, icon_custom_emoji_id=icon_custom_emoji_id)