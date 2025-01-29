from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class PassportFile(BaseObject):
    def __init__(
            self,
            file_id: str,
            file_unique_id: str,
            file_size: Optional[int] = None,
            file_date: Optional[int] = None,
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            file_size=file_size,
            file_date=file_date,
        )