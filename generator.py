# This program generates a password
# using alphanumeric characters.
# The user can specify the number of characters used.

# TODO
# getLength needs error handling for non int and 0 inputs.
# addChar needs error handling for non int
# addSpecial needs handling for non int
# Specified password length does not output according to length limit if the user
# enters more characters than initially specified.
# 

import secrets, string, random # Keeping random so program doesn't break for now, switching to secrets
from random import shuffle # This lets you randomize a list

password = [] 

def getLength():
    # Get the password length.

    length = int(input("Password length (number): "))
    return length

def addChar(password):
    # Counter variable no longer necessary
    
    #counter = 0

    # Get # of integers in password
    amtInt = int(input("Min. # of integers (0 if none): "))
    if amtInt > 0:
        digits = string.digits
        intpass = secrets.choice(digits)
    else:
        print("You are adding (0) numbers.")

    # Get # of alphabetic characters in password 
    amtAlpha = int(input("Min. # of letters (0 if none): "))
    if amtAlpha > 0:
        alphabet = string.ascii_letters
        alphapass = secrets.choice(alphabet)
    else:
        print("You are adding (0) numbers.")

    #if addNums > 0:
    #while counter < addNums:
    #password.append(random.randint(0, 9))
    #counter += 1
    #else:
    #print("You are adding (0) numbers.")

def addSpecial(password):

    counter = 0
    addSpecial = int(input("Min. # of special characters (0 if none): "))
    if addSpecial > 0:
        special = secrets.choice(string.punctuation)
        password.append(special)
    else:
        print("You are adding (0) special characters.")


def createPass(password, length):
    # Create a password based on the length entered by the user.

    while len(password) < length:
        char = random.choice(string.ascii_letters)
        password.append(char)


def shufflePass(password):
    # Randomize the password.
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password)

def displayPass(password):
    # Display the password in a non-list format.
    for char in password:
        print(char, end='')


def main():

    length = getLength()

    createPass(password, length)

    addChar(password)

    addSpecial(password)

    shufflePass(password)

    displayPass(password)

    passString = ''.join(str(i) for i in password)

    return passString 


if __name__ == "__main__":
    main()
    
