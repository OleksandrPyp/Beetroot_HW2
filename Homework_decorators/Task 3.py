#Task 3
from functools import wraps
max_length = 15
type_ = str
contains1 = type(list)

def arg_rules(type_: type, max_length: int, contains: list):
    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            item_in_contains = True
            for item in contains:
                if item not in args:
                    item_in_contains = False
                    break
            if item_in_contains == False:
                print("item does not meet the requirements")
                return False
            if len(res) > max_length:
                return False
            elif type(args) != type_:
                return False
            else:
                print("Error")
                return res
        return wrapper
    return inner_func

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("S@sh"))