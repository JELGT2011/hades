from abc import ABC
from enum import Enum as Enum_


# TODO: move to a framework for these
class Entity(ABC):
    pass


class Enum(Enum_):

    def __str__(self):
        return self.name
