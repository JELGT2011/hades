from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.lib import get_logger

logger = get_logger(__name__)


class InputController(Controller):

    def __init__(self):
        from hades.controller.callback import on_move, on_click, on_scroll, on_press, on_release
        self.listeners = [
            keyboard.Listener(
                on_press=on_press,
                on_release=on_release,
            ),
            mouse.Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll,
            ),
        ]

    def start(self):
        for listener in self.listeners:
            listener.start()
            listener.wait()

    def stop(self):
        for listener in self.listeners:
            listener.stop()

    @property
    def running(self):
        return all([listener.running for listener in self.listeners])


input_controller = InputController()
