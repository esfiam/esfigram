from __future__ import annotations
from esfigram.types.base_object import BaseObject


class InputFile(BaseObject):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        super().__init__(file_path=file_path)