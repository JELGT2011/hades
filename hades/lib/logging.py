import logging

import sys

FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger_formatter = logging.Formatter(FORMATTER)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logger_formatter)
    logger.addHandler(handler)
    return logger
