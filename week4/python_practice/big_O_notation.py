from random import random

# Big-O Notation - Simplification Rules
"""
- Change non-zero coefficients to 1
    - When n become extremely large, the constant values become insignificant
- Ignore low-order terms. High-order terms dominate the equation
    - 1 < logn < n < nlogn < n^2 < 2^n < n 
    """


# Big-O Notation - Logarithmic Complexity 
""" 
The complexity of this algorithm is logarithmic, O(log n), since the value of i in the while loop grows(increments),
 the number of iterations is less than n. 
 """
 
def printAFew(input):
    i = 1
    while i < len(input):
        print(input[i])
        i *= 2
        
printAFew([random.randint(0, 1000) for i in range(1, 1000001)])


# Big-O Notiation - Quadratice Complexity
"""
The complexity of this algorithm is quadratic, O(n to the 2nd power). 
 For each iteration of the outer loop, the nested inner loop iteraties n times. 
 The total number of iterations performed is n*n.
 """


def example(n):
    for i in range(n):
        for j in range(n):
            print(i * j)

example(5)


#Example

n = 10
sum = 0 

for i in range(1, n+1):
    sum += i
print(i)