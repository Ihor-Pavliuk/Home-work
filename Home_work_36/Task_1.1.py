# Practice asynchronous code

# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. 
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
# You need to get four lists of results from corresponding functions.

# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
# Time the execution of both realizations, explore the results, what realization is more effective, why did you get a result like this.

import asyncio

async def fibonacci(n):
    if n <= 1: return n
    else:
        return await fibonacci(n-1) + await fibonacci(n-2) 

async def factorial(n): 
    if n == 0: return 1 
    else: 
        return n * await factorial(n-1) 

async def square(n): 
    return n * n 

async def cubic(n): 
    return n * n * n 

async def main(): 
    numbers = range(1, 11) 
    fib_results = await asyncio.gather(*[fibonacci(n) for n in numbers]) 
    fac_results = await asyncio.gather(*[factorial(n) for n in numbers]) 
    sq_results = await asyncio.gather(*[square(n) for n in numbers]) 
    cu_results = await asyncio.gather(*[cubic(n) for n in numbers]) 
    return fib_results, fac_results, sq_results, cu_results
 
results = asyncio.run(main()) 

print("Fibonacci:", results[0]) 
print("Factorial:", results[1]) 
print("Squares:", results[2]) 
print("Cubics:", results[3])


