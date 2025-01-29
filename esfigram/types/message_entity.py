from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.user import User


class MessageEntity(BaseObject):
    def __init__(
        self,
        type: str,
        offset: int,
        length: int,
        url: Optional[str] = None,
        user: Optional[User] = None,
        language: Optional[str] = None,
        custom_emoji_id: Optional[str] = None,
    ) -> None:
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language
        self.custom_emoji_id = custom_emoji_id
        super().__init__(
            type=type,
            offset=offset,
            length=length,
            url=url,
            user=user,
            language=language,
            custom_emoji_id=custom_emoji_id,
        )