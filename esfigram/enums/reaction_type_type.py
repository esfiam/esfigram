from enum import Enum


class ReactionType(str, Enum):
    """
    Represents the type of a reaction.

    For more details, visit:
    https://core.telegram.org/bots/api#reactiontype

    Attributes:
        EMOJI: A reaction based on a standard emoji.
        CUSTOM_EMOJI: A reaction based on a custom emoji.
        PAID: A paid reaction.
    """
    EMOJI = "emoji"
    CUSTOM_EMOJI = "custom_emoji"
    PAID = "paid"

    @classmethod
    def list_reaction_types(cls):
        """
        Returns a list of all available reaction types.

        Returns:
            list[str]: A list of all reaction types.
        """
        return [reaction.value for reaction in cls]

