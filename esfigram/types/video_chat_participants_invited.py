from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.user import User


class VideoChatParticipantsInvited(BaseObject):
    def __init__(self, users: List[User], **kwargs) -> None:
        self.users = users
        super().__init__(users=users, **kwargs)