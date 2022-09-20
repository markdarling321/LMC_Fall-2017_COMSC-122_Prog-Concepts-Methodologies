# Program 6-32 largest.py
# This program displays the largest integer saved in a file.
def main():

    total = 0
    count = 0
    
    filename = input('Please Enter the Filename desired: ')
    infile = open(filename,'r')

    print()
    
    smallest = float(infile.readline()) # Start by assuming the first number is smallest

    total = smallest
    count = 1

    for line in infile:
        count += 1
        amount = float(line)
        total += amount
        if amount < smallest:       # If subsequent number is smaller, make that the smallest
            smallest = amount
    infile.close()

    print('The smallest number in ',filename,'is',format(smallest,',.2f'))
    print('There are',count,'lines in the file.')
    print('The total of all the numbers on each line is:',int(total))

    exit = input('')
    
main()
