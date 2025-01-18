f = open("results.csv", "r")

dict = {}
rank_dict = {}
event_players = []

dict["Nick D"] = [18,20,8]
dict["Juwan"] = [7,14,6]
dict["Zane"] = [1,5,2]
dict["Sonny"] = [2,5,2]
dict["Chris A"] = [8,19,7]
dict["Matt"] = [10,12,6]
dict["Simon"] = [7,16,7]
dict["Adam"] = [4,8,3]
dict["Chris K"] = [2,4,2]
dict["Mike"] = [2,5,2]
dict["Todd"] = [2,6,3]
dict["Evan"] = [0,5,2]
dict["Evan S"] = [2,4,2]
dict["Ian"] = [1,2,1]
dict["Jorgie"] = [1,3,1]
dict["Clayton"] = [3,6,2]
dict["Julio"] = [1,2,1]
dict["Alice"] = [1,3,1]
dict["Andre"] = [0,2,1]
dict["Vincent"] = [2,3,1]
dict["Khang"] = [2,3,1]
dict["David"] = [1,4,2]
dict["Marco"] = [1,3,1]
dict["Patrick"] = [1,3,1]
dict["Travis"] = [0,2,1]
dict["Ken"] = [2,2,1]

def increment_event():
        for player in event_players:
                dict[player][2] += 1

def append_events(player_one, player_two, event_players):
        if(player_one not in event_players):
                event_players.append(player_one)
        if(player_two not in event_players):
                event_players.append(player_two)

for line in f:
        if(line == "\n"):
                increment_event()
                event_players = []
                continue
        #if(len(line.split(',')) > 3):
        #        increment_event()
        #        event_players = []

        match = line.split(",")
        player_one = match[0]
        player_two = match[1]
        result = match[2]

        if(player_one not in dict):
                dict[player_one] = [0,0,0]
        if(player_two not in dict):
                dict[player_two] = [0,0,0]

        if(result.strip() == "1"):
                dict[player_one][0] += 1
        else:
                dict[player_two][0] += 1
        dict[player_one][1] += 1
        dict[player_two][1] += 1

        append_events(player_one, player_two, event_players)            

for key in dict:

        wins = int(dict[key][0])
        matches = int(dict[key][1])
        events = int(dict[key][2])
        
        rank_dict[key] = (wins/matches, events, str(wins) + "-" + str(matches-wins))

rank = 1

print("5/6/22 to 11/5/22")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts " + v[2])
        rank += 1

print("\n")
rank = 1
print("5/6/22 to 11/5/22 excluding players with less than 4 drafts")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        if(v[1] > 3):
                print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts " + v[2])
                rank += 1

