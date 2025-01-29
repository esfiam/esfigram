from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class LinkPreviewOptions(BaseObject):
    def __init__(
        self,
        is_disabled: Optional[bool] = False,
        url: Optional[str] = None,
        prefer_small_media: Optional[bool] = False,
        prefer_large_media: Optional[bool] = False,
        show_above_text: Optional[bool] = False,
    ) -> None:
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text
        super().__init__(
            is_disabled=is_disabled,
            url=url,
            prefer_small_media=prefer_small_media,
            prefer_large_media=prefer_large_media,
            show_above_text=show_above_text,
        )