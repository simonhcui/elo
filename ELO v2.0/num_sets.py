f = open ("results.csv", "r")

sets_dict = {}

for line in f:
    s = line.split(",")

    if(len(s) > 3):
        if(s[3] not in sets_dict):
            sets_dict[s[3]] = 1
        else:
            sets_dict[s[3]] = sets_dict[s[3]] + 1

print(sets_dict) 