from esfigram.types.base_object import BaseObject
from typing import Optional


class Chat(BaseObject):
    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        is_forum: Optional[bool] = None,
    ) -> None:
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        super().__init__(
            id=self.id,
            type=self.type,
            title=self.title,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            is_forum=self.is_forum,
        )