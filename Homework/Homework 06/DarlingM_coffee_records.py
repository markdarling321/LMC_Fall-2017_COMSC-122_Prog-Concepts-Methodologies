#INFO===========================================================================

# Mark Darling
# COMSC-122-0940
# Saturday 09-23-17
# Homework 06 - A Coffee File Management Program
# Description: This is the module that holds the various menu choice functions.

#===============================================================================
# This function adds coffee inventory records to the coffee.txt file.

def add_coffee():

    print()
    print('===========================================')
    print('  [1] Add more Coffee Choices to the List  ')
    print('===========================================')
    
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt','a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data: ')
        print()
        descr = input('Description: ')
        qty = float(input('Quantity (in pounds): '))

        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add another record to the file.
        #
        print()
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')
        print()

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

#===============================================================================  
# This function displays the records in the coffee.txt file.

def show_coffee():

    print()
    print('======================================')
    print('  [2] Display all the Coffee Choices  ')
    print('======================================')
    print()
    
    # Open the coffee.txt file for reading.
    coffee_file = open('coffee.txt','r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print('Description:',descr)
        print('Quantity:',qty)

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

#===============================================================================
# This function allows the user to search the coffee.txt file for records
# matching a description.

def search_coffee():

    print()
    print('=============================')
    print('  [3] Search Coffee Choices  ')
    print('=============================')
    print()
    
    # Create a bool varible to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a description to search for: ')

    # Open the coffee.txt file.
    coffee_file = open('coffee.txt','r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Determine whether this record matches the search value.
        if descr == search:
            # Display the record.
            print()
            print('Description:',descr)
            print('Quantity:',qty)
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

    # If the search value was not found in the file display a message.
    if not found:
        print('ERROR: That item was not found in the file.')

#===============================================================================
# This function allows the user to modify the quantity in a record in the
# coffee.txt file.

def modify_coffee():

    print()
    print('=============================')
    print('  [4] Modify Coffee Choices  ')
    print('=============================')
    print()
    
    import os   # Needed for the remove and rename functions

    # Create a bool variable to use as a flag.
    found = False

    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_qty = float(input('Enter the new quantity: '))

    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt','r')

    # Open the temporary file.
    temp_file = open('temp.txt','w')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file, or the new record
        # if this is the one that is to be modified.
        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt','coffee.txt')

    # If the search value was not found in the file display a message.
    if found:
        print()
        print('The file has been updated.')
    else:
        print()
        print('That item was not found in the file.')

#===============================================================================
# This function allows the user to delete a record in the cofee.txt file.

def delete_coffee():

    print()
    print('==============================')
    print('  [5] Delete a Coffee Choice  ')
    print('==============================')
    print()
    
    import os   # Needed for the remove and rename functions

    # Create a bool variable to use as a flag.
    found = False

    # Get the coffee to delete.
    search = input('Which coffee do you want to delete? ')

    # Open the original coffee.txt file.
    coffee_file = open('coffee.txt','r')

    # Open the temporary file.
    temp_file = open('temp.txt','w')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # If this is not the record to delete, then write it to the
        # temporary file.
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the coffee file and the temporary file.
    coffee_file.close()
    temp_file.close()

    # Delete the original coffee.txt file.
    os.remove('coffee.txt')

    # Rename the temporary file.
    os.rename('temp.txt','coffee.txt')

    # If the search value was not found in the file display a message.
    if found:
        print()
        print('The file has been updated.')
    else:
        print()
        print('That item was not found in the file.')
    
#===============================================================================
