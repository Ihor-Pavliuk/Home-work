#розділив приклади, тому що якщо запускати одночасно їх, виходить цікавий ефект)
import multiprocessing

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def square(n):
    return n * n

def cubic(n):
    return n * n * n

def calculate(function, numbers):
    with multiprocessing.Pool() as pool:
        return pool.map(function, numbers)

if __name__ == "__main__":
    numbers = range(1, 11)
    
    fib_results = calculate(fibonacci, numbers)
    fac_results = calculate(factorial, numbers)
    sq_results = calculate(square, numbers)
    cu_results = calculate(cubic, numbers)

    print("Fibonacci:", fib_results)
    print("Factorial:", fac_results)
    print("Squares:", sq_results)
    print("Cubics:", cu_results)
