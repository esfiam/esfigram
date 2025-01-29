from esfigram.types.base_object import BaseObject
from typing import Optional


class ChatAdministratorRights(BaseObject):
    def __init__(
        self,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_stories: bool,
        can_edit_stories: bool,
        can_delete_stories: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
    ) -> None:
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        super().__init__(
            is_anonymous=self.is_anonymous,
            can_manage_chat=self.can_manage_chat,
            can_delete_messages=self.can_delete_messages,
            can_manage_video_chats=self.can_manage_video_chats,
            can_restrict_members=self.can_restrict_members,
            can_promote_members=self.can_promote_members,
            can_change_info=self.can_change_info,
            can_invite_users=self.can_invite_users,
            can_post_stories=self.can_post_stories,
            can_edit_stories=self.can_edit_stories,
            can_delete_stories=self.can_delete_stories,
            can_post_messages=self.can_post_messages,
            can_edit_messages=self.can_edit_messages,
            can_pin_messages=self.can_pin_messages,
            can_manage_topics=self.can_manage_topics,
        )