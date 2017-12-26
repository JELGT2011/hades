from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.controller.callback import OnPress, OnRelease, OnMove, OnClick, OnScroll
from hades.entity.action import Action
from hades.entity.event import Event
from hades.entity.state import MARK_ITERATION_ACTION
from hades.lib import get_logger
from hades.matcher.action import ActionMatcher
from hades.matcher.event import EventMatcher
from hades.state_machine.keyboard import KeyboardStateMachine
from hades.state_machine.mouse import MouseStateMachine

logger = get_logger(__name__)


class InputController(Controller):

    def __init__(self):
        super().__init__()
        self.keyboard_state_machine = KeyboardStateMachine(controller=self)
        self.mouse_state_machine = MouseStateMachine(controller=self)
        self.state_machines = [
            self.keyboard_state_machine,
            self.mouse_state_machine,
        ]
        # TODO: move entirely to action matching
        self.event_matcher = EventMatcher()
        self.action_matcher = ActionMatcher()
        self.matchers = [
            self.event_matcher,
            self.action_matcher,
        ]
        self.listeners = [
            keyboard.Listener(
                on_press=OnPress(controller=self),
                on_release=OnRelease(controller=self),
            ),
            mouse.Listener(
                on_move=OnMove(controller=self),
                on_click=OnClick(controller=self),
                on_scroll=OnScroll(controller=self),
            ),
        ]

    def register_event(self, event: Event):
        self.events.append(event)

    def register_action(self, action: Action):
        self.actions.append(action)
        # if action.type_ == MARK_ITERATION_ACTION:
        #     self.action_matcher.insert_iteration(self.actions)
        #     self.actions = list()
        #     if self.action_matcher.found_match:
        #         print(self.action_matcher.get_opcodes())
        #         self.stop()

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
