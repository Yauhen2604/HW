def debug(func):
    def wrapper(a, b):
        print(func.__name__, a, b)
        print(func(2, 4))

    return wrapper


@debug
def my_func(a, b):
    return a + b


my_func(2, 4)

