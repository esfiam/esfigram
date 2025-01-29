from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from esfigram.types.photo_size import PhotoSize
    from esfigram.types.video import Video


class PaidMedia(BaseObject):
    def __init__(self, type: str, **kwargs) -> None:
        self.type = type
        super().__init__(type=type, **kwargs)


class PaidMediaPreview(PaidMedia):
    def __init__(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        **kwargs,
    ) -> None:
        self.width = width
        self.height = height
        self.duration = duration
        super().__init__(type="preview", width=width, height=height, duration=duration, **kwargs)


class PaidMediaPhoto(PaidMedia):
    def __init__(self, photo: List[PhotoSize], **kwargs) -> None:
        self.photo = photo
        super().__init__(type="photo", photo=photo, **kwargs)


class PaidMediaVideo(PaidMedia):
    def __init__(self, video: Video, **kwargs) -> None:
        self.video = video
        super().__init__(type="video", video=video, **kwargs)