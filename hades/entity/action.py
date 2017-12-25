from enum import Enum

from hades.entity.base import Entity


class Action(Entity):

    def __init__(self, type_: Enum, timestamp: int):
        super().__init__()
        self.type_ = type_
        self.timestamp = timestamp
