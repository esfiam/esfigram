from enum import Enum


class DiceEmoji(str, Enum):
    """
    Represents emojis used for the dice throw animation in Telegram.
    For more details, visit:
    https://core.telegram.org/bots/api#dice

    Attributes:
        DICE: Standard dice emoji.
        DART: Dartboard emoji.
        BASKETBALL: Basketball emoji.
        FOOTBALL: Football emoji.
        SLOT_MACHINE: Slot machine emoji.
        BOWLING: Bowling emoji.
    """
    DICE = "🎲"
    DART = "🎯"
    BASKETBALL = "🏀"
    FOOTBALL = "⚽"
    SLOT_MACHINE = "🎰"
    BOWLING = "🎳"

    @classmethod
    def list_emojis(cls):
        """
        Returns a list of all dice emojis.

        Returns:
            list[str]: A list of all dice emojis.
        """
        return [emoji.value for emoji in cls]

