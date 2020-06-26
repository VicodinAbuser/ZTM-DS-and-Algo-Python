#Now we will implement our old Fibonacci program using Dynamic Programming
#Fibonacci Sequence : 0 1 1 2 3 5 8 13 21 35 55 89 144 233 . . .

import time

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


cache = {}
def dynamic_fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
            return cache[n]


t1 = time.time()
print(fibonacci(30))
t2 = time.time()
print(t2-t1)
#832040
#0.39888763427734375

t1 = time.time()
print(dynamic_fibonacci(30))
t2 = time.time()
print(t2-t1)
#832040
#0.0


t1 = time.time()
print(dynamic_fibonacci(60))
t2 = time.time()
print(t2-t1)
#1548008755920
#0.0


t1 = time.time()
print(dynamic_fibonacci(100))
t2 = time.time()
print(t2-t1)
#354224848179261915075
#0.0

t1 = time.time()
print(dynamic_fibonacci(1000))
t2 = time.time()
print(t2-t1)
#43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
#0.0009982585906982422

#I won't even dare to try calculating fibonacci(1000) using the normal recursive function!