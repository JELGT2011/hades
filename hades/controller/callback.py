from enum import Enum
from time import time

from hades.entity.action import Action, MouseActionType, KeyboardActionType
from hades.lib import get_logger
from hades.matcher import matcher

logger = get_logger(__name__)


MOUSE_PRESS_MAPPING = {
    True: MouseActionType.BUTTON_DOWN,
    False: MouseActionType.BUTTON_UP,
}


# noinspection PyUnusedLocal
def on_move(x: float, y: float):
    # kwargs = {'x': x, 'y': y}
    # action = Action({
    #     'type_': MouseActionType.MOVE,
    #     'timestamp': int(time()),
    #     'kwargs': kwargs,
    # })
    # matcher.append(action)
    pass


def on_scroll(x: float, y: float, dx: float, dy: float):
    kwargs = {'x': x, 'y': y, 'dx': dx, 'dy': dy}
    action = Action({
        'type_': MouseActionType.SCROLL.name,
        'timestamp': int(time()),
        'kwargs': kwargs,
    })
    matcher.append(action)


def on_click(x: float, y: float, button: Enum, pressed: bool):
    kwargs = {'x': x, 'y': y, 'button': button, 'pressed': pressed}
    action = Action({
        'type_': MOUSE_PRESS_MAPPING[pressed].name,
        'timestamp': int(time()),
        'kwargs': kwargs,
    })
    matcher.append(action)


def on_press(key: Enum):
    kwargs = {'key': key}
    action = Action({
        'type_': KeyboardActionType.KEY_DOWN.name,
        'timestamp': int(time()),
        'kwargs': kwargs,
    })
    matcher.append(action)


def on_release(key: Enum):
    kwargs = {'key': key}
    action = Action({
        'type_': KeyboardActionType.KEY_UP.name,
        'timestamp': int(time()),
        'kwargs': kwargs,
    })
    matcher.append(action)
