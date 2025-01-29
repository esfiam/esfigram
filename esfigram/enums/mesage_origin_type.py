from enum import Enum


class MessageOriginType(str, Enum):
    """
    Represents the origin of a message.

    For more details, visit:
    https://core.telegram.org/bots/api#messageorigin

    Attributes:
        USER: The message was sent by a user.
        HIDDEN_USER: The message was sent by a hidden user.
        CHAT: The message was sent in a chat.
        CHANNEL: The message was sent in a channel.
    """
    USER = "user"
    HIDDEN_USER = "hidden_user"
    CHAT = "chat"
    CHANNEL = "channel"

    @classmethod
    def list_origins(cls):
        """
        Returns a list of all message origin types.

        Returns:
            list[str]: A list of all message origin types.
        """
        return [origin.value for origin in cls]

