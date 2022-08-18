import time

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

num_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]	

    
word_list = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
start = time.time()
print(binary_search(num_list, 31))
end = time.time()
print(f"Execution time: {end-start}")
print(binary_search(num_list, 77))
print(binary_search(word_list, "Delta")) 










