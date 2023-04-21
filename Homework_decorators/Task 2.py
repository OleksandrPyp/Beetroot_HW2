#Task 2 Stop words decorator
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
from functools import wraps
from typing import Callable
def stop_words(words: list):
    def inner_func(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for w in words:
                result = result.replace(w, "*")
            return result
        return wrapper
    return inner_func

@stop_words(['pepsi', 'BMW'])
def create_slogan(name = "Oleks"):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan())

