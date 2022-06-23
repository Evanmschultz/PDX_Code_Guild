"""
Simple distance unit converter using dictionaries and not using any if/elif statements
"""

conversions = {
    "in": 0.0254,
    "ft": 0.3048, 
    "yd": 0.9144, 
    "m": 1, 
    "km": 1/1000, 
    "mi": 1/1609.34
}

def converter(convert_from, convert_to, num_of_units):
    meters = conversions[convert_from] * float(num_of_units)
    print(f"convert from units value: {conversions[convert_from]}")
    print(meters)
    final_units = conversions[convert_to] * meters
    
    return final_units

print("Welcome to your friendly conversion tool. Type 'done' if you ever want to exit the program\n")
convert_more = "yes"

while convert_more == "yes":
    convert_from = input("\nEnter the unit you want to convert from:\n").lower()
    while convert_from not in conversions:
        if convert_from == "done":
            exit()
        print("Make sure you are typing the 2 digit representation of the unit, or 'm' for meter.")
        convert_from = input("\nEnter the unit you want to convert from:\n").lower()

    convert_to = input("\nEnter the unit you want to convert to:\n").lower()
    while convert_to not in conversions:
        if convert_to == "done":
            exit()
        print("Make sure you are typing the 2 digit representation of the unit, or 'm' for meter.")
        convert_to = input("\nEnter the unit you want to convert from:\n").lower()

    num_of_units = None
    while num_of_units is not float:
        num_of_units = input(f"\nEnter the amount of '{convert_from}' you want to convert to '{convert_to}':\n").lower()
        if num_of_units == "done":
            exit()
        try:
            float(num_of_units)
            break
        except ValueError:
            print("\nMake sure you are entering a real number!")
            continue

    output = converter(convert_from, convert_to, num_of_units)
    print(f"\n{num_of_units} is {output} {convert_to}!")

    convert_more = input("\nWould you like to convert more units, yes or no?\n").lower()
