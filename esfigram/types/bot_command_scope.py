from __future__ import annotations
from typing import TYPE_CHECKING, Union
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    pass


class BotCommandScope(BaseObject):
    pass


class BotCommandScopeDefault(BotCommandScope):
    def __init__(self) -> None:
        self.scope_type = "default"
        super().__init__(scope_type=self.scope_type)


class BotCommandScopeAllPrivateChats(BotCommandScope):
    def __init__(self) -> None:
        self.scope_type = "all_private_chats"
        super().__init__(scope_type=self.scope_type)


class BotCommandScopeAllGroupChats(BotCommandScope):
    def __init__(self) -> None:
        self.scope_type = "all_group_chats"
        super().__init__(scope_type=self.scope_type)


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    def __init__(self) -> None:
        self.scope_type = "all_chat_administrators"
        super().__init__(scope_type=self.scope_type)


class BotCommandScopeChat(BotCommandScope):
    def __init__(self, chat_id: Union[int, str]) -> None:
        self.scope_type = "chat"
        self.chat_id = chat_id
        super().__init__(scope_type=self.scope_type, chat_id=self.chat_id)


class BotCommandScopeChatAdministrators(BotCommandScope):
    def __init__(self, chat_id: Union[int, str]) -> None:
        self.scope_type = "chat_administrators"
        self.chat_id = chat_id
        super().__init__(scope_type=self.scope_type, chat_id=self.chat_id)


class BotCommandScopeChatMember(BotCommandScope):
    def __init__(self, chat_id: Union[int, str], user_id: int) -> None:
        self.scope_type = "chat_member"
        self.chat_id = chat_id
        self.user_id = user_id
        super().__init__(scope_type=self.scope_type, chat_id=self.chat_id, user_id=self.user_id)