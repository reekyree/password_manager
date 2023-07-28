# A terminal password manager. 

# TODO
# Create a 'menu' function.
# Create funcs
# Save the password to a username in a dictionary.
# Create a function to display all passwords in the txt file.


import generator, sys


def showMenu():
    print("(1) Generate a new password")
    print("(2) Search Passwords")
    print("(3) Show All Passwords")
    print("(4) Quit Manager")


def savePass(password):

    pass_file = open("passwords.txt", "w")

    pass_file.write(password)
    
    print("Your new password has been saved.")

    pass_file.close()


def displayAll():
    # Display the passwords listed in passwords.txt.
    pass_file = open("passwords.txt", "r")

    print(pass_file.readline())

    pass_file.close()


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
        print()

        action = int(input("What would you like to do? "))
    
        if action == 1:
            generatePass()

        elif action == 3:
            displayAll()
            
        elif action == 4:
            on = False
            quitManager()
        
        else:
            print("Select an action to perform.")


if __name__ == "__main__":
    main()
