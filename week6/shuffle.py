import random

shuffled_list = []
# def shuffle(list):
#     random.shuffle(list)
#     # random.sample(list, len(list))
    
    
    
num_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
# print(num_list)
# shuffle(num_list)
# print(num_list)

def shuffle(list):
    temp = list.copy()
    if len(list) > 0:
        elem = temp.pop(random.randint(0, len(temp)-1))
        shuffled_list.append(elem)
        return shuffle(temp)
    else:
        print(shuffled_list)
        shuffled_list.clear()

print('Before Shuffle: ')
print(f'{num_list}')

print('Shuffled: ')
shuffle(num_list)
shuffle(num_list)
shuffle(num_list)
