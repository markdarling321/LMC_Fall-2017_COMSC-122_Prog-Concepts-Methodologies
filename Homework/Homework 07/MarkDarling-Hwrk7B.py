# COMSC-122-0940
# Wednesday 10-11-17
# Homework 07B - Bay Area Annual Rainfall Data Processor.
# Description:   This program processes a rain data file and then outputs relevant data.

def main():

##########################################################################################

    # Initialize while loop control variable to ensure while loop iterates
    # at least once.
    keep_going = 'y'

    # If any exceptions are raised, give the user another chance to re-enter
    # the file name without having to completely restart the program.
    while keep_going == 'y' or keep_going == 'Y':

        err_flag = False
        
        # Allow user to specify the file name containing rainfall data to be
        # processed into memory. Include exception handling as well.
        try:

            RainData_file = input("\nPlease enter the name of the file containing " +
                                  "the RAINFALL DATA: ")

            # Open both files for processing.
            RainData_infile = open(RainData_file,'r')
            Months_infile = open('months.txt','r')

            # Process the files' contents into respective lists.
            RainData_list = RainData_infile.readlines()
            Months_list = Months_infile.readlines()

            # Strip the \n from each element in both lists.
            index = 0
            while index < len(RainData_list):
                RainData_list[index] = RainData_list[index].rstrip('\n')
                index += 1

            index = 0
            while index < len(Months_list):
                Months_list[index] = Months_list[index].rstrip('\n')
                index += 1

            # Convert all elements for RainData_list to floats.
            index = 0
            while index < len(RainData_list):
                RainData_list[index] = float(RainData_list[index])
                index += 1
            
            # DEBUG BLOCK:
            # Display on screen the contents of each list after being read into memory.
            #print()
            #print(RainData_list)
            #input()
            #
            #print()
            #print(Months_list)
            #input()

            # Close the files now that their contents are in working memory.
            RainData_infile.close()
            Months_infile.close()

            # If file name is taken from user and contents processed with no
            # exceptions raised, exit the loop after one iteration.
            keep_going = 'n'
            
        # File Not Found Error.
        except FileNotFoundError as fnf_err:
            print()
            print('ERROR: File does not exist!')
            print('ERROR:',fnf_err)
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
                
        # Catch all for any other exceptions.
        except:
            print()
            print('ERROR: An unknown error occured.')
            print()
            err_flag = True
            keep_going = input('Would you like to try again? [Y/y] or [N/n]: ')
            print()
            
##########################################################################################

    # Initialize the while loop control variable again for the second (independent)
    # while loop iteration that needs to be used.
    keep_going = 'y'

    # The err_flag flag allows the user to try multiple times, or exit the file
    # name input section after a bad file name that raises an exception without
    # proceeding unnecessarily into the rest of the program and causing it to
    # crash due to lack of proper input parameters.
    while (err_flag == False) and (keep_going == 'y' or keep_going == 'Y'):
        
        # Calculate the total rainfall and then display the result.
        index = 0
        total_rainfall = 0
        while index < len(RainData_list):
            total_rainfall += RainData_list[index]
            index += 1
        print()
        print('The TOTAL rainfall (in inches) for the year is: ' +
              '\t',format(total_rainfall,',.2f'))

        # Calculate the average rainfall and display the result.
        avg_rainfall = total_rainfall / 12
        print()
        print('The AVERAGE rainfall (in inches) for the year is: ' +
              '\t',format(avg_rainfall,',.2f'))

        # Determine the month with the maximum rainfall:
        index = 0
        temp = -1
        while index < len(RainData_list) and temp != max(RainData_list):
            temp = RainData_list[index]
            index += 1
        print()
        print('The MONTH with the MAXIMUM rainfall is:\t\t\t',Months_list[index-1],'\n' +
              Months_list[index-1],"'s rainfall (in inches) was:\t\t\t\t" +
              format(max(RainData_list),',.2f'))

        # Determine the month with the minimum rainfall:
        index = 0
        temp = -1
        while index < len(RainData_list) and temp != min(RainData_list):
            temp = RainData_list[index]
            index += 1
        print()
        print('The MONTH with the MINIMUM rainfall is:\t\t\t',Months_list[index-1],'\n' +
              Months_list[index-1],"'s rainfall (in inches) was:\t\t\t\t" +
              format(min(RainData_list),',.2f'))
        
        # Exit the loop after a successful iteration.
        keep_going = 'n'
    
##########################################################################################

# Program begins executing here.
main()

# Hold the screen open if being run from Windows shell.
exit = input('\nPress ENTER to exit.')
