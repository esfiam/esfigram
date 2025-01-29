from esfigram.types.base_object import BaseObject
from typing import Optional, Union
from esfigram.types.user import User
from esfigram.types.maybe_inaccessible_message import Message, InaccessibleMessage


class CallbackQuery(BaseObject):
    def __init__(
        self,
        id: str,
        from_user: User,
        chat_instance: str,
        message: Optional[Union[Message, InaccessibleMessage]] = None,
        inline_message_id: Optional[str] = None,
        data: Optional[str] = None,
        game_short_name: Optional[str] = None,
    ) -> None:
        self.id = id
        self.from_user = from_user
        self.chat_instance = chat_instance
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data
        self.game_short_name = game_short_name
        super().__init__(
            id=self.id,
            from_user=self.from_user,
            chat_instance=self.chat_instance,
            message=self.message,
            inline_message_id=self.inline_message_id,
            data=self.data,
            game_short_name=self.game_short_name,
        )