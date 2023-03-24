def make_operation_1 (operator, x, y, *args):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    else:
        print("Wrong input")


print(make_operation_1("+",10,30))