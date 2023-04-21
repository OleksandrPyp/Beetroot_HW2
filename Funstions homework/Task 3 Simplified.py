def make_operation_1 (operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0]-sum(args[1:])
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
        return result
    else:
        print("Wrong input")


print(make_operation_1("*",2,7,5))