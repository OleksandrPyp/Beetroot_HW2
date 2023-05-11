#Task 3 Type Decorators
from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                raise ValueError(f"Can't convert {result} to int")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except (ValueError, TypeError):
                raise ValueError(f"Can't convert {result} to str")
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            possible_trues = ["true", "yes", "1"]
            possible_falses = ["false", "no", "0"]
            if isinstance(result, bool):
                return result
            if isinstance(result, str):
                if result.lower() in possible_trues:
                    return True
                elif result.lower() in possible_falses:
                    return False
            raise ValueError(f"Can't convert {result} to str")
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                raise ValueError(f"Can't convert {result} to float")
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


