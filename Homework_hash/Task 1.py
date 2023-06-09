#Task 1 Binary search with recursion
def binary_search_rec(array, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return binary_search_rec(array, target, mid + 1, high)
        else:
            return binary_search_rec(array, target, low, mid - 1)

    return False



