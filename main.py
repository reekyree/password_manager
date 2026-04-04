# A terminal password manager. 

# TODO
# Test all functions.
# Password variable continues to store old pass after save. *Note* this is likely due to the random library and its limitations.
# Program needs to search computer for master password file. A "vault" so to speak.
# Add a username search function.
# Lacks encryption, use cryptopgraphy library 

import generator, sys, json


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
    with open("passwords.json", "r") as pass_file:
        data = json.load(pass_file)
         
    for k, v in data.items():
        print(f"{k} : {v}")

def createItem():
    newPair = {}
    itemName = input("Enter item name: ")
    # Add username into newPair dictionary
    password = input("Would you like to generate a new password? (y/n): ")
    if password.lower() == 'y':
        password = generator.main()
        # Add password to newPair dictionary
    elif password.lower() == 'n':
        password = input("Enter your new password now: ")
        # Add password to newPair dictionary
    
    # Add pair to the dictionary
    newPair[itemName] = password
   
    # Write the new pair to the file 
    #for key, value in newPair.items():
    #pass_file.write('%s:%s\n' % (key, value))

    # Open the password file     
    with open("passwords.json", "w") as pass_file:
        json.dump(newPair, pass_file)

    # Close the file 
    pass_file.close()
        

# I think this fucntion needs to be able to search the repo or the computer
# to find the file it needs. If the file doesn't exist, it can't be called.

def searchPasswords():
    print("Coming soon!")
    #pass_file = open("passwords.txt", "r")
    
    
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
            createItem()
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
