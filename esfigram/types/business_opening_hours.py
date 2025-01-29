from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.business_opening_hours_interval import BusinessOpeningHoursInterval


class BusinessOpeningHours(BaseObject):
    def __init__(self, time_zone_name: str, opening_hours: List[BusinessOpeningHoursInterval]) -> None:
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours
        super().__init__(
            time_zone_name=self.time_zone_name,
            opening_hours=self.opening_hours,
        )