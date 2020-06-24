#Given a number, we have to return its factorial.
#For example, factorial(5) should return 5! = 5*4*3*2*1 = 120
#We can solve this recursively, or iteratively.
#First we are going to solve it iteratively.

def iterative_factorial(number):
    f = 1
    for i in range(1, number+1):
        f = f * i
    return f

print(iterative_factorial(0))
#1
print(iterative_factorial(5))
#120
print(iterative_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000
