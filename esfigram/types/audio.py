from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.photo_size import PhotoSize


class Audio(BaseObject):
    def __init__(
        self: Audio,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumbnail: Optional[PhotoSize] = None,
    ) -> None:
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.duration: int = duration
        self.performer: Optional[str] = performer
        self.title: Optional[str] = title
        self.file_name: Optional[str] = file_name
        self.mime_type: Optional[str] = mime_type
        self.file_size: Optional[int] = file_size
        self.thumbnail: Optional[PhotoSize] = thumbnail

        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            duration=duration,
            performer=performer,
            title=title,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
            thumbnail=thumbnail,
        )