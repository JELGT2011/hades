from abc import abstractmethod, ABC
from time import time
from typing import Callable

from transitions import Machine

from hades.controller.base import Controller
from hades.entity.event import Event, MouseEventType, KeyboardEventType
from hades.lib import get_logger

logger = get_logger(__name__)


MOUSE_PRESS_MAPPING = {
    True: 'down',
    False: 'up',
}

KEY_PRESS_MAPPING = {
    True: 'modifier',
    False: 'standard',
}

MODIFIER_KEYS = frozenset({
    # TODO: find windows and linux super key codes
    'cmd',
    'alt',
    'ctrl',
    'shift',
    'caps_lock',
})


class Callback(ABC):

    event_type = None

    def __init__(self, controller: Controller, machine: Machine):
        self.controller = controller
        self.machine = machine

    def __call__(self, *args):
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        trigger = self.get_trigger()
        trigger(*args)
        self.controller.register_event(event)

    @abstractmethod
    def get_method(self, *args: tuple) -> str:
        pass

    def get_trigger(self) -> Callable:
        return getattr(self.machine, self.get_method())


class OnMove(Callback):
    event_type = MouseEventType.MOVE

    def get_method(self, x, y) -> str:
        return 'move'


class OnScroll(Callback):
    event_type = MouseEventType.SCROLL

    def get_method(self, x, y, dx, dy) -> str:
        return 'scroll'


class OnClick(Callback):

    event_type = MouseEventType.CLICK

    def get_method(self, x, y, button, pressed) -> str:
        return '{}_{}'.format(button.name, MOUSE_PRESS_MAPPING[pressed])


class OnPress(Callback):
    event_type = KeyboardEventType.PRESS

    def get_method(self, key) -> str:
        return '{}_down'.format(KEY_PRESS_MAPPING[key.name in MODIFIER_KEYS])


class OnRelease(Callback):
    event_type = KeyboardEventType.RELEASE

    def get_method(self, key) -> str:
        return '{}_up'.format(KEY_PRESS_MAPPING[key.name in MODIFIER_KEYS])
