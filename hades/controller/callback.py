from time import time

from hades.controller.base import Controller
from hades.entity.event import EventType, Event
from hades.lib import get_logger

logger = get_logger(__name__)


class Callback(object):

    event_type = EventType.NO_OP

    def __init__(self, controller: Controller, handler):
        self.controller = controller
        self.handler = handler

    def __call__(self, *args, **kwargs):
        event = Event(type_=self.event_type, timestamp=int(time()), args=args)
        self.controller.register_event(event)


class OnMove(Callback):
    event_type = EventType.MOUSE_MOVE


class OnClick(Callback):
    event_type = EventType.MOUSE_CLICK


class OnScroll(Callback):
    event_type = EventType.MOUSE_SCROLL


class OnPress(Callback):
    event_type = EventType.KEY_PRESS


class OnRelease(Callback):
    event_type = EventType.KEY_RELEASE
