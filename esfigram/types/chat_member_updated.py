from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.chat import Chat
    from esfigram.types.user import User
    from esfigram.types.chat_member import ChatMember
    from esfigram.types.chat_invite_link import ChatInviteLink


class ChatMemberUpdated(BaseObject):
    def __init__(
        self,
        chat: Chat,
        from_user: User,
        date: int,
        old_chat_member: ChatMember,
        new_chat_member: ChatMember,
        invite_link: Optional[ChatInviteLink] = None,
        via_join_request: Optional[bool] = None,
        via_chat_folder_invite_link: Optional[bool] = None,
    ):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link
        super().__init__(
            chat=chat,
            from_user=from_user,
            date=date,
            old_chat_member=old_chat_member,
            new_chat_member=new_chat_member,
            invite_link=invite_link,
            via_join_request=via_join_request,
            via_chat_folder_invite_link=via_chat_folder_invite_link,
        )