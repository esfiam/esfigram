from enum import Enum


class StickerType(str, Enum):
    """
    Represents the type of a sticker.

    For more details, visit:
    https://core.telegram.org/bots/api#maskposition

    Attributes:
        REGULAR: A standard sticker.
        MASK: A sticker used as a mask.
        CUSTOM_EMOJI: A sticker used as a custom emoji.
    """
    REGULAR = "regular"
    MASK = "mask"
    CUSTOM_EMOJI = "custom_emoji"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all sticker types.

        Returns:
            list[str]: A list of all sticker type values.
        """
        return [sticker_type.value for sticker_type in cls]

