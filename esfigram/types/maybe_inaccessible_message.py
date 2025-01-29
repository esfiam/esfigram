from __future__ import annotations

from dataclasses import dataclass

from esfigram.types.base_object import BaseObject
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types import (
        Chat, User, MessageOrigin, ExternalReplyInfo, TextQuote, Story, MessageEntity,
        LinkPreviewOptions, Animation, Audio, Document, PaidMediaInfo, PhotoSize, Video,
        VideoNote, Voice, Contact, Dice, Venue, Poll, Location, MessageAutoDeleteTimerChanged,
        UsersShared, ChatShared, WriteAccessAllowed, ProximityAlertTriggered, ChatBoostAdded,
        ForumTopicCreated, ForumTopicEdited, ChatBackground, ForumTopicClosed, ForumTopicReopened,
        GeneralForumTopicHidden, GeneralForumTopicUnhidden, InlineKeyboardMarkup, WebAppData,
        VideoChatParticipantsInvited, VideoChatEnded, VideoChatStarted, VideoChatScheduled,
        GiveawayCreated, Giveaway, GiveawayWinners, GiveawayCompleted
    )
    from esfigram.types.game import Game
    from esfigram.types.invoice import Invoice
    from esfigram.types.passport_data import PassportData
    from esfigram.types.refunded_payment import RefundedPayment
    from esfigram.types.sticker import Sticker
    from esfigram.types.successful_payment import SuccessfulPayment


