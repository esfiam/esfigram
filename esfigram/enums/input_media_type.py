from enum import Enum


class InputMediaType(str, Enum):
    """
    Represents the types of input media supported in Telegram.

    For more details, visit:
    https://core.telegram.org/bots/api#inputmedia

    Attributes:
        ANIMATION: Represents an animation (GIF or H.264/MPEG-4 AVC video without sound).
        AUDIO: Represents an audio file to be sent.
        DOCUMENT: Represents a general file to be sent.
        PHOTO: Represents a photo to be sent.
        VIDEO: Represents a video to be sent.
    """
    ANIMATION = "animation"
    AUDIO = "audio"
    DOCUMENT = "document"
    PHOTO = "photo"
    VIDEO = "video"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all input media types.

        Returns:
            list[str]: A list of all input media types.
        """
        return [media_type.value for media_type in cls]

