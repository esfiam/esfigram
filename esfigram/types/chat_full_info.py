from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional, List
    from esfigram.types.birthdate import Birthdate
    from esfigram.types.business_intro import BusinessIntro
    from esfigram.types.business_location import BusinessLocation
    from esfigram.types.business_opening_hours import BusinessOpeningHours
    from esfigram.types.chat import Chat
    from esfigram.types.chat_location import ChatLocation
    from esfigram.types.chat_permissions import ChatPermissions
    from esfigram.types.chat_photo import ChatPhoto
    from esfigram.types.maybe_inaccessible_message import Message
    from esfigram.types.reaction_type import ReactionType


class ChatFullInfo(BaseObject):
    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[bool] = None,
        accent_color_id: int = 0,
        max_reaction_count: int = 0,
        photo: Optional[ChatPhoto] = None,
        active_usernames: Optional[List[str]] = None,
        birthdate: Optional[Birthdate] = None,
        business_intro: Optional[BusinessIntro] = None,
        business_location: Optional[BusinessLocation] = None,
        business_opening_hours: Optional[BusinessOpeningHours] = None,
        personal_chat: Optional[Chat] = None,
        available_reactions: Optional[List[ReactionType]] = None,
        background_custom_emoji_id: Optional[str] = None,
        profile_accent_color_id: Optional[int] = None,
        profile_background_custom_emoji_id: Optional[str] = None,
        emoji_status_custom_emoji_id: Optional[str] = None,
        emoji_status_expiration_date: Optional[int] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[bool] = None,
        has_restricted_voice_and_video_messages: Optional[bool] = None,
        join_to_send_messages: Optional[bool] = None,
        join_by_request: Optional[bool] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional[Message] = None,
        permissions: Optional[ChatPermissions] = None,
        can_send_paid_media: Optional[bool] = None,
        slow_mode_delay: Optional[int] = None,
        unrestrict_boost_count: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_aggressive_anti_spam_enabled: Optional[bool] = None,
        has_hidden_members: Optional[bool] = None,
        has_protected_content: Optional[bool] = None,
        has_visible_history: Optional[bool] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[bool] = None,
        custom_emoji_sticker_set_name: Optional[str] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional[ChatLocation] = None,
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location
        super().__init__(
            id=id,
            type=type,
            title=title,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_forum=is_forum,
            accent_color_id=accent_color_id,
            max_reaction_count=max_reaction_count,
            photo=photo,
            active_usernames=active_usernames,
            birthdate=birthdate,
            business_intro=business_intro,
            business_location=business_location,
            business_opening_hours=business_opening_hours,
            personal_chat=personal_chat,
            available_reactions=available_reactions,
            background_custom_emoji_id=background_custom_emoji_id,
            profile_accent_color_id=profile_accent_color_id,
            profile_background_custom_emoji_id=profile_background_custom_emoji_id,
            emoji_status_custom_emoji_id=emoji_status_custom_emoji_id,
            emoji_status_expiration_date=emoji_status_expiration_date,
            bio=bio,
            has_private_forwards=has_private_forwards,
            has_restricted_voice_and_video_messages=has_restricted_voice_and_video_messages,
            join_to_send_messages=join_to_send_messages,
            join_by_request=join_by_request,
            description=description,
            invite_link=invite_link,
            pinned_message=pinned_message,
            permissions=permissions,
            can_send_paid_media=can_send_paid_media,
            slow_mode_delay=slow_mode_delay,
            unrestrict_boost_count=unrestrict_boost_count,
            message_auto_delete_time=message_auto_delete_time,
            has_aggressive_anti_spam_enabled=has_aggressive_anti_spam_enabled,
            has_hidden_members=has_hidden_members,
            has_protected_content=has_protected_content,
            has_visible_history=has_visible_history,
            sticker_set_name=sticker_set_name,
            can_set_sticker_set=can_set_sticker_set,
            custom_emoji_sticker_set_name=custom_emoji_sticker_set_name,
            linked_chat_id=linked_chat_id,
            location=location,
        )