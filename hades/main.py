import time

from hades.service.input import input_service


def setup():
    input_service.start()


def teardown():
    input_service.stop()


if __name__ == '__main__':
    setup()
    time.sleep(5)
    teardown()
