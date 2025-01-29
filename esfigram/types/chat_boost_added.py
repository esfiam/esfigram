from esfigram.types.base_object import BaseObject


class ChatBoostAdded(BaseObject):
    def __init__(self, boost_count: int) -> None:
        self.boost_count = boost_count
        super().__init__(boost_count=self.boost_count)

