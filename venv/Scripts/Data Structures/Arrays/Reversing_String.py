# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

#The first solution that comes to mind is we can create a new array and append the characters of the original array,
#one by one from the end to the beginning.

def simple_reverse(string):
    new_string = str()
    for i in range(len(string)-1, -1, -1): #The for loop runs from the last element to the first element of the original string
        new_string = new_string + string[i] #The characters of the original string are added to the new string
    return new_string

string = "Hello"
print(simple_reverse(string))
#Since we only have to traverse the string once, the time complexity is O(n)
#But since we are also creating a new array of the same size , the space complexity is also O(n)
