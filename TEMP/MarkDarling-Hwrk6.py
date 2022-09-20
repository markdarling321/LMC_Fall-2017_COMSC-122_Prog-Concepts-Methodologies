#INFO===========================================================================

# Mark Darling
# COMSC-122-0940
# Saturday 09-23-17
# Homework 06 - A Coffee File Management Program
# Description: This is the main driver program that handles the main menu and
#              calls the appropriate functions that reside in the add-on module.

#IMPORT MODULES=================================================================

import DarlingM_coffee_records     # Here's where we import the module we made.

#DEFINE GLOBAL VARIABLES========================================================
                                    # Define GLOBAL CONSTANTS for all choices
ADD_COFFEE_CHOICE    = 1            # [1] ADD_COFFEE
SHOW_COFFEE_CHOICE   = 2            # [2] SHOW_COFFEE
SEARCH_COFFEE_CHOICE = 3            # [3] SEARCH_COFFEE
MODIFY_COFFEE_CHOICE = 4            # [4] MODIFY_COFFEE
DELETE_COFFEE_CHOICE = 5            # [5] DELETE_COFFEE
QUIT_CHOICE          = 6            # [6] QUIT

#DEFINE MAIN()==================================================================

def main():                         # Define main() function.
    choice = 0                      # Initialize menu choice compare variable.
    while choice != QUIT_CHOICE:    # Always come back to main menu and give
        display_menu()              # user a selection choice unless they choose
                                    # to quit.
        choice = int(input('Enter your choice: '))
        if choice == ADD_COFFEE_CHOICE:
            DarlingM_coffee_records.add_coffee()   # Call the add function.
        elif choice == SHOW_COFFEE_CHOICE:
            DarlingM_coffee_records.show_coffee()  # Call the show function.
        elif choice == SEARCH_COFFEE_CHOICE:
            DarlingM_coffee_records.search_coffee()# Call the search function.
        elif choice == MODIFY_COFFEE_CHOICE:
            DarlingM_coffee_records.modify_coffee()# Call the modify function.
        elif choice == DELETE_COFFEE_CHOICE:
            DarlingM_coffee_records.delete_coffee()# Call the delete function.
        elif choice == QUIT_CHOICE:
            print('\nExiting the program...')       # Exit the program.
            input()
        else:
            print('ERROR: invalid selection.')      # Error handling.
            input()
    # PROGRAM ENDS HERE.
    input()
    
#DEFINE DISPLAY_MENU()==========================================================
            
def display_menu():     # Define display_menu() function.
    print()
    print('==========================================')
    print('   MARK Darling COFFEE MANAGEMENT MENU   ')
    print('==========================================')
    print('[1] Add more Coffee Choices to List')
    print('[2] Display all the Coffee Choices')
    print('[3] Search Coffee Choices')
    print('[4] Modify Coffee Choices')
    print('[5] Delete a Coffee Choice')
    print('[6] Quit')
    print()

#BEGIN EXECUTION================================================================

main()                  # Start the execution of the program by calling main().
