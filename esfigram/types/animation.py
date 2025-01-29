from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.photo_size import PhotoSize


class Animation(BaseObject):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
    ) -> None:
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumbnail: Optional[PhotoSize] = thumbnail
        self.file_name: Optional[str] = file_name
        self.mime_type: Optional[str] = mime_type
        self.file_size: Optional[int] = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            width=width,
            height=height,
            duration=duration,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
        )