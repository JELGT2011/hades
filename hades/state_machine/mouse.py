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
    State(MouseState.LEFT_CLICKED.name, on_enter=['on_single_click']),
    # State(MouseState.DOUBLE_CLICKED.name, on_enter=['on_double_click']),
    # State(MouseState.TRIPLE_CLICKED.name, on_enter=['on_triple_click']),
    State(MouseState.RIGHT_CLICKED.name, on_enter=['on_right_click']),
    # State(MouseState.MIDDLE_CLICKED.name, on_enter=['on_middle_click']),
]

TRANSITIONS = [
    {
        'trigger': 'left_down',
        'source': [MouseState.DEFAULT.name, MouseState.LEFT_CLICKED.name],
        'dest': MouseState.LEFT_DOWN.name,
    },
    {
        'trigger': 'left_up',
        'source': MouseState.LEFT_DOWN.name,
        'dest': MouseState.LEFT_CLICKED.name,
    },
    {
        'trigger': 'right_down',
        'source': MouseState.DEFAULT.name,
        'dest': MouseState.RIGHT_DOWN.name,
    },
    {
        'trigger': 'right_up',
        'source': MouseState.RIGHT_DOWN.name,
        'dest': MouseState.RIGHT_CLICKED.name,
    },
]


class MouseStateMachine(Machine):

    def __init__(self, controller: Controller):
        self.state = None
        self.controller = controller
        super().__init__(states=STATES, transitions=TRANSITIONS, initial=MouseState.DEFAULT.name)

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

    def middle_down(self):
        pass

    def middle_up(self):
        pass

    def on_single_click(self):
        action = Action(type_=MouseState.LEFT_CLICKED, timestamp=int(time()))
        self.controller.register_action(action)

    # def on_double_click(self):
    #     action = Action(type_=MouseState.DOUBLE_CLICKED, timestamp=int(time()))
    #     self.controller.register_action(action)
    #
    # def on_triple_click(self):
    #     action = Action(type_=MouseState.TRIPLE_CLICKED, timestamp=int(time()))
    #     self.controller.register_action(action)

    def on_right_click(self):
        action = Action(type_=MouseState.RIGHT_CLICKED, timestamp=int(time()))
        self.controller.register_action(action)

    def on_middle_click(self):
        action = Action(type_=MouseState.MIDDLE_CLICKED, timestamp=int(time()))
        self.controller.register_action(action)
