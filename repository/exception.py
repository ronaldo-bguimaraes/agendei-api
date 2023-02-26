class RepositoryException(Exception):
    pass


def repository_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise RepositoryException(e)

    return wrapper
