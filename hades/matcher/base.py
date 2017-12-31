from abc import abstractmethod
from difflib import SequenceMatcher as SequenceMatcher_
from typing import List

from hades.entity.action import Action

MINIMUM_CONFIDENCE = 0.8


class Matcher(SequenceMatcher_):

    @abstractmethod
    def insert_iteration(self, iteration: List[Action]):
        pass

    @property
    def found_match(self):
        return self.ratio() > MINIMUM_CONFIDENCE
