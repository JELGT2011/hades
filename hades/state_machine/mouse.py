from enum import Enum, auto

from transitions import Machine, State


class MouseState(Enum):

    DEFAULT = auto()
    LEFT_DOWN = auto()
    SINGLE_CLICKED = auto()
    DOUBLE_CLICKED = auto()
    TRIPLE_CLICKED = auto()
    RIGHT_CLICKED = auto()

    def __str__(self):
        return self.name


STATES = [
    State(MouseState.DEFAULT.name),
    State(MouseState.LEFT_DOWN.name),
    State(MouseState.SINGLE_CLICKED.name),
    State(MouseState.DOUBLE_CLICKED.name),
]

TRANSITIONS = [
    {'trigger': 'left_down', 'source': MouseState.DEFAULT.name, 'dest': MouseState.LEFT_DOWN.name, 'conditions': []},
    {'trigger': 'left_up', 'source': MouseState.LEFT_DOWN.name, 'dest': MouseState.SINGLE_CLICKED.name, 'conditions': []},
]


class MouseStateMachine(object):

    def __init__(self):
        self.state = None
        self.machine = Machine(model=self, states=STATES, transitions=TRANSITIONS, initial=MouseState.DEFAULT.name)

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
