from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from esfigram.types.webapp_info import WebAppInfo


class MenuButton(BaseObject):
    def __init__(self, type: str, **kwargs) -> None:
        self.type = type
        super().__init__(type=type, **kwargs)


class MenuButtonCommands(MenuButton):
    def __init__(self) -> None:
        super().__init__(type="commands")


class MenuButtonWebApp(MenuButton):
    def __init__(self, text: str, web_app: WebAppInfo) -> None:
        self.text = text
        self.web_app = web_app
        super().__init__(type="web_app", text=text, web_app=web_app)


class MenuButtonDefault(MenuButton):
    def __init__(self) -> None:
        super().__init__(type="default")