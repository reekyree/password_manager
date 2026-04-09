# This program generates a password
# using alphanumeric characters.
# The user can specify the number of characters used.

# TODO
# getLength needs error handling for non int and 0 inputs.
# addChar needs error handling for non int
# addSpecial needs handling for non int
# Specified password length does not output according to length limit if the user
# enters more characters than initially specified.


import secrets, string, random # Keeping random so program doesn't break for now, switching to secrets and will be dropping random module entirely once changes are made

# password variable is global, move it to local
 

def createPass():
    
    password = []

    # Update this function to be createPass()
    # Get the password length.
    while True:
        try: 
            length = int(input("Password length (number): "))
        except ValueError:
            print("Please enter a valid number.")
    
        # Get # of integers in password
        try:
            amtInt = int(input("Min. # of integers (0 if none): "))
            if amtInt > 0:
                digits = string.digits
                intpass = secrets.choice(digits)
            else:
                print("You are adding (0) numbers.")
        except ValueError:
            print("Please enter a valid number.")

        # Get # of alphabetic characters in password 
        try: 
            amtAlpha = int(input("Min. # of letters (0 if none): "))
            if amtAlpha > 0:
                alphabet = string.ascii_letters
                alphapass = secrets.choice(alphabet)
            else:
                print("You are adding (0) numbers.")
        except ValueError:
            print("Please enter a valid number.")
    
        # Get # of special characters 
        try:
            addSpecial = int(input("Min. # of special characters (0 if none): "))
            if addSpecial > 0:
                special = secrets.choice(string.punctuation)
                password.append(special)
            else:
                print("You are adding (0) special characters.")
        except ValueError:
            print("Please enter a valid number.")

    while len(password) < length:
        char = secrets.choice(string.ascii_letters)
        password.append(char)

    passString = ''.join(str(i) for i in password)

    return passString



    #def shufflePass(password):
    # Randomize the password.
    #secrets.SystemRandom().shuffle(password)

    #def displayPass(password):
    # Display the password in a non-list format.
    #for char in password:
    #print(char, end='')


def main():

    # This logic needs to be changed to reflect the removal of the other functions 

    password = createPass()

    #shufflePass(password)

    #displayPass(password)
    
    print(password)

if __name__ == "__main__":
    main()
    
