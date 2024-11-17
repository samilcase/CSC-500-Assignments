#
#Sami Case
#CSC500 Module 1 Critical Thinking Activity
#Created: October 5, 2024

#Assignment Prompt
#-------------------
#Creating Python Programs
# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.

# Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.

# Part 2:
# Write a Python program to find the multiplication and division of two numbers.

# Ask the user to input two numbers (num1 and num2). Given those two numbers, multiply them together to find the output. Also, divide num1/num2 to find the output.

# Source Code:
# -------------------

#Part 1

num1 = int(input('Enter integer:\n'))
num2 = int(input('Enter another integer:\n'))

sum = num1 + num2
dif = num1 - num2

print(num1,'+',num2,"is",sum)
print(num1,'-',num2,'is',dif)

#Part 2

num1 = int(input('Enter integer:\n'))
num2 = int(input('Enter another integer:\n'))

prod = num1 * num2
div = num1 / num2

print(num1,'*',num2,"is",prod)
print(num1,'/',num2,'is',div)
