from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from esfigram.types.user import User
    from typing import Optional


class ChatMember(BaseObject):
    pass


class ChatMemberOwner(ChatMember):
    def __init__(self, user: User, is_anonymous: bool, custom_title: Optional[str] = None) -> None:
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title
        super().__init__(status="creator", user=user, is_anonymous=is_anonymous, custom_title=custom_title)


class ChatMemberAdministrator(ChatMember):
    def __init__(
        self,
        user: User,
        can_be_edited: bool,
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
        custom_title: Optional[str] = None,
    ) -> None:
        self.user = user
        self.can_be_edited = can_be_edited
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
        self.custom_title = custom_title
        super().__init__(
            status="administrator",
            user=user,
            can_be_edited=can_be_edited,
            is_anonymous=is_anonymous,
            can_manage_chat=can_manage_chat,
            can_delete_messages=can_delete_messages,
            can_manage_video_chats=can_manage_video_chats,
            can_restrict_members=can_restrict_members,
            can_promote_members=can_promote_members,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_post_stories=can_post_stories,
            can_edit_stories=can_edit_stories,
            can_delete_stories=can_delete_stories,
            can_post_messages=can_post_messages,
            can_edit_messages=can_edit_messages,
            can_pin_messages=can_pin_messages,
            can_manage_topics=can_manage_topics,
            custom_title=custom_title,
        )


class ChatMemberMember(ChatMember):
    def __init__(self, user: User, until_date: Optional[int] = None) -> None:
        self.user = user
        self.until_date = until_date
        super().__init__(status="member", user=user, until_date=until_date)


class ChatMemberRestricted(ChatMember):
    def __init__(
        self,
        user: User,
        is_member: bool,
        can_send_messages: bool,
        can_send_audios: bool,
        can_send_documents: bool,
        can_send_photos: bool,
        can_send_videos: bool,
        can_send_video_notes: bool,
        can_send_voice_notes: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_manage_topics: bool,
        until_date: int,
    ) -> None:
        self.user = user
        self.is_member = is_member
        self.can_send_messages = can_send_messages
        self.can_send_audios = can_send_audios
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice_notes = can_send_voice_notes
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics
        self.until_date = until_date
        super().__init__(
            status="restricted",
            user=user,
            is_member=is_member,
            can_send_messages=can_send_messages,
            can_send_audios=can_send_audios,
            can_send_documents=can_send_documents,
            can_send_photos=can_send_photos,
            can_send_videos=can_send_videos,
            can_send_video_notes=can_send_video_notes,
            can_send_voice_notes=can_send_voice_notes,
            can_send_polls=can_send_polls,
            can_send_other_messages=can_send_other_messages,
            can_add_web_page_previews=can_add_web_page_previews,
            can_change_info=can_change_info,
            can_invite_users=can_invite_users,
            can_pin_messages=can_pin_messages,
            can_manage_topics=can_manage_topics,
            until_date=until_date,
        )


class ChatMemberLeft(ChatMember):
    def __init__(self, user: User) -> None:
        self.user = user
        super().__init__(status="left", user=user)


class ChatMemberBanned(ChatMember):
    def __init__(self, user: User, until_date: int) -> None:
        self.user = user
        self.until_date = until_date
        super().__init__(status="kicked", user=user, until_date=until_date)