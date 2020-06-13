import time

large1 = ['nemo' for i in range(100000)]
large2 = ['nemo' for i in range(100000)]

def find_nemo(array1, array2):

    #Here there are two different variables array1 and array2.
    #They have to be represented by 2 different variables in the Big-O representation as well.
    #Let array1 correspond to m and array2 correspond to n

    t0 = time.time() #O(1)
    for i in range(0,len(array1)): #O(m)
        if array1[i] == 'nemo': #m*O(1)
            print("Found Nemo!!") #k1*O(1) where k1 <= m because this statement will be executed only if the if statement returns True, which can be k1(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1-t0} seconds.') #O(1)

    t0 = time.time() #O(1)
    for i in range(0, len(array2)): #O(n)
        if array2[i] == 'nemo': #n*O(1)
            print("Found Nemo!!") #k2*O(1) where k2 <= m because this statement will be executed only if the if statement returns True, which can be k2(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1 - t0} seconds.') #O(1)

find_nemo(large1, large2)

#Total time complexity of the find_nemo function =
#O(1 + m + m*1 + k1*1 + 1 + 1 + 1 + n + n*1 + k2*1 + 1 + 1) = O(6 + 2m + 2n + k1 + k2)
#Now k1<=m and k2<=n. In the worst case, k1 can be m and k2 can be n. We'll consider the worst case and calculate the Big-O
#O(6 + 2m + 2n + m + n) = O(3m + 3n + 6) = O(3(m + n + 2))
#The constants can be safely ignored.
#Therefore, O(m + n + 2) = O(m + n)
