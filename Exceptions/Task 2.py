#Task 2
def square_func():
    a = int(input("Please enter the number you want to have squared: "))
    b = int(input("Please enter the number you use as a divider: "))
    c = a ** 2 / b
    print(c)

while True:
    try:
        square_func()
    except ZeroDivisionError:
        print("Division by zero!")
    except ValueError:
        print("Please input the number! ")

print(square_func())

