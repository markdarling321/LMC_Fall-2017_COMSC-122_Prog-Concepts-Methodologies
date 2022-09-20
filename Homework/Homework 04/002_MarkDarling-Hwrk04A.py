#HEADER====================================================================================

# Mark Darling
# COMSC-122-0940
# Sunday 09-10-17
# Homework 04A - Grading Program
# Description: This program gets a numeric score from the user and displays the
#              corresponding letter grade.

#START=====================================================================================

print("Mark Darling's Grading Program")

# constants for comparing
MAX_SCORE = 100
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
MIN_SCORE = 0

# initialize these variables before using them
score = 0        # set this to zero so it is within valid range but not giving away free
                 # points in the event of a logic error
                 
keep_going = 'y' # set this to 'y' to satisfy the first while loop on its first iteration

#BODY======================================================================================

# as long as the user enters 'y' when prompted, keep taking input from user
while keep_going == 'y':
    score = int(input('\nEnter your test score: ')) # give user a chance to enter a score
    
    if score < MIN_SCORE or score > MAX_SCORE:  # disallow extraneous score values
        print('Test score is not within allowed range, please re-enter test score.')
        score = int(input('\nEnter your test score: ')) # give user a chance to change an
                                                        # extraneous input so the program
                                                        # can proceed
    while score >= MIN_SCORE and score <= MAX_SCORE and keep_going == 'y':    

        if score >= A_SCORE:
            print('Your grade is A.')
        elif score >= B_SCORE:
            print('Your grade is B.')
        elif score >= C_SCORE:
            print('Your grade is C.')
        elif score >= D_SCORE:
            print('Your grade is D.')
        else:
            print('Your grade is F.')

        keep_going = input('\nWould you like to convert another quiz score to a letter \
grade? \nEnter "y" to continue or "n" to stop: ')

#FOOTER====================================================================================

print('\nPress ENTER to exit.')
exit = input('')

#END=======================================================================================
