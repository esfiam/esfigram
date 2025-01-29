from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional


class Contact(BaseObject):
    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        user_id: Optional[int] = None,
        vcard: Optional[str] = None,
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
        super().__init__(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            user_id=user_id,
            vcard=vcard,
        )