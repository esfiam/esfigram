from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional, List
    from esfigram.types.inline_keyboard_markup import InlineKeyboardMarkup
    from esfigram.types.input_message_content import InputMessageContent
    from esfigram.types.message_entity import MessageEntity


class InlineQueryResult(BaseObject):
    def __init__(self, type: str, id: str, **kwargs) -> None:
        self.type: str = type
        self.id: str = id
        super().__init__(type=type, id=id, **kwargs)


class InlineQueryResultArticle(InlineQueryResult):
    def __init__(
        self,
        id: str,
        title: str,
        input_message_content: InputMessageContent,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        thumbnail_width: Optional[int] = None,
        thumbnail_height: Optional[int] = None,
        **kwargs
    ) -> None:
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        super().__init__(
            type="article",
            id=id,
            title=title,
            input_message_content=input_message_content,
            reply_markup=reply_markup,
            url=url,
            description=description,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            thumbnail_height=thumbnail_height,
            **kwargs
        )


class InlineQueryResultPhoto(InlineQueryResult):
    def __init__(
        self,
        id: str,
        photo_url: str,
        thumbnail_url: str,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        input_message_content: Optional[InputMessageContent] = None,
        **kwargs
    ) -> None:
        self.id = id
        self.photo_url = photo_url
        self.thumbnail_url = thumbnail_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="photo",
            id=id,
            photo_url=photo_url,
            thumbnail_url=thumbnail_url,
            photo_width=photo_width,
            photo_height=photo_height,
            title=title,
            description=description,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            **kwargs
        )


