f = open("travisdata.csv", "r")

x_map = {
        1: open("datax1.csv", "w"),
        2: open("datax2.csv", "w"),
        3: open("datax3.csv", "w"),
        4: open("datax4.csv", "w"),
        5: open("datax5.csv", "w"),
        6: open("datax6.csv", "w"),
        7: open("datax7.csv", "w"),
        8: open("datax8.csv", "w"),
        9: open("datax9.csv", "w"),
        10: open("datax10.csv", "w"), }

y_map = {
        1: open("datay1.csv", "w"),
        2: open("datay2.csv", "w"),
        3: open("datay3.csv", "w"),
        4: open("datay4.csv", "w"),
        5: open("datay5.csv", "w"),
        6: open("datay6.csv", "w"),
        7: open("datay7.csv", "w"),
        8: open("datay8.csv", "w"),
        9: open("datay9.csv", "w"),
        10: open("datay10.csv", "w"), }


for line in f:
        split = line.split(",")

        season = int(split[2].strip())
        print(split)        
        x_map[season].write("\"" + split[0] + "\"" + ",")
        y_map[season].write(split[1] + ",")
