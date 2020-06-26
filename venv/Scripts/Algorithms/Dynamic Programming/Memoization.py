#Memoization is an optimization technique used to speed up programs by storing the results of expensive function calls
#and returning the cached result when the same inputs occur again.
#In Python there's a module named functools with a method lru_cache() which allows us to use this optimization technique
#First, we'll implement memoization on our own with an example function, then with the help of lru_cache

import time, random

times =[]

def squaring_without_memoization(number): #Function to calculate the suare of a number
    return number**2

array = [random.randint(1,10) for _ in range(10000000)] #Generates an array of size 1000000 with random integers between 1-10(both included)
t1 = time.time()
for i in range(len(array)):
    print(squaring_without_memoization(array[i]))
t2 = time.time()
times.append(t2-t1)


cache = {}
def squaring_with_memoization(number):
    if number in cache:
        return cache[number]
    else:
        cache[number] = number**2
        return cache[number]

t1 = time.time()
for i in range(len(array)):
    print(squaring_with_memoization(array[i]))
t2 = time.time()
times.append(t2-t1)


from functools import lru_cache

@lru_cache(maxsize=10000)
def squaring(number):
    return  number**2

print(array)
t1 = time.time()
for i in range(len(array)):
    print(squaring(array[i]))
t2 = time.time()
times.append(t2-t1)

print(times)
#[203.95188665390015, 148.48580384254456, 148.26833629608154]   ---  When array size was 10000000
#[7.06306266784668, 6.145563125610352, 5.758295774459839]   ---   When array size was 1000000

print(cache)
#{8: 64, 7: 49, 6: 36, 1: 1, 4: 16, 9: 81, 2: 4, 5: 25, 3: 9, 10: 100}

print(squaring.cache_info())
#CacheInfo(hits=999990, misses=10, maxsize=10000, currsize=10)   ---   When array size was 1000000
#CacheInfo(hits=9999990, misses=10, maxsize=10000, currsize=10)   ---  When array size was 10000000

