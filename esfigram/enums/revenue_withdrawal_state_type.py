from enum import Enum


class RevenueWithdrawalStateType(str, Enum):
    """
    Represents the state of a revenue withdrawal operation.

    For more details, visit:
    https://core.telegram.org/bots/api#revenuewithdrawalstate

    Attributes:
        FAILED: The withdrawal failed and the transaction was refunded.
        PENDING: The withdrawal is in progress.
        SUCCEEDED: The withdrawal succeeded.
    """
    FAILED = "failed"
    PENDING = "pending"
    SUCCEEDED = "succeeded"

    @classmethod
    def list_states(cls):
        """
        Returns a list of all revenue withdrawal states.

        Returns:
            list[str]: A list of all withdrawal state types.
        """
        return [state.value for state in cls]

