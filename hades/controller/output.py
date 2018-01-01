from typing import List

from pynput import keyboard, mouse

from hades.entity.action import Action
from hades.controller.base import Controller
from hades.lib import get_logger

logger = get_logger(__name__)


class OutputController(Controller):

    def __init__(self):
        self.actuators = [
            keyboard.Controller(),
            mouse.Controller(),
        ]

    def replay_actions(self, actions: List[Action]):
        pass


output_controller = OutputController()
