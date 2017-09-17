from hades.input_listener import capture_screen
from hades.lib.logging import get_logger

logger = get_logger(__name__)


@capture_screen
def on_keyboard_press(key):
    logger.info('on_keyboard_press called with args: {}'.format(key))
    return on_keyboard_press.__name__


@capture_screen
def on_keyboard_release(key):
    logger.info('on_keyboard_release called with args: {}'.format(key))
    return on_keyboard_release.__name__
