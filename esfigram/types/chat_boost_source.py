from esfigram.types.base_object import BaseObject


class ChatBoostSource(BaseObject):
    pass


class ChatBoostSourcePremium(ChatBoostSource):
    def __init__(self, user) -> None:
        self.user = user
        super().__init__(source="premium", user=self.user)


class ChatBoostSourceGiftCode(ChatBoostSource):
    def __init__(self, user) -> None:
        self.user = user
        super().__init__(source="gift_code", user=self.user)


class ChatBoostSourceGiveaway(ChatBoostSource):
    def __init__(
        self,
        giveaway_message_id: int,
        user=None,
        prize_star_count=None,
        is_unclaimed=None,
    ) -> None:
        self.giveaway_message_id = giveaway_message_id
        self.user = user
        self.prize_star_count = prize_star_count
        self.is_unclaimed = is_unclaimed
        super().__init__(
            source="giveaway",
            giveaway_message_id=self.giveaway_message_id,
            user=self.user,
            prize_star_count=self.prize_star_count,
            is_unclaimed=self.is_unclaimed,
        )