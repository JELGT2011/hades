from enum import auto
from hades.entity.base import Enum


class MouseState(Enum):
    DEFAULT = auto()
    LEFT_DOWN = auto()
    RIGHT_DOWN = auto()
    LEFT_CLICK = auto()
    RIGHT_CLICK = auto()


class KeyboardState(Enum):
    DEFAULT = auto()
    MODIFIED = auto()


MARK_ITERATION_ACTION = MouseState.RIGHT_CLICK
