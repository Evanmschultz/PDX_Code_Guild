"""
Evan Schultz
Programming 101
Unit 2 Exercise 2
"""

word = input("Enter a word or phrase and watch how we can switch the cases: ")

def swap_case(word):
    output = word.swapcase()
    return output

def case_swapper(word):
    output = ""
    for i in range(len(word)):
        if word[i].isupper():
            output += word[i].lower()
        else:
            output += word[i].upper()
    return output

print(swap_case(word))
print(case_swapper(word))
