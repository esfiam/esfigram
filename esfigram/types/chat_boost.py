from esfigram.types.base_object import BaseObject
from esfigram.types.chat_boost_source import ChatBoostSource


class ChatBoost(BaseObject):
    def __init__(self, boost_id: str, add_date: int, expiration_date: int, source: ChatBoostSource) -> None:
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source
        super().__init__(
            boost_id=self.boost_id,
            add_date=self.add_date,
            expiration_date=self.expiration_date,
            source=self.source,
        )