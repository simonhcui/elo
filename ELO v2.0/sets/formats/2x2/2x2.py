import math

def add_white(cd, wins, rounds):
    cd["White"][0] += int(wins)
    cd["White"][1] += int(rounds)
    #cd["White"][2] += int(cd["White"][0])/int(cd["White"][1])
    cd["White"][2] = cd["White"][0]/cd["White"][1]
                        
def add_blue(cd, wins, rounds):
    cd["Blue"][0] += int(wins)
    cd["Blue"][1] += int(rounds)
    cd["Blue"][2] = cd["Blue"][0]/cd["Blue"][1]

def add_black(cd, wins, rounds):
    cd["Black"][0] += int(wins)
    cd["Black"][1] += int(rounds)
    cd["Black"][2] = cd["Black"][0]/cd["Black"][1]

def add_red(cd, wins, rounds):
    cd["Red"][0] += int(wins)
    cd["Red"][1] += int(rounds)
    cd["Red"][2] = cd["Red"][0]/cd["Red"][1]

def add_green(cd, wins, rounds):
    cd["Green"][0] += int(wins)
    cd["Green"][1] += int(rounds)
    cd["Green"][2] = cd["Green"][0]/cd["Green"][1]

def color_dictionary(cd, archetype, wins, rounds):
    if(archetype == "4c no red"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Esper"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)    
    if(archetype == "Selesnya"):
        add_white(cd, wins, rounds)
        add_green(cd, wins, rounds)    
    if(archetype == "5c"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Grixis"):
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "Boros"):
        add_white(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "Abzan"):
        add_white(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Mardu"):
        add_white(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "Jund"):
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "4c no white"):
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Sultai"):
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Jeskai"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "Izzet"):
        add_blue(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "Orzhov"):
        add_white(cd, wins, rounds)
        add_black(cd, wins, rounds)
    if(archetype == "Rakdos"):
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "4c no green"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
    if(archetype == "4c no black"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "4c no blue"):
        add_white(cd, wins, rounds)
        add_black(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Temur"):
        add_blue(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Naya"):
        add_white(cd, wins, rounds)
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Bant"):
        add_white(cd, wins, rounds)
        add_blue(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Gruul"):
        add_red(cd, wins, rounds)
        add_green(cd, wins, rounds)
    if(archetype == "Golgari"):
        add_black(cd, wins, rounds)
        add_green(cd, wins, rounds)

f1 = open("2x2.txt", "r")

# (wins, rounds, attempts)
dict = {}
player_dict = {}
color_dict = {"White": [0, 0, 0], "Blue": [0, 0, 0], "Black": [0, 0, 0], "Red": [0, 0, 0], "Green": [0, 0, 0]}



for line in f1:
    stats = line.split(",")

    wins = stats[0]
    rounds = int(stats[0]) + int(stats[1])
    archetype = stats[2]
    player = stats[3].strip()

    if(archetype not in dict):
        dict[archetype] = [int(wins), int(rounds), 1, int(wins)/int(rounds)]
    else:
        dict[archetype][0] += int(wins)
        dict[archetype][1] += int(rounds)
        dict[archetype][2] += 1        
        dict[archetype][3] = int(dict[archetype][0])/int(dict[archetype][1])

    if(player not in player_dict):
        player_dict[player] = {archetype: 1}

    if(archetype not in player_dict[player]):
        player_dict[player][archetype] = 1
    else:
        player_dict[player][archetype] += 1

    color_dictionary(color_dict, archetype, wins, rounds)

print(color_dict)  

position = 1
for i in sorted(dict.items(), key=lambda x: x[1][3], reverse=True):
    print('{:<3} {:<15} {:<5} {:<20}'.format(str(position), str(i[0]), str(round(i[1][3]*100, 2)) + "%", "  Out of " + str(i[1][2]) + " drafts")) 
    position+=1

position = 1
print("\nExcluding archetypes drafted less than 5 times")
for i in sorted(dict.items(), key=lambda x: x[1][3], reverse=True):
    if(i[1][2] > 4):
        print('{:<3} {:<15} {:<5} {:<20}'.format(str(position), str(i[0]), str(round(i[1][3]*100, 2)) + "%", "  Out of " + str(i[1][2]) + " drafts")) 
        position+=1

position = 1
print("\nColor Win Percentage")
for i in sorted(color_dict.items(), key=lambda x: x[1][2], reverse=True):
    print('{:<3} {:<10} {:<5}'.format(str(position), str(i[0]), str(round(i[1][2], 4)*100) + "%")) 
    position+=1

print("\nMost commonly drafted archetypes for Juwan")
most = [(key, value) for key, value in player_dict["Juwan"].items() if value == max(player_dict["Juwan"].values())]
print(most)

print("Most commonly drafted archetypes for Nick D")
most = [(key, value) for key, value in player_dict["Nick D"].items() if value == max(player_dict["Nick D"].values())]
print(most)

print("Most commonly drafted archetypes for Chris A")
most = [(key, value) for key, value in player_dict["Chris A"].items() if value == max(player_dict["Chris A"].values())]
print(most)

print("Most commonly drafted archetypes for Matt")
most = [(key, value) for key, value in player_dict["Matt"].items() if value == max(player_dict["Matt"].values())]
print(most)

print("Most commonly drafted archetypes for Zane")
most = [(key, value) for key, value in player_dict["Zane"].items() if value == max(player_dict["Zane"].values())]
print(most)

print("Most commonly drafted archetypes for Angga")
most = [(key, value) for key, value in player_dict["Angga"].items() if value == max(player_dict["Angga"].values())]
print(most)

print("Most commonly drafted archetypes for Simon")
most = [(key, value) for key, value in player_dict["Simon"].items() if value == max(player_dict["Simon"].values())]
print(most)

print("Most commonly drafted archetypes for Sonny")
most = [(key, value) for key, value in player_dict["Sonny"].items() if value == max(player_dict["Sonny"].values())]
print(most)

print("Most commonly drafted archetypes for Ana")
most = [(key, value) for key, value in player_dict["Ana"].items() if value == max(player_dict["Ana"].values())]
print(most)

print("Most commonly drafted archetypes for Nick C")
most = [(key, value) for key, value in player_dict["Nick C"].items() if value == max(player_dict["Nick C"].values())]
print(most)

print("\nMost commonly drafted archetypes for Todd")
most = [(key, value) for key, value in player_dict["Todd"].items() if value == max(player_dict["Todd"].values())]
print(most)

print("\nMost commonly drafted archetypes for Adam")
most = [(key, value) for key, value in player_dict["Adam"].items() if value == max(player_dict["Adam"].values())]
print(most)

print("\nMost commonly drafted archetypes for Evan S")
most = [(key, value) for key, value in player_dict["Evan S"].items() if value == max(player_dict["Evan S"].values())]
print(most)

print("\nMost commonly drafted archetypes for Patrick R")
most = [(key, value) for key, value in player_dict["Patrick R"].items() if value == max(player_dict["Patrick R"].values())]
print(most)

print("\nMost commonly drafted archetypes for Patrick H")
most = [(key, value) for key, value in player_dict["Patrick H"].items() if value == max(player_dict["Patrick H"].values())]
print(most)

print("\nMost commonly drafted archetypes for John K")
most = [(key, value) for key, value in player_dict["John K"].items() if value == max(player_dict["John K"].values())]
print(most)

print("\nMost commonly drafted archetypes for Tony")
most = [(key, value) for key, value in player_dict["Tony"].items() if value == max(player_dict["Tony"].values())]
print(most)

print("\nMost commonly drafted archetypes for Jacob")
most = [(key, value) for key, value in player_dict["Jacob"].items() if value == max(player_dict["Jacob"].values())]
print(most)

print("\nMost commonly drafted archetypes for Alberto")
most = [(key, value) for key, value in player_dict["Alberto"].items() if value == max(player_dict["Alberto"].values())]
print(most)

print("\nMost commonly drafted archetypes for Andrew")
most = [(key, value) for key, value in player_dict["Andrew D"].items() if value == max(player_dict["Andrew D"].values())]
print(most)

print("\nMost commonly drafted archetypes for Travis")
most = [(key, value) for key, value in player_dict["Travis"].items() if value == max(player_dict["Travis"].values())]
print(most)

print("\nMost commonly drafted archetypes for Mike")
most = [(key, value) for key, value in player_dict["Mike"].items() if value == max(player_dict["Mike"].values())]
print(most)

print("\nMost commonly drafted archetypes for Alice")
most = [(key, value) for key, value in player_dict["Alice"].items() if value == max(player_dict["Alice"].values())]
print(most)

print("\nMost commonly drafted archetypes for Clayton")
most = [(key, value) for key, value in player_dict["Clayton"].items() if value == max(player_dict["Clayton"].values())]
print(most)

print(player_dict["Chris A"])
