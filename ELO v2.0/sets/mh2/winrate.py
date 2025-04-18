f = open("results.csv", "r")

dict = {}
rank_dict = {}
event_players = []


def increment_event():
        for player in event_players:
                dict[player][2] += 1

def append_events(player_one, player_two, event_players):
        if(player_one not in event_players):
                event_players.append(player_one)
        if(player_two not in event_players):
                event_players.append(player_two)

for line in f:
        if(line == '\n'):
                increment_event()
                event_players = []
                continue

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
        
        rank_dict[key] = (wins/matches, events)

rank = 1

print("Drafts from start of ELO calculation (8/4/22) to 11/5/22")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts")
        rank += 1

print("\n")
rank = 1
print("Drafts from start of ELO calculation (8/4/22) to 11/5/22 excluding players with less than 5 drafts")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        if(v[1] > 4):
                print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts")
                rank += 1

