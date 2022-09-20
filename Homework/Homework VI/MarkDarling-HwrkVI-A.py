#===============================================================================
# Mark Darling
# 10-02-17
# COMSC122-0940
# Homework VI-A - Number file handling application that counts the number of
#                 numbers and totals them before yielding an average.
#===============================================================================

# Define main() function.
def main():
    # Initialize loop deciding variable so loop will always execute at least once.
    keep_going = 'y'
    # Keep running the program until the user decides not to.
    while keep_going == 'y' or keep_going == 'Y':
        # Open the text file for reading.
        file_name = input('Enter the name of the file you want to read into memory: ')
        infile = open(file_name,'r')

        # Read the first line into the working variable: number.
        number = int(infile.readline())

        # Make sure to count the first iteration and number being totaled
        total = number
        count = 1

        # Iterate for the remaining number of lines in the text file.
        # For every iteration add 1 to the number of numbers being handled counter.
        # For every iteration add the number read from the line to the running total.
        for line in infile:
            count += 1
            number = int(line)
            total += number

        # Calculate average.
        average = total/count

        # Display results.
        print()
        print('# of lines: \t\t',count)
        print('Total of all numbers: \t',total)
        print('Average of all numbers: ',average)
        print()
        # Give user a choice to keep going or end using the program.
        keep_going = input('Would you like to open another file? [Y/y] or [N/n]: ')
        print()

# Program starts executing here.
main()
