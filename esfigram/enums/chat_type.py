from enum import Enum


class ChatType(str, Enum):
    """
    Represents the type of a chat.

    Attributes:
        SENDER: Represents a chat with the message sender.
        PRIVATE: Represents a private chat.
        GROUP: Represents a group chat.
        SUPERGROUP: Represents a supergroup chat.
        CHANNEL: Represents a channel.
    """
    SENDER = "sender"
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"

    @classmethod
    def list_chat_types(cls):
        """
        Returns a list of all available chat types.

        Returns:
            list[str]: A list of all chat type names.
        """
        return [chat_type.value for chat_type in cls]

