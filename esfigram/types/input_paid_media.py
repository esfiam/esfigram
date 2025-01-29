from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional, Union
    from esfigram.types.input_file import InputFile


class InputPaidMedia(BaseObject):
    def __init__(self, type: str, media: str, **kwargs) -> None:
        self.type = type
        self.media = media
        super().__init__(type=type, media=media, **kwargs)


class InputPaidMediaPhoto(InputPaidMedia):
    def __init__(self, media: str) -> None:
        self.media = media
        super().__init__(type="photo", media=media)


class InputPaidMediaVideo(InputPaidMedia):
    def __init__(
            self,
            media: str,
            thumbnail: Optional[Union[InputFile, str]] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None,
            supports_streaming: Optional[bool] = None,
    ) -> None:
        self.media = media
        self.thumbnail = thumbnail
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming
        super().__init__(
            type="video",
            media=media,
            thumbnail=thumbnail,
            width=width,
            height=height,
            duration=duration,
            supports_streaming=supports_streaming,
        )