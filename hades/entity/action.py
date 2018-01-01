from enum import auto

from schematics.types import StringType, IntType, DictType

from hades.entity.base import Entity, Enum


class ActionType(Enum):
    pass


class MouseActionType(ActionType):
    MOVE = auto()
    SCROLL = auto()
    BUTTON_DOWN = auto()
    BUTTON_UP = auto()
    BUTTON_CLICK = auto()


class KeyboardActionType(ActionType):
    KEY_DOWN = auto()
    KEY_UP = auto()
    KEY_CLICK = auto()


ACTION_TYPES = list(map(str, MouseActionType.__iter__() + KeyboardActionType.__iter__()))


class Action(Entity):

    type_ = StringType(required=True, choices=ACTION_TYPES)
    timestamp = IntType(required=True)
    kwargs = DictType(field=StringType())

    def __sub__(self, other):
        if not self.type_ == other.type_:
            raise Exception('cannot create delta of different action types')
        pass
