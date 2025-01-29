from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from esfigram.types.location import Location


class ChatLocation(BaseObject):
    def __init__(self, location: Location, address: str):
        self.location = location
        self.address = address
        super().__init__(location=location, address=address)