

# # Sequential (Linear) Search on Unordered List  o(n)
# def linear_search(list, term):
# 	list_size = len(list)
# 	for i in range(list_size):
# 		if term == list[i]:
# 			return True
# 	return False

# myList = [11, 30, 25, 27, 9, 19, 28, 3, 21, 17]

# print(linear_search(myList,4))   

# # Sequential (Linear) Search on Ordered List  0(n)
# def linear_search(list, term):
# 	list_size = len(list)
# 	for i in range(list_size):
# 		if term == list[i]:
# 			return True
# 		elif list[i] > term:
# 			return False
# 	return False

# myList = [11, 30, 25, 27, 9, 19, 28, 3, 21, 17]

# print(linear_search(myList,4))   

# # Sequential (Linear) Search on Unordered List  o(n)
# def search(unordered_list, term): 
#     unordered_list_size = len(unordered_list) 
#     for i in range(unordered_list_size): 
#         if term == unordered_list[i]: 
#             return i 

#     return None

# # Sequential (Linear) Search on Ordered List  0(n)
# def search(unordered_list, term): 
#     unordered_list_size = len(unordered_list) 
#     for i in range(unordered_list_size): 
#         if term == unordered_list[i]: 
#             return i 

#     return None


# BINARY SEARCH
def binary_search(ordered_list, term): 

    size_of_list = len(ordered_list) - 1 

    index_of_first_element = 0 
    index_of_last_element = size_of_list 

    while index_of_first_element <= index_of_last_element: 
        mid_point = (index_of_first_element + index_of_last_element)/2 

        if ordered_list[mid_point] == term: 
            return mid_point 

        if term > ordered_list[mid_point]: 
            index_of_first_element = mid_point + 1 
        else: 
            index_of_last_element = mid_point - 1 

    if index_of_first_element > index_of_last_element: 
        return None
    
# def binary_search(ordered_list, first_element_index, last_element_index, term): 

#     if (last_element_index < first_element_index): 
#         return None 
#     else: 
#         mid_point = first_element_index + ((last_element_index - first_element_index) / 2) 

#         if ordered_list[mid_point] > term: 
#             return binary_search(ordered_list, first_element_index, mid_point-1,term) 
#         elif ordered_list[mid_point] < term: 
#             return binary_search(ordered_list, mid_point+1, last_element_index, term) 
#         else: 
#             return mid_point 
        
store = [2, 4, 5, 12, 43, 54, 60, 77]
print(binary_search(store, 12))
# print(binary_search(store, 0, 7, 2))      