from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import Optional


class WriteAccessAllowed(BaseObject):
    def __init__(
        self,
        from_request: Optional[bool] = None,
        web_app_name: Optional[str] = None,
        from_attachment_menu: Optional[bool] = None,
        **kwargs,
    ) -> None:
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu
        super().__init__(
            from_request=from_request,
            web_app_name=web_app_name,
            from_attachment_menu=from_attachment_menu,
            **kwargs,
        )