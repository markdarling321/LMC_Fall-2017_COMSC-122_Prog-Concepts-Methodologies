#HEADER====================================================================================

# Mark Darling
# COMSC-122-0940
# Sunday 09-10-17
# Homework 04B - Sales Bar Chart
# Description: This program displays a bar chart made of asterisks that correlates to
#              sales values input by the user.
#START=====================================================================================

# program title including our name per instructor's request
print("Mark Darling's Store Sales\n")

# set named constants
END = 0
STEP = -1

# initialize variables
store1 = 0
store2 = 0
store3 = 0
store4 = 0
store5 = 0

#BODY======================================================================================

# take input from user sequentially
store1 = int(input("Enter today's sales for store 1: "))
store2 = int(input("Enter today's sales for store 2: "))
store3 = int(input("Enter today's sales for store 3: "))
store4 = int(input("Enter today's sales for store 4: "))
store5 = int(input("Enter today's sales for store 5: "))

# print BAR CHART header and key
print("\nSALES BAR CHART")
print("Each * = $100")

# Use multiple unique print statements with their own for loops
# because we haven't learned about arrays or otherwise yet
# and I couldn't figure out a better way to do this part.
for name in ['Store 1','Store 2','Store 3','Store 4','Store 5']:
    
    print("\n",name,": ", end='')
    if name == 'Store 1':    
        for i in range(int(store1/100), END, STEP): # First divide the store's sales amount by 100
            print('*', end='')                  # to determine the multiple of loops needed to

    elif name == 'Store 2':                                            # print asterisks. Don't forget to use the
        print("\nStore 2: ", end='')                # int() function to address cases of less than
        for i in range(int(store2/100), END, STEP): # $100.00 in sales. We take single steps in the
            print('*', end='')                  # negative direction until we end at zero. Then
                                                # we move on to the next store in the sequence.
    print("\nStore 3: ", end='')
    for i in range(int(store3/100), END, STEP):
            print('*', end='')
            
    print("\nStore 4: ", end='')
    for i in range(int(store4/100), END, STEP):
            print('*', end='')
            
    print("\nStore 5: ", end='')
    for i in range(int(store5/100), END, STEP):
            print('*', end='')
    
#FOOTER====================================================================================

# hold everything on the screen when running from Windows' shell
print('\n\nPress ENTER to exit.')
exit = input('')

#END=======================================================================================
