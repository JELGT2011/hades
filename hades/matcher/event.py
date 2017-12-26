from typing import List

from hades.entity.event import Event
from hades.matcher.base import SequenceMatcher


class EventMatcher(SequenceMatcher):

    def insert_iteration(self, iteration: List[Event]):
        super().insert_iteration(iteration)
