#Given a number, we have to return the number at that index of the fibonacci sequence.
#Fibonacci Sequence - 0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .
#For example, fibonacci(5) should return 5 as the 5th index (staring from 0) of the fibonacci sequence is the number 5
#Again , we will do both the iterative and recursive solutions

def iterative_fibonacci(index):
    first_number = 0
    second_number = 1
    if index == 0:
        return first_number
    if index == 1:
        return second_number
    for i in range(2,index +1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number

print(iterative_fibonacci(0))  #0
print(iterative_fibonacci(1))  #1
print(iterative_fibonacci(5))  #5
print(iterative_fibonacci(7))  #13
print(iterative_fibonacci(10)) #55
print(iterative_fibonacci(12)) #144


def recursive_fibonacci(index):
    if index == 0: #Base case 1
        return 0
    if index == 1: #Base case 2
        return 1
    return  recursive_fibonacci(index-1) + recursive_fibonacci(index-2) #Every term in fib sequence = sum of previous two terms

print(recursive_fibonacci(0))   #0
print(recursive_fibonacci(1))   #1
print(recursive_fibonacci(5))   #5
print(recursive_fibonacci(7))   #13
print(recursive_fibonacci(10))  #55
print(recursive_fibonacci(12))  #144
