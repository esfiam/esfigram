from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class ForumTopic(BaseObject):
    def __init__(
        self,
        message_thread_id: int,
        name: str,
        icon_color: int,
        icon_custom_emoji_id: Optional[str] = None,
    ) -> None:
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id
        super().__init__(
            message_thread_id=message_thread_id,
            name=name,
            icon_color=icon_color,
            icon_custom_emoji_id=icon_custom_emoji_id,
        )