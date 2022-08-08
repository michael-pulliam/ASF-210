from collections import Counter




ct = Counter() # Creates an empty counter object

ct.update('abca') # Populates the object

print(ct) # Counter({'a': 2, 'b': 1, 'c': 1})

ct.update({'a':3})

print(ct) # Counter({'a': 5, 'b': 1, 'c': 1})


for item in ct:
        print('%s : %d' % (item, ct[item]))
        
ct.update({'a': -3, 'b': -2, 'd': 3, "e": 2}) # perform an update

print(sorted(ct.elements())) # Returns a sorted list from the iterator 
# ** ['a', 'a', 'c', 'd', 'd', 'd', 'e', 'e']

ct.most_common()

ct.subtract({'a':2})

print(ct) # Counter({'d': 3, 'e': 2, 'c': 1, 'a': 0, 'b': -1})
