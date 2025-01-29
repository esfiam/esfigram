from __future__ import annotations
from esfigram.types.base_object import BaseObject


class PreparedInlineMessage(BaseObject):
    def __init__(self, id: str, expiration_date: int) -> None:
        self.id = id
        self.expiration_date = expiration_date
        super().__init__(id=id, expiration_date=expiration_date)