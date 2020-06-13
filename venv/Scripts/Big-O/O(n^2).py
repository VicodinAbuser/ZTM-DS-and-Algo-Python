import time

array = ['a','b','c','d','e']

def log_all_pairs(array):

    #There are nested for loops in this function but there is only one variable array. So we don't need two variables for the Big-O

    for i in range(len(array)): #n*O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i], array[j]) #n*n*O(1)

log_all_pairs(array)

#Total time complexity of the log_all_pairs function =
#O(n*n + n*n + n*n*1) = O(3n^2)
#The constants can be safely ignored.
#Therefore, O(3n^2) = O(n^2)

new_array = [1,2,3,4,5]
def print_numbers_then_pairs(array):

    #There are a total of three loops here but only one variable. So we need only variable for our Big-O notation

    print("The numbers are : ") #O(1)
    for i in range(len(array)): #O(n)
        print(array[i]) #n*O(1)

    print("The pairs are :") #O(1)
    for i in range(len(array)): #n*O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i], array[j]) #n*n*O(1)

print_numbers_then_pairs(new_array)

#Total time complexity of the print_numbers_then_pairs function =
#O(1 + n + n*1 + 1 + n*n + n*n + n*n*1) = O(3n^2 + 2n + 2)
#Now, Big-O presents scalability of the cod, i.e., how the code will behave as the inputs grow larger and larger
#Therefore if the expression contains terms of different degrees and the size of inputs is huge, the terms of the smaller degrees become negligible in comparison to those of the higher degrees
#Therefore, we can ignore the terms of the smaller degrees and only keep the highest degree term
#O(3n^2 + 2n + 2) = O(3n2)
#The constants can be safely ignored.
#Therefore, O(3n^2) = O(n^2)