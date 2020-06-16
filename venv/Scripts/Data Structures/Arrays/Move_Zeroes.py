#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

#The first solution that comes to mind is we can traverse the original length of the array and for every zero we find,
#We append a 0 at the end of the array.
#Then we again traverse the array, only for the original length of the array,
#And we pop every 0 that we find, thus removing every 0 from the original part of the array and moving them all to the end.
#This seems inefficient as pop operation anywhere apart fromthe end of the array costs O(n) time
#And we have loop over the entire array so it becomes O(n^2), but lets see.

def naive_zero_mover(array):
    l = len(array)
    for i in range(l):
        if array[i] == 0:
            array.append(0) #We have appended 0's at the end for every 0 in the original array
    j = 0
    c = 0
    while c < l: #We run the while loop only for l times, i.e., the original length of the array
        if array[j]!=0:
            j += 1 #If the element is non-zero we increment j by 1, which keeps track of every index of the array upto l
        else:
            array.pop(j) #If we find a 0 , we pop it and we do not increase j as all the elements have been shifted left. So the next element is in jth index only
        c += 1
    return array

array = [0,1,0,3,0,0,0,12]
print(naive_zero_mover(array))

