from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional


class ChatPermissions(BaseObject):
    def __init__(self,
                 can_send_messages: Optional[bool] = None,
                 can_send_audios: Optional[bool] = None,
                 can_send_documents: Optional[bool] = None,
                 can_send_photos: Optional[bool] = None,
                 can_send_videos: Optional[bool] = None,
                 can_send_video_notes: Optional[bool] = None,
                 can_send_voice_notes: Optional[bool] = None,
                 can_send_polls: Optional[bool] = None,
                 can_send_other_messages: Optional[bool] = None,
                 can_add_web_page_previews: Optional[bool] = None,
                 can_change_info: Optional[bool] = None,
                 can_invite_users: Optional[bool] = None,
                 can_pin_messages: Optional[bool] = None,
                 can_manage_topics: Optional[bool] = None):
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
        super().__init__(
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
        )