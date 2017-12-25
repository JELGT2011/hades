from transitions import Machine, State

from hades.controller.base import Controller
from hades.entity.state import KeyboardState

STATES = [
    State(KeyboardState.DEFAULT.name),
    State(KeyboardState.MODIFIED.name),
]

TRANSITIONS = [
    {
        'trigger': 'caps_lock_down',
        'source': [KeyboardState.DEFAULT.name],
        'dest': KeyboardState.MODIFIED.name,
    },
]


class KeyboardStateMachine(Machine):

    def __init__(self, controller: Controller):
        self.state = None
        self.controller = controller
        super().__init__(states=STATES, transitions=TRANSITIONS, initial=KeyboardState.DEFAULT.name)
