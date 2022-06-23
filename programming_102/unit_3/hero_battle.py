# ______________________________________________ #
# Setup
# ______________________________________________ #

# defining hero/villian stats

hero = {
    "name": "Sjöfn", 
    "hp": 100, 
    "attack": 12
    }
villian = {
    "name": "Fenrir", 
    "hp": 100, 
    "attack": 10
    }

def is_defeated(character):
    # returns True if 'hp' is equal to or below 0
    # Otherwise returns False
    return character["hp"] <= 0

while True:
    print("\nWelcome to Hero Battle!")
    hero_name = hero["name"]
    villian_name = villian["name"]
    round_num = 0

    user_input = input(f"\nAre you ready to watch {hero_name} take on {villian_name}. Enter 'yes' to start or 'done' at any time to exit.\n")
    if user_input != "yes":
        break

    while not is_defeated(hero) and not is_defeated(villian):
        hero_attack = hero["attack"]
        hero_hp = hero["hp"]
        villian_hp = villian["hp"]
        villian_attack = villian["attack"]

        print(f"\n{hero_name} and {villian_name}: Round {round_num}!\n")
        print(f"{hero_name} has an hp of {hero_hp} and attacks with {hero_attack}")
        print(f"{villian_name} has an hp of {villian_hp} and attacks with {villian_attack}")
        print(f"\nOhhhh!!! Now {hero_name}'s hp is {hero_hp} and {villian_name}'s is {villian_hp}!")
        hero["hp"] -= villian_attack
        villian["hp"] -= hero_attack
        round_num += 1

    if hero_hp == villian_hp:
        print(f"\nStrange... It looks like {hero_name} and {villian_name} knocked each other out in the {round_num} round!")
    elif hero_hp > villian_hp:
        print(f"\nIt looks {hero_name} knocked out {villian_name} in round {round_num}!")
    else:
        print(f"\nIt looks {villian_name} knocked out {hero_name} in round {round_num}!")
