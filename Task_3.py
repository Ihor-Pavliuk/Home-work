#Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's 
# possible):

#methods:

#to_int

#to_str

#to_bool

#to_float

#Don't forget to use @wraps
from functools import wraps
class TypeDecorators:
    def __init__(self):
        pass

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(agrs):
            try:
                return int(func(agrs))
            except ValueError:
                raise ValueError("Cann't convert it")
        return wrapper
    
    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(agrs):
            try:
                return str(func(agrs))
            except ValueError:
                raise ValueError("Cann't convert it")
        return wrapper
    
    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(agrs):
            if agrs.lower() == "true":
                return True
            elif agrs.lower() == "false":
                return False
            else:
                raise ValueError("Cann't convert it")
        return wrapper
    
    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(agrs):
            try:
                return float(func(agrs))
            except ValueError:
                raise ValueError("Cann't convert it")
        return wrapper
 

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25

assert do_something('True') is True
