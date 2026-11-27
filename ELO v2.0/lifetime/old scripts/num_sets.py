f = open ("results.csv", "r")
w = open ("num_sets.csv", "w")

sets_dict = {}

sets_dict['2X2'] = 7
sets_dict['Chaos'] = 2
sets_dict['CNS'] = 1
sets_dict['DOM'] = 1
sets_dict['ELD'] = 1
sets_dict['EMN'] = 1
sets_dict['MH2'] = 7
sets_dict['NEO'] = 1
sets_dict['ORI'] = 1
sets_dict['UMA'] = 1

for line in f:
    s = line.split(",")

    if(len(s) > 3):
        if(s[3] not in sets_dict):
            sets_dict[s[3]] = 1
        else:
            sets_dict[s[3]] = sets_dict[s[3]] + 1

print(sets_dict) 

for set in sets_dict:
    w.write(set + "," + str(sets_dict[set]) + "\n")