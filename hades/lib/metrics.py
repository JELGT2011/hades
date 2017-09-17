import functools


def instrument_wrapper(logger):

    def wrapper_factory(func):

        name_ = func.__name__

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info('{} being'.format(name_))
            func(*args, **kwargs)
            logger.info('{} end'.format(name_))

        return wrapper

    return wrapper_factory
