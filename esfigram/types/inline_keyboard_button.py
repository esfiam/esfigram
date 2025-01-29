from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.callback_game import CallbackGame
    from esfigram.types.copy_text_button import CopyTextButton
    from esfigram.types.login_url import LoginUrl
    from esfigram.types.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
    from esfigram.types.webapp_info import WebAppInfo


class InlineKeyboardButton(BaseObject):
    def __init__(
        self,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
        web_app: Optional[WebAppInfo] = None,
        login_url: Optional[LoginUrl] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = None,
        copy_text: Optional[CopyTextButton] = None,
        callback_game: Optional[CallbackGame] = None,
        pay: Optional[bool] = None,
    ) -> None:
        self.text: str = text
        self.url: Optional[str] = url
        self.callback_data: Optional[str] = callback_data
        self.web_app: Optional[WebAppInfo] = web_app
        self.login_url: Optional[LoginUrl] = login_url
        self.switch_inline_query: Optional[str] = switch_inline_query
        self.switch_inline_query_current_chat: Optional[str] = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = switch_inline_query_chosen_chat
        self.copy_text: Optional[CopyTextButton] = copy_text
        self.callback_game: Optional[CallbackGame] = callback_game
        self.pay: Optional[bool] = pay
        super().__init__(
            text=text,
            url=url,
            callback_data=callback_data,
            web_app=web_app,
            login_url=login_url,
            switch_inline_query=switch_inline_query,
            switch_inline_query_current_chat=switch_inline_query_current_chat,
            switch_inline_query_chosen_chat=switch_inline_query_chosen_chat,
            copy_text=copy_text,
            callback_game=callback_game,
            pay=pay,
        )