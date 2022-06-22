"""
Evan Schultz
Programming 101
Unit 5 Lab
"""
import random
import string

"""
Edge cases:
input can't be turned into an (int)
input not long enough or too long
# not edge cases, but necessary check
    what type of characters the user wants in their passwords
    minimum amount of each "special" character they want in their password
does the minimum amount they require fit the password length they requested 
    also when the other "special" characters are accounted for
    if they messed up this counting, do they want to restart the program or shut it down
are spaces " " in the beginning or end of the password/s? 
    this will make the passwords harder to copy and use, so avoid that

Refactor still needed:
extra character types questions can be placed in a function to shorten and clean code
add_to_password() function that repeats/shortens code of making sure the minimum of each "special"
    character is actually added to each password... see while loops at end of password_generator()

additional logic that should be added:
yes checker: make sure the string is meant to say "yes" the user wants "x" in their passwords
"""

# all characters the user will be able to pick from
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
space = " "


def password_generator():
    print("Hello, I am your friendly password generator.  Let's get started!\n")
    characters = {"lower_letters": lower_letters}
    min_special_chars = 1 # set to '1' so it will ALWAYS have a lowercase letter in the passwords

    # variables needed for try_accept function below for amount of passwords input
    amount_input = "How many passwords would you like me to generate?\n"
    error_1 = "I can only make an integer amount of passwords!\n"
    error_2 = "I need to make you at least 1 password!\n"

    # function to make sure the user won't break the program with bad inputs
    amount = try_except(amount_input, error_1, error_2)

    # same as amount above, but for length
    length_input = "How many characters would you like your passwords to be?\n"
    error_1 = "I can only make passwords of an integer length!\n"
    min_input = 4
    error_2 = f"I need to make your password/s at least '{min_input}' character in length.\n"

    length = try_except(length_input, error_1, error_2, min_input)

    """
    all if statements below add addtional characters for possible use in passwords
    """
    upper_case = input("\nWould you like me to add uppercase letters, write, 'yes' or 'no'.\n").lower()
    upper_chars = False
    if upper_case == "yes":
        char_count_message = "What is the minimum amount of these you need me to add?\n"
        error_1 = "I can only add an integer number amount of characters!\n"
        error_2 = "I need to add at least 1 of these characters if you want them in the passwords!\n"

        char_count_upper = try_except(char_count_message, error_1, error_2)

        while min_special_chars + char_count_upper > length:
            print("That is too many of those characters for these passwords!\n")
            response = input("Would you like to restart me, continue, or exit? Reply with: 'restart', 'continue', or 'no'\n").title()
            if response == "Restart":
                password_generator()
            elif response == "Continue":
                char_count_upper = try_except(char_count_message, error_1, error_2)
            else:
                print("\nOk, thank you for using me as your password generator.  See you again soon!")
                exit()

        upper_chars = True
        characters["upper_letters"] = upper_letters
        min_special_chars += char_count_upper

    numbers = input("\nWould you like me to add numbers in your?\n")
    number_chars = False
    if numbers == "yes":
        char_count_message = "What is the minimum amount of these you need me to add?\n"
        error_1 = "I can only add an integer number amount of characters!\n"
        error_2 = "I need to add at least 1 of these characters if you want them in the passwords!\n"

        char_count_numbers = try_except(char_count_message, error_1, error_2)

        while min_special_chars + char_count_numbers > length:
            print("That is too many of those characters for these passwords!\n")
            response = input("Would you like to restart me, continue, or exit? Reply with: 'restart', 'continue', or 'no'\n").title()
            if response == "Restart":
                password_generator()
            elif response == "Continue":
                char_count_numbers = try_except(char_count_message, error_1, error_2)
            else:
                print("\nOk, thank you for using me as your password generator.  See you again soon!")
                exit()

        number_chars = True
        characters["digits"] = digits
        min_special_chars += char_count_numbers
    
    special_characters = input("\nWould you like me to add special characters to your passwords?\n")
    punctuation_chars = False
    if special_characters == "yes":
        char_count_message = "What is the minimum amount of these you need me to add?\n"
        error_1 = "I can only add an integer number amount of characters!\n"
        error_2 = "I need to add at least 1 of these characters if you want them in the passwords!\n"

        char_count_punctuation = try_except(char_count_message, error_1, error_2)

        while min_special_chars + char_count_punctuation > length:
            print("That is too many of those characters for these passwords!\n")
            response = input("Would you like to restart me, continue, or exit? Reply with: 'restart', 'continue', or 'no'\n").title()
            if response == "Restart":
                password_generator()
            elif response == "Continue":
                char_count_punctuation = try_except(char_count_message, error_1, error_2)
            else:
                print("\nOk, thank you for using me as your password generator.  See you again soon!")
                exit()

        punctuation_chars = True
        characters["punctuation"] = punctuation
        min_special_chars += char_count_punctuation

    spaces = input("\nWould you like me to add spaces ' ' to your passwords?\n")
    space_chars = False
    if spaces == "yes":
        char_count_message = "What is the minimum amount of these you need me to add?\n"
        error_1 = "I can only add an integer number amount of characters!\n"
        error_2 = "I need to add at least 1 of these characters if you want them in the passwords!\n"

        char_count_space = try_except(char_count_message, error_1, error_2)

        while min_special_chars + char_count_space > length:
            print("That is too many of those characters for these passwords!\n")
            response = input("Would you like to restart me, continue, or exit? Reply with: 'restart', 'continue', or 'no'\n").title()
            if response == "Restart":
                password_generator()
            elif response == "Continue":
                char_count_space = try_except(char_count_message, error_1, error_2)
            else:
                print("\nOk, thank you for using me as your password generator.  See you again soon!")
                exit()
            
        space_chars = True
        characters["space"] = space
        print(characters["space"])
        min_special_chars += char_count_space

    # passwords = [] # simply adds functionality for possible future uses if this function needs to return a list

    for i in range(amount):
        password = [random.choice(characters["lower_letters"])]
     
        while upper_chars:
            for i in range(char_count_upper):
                password += random.choice(characters["upper_letters"])
            break

        while number_chars:
            for i in range(char_count_numbers):
                password += random.choice(characters["digits"])
            break

        while punctuation_chars:
            for i in range(char_count_punctuation):
                password += random.choice(characters["punctuation"])
            break

        while space_chars:
            for i in range(char_count_space):
                password += random.choice(characters["space"])
            break
        
        while len(password) < length:
            key = random.choice(list(characters.keys()))
            password += characters[key][random.randint(0, len(characters[key]) - 1)]

            if password.count(" ") > len(password) - 2:
                password.pop(password.index(" "))
                continue

        split = [character for character in password]
        random.shuffle(split)

        if space_chars:
            while split[0] == " " or split[-1] == " ":
                random.shuffle(split)

        password = "".join(split)

        print(password)
        # passwords.append(password) # for future possbile uses


    more_passwords = input("\n\nWould you like me to make you more passwords? Write 'yes' or 'no'.\n")
    if more_passwords == "yes":
        password_generator()
    
    # return passwords # simply adds functionality for possible future uses if this function needs to return a list


