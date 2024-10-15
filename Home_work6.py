import random
#Task 1
count = 0
some_random_list = list()
while count < 10:
    some_random = random.randint(a, b)
    some_random_list.append(some_random)
    count += 1
    if count == 10:
        print (max(some_random_list)) 

#Task 2
count = 0
some_random_set1 = set() #множини
some_random_set2 = set()
while count < 10:
    some_random = random.randint(0, 100)
    some_random_set1.add(some_random)
    some_random2 = random.randint(0, 100)
    some_random_set2.add(some_random2)
    count += 1
    if count == 10:
        print(some_random_set1)
        print(some_random_set2)
        some_random_set3 = some_random_set1 | some_random_set2 #для себе запишу що поєднати ще можна так: some_random_set3 = some_random_set2.union(some_random_set1)
        print(some_random_set3)


#Task 3 # дуже довго довбався, але з першого відео уроку 7, відразу все зрозумів 
some_list10 = list()
i = 0
while i < 100:
    i += 1
    if i % 7 == 0 and i % 5 != 0: # тут була проблема тому що використовув // замість %, і ще використовув set замість list
        some_list10.append(i)
    elif i % 7 == 0 and not i % 5 != 0:
        some_list10.append(i)
print(some_list10)
