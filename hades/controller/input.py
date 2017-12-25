from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.controller.callback import OnPress, OnRelease, OnMove, OnClick, OnScroll
from hades.entity.action import Action
from hades.entity.event import Event
from hades.lib import get_logger
from hades.state_machine.keyboard import KeyboardStateMachine
from hades.state_machine.mouse import MouseStateMachine

logger = get_logger(__name__)


class InputController(Controller):

    def __init__(self):
        super().__init__()
        self.keyboard_listener = keyboard.Listener(
            on_press=OnPress(controller=self),
            on_release=OnRelease(controller=self),
        )
        self.keyboard_listener.start()
        self.mouse_listener = mouse.Listener(
            on_move=OnMove(controller=self),
            on_click=OnClick(controller=self),
            on_scroll=OnScroll(controller=self),
        )
        self.listeners = [
            # self.keyboard_listener,
            self.mouse_listener,
        ]
        self.keyboard_state_machine = KeyboardStateMachine(controller=self)
        self.mouse_state_machine = MouseStateMachine(controller=self)

    def register_event(self, event: Event):
        self.events.append(event)

    def register_action(self, action: Action):
        self.actions.append(action)

    def start(self):
        for listener in self.listeners:
            listener.start()
            listener.join()
            listener.wait()

    def stop(self):
        [listener.stop() for listener in self.listeners]

    @property
    def running(self):
        return any([listener.running for listener in self.listeners])
