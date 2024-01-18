# A terminal password manager. 

# TODO
# Save the password to a username in a dictionary.
# Password variable continues to store old pass after save.
# Even when variable is cleared, the same letters get reused.
# Add a username search function.

import generator, sys


def showMenu():
    print("(1) Generate a new password")
    print("(2) Create a username/password combo")
    print("(3) Search Passwords")
    print("(4) Show All Passwords")
    print("(5) Quit Manager")
    print()


    #def savePass(password):

    #pass_file = open("passwords.txt", "a")

    #pass_file.write(password + "\n")
    
    #print("Your new password has been saved.")

    #pass_file.close()


def displayAll():
    # Display the passwords listed in passwords.txt.
    pass_file = open("passwords.txt", "r")
    
    
    # print(pass_file.readline())
    for line in pass_file:
        print(line)

    pass_file.close()


def createUsername():
    newPair = {}
    username = input("Enter a new username: ")
    # Add username into newPair dictionary
    password = input("Would you like to generate a new password? (y/n): ")
    if password.lower() == 'y':
        password = generator.main()
        # Add password to newPair dictionary
    elif password.lower() == 'n':
        password = input("Enter your new password now: ")
        # Add password to newPair dictionary
    
    # Open the password file and write the pair to the file    
    pass_file = open("passwords.txt", "a")
    
    # Add pair to the dictionary
    newPair[username] = password
    
    for key, value in newPair.items():
        pass_file.write('%s:%s\n' % (key, value))
        



def searchPasswords():
    #print("Coming soon!")
    pass_file = open("passwords.txt", "r")
    


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
            password = generatePass()
            print()
            save = input("Would you like to save this password? (y/n): ")
            if save.lower() == 'y':
                savePass(password)
                password = ''
            else:
                print("Password not saved.")
            print()

        elif action == 2:
            createUsername()
            print()

        elif action == 3:
            searchPasswords()
            print()

        elif action == 4:
            displayAll()
            print()
            
        elif action == 5:
            on = False
            quitManager()
        
        else:
            print("Select an action to perform.")


if __name__ == "__main__":
    main()
