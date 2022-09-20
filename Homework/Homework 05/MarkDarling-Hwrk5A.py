#INFO===========================================================================

# Mark Darling
# COMSC-122-0940
# Sunday 09-20-17
# Homework 05A - Prime Numbers Function
# Description: This boolean function takes an integer as an argument and returns
#               true if the argument is a prime number, or false otherwise.

#INITIALIZE VARIABLES===========================================================

keep_going = 'y'

#FUNCTION DEFINITIONS===========================================================

# define main() function
def main():
    # program title including our name per instructor's request
    print("\n\n\nMark Darling's Prime Number Checker \n")
    # take the user's input in the form of an integer for the first time
    user_input = int(input("Please enter an integer 2 or greater: "))
    # check to make sure the user's input is greater than or equal to 2
    while user_input < 2:
        # if user gives bad input, make them re-enter their input again
        # until they give acceptable input
        user_input = int(input("\nSorry, that is not a valid input,"
                               "please try again: "))
    # pass user input to the prime-checking function
    if isprime(user_input) == True:
        # if prime-checking function returns TRUE:
        print("\n",user_input," is prime.\n",sep='')
    else:
        # otherwise if prime-checking function returns FALSE:
        print("\n",user_input," is NOT prime.\n",sep='')
    
                     
# define isprime() function
def isprime(number):
    if number == 2 or number == 3:      # 2 is a unique case and always prime
        return True                     # 3 is also included here because of
                                        # my testing method below and because
                                        # the range() function only counts to
                                        # (number-1) by default
    
    elif number % 2 == 0:               # all other even numbers are NOT prime
        return False

    else:                               # now we check any odd numbers given
        for test in range(3,number,1):  # odd numbers are never divisible by 2
            if number % test == 0:      # check to see if number divides evenly
                return False            # if evenly divisible, number NOT prime
            else:
                return True
            #print (test)             # DEBUG: check for loop range for accuracy

#START==========================================================================

# call main() function to start the program and continue until the user says no
while keep_going == 'y':
    main()
    keep_going = input("Would you like to test another number to see if it is "
                       "prime? Enter [y]/[n]: ")
    
#FINISH=========================================================================

# hold everything on the screen when running from Windows shell
print('\n\nPress ENTER to exit.')
exit = input('')

#END============================================================================
