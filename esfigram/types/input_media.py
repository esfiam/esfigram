from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional, Union, List
    from esfigram.types.message_entity import MessageEntity
    from esfigram.types.input_file import InputFile


class InputMedia(BaseObject):
    def __init__(self, type: str, media: str, **kwargs) -> None:
        self.type = type
        self.media = media
        super().__init__(type=type, media=media, **kwargs)


class InputMediaPhoto(InputMedia):
    def __init__(
            self,
            media: str,
            type: str = 'photo',
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            has_spoiler: Optional[bool] = None,
    ) -> None:
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_spoiler = has_spoiler
        super().__init__(
            media=media,
            type=type,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            has_spoiler=has_spoiler,
        )


class InputMediaVideo(InputMedia):
    def __init__(
            self,
            media: str,
            type: str = 'video',
            thumbnail: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None,
            supports_streaming: Optional[bool] = None,
            has_spoiler: Optional[bool] = None,
    ) -> None:
        self.media = media
        self.type = type
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler
        super().__init__(
            media=media,
            type=type,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            width=width,
            height=height,
            duration=duration,
            supports_streaming=supports_streaming,
            has_spoiler=has_spoiler,
        )


class InputMediaAnimation(InputMedia):
    def __init__(
            self,
            media: str,
            type: str = 'animation',
            thumbnail: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            show_caption_above_media: Optional[bool] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None,
            has_spoiler: Optional[bool] = None,
    ) -> None:
        self.media = media
        self.type = type
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.width = width
        self.height = height
        self.duration = duration
        self.has_spoiler = has_spoiler
        super().__init__(
            media=media,
            type=type,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            show_caption_above_media=show_caption_above_media,
            width=width,
            height=height,
            duration=duration,
            has_spoiler=has_spoiler,
        )


class InputMediaAudio(InputMedia):
    def __init__(
            self,
            media: str,
            type: str = 'audio',
            thumbnail: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            duration: Optional[int] = None,
            performer: Optional[str] = None,
            title: Optional[str] = None,
    ) -> None:
        self.media = media
        self.type = type
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title
        super().__init__(
            media=media,
            type=type,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
        )


class InputMediaDocument(InputMedia):
    def __init__(
            self,
            media: str,
            type: str = 'document',
            thumbnail: Optional[Union[InputFile, str]] = None,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            caption_entities: Optional[List[MessageEntity]] = None,
            disable_content_type_detection: Optional[bool] = None,
    ) -> None:
        self.media = media
        self.type = type
        self.thumbnail = thumbnail
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection
        super().__init__(
            media=media,
            type=type,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
        )
