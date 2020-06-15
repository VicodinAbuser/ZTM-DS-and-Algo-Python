#This question is same as that in the Google interview question video.
#We are given an array of integers and a particular sum.
#We have to check if there are any two elements in the array that add up to the given sum.
#For example, array = [1,2,4,5] ,sum = 6
#This should return True as 2+4 = 6


#Again, the very first solution that comes to mind is the naive, or brute force approach. Lets implement that.

array = [1,2,4,5]
sum = 3
def brute_force_pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == sum:
                return "Yes"
    return "No"

#print(brute_force_pair_sum(array, sum))

#As we can clearly see, the complexity of this function is O(n^2), which will become very inefficient for large inputs
#We need to  optimize the function


#One solution better than O(n^2) that comes to mind is :
#We loop through the array once and for every element we encounter, we calculate its complement,i.e., the number which when added
#to the element at hand, will give the sum.
#Then we do a binary search for this complement in the remaining portion of the array
#Since binary search is O(log n) and we loop through the array once, the overall complexity is O(nlog n), which is better than O(n^2)

def binary_search(array,left,right, ele):
    if right >= left:
        mid = (left+right)//2
        if (array[mid]) == ele:
            return True
        elif array[mid] > ele:
            return binary_search(array, left, mid - 1, ele)
        else:
            return binary_search(array, mid + 1, right, ele)
    else:
        return False

def slightly_better_pair_sum(array, sum):
    for i in range(len(array)):
        comp = sum - array[i]
        if binary_search(array,i+1,len(array)-1,comp):
            return "Yes"
    return "No"

print(slightly_better_pair_sum(array,sum))

#We have arrived at an O(nlog n) function from the naive O(n^2)
#But this is still not great and it seems like there is some scope for improvement.
#Lets try to make it O(n)

#One solution is :
#We take one element from each end and calculate their sum. If it equals the given sum, job done!
#If not, and if the given sum is greater than what we get, it means we require the sum of the pair to be higher
#To achieve that we move the left index by one and add the corresponding element to the element at the right index
#And if the given sum is less than what we get, it means we require the sum of the pair to be smaller,
#So we move the right index one step left and add the corresponding element to the element at the left index.
#We keep on moving like this until we find a pair which adds up to the given sum or until the left and right indices cross
#Since this procedure requires only one traversal of the array, the complexity is O(n)!


def smart_pair_sum(array, sum):
    left = 0
    right = len(array)-1
    while right > left:
        if array[left] + array[right] == sum:
            return "Yes"
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return "No"

print(smart_pair_sum(array,sum))


#Although we have achieved an efficient time complexity of O(n) we've done so under the assumption that the array will be sorted
#What if the array isn't sorted?
#In that case the first solution that comes to mind is that we can sort the array in O(nlog n) time
#And then perform the smart_pair_sum operation on the sorted array to give us a final time complexity of O(nlog n)
#Python's built-in sort method uses Tim Sort which has an average case time coplexity of O(nlog n)
#So we can simply use that, or use a different sorting algorithm such as quicksort or heapsort.
#Here, we are going with the built-in method


def sort_pair_sum(array, sum):
    array.sort()
    left = 0
    right = len(array)-1
    while right > left:
        if array[left] + array[right] == sum:
            return "Yes"
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return "No"

print(sort_pair_sum(array,sum))

#This solves our problem if the array is unsorted to begin with.
#But we have lost out on time complexity as we have gone from O(n) to O(nlog n)
#One thing we can do to get back to O(n) complexity is :
#We can create a dictionary as we go along the array and enter the element we encounter to the dictionary
#If the complement of the present element isn't already present in the dictionary
#That is, we loop through the array once, and first check if the complement of the current element is present in the dictionary
#If yes, then we return "Yes". If no, then we add the current element to the dictionary.

def smartest_pair_sum(array, sum):
    dictionary = dict()
    for item in array:
        comp = sum - item
        if not comp in dictionary:
            dictionary[item] = True
        else:
            return "Yes"
    return "No"

print(smartest_pair_sum(array, sum))

#We have achieved an O(n) algorithm taking into consideration that the array can be unsorted!
