import random
generate_name = True


tanks = ("D.Va", "Doomfist", "Hazard", "Junker Queen", "Mauga", "Orisa", "Ramattra", "Reinhardt", "Roadhog", "Sigma", "Winston", "Wrecking Ball", "Zarya")
dps = ("Ashe", "Bastion", "Cassidy", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Reaper", "Sojourn", "Soldier: 76", "Sombra", "Symmetra", "Torbjörn", "Tracer", "Widowmaker")
support = ("Ana", "Baptiste", "Brigitte", "Illari", "Kiriko", "Lifeweaver", "Lucio", "Mercy", "Moira", "Zenyatta")

while generate_name:
    while True:
        role = int(input("Which role would you like to be? [1 - TANK, 2 - DPS, 3 - SUPPORT]: "))
        input("PRESS ENTER TO GENERATE")
        if role == 1:
            result = random.choice(tanks)
        elif role == 2:
            result = random.choice(dps)
        elif role == 3:
            result = random.choice(support)
        else:
            print("Invalid input. Please input 1, 2, or 3.")
            continue

        print("YOUR HERO IS: ", result)

        again = input("Would you like to generate a new hero? [y/n]: ").lower()
        if again != "y":
            generate_name = False
            break