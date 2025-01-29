from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.user import User


class ProximityAlertTriggered(BaseObject):
    def __init__(self, traveler: User, watcher: User, distance: int) -> None:
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance
        super().__init__(traveler=traveler, watcher=watcher, distance=distance)