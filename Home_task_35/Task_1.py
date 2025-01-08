# Primes

# We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input 
# a number and returns a bool, whether it is prime or not.

# Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 

# Compare the results and performance of each of them.

import multiprocessing

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def process_worker(numbers, results, index):
    results[index] = [is_prime(number) for number in numbers]

def processpool_executor(numbers):
    processes = []
    manager = multiprocessing.Manager()
    results = manager.list([None] * len(numbers))
    
    for i in range(len(numbers)):
        process = multiprocessing.Process(target=process_worker, args=([numbers[i]], results, i))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    return results

if __name__ == "__main__":
    process_results = processpool_executor(NUMBERS)

    print("ProcessPoolExecutor Results:", process_results)

