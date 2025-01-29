from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.webapp_info import WebAppInfo


class InlineQueryResultsButton(BaseObject):
    def __init__(
            self,
            text: str,
            web_app: Optional[WebAppInfo] = None,
            start_parameter: Optional[str] = None,
    ) -> None:
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter
        super().__init__(
            text=text,
            web_app=web_app,
            start_parameter=start_parameter,
        )