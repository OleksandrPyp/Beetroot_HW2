#Task 1 Detecting local variables in a function
def no_local():
    pass


def have_local():
    a = 1
    b = 12.1
    c = "I am a test string"

print("Number of local variables in a function:", no_local.__code__.co_nlocals)
print("Number of local variables in a function:", have_local.__code__.co_nlocals)
