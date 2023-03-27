#Task3 The math quiz program
import random

variable1 = random.randint(0,100)
variable2 = random.randint(0,100)
totals = int(variable2) + int(variable1)
print(f"Variable 1 is equal to {variable1} and Variable 2 is equal to {variable2}")
answer = int(input("What is the sum of variables? Please enter the number "))

if answer == totals:
    print("You are right! Congrats")
elif answer != totals:
    print("Nope,try again:)")
else:
    print("That is not an option")

