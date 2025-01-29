from enum import Enum


class InlineQueryResultType(str, Enum):
    """
    Represents the types of inline query results in Telegram.

    For more details, visit:
    https://core.telegram.org/bots/api#inlinequeryresult

    Attributes:
        AUDIO: Represents an audio file.
        DOCUMENT: Represents a document file.
        GIF: Represents an animated GIF file.
        MPEG4_GIF: Represents a video animation (H.264/MPEG-4 AVC video without sound).
        PHOTO: Represents a photo.
        STICKER: Represents a sticker.
        VIDEO: Represents a video file.
        VOICE: Represents a voice recording.
        ARTICLE: Represents an article or web page.
        CONTACT: Represents a contact with a phone number.
        GAME: Represents a game.
        LOCATION: Represents a location on a map.
        VENUE: Represents a venue.
    """
    AUDIO = "audio"
    DOCUMENT = "document"
    GIF = "gif"
    MPEG4_GIF = "mpeg4_gif"
    PHOTO = "photo"
    STICKER = "sticker"
    VIDEO = "video"
    VOICE = "voice"
    ARTICLE = "article"
    CONTACT = "contact"
    GAME = "game"
    LOCATION = "location"
    VENUE = "venue"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all inline query result types.

        Returns:
            list[str]: A list of all inline query result types.
        """
        return [result_type.value for result_type in cls]

