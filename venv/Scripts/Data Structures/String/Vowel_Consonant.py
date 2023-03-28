#   Author: Pavankumar Hegde 
"""
    Problem statement
For any input character, we have to check whether a character is a vowel or consonant.

[elementor-template id=”5257″]

For example:

Case 1: If a user is given input a or A

              The output should be “Vowel”

              As we know that A is a vowel

Case2: If the user is given b or B

             The output should be “consonant”

             As we know that B is consonant
             
             Our logic to check given character is vowel or consonant
Our program will take any character as an input from the user
Then checks if the character taken belongs to vowels or consonants, we achieve this using if-else conditional statements.
[elementor-template id=”5256″]


# Algorithm to check given character is vowel or consonant


Step1:  Start

Step2    Take input from the user

Step3    Apply if-else condition,

                     if(vowel):

                            Print (‘vowel’)

                    else:

                           Print(’consonant’)

Step4 :  Stop


"""

# Python code to check given character is vowel or consonant

Ch=input("Enter a character to check vowel or consonant :") 
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
	#if ‘if’ condition satisfy
	print("Given character”, ch ,”is vowel")
else: 
#if ‘if’ condition does not satisfy the condition
	print("Given character”,ch, “is  consonant")


