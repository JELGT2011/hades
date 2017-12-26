from transitions import Machine, State

from hades.controller.base import Controller
from hades.entity.state import KeyboardState

STATES = [
    State(KeyboardState.DEFAULT.name),
    State(KeyboardState.STANDARD_DOWN.name),
    State(KeyboardState.MODIFIER_DOWN.name),
]

TRANSITIONS = [
    {
        'trigger': 'standard_down',
        'source': [KeyboardState.DEFAULT.name],
        'dest': KeyboardState.STANDARD_DOWN.name,
    },
    {
        'trigger': 'standard_up',
        'source': [KeyboardState.STANDARD_DOWN.name],
        'dest': KeyboardState.DEFAULT.name,
    },
    {
        'trigger': 'modifier_down',
        'source': [KeyboardState.DEFAULT.name],
        'dest': KeyboardState.MODIFIER_DOWN.name,
    },
    {
        'trigger': 'modifier_up',
        'source': [KeyboardState.DEFAULT.name],
        'dest': KeyboardState.MODIFIED.name,
    },
]


class KeyboardStateMachine(Machine):

    def __init__(self, controller: Controller):
        self.state = None
        self.controller = controller
        super().__init__(states=STATES, transitions=TRANSITIONS, initial=KeyboardState.DEFAULT.name)

    def standard_down(self, key):
        pass

    def standard_up(self, key):
        pass

    def modifier_down(self, key):
        pass

    def modifier_up(self, key):
        pass
