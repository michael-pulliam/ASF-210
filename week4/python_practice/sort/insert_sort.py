"""Insertion sort algorithm works by maintaining a sorted sublist in the lower positions of the list.  
As a new item is found, it is inserted into the sorted sublist in the correct position. 
The sorted sublist grows by one with each new item as the “unsorted” sublist shrinks by one.
The time complexity of Insertion sort remains the same as bubble and selection sort at O(n^2)
    """

# def insertion_sort(a_list):
#     passCount = 1
#     for index in range(1, len(a_list)):
#         current_value = a_list[index]
#         position = index

#         while position > 0 and a_list[position - 1] > current_value:
#             a_list[position] = a_list[position - 1]
#             position = position - 1

#         a_list[position] = current_value

#         print(passCount,"- ",a_list)
#         passCount += 1
        
def insertionSort(list):
    for i in range(1, len(list)):
        anchor = list[i]
        j = i - 1
        while j >=0 and anchor < list[j]:
            list[j+1] = list[j]
            j = j -1 
            list[j+1] = anchor



myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
insertionSort(myList)
print()
print("Sorted Listed: ")
print(myList)