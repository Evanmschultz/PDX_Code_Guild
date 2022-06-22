"""
Evan Schultz
Programming 101
Unit 2 Lab 'Mad Libs'
"""

adjetives = input("Enter three adjetives separated by commas: ")
animal = input("Enter a strange animal: ")
food = input("Enter your favorite food: ")
name = input("Enter a funny name: ")
tool = input("Enter a kind of tool: ")
expression = input("Enter a strange facial expression: ")
activity = input("Enter a fun hobby: ")
time = input("Enter a little known holiday: ")

adjetives_list = adjetives.split(",")


childrens_story = f"""
Once there was this {adjetives_list[0]} {animal} who loved {food}.
She went to her {adjetives_list[1]} friend {name} and handed her a {tool}.
Her friend {expression}, and looked at the {tool}.
'Why didn't we do {activity} earlier', she said.
The {animal} said, 'because it wasn't {adjetives_list[2]} {time} yet.

The end?
"""

print(childrens_story)
