#Task 1 Bubble sort (bidirectional)
def bidirectional_bubble_sort(array):
    n = len(array)
    is_sorted = False
    start = 0
    end = n - 1

    while not is_sorted:
        is_sorted = True
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        is_sorted = True
        end -= 1

        for i in range(end - 1, start - 1, 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        start += 1

