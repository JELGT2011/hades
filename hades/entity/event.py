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


MARK_ITERATION_EVENT = KeyboardEventType.PRESS


class Event(Entity):

    def __init__(self, type_: EventType, timestamp: int, args: tuple):
        self.type_ = type_
        self.timestamp = timestamp
        self.args = args


class MouseEvent(Event):

    def __init__(self,
                 type_: MouseEventType,
                 timestamp: int,
                 x: float,
                 y: float,
                 dx: int,
                 dy: int,
                 button: str,
                 pressed: bool):
        self.type_ = type_
        self.timestamp = timestamp
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.button = button
        self.pressed = pressed


class KeyboardEvent(Event):

    def __init__(self,
                 type_: KeyboardEventType,
                 timestamp: int,
                 key: str,
                 pressed: bool):
        self.type_ = type_
        self.timestamp = timestamp
        self.key = key
        self.pressed = pressed
