import time

from hades.service.input_listener import input_listener_service


def setup():
    input_listener_service.start()
    time.sleep(5)
    input_listener_service.stop()


def teardown():
    pass


if __name__ == '__main__':
    setup()
    teardown()
