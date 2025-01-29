from enum import Enum


class EncryptedPassportElement(str, Enum):
    """
    Represents types of encrypted passport elements in Telegram.

    For more details, visit:
    https://core.telegram.org/bots/api#encryptedpassportelement

    Attributes:
        PERSONAL_DETAILS: Personal details of the user.
        PASSPORT: Passport information.
        DRIVER_LICENSE: Driver's license information.
        IDENTITY_CARD: Identity card information.
        INTERNAL_PASSPORT: Internal passport information.
        ADDRESS: Address details.
        UTILITY_BILL: Utility bill information.
        BANK_STATEMENT: Bank statement details.
        RENTAL_AGREEMENT: Rental agreement information.
        PASSPORT_REGISTRATION: Passport registration details.
        TEMPORARY_REGISTRATION: Temporary registration details.
        PHONE_NUMBER: User's phone number.
        EMAIL: User's email address.
    """
    PERSONAL_DETAILS = "personal_details"
    PASSPORT = "passport"
    DRIVER_LICENSE = "driver_license"
    IDENTITY_CARD = "identity_card"
    INTERNAL_PASSPORT = "internal_passport"
    ADDRESS = "address"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    RENTAL_AGREEMENT = "rental_agreement"
    PASSPORT_REGISTRATION = "passport_registration"
    TEMPORARY_REGISTRATION = "temporary_registration"
    PHONE_NUMBER = "phone_number"
    EMAIL = "email"

    @classmethod
    def list_elements(cls):
        """
        Returns a list of all encrypted passport element types.

        Returns:
            list[str]: A list of all passport element types.
        """
        return [element.value for element in cls]

