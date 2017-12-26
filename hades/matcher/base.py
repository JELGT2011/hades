from difflib import SequenceMatcher as SequenceMatcher_
from typing import List, Union

from hades.entity.action import Action
from hades.entity.event import Event

MINIMUM_CONFIDENCE = 0.8

SET_SEQ_MAPPING = {
    True: 'set_seq1',
    False: 'set_seq2',
}


class SequenceMatcher(SequenceMatcher_):

    def __init__(self, isjunk=None, a='', b='', autojunk=False):
        super().__init__(isjunk=isjunk, a=a, b=b, autojunk=autojunk)
        self.iterations = list()

    def insert_iteration(self, iteration: List[Union[Event, Action]]):
        self.iterations.append(iteration)
        func = getattr(self, SET_SEQ_MAPPING[bool(self.b)])
        func([event.type_ for event in iteration])

    @property
    def found_match(self):
        return self.ratio() > MINIMUM_CONFIDENCE
