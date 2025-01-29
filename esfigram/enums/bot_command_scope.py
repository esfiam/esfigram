from enum import Enum


class BotCommandScope(str, Enum):
    """
    Represents the scope for bot commands.

    Attributes:
        DEFAULT: Applies to all users in all chats by default.
        ALL_PRIVATE_CHATS: Applies to all private chats.
        ALL_GROUP_CHATS: Applies to all group and supergroup chats.
        ALL_CHAT_ADMINISTRATORS: Applies to all administrators of group and supergroup chats.
        CHAT: Applies to a specific chat.
        CHAT_ADMINISTRATORS: Applies to all administrators in a specific chat.
        CHAT_MEMBER: Applies to a specific member of a group or supergroup chat.
    """
    DEFAULT = "default"
    ALL_PRIVATE_CHATS = "all_private_chats"
    ALL_GROUP_CHATS = "all_group_chats"
    ALL_CHAT_ADMINISTRATORS = "all_chat_administrators"
    CHAT = "chat"
    CHAT_ADMINISTRATORS = "chat_administrators"
    CHAT_MEMBER = "chat_member"

    @classmethod
    def list_scopes(cls):
        """
        Returns a list of all available bot command scopes.

        Returns:
            list[str]: A list of all command scope names.
        """
        return [scope.value for scope in cls]

