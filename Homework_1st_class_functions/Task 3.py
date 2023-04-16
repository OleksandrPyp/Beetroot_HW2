#Task 3 The choosing function
def choose_func(nums:list, func_1, func_2):

    for n in nums:
        if n < 0:
            return func_2(nums)
    else:
        return func_1(nums)

nums_1 = [1, 2, 3, 4, 5]
nums_2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num**2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

print(choose_func(nums_1, square_nums, remove_negatives))
print(choose_func(nums_2, square_nums, remove_negatives))


