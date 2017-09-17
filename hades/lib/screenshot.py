import functools
import os
import tkinter

import pyscreenshot
import time

from hades.entity.action import Action
from hades.lib import get_logger


SCREENSHOT_NAME_FORMAT = '{action}_{timestamp}.png'
SCREENSHOT_DIR = r'C:\Users\jelgt\Documents\hades\data'

tkinter_root = tkinter.Tk()
width = tkinter_root.winfo_screenwidth()
height = tkinter_root.winfo_screenheight()


logger = get_logger(__name__)


def capture_screen_wrapper(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
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

    return wrapper

