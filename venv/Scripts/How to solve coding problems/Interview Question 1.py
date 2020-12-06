# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.

# Now, the very first solution that comes to mind is the naive, or brute force solution.
# So let's code that down.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

def brute_force_matching_element(array1, array2):
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                return True
    return False

#Complexity of brute_force_matching_element function = ?
#At first glance it looks like O(n^2) but since there are two different variables in the form of array1 and array2,
#The complexity actually is O(m*n), which is equally bad.

#This is a good first solution to come up with but we can easily recognize here that as the input size gets large,
#This function becomes very inefficient.
#So we need to come up with something better.

#One solution can be creating a dictionary for one of the arrays and then looping over the other array
#To check if any of its elements are present in the dictionary's keys.
#Dictionaries are implemented as hash tables in python, and the time complexity for look-ups or searching for an item, is O(1).
#Therefore, the dictionary can be created in O(n) time and then we loop over one array of size say m,
#Where we check for every element if it is present in the dictionary's keys, which is an O(1) operation.
#Therefore, the overall complexity of the function becomes, O(n + m*1) = O(m+n)
#Which is significantly better than our previous function.

def smarter_matching(array1, array2):
    dictionary = dict()
    for i in range(len(array1)):
        dictionary[array1[i]] = True

    for i in range(len(array2)):
        if array2[i] in dictionary:
            return True

    return False

print(smarter_matching(array1, array2))


#In this solution, we've made a number of asssumptions, like there will be no repitions of any element in an array,
#Or that our function will receive exactly 2 inputs which will be arrays.
#Now that we have come up with a better solution in terms of time complexity, we can look to iron out the minor flaws.
#Let's make our function such that it can receive arrays with repititve elements, and if it receives anything other than two arrays
#It gives an error message instead of just crashing out.

def smarter_matching2(array1, array2):
    try:
        dictionary = dict()
        for i in range(len(array1)):
            if array1[i] not in dictionary:
                dictionary[array1[i]] = True

        for i in range(len(array2)):
            if array2[i] in dictionary:
                return True
        return False

    except TypeError:
        return "Exactly two arrays required."
