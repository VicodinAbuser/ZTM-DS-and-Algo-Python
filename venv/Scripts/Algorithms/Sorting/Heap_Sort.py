#Heap Sort as the name suggests, uses the heap data structure.
#First the array is converted into a binary heap. Then the first element which is the maximum elemet in case of a max-heap,
#is swapped with the last element so that the maximum element goes to the end of the array as it should be in a sorted array.
#Then the heap size is reduced by 1 and max-heapify function is called on the root.
#Time complexity is O(nlog N) in all cases and space complexity = O(1)

count = 0
def max_heapify(array, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    global count
    if left < heap_size:
        count += 1
        if array[left] > array[largest]:
            largest = left
    if right < heap_size:
        count += 1
        if array[right] > array[largest]:
            largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heap_size, largest)

def build_heap(array):
    heap_size = len(array)
    for i in range ((heap_size//2),-1,-1):
        max_heapify(array,heap_size, i)

def heap_sort(array):
    heap_size = len(array)
    build_heap(array)
    print (f'Heap : {array}')
    for i in range(heap_size-1,0,-1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, heap_size, 0)

array = [5,9,3,10,45,2,0]
heap_sort(array)
print (array)
print(f'Number of comparisons = {count}')
'''
Heap : [45, 10, 3, 5, 9, 2, 0]
[0, 2, 3, 5, 9, 10, 45]
Number of comparisons = 22
'''

sorted_array = [5,6,7,8,9]
heap_sort(sorted_array)
print(sorted_array)
print(f'Number of comparisons = {count}')
'''
Heap : [9, 8, 7, 5, 6]
[5, 6, 7, 8, 9]
Number of comparisons = 12
'''

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
heap_sort(reverse_sorted_array)
print(reverse_sorted_array)
print(f'Number of comparisons = {count}')
'''
Heap : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Number of comparisons = 105
'''