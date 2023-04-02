#Task 1
def oops():
    raise IndexError


def solution_oops():
    try:
        oops()
    except IndexError:
        print("It was an error but we solved it")

print(solution_oops())

#if we substitute the IndexError with KeyError function is not going to work properly and going to return the KeyError




