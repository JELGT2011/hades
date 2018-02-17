from schematics.types import StringType, IntType, FloatType

from hades.entity.base import Entity


class Action(Entity):

    timestamp = IntType(required=True)

    def __add__(self, other):
        assert isinstance(other, self.__class__), 'cannot apply delta to different action types'
        return self

    def __sub__(self, other):
        assert isinstance(other, self.__class__), 'cannot create delta of different action types'
        return self


class MouseAction(Action):

    x = FloatType(required=True)
    y = FloatType(required=True)
    button = StringType(required=False)


class ButtonMouseAction(MouseAction):

    def __add__(self, other):
        super().__add__(other)
        summation = self.__class__({
            'timestamp': other.timestamp,
            'x': self.x + other.x,
            'y': self.y + other.y,
        })
        return summation

    def __sub__(self, other):
        super().__sub__(other)
        difference = self.__class__({
            'timestamp': self.timestamp - other.timestamp,
            'x': self.x - other.x,
            'y': self.y - other.y,
        })
        return difference


class ButtonDownMouseAction(MouseAction):
    pass


class ButtonUpMouseAction(MouseAction):
    pass


class KeyboardAction(Action):

    key = StringType(required=True)


class KeyDownKeyboardAction(KeyboardAction):
    pass


class KeyUpKeyboardAction(KeyboardAction):
    pass