def try_except(input_string, error_1, error_2, min_input=1): # this makes sure the user input is usable 
    user_input = input(input_string)
    while user_input is not int: 
        try:
            user_input = int(user_input)
        except:
            print(error_1)
            user_input = input(input_string)
            continue
        if user_input < min_input:
            print(error_2)
            user_input = input(input_string)
            continue

        return user_input

password_generator()

"""
Below is a function to refactor the code into a simpler, more readable format that I haven't gotten to yet.
"""

# def special_char_count_checker(special_chars, min_special_chars, length, char_count_message, error_1, error_2):
#     spaces = input("\nWould you like me to add spaces ' ' to your passwords?\n")
#     space_chars = False
#     if spaces == "yes":
#         char_count_message = "What is the minimum amount of these you need me to add?\n"
#         error_1 = "I can only add an integer number amount of characters!\n"
#         error_2 = "I need to add at least 1 of these characters if you want them in the passwords!\n"

#         char_count_space = try_except(char_count_message, error_1, error_2)

#         while min_special_chars + char_count_space > length:
#             print("That is too many of those characters for these passwords!\n")
#             response = input("Would you like to restart me, continue, or exit? Reply with: 'restart', 'continue', or 'no'\n").title()
#             if response == "Restart":
#                 password_generator()
#             elif response == "Continue":
#                 char_count_space = try_except(char_count_message, error_1, error_2)
#             else:
#                 print("\nOk, thank you for using me as your password generator.  See you again soon!")
#                 exit()
            
#         space_chars = True
#         characters["space"] = space
#         print(characters["space"])
#         min_special_chars += char_count_space

# def add_to_password():
#     while upper_chars:
#             for i in range(char_count_upper):
#                 password += random.choice(characters["upper_letters"])
#             break
