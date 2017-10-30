import pynput

from hades.entity.input_listener_callback import on_keyboard_press
from hades.entity.input_listener_callback import on_keyboard_release
from hades.entity.input_listener_callback import on_mouse_click
from hades.entity.input_listener_callback import on_mouse_move
from hades.entity.input_listener_callback import on_mouse_scroll
from hades.lib import get_logger

logger = get_logger(__name__)


mouse_listener = pynput.mouse.Listener(
    on_move=on_mouse_move,
    on_click=on_mouse_click,
    on_scroll=on_mouse_scroll,
)

keyboard_listener = pynput.keyboard.Listener(
    on_press=on_keyboard_press,
    on_release=on_keyboard_release,
)
