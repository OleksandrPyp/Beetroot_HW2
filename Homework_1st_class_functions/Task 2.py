#Task 2 Function to access another function
def test_func(x):
    if x%2 == 0:
        return x**2
    else:
        return x

numbers_1 = list(range(1, 11))
func_call = list(map(test_func, numbers_1))
print(func_call)

#Second solution with the lambda cause I still need to understand how it works
numbers = list(range(1, 11))
result = map(lambda x: x**2, numbers)
print(list(result))

