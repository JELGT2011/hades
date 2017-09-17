from hades.input_listener import capture_screen
from hades.lib.logging import get_logger

logger = get_logger(__name__)


@capture_screen
def on_mouse_click(x, y, button, pressed):
    logger.info('on_mouse_click called with args: {} {} {} {}'.format(x, y, button, pressed))
    return on_mouse_click.__name__


@capture_screen
def on_mouse_scroll(x, y, dx, dy):
    logger.info('on_mouse_scroll called with args: {} {} {} {}'.format(x, y, dx, dy))
    return on_mouse_scroll.__name__
