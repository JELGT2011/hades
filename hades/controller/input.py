from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.entity.action import Action
from hades.lib import get_logger
from hades.matcher.action import ActionMatcher

logger = get_logger(__name__)


class InputController(Controller):

    def __init__(self):
        from hades.controller.callback import on_move, on_click, on_scroll, on_press, on_release
        self.actions = list()
        self.matcher = ActionMatcher()
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

    def register_action(self, action: Action):
        self.actions.append(action)

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
