# The get_logic_name function accepts a first name,
# last name, and IFD number as arguments. It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 charactersm the
    # slice will return the entire first name.
    set1 = first[0:1]
    set1 = set1.lower()

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[:]
    set2 = set2.lower()

    # Get the last three characters of the student ID.
    # If the ID number is less than 3 characters, the
    # slice will return the entire last name.
    set3 = idnumber[-3:]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

def valid_password(password):
    # Set the Boolean variables to false.
    correct_lnegth = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_symbol = False
    has_space = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 8:
        correct_length = True

        # Test each character and set the
        # approipriate flag then a required
        # character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
                #print('has_uppercase = TRUE')
            if ch.islower():
                has_lowercase = True
                #print('has_lowercase = TRUE')
            if ch.isdigit():
                has_digit = True
                #print('has_digit = TRUE')
            if not ch.isalnum():
                has_symbol = True
                #print('has_symbol = TRUE')
            if ch.isspace():
                has_space = True
                #print('has_no_space = TRUE')

        # Determine whether all of the requirements
        # are met. If they are, set is_valid to true.
        # Otherwise, set is_valid to false.
        if correct_length and has_uppercase and \
           has_lowercase and has_digit and \
           has_symbol and not has_space:
            is_valid = True
        else:
            is_valid = False

        # Return the is_valid variable.
        return is_valid
