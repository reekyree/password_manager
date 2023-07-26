# A terminal password manager. 

# TODO
# Move save func to the generation side of the if/else statement
# Create funcs
# Create a file to write passwords to.
# Ask the user if they want to save a password.
# Save the password to a username in a dictionary.

import generator

# Ask whether the user wants to generate a password.
answer = input("Would you like to generate a new pasword? (y/n) ")

if answer.lower() == 'y':
    password = generator.main()
    save = input("Would you like to save the password? ")

    if save.lower() == 'y':
        pass_file = open("passwords.txt", "w")
        pass_file.write(password)
        print("Your new password has been saved.")
        pass_file.close()
    else:
        print("Goodbye.")

else:
    print("Then we are done here.")

save = input("Would you like to save the password? ")

if save.lower() == 'y':
    pass_file = open("passwords.txt", "w")
    pass_file.write(password)
    print("Your new password has been saved.")
    pass_file.close()
else:
    print("Goodbye.")



