import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


""" The algorithm sacrifices space complexity for time, as if the uses memory to store the results to the function calls. """

def dyna_fib(n, lookup):
    if n <= 2:
        lookup[n] = 1
    
    if lookup is None:
        lookup[n] = dyna_fib(n-1, lookup) + dyna_fib(n-2, lookup)
        
    return lookup[n]


nthTerm = 36

start_time = time.time()
print(fibonacci(nthTerm))
end_time = time.time()
print(f'The execution time is: {end_time-start_time}')

fibonacci_values = [None] * (10000)
start_time = time.time()
print(dyna_fib(nthTerm, fibonacci_values))
end_time = time.time()
print(f'The execution time is: {end_time-start_time}')
