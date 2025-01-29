from enum import Enum


class ChatMemberType(str, Enum):
    """
    Represents the types of chat members.

    Attributes:
        OWNER: Represents a chat member who is the owner of the chat.
        ADMINISTRATOR: Represents a chat member who is an administrator.
        MEMBER: Represents a regular chat member with no additional privileges.
        RESTRICTED: Represents a chat member with restrictions.
        LEFT: Represents a chat member who has left the chat.
        BANNED: Represents a chat member who is banned from the chat.
    """
    OWNER = "owner"
    ADMINISTRATOR = "administrator"
    MEMBER = "member"
    RESTRICTED = "restricted"
    LEFT = "left"
    BANNED = "banned"

    @classmethod
    def list_member_types(cls):
        """
        Returns a list of all available chat member types.

        Returns:
            list[str]: A list of all member type names.
        """
        return [member_type.value for member_type in cls]
