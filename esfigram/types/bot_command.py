from __future__ import annotations
from esfigram.types.base_object import BaseObject


class BotCommand(BaseObject):
    def __init__(self, command: str, description: str) -> None:
        self.command = command
        self.description = description
        if not (1 <= len(command) <= 32) or not command.isidentifier():
            raise ValueError(
                "Command must be 1-32 characters long and can only contain lowercase English letters, digits, and underscores."
            )
        if not (1 <= len(description) <= 256):
            raise ValueError("Description must be 1-256 characters long.")
        super().__init__(command=command, description=description)