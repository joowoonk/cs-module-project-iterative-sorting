def linear_search(arr, target):
    for i in (range(len(arr))):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        #first using first digit division
        middle = (first + last)//2

        if arr[middle] == target:
            return middle

        else:
            if target < arr[middle]:
                last = middle -1
            else:
                first = middle + 1


    return -1  # not found
