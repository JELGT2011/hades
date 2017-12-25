from enum import auto

from hades.entity.base import Entity, Enum


class EventType(Enum):
    pass


class MouseEventType(EventType):
    MOVE = auto()
    CLICK = auto()
    SCROLL = auto()


class KeyboardEventType(EventType):
    PRESS = auto()
    RELEASE = auto()


class Event(Entity):

    def __init__(self, type_: Enum, timestamp: int, args: tuple):
        self.type_ = type_
        self.timestamp = timestamp
        self.args = args
