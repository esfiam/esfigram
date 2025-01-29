from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from esfigram.types.shared_user import SharedUser


class UsersShared(BaseObject):
    def __init__(self, request_id: int, users: List[SharedUser], **kwargs) -> None:
        self.request_id = request_id
        self.users = users
        super().__init__(request_id=request_id, users=users, **kwargs)