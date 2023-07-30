#Task 3 Insertion and Quicksort
#we are going to use the "limit" variable in order to switch between different types of sorting
#This approach going to save us time on a smaller lists i.e if the lenght of list is smaller or equal to the limit
#we will utilize the insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def quick_sort(array, limit):
    if len(array) <= limit:
        insertion_sort(array)
    else:
        if len(array) > 1:
            pivot = array[len(array) // 2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]

            quick_sort(left, limit)
            quick_sort(right, limit)

            array[:] = left + middle + right

