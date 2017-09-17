from hades.lib import get_logger
from hades.lib import capture_screen_wrapper

logger = get_logger(__name__)


def no_op(*args, **kwargs):
    return no_op.__name__


def on_mouse_move(x, y):
    return on_mouse_move.__name__


@capture_screen_wrapper
def on_mouse_click(x, y, button, pressed):
    logger.info('{} called with args: {} {} {} {}'.format(on_mouse_click.__name__, x, y, button, pressed))
    return on_mouse_click.__name__


@capture_screen_wrapper
def on_mouse_scroll(x, y, dx, dy):
    logger.info('{} called with args: {} {} {} {}'.format(on_mouse_scroll.__name__, x, y, dx, dy))
    return on_mouse_scroll.__name__


@capture_screen_wrapper
def on_keyboard_press(key):
    logger.info('{} called with args: {}'.format(on_keyboard_press.__name__, key))
    return on_keyboard_press.__name__


@capture_screen_wrapper
def on_keyboard_release(key):
    logger.info('{} called with args: {}'.format(on_keyboard_release.__name__, key))
    return on_keyboard_release.__name__

