from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.file import File
    from esfigram.types.mask_position import MaskPosition
    from esfigram.types.photo_size import PhotoSize


class Sticker(BaseObject):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int,
        is_animated: bool,
        is_video: bool,
        thumbnail: Optional[PhotoSize] = None,
        emoji: Optional[str] = None,
        set_name: Optional[str] = None,
        premium_animation: Optional[File] = None,
        mask_position: Optional[MaskPosition] = None,
        custom_emoji_id: Optional[str] = None,
        needs_repainting: Optional[bool] = None,
        file_size: Optional[int] = None,
        **kwargs
    ) -> None:
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size
        super().__init__(
            file_id=file_id,
            file_unique_id=file_unique_id,
            type=type,
            width=width,
            height=height,
            is_animated=is_animated,
            is_video=is_video,
            thumbnail=thumbnail,
            emoji=emoji,
            set_name=set_name,
            premium_animation=premium_animation,
            mask_position=mask_position,
            custom_emoji_id=custom_emoji_id,
            needs_repainting=needs_repainting,
            file_size=file_size,
            **kwargs,
        )