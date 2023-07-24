# A terminal password manager. 

# TODO
# Create a file to write passwords to.
# Ask the user if they want to save a password.
# Save the password to a username in a dictionary.

import generator

# Ask whether the user wants to generate a password.
answer = input("Would you like to generate a new pasword? (y/n) ")

if answer.lower() == 'y':
    password = generator.main()
else:
    print("Then we are done here.")

