from transitions import Machine, State

from hades.controller.base import Controller
from hades.entity.state import MouseState
from hades.lib import get_logger

logger = get_logger(__name__)


STATES = [
    State(MouseState.DEFAULT.name),
    State(MouseState.LEFT_DOWN.name),
    State(MouseState.SINGLE_CLICKED.name, on_enter=['register_action']),
    State(MouseState.DOUBLE_CLICKED.name, on_enter=['register_action']),
    State(MouseState.TRIPLE_CLICKED.name, on_enter=['register_action']),
    State(MouseState.RIGHT_CLICKED.name, on_enter=['register_action']),
    State(MouseState.MIDDLE_CLICKED.name, on_enter=['register_action']),
]

TRANSITIONS = [
    {'trigger': 'left_down', 'source': MouseState.DEFAULT.name, 'dest': MouseState.LEFT_DOWN.name},
    {'trigger': 'left_up', 'source': MouseState.LEFT_DOWN.name, 'dest': MouseState.SINGLE_CLICKED.name},
    {'trigger': 'right_down', 'source': MouseState.DEFAULT.name, 'dest': MouseState.RIGHT_DOWN.name},
    {'trigger': 'right_up', 'source': MouseState.RIGHT_DOWN.name, 'dest': MouseState.RIGHT_CLICKED.name},
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

    def register_action(self, *args, **kwargs):
        logger.info('{} called with {} and {}'.format(self.register_action.__name__, args, kwargs))
