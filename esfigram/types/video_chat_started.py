from __future__ import annotations
from esfigram.types.base_object import BaseObject


class VideoChatStarted(BaseObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)