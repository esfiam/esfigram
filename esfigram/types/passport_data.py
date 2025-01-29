from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from esfigram.types.encrypted_credentials import EncryptedCredentials
    from esfigram.types.encrypted_passport_element import EncryptedPassportElement


class PassportData(BaseObject):
    def __init__(self, data: List[EncryptedPassportElement], credentials: EncryptedCredentials) -> None:
        self.data = data
        self.credentials = credentials
        super().__init__(data=data, credentials=credentials)