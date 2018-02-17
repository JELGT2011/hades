from difflib import SequenceMatcher

from hades.entity.action import Action
from hades.lib import get_logger

logger = get_logger(__name__)

MINIMUM_CONFIDENCE = 0.8
MINIMUM_ACTION_LENGTH = 2


class ActionMatcher(SequenceMatcher):

    def __init__(self, isjunk=None, a='', b='', autojunk=False):
        super().__init__(isjunk=isjunk, a=a, b=b, autojunk=autojunk)
        self.actions = list()
        self.deltas = list()

    def append(self, action: Action):
        self.actions.append(action)
        if not self.minimum_length:
            return
        mid = int(len(self.actions) / 2)
        action_types = [action.type_ for action in self.actions]
        left, right = action_types[mid:], action_types[:mid]
        self.set_seqs(left, right)

    def get_sequence_and_delta(self):
        mid = int(len(self.actions) / 2)
        left, right = self.actions[mid:], self.actions[:mid]

        # TODO: apply opcodes to sequence, instead of taking raw sequence
        opcodes = self.get_opcodes()
        sequence = left
        delta = [left[i] - right[i] for i in range(len(sequence))]
        return sequence, delta

    @property
    def minimum_length(self):
        return len(self.actions) >= MINIMUM_ACTION_LENGTH

    @property
    def found_match(self):
        return self.minimum_length and self.ratio() > MINIMUM_CONFIDENCE
