import random
#Task 1.1 не запускати, бо майже infinity loop, з меньшими цифрами працює)
a = 1000000000
b = 9999999999
some_random = random.randint(a, b)
while some_random != b:
    some_random = random.randint(a, b)
    if some_random  == b:
        print(some_random)
        break

#Task 1.2 # Ось відповідь на першу задачу
a = 1000000000
b = 9999999999
count = 0
some_random_list = list()
while count < 10:
    some_random = random.randint(a, b)
    some_random_list.append(some_random)
    count += 1
    if count == 10:
        print (max(some_random_list)) 

#Task 2
c = 1
d = 10
count = 0
some_random_set1 = set() #множини
some_random_set2 = set()
while count < 10:
    some_random = random.randint(c, d)
    some_random_set1.add(some_random)
    some_random2 = random.randint(c, d)
    some_random_set2.add(some_random2)
    count += 1
    if count == 10:
        print(some_random_set1)
        print(some_random_set2)
        some_random_set3 = some_random_set1 | some_random_set2 #для себе запишу що поєднати ще можна так: some_random_set3 = some_random_set2.union(some_random_set1)
        print(some_random_set3)

#Task 3 # дуже довго довбався, але з першого відео уроку 7, відразу все зрозумів 
some_list10 = list()
to_remove = list()
i = 0
while i < 100:
    i += 1
    some_list10.append(i)
for i in some_list10:
    if i % 7 == 0 and not i % 5 == 0: # тут була проблема тому що використовув // замість %, і ще використовув set замість list
        some_list10.remove(i)
print(some_list10)