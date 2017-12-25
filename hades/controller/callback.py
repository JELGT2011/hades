from time import time

from hades.controller.base import Controller
from hades.entity.event import Event, MouseEventType, KeyboardEventType
from hades.lib import get_logger

logger = get_logger(__name__)


PRESSED_MAPPING = {
    True: 'down',
    False: 'up',
}


class Callback(object):

    event_type = None

    def __init__(self, controller: Controller):
        self.controller = controller

    def __call__(self, *args):
        logger.info('{} called with args {}'.format(self.event_type.name, args))
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnMove(Callback):
    event_type = MouseEventType.MOVE

    def __call__(self, *args):
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnClick(Callback):
    event_type = MouseEventType.CLICK

    def __call__(self, x, y, button, pressed):
        super().__call__(x, y, button, pressed)
        method_name = '{}_{}'.format(button.name, PRESSED_MAPPING[pressed])
        trigger = getattr(self.controller.mouse_state_machine, method_name)
        trigger()


class OnScroll(Callback):
    event_type = MouseEventType.SCROLL


class OnPress(Callback):
    event_type = KeyboardEventType.PRESS


class OnRelease(Callback):
    event_type = KeyboardEventType.RELEASE
