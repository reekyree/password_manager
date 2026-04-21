# This program generates a password
# using alphanumeric characters.
# The user can specify the number of characters used.

# TODO
# Ask user to specifiy desired # of alpha, digits, and special
# Show user password character length after getting parameters
# Create password based on parameters
# Display password in non-list format

import secrets, string, sys   

def createPass():
   
    # Starting variables
    password = []
    alpha = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    total_alpha = 0
    total_digits = 0
    total_special = 0

    while True:
        try:
            total_alpha = int(input("# of letters: "))
        except ValueError:
            print("Enter a valid number.")

        total_digits = int(input("# of digits: "))
        total_special = int(input("# of special: "))
        length = total_alpha + total_digits + total_special
        choice = input(f"password will be {length} characters long. y/n: ")

        if choice.lower() == 'y':

            while len(password) < length:
                add_alpha = secrets.choice(alpha)
                password.append(add_alpha)
   
    # shuffle password (replaces shufflePass func) 
    secrets.SystemRandom().shuffle(password)
    
    return password
        
def displayPass(password):
    # Display the password in a non-list format.
    for char in password:
        print(char, end='')

def main():
    # This logic needs to be changed to reflect the removal of the other functions 
    password = createPass()
    displayPass(password)

if __name__ == "__main__":
    main()
