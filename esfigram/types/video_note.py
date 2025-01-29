from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from esfigram.types.photo_size import PhotoSize


class VideoNote(BaseObject):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_size: Optional[int] = None,
        **kwargs
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnail = thumbnail
        self.file_size = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            length=length,
            duration=duration,
            thumbnail=thumbnail,
            file_size=file_size,
            **kwargs
        )