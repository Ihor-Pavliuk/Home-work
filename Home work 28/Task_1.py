# A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list and the second pass moves "down."
# This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate. Жодного уявлення для чого це пригодиться. 

def bubble_sort(data):
    n = len(data)
    start = 0
    end = n - 1
    iteration = True
    while iteration:
        iteration = False
        for i in range(start, end):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                iteration = True
        if not iteration:
            break
        end -= 1
        iteration = False
        for i in range(end, start, -1):
            if data[i] < data[i - 1]: 
                temp = data[i] 
                data[i] = data[i - 1]
                data[i - 1] = temp
                iteration = True
        if not iteration:
            break
        start += 1
    return data

x = [6, 1, 7, 3, 3, 3, 4, 2, 5, 2, 9] 
y = [1, 2, 3, 9, 9, 8, 7, 11, 12, 13 ]
print (bubble_sort(x))           
print (bubble_sort(y)) 