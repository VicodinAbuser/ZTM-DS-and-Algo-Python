import time

nemo = ["nemo"]
everyone = [
    "dory",
    "bruce",
    "marlin",
    "nemo",
    "gill",
    "bloat",
    "nigel",
    "squirt",
    "darla",
]
large = ["nemo" for i in range(100000)]


# Function to find 'nemo' in an array
def find_nemo(array):
    t0 = time.time()
    for i in array:
        if i == "nemo":
            print("Found Nemo!!")
    t1 = time.time()
    print(f"The search took {t1-t0} seconds.")


# Test with different input sizes
# find_nemo(nemo)
# find_nemo(everyone)
# find_nemo(large)


# Function to demonstrate time complexity analysis
def funchallenge(input):
    temp = 10  # O(1)
    temp += 50  # O(1)
    a = 0  # O(1)
    for i in input:  # O(n)
        var = True  # n * O(1)
        a += 1  # n * O(1)
    return a  # O(1)


funchallenge(large)

# Total running time of the funchallenge function
# O(1 + 1 + 1 + n + n * 1 + n * 1 + 1) = O(3n + 4)
# Since constants terms are ignored in Big-O notation, this simplifies to O(n)
# Therefore, the funchallenge function exhibits linear time complexity.

# O(n) - Linear Time
# The input size (n) increases, the time taken to execute the algorithm or operation also increases linearly.
# for loops, while loops through n items
