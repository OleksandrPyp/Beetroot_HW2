#Task4 The name check

my_name = "oleks"
user_input = input("Please enter your name: ")
if user_input.casefold() == my_name.casefold():
    print(my_name)
    print(True)

