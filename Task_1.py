def logger(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with args:{args}")
    return wrapper

@logger
def add(a, b):
    return a + b
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3, 4, 5)