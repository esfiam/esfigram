from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class PhotoSize(BaseObject):
    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            width: int,
            height: int,
            file_size: Optional[int] = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            width=width,
            height=height,
            file_size=file_size,
        )