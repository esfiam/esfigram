from enum import Enum


class MenuButtonType(str, Enum):
    """
    Represents the type of a Menu button.

    For more details, visit:
    https://core.telegram.org/bots/api#menubuttondefault

    Attributes:
        DEFAULT: Indicates no specific menu button is set, the default is applied.
        COMMANDS: Opens the bot's list of commands.
        WEB_APP: Launches a Web App.
    """
    DEFAULT = "default"
    COMMANDS = "commands"
    WEB_APP = "web_app"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all menu button types.

        Returns:
            list[str]: A list of all menu button types.
        """
        return [button_type.value for button_type in cls]


