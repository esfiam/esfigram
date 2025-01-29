from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.reaction_type import ReactionType


class ReactionCount(BaseObject):
    def __init__(self, type: ReactionType, total_count: int) -> None:
        self.type = type
        self.total_count = total_count
        super().__init__(type=type, total_count=total_count)