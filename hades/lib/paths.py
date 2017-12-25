from os import path

APPLICATION_ID = 'hades'

PROJECT_DIR = path.realpath(path.join(__file__, path.sep.join(['..'] * 3)))
SOURCE_DIR = path.join(PROJECT_DIR, APPLICATION_ID)
DATA_DIR = path.join(PROJECT_DIR, 'data')
SCREENSHOT_DIR = path.join(DATA_DIR, 'screenshots')
