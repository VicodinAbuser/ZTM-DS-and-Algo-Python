#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
#and return its sum.
#Example:
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


#The first solution that comes to mind, as always, is the brute force solution.
#Here we will extract the sum of every possible subarray of the given array and return the maximum value.
#We can predict right off the bat that it is not going to be an optimal solution, but it is going to be a solution nonetheless.
#So let's try it.

def brute_force_max_subarray(array):
    maximum = 0
    if len(array)==0:
        return None
    for i in range(len(array)):
        cum_sum = 0
        for j in range(i,len(array)):
            cum_sum += array[j]
            maximum = max(maximum, cum_sum)
    return maximum

array = [-2,1,-3,4,-1,2,1,-5,4]
print(brute_force_max_subarray(array))

#What's happening here is each iteration of the outer loop is giving us all the possible subarrays starting from the ith index.
#For example, in the first iteration we get all the subarrays starting with the first element and so on.
#Now with the second for loop we are building a subarray starting from the ith index to the last index
#In the process we are cumulating the sum at every iteration which is giving us the sum of the subarray from the ith index to the jth index
#Then we are checking if the cumulative sum is greater than all other cumulative sums we have found so far and storing the greatest sum in "maximum"
#Finally we return maximum which contains the greatest sum of any subarray in the array.
#Since we are looping through two nested for loops the time complexity is O(n^2)


#There's a much faster way to solve this though, and that is by using the Kadane's algorithm.
#In this, we loop over the array and for every iteration we check for the mximum subarray ending at that index.
#Now the maximum subarray ending at a particular index can be either of two things:
#1. Sum of the maximum subarray ending at the previous index + the element at the current index, or
#2. The current element only.
#So lets implement this algorithm.

def kadane(array):
    maximum = maxarray = array[0]
    for i in range(1,len(array)):
        maxarray = max(array[i], maxarray+array[i])
        maximum = max(maxarray, maximum)
    return maximum

print(kadane(array))

#We set the variables maximum and maxarray to the value of the first element of the array.
#Then we loop over the entire array from the first index.
#At every iteration, we update the value of maxarray to be the maximum among the current element
#and the sum of the maxarray ending at the previous index and the current element
#This way, maxarray stores the maximum subarray ending at index i
#And the variable maximum stores the maximum among all the maxarrays ending at every index, effectively storing the global maximum
#Since this requires only one for loop, the time complexity is an effiecient O(n)!