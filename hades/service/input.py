from hades.entity.input_listener import keyboard_listener
from hades.entity.input_listener import mouse_listener
from hades.lib import get_logger
from hades.lib import instrument_wrapper
from hades.service.base import Service

logger = get_logger(__name__)


class InputService(Service):

    def __init__(self, input_listeners):
        super().__init__()
        self.input_listeners = input_listeners

    @instrument_wrapper(logger)
    def start(self):
        for input_listener in self.input_listeners:
            input_listener.start()
            input_listener.wait()

    @instrument_wrapper(logger)
    def stop(self):
        for input_listener in self.input_listeners:
            input_listener.stop()


input_service = InputService(
    input_listeners=[
        mouse_listener,
        keyboard_listener,
    ],
)
