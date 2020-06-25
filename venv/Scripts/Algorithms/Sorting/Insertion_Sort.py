#In Insertion sort, for the first iteration we fix the first element, assuming it is at its correct position
#Then we loop through the rest of the elements and insert them in their correct positions, with respect to the alreay sorted part of the array
#Time complexity is O(n^2) in worst case

def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        print(array)
        last_sorted_position = array[i-1]  #We store the last element which is sorted
        count += 1
        if array[i] < last_sorted_position: #We check if the current element is lesser than the last sorted element
            temp = array[i] #If yes, we store the curent element in a temporary variable.
            for j in range(i-1,-1,-1):  #We loop backwards through the sorted part of the array to check where the current element fits
                count += 1
                if temp < array[j]: #For every element we find in the sorted part which is greater than the current element, we shift them one place towards right to make room for the current element
                    if j == 0: #If we reach the beginning of the array in the process, we shift the elements right and we assign the current element to the 0th position
                        array[j+1] = array[j]
                        array[j] = temp
                    else: #Otherwise we just keep shifting
                        array[j+1] = array[j]
                else: #Once we find an element that is smaller than the current element, it means we have found the position to insert out current element at
                    array[j+1] = temp #So we just assign the element to its correct position
                    break #And break out of this loop
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(insertion_sort(array))
'''
[5, 9, 3, 10, 45, 2, 0]
[5, 9, 3, 10, 45, 2, 0]
[3, 5, 9, 10, 45, 2, 0]
[3, 5, 9, 10, 45, 2, 0]
[3, 5, 9, 10, 45, 2, 0]
[2, 3, 5, 9, 10, 45, 0]
[0, 2, 3, 5, 9, 10, 45] 
Number of comparisons = 19
'''

sorted_array = [5,6,7,8,9]
print(insertion_sort(sorted_array))
'''
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9] 
Number of comparisons = 4
'''

#It is fast for sorted or nearly sorted inputs as can be seen with the number of comparisons above.

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(insertion_sort(reverse_sorted_array))
'''
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[8, 9, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[7, 8, 9, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[6, 7, 8, 9, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[5, 6, 7, 8, 9, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[4, 5, 6, 7, 8, 9, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[3, 4, 5, 6, 7, 8, 9, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[2, 3, 4, 5, 6, 7, 8, 9, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -2, -3, -4, -5, -6, -7, -8, -9, -10]

[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -3, -4, -5, -6, -7, -8, -9, -10]

[-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -4, -5, -6, -7, -8, -9, -10]

[-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -5, -6, -7, -8, -9, -10]

[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -6, -7, -8, -9, -10]

[-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -7, -8, -9, -10]

[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -8, -9, -10]

[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -9, -10]

[-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -10]

[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

Number of comparisons = 209
'''