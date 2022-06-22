"""
Evan Schultz
Programming 101
Unit 4 Lab
"""
import random


list_of_choices = ["Rock", "Paper", "Scissors"]
# all possible non-tieing combinations of user and computer choices
outcomes = {"RockPaper": False, "RockScissors": True, "PaperRock": True, "PaperScissors": False, "ScissorsRock": False, "ScissorsPaper": True}

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!\n\nYour options are:\n\n")
    for choice in list_of_choices:
        print(f"- {choice}")

    users_choice = input("\nEnter your selection, or 'done' at any time to exit\n").title()
    computer_choice = random.choice(list_of_choices)

    exit_func(users_choice)

    while users_choice not in list_of_choices:
        users_choice = input("\nDid you spell your choice correctly?\nIf you want to end, type done!\n").title()

        exit_func(users_choice)

    exit_func(users_choice)

    # combines the user and computer's choice to use to search through the dictionary for the outcome
    choices = users_choice + computer_choice
    outcome = outcomes.get(choices)

    if users_choice == computer_choice:
        print(f"\nUhh... You and the computer tied I guess. You both chose {users_choice}.")
    elif outcome:
        print(f"\nYes!!! Your {users_choice} beat the computer's {computer_choice}.")
    else:
        print(f"\nSorry... Your {users_choice} was beaten by the computer's {computer_choice}.")
    
    continue_playing = input("\nWould you like to continue type 'Yes', otherwise type anything\n").title()

    if continue_playing == "Yes":
        rock_paper_scissors()

def exit_func(input):
    if input == "Done":
            print("Thank you for playing, see you again soon!")
            exit()
    

rock_paper_scissors()
