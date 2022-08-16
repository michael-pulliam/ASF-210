def mergeSort(nlist):
    print("Splitting ",nlist)

    # insert your code to complete the mergeSort function
    list_size = len(nlist)
    mid_index = (list_size / 2)
    if len(nlist) > 1:
        left = nlist[:int(mid_index)]
        right = nlist[int(mid_index):]
        mergeSort(left)
        mergeSort(right)
        merge(nlist, left, right)
    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1
    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist


list = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
mergeSort(list)
# # Allow user to input list and target
# usr_lst = input('Provide an unordered list of numbers to sort: ')
# stringified_lst = usr_lst.strip('][').split(', ')
# parsed_lst = []

# # Parse list from user for search function
# def parse(list):
#     if len(list) > 0:
#         parsed_lst.append(int(list[0]))
#         list.pop(0)
#         return parse(list)
#     return
# parse(stringified_lst)
# mergeSort(parsed_lst)

