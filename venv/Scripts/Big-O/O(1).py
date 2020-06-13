#O(1) - Constant Time
#The no. of operations do not depend on the size of the input and are always constant.
import time

array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(100000)]

def finding_nemo(array):
    t0 = time.time()
    print(array[0]) #O(1) operation
    print(array[1]) #O(1) operation
    t1 = time.time()
    print(f'Time taken = {t1-t0}')

finding_nemo(array_small)
finding_nemo(array_medium)
finding_nemo(array_large)

#Time taken in all 3 cases would be 0.0 seconds because we are only extracting the first and second elements of the arays.
#We are not looping over the entire array.
#We are performing two O(1) operations, which equal to O(2)
#Any constant number can be considered as 1. There we can say this function is of O(1) - Constant Time Complexity.

