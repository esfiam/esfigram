from enum import Enum


class TransactionPartnerType(str, Enum):
    """
    Represents the type of a transaction partner.

    For more details, visit:
    https://core.telegram.org/bots/api#transactionpartner

    Attributes:
        FRAGMENT: The partner is a Fragment entity.
        OTHER: The partner is an unspecified entity.
        USER: The partner is a user.
        TELEGRAM_ADS: The partner is related to Telegram Ads.
        TELEGRAM_API: The partner is related to the Telegram API.
        AFFILIATE_PROGRAM: The partner is related to an affiliate program.
    """
    FRAGMENT = "fragment"
    OTHER = "other"
    USER = "user"
    TELEGRAM_ADS = "telegram_ads"
    TELEGRAM_API = "telegram_api"
    AFFILIATE_PROGRAM = "affiliate_program"

    @classmethod
    def list_partner_types(cls):
        """
        Returns a list of all transaction partner types.

        Returns:
            list[str]: A list of all partner type names.
        """
        return [partner.value for partner in cls]

    @classmethod
    def is_valid_partner_type(cls, partner_type: str) -> bool:
        """
        Checks if a given partner type is valid.

        Args:
            partner_type (str): The partner type to validate.

        Returns:
            bool: True if the partner type is valid, otherwise False.
        """
        return partner_type in cls._value2member_map_

