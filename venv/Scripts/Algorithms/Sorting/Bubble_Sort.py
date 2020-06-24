#In Bubble Sort, the largest value is bubbled up in every pass.
#Every two adjacent items are compared and they are swapped if they are in the wrong order.
#This way, after every pass, the largest element reaches to the end of the array.
#Time complexity of Bubble Sort in Worst and Average Case is O(n^2) and in best case, its O(n)

def bubble_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(len(array)-i-1): #In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            if array[j] > array[j+1]: #If two adjacent elements in the wrong order are found, they are swapped
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))
'''
[5, 9, 3, 10, 45, 2, 0]
[5, 3, 9, 10, 2, 0, 45]
[3, 5, 9, 2, 0, 10, 45]
[3, 5, 2, 0, 9, 10, 45]
[3, 2, 0, 5, 9, 10, 45]
[2, 0, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
'''