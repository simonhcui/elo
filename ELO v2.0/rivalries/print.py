f = open("pairings.csv", "r")
f1 = open("print.txt", "w")

for line in f:

    split = line.split(",")
    f1.write(split[0] + " v " + split[1] + " " + split[2] + "-" + split[3])