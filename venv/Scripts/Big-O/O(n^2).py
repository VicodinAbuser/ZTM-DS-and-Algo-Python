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