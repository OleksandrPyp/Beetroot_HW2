#Task 1 Decorator to print a function
def logger(func):
    def wrapper_logger(*args):
        result = print(f"Function {func.__name__}, called with following parameters: {args}")
        return result
    return wrapper_logger

@logger
def add(x:int,y:int):
    return x + y
@logger
def square_all(*args):
    return [arg**2 for arg in args]

add(3,4)
square_all(2,4)


