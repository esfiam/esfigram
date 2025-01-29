from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from esfigram.types.paid_media import PaidMedia


class PaidMediaInfo(BaseObject):
    def __init__(self, star_count: int, paid_media: List[PaidMedia]) -> None:
        self.star_count = star_count
        self.paid_media = paid_media
        super().__init__(star_count=star_count, paid_media=paid_media)