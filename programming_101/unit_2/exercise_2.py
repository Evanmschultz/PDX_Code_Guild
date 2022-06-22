"""
Evan Schultz
Progamming 101
Unit 2 Exercise 2
"""

def letter_counter():
    word = input("Please write a word: ")
    letter = input("Please give a letter to count in your word: ")
    count = word.count(letter)

    if count == 1:
        time = "time"
    else:
        time = "times"

    print(f"The letter {letter} occurs {count} {time} in {word}")

letter_counter()
