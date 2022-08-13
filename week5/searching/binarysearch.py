import time
# def binary_search(ordered_list, term): 

#     size_of_list = len(ordered_list) - 1 

#     index_of_first_element = 0 
#     index_of_last_element = size_of_list 

#     while index_of_first_element <= index_of_last_element: 
#         mid_point = (index_of_first_element + index_of_last_element)/2 

#         if ordered_list[mid_point] == term: 
#             return mid_point 

#         if term > ordered_list[mid_point]: 
#             index_of_first_element = mid_point + 1 
#         else: 
#             index_of_last_element = mid_point - 1 

#     if index_of_first_element > index_of_last_element: 
#         return None

# Sequential (Linear) Search on Ordered List  0(n)
def linear_search(list, term):
	list_size = len(list)
	for i in range(list_size):
		if term == list[i]:
			return True
		elif list[i] > term:
			return False
	return False

num_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

word_list = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
# start = time.time()
print(linear_search(num_list, 31))
# end = time.time()
# print(f"Execution time: {end-start}")
print(linear_search(num_list, 77))
print(linear_search(word_list, "Delta"))
