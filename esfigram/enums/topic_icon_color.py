from enum import Enum


class TopicIconColor(int, Enum):
    """
    Represents the color of a topic icon in RGB format.

    For more details, visit:
    https://github.com/telegramdesktop/tdesktop/blob/991fe491c5ae62705d77aa8fdd44a79caf639c45/Telegram/SourceFiles/data/data_forum_topic.cpp#L51-L56

    Attributes:
        BLUE: Blue color with RGB value 7322096.
        YELLOW: Yellow color with RGB value 16766590.
        VIOLET: Violet color with RGB value 13338331.
        GREEN: Green color with RGB value 9367192.
        ROSE: Rose color with RGB value 16749490.
        RED: Red color with RGB value 16478047.
    """
    BLUE = 7322096
    YELLOW = 16766590
    VIOLET = 13338331
    GREEN = 9367192
    ROSE = 16749490
    RED = 16478047

    @classmethod
    def list_colors(cls):
        """
        Returns a list of all topic icon colors.

        Returns:
            list[int]: A list of all topic icon color RGB values.
        """
        return [color.value for color in cls]

    @classmethod
    def get_color_name(cls, rgb_value: int) -> str:
        """
        Gets the name of the color by its RGB value.

        Args:
            rgb_value (int): The RGB value of the color.

        Returns:
            str: The name of the color if it exists, otherwise "Unknown".
        """
        for color in cls:
            if color.value == rgb_value:
                return color.name
        return "Unknown"


