from esfigram.types.base_object import BaseObject
from esfigram.types.background_type import BackgroundType


class ChatBackground(BaseObject):
    def __init__(self, type: BackgroundType) -> None:
        self.type = type
        super().__init__(type=self.type)