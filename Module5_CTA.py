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
