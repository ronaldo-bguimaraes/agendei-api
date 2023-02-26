class ServiceException(Exception):
    pass


def service_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise ServiceException(e)

    return wrapper
