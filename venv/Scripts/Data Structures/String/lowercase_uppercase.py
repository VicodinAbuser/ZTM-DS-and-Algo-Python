#   Author: Pavankumar Hegde


# Python Program to Convert lowercase to uppercase character

"""
Problem Statement
For any input string, any lowercase character used in input string will be replaced with uppercase character of same alphabet as lowercase character.

For example:

Case1: if user inputs ‘Quescol’

         The output should be ‘QUESCOL’

         The ‘uescol’ of string is replaced with ‘UESCOL’

Case2: if user inputs ‘pyThon’

         The output should be ‘PYTHON’




Our logic to convert lowercase character to uppercase character
Our program will take a string input from the user.
Then program will iterate through each character of the string.
If any lowercase letter will found, then our program will convert it into uppercase letter using upper() function.
And finally print the output.



Algorithm to convert lowercase character to uppercase character


Step1:  Start

Step2:   Take a string as an input from the user.

Step3: Create an empty string, as result = “ ”

Step4:  Use for loop to iterate through the string.

Step5: if lowercase found:

                  i = i.uppercase()

                 result +=i ( concatenate the characters of string)

Step6:  Stop


""" 

# Python code to convert lowercase character to uppercase character of string


string = input("Enter a String : ")
result=''
for i in string:  #iterate through each letter/character from the string
        if i.islower():  #if lowercase
            i = i.upper() #converting lowercase into uppercase letter
        result += i #concatenating each character of the string without lowercase letter 
print("String after converting lower case to upper :",result)



