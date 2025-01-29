from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.user import User
    from esfigram.types.chat import Chat
    from typing import Optional, List


class PollAnswer(BaseObject):
    def __init__(
        self,
        poll_id: str,
        option_ids: List[int],
        voter_chat: Optional[Chat] = None,
        user: Optional[User] = None,
    ) -> None:
        self.poll_id = poll_id
        self.option_ids = option_ids
        self.voter_chat = voter_chat
        self.user = user
        super().__init__(
            poll_id=poll_id,
            option_ids=option_ids,
            voter_chat=voter_chat,
            user=user,
        )