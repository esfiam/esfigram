from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class ResponseParameters(BaseObject):
    def __init__(
        self,
        migrate_to_chat_id: Optional[int] = None,
        retry_after: Optional[int] = None,
    ) -> None:
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after
        super().__init__(
            migrate_to_chat_id=migrate_to_chat_id,
            retry_after=retry_after,
        )