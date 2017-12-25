from transitions import Machine, Transition

DEFAULT = 'default'
MODIFIED = 'modified'


class KeyboardStateMachine(object):

    STATES = [
        DEFAULT,
        MODIFIED,
    ]

    TRANSITIONS = [
        Transition(source=DEFAULT, dest=MODIFIED, conditions=[]),
        Transition(source=MODIFIED, dest=DEFAULT, conditions=[]),
    ]

    def __init__(self):
        self.state = None
        self.machine = Machine(model=self, states=self.STATES, transitions=self.TRANSITIONS, initial=DEFAULT)
        self.modifiers = set()

    def modifier_down(self, modifier):
        self.modifiers.add(modifier)

    def modifier_up(self, modifier):
        self.modifiers.remove(modifier)


keyboard_state_machine = KeyboardStateMachine()
