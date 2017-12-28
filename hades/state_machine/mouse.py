from time import time

from transitions import Machine, State

from hades.entity.action import Action
from hades.controller.base import Controller
from hades.entity.state import MouseState
from hades.lib import get_logger

logger = get_logger(__name__)


STATES = [
    State(MouseState.DEFAULT.name),
    State(MouseState.LEFT_DOWN.name),
    State(MouseState.RIGHT_DOWN.name),
]

TRANSITIONS = [
    {
        'trigger': 'left_down',
        'source': MouseState.DEFAULT.name,
        'dest': MouseState.LEFT_DOWN.name,
    },
    {
        'trigger': 'left_up',
        'source': MouseState.LEFT_DOWN.name,
        'dest': MouseState.LEFT_CLICK.name,
        'after': 'on_left_click',
    },
    {
        'trigger': 'right_down',
        'source': MouseState.DEFAULT.name,
        'dest': MouseState.RIGHT_DOWN.name,
    },
    {
        'trigger': 'right_up',
        'source': MouseState.RIGHT_DOWN.name,
        'dest': MouseState.RIGHT_CLICK.name,
        'after': 'on_right_click',
    },
]


class MouseStateMachine(Machine):

    def __init__(self, controller: Controller):
        self.state = None
        self.controller = controller
        super().__init__(states=STATES, transitions=TRANSITIONS, initial=MouseState.DEFAULT.name)

    def move(self, x, y):
        pass

    def unknown_down(self):
        raise Exception('unsupported key pressed')

    def unknown_up(self):
        raise Exception('unsupported key pressed')

    def left_down(self):
        pass

    def left_up(self):
        pass

    def right_down(self):
        pass

    def right_up(self):
        pass

    def scroll(self, x, y, dx, dy):
        pass

    def on_left_click(self):
        action = Action(type_=MouseState.LEFT_CLICK, timestamp=int(time()))
        self.controller.register_action(action)

    def on_right_click(self):
        action = Action(type_=MouseState.RIGHT_CLICK, timestamp=int(time()))
        self.controller.register_action(action)
