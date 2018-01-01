from typing import Iterable

from pynput import keyboard, mouse

from hades.controller.base import Controller
from hades.entity.action import Action, MouseActionType, KeyboardActionType
from hades.lib import get_logger

logger = get_logger(__name__)

keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()


ACTION_TYPE_TO_CONTROLLER_FUNCTION = {
    MouseActionType.MOVE: lambda controller, kwargs: controller.move(dx=kwargs['dx'], dy=kwargs['dy']),
    MouseActionType.SCROLL: lambda controller, kwargs: controller.scroll(dx=kwargs['dx'], dy=kwargs['dy']),
    MouseActionType.BUTTON_DOWN: lambda controller, kwargs: controller.press(button=kwargs['button']),
    MouseActionType.BUTTON_UP: lambda controller, kwargs: controller.release(button=kwargs['button']),
    # MouseActionType.BUTTON_CLICK: lambda controller, kwargs: controller.click(button=kwargs['button']),
    KeyboardActionType.KEY_DOWN: lambda controller, kwargs: controller.press(key=kwargs['key']),
    KeyboardActionType.KEY_UP: lambda controller, kwargs: controller.release(key=kwargs['key']),
    # KeyboardActionType.KEY_CLICK: lambda controller, kwargs: controller.type(string=None),
}


class OutputController(Controller):

    def replay_actions(self, actions: Iterable[Action], iterations: int=0):
        for i in range(iterations):
            for action in actions:
                self.replay_action(action)

    def replay_action(self, action: Action):
        if isinstance(action.type_, MouseActionType):
            controller = mouse_controller
        else:
            controller = keyboard_controller
        func = ACTION_TYPE_TO_CONTROLLER_FUNCTION[action.type_]
        func(controller, action.kwargs)


output_controller = OutputController()
