def stop_words(words: list):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            for i in words:
                result = result.replace(i, '*')
            return result
        return wrapper
    return decorator
@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
     
        

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Toy"))