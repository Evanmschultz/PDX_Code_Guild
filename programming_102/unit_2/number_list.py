nums = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]

def sum(list):
    sum = 0

    for i in list:
        sum += i
    
    return sum

fifty_three = sum(nums)
print(fifty_three) # prints '53'


def input_func():
    # takes user's input and returns list
    user_list = []

    while True:
        # cannot take in float values, but does work with negatives
        user_input = input("Enter a number or 'done' to quit: \n").lower()
        if user_input == "done":
            return sum(user_list)
        elif user_input.isdigit():
            user_list.append(float(user_input))
            continue
        elif user_input.startswith("-") and user_input[1:].isdigit():
            user_list.append(float(user_input))
            continue
        else:
            print(f"{user_input} is not a number.")
            continue

def try_except_input_func():
    # takes user's input, including floats and returns sum(list)
    user_list = []

    while True: 
        # This seems much shorter and easier to read than the other method
        user_input = input("Enter a number or 'done' to quit: \n").lower()

        if user_input == "done":
            return sum(user_list)
        else:
            try:
                user_input = float(user_input)
            except ValueError:
                print(f"{user_input} is not a number.")
                continue

            user_list.append(user_input)
            continue


print(try_except_input_func())
# print(input_func())
