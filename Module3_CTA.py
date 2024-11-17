#
#Sami Case
#CSC500 Module 3 Critical Thinking Activity
#Created: October 25, 2024

#Assignment Prompt
#-------------------
# Creating Python Programs
# Part 1:
# Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total price.

# Part 2:
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on a 24-hour clock when the alarm goes off.

# Source Code:
# -------------------

#Part 1

import math

#Ask the user for the food charge.
food_total = float(input('Enter the total amount for food charges:'))

#Calculate tax & tip
tax_rate = 0.07 #Tax rate is 7%.
tip_rate = float(input('What percentage (%) would you like to tip for service?'))/100 #User can decide how much to tip. In this ex., 18%.

tax = math.ceil(food_total * tax_rate * 100.0)/100.0 #You can't have a fraction of a cent, so this allows us to always round up to the 100th place.
tip = math.ceil(food_total * tip_rate * 100.0)/100.0 #You can't have a fraction of a cent, so this allows us to always round up to the 100th place.

#Calculate
total_charge = food_total + tax + tip

print('Food Total:        ${:.2f}'.format(food_total))
print('Sales Tax ({:.0f}%):    ${:.2f}'.format(tax_rate*100,tax))
print('Service Tip ({:.0f}%): ${:.2f}'.format(tip_rate*100,tip))
print('__________________________')
print('Total Charge:      ${:.2f}'.format(total_charge))

print('\nThank you!')

#Part 2

# Ask the user for the current time (in hours on a 24-hour clock)
current_time = int(input("Enter the current time (in hours on a 24-hour clock): "))

# Ask the user for the number of hours to wait until the alarm goes off
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time the alarm will go off
alarm_time = (current_time + wait_hours) % 24

# Output the result
print('The time when the alarm goes off will be: {}'.format(alarm_time))
