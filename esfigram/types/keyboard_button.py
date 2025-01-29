from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.keyboard_button_poll_type import KeyboardButtonPollType
    from esfigram.types.keyboard_button_request_chat import KeyboardButtonRequestChat
    from esfigram.types.keyboard_button_request_users import KeyboardButtonRequestUsers
    from esfigram.types.webapp_info import WebAppInfo


class KeyboardButton(BaseObject):
    def __init__(
        self,
        text: str,
        request_users: Optional[KeyboardButtonRequestUsers] = None,
        request_chat: Optional[KeyboardButtonRequestChat] = None,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional[KeyboardButtonPollType] = None,
        web_app: Optional[WebAppInfo] = None,
    ) -> None:
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app
        super().__init__(
            text=text,
            request_users=request_users,
            request_chat=request_chat,
            request_contact=request_contact,
            request_location=request_location,
            request_poll=request_poll,
            web_app=web_app,
        )