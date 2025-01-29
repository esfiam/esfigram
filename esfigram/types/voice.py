from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    pass


class Voice(BaseObject):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **kwargs
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            duration=duration,
            mime_type=mime_type,
            file_size=file_size,
            **kwargs
        )