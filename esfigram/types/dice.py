from __future__ import annotations
from esfigram.types.base_object import BaseObject


class Dice(BaseObject):
    def __init__(self, emoji: str, value: int):
        if emoji not in ["🎲", "🎯", "🎳", "🏀", "⚽", "🎰"]:
            raise ValueError(f"Invalid emoji: {emoji}")
        if emoji in ["🎲", "🎯", "🎳"] and not (1 <= value <= 6):
            raise ValueError(f"Value for {emoji} must be between 1 and 6.")
        if emoji in ["🏀", "⚽"] and not (1 <= value <= 5):
            raise ValueError(f"Value for {emoji} must be between 1 and 5.")
        if emoji == "🎰" and not (1 <= value <= 64):
            raise ValueError(f"Value for {emoji} must be between 1 and 64.")
        self.emoji = emoji
        self.value = value
        super().__init__(emoji=emoji, value=value)