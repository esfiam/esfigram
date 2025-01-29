from __future__ import annotations
from typing import TYPE_CHECKING
from esfigram.types.base_object import BaseObject

if TYPE_CHECKING:
    from typing import Optional


class KeyboardButtonRequestUsers(BaseObject):
    def __init__(
        self,
        request_id: int,
        user_is_bot: Optional[bool] = None,
        user_is_premium: Optional[bool] = None,
        max_quantity: Optional[int] = 1,
        request_name: Optional[bool] = None,
        request_username: Optional[bool] = None,
        request_photo: Optional[bool] = None,
    ) -> None:
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo
        super().__init__(
            request_id=request_id,
            user_is_bot=user_is_bot,
            user_is_premium=user_is_premium,
            max_quantity=max_quantity,
            request_name=request_name,
            request_username=request_username,
            request_photo=request_photo,
        )