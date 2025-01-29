from esfigram.types.base_object import BaseObject


class ChatBoostRemoved(BaseObject):
    def __init__(self, chat, boost_id: str, remove_date: int, source) -> None:
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source
        super().__init__(chat=self.chat, boost_id=self.boost_id, remove_date=self.remove_date, source=self.source)