from enum import Enum
from time import time

from hades.entity.action import KeyDownKeyboardAction, KeyUpKeyboardAction, ButtonUpMouseAction, \
    ButtonDownMouseAction
from hades.lib import get_logger
from hades.matcher import matcher

logger = get_logger(__name__)


MOUSE_PRESS_MAPPING = {
    True: ButtonDownMouseAction,
    False: ButtonUpMouseAction,
}


def noop(*args, **kwargs):
    pass


def on_click(x: float, y: float, button: Enum, pressed: bool):
    action_class = MOUSE_PRESS_MAPPING[pressed]
    action = action_class({
        'timestamp': int(time()),
        'x': x,
        'y': y,
        'button': button.name,
    })
    matcher.append(action)


def on_press(key: Enum):
    action = KeyDownKeyboardAction({'timestamp': int(time()), 'key': key.name})
    matcher.append(action)


def on_release(key: Enum):
    action = KeyUpKeyboardAction({'timestamp': int(time()), 'key': key.name})
    matcher.append(action)
