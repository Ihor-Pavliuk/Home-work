#One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the "partition limit"). 
# Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. 
# Perform analysis using different list sizes for the partition limit.

#Why does this make sense? Комбінується швидкість quick sort для великих масивів та ефективність insertiom sort для коротких списків
import random

def quick_sort(array):
    partition_limit = 10
    if len(array) <= 1:
        return array
    if len(array) > partition_limit:
        pivot = array[-1]
        left = [x for x in array[:-1] if x <= pivot]
        right = [x for x in array[:-1] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        for index in range(1, len(array)):
            current_value = array[index]
            position = index
            while position > 0 and array[position - 1] > current_value:
                array[position] = array[position - 1]
                position = position - 1
            array[position] = current_value
        return array
x = [random.randint(1, 100000) for _ in range(1000000)]
print(quick_sort(x))
