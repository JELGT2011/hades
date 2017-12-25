from enum import Enum, auto

from hades.entity.base import Entity


class EventType(Enum):
    NO_OP = auto()


class MouseEventType(Enum):
    MOVE = auto()
    CLICK = auto()
    SCROLL = auto()


class KeyboardEventType(Enum):
    PRESS = auto()
    RELEASE = auto()


class Event(Entity):

    def __init__(self, type_: EventType, timestamp: int, args):
        self.type_ = type_
        self.timestamp = timestamp
        self.args = args
