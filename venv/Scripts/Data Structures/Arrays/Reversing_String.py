# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

#The first solution that comes to mind is we can create a new array and append the characters of the original array,
#one by one from the end to the beginning.

def simple_reverse(string):
    new_string = []
    for i in range(len(string)-1, -1, -1): #The for loop runs from the last element to the first element of the original string
        new_string.append(string[i]) #The characters of the original string are added to the new string
    return ''.join(new_string) #The characters of the reversed array are joined to form a string

string = "Hello"
print(simple_reverse(string))
#Since we only have to traverse the string once, the time complexity is O(n)
#But since we are also creating a new array of the same size , the space complexity is also O(n)


#A smarter way to do this , can be taking a pair of elements from either end of the string and swapping them
#We have start at both the ends and continue swapping pairs till the middle of the string
#This way we can avoid having to create a new array and save on space complexity while keeping time complexity at O(n)

def swap(string, a, b): #Function which swaps two characters of a string
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

def smarter_reverse(string):
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string

print(smarter_reverse(string))


#Apart from these, some built-in functions that can be used to reverse a string are as follows:

string1 = 'abcde'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))

#Both these methods are of O(n) time complexity