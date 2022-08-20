import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
# myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

# print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList)   

print(f"The execution time is: {end_time-start_time}")

# -- LAST ELEMENT AS PIVOT --
import sys
x=1500
sys.setrecursionlimit(x)

def last_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Last Elem Pivot):')

start_time = time.time()
last_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

# -- RANDOM ELEMENT AS PIVOT --
def random_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop(random.randint(0, len(sequence)-1))

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Random Elem Pivot):')

start_time = time.time()
random_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

# -- MEAN AS PIVOT --
def mean_sort(sequence):
    start = sequence[0]
    middle = sequence[int(len(sequence) / 2)]
    end = sequence[int(len(sequence) - 1)]

    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop(sequence.index(int((start + middle + end) / 3)))

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Mean Pivot):')

start_time = time.time()
mean_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")
















# def partition(unsorted_array, first_index, last_index): 

#     if first_index == last_index: 
#         return first_index 
#     else: 
#         nearest_median = median_of_medians(unsorted_array[first_index:last_index]) 

#     index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median) 

#     swap(unsorted_array, first_index, index_of_nearest_median) 

#     pivot = unsorted_array[first_index] 
#     pivot_index = first_index 
#     index_of_last_element = last_index 

#     less_than_pivot_index = index_of_last_element 
#     greater_than_pivot_index = first_index + 1
    
# def median_of_medians(elems): 

#     sublists = [elems[j:j+5] for j in range(0, len(elems), 5)] 

#     medians = [] 
#     for sublist in sublists: 
#         medians.append(sorted(sublist)[len(sublist)/2]) 

#     if len(medians) <= 5: 
#         return sorted(medians)[len(medians)/2] 
#     else: 
#         return median_of_medians(medians) 
    
# def get_index_of_nearest_median(array_list, first, second, median): 
#     if first == second: 
#         return first 
#     else: 
#         return first + array_list[first:second].index(median) 
    
# def swap(array_list, first, second): 
#     temp = array_list[first] 
#     array_list[first] = array_list[second] 
#     array_list[second] = temp
    
# def deterministic_select(array_list, left, right, k): 

#     split = partition(array_list, left, right) 
#     if split == k: 
#         return array_list[split] 
#     elif split < k : 
#         return deterministic_select(array_list, split + 1, right, k) 
#     else: 
#         return deterministic_select(array_list, left, split-1, k) 