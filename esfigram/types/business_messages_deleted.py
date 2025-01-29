from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.chat import Chat


class BusinessMessagesDeleted(BaseObject):
    def __init__(
        self,
        business_connection_id: str,
        chat: Chat,
        message_ids: List[int],
    ) -> None:
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids
        super().__init__(
            business_connection_id=self.business_connection_id,
            chat=self.chat,
            message_ids=self.message_ids,
        )