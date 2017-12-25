from collections import UserList
from difflib import SequenceMatcher


class EventMatcher(UserList):

    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.sequence_matcher = SequenceMatcher(autojunk=False)

    def append(self, item):
        super().append(item)
        pass

    def find_matches(self):
        pass
        # matcher = self.sequence_matcher(a='', b='')
