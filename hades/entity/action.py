from enum import auto

from hades.entity.base import Entity, Enum


class ActionType(Enum):
    pass


class MouseActionType(ActionType):
    MOVE = auto()
    SCROLL = auto()
    BUTTON_DOWN = auto()
    BUTTON_UP = auto()
    BUTTON_CLICK = auto()
    COMPOUND = auto()


class KeyboardActionType(ActionType):
    KEY_DOWN = auto()
    KEY_UP = auto()
    KEY_CLICK = auto()
    COMPOUND = auto()


class Action(Entity):

    def __init__(self, type_: ActionType, timestamp: int, kwargs: dict):
        super().__init__()
        self.type_ = type_
        self.timestamp = timestamp
        self.kwargs = kwargs
