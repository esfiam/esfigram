from enum import Enum


class ChatBoostSource(str, Enum):
    """
    Represents the source of a chat boost.

    Attributes:
        PREMIUM: The boost was obtained through a Telegram Premium subscription or by gifting a Premium subscription.
        GIFT_CODE: The boost was obtained through a Telegram Premium gift code.
        GIVEAWAY: The boost was obtained through a giveaway.
    """
    PREMIUM = "premium"
    GIFT_CODE = "gift_code"
    GIVEAWAY = "giveaway"

    @classmethod
    def list_sources(cls):
        """
        Returns a list of all available chat boost sources.

        Returns:
            list[str]: A list of all boost source names.
        """
        return [source.value for source in cls]

