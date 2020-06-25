#Selection sort involves finding the minimum element in one pass through the array
#and then swapping it with the first position of the unsorted part of the array.
#Time complexity of selection sort is O(n^2) in all cases

def selection_sort(array):
    count = 0
    for i in range(len(array)-1): #-1 because when only 1 elment remians, it will be already be sorted
        print(array)
        minimum = array[i] #We set the minu=imum element to be the ith element
        minimum_index = i #And the minimum index to be the ith index
        for j in range(i+1,len(array)): #Then we check the array from the i+1th element to the end
            count += 1
            if array[j] < minimum: #If a smaller element than the minimum element is found, we re-assign the minimum element and the minimu index
                minimum = array[j]
                minimum_index = j
        if minimum_index != i: #If minimum index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(selection_sort(array))
'''
[5, 9, 3, 10, 45, 2, 0]
[0, 9, 3, 10, 45, 2, 5]
[0, 2, 3, 10, 45, 9, 5]
[0, 2, 3, 10, 45, 9, 5]
[0, 2, 3, 5, 45, 9, 10]
[0, 2, 3, 5, 9, 45, 10]
[0, 2, 3, 5, 9, 10, 45] 
Number of comparisons = 21
'''
sorted_array = [5,6,7,8,9]
print(selection_sort(sorted_array))
"""
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9] 
Number of comparisons = 10
"""

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(selection_sort(reverse_sorted_array))
'''
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[-10, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, 9]

[-10, -9, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, 8, 9]

[-10, -9, -8, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, 7, 8, 9]

[-10, -9, -8, -7, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, 3, 2, 1, 0, -1, -2, -3, -4, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, 2, 1, 0, -1, -2, -3, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, 1, 0, -1, -2, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, 0, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

Number of comparisons = 190
'''
