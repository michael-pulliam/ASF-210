
# def __len__(n):
#     return n * 2

def add(n):
    print(n + 2)
n = 5
x = 12
# add(n+x)

s1 = {'ab', 3, 4, (5,6)}
s2 = {'ab', 7, (7,6)}

# print(s1.difference(s2))
print(s1)
print(len(s1))

s1.symmetric_difference_update(s2)
# s1.update(s2)
# print(s2)
print(s1)

print(len(s1))

# s1.symmetric_difference_update(s2)
# print(s1)
