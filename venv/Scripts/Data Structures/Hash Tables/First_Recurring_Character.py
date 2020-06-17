#Google Question
#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2
#Example 2 : array = [2,6,4,6,1,3,8,1,2]
#It should return 6

#First thing that comes to mind is we can create a dictionary and keep storing each element of the array in the dictionary
#as we go along the array. But before adding the element to the dictionary, we'll check if the element is already present in the dictionary
#If yes, then we simply return the element and break out
#If not, then we add the element to the dictionary and move forward

def simple_frc(array):
    dictionary = dict()
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None

array = [2,1,4,1,5,2,6]
#print(simple_frc(array))

#The time complexity is O(n) as we are looping through the array only once
#And the search which we are doing in the dictionary, is of O(1) time, since it is basically an implementation of hash table.


#Another aproach can be the naive approach using two nested loops

def naive_frc(array):
    l = len(array)
    i= 0
    frc = None
    while(i<l):
        j = i+1
        while(j<l):
            if array[i] == array[j]:
                l = j
                frc = array[j]
                continue
            else:
                j+=1
        i += 1
    return frc

print(naive_frc(array))

#The outer while loop runs from the first index of the array to the index of the first recurring character
#For example, in the given array here, [2,1,4,1,5,2,6], in the first iteration the loop runs till index 5, where it encounters 2,
#The first recurring character with respect to the element at index i, which in the first iteration is 2
#After finding the first recurring character of the element at the ith index, it runs from the i+1th index to l-1th index,
#where l is the index of the recurring character, or the last element of the array if no recurring character is found
#This way, every time a recurring character is found in the array before the occurence of the recurring character found by the previous iteration,
#It gets updated in the variable frc and the indices are adjusted so as to run the loop only till the index of the recurring character found in the previous iteration
#Because if no recurring character is found before that, it implies the previous recurring character is the first one!
#Time Complexity is O(n^2) but space complexity is O(1), which is better than the earlier solution
