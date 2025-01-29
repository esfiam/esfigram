from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.chat import Chat
    from esfigram.types.user import User
    from esfigram.types.reaction_type import ReactionType


class MessageReactionUpdated(BaseObject):
    def __init__(
        self,
        chat: Chat,
        message_id: int,
        date: int,
        old_reaction: list[ReactionType],
        new_reaction: list[ReactionType],
        user: User | None = None,
        actor_chat: Chat | None = None,
    ) -> None:
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction
        self.user = user
        self.actor_chat = actor_chat
        super().__init__(
            chat=chat,
            message_id=message_id,
            date=date,
            old_reaction=old_reaction,
            new_reaction=new_reaction,
            user=user,
            actor_chat=actor_chat,
        )