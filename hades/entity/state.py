from enum import auto
from hades.entity.base import Enum


class MouseState(Enum):
    DEFAULT = auto()
    UP = auto()
    DOWN = auto()


class KeyboardState(Enum):
    DEFAULT = auto()
    UP = auto()
    DOWN = auto()


MARK_ITERATION_ACTION = MouseState.RIGHT_CLICK
