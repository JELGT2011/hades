from time import sleep
from typing import List

from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.entity.action import Action, ButtonDownMouseAction, ButtonUpMouseAction, KeyDownKeyboardAction, \
    KeyUpKeyboardAction, MouseAction, KeyboardAction
from hades.lib import get_logger

logger = get_logger(__name__)

keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()


ACTION_TYPE_TO_CONTROLLER_FUNCTION = {
    ButtonDownMouseAction: lambda action: mouse_controller.press(button=action.button),
    ButtonUpMouseAction: lambda action: mouse_controller.release(button=action.button),
    KeyDownKeyboardAction: lambda action: keyboard_controller.press(key=action.key),
    KeyUpKeyboardAction: lambda action: keyboard_controller.release(key=action.key),
}


class OutputController(Controller):

    def replay_actions(self, actions: List[Action], deltas: List[Action], iterations: int=0):
        assert len(actions) == len(deltas)
        for i in range(iterations):
            for action in actions:
                self.replay_action(action)
            actions = [actions[i] + deltas[i] for i in range(len(actions))]

    def replay_action(self, action: Action):
        assert isinstance(action, (MouseAction, KeyboardAction)), 'Unknown Action, {}'.format(action.__class__)
        if isinstance(action, MouseAction):
            self.move_mouse_absolute(action.x, action.y)
        # TODO: respect timestamp delta option
        sleep(int(action.timestamp))
        # noinspection PyTypeChecker
        func = ACTION_TYPE_TO_CONTROLLER_FUNCTION[action.__class__]
        func()

    def move_mouse_relative(self, dx: float=0, dy: float=0):
        mouse_controller.move(dx, dy)

    def move_mouse_absolute(self, x: float=0, y: float=0):
        dx, dy = mouse_controller.position
        mouse_controller.move(x - dx, y - dy)


output_controller = OutputController()
