from enum import Enum

from transitions import Machine, State


class KeyboardState(Enum):
    DEFAULT = 'default'
    MODIFIED = 'modified'

    def __str__(self):
        return self.name


STATES = [
    State(KeyboardState.DEFAULT.name),
    State(KeyboardState.MODIFIED.name),
]

TRANSITIONS = [
    {'trigger': 'caps_locks', 'source': KeyboardState.DEFAULT, 'dest': KeyboardState.MODIFIED.name, 'conditions': []},
]


class KeyboardStateMachine(object):

    def __init__(self):
        self.state = None
        self.machine = Machine(model=self, states=STATES, transitions=TRANSITIONS, initial=KeyboardState.DEFAULT.name)


keyboard_state_machine = KeyboardStateMachine()
