dict = {}
rank_dict = {}
event_players = []

dict["Nick D"] = [31,45,16]
dict["Juwan"] = [25,43,17]
dict["Chris H"] = [2,3,1]
dict["Zane"] = [4,18,7]
dict["Sonny"] = [15,33,12]
dict["Chris A"] = [22,43,16]
dict["Matt"] = [22,37,16]
dict["Simon"] = [27,53,20]
dict["Angga"] = [8,18,6]
dict["Charles"] = [2,3,1]
dict["Adam"] = [11,17,6]
dict["Travis"] = [1,8,3]
dict["Chris K"] = [3,7,3]
dict["Mike"] = [1,3,1]
dict["Todd"] = [9,27,10]
dict["Evan"] = [2,8,3]
dict["Evan S"] = [2,4,2]
dict["Ian"] = [3,5,2]
dict["Jorgie"] = [2,10,4]
dict["Clayton"] = [4,8,3]
dict["Julio"] = [2,6,2]
dict["Alice"] = [6,11,4]
dict["Andre"] = [0,4,2]
dict["Karen"] = [2,2,1]
dict["Jacob"] = [2,6,2]
dict["Vanndy"] = [5,6,2]
dict["Patrick R"] = [2,3,1]
dict["Ana"] = [4,6,2]
dict["Michael"] = [2,3,1]
dict["Nick C"] = [3,6,2]
dict["Tomoya"] = [1,8,3]
dict["Ryan"] = [0,2,1]

for key in dict:

        wins = int(dict[key][0])
        matches = int(dict[key][1])
        events = int(dict[key][2])
        
        rank_dict[key] = (wins/matches, events)

rank = 1

print("Drafts from start of stat tracking (5/6/22) to right before start of ELO tracking (7/31/22)")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts")
        rank += 1

print("\n")
rank = 1
print("Drafts from start of stat tracking (5/6/22) to right before start of ELO tracking (7/31/22) excluding players with less than 5 drafts")
for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        if(v[1] > 4):
                print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts")
                rank += 1

