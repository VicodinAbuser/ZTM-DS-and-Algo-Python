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

array = [0,0,0,0,1,0,3,0,0,0,12,9,7]
print(naive_zero_mover(array))


#A far better solution can be swapping every non-zero element we find with the first un-swapped zero

def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z += 1
    return array
print(swap_move(array))
#In this solution, we traverse the array and swap every non-zero element with itself until we find a 0
#Then we swap the next non-zero element with the 0 and we keep doing this until we have looped over the entire array.
#This seems like a cleaner solution to the first one but still there are lots of unnecessary swaps going on here.
#Still, we are looping over the array once and the swapping is done in constant time, so overall time complexity is O(n)


#A very elegant solution to this problem can be the following one-liner :

def one_liner_move(array):
    array.sort(key=bool, reverse=True)
    return array

print(one_liner_move(array))

#What this does is it sorts the array in place using the key as boolean.
#Now the integer 0 is considered as boolean 0 and all other integers are considered as boolean 1
#So providing the key as bool, we are telling the sort method to sort the array on the basis of boolean values
#The 0's , which are considered as 0, come first, and the remaining numbers, considered as 1, come next, in their original order.
#The reverse=True reverses this arrangement so that the 0's are all the end and the non-zero numbers at the front.
#The complexity for this is O(nlog n) as the complexity of Python's built-in sort method is O(nlog n)