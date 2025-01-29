from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.user import User
    from esfigram.types.location import Location


class InlineQuery(BaseObject):
    def __init__(
            self,
            id: str,
            from_user: User,
            query: str,
            offset: str,
            chat_type: Optional[str] = None,
            location: Optional[Location] = None,
    ) -> None:
        self.id: str = id
        self.from_user: User = from_user
        self.query: str = query
        self.offset: str = offset
        self.chat_type: Optional[str] = chat_type
        self.location: Optional[Location] = location
        super().__init__(
            id=id,
            from_user=from_user,
            query=query,
            offset=offset,
            chat_type=chat_type,
            location=location,
        )