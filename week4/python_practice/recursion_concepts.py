# The factorial function says to multiply all whole numbers from a chosen number down to 1.
# if n = 3, then we have 3 * 2 * 1 = 6
# If n = 5, then we have 5 * 4 * 3 * 2 * 1 = 120
# If n = 8, then we have 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320

# Three Parts of a Recursive Algorithm
    # 1. Must have a base case – base case stops the recursion
    # 2. Must move towards the base case by changing the state
    # 3. Recursively call itself

# ------------------------------------------------------------------------------------------------------------------------------------
# Iterative loop factorial function and Recursion
# ------------------------------------------------------------------------------------------------------------------------------------

# Example 1

def factorialLoop(x):
    retVal = x
    for i in reversed(range(1,x)):
        retVal *= i
    return retVal

# Recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

n = 5
print(factorialLoop(n)) 
print(factorial(n))

# Example 2

def countDown():
    for i in range(10,0,-1):
        print(i)
    print("Blast Off!!!!")

# Recursion

def blastOff(x):
    if x == 0:
        print('Blast Off!!')
    else:
        print(x)
        blastOff(x-1)
     
n = 5   
countDown()
print(blastOff(n))
# -------------------------------------------------------------------------------------------------------------------------------------

# Example 3

# Iterative Function

def loopSum(n):
    sum = 0
    for x in range (1, n+1):
        sum += x
    return sum
n = 7
print(loopSum(n))

# # Recursive Function

def recSum(n):
    if n <= 1:
        return n
    return n + recSum(n-1)
n = 7
print(recSum(n))




# ------------------------------------------------------------------------------------------------------------------------------------
#  recursive factorial algorithm
# ------------------------------------------------------------------------------------------------------------------------------------



def factorial(n):
        #test for a base case
    if n==0:
        return 1
        # make a calculation and a recursive call
    f= n*factorial(n-1)
    
    print(f)
    return(f)
factorial(4)




# ------------------------------------------------------------------------------------------------------------------------------------
# Back Tracking
# ------------------------------------------------------------------------------------------------------------------------------------


def bitStr(n, s):            

    if n == 1: return s 
    return [ digit + bits for digit in bitStr(1,s)for bits in bitStr(n - 1,s)] 

print (bitStr(3,'abc'))