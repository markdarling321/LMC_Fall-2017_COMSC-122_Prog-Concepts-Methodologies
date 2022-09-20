# COMSC-122-0940
# Wednesday 10-11-17
# Homework 07A - Popular names checker.
# Description:   This program asks the user to input a file with names on individual
#                lines and reads them into memory before asking the user what sex and
#                name they would like to search for. It then tells the user whether or
#                not that name is contained in either of the appropriate lists. This
#                program also includes some error handling as well as the option to
#                search as many names as the user desires without having to restart the
#                program from the beginning each time.

def main():

##########################################################################################

    # Initialize while loop control variable to ensure while loop iterates
    # at least once.
    keep_going = 'y'

    # If any exceptions are raised, give the user another chance to re-enter
    # the file names without having to completely restart the program.
    while keep_going == 'y' or keep_going == 'Y':

        err_flag = False
        
        # Allow user to specify the file names to be processed into memory.
        # Include exception handling as well.
        try:

            BoyNames_file = input("\nPlease enter the name of the file containing " +
                                  "BOY NAMES: ")
            # DEBUG:
            #print(BoyNames_file)
                
            GirlNames_file = input("\nPlease enter the name of the file containing " +
                                   "GIRL NAMES: ")
            # DEBUG:
            #print(GirlNames_file)

            # Open both files for processing.
            Boy_infile = open(BoyNames_file,'r')
            Girl_infile = open(GirlNames_file,'r')

            # Process the files' contents into respective lists.
            BoyList = Boy_infile.readlines()
            GirlList = Girl_infile.readlines()

            # Strip the \n from each element in both lists.
            index = 0
            while index < len(BoyList):
                BoyList[index] = BoyList[index].rstrip('\n')
                index += 1

            index = 0
            while index < len(GirlList):
                GirlList[index] = GirlList[index].rstrip('\n')
                index += 1
            
            # DEBUG BLOCK:
            # Display on screen the contents of each list after being read into memory.
            #print()
            #print(BoyList)
            #input()
            #
            #print()
            #print(GirlList)
            #input()

            # Close the files now that their contents are in working memory.
            Boy_infile.close()
            Girl_infile.close()

            # If both file names are taken from user and no exceptions raised,
            # exit the loop after one iteration.
            keep_going = 'n'
            
        # File Not Found Error.
        except FileNotFoundError as fnf_err:
            print()
            print('ERROR: File does not exist!')
            print('ERROR:',fnf_err)
            print('One or more of the file names entered do not exist!')
            print()
            err_flag = True
            keep_going = input('Would you like to try again? [Y/y] or [N/n]: ')
            print()
                
        # Input / Output Error.
        # Pretty sure this error handler can never be triggered, but I left it in anyways.
        except IOError as io_err:
            print()
            print('ERROR: An IOError occured!')
            print('ERROR:',io_err)
            print()
            err_flag = True
            keep_going = input('Would you like to try again? [Y/y] or [N/n]: ')
            print()
                
        # Mismatching variable types Error.
        # Pretty sure this error handler can never be triggered, but I left it in anyways.
        except ValueError as val_err:
            print()
            print('ERROR: A ValueError occured!')
            print('ERROR:',val_err)
            print()
            err_flag = True
            keep_going = input('Would you like to try again? [Y/y] or [N/n]: ')
            print()
                
        # Catch all for any other exceptions.
        except:
            print()
            print('ERROR: An unknown error occured.')
            print()
            err_flag = True
            keep_going = input('Would you like to try again? [Y/y] or [N/n]: ')
            print()
            
##########################################################################################
            
    # Initialize while loop control variable to ensure while loop iterates
    # at least once.
    keep_going = 'y'

    # Allow user to look up as many names as they would like
    # after the files have been processed first.
    while (keep_going == 'y' or keep_going == 'Y') and (err_flag == False):
            
        # Take user's input to determine the sex of name they want to look up.
        lookup = input("\nIf you are looking up a Girl's name, enter 'G' \n" +
                       "If you are looking up a Boy's name, enter 'B'  \n" +
                       "Which would you like to look up: ")

        # Check user's input to determine which list to compare against
        # for matches. Then check the relevant list to see if it contains
        # the specified name the user is trying to look up in the list.
        if lookup == 'B' or lookup == 'b':
            name = input("\nPlease enter the Boy's name you would like to look up: ")

            if name in BoyList:
                print(name,'was FOUND in the list of popular names.\n')

            else:
                print(name,'was NOT FOUND in the list of popular names.\n')

            keep_going = input('Would you like to look up another name? ' +
                               'Enter [Y/y] or [N/n]: ')

        elif lookup == 'G' or lookup == 'g':
            name = input("\nPlease enter the Girl's name you would like to look up: ")

            if name in GirlList:
                print(name,'was FOUND in the list of popular names.\n')

            else:
                print(name,'was NOT FOUND in the list of popular names.\n')

            keep_going = input('Would you like to look up another name? ' +
                               'Enter [Y/y] or [N/n]: ')
        else:
            print()
            print("ERROR: An unknown error has occured.\n")

            keep_going = input('Would you like to look up another name? ' +
                               'Enter [Y/y] or [N/n]: ')
        
##########################################################################################

# Program begins executing here.
main()

# Hold the screen open if being run from Windows shell.
exit = input('\nPress ENTER to exit.')
