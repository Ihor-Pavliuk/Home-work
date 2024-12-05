#Implement the mergeSort function without using the slice operator.

def merge_sort(array):
    if len(array) > 1:
        start = 0
        end = len(array)
        stop = len(array) // 2
        left_half = []
        right_half = []
        while (start < stop):
            left_half.append(array[start])
            start += 1

        while (stop < end ):
            right_half.append(array[stop])
            stop += 1

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1
    return array

x = [6, 1, 7, 3, 3, 3, 4, 2, 5, 2] 
y = [1, 2, 3, 9, 9, 8, 7, 11, 12, 13 ]
print (merge_sort(x))           
#print (merge_sort(y)) 
