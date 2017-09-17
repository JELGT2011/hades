import functools
import os
import time
import tkinter

import pynput
import pyscreenshot

from hades.entity.action import Action
from hades.lib.logging import get_logger

logger = get_logger(__name__)

SCREENSHOT_NAME_FORMAT = '{action}_{timestamp}.png'
SCREENSHOT_DIR = r'C:\Users\jelgt\Documents\hades\data'

tkinter_root = tkinter.Tk()
width = tkinter_root.winfo_screenwidth()
height = tkinter_root.winfo_screenheight()


def capture_screen(func):

    @functools.wraps(func)
    def __wrapper(*args, **kwargs):
        logger.info('capturing screen from {}'.format(func.__name__))
        # bounding_box = (0, 0, width, height)
        screenshot = pyscreenshot.grab()
        epoch_time = int(time.time())
        screenshot_name = SCREENSHOT_NAME_FORMAT.format(
            action=func.__name__,
            timestamp=epoch_time,
        )
        screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
        screenshot.save(screenshot_path)

        input_event = func(*args, **kwargs)
        action = Action(input_event=input_event, screenshot=screenshot)
        return input_event

    return __wrapper


def no_op_callback(*args, **kwargs):
    return no_op_callback.__name__


class InputListeners(object):

    def __init__(self):
        from hades.input_listener.keyboard import on_keyboard_press
        from hades.input_listener.keyboard import on_keyboard_release
        from hades.input_listener.mouse import on_mouse_click
        from hades.input_listener.mouse import on_mouse_scroll
        self.mouse_listener = pynput.mouse.Listener(
            on_move=no_op_callback,
            on_click=on_mouse_click,
            on_scroll=on_mouse_scroll,
        )
        self.keyboard_listener = pynput.keyboard.Listener(
            on_press=on_keyboard_press,
            on_release=on_keyboard_release,
        )
        self.listeners = [
            self.mouse_listener,
            self.keyboard_listener,
        ]

    def start(self):
        logger.info('{}.{}'.format(self.__class__.__name__, self.start.__name__))
        for listener in self.listeners:
            listener.start()
            listener.wait()

    def stop(self):
        logger.info('{}.{}'.format(self.__class__.__name__, self.stop.__name__))
        for listener in self.listeners:
            listener.stop()


input_listeners = InputListeners()
