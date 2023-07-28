# A terminal password manager. 

# TODO
# Create a 'menu' function.
# Create funcs
# Save the password to a username in a dictionary.
# Create a function to display all passwords in the txt file.


import generator, sys


def showMenu():
    print("(1) Generate a new password")
    print("(2) ")


def savePass(password):

    pass_file = open("passwords.txt", "w")

    pass_file.write(password)
    
    print("Your new password has been saved.")

    pass_file.close()


def displayAll():
    # Display the passwords listed in passwords.txt.
    print("Coming soon!")

def generatePass():

    password = generator.main()
    return password

def quitManager():
    sys.exit()
    
def main():

    # Main program function
    on = True

    while on:
        showMenu()

        action = input("What would you like to do? ")

        if action == 1:
            generatePass()




