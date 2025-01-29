from typing import Optional, Dict


class TelegramAPIError(Exception):
    """
    Base class for all Telegram API errors.
    """

    def __init__(self, message: str, method: str, params: Dict, status_code: Optional[int] = None):
        super().__init__(message)
        self.method = method
        self.params = params
        self.status_code = status_code

    def __str__(self):
        base_message = f"{self.__class__.__name__}: {self.args[0]}"
        details = f"(Method: {self.method}, Params: {self.params}, Status Code: {self.status_code})"
        return f"{base_message} {details}"


class BadRequestError(TelegramAPIError):
    """
    Represents a 400 Bad Request error from Telegram API.
    """
    pass


class UnauthorizedError(TelegramAPIError):
    """
    Represents a 401 Unauthorized error from Telegram API.
    """
    pass


class ForbiddenError(TelegramAPIError):
    """
    Represents a 403 Forbidden error from Telegram API.
    """
    pass


class NotFoundError(TelegramAPIError):
    """
    Represents a 404 Not Found error from Telegram API.
    """
    pass


class TooManyRequestsError(TelegramAPIError):
    """
    Represents a 429 Too Many Requests error from Telegram API.
    """

    def __init__(self, message: str, method: str, params: Dict, status_code: Optional[int] = None,
                 retry_after: Optional[int] = None):
        super().__init__(message, method, params, status_code)
        self.retry_after = retry_after

    def __str__(self):
        base_message = super().__str__()
        retry_info = f" Retry After: {self.retry_after}s" if self.retry_after else ""
        return f"{base_message}{retry_info}"


class InternalServerError(TelegramAPIError):
    """
    Represents a 500 Internal Server Error from Telegram API.
    """
    pass


class UnknownError(TelegramAPIError):
    """
    Represents an unknown error from Telegram API.
    """
    pass


# Optional: Mapping of HTTP status codes to specific error classes.
ERROR_MAP = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    429: TooManyRequestsError,
    500: InternalServerError,
}
