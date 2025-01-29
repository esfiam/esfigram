from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class LoginUrl(BaseObject):
    def __init__(
        self,
        url: str,
        forward_text: Optional[str] = None,
        bot_username: Optional[str] = None,
        request_write_access: Optional[bool] = None,
    ) -> None:
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
        super().__init__(
            url=url,
            forward_text=forward_text,
            bot_username=bot_username,
            request_write_access=request_write_access,
        )