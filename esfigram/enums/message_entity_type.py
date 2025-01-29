from enum import Enum


class MessageEntityType(str, Enum):
    """
    Represents the type of a message entity.

    For more details, visit:
    https://core.telegram.org/bots/api#messageentity

    Attributes:
        MENTION: A mention of a user (@username).
        HASHTAG: A hashtag (#hashtag).
        CASHTAG: A cashtag ($USD).
        BOT_COMMAND: A bot command (/start@bot).
        URL: A URL (https://example.com).
        EMAIL: An email address.
        PHONE_NUMBER: A phone number.
        BOLD: Bold text.
        ITALIC: Italic text.
        UNDERLINE: Underlined text.
        STRIKETHROUGH: Strikethrough text.
        SPOILER: Spoiler text (hidden).
        BLOCKQUOTE: A blockquote.
        EXPANDABLE_BLOCKQUOTE: An expandable blockquote.
        CODE: Monospaced inline code.
        PRE: Block of monospaced code.
        TEXT_LINK: Clickable text URLs.
        TEXT_MENTION: A text mention of a user without a username.
        CUSTOM_EMOJI: A custom emoji.
    """
    MENTION = "mention"
    HASHTAG = "hashtag"
    CASHTAG = "cashtag"
    BOT_COMMAND = "bot_command"
    URL = "url"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    BOLD = "bold"
    ITALIC = "italic"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    SPOILER = "spoiler"
    BLOCKQUOTE = "blockquote"
    EXPANDABLE_BLOCKQUOTE = "expandable_blockquote"
    CODE = "code"
    PRE = "pre"
    TEXT_LINK = "text_link"
    TEXT_MENTION = "text_mention"
    CUSTOM_EMOJI = "custom_emoji"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all message entity types.

        Returns:
            list[str]: A list of all message entity types.
        """
        return [entity.value for entity in cls]

