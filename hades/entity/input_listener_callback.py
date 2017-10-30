import time

from entity.action import Action
from hades.lib import get_logger, capture_screen

logger = get_logger(__name__)


def no_op(*args, **kwargs):
    return no_op.__name__


def on_mouse_move(x, y):
    return on_mouse_move.__name__


def on_mouse_click(x, y, button, pressed):
    logger.info('{} called with args: {} {} {} {}'.format(on_mouse_click.__name__, x, y, button, pressed))
    timestamp = int(time.time())
    screenshot = capture_screen(timestamp=timestamp)
    action = Action(input_event=on_mouse_click.__name__, screenshot=screenshot)
    return on_mouse_click.__name__


def on_mouse_scroll(x, y, dx, dy):
    logger.info('{} called with args: {} {} {} {}'.format(on_mouse_scroll.__name__, x, y, dx, dy))
    timestamp = int(time.time())
    screenshot = capture_screen(timestamp=timestamp)
    action = Action(input_event=on_mouse_scroll.__name__, screenshot=screenshot)
    return on_mouse_scroll.__name__


def on_keyboard_press(key):
    logger.info('{} called with args: {}'.format(on_keyboard_press.__name__, key))
    timestamp = int(time.time())
    screenshot = capture_screen(timestamp=timestamp)
    action = Action(input_event=on_keyboard_press.__name__, screenshot=screenshot)
    return on_keyboard_press.__name__


def on_keyboard_release(key):
    logger.info('{} called with args: {}'.format(on_keyboard_release.__name__, key))
    timestamp = int(time.time())
    screenshot = capture_screen(timestamp=timestamp)
    action = Action(input_event=on_keyboard_release.__name__, screenshot=screenshot)
    return on_keyboard_release.__name__

