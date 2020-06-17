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
    for i in range(k%len(array)):
        new_array.append(array[len(array)-k+i])
    for i in range(len(array)-k%len(array)):
        new_array.append(array[i])
    return new_array

array = [1,2,3,4,5,6,7,8,9]
k = 11
print(naive_rotation(array,k))


#Another inefficient but correct approach can be the brute force appoach where we rotate the array by 1 element in each traversal of the array
#This way we won't have to use another array, so we'll save on space complexity
#But the time complexity would be O(n*k) as we we'll have to rotate the array k times and for each rotation, we need to traverse the entire array

def brute_force_rotation(array, k):
    for i in range(k):
        temp = array[-1]
        for i in range(len(array)-1,0,-1):
            array[i] = array[i-1]
        array[0] = temp
    return array

print(brute_force_rotation(array, k))


#A better solution can be using the Reversal Algorithm
#In this, we first reverse the entire array, then we reverse the first k elements, followed by reversing the last n-k elements
#Since, the time complexity of reversing is O(n)
#Therefore, overall time complexity for this algorithm would be O(3n) which is equal to O(n), with no extra space required

def reverse(array, start, end): #Function to reverse the elements of array from index start to index end
    while start<end:
        print(start, end)
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

def reverse_rotate(array, k):
    array = reverse(array,0,len(array)-1)
    print(array) #At this stage, the entire array would be reverse. Output : [9,8,7,6,5,4,3,2,1]
    array = reverse(array,0,k%len(array)-1)
    print(array) #By now, the first k elements would be reverse. Output : [8,9,7,6,5,4,3,2,1]
    array = reverse(array,k%len(array),len(array)-1)
    print(array) #Finally the last k%len(array) - n items would be reverse. Output: [8,9,1,2,3,4,5,6,7]
    return array

a = [1,2,3,4,5,6,7,8,9]
print(reverse_rotate(a,k))
