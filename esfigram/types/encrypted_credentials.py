from __future__ import annotations
from esfigram.types.base_object import BaseObject


class EncryptedCredentials(BaseObject):
    def __init__(self, data: str, hash: str, secret: str) -> None:
        self.data = data
        self.hash = hash
        self.secret = secret
        super().__init__(data=data, hash=hash, secret=secret)