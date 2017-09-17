import time

from hades.input_listener import input_listeners


def setup():
    input_listeners.start()
    time.sleep(5)
    input_listeners.stop()


def teardown():
    pass


if __name__ == '__main__':
    setup()
    teardown()
