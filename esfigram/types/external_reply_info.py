from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.animation import Animation
    from esfigram.types.audio import Audio
    from esfigram.types.chat import Chat
    from esfigram.types.contact import Contact
    from esfigram.types.dice import Dice
    from esfigram.types.document import Document
    from esfigram.types.game import Game
    from esfigram.types.give_away import Giveaway
    from esfigram.types.give_away_winners import GiveawayWinners
    from esfigram.types.invoice import Invoice
    from esfigram.types.link_preview_options import LinkPreviewOptions
    from esfigram.types.location import Location
    from esfigram.types.message_origin import MessageOrigin
    from esfigram.types.paid_media_info import PaidMediaInfo
    from esfigram.types.photo_size import PhotoSize
    from esfigram.types.poll import Poll
    from esfigram.types.sticker import Sticker
    from esfigram.types.story import Story
    from esfigram.types.venue import Venue
    from esfigram.types.video import Video
    from esfigram.types.video_note import VideoNote
    from esfigram.types.voice import Voice


class ExternalReplyInfo(BaseObject):
    def __init__(
        self,
        origin: MessageOrigin,
        chat: Optional[Chat] = None,
        message_id: Optional[int] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
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
        has_media_spoiler: Optional[bool] = None,
        contact: Optional[Contact] = None,
        dice: Optional[Dice] = None,
        game: Optional[Game] = None,
        giveaway: Optional[Giveaway] = None,
        giveaway_winners: Optional[GiveawayWinners] = None,
        invoice: Optional[Invoice] = None,
        location: Optional[Location] = None,
        poll: Optional[Poll] = None,
        venue: Optional[Venue] = None,
    ):
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
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
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue
        super().__init__(
            origin=origin,
            chat=chat,
            message_id=message_id,
            link_preview_options=link_preview_options,
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
            has_media_spoiler=has_media_spoiler,
            contact=contact,
            dice=dice,
            game=game,
            giveaway=giveaway,
            giveaway_winners=giveaway_winners,
            invoice=invoice,
            location=location,
            poll=poll,
            venue=venue,
        )