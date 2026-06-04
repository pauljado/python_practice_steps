
def merge_sort(array):

    length: int = len(array)

    if length <= 1:
        return
    
    middle: int = length // 2
    left_array: list[int] = []
    right_array: list[int] = []

    i: int = 0
    j: int = 0

    for i in range(length):
        if i < middle:
            left_array.append(array[i])
        else:
            right_array.append(array[i])
            j += 1

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)


    return

def merge(left_array, right_array, array):

    left_size = len(array) // 2
    right_size = len(array) - left_size
    i = 0
    l = 0
    r = 0

    while l < left_size and r < right_size:
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1

    
    while l < left_size:
        array[i] = left_array[l]
        i += 1
        l += 1

    while r < right_size:
        array[i] = right_array[r]
        i += 1
        r += 1

    return


array = [5, 2, 4, 6, 7, 3, 1, 8, 9]

merge_sort(array)
print(array)