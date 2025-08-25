import json

pairings = open("pairings.csv", "r")

data = {}

for line in pairings:

    split = line.split(",")

    player_one = split[0]
    player_two = split[1]
    one_wins = split[2]
    one_losses = split[3]
    win_percentage = split[4]
    total_matches = split[5]

    if player_one not in data:
        data[player_one] = []
    if player_two not in data:
        data[player_two] = []
    
    one_entry = {
        "Player": player_two,
        "Record": str(one_wins) + "-" + str(one_losses),
        "Win %": str(round(float(win_percentage) * 100, 2)) + "%",
        "Total Matches": total_matches.strip()
    }

    data[player_one].append(one_entry)

    two_entry = {
        "Player": player_one,
        "Record": str(one_losses) + "-" + str(one_wins),
        "Win %": str(round((1-float(win_percentage)) * 100, 2)) + "%",
        "Total Matches": total_matches.strip()
    }

    data[player_two].append(two_entry)

print(data)

json_str = json.dumps(data, indent=4)
with open("test.json", "w") as f:
    f.write(json_str)