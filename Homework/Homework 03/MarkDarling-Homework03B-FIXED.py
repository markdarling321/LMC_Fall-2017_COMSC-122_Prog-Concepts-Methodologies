# HEADER===================================================================================

# Mark Darling
# COMSC122-0940
# Homework 3B - Magic Date Program
# Description: This program will determine if a given date is valid first
#              and then whether it is also a magic date or not.

# START====================================================================================

print("Mark Darling's Magic Date Validation App\n")

# INPUT====================================================================================
# Take the necessary input from the user and store it in appropriate variable types.

day_of_month = int(input("Enter the day of the month as an Integer: "))
month_of_year = int(input("Enter the month of the year as an Integer: "))
year_of_century = int(input("Enter the year of the Century as a two digit Integer: "))

# COMPUTATIONS=============================================================================
# Determine if the date input by the user is a valid date.

# First make sure the given inputs entered are within general valid ranges for each.
# We will narrow down the details more specifically next.

if (
    ( (year_of_century) >= 00 and (year_of_century) <= 99 )
    and
    ( (month_of_year) >= 1 and (month_of_year) <= 12 )
    and
    ( (day_of_month) >= 1 and (day_of_month) <= 31 )
    ):
    
###########################################################################################
    # February is a special case and needs additional checks.

    if ((month_of_year) == 2):
        # First we need to check the year to find out if it is a leap year or not
        # before we know how many days to check for in the month.
        print("DEBUG: MoY == 2")

        # If it is a leap year, there should be 29 days or less in the month.
        if (((year_of_century%4) == 0) and (day_of_month <= 29)):
            print("DEBUG: YoC % 4 == 0 and DoM <= 29")
            is_valid = True
            
        # Otherwise if it is not a leap year, there should only be 28 days or less in the month.
        elif (((year_of_century%4) != 0) and (day_of_month <= 28)):
            print("DEBUG: YoC % 4 != 0 and DoM <= 28")
            is_valid = True
            
        # This is needed to define is_valid for later use in the event that a bad February date
        # is given as the input. Such as 29/2/58.
        else:
            print("DEBUG: is_valid = FALSE during February checks")
            is_valid = False
            
###########################################################################################    

    # Now we can proceed to determine if the day entered is valid based on the month given.

    elif (month_of_year)== 1 and (day_of_month) <=31: # JANUARY
        is_valid = True
    elif (month_of_year)== 3 and (day_of_month) <=31: # MARCH
        is_valid = True
    elif (month_of_year)== 4 and (day_of_month) <=30: # APRIL
        is_valid = True
    elif (month_of_year)== 5 and (day_of_month) <=31: # MAY
        is_valid = True
    elif (month_of_year)== 6 and (day_of_month) <=30: # JUNE
        is_valid = True
    elif (month_of_year)== 7 and (day_of_month) <=31: # JULY
        is_valid = True
    elif (month_of_year)== 8 and (day_of_month) <=31: # AUGUST
        is_valid = True
    elif (month_of_year)== 9 and (day_of_month) <=30: # SEPTEMBER
        is_valid = True
    elif (month_of_year)== 10 and (day_of_month) <=31: # OCTOBER
        is_valid = True
    elif (month_of_year)== 11 and (day_of_month) <=30: # NOVEMBER
        is_valid = True
    elif (month_of_year)== 12 and (day_of_month) <=31: # DECEMBER
        is_valid = True

    # Day given does not correspond to month given.
    else:
        is_valid = False
        print('\nThe given day of the month is INVALID based on the month.')

# Initial broad check failed.
else:
    is_valid = False
    print('\nOne or more of the given values does not fall within accepted ranges.')

# OUTPUT===================================================================================
if is_valid == True:

    # Determine whether or not the date is a Magic Date.
    if (day_of_month * month_of_year) == (year_of_century):
        is_magic = " is a"
    else:
        is_magic = " is NOT a"
        
    # Output the final result to the screen.
    print("\n",day_of_month,"/",month_of_year,"/",format(year_of_century,'02d'),is_magic," Magic Date.",sep='')

elif is_valid == False:
    print('The date entered was determined to NOT be a valid date!')
    
# FOOTER===================================================================================

# Hold the output on the screen when run from Windows.
print('\nPress ENTER to exit.')
input('')

# END======================================================================================
