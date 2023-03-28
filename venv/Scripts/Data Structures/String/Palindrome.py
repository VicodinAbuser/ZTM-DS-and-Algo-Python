#   String Palindrome program in python

#   Author: Pavankumar Hegde 
"""How this Python program will behave?
To check String is Palindrome or not?  This Program will take a String as an input. And after applying some logic it will return output as String is Palindrome or not.

For Example: 

Suppose if we give input a string “madam”. This is palindrome String then our program will print “Given string is palindrome”.

And if we give “abcd” then our program will give “Given String is not palindrome”.

Palindrome program of String in Python
Using reverse and compare
Below program is very simple. Here first we will reverse the original input string and then compare it with original input.

If both string, before reverse and after reverse is equal then print String is Palindrome otherwise not.

To reverse string in this program [:: -1] is used.

To compare string, == is used in if-else statement."""
#   Program: String Palindrome program in Python



string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome") 