"""
Evan Schultz
Programming 101 
Unit 2 Exercise 1

I am a little uncertain how to effectively create logic that will further prevent people from inputing 
random strings of characters instead of actual addresses outside of increasing the amount of inputs
and/or using an api
"""

street = input("Enter your full street address: ")
city = input("Enter your city: ")
state = input("Enter your two letter state code: ")

while len(state) != 2:
    print("Make sure you input your state's correct 2 letter code")
    state = input("Enter your two letter state code: ")

zip_code = input("Enter your zip code: ")

while len(zip_code) != 5:
    print("Make sure you have your zip code correct")
    zip_code = input("Enter your zip code: ")

print(f"""

{street.title()}
{city.capitalize()}
{state.upper()}
{zip_code}
""")
