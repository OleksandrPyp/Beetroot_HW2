#Task 2 Fibbonacci search
def fibonacci_search(arr, target):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)
        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib == 1 and arr[offset + 1] == target:
        return offset + 1
    #else:
        #raise ValueError("Element is not in the range")

    return False


