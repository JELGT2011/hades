from time import time

from hades.controller.base import Controller
from hades.entity.event import EventType, Event, MouseEventType, KeyboardEventType
from hades.lib import get_logger

logger = get_logger(__name__)


class Callback(object):

    event_type = EventType.NO_OP

    def __init__(self, controller: Controller):
        self.controller = controller

    def __call__(self, *args, **kwargs):
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnMove(Callback):
    event_type = MouseEventType.MOVE


class OnClick(Callback):
    event_type = MouseEventType.CLICK

    def __call__(self, *args, **kwargs):
        logger.info('OnClick called with {}, {}'.format(args, kwargs))
        super().__call__(*args, **kwargs)


class OnScroll(Callback):
    event_type = MouseEventType.SCROLL


class OnPress(Callback):
    event_type = KeyboardEventType.PRESS


class OnRelease(Callback):
    event_type = KeyboardEventType.RELEASE
