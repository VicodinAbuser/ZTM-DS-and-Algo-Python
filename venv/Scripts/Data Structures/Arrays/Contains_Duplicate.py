#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

#As usual we'll get the naive approach out of the way first.

def brute_force_duplicate_search(array):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                return True
    return False

array = [1,2,46,32,98,61,34,46]
print(brute_force_duplicate_search(array))

#This is pretty simple, as we go through every possible pair of elements to check if they are the same.
#If we find a pair having the same elements we return True, else we return False
#Time Complexity - O(n^2)

#A slightly better solution can be :
#First we sort the array using O(nlog n) built-in sort of Python.
#Then we loop through the array once to check if any consecutive elements are same, which will be O(n).
#So overall complexity will be O(nlog n)

def better_duplicate_search(array):
    array.sort()
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            return True
    return False

print(better_duplicate_search(array))

#An even better solution can be using a dictionary.
#As we loop through the array, we'll check first if the current element is present in the dictionary
#If yes, we return True
#If no, we add the element to the dictionary.
#Since looking up in a dictionary is O(1) time, overall complexity would be O(n)

def smart_duplicate_search(array):
    dictionary = dict()
    if len(array)<2:
        return False
    else:
        for i in range(len(array)):
            if array[i] in dictionary:
                return True
            else:
                dictionary[array[i]] = True
    return False

print(smart_duplicate_search(array))