from hades.controller.input import input_controller
from hades.lib import get_logger

logger = get_logger(__name__)


if __name__ == '__main__':
    input_controller.start()
    while input_controller.running:
        pass
