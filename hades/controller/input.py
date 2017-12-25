from functools import partial

from pynput import keyboard, mouse
from six import reraise

from hades.controller.base import Controller
from hades.controller.callback import OnPress, OnRelease, OnMove, OnClick, OnScroll
from hades.entity.action import Action
from hades.entity.event import Event, MARK_ITERATION_EVENT
from hades.entity.state import MARK_ITERATION_ACTION
from hades.lib import get_logger
from hades.state_machine.keyboard import KeyboardStateMachine
from hades.state_machine.mouse import MouseStateMachine

logger = get_logger(__name__)


class InputController(Controller):

    def __init__(self):
        super().__init__()
        self.keyboard_listener_factory = partial(
            keyboard.Listener,
            on_press=OnPress(controller=self),
            on_release=OnRelease(controller=self),
        )
        self.keyboard_listener = None
        self.mouse_listener_factory = partial(
            mouse.Listener,
            on_move=OnMove(controller=self),
            on_click=OnClick(controller=self),
            on_scroll=OnScroll(controller=self),
        )
        self.mouse_listener = None
        self.listener_factories = {
            'keyboard': self.keyboard_listener_factory,
            'mouse': self.mouse_listener_factory,
        }
        self.listeners = {
            'keyboard': self.keyboard_listener,
            'mouse': self.mouse_listener,
        }
        self.keyboard_state_machine = KeyboardStateMachine(controller=self)
        self.mouse_state_machine = MouseStateMachine(controller=self)
        self.state_machines = [
            self.keyboard_state_machine,
            self.mouse_state_machine,
        ]

    def register_event(self, event: Event):
        self.events.append(event)
        if event.type_ == MARK_ITERATION_EVENT:
            logger.info('iteration event')

    def register_action(self, action: Action):
        self.actions.append(action)
        if action.type_ == MARK_ITERATION_ACTION:
            logger.info('iteration action')

    def start(self):
        with self.mouse_listener_factory() as self.mouse_listener:
            self.listeners['mouse'] = self.mouse_listener
            with self.keyboard_listener_factory() as self.keyboard_listener:
                self.listeners['keyboard'] = self.keyboard_listener
                while not self.stopped:
                    pass
                for name, listener in self.listeners.items():
                    if not listener.running:
                        # noinspection PyProtectedMember
                        exc_type, exc_value, exc_traceback = listener._queue.get()
                        reraise(exc_type, exc_value, exc_traceback)

    def stop(self):
        [listener.stop() for name, listener in self.listeners.items() if listener.running]

    @property
    def stopped(self):
        return any([not listener.running for name, listener in self.listeners.items()])

    @property
    def running(self):
        return all([listener.running for name, listener in self.listeners.items()])
