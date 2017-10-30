import functools


def instrument_wrapper(logger):

    def wrapper_factory(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info('{} begin'.format(func.__name__))
            func(*args, **kwargs)
            logger.info('{} end'.format(func.__name__))

        return wrapper

    return wrapper_factory
