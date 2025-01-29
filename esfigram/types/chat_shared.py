from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.photo_size import PhotoSize


class ChatShared(BaseObject):
    def __init__(
        self,
        request_id: int,
        chat_id: int,
        title: Optional[str] = None,
        username: Optional[str] = None,
        photo: Optional[List[PhotoSize]] = None,
    ) -> None:
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo
        super().__init__(
            request_id=request_id,
            chat_id=chat_id,
            title=title,
            username=username,
            photo=photo,
        )