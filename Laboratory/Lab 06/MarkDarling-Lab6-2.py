# This program displays five random numbers in the range of 1 through 100

import random

def main():
    
    # Open text file to write random numbers into
    number_file = open('numbers.txt','r')
                      
    # Initialize an accumulator
    total = 0
    count = 0
    
    #while number_file.read() != '':
    for line in number_file:
        total += int(line)
        count += 1
    print(total/count)
    input()
    
    
    # Close the random number file
    number_file.close()

    # Hold the shell open
    input()
    
# Call the main function.
main()
