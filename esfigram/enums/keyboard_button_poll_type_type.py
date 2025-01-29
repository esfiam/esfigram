from enum import Enum


class KeyboardButtonPollTypeType(str, Enum):
    """
    Represents the type of a poll that can be created and sent when the corresponding button is pressed.

    For more details, visit:
    https://core.telegram.org/bots/api#keyboardbuttonpolltype

    Attributes:
        QUIZ: A quiz-type poll.
        REGULAR: A regular poll.
    """
    QUIZ = "quiz"
    REGULAR = "regular"

    @classmethod
    def list_types(cls):
        """
        Returns a list of all keyboard button poll types.

        Returns:
            list[str]: A list of all poll types.
        """
        return [poll_type.value for poll_type in cls]

