"""
Evan Schultz
Programming 101
Unit 1 - Lab
"""

from random import randint


rival_grade = randint(0, 101)
grade = input("Enter a grade between 0 and 100: ")

def letter_grade(grade): # function to convert user input number grade into a letter grade
    letter_grade = None
    grade = float_converter(grade)
    
    # logic to convert usable input grade into a letter grade
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    return letter_grade, grade

def float_converter(grade):
     # converts user input into a float and warns user if input is not a number
    while grade is not float:
        try:
            grade = float(grade) 
        except:
            print(f"'{grade}' is not a number\n")
            grade = input("Make sure the grade is an number between 0 and 100: ")
            continue
        
        # checks if input grade is usable value
        if grade < 0 or grade > 100:
            grade = input("Make sure the grade is an number between 0 and 100: ")
            continue
         
        return grade

def rival_comparison(grade, rival_grade):
    user_grade = letter_grade(grade)
    rival_grade = letter_grade(rival_grade)
    user_letter_grade = user_grade[0]
    user_num_grade = user_grade[1]
    rival_letter_grade = rival_grade[0]
    rival_num_grade = rival_grade[1]

    if user_num_grade > rival_num_grade:
        delta = user_num_grade - rival_num_grade
        print(f"""\n\nYou got {user_num_grade} out of 100.
                \rYou did better than your rival by {delta} points.\n
                \rYou got a {user_letter_grade}, and your rival got a {rival_letter_grade}
                """)
    else:
        delta = rival_num_grade - user_num_grade
        print(f"""\n\nYou got {user_num_grade} out of 100.
                \rYour rival did better than you by {delta} points.\n
                \rYou got a {user_letter_grade}, and your rival got a {rival_letter_grade}
                """)


# print(letter_grade("f"))
rival_comparison(grade, rival_grade)
# print(float_converter(-1))
