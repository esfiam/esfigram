from enum import Enum


class PassportElementErrorType(str, Enum):
    """
    Represents the type of errors related to Telegram Passport elements.

    For more details, visit:
    https://core.telegram.org/bots/api#passportelementerror

    Attributes:
        DATA: Error in the provided data.
        FRONT_SIDE: Error in the front side of the document.
        REVERSE_SIDE: Error in the reverse side of the document.
        SELFIE: Error in the selfie with the document.
        FILE: Error in a single file.
        FILES: Error in multiple files.
        TRANSLATION_FILE: Error in a single translation file.
        TRANSLATION_FILES: Error in multiple translation files.
        UNSPECIFIED: An unspecified error.
    """
    DATA = "data"
    FRONT_SIDE = "front_side"
    REVERSE_SIDE = "reverse_side"
    SELFIE = "selfie"
    FILE = "file"
    FILES = "files"
    TRANSLATION_FILE = "translation_file"
    TRANSLATION_FILES = "translation_files"
    UNSPECIFIED = "unspecified"

    @classmethod
    def list_error_types(cls):
        """
        Returns a list of all available passport element error types.

        Returns:
            list[str]: A list of all error types.
        """
        return [error.value for error in cls]

