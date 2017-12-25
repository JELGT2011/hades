from operator import methodcaller
from time import time

from pynput import mouse

from hades.controller.base import Controller
from hades.entity.event import EventType, Event, MouseEventType, KeyboardEventType
from hades.lib import get_logger

logger = get_logger(__name__)

BUTTON_MAPPING = {
    mouse.Button.left: None,
    mouse.Button.middle: None,
    mouse.Button.right: None,
}


class Callback(object):

    event_type = EventType.NO_OP

    def __init__(self, controller: Controller):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        logger.info('{} called with {}, {}'.format(self.event_type.name, args, kwargs))
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnMove(Callback):
    event_type = MouseEventType.MOVE

    def __call__(self, *args, **kwargs):
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnClick(Callback):
    event_type = MouseEventType.CLICK

    def __call__(self, x, y, button, pressed):
        event = Event(type_=self.event_type, timestamp=int(time()), args=(x, y, button, pressed))
        method = '{}_{}'.format(button.name, 'down' if pressed else 'up')
        machine = self.controller.mouse_state_machine
        methodcaller(machine, method)
        self.controller.register_event(event)


class OnScroll(Callback):
    event_type = MouseEventType.SCROLL


class OnPress(Callback):
    event_type = KeyboardEventType.PRESS


class OnRelease(Callback):
    event_type = KeyboardEventType.RELEASE
