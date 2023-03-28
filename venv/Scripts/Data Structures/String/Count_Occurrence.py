#  Python Program to count occurrence of given character in string.add()
#   Author: Pavankumar Hegde 


# Using for Loop


string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)


# Using while Loop

string = input("Please enter String : ")
char = input("Please enter a Character : ")
index, count = 0, 0
while(index < len(string)):
    if(string[index] == char):
        count = count + 1
    index = index + 1
print("Total Number of occurence of ", char, "is :" , count)

# Using Method

def countOccur(char, string):
    count = 0
    for i in range(len(string)):
        if(string[i] == char):
            count = count + 1
    return count
string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = countOccur(char, string)
print("Total Number of occurence of ", char, "is :" , count) 
