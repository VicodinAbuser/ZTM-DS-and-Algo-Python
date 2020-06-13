import time

array1 = ['a','b','c','d','e']
array2 = [1,2,3,4,5]

def pairs(array1, array2):

    # Here there are two different variables array1 and array2.
    # They have to be represented by 2 different variables in the Big-O representation as well.
    # Let array1 correspond to m and array2 correspond to n

    for i in range(len(array1)): #n*O(m)
        for j in range(len(array2)): #m*O(n)
            print(array1[i],array2[j]) #m*n*O(1)

pairs(array1,array2)

#Total time complexity of the pairs function =
#O(n*m + m*n + m*n*1) = O(3*m*n)
#The constants can be safely ignored.
#Therefore, O(m * n * 3) = O(m * n)

