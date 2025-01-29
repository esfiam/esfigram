from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.chat import Chat
    from esfigram.types.user import User
    from esfigram.types.chat_invite_link import ChatInviteLink


class ChatJoinRequest(BaseObject):
    def __init__(
        self,
        chat: Chat,
        from_user: User,
        user_chat_id: int,
        date: int,
        bio: Optional[str] = None,
        invite_link: Optional[ChatInviteLink] = None,
    ):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link
        super().__init__(
            chat=chat,
            from_user=from_user,
            user_chat_id=user_chat_id,
            date=date,
            bio=bio,
            invite_link=invite_link,
        )