from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.photo_size import PhotoSize


class Document(BaseObject):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        thumbnail: Optional[PhotoSize] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            file_size=file_size,
        )