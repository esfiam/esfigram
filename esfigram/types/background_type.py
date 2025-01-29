from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional
    from esfigram.types.background_fill import BackgroundFill
    from esfigram.types.document import Document


class BackgroundType(BaseObject):
    pass


class BackgroundTypeFill(BackgroundType):
    def __init__(self, fill: BackgroundFill, dark_theme_dimming: int) -> None:
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming
        super().__init__(type="fill", fill=fill, dark_theme_dimming=dark_theme_dimming)


class BackgroundTypeWallpaper(BackgroundType):
    def __init__(
            self,
            document: Document,
            dark_theme_dimming: int,
            is_blurred: Optional[bool] = None,
            is_moving: Optional[bool] = None,
    ) -> None:
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving
        super().__init__(
            type="wallpaper",
            document=document,
            dark_theme_dimming=dark_theme_dimming,
            is_blurred=is_blurred,
            is_moving=is_moving,
        )


class BackgroundTypePattern(BackgroundType):
    def __init__(
            self,
            document: Document,
            fill: BackgroundFill,
            intensity: int,
            is_inverted: Optional[bool] = None,
            is_moving: Optional[bool] = None,
    ) -> None:
        self.document = document
        self.fill = fill
        self.intensity = intensity
        self.is_inverted = is_inverted
        self.is_moving = is_moving
        super().__init__(
            type="pattern",
            document=document,
            fill=fill,
            intensity=intensity,
            is_inverted=is_inverted,
            is_moving=is_moving,
        )


class BackgroundTypeChatTheme(BackgroundType):
    def __init__(self, theme_name: str) -> None:
        self.theme_name = theme_name
        super().__init__(type="chat_theme", theme_name=theme_name)