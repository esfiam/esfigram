from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, Union, List
    from esfigram.types.message_entity import MessageEntity


class ReplyParameters(BaseObject):
    def __init__(
        self,
        message_id: int,
        chat_id: Optional[Union[int, str]] = None,
        allow_sending_without_reply: Optional[bool] = None,
        quote: Optional[str] = None,
        quote_parse_mode: Optional[str] = None,
        quote_entities: Optional[List[MessageEntity]] = None,
        quote_position: Optional[int] = None,
    ) -> None:
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position
        super().__init__(
            message_id=message_id,
            chat_id=chat_id,
            allow_sending_without_reply=allow_sending_without_reply,
            quote=quote,
            quote_parse_mode=quote_parse_mode,
            quote_entities=quote_entities,
            quote_position=quote_position,
        )