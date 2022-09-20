# This program displays five random numbers in the range of 1 through 100

import random

def main():
    # Take user input
    number_of_rand = int(input("How many random numbers do you want to generate? "))
    lower_bound = int(input("What do you want the lower bound of the random"
                            "numbers to be? "))
    upper_bound = int(input("What do you want the upper bound of the random"
                            "numbers to be? "))

    # Open text file to write random numbers into
    number_file = open('float_numbers.txt','w')
                      
    # Generate specified number of random numbers
    for count in range(number_of_rand):
        # Get a random number.
        number = random.uniform(lower_bound,upper_bound)
        # Display the number in the shell.
        print(number)
        # Write the randomly generated number into the file
        number_file.write(str(number) + '\n')

    # Close the random number file
    number_file.close()

    # Hold the shell open
    input()
    
# Call the main function.
main()
