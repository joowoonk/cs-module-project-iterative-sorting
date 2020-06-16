def insertion_sort(arr):
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        current_item = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        prev_indx = i-1
        while prev_indx >=0 and current_item < arr[prev_indx] : 
                arr[prev_indx+1] = arr[prev_indx] 
                prev_indx -= 1
        arr[prev_indx+1] = current_item 

# insertion_sort([4,2,10,6,1])

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for item in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[item]:
                smallest_index = item
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]        

    return arr
# [3, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    current_index = len(arr)
    for index in range(current_index-1):
        for compare in range(0,current_index-index-1):
            if arr[compare] > arr[compare+1] :
                arr[compare], arr[compare+1] = arr[compare+1], arr[compare]
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