class InlineQueryResultGif(InlineQueryResult):
    def __init__(
            self,
            id: str,
            gif_url: str,
            thumbnail_url: str,
            gif_width: Optional[int] = None,
            gif_height: Optional[int] = None,
            gif_duration: Optional[int] = None,
            thumbnail_mime_type: Optional[str] = None,
            title: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
            **kwargs
    ) -> None:
        self.id = id
        self.gif_url = gif_url
        self.thumbnail_url = thumbnail_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="gif",
            id=id,
            gif_url=gif_url,
            thumbnail_url=thumbnail_url,
            gif_width=gif_width,
            gif_height=gif_height,
            gif_duration=gif_duration,
            thumbnail_mime_type=thumbnail_mime_type,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            **kwargs
        )


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    def __init__(
            self,
            id: str,
            mpeg4_url: str,
            thumbnail_url: str,
            mpeg4_width: Optional[int] = None,
            mpeg4_height: Optional[int] = None,
            mpeg4_duration: Optional[int] = None,
            thumbnail_mime_type: Optional[str] = None,
            title: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.thumbnail_url = thumbnail_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumbnail_mime_type = thumbnail_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="mpeg4_gif",
            id=id,
            mpeg4_url=mpeg4_url,
            thumbnail_url=thumbnail_url,
            mpeg4_width=mpeg4_width,
            mpeg4_height=mpeg4_height,
            mpeg4_duration=mpeg4_duration,
            thumbnail_mime_type=thumbnail_mime_type,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultVideo(InlineQueryResult):
    def __init__(
            self,
            id: str,
            video_url: str,
            mime_type: str,
            thumbnail_url: str,
            title: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            video_width: Optional[int] = None,
            video_height: Optional[int] = None,
            video_duration: Optional[int] = None,
            description: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="video",
            id=id,
            video_url=video_url,
            mime_type=mime_type,
            thumbnail_url=thumbnail_url,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            video_width=video_width,
            video_height=video_height,
            video_duration=video_duration,
            description=description,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultAudio(InlineQueryResult):
    def __init__(
            self,
            id: str,
            audio_url: str,
            title: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            performer: Optional[str] = None,
            audio_duration: Optional[int] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="audio",
            id=id,
            audio_url=audio_url,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            performer=performer,
            audio_duration=audio_duration,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultVoice(InlineQueryResult):
    def __init__(
            self,
            id: str,
            voice_url: str,
            title: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            voice_duration: Optional[int] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="voice",
            id=id,
            voice_url=voice_url,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            voice_duration=voice_duration,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultDocument(InlineQueryResult):
    def __init__(
            self,
            id: str,
            title: str,
            document_url: str,
            mime_type: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            description: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
            thumbnail_url: Optional[str] = None,
            thumbnail_width: Optional[int] = None,
            thumbnail_height: Optional[int] = None,
    ) -> None:
        self.id = id
        self.title = title
        self.document_url = document_url
        self.mime_type = mime_type
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        super().__init__(
            type="document",
            id=id,
            title=title,
            document_url=document_url,
            mime_type=mime_type,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            description=description,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            thumbnail_height=thumbnail_height
        )


class InlineQueryResultLocation(InlineQueryResult):
    def __init__(
            self,
            id: str,
            latitude: float,
            longitude: float,
            title: str,
            horizontal_accuracy: Optional[float] = None,
            live_period: Optional[int] = None,
            heading: Optional[int] = None,
            proximity_alert_radius: Optional[int] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
            thumbnail_url: Optional[str] = None,
            thumbnail_width: Optional[int] = None,
            thumbnail_height: Optional[int] = None,
    ) -> None:
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        super().__init__(
            type="location",
            id=id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            thumbnail_height=thumbnail_height,
        )


class InlineQueryResultVenue(InlineQueryResult):
    def __init__(
            self,
            id: str,
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            foursquare_id: Optional[str] = None,
            foursquare_type: Optional[str] = None,
            google_place_id: Optional[str] = None,
            google_place_type: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
            thumbnail_url: Optional[str] = None,
            thumbnail_width: Optional[int] = None,
            thumbnail_height: Optional[int] = None,
    ) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        super().__init__(
            type="venue",
            id=id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            thumbnail_height=thumbnail_height,
        )


class InlineQueryResultContact(InlineQueryResult):
    def __init__(
            self,
            id: str,
            phone_number: str,
            first_name: str,
            last_name: Optional[str] = None,
            vcard: Optional[str] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
            thumbnail_url: Optional[str] = None,
            thumbnail_width: Optional[int] = None,
            thumbnail_height: Optional[int] = None,
    ) -> None:
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
        super().__init__(
            type="contact",
            id=id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            thumbnail_height=thumbnail_height,
        )


class InlineQueryResultGame(InlineQueryResult):
    def __init__(
            self,
            id: str,
            game_short_name: str,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> None:
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup
        super().__init__(
            type="game",
            id=id,
            game_short_name=game_short_name,
            reply_markup=reply_markup,
        )


class InlineQueryResultCachedPhoto(InlineQueryResult):
    def __init__(
            self,
            id: str,
            photo_file_id: str,
            title: Optional[str] = None,
            description: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[list[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="photo",
            id=id,
            photo_file_id=photo_file_id,
            title=title,
            description=description,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
        )


class InlineQueryResultCachedGif(InlineQueryResult):
    def __init__(
            self,
            id: str,
            gif_file_id: str,
            title: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="gif",
            id=id,
            gif_file_id=gif_file_id,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    def __init__(
            self,
            id: str,
            mpeg4_file_id: str,
            title: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="mpeg4_gif",
            id=id,
            mpeg4_file_id=mpeg4_file_id,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultCachedSticker(InlineQueryResult):
    def __init__(
            self,
            id: str,
            sticker_file_id: str,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="sticker",
            id=id,
            sticker_file_id=sticker_file_id,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultCachedDocument(InlineQueryResult):
    def __init__(
            self,
            id: str,
            title: str,
            document_file_id: str,
            description: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="document",
            id=id,
            title=title,
            document_file_id=document_file_id,
            description=description,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            reply_markup=reply_markup,
            input_message_content=input_message_content
        )


class InlineQueryResultCachedVideo(InlineQueryResult):
    def __init__(
            self,
            id: str,
            video_file_id: str,
            title: str,
            description: Optional[str] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="video",
            id=id,
            video_file_id=video_file_id,
            title=title,
            description=description,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
        )


class InlineQueryResultCachedVoice(InlineQueryResult):
    def __init__(
            self,
            id: str,
            voice_file_id: str,
            title: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="voice",
            id=id,
            voice_file_id=voice_file_id,
            title=title,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
        )


class InlineQueryResultCachedAudio(InlineQueryResult):
    def __init__(
            self,
            id: str,
            audio_file_id: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            reply_markup: Optional[InlineKeyboardMarkup] = None,
            input_message_content: Optional[InputMessageContent] = None,
    ) -> None:
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        super().__init__(
            type="audio",
            id=id,
            audio_file_id=audio_file_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            reply_markup=reply_markup,
            input_message_content=input_message_content,
        )
