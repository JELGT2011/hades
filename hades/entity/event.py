from enum import Enum, auto

from hades.entity.base import Entity


class EventType(Enum):

    NO_OP = auto()

    MOUSE_MOVE = auto()
    MOUSE_CLICK = auto()
    MOUSE_SCROLL = auto()
    KEY_PRESS = auto()
    KEY_RELEASE = auto()

    STRING = auto()
    MODIFIED_STRING = auto()

    COMPOUND = auto()


class Event(Entity):

    def __init__(self, type_: EventType, timestamp: int, args):
        self.type_ = type_
        self.timestamp = timestamp
        self.args = args