class MaybeInaccessibleMessage(BaseObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


class InaccessibleMessage(MaybeInaccessibleMessage):
    def __init__(self, chat: Chat, message_id: int, date: int = 0, **kwargs) -> None:
        self.chat = chat
        self.message_id = message_id
        self.date = date
        super().__init__(chat=chat, message_id=message_id, date=date, **kwargs)


class Message(MaybeInaccessibleMessage):
    def __init__(
        self,
        message_id: int,
        chat: Chat,
        date: int,
        message_thread_id: Optional[int] = None,
        from_user: Optional[User] = None,
        sender_chat: Optional[Chat] = None,
        sender_boost_count: Optional[int] = None,
        sender_business_bot: Optional[User] = None,
        business_connection_id: Optional[str] = None,
        forward_origin: Optional[MessageOrigin] = None,
        is_topic_message: Optional[bool] = None,
        is_automatic_forward: Optional[bool] = None,
        reply_to_message: Optional[Message] = None,
        external_reply: Optional[ExternalReplyInfo] = None,
        quote: Optional[TextQuote] = None,
        reply_to_story: Optional[Story] = None,
        via_bot: Optional[User] = None,
        edit_date: Optional[int] = None,
        has_protected_content: Optional[bool] = None,
        is_from_offline: Optional[bool] = None,
        media_group_id: Optional[str] = None,
        author_signature: Optional[str] = None,
        text: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        effect_id: Optional[str] = None,
        animation: Optional[Animation] = None,
        audio: Optional[Audio] = None,
        document: Optional[Document] = None,
        paid_media: Optional[PaidMediaInfo] = None,
        photo: Optional[List[PhotoSize]] = None,
        sticker: Optional[Sticker] = None,
        story: Optional[Story] = None,
        video: Optional[Video] = None,
        video_note: Optional[VideoNote] = None,
        voice: Optional[Voice] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_media_spoiler: Optional[bool] = None,
        contact: Optional[Contact] = None,
        dice: Optional[Dice] = None,
        game: Optional[Game] = None,
        poll: Optional[Poll] = None,
        venue: Optional[Venue] = None,
        location: Optional[Location] = None,
        new_chat_members: Optional[List[User]] = None,
        left_chat_member: Optional[User] = None,
        new_chat_title: Optional[str] = None,
        new_chat_photo: Optional[List[PhotoSize]] = None,
        delete_chat_photo: Optional[bool] = None,
        group_chat_created: Optional[bool] = None,
        supergroup_chat_created: Optional[bool] = None,
        channel_chat_created: Optional[bool] = None,
        message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None,
        migrate_to_chat_id: Optional[int] = None,
        migrate_from_chat_id: Optional[int] = None,
        pinned_message: Optional[MaybeInaccessibleMessage] = None,
        invoice: Optional[Invoice] = None,
        successful_payment: Optional[SuccessfulPayment] = None,
        refunded_payment: Optional[RefundedPayment] = None,
        users_shared: Optional[UsersShared] = None,
        chat_shared: Optional[ChatShared] = None,
        connected_website: Optional[str] = None,
        write_access_allowed: Optional[WriteAccessAllowed] = None,
        passport_data: Optional[PassportData] = None,
        proximity_alert_triggered: Optional[ProximityAlertTriggered] = None,
        boost_added: Optional[ChatBoostAdded] = None,
        chat_background_set: Optional[ChatBackground] = None,
        forum_topic_created: Optional[ForumTopicCreated] = None,
        forum_topic_edited: Optional[ForumTopicEdited] = None,
        forum_topic_closed: Optional[ForumTopicClosed] = None,
        forum_topic_reopened: Optional[ForumTopicReopened] = None,
        general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = None,
        general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = None,
        giveaway_created: Optional[GiveawayCreated] = None,
        giveaway: Optional[Giveaway] = None,
        giveaway_winners: Optional[GiveawayWinners] = None,
        giveaway_completed: Optional[GiveawayCompleted] = None,
        video_chat_scheduled: Optional[VideoChatScheduled] = None,
        video_chat_started: Optional[VideoChatStarted] = None,
        video_chat_ended: Optional[VideoChatEnded] = None,
        video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = None,
        web_app_data: Optional[WebAppData] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs,
    ) -> None:
        self.message_id = message_id
        self.chat = chat
        self.date = date
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.sender_business_bot = sender_business_bot
        self.business_connection_id = business_connection_id
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.is_from_offline = is_from_offline
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue,
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.refunded_payment = refunded_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup
        super().__init__(
            message_id=message_id,
            chat=chat,
            date=date,
            message_thread_id=message_thread_id,
            from_user=from_user,
            sender_chat=sender_chat,
            sender_boost_count=sender_boost_count,
            sender_business_bot=sender_business_bot,
            business_connection_id=business_connection_id,
            forward_origin=forward_origin,
            is_topic_message=is_topic_message,
            is_automatic_forward=is_automatic_forward,
            reply_to_message=reply_to_message,
            external_reply=external_reply,
            quote=quote,
            reply_to_story=reply_to_story,
            via_bot=via_bot,
            edit_date=edit_date,
            has_protected_content=has_protected_content,
            is_from_offline=is_from_offline,
            media_group_id=media_group_id,
            author_signature=author_signature,
            text=text,
            entities=entities,
            link_preview_options=link_preview_options,
            effect_id=effect_id,
            animation=animation,
            audio=audio,
            document=document,
            paid_media=paid_media,
            photo=photo,
            sticker=sticker,
            story=story,
            video=video,
            video_note=video_note,
            voice=voice,
            caption=caption,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_media_spoiler=has_media_spoiler,
            contact=contact,
            dice=dice,
            game=game,
            poll=poll,
            venue=venue,
            location=location,
            new_chat_members=new_chat_members,
            left_chat_member=left_chat_member,
            new_chat_title=new_chat_title,
            new_chat_photo=new_chat_photo,
            delete_chat_photo=delete_chat_photo,
            group_chat_created=group_chat_created,
            supergroup_chat_created=supergroup_chat_created,
            channel_chat_created=channel_chat_created,
            message_auto_delete_timer_changed=message_auto_delete_timer_changed,
            migrate_to_chat_id=migrate_to_chat_id,
            migrate_from_chat_id=migrate_from_chat_id,
            pinned_message=pinned_message,
            invoice=invoice,
            successful_payment=successful_payment,
            refunded_payment=refunded_payment,
            users_shared=users_shared,
            chat_shared=chat_shared,
            connected_website=connected_website,
            write_access_allowed=write_access_allowed,
            passport_data=passport_data,
            proximity_alert_triggered=proximity_alert_triggered,
            boost_added=boost_added,
            chat_background_set=chat_background_set,
            forum_topic_created=forum_topic_created,
            forum_topic_edited=forum_topic_edited,
            forum_topic_closed=forum_topic_closed,
            forum_topic_reopened=forum_topic_reopened,
            general_forum_topic_hidden=general_forum_topic_hidden,
            general_forum_topic_unhidden=general_forum_topic_unhidden,
            giveaway_created=giveaway_created,
            giveaway=giveaway,
            giveaway_winners=giveaway_winners,
            giveaway_completed=giveaway_completed,
            video_chat_scheduled=video_chat_scheduled,
            video_chat_started=video_chat_started,
            video_chat_ended=video_chat_ended,
            video_chat_participants_invited=video_chat_participants_invited,
            web_app_data=web_app_data,
            reply_markup=reply_markup,
            **kwargs,
        )