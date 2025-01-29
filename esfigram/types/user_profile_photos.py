from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.photo_size import PhotoSize


class UserProfilePhotos(BaseObject):
    def __init__(self, total_count: int, photos: List[List[PhotoSize]], **kwargs) -> None:
        self.total_count = total_count
        self.photos = photos
        super().__init__(total_count=total_count, photos=photos, **kwargs)