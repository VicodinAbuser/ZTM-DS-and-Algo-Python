#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]

#One solution can be : we compare the corresponding elements of both arrays
#We add the smaller element to a new array and increment the index of the array from which the element was added.
#Again we compare the elements of both arrays and repeat the procedure until all the elements have been added.

def merge(array1, array2):
    new_array = []
    flag = 0
    first_array_index = second_array_index = 0
    while not (first_array_index>=len(array1) or second_array_index>=len(array2)): #The loop runs until we reach the end of either of the arrays
        if array1[first_array_index] <= array2[second_array_index]:
            new_array.append(array1[first_array_index])
            first_array_index += 1
        else:
            new_array.append(array2[second_array_index])
            second_array_index += 1

        if first_array_index==len(array1): #When the loop finishes, we need to know which array's end was reached, so that the remaining elements of the other array can be appended to the new array
            flag = 1 #This flag will tell us if we reached the end of the first array or the second array

    if flag == 1: #If the end of the first array was reached, the remaining elements of the second array are added to the new array
        for item in array2[second_array_index:]:
            new_array.append(item)
    else: #And if the end of the second array was reached, the remaining elements of the first array are added to the new array
        for item in array1[first_array_index:]:
            new_array.append(item)

    return new_array

array1 = [1,3,5,7]
array2 = [2,4,6,8,10,12]
print(merge(array1,array2))
#[1, 2, 3, 4, 5, 6, 7, 8, 10, 12]



