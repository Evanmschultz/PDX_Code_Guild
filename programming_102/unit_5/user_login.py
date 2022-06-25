profiles = [
    {
        "username": "gandalfTheGrey", 
        "password": "noneShallPass!"
    },
    {
        "username": "bilboBaggins",
        "password": "theShire123"
    },
    {
        "username": "iAmSmeagol",
        "password": "myPrecious!"
    }
]

def login(username_attempt, password_attempt, profiles):
    for profile in profiles:
        if username_attempt == profile["username"] and password_attempt == profile["password"]:
            return True

    return False

login_attempt = False
attempts = 1

while login_attempt == False:
    username_attempt = input("Please enter your username\n")
    password_attempt = input("Please enter your password\n")

    if login(username_attempt, password_attempt, profiles):
        print(f"Welcome {username_attempt}!")
        exit()
    else:
        print("Error! Your username or password was incorrect!\n")

        if attempts >= 3:
            exit()

        print(f"You have {3-attempts} attempts left..\n")

        attempts += 1
        try_again = input("Type 'yes' if you would like to try again, otherwise type anything\n").lower()

        if try_again == "yes":
            continue
        else:
            break
