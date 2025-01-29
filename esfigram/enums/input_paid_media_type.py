from enum import Enum


class InputPaidMediaType(str, Enum):
    """
    Represents the types of media in a paid message.

    For more details, visit:
    https://core.telegram.org/bots/api#inputpaidmedia

    Attributes:
        PHOTO: Represents a photo in a paid message.
        VIDEO: Represents a video in a paid message.
    """
    PHOTO = "photo"
    VIDEO = "video"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all input paid media types.

        Returns:
            list[str]: A list of all input paid media types.
        """
        return [media_type.value for media_type in cls]


