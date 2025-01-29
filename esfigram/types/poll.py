from __future__ import annotations
from esfigram.types.base_object import BaseObject
from typing import TYPE_CHECKING, Optional, List

if TYPE_CHECKING:
    from esfigram.types.message_entity import MessageEntity
    from esfigram.types.poll_option import PollOption


class Poll(BaseObject):
    def __init__(
        self,
        id: str,
        question: str,
        options: List[PollOption],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
    ) -> None:
        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        super().__init__(
            id=id,
            question=question,
            options=options,
            total_voter_count=total_voter_count,
            is_closed=is_closed,
            is_anonymous=is_anonymous,
            type=type,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_id=correct_option_id,
            explanation=explanation,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
        )