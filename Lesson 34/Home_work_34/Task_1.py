# A shared counter

# Make a class called Counter, and make it a subclass of the Thread class in the Threading module. 
# Make the class have two global variables, one called counter set to 0, and another called rounds set 
# to 100.000. Now implement the run() method, let it include a simple for-loop that iterates through rounds 
# (e.i. 100.000 times) and for each time increments the value of the counter by 1. 
# Create 2 instances of the thread and start them, then join them and check the result of the counter, 
# it should be 200.000, right? Run it a couple of times and consider some different reasons why you get 
# the answer that you get. 

import threading
from threading import Thread
COUNTER = 0
ROUNDS = 100000



class Counter(Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        global COUNTER
        for _ in range(ROUNDS):
            COUNTER += 1

        
new_thread_1 =Counter()
new_thread_2 =Counter()
new_thread_1.start()
new_thread_2.start()
new_thread_1.join()
new_thread_2.join()
print(new_thread_1)
print(new_thread_2)
print("Final value of COUNTER:", COUNTER)



