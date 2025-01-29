from enum import Enum


class StickerFormat(str, Enum):
    """
    Represents the format of a sticker.

    For more details, visit:
    https://core.telegram.org/bots/api#createnewstickerset

    Attributes:
        STATIC: Represents a static sticker.
        ANIMATED: Represents an animated sticker.
        VIDEO: Represents a video sticker.
    """
    STATIC = "static"
    ANIMATED = "animated"
    VIDEO = "video"

    @classmethod
    def list_formats(cls):
        """
        Returns a list of all sticker formats.

        Returns:
            list[str]: A list of all sticker format types.
        """
        return [format.value for format in cls]


