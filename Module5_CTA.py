#
#Sami Case
#CSC500 Module 5 Critical Thinking Activity
#Created: November 1, 2024

#Assignment Prompt
#-------------------
# Creating Python Programs
# Part 1:
# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# Part 2:
# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

#Source Code:
#-------------------


# Part 1

years = int(input('Enter number of years: '))

count_month = 0
total_rainfall = 0
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for year in range(years):
    for month in range(12):
        monthly_rain = int(input('Enter inches of rainfall for Year {} {}: '.format(year + 1, months[month])))
        total_rainfall += monthly_rain
        count_month += 1
    print()  # New line after each year for readability

avg_rainfall = total_rainfall / count_month
print('\nNumber of months: {}'.format(count_month))
print('Total rainfall: {} inches'.format(total_rainfall))
print('Average rainfall per month: {:.2f} inches\n'.format(avg_rainfall))


# Part 2

books = int(input('Enter number of books purchased this month: '))

if books < 2:
    points = 0
elif 4 > books >= 2:
    points = 5
elif 6 > books >= 4:
    points = 15
elif 8 > books >= 6:
    points = 30
else:
    points = 60

print('Points Awarded: {}'.format(points))
