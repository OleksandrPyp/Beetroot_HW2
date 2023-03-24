#Task 3 a simple calculator
import time
def make_operation ():
    operator = input('''
    Please select the operation you would like to complete:
    + - addition
    - - subtractiom
    * - multiplication
    ''')
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    if operator == "+":
        print(f"{x} + {y} is equal to .... ")
        time.sleep(1.5)
        return x + y
    elif operator == "-":
        print(f"{x} - {y} is equal to .... ")
        time.sleep(1.5)
        return x - y
    elif operator == "*":
        print(f"{x} * {y} is equal to .... ")
        time.sleep(1.5)
        return x * y
    else:
        print("Wrong operator, brother")

print(make_operation())