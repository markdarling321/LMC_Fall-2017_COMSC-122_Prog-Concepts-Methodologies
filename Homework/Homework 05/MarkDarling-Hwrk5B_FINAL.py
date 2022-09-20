#INFO===========================================================================

# Mark Darling
# COMSC-122-0940
# Sunday 09-20-17
# Homework 05B - Prime Numbers List
# Description: This program will display all prime numbers from 2 to whatever
#              integer the user puts in as the endpoint.

#INITIALIZE VARIABLES===========================================================

keep_going = 'y'

#FUNCTION DEFINITIONS===========================================================

# define main() function
def main():
    # program title including our name per instructor's request
    print("\n\n\nMark Darling's Prime Number List \n")
    # take the user's input in the form of an integer for the first time
    user_input = int(input("Please enter an integer 2 or greater: "))
    print() # skip a line a single time for output clarity
    # check to make sure the user's input is greater than or equal to 2
    while user_input < 2:
        # if user gives bad input, make them re-enter their input again
        # until they give acceptable input
        user_input = int(input("\nSorry, that is not a valid input,"
                               "please try again: "))

    for num in range(2,(user_input+1),1): # must go to (user_input+1) to account
                                          # for range() default endpoint behavior
        # pass user input to the prime-checking function
        if isprime(num) == True:
            # if prime-checking function returns TRUE:
            print(num," is prime.",sep='')
        # we do NOT want to print the number if it is NOT prime so I commented
        # out the else statement below
        #else:
            # otherwise if prime-checking function returns FALSE:
            #print(num," is NOT prime.",sep='')
    
                     
# define isprime() function
def isprime(number):
    for test in range (2,number,1):
        if (number % test) == 0:
            return False
    return True

#START==========================================================================

# call main() function to start the program and continue until the user says no
while keep_going == 'y':
    main()
    keep_going = input("\nWould you like to print another list of prime "
                       "numbers? Enter [y]/[n]: ")
    
#FINISH=========================================================================

# hold everything on the screen when running from Windows shell
print('\n\nPress ENTER to exit.')
exit = input('')

#END============================================================================
