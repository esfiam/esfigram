from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.chat import Chat
    from esfigram.types.reaction_count import ReactionCount


class MessageReactionCountUpdated(BaseObject):
    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        reactions: list[ReactionCount],
    ) -> None:
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions
        super().__init__(
            chat=chat,
            message_id=message_id,
            date=date,
            reactions=reactions,
        )