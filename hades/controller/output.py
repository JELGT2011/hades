from typing import List

from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.entity.action import Action, MouseActionType, KeyboardActionType
from hades.lib import get_logger

logger = get_logger(__name__)

ACTION_TYPE_TO_ACTUATOR_FUNCTION = {
    MouseActionType.MOVE: 'move',
    MouseActionType.SCROLL: 'scroll',
    MouseActionType.BUTTON_DOWN: 'press',
    MouseActionType.BUTTON_UP: 'release',
    MouseActionType.BUTTON_CLICK: 'click',
    MouseActionType.COMPOUND: None,
    KeyboardActionType.KEY_DOWN: 'press',
    KeyboardActionType.KEY_UP: 'release',
    KeyboardActionType.KEY_CLICK: 'type',
    KeyboardActionType.COMPOUND: None,
}


class OutputController(Controller):

    def __init__(self):
        self.actuators = {
            'keyboard': keyboard.Controller(),
            'mouse': mouse.Controller(),
        }

    def replay_actions(self, actions: List[Action], iterations: int=0):
        for i in range(iterations):
            for action in actions:
                self.replay_action(action)

    def replay_action(self, action: Action):

        if isinstance(action.type_, MouseActionType):
            actuator = self.actuators['mouse']
        else:
            actuator = self.actuators['keyboard']
        func = getattr(actuator, ACTION_TYPE_TO_ACTUATOR_FUNCTION[action.type_])
        func(**action.kwargs)


output_controller = OutputController()
