from enum import Enum


class ParseMode(str, Enum):
    """
    Represents the formatting options for Telegram messages.

    For more details, visit:
    https://core.telegram.org/bots/api#formatting-options

    Attributes:
        MARKDOWN_V2: Use Markdown version 2 for formatting.
        MARKDOWN: Use Markdown for formatting.
        HTML: Use HTML for formatting.
    """
    MARKDOWN_V2 = "MarkdownV2"
    MARKDOWN = "Markdown"
    HTML = "HTML"

    @classmethod
    def list_modes(cls):
        """
        Returns a list of all available parse modes.

        Returns:
            list[str]: A list of all parse modes.
        """
        return [mode.value for mode in cls]


