"""
How our program will behave?
You have to give a string to the program during the execution and also a character which you want to remove from the given string.

"""
#   Author: Pavankumar Hegde 

#Remove character from string in Python

str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," ")) 



#output :- 

             #please enter a string : char
             #please enter a character : ch
             #ar
             
"""There are Two approach to write a program to remove a given character from string in Python.

1). Using replace() method

2). Using translate() method

Using replace() method
Using replace() method of python we can easily remove a given character from string.

replace() function takes two parameter where first parameter is the character which we want to remove or replace and second parameter is new value which will replace the first parameter from string.

Here we want to remove a given character. So we will replace the character which we want to remove with white space.

Lets see Program below

Remove character from string using replace() method in python

def remove_char(s1,s2):
    print(s1.replace(s2, ''))
s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 


Using translate() method
Using translate() method in python we can also remove all occurrence of a given character from string.

The translate() method in python returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

And to use dictionary we have to use ascii codes instead of characters. 

For this purpose we will use ord() function which takes a character as an input and convert it to ascii.

Lets see program 

Remove character from string using translate() method in python
def remove_char(s1,s2):
    dict = {ord(s2) : None}
    print(s1.translate(dict))
s1 = input("please give a String : ")
s2 = input("please give a Character to remove : ")
remove_char(s1,s2) 
    """