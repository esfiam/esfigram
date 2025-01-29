from enum import Enum


class PollType(str, Enum):
    """
    Represents the type of a poll.

    For more details, visit:
    https://core.telegram.org/bots/api#poll

    Attributes:
        REGULAR: A regular poll where users can select one or multiple options.
        QUIZ: A quiz-style poll where only one option is correct.
    """
    REGULAR = "regular"
    QUIZ = "quiz"

    @classmethod
    def list_poll_types(cls):
        """
        Returns a list of all available poll types.

        Returns:
            list[str]: A list of all poll types.
        """
        return [poll.value for poll in cls]

