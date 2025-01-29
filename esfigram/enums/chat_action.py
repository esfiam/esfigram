from enum import Enum


class ChatAction(str, Enum):
    """
    Represents the actions a bot can perform.

    Attributes:
        TYPING: Indicates the bot is typing a text message.
        UPLOAD_PHOTO: Indicates the bot is uploading a photo.
        RECORD_VIDEO: Indicates the bot is recording a video.
        UPLOAD_VIDEO: Indicates the bot is uploading a video.
        RECORD_VOICE: Indicates the bot is recording a voice note.
        UPLOAD_VOICE: Indicates the bot is uploading a voice note.
        UPLOAD_DOCUMENT: Indicates the bot is uploading a document.
        CHOOSE_STICKER: Indicates the bot is choosing a sticker.
        FIND_LOCATION: Indicates the bot is sending location data.
        RECORD_VIDEO_NOTE: Indicates the bot is recording a video note.
        UPLOAD_VIDEO_NOTE: Indicates the bot is uploading a video note.
    """
    TYPING = "typing"
    UPLOAD_PHOTO = "upload_photo"
    RECORD_VIDEO = "record_video"
    UPLOAD_VIDEO = "upload_video"
    RECORD_VOICE = "record_voice"
    UPLOAD_VOICE = "upload_voice"
    UPLOAD_DOCUMENT = "upload_document"
    CHOOSE_STICKER = "choose_sticker"
    FIND_LOCATION = "find_location"
    RECORD_VIDEO_NOTE = "record_video_note"
    UPLOAD_VIDEO_NOTE = "upload_video_note"

    @classmethod
    def list_actions(cls):
        """
        Returns a list of all available actions.

        Returns:
            list[str]: A list of all chat actions.
        """
        return [action.value for action in cls]


