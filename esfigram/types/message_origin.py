from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.chat import Chat
    from esfigram.types.user import User


class MessageOrigin(BaseObject):
    def __init__(self, type: str, date: int, **kwargs) -> None:
        self.type = type
        self.date = date
        super().__init__(type=type, date=date, **kwargs)


class MessageOriginUser(MessageOrigin):
    def __init__(self, date: int, sender_user: User, **kwargs) -> None:
        self.sender_user = sender_user
        super().__init__(type="user", date=date, sender_user=sender_user, **kwargs)


class MessageOriginHiddenUser(MessageOrigin):
    def __init__(self, date: int, sender_user_name: str, **kwargs) -> None:
        self.sender_user_name = sender_user_name
        super().__init__(type="hidden_user", date=date, sender_user_name=sender_user_name, **kwargs)


class MessageOriginChat(MessageOrigin):
    def __init__(self, date: int, sender_chat: Chat, author_signature: Optional[str] = None, **kwargs) -> None:
        self.sender_chat = sender_chat
        self.author_signature = author_signature
        super().__init__(type="chat", date=date, sender_chat=sender_chat, author_signature=author_signature, **kwargs)


class MessageOriginChannel(MessageOrigin):
    def __init__(self, date: int, chat: Chat, message_id: int, author_signature: Optional[str] = None, **kwargs) -> None:
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature
        super().__init__(type="channel", date=date, chat=chat, message_id=message_id, author_signature=author_signature, **kwargs)