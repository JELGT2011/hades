from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.controller.callback import OnPress, OnRelease, OnMove, OnClick, OnScroll
from hades.entity.event import Event, EventType
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
        self.mouse_listener = mouse.Listener(
            on_move=OnMove(controller=self),
            on_click=OnClick(controller=self),
            on_scroll=OnScroll(controller=self),
        )
        self.listeners = [
            self.keyboard_listener,
            self.mouse_listener,
        ]
        self.keyboard_state_machine = KeyboardStateMachine()
        self.mouse_state_machine = MouseStateMachine()

    def register_event(self, event: Event):
        self.events.append(event)
        if event.type_ == EventType.MOUSE_SCROLL:
            self.stop()

    def start(self):
        [listener.start() for listener in self.listeners]

    def stop(self):
        [listener.stop() for listener in self.listeners]

    @property
    def running(self):
        return any([listener.running for listener in self.listeners])


input_controller = InputController()
