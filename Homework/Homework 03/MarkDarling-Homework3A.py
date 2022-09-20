# Mark Darling
# COMSC122-0940
# Homework 3A - Magic Date Program
# Description: This program will determine if a given date is a magic date or not.

# START
print("Mark Darling's Magic Date Testing App\n")

# Take the necessary input from the user and store it in appropriate variable types.
day_of_month = int(input("Enter the day of the month as an Integer: "))
month_of_year = int(input("Enter the month of the year as an Integer: "))
year_of_century = int(input("Enter the year of the Century as a two digit Integer: "))

# Determine whether or not the date is a Magic Date.
if (day_of_month * month_of_year) == (year_of_century):
    is_magic = " is a"
else:
    is_magic = " is NOT a"

# Output the final result to the screen.
print("\n",day_of_month,"/",month_of_year,"/",format(year_of_century,'02d'),is_magic," Magic Date.", sep='')

# Hold the output on the screen when run from Windows.
print('\nPress ENTER to exit.')
input('')
# END
