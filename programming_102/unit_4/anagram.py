"""
anagram checker
take inputs
convert to list
sort list
check if they are equal
"""
from string import punctuation


def anagram_checker(input_list):
    word_list = []
    for word in input_list:
        word.replace(" ", "")

        for char in word:
            if char in punctuation:
                word = word.replace(char, "")
        
        word = list(word.lower())
        word.sort()
        word_list.append(word)

    if word_list.count(word_list[0]) == len(word_list):
        return True
    else:
        return False


while True:
    print("Welcome to Anagram Checker!")
    input_amount = None
    while input_amount is not int:
        input_amount = input("\nHow many words would you like me to compare?\n").lower()

        try:
            input_amount = int(input_amount)
        except ValueError:
            print("Please enter a number!")
            continue

        if input_amount < 2:
            print("I need to compare at least two words!")
            input_amount = input("\nHow many words would you like me to compare?")
            continue
        else:
            break

    print(f"\nGreat let's check if your {input_amount} words are anagrams!")
    input_list = []

    for i in range(input_amount):
        word = input(f"\nPlease enter word {i+1}: ")
        input_list.append(word)
    
    if anagram_checker(input_list):
        print("\nWow, all of your inputed words are anagrams!")
    else:
        print("\nSorry, those words are not anagrams.")

    restart = input("\nIf you would like to start over enter 'yes', else enter anything!\n")
    if restart == "yes":
        continue
    else:
        exit()
