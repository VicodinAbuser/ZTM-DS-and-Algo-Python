#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Example 1:
#nput: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]

#The instant solution for this that comes to mind is :
#We create a new array and initialize the first k elemenst of the new array with the last k elements of the original array.
#Then we fill in the remaining elements
#The time complexity is O(n) and the space complexity is also O(n)


def naive_rotation(array, k):
    new_array = []
    for i in range(k):
        new_array.append(array[len(array)-k+i])
    for i in range(len(array)-k):
        new_array.append(array[i])
    return new_array

array = [1,2,3,4,5,6,7,8,9]
k = 5
print(naive_rotation(array,k))

