from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from esfigram.types.passport_file import PassportFile


class EncryptedPassportElement(BaseObject):
    def __init__(
        self,
        type: str,
        data: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        files: Optional[List[PassportFile]] = None,
        front_side: Optional[PassportFile] = None,
        reverse_side: Optional[PassportFile] = None,
        selfie: Optional[PassportFile] = None,
        translation: Optional[List[PassportFile]] = None,
        hash: str = "",
    ) -> None:
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash
        super().__init__(
            type=type,
            data=data,
            phone_number=phone_number,
            email=email,
            files=files,
            front_side=front_side,
            reverse_side=reverse_side,
            selfie=selfie,
            translation=translation,
            hash=hash,
        )