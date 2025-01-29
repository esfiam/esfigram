from enum import Enum


class MaskPositionPoint(str, Enum):
    """
    Represents the part of the face relative to which the mask should be placed.

    For more details, visit:
    https://core.telegram.org/bots/api#maskposition

    Attributes:
        FOREHEAD: The mask should be placed relative to the forehead.
        EYES: The mask should be placed relative to the eyes.
        MOUTH: The mask should be placed relative to the mouth.
        CHIN: The mask should be placed relative to the chin.
    """
    FOREHEAD = "forehead"
    EYES = "eyes"
    MOUTH = "mouth"
    CHIN = "chin"

    @classmethod
    def list_positions(cls):
        """
        Returns a list of all mask position points.

        Returns:
            list[str]: A list of all position points.
        """
        return [position.value for position in cls]

