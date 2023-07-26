# A terminal password manager. 

# TODO
# Create funcs
# Save the password to a username in a dictionary.
# Create a function to display all passwords in the txt file.


import generator


def savePass(password):

    pass_file = open("passwords.txt", "w")

    pass_file.write(password)
    
    print("Your new password has been saved.")

    pass_file.close()


def displayAll():
    # Display the passwords listed in passwords.txt.
    print("Coming soon!")


# Ask whether the user wants to generate a password.
answer = input("Would you like to generate a new pasword? (y/n) ")

if answer.lower() == 'y':

    password = generator.main()
    
    save = input("Would you like to save the password? ")
    
    if save.lower() == 'y':

        savePass(password)

    else:
        
        print("Then we are done here.")

