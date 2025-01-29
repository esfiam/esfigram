from __future__ import annotations
from esfigram.types.base_object import BaseObject


class WebAppInfo(BaseObject):
    def __init__(self, url: str, **kwargs) -> None:
        self.url = url
        super().__init__(url=url, **kwargs)