from enum import Enum
from time import time

from hades.entity.action import Action, MouseActionType, KeyboardActionType
from hades.lib import get_logger
from hades.matcher.action import ActionMatcher

logger = get_logger(__name__)


MOUSE_PRESS_MAPPING = {
    True: MouseActionType.BUTTON_DOWN,
    False: MouseActionType.BUTTON_UP,
}

MATCHER = ActionMatcher()


# noinspection PyUnusedLocal
def on_move(x: float, y: float):
    # kwargs = {'x': x, 'y': y}
    # action = Action(type_=MouseActionType.MOVE, timestamp=int(time()), kwargs=kwargs)
    # input_controller.register_action(action)
    pass


def on_scroll(x: float, y: float, dx: float, dy: float):
    kwargs = {'x': x, 'y': y, 'dx': dx, 'dy': dy}
    action = Action(type_=MouseActionType.SCROLL, timestamp=int(time()), kwargs=kwargs)
    MATCHER.append(action)


def on_click(x: float, y: float, button: Enum, pressed: bool):
    kwargs = {'x': x, 'y': y, 'button': button.name, 'pressed': pressed}
    action = Action(type_=MOUSE_PRESS_MAPPING[pressed], timestamp=int(time()), kwargs=kwargs)
    MATCHER.append(action)


def on_press(key: Enum):
    kwargs = {'key': key.name, 'pressed': True}
    action = Action(type_=KeyboardActionType.KEY_DOWN, timestamp=int(time()), kwargs=kwargs)
    MATCHER.append(action)


def on_release(key: Enum):
    kwargs = {'key': key.name, 'pressed': False}
    action = Action(type_=KeyboardActionType.KEY_UP, timestamp=int(time()), kwargs=kwargs)
    MATCHER.append(action)
