#Task1 String manipulation

import random

Trial_str = input("Please enter the string: ")
task_str = ""

task_str += (Trial_str[0:2] + Trial_str[-2:])
if len(Trial_str) < 2:
    print("Empty String")
else:
    print(task_str)

#Task2 The valid phone number program.

phone_num = input("Please enter the phone number: ")
if len(phone_num) == 10 and phone_num.isnumeric():
    print("This is a phone number")
else:
    print("Phone number could only be 10 digits and consist of numbers")

#Task3 The math quiz program

variable1 = random.randint(0,100)
variable2 = random.randint(0,100)
Totals = int(variable2) + int(variable1)
print(f"Variable 1 is equal to {variable1} and Variable 2 is equal to {variable2}")
while True:
    try:
        answer = int(input("What is the sum of variables? Please enter the number "))
        break
    except:
        print("That is not an option")
        int(input("What is the sum of variables? Please enter the number "))
if answer == Totals:
    print("You are right! Congrats")
elif answer != Totals:
    print("Nope,try again:)")
    int(input("What is the sum of variables? Please enter the number "))
else:
    print("That is not an option")

#Task4 The name check

my_name = "oleks"
user_input = input("Please enter your name: ")
if user_input.casefold() == my_name.casefold():
    print(my_name)
    print(True)