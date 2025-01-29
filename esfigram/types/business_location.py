from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.location import Location


class BusinessLocation(BaseObject):
    def __init__(self, address: str, location: Optional[Location] = None) -> None:
        self.address = address
        self.location = location
        super().__init__(address=self.address, location=self.location)