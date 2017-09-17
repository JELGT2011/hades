import pynput

from hades.entity import Entity
from hades.entity.input_listener_callback import on_keyboard_press
from hades.entity.input_listener_callback import on_keyboard_release
from hades.entity.input_listener_callback import on_mouse_click
from hades.entity.input_listener_callback import on_mouse_move
from hades.entity.input_listener_callback import on_mouse_scroll
from hades.lib import get_logger

logger = get_logger(__name__)


class InputListener(Entity):

    def __init__(self, pynput_listener):
        super(Entity, self).__init__()
        self.pynput_listener = pynput_listener

    def start(self):
        self.pynput_listener.start()
        self.pynput_listener.wait()

    def stop(self):
        self.pynput_listener.stop()


mouse_listener = InputListener(
    pynput_listener=pynput.mouse.Listener(
        on_move=on_mouse_move,
        on_click=on_mouse_click,
        on_scroll=on_mouse_scroll,
    ),
)

keyboard_listener = InputListener(
    pynput_listener=pynput.keyboard.Listener(
        on_press=on_keyboard_press,
        on_release=on_keyboard_release,
    ),
)
