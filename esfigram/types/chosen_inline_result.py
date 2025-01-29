from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.location import Location
    from esfigram.types.user import User


class ChosenInlineResult(BaseObject):
    def __init__(
        self,
        result_id: str,
        from_user: User,
        query: str,
        location: Optional[Location] = None,
        inline_message_id: Optional[str] = None,
    ) -> None:
        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        self.location = location
        self.inline_message_id = inline_message_id
        super().__init__(
            result_id=result_id,
            from_user=from_user,
            query=query,
            location=location,
            inline_message_id=inline_message_id,
        )