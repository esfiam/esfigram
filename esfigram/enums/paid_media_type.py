from enum import Enum


class PaidMediaType(str, Enum):
    """
    Represents the type of media in a paid message.

    For more details, visit:
    https://core.telegram.org/bots/api#paidmedia

    Attributes:
        PHOTO: The media is a photo.
        PREVIEW: The media is a preview.
        VIDEO: The media is a video.
    """
    PHOTO = "photo"
    PREVIEW = "preview"
    VIDEO = "video"

    @classmethod
    def list_media_types(cls):
        """
        Returns a list of all paid media types.

        Returns:
            list[str]: A list of all media types.
        """
        return [media_type.value for media_type in cls]

