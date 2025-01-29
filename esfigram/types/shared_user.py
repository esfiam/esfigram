from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, List
    from esfigram.types.photo_size import PhotoSize


class SharedUser(BaseObject):
    def __init__(
        self,
        user_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        photo: Optional[List[PhotoSize]] = None,
        **kwargs,
    ) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo or []
        super().__init__(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
            photo=self.photo,
            **kwargs,
        )