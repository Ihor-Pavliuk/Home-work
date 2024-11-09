#Write a decorator 'arg_rules' that validates arguments passed to the function.

#A decorator should take 3 arguments:

#max_length: 15
#type_: str
#contains: []  - list of symbols that an argument should contain

#If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(args): # тут виникла цікава помилка, якщо написати *args тоді всі аргументи будуть кортежом, і завжди не будуть проходити перевірку. 
            if not isinstance (args, type_):
                print(f"Type is not {type_}, please check it")
                return False
            if len(args) > max_length:
                print(f"Max length is bigger than {max_length}")
                return False
            if contains:
                for i in contains:
                    if i not in args:
                        print(f'Contains mast have {contains}')
                        return False
            return func(args)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"

