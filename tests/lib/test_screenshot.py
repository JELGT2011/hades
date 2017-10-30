from lib import capture_screen_wrapper


def test_capture_screen_wrapper():

    @capture_screen_wrapper
    def func(*args, **kwargs):
        pass

    input_event = func()
