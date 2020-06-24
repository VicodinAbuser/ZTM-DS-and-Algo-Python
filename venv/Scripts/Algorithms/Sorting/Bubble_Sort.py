#In Bubble Sort, the largest value is bubbled up in every pass.
#Every two adjacent items are compared and they are swapped if they are in the wrong order.
#This way, after every pass, the largest element reaches to the end of the array.
#Time complexity of Bubble Sort in Worst and Average Case is O(n^2) and in best case, its O(n)

def bubble_sort(array):
    count = 0
    for i in range(len(array)-1): #-1 because when only 1 item will be left, we don't need to sort that
        print(array)
        for j in range(len(array)-i-1): #In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            count += 1
            if array[j] > array[j+1]: #If two adjacent elements in the wrong order are found, they are swapped
                array[j], array[j+1] = array[j+1], array[j]
    #print(f'Number of comparisons = {count}')
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))

'''
[5, 9, 3, 10, 45, 2, 0]
[5, 3, 9, 10, 2, 0, 45]
[3, 5, 9, 2, 0, 10, 45]
[3, 5, 2, 0, 9, 10, 45]
[3, 2, 0, 5, 9, 10, 45]
[2, 0, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
Number of comparisons = 21
'''


sorted_array = [5,6,7,8,9]
print(bubble_sort(sorted_array))

'''
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9] 
Number of comparisons = 10
'''



#We can optimize the bubble sort slightly by adding a new boolean variable
#which keeps track of wehether any swaps were done in the last iteration or not
#This way, if say halfway through the loops, the array becomes completely sorted, then we won't do unnecessary comparisons
def optimized_bubble_sort(array):
    count = 0
    for i in range(len(array) - 1):
        swap = False
        print(array)
        for j in range(len(array) - i - 1):
            count += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if swap==False:
            return (f'{array} \nNumber of comparisons = {count}')
    return (f'{array} \nNumber of comparisons = {count}')


array1 = [5,9,3,10,45,2,0]
print(optimized_bubble_sort(array1))

'''
[5, 9, 3, 10, 45, 2, 0]
[5, 3, 9, 10, 2, 0, 45]
[3, 5, 9, 2, 0, 10, 45]
[3, 5, 2, 0, 9, 10, 45]
[3, 2, 0, 5, 9, 10, 45]
[2, 0, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45] 
Number of comparisons = 21
'''


sorted_array1 = [5,6,7,8,9]
print(optimized_bubble_sort(sorted_array1))

'''
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9] 
Number of comparisons = 4
'''