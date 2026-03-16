f = open("vanguard.txt", "r")

vanguard_dict = {}

for line in f:
    split = line.split(',')

    wins = split[0]
    losses = split[1]
    vanguard = split[2]

    if(vanguard not in vanguard_dict):
        vanguard_dict[vanguard] = {"wins": wins, "losses": losses, "winrate": int(wins)/(int(wins) + int(losses))}
    else:
        vanguard_dict[vanguard]["wins"] = str(int(vanguard_dict[vanguard]["wins"]) + int(wins))
        vanguard_dict[vanguard]["losses"] = str(int(vanguard_dict[vanguard]["losses"]) + int(losses))
        vanguard_dict[vanguard]["winrate"] = int(vanguard_dict[vanguard]["wins"])/(int(vanguard_dict[vanguard]["wins"]) + int(vanguard_dict[vanguard]["losses"]))


for i in vanguard_dict.items():
    print(i[0] + "," + str(i[1]['winrate']) + ',' + str(i[1]['wins']) + ',' + str(i[1]['losses']))

# position = 1
# for i in sorted(vanguard_dict.items(), key=lambda x: x[2], reverse=True):
#     print('{:<3} {:<15} {:<5} {:<20}'.format(str(position), str(i[0]), str(round(i[2]*100, 2)) + "%", "  Out of " + str(i[1]) + " drafts")) 
#     position+=1

print(vanguard_dict)