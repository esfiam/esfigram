from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.sticker import Sticker


class Gift(BaseObject):
    def __init__(
        self,
        id: str,
        sticker: Sticker,
        star_count: int,
        upgrade_star_count: Optional[int] = None,
        total_count: Optional[int] = None,
        remaining_count: Optional[int] = None,
    ) -> None:
        self.id: str = id
        self.sticker: Sticker = sticker
        self.star_count: int = star_count
        self.upgrade_star_count: Optional[int] = upgrade_star_count
        self.total_count: Optional[int] = total_count
        self.remaining_count: Optional[int] = remaining_count
        super().__init__(
            id=id,
            sticker=sticker,
            star_count=star_count,
            upgrade_star_count=upgrade_star_count,
            total_count=total_count,
            remaining_count=remaining_count,
        )