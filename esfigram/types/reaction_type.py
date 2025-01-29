from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class ReactionType(BaseObject):
    def __init__(self, **kwargs) -> None:

        super().__init__(**kwargs)


class ReactionTypeEmoji(ReactionType):
    def __init__(self, emoji: str) -> None:
        self.emoji = emoji
        super().__init__(type="emoji", emoji=emoji)


class ReactionTypeCustomEmoji(ReactionType):
    def __init__(self, custom_emoji_id: str) -> None:
        self.custom_emoji_id = custom_emoji_id
        super().__init__(type="custom_emoji", custom_emoji_id=custom_emoji_id)


class ReactionTypePaid(ReactionType):
    def __init__(self) -> None:
        super().__init__(type="paid")
