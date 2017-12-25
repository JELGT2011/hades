from enum import auto
from hades.entity.base import Enum


class MouseState(Enum):
    DEFAULT = auto()
    LEFT_DOWN = auto()
    RIGHT_DOWN = auto()
    # MIDDLE_DOWN = auto()
    LEFT_CLICKED = auto()
    # DOUBLE_CLICKED = auto()
    # TRIPLE_CLICKED = auto()
    RIGHT_CLICKED = auto()
    # MIDDLE_CLICKED = auto()


class KeyboardState(Enum):
    DEFAULT = auto()
    MODIFIED = auto()
