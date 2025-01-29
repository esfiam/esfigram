from esfigram.types import ChatBoost, Chat
from esfigram.types.base_object import BaseObject


class ChatBoostUpdated(BaseObject):
    def __init__(self, chat: Chat, boost: ChatBoost) -> None:
        self.chat = chat
        self.boost = boost
        super().__init__(chat=self.chat, boost=self.boost)