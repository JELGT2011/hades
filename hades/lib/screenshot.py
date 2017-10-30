import os
import tkinter

import pyscreenshot

from hades.lib import SCREENSHOT_DIR, get_logger

SCREENSHOT_NAME_FORMAT = '{timestamp}.png'

tkinter_root = tkinter.Tk()
width = tkinter_root.winfo_screenwidth()
height = tkinter_root.winfo_screenheight()

logger = get_logger(__name__)


def capture_screen(timestamp):
    screenshot = pyscreenshot.grab(childprocess=False)
    screenshot_name = SCREENSHOT_NAME_FORMAT.format(timestamp=timestamp)
    screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot_name)
    screenshot.save(screenshot_path)
    return screenshot
