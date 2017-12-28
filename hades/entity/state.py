from enum import auto
from hades.entity.base import Enum


class MouseState(Enum):
    DEFAULT = auto()
    LEFT_DOWN = auto()
    RIGHT_DOWN = auto()


class KeyboardState(Enum):
    DEFAULT = auto()
    STANDARD_DOWN = auto()
    MODIFIER_DOWN = auto()


MARK_ITERATION_ACTION = MouseState.RIGHT_CLICK
