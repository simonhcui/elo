import os
import shutil

def remove_folders(parent, folders):
        for folder in os.listdir(parent):
                folder_path = os.path.join(parent, folder)

                if os.path.isdir(folder_path) and folder in folders:
                        try:
                                shutil.rmtree(folder_path)
                        except Exception as e:
                                print(f"Failed to remote {folder_path}: {e}")

#parent = "C:\\Users\\cui\\Desktop\\elosite\\elo\\profiles\\historygraph\\s13"d
parent = "C:\\Users\\simoncui\\Desktop\\elosite\\elo\\profiles\\historygraph\\s13"
folders = ['adam', 'alan', 'alberto', 'andrew d', 'chris a', 'clayton', 'collin', 'david o', 'eric k', 'evan s', 'jacob', 'john k', 'juwan', 'kevin s', 'luca', 'luis', 'luke', 'marco', 'matt y', 'nick d', 'noah', 'simon', 'sonny', 'stephen', 'todd', 'tony', 'travis', 'walski', 'zane', 'frank', 'thana']
remove_folders(parent, folders)


players = ['adam.csv', 'alan.csv', 'alberto.csv', 'andrew d.csv', 'chris a.csv', 'clayton.csv', 'collin.csv', 'david o.csv', 'eric k.csv', 'evan s.csv', 'jacob.csv', 'john k.csv', 'juwan.csv', 'kevin s.csv', 'luca.csv', 'luis.csv', 'luke.csv', 'marco.csv', 'matt y.csv', 'nick d.csv', 'noah.csv', 'simon.csv', 'sonny.csv', 'stephen.csv', 'todd.csv', 'tony.csv', 'travis.csv', 'walski.csv', 'zane.csv', 'frank.csv', 'thana.csv']
#players = ['adam.csv']

for player in players:

        f = open(player, "r")
        player_name = player.split(".")[0]
        os.makedirs(player_name)

        x_map = {
                1: open(player_name + "/datax1.csv", "w"),
                2: open(player_name + "/datax2.csv", "w"),
                3: open(player_name + "/datax3.csv", "w"),
                4: open(player_name + "/datax4.csv", "w"),
                5: open(player_name + "/datax5.csv", "w"),
                6: open(player_name + "/datax6.csv", "w"),
                7: open(player_name + "/datax7.csv", "w"),
                8: open(player_name + "/datax8.csv", "w"),
                9: open(player_name + "/datax9.csv", "w"),
                10: open(player_name + "/datax10.csv", "w"),
                11: open(player_name + "/datax11.csv", "w"),
                12: open(player_name + "/datax12.csv", "w"),
                13: open(player_name + "/datax13.csv", "w"), }

        y_map = {
                1: open(player_name + "/datay1.csv", "w"),
                2: open(player_name + "/datay2.csv", "w"),
                3: open(player_name + "/datay3.csv", "w"),
                4: open(player_name + "/datay4.csv", "w"),
                5: open(player_name + "/datay5.csv", "w"),
                6: open(player_name + "/datay6.csv", "w"),
                7: open(player_name + "/datay7.csv", "w"),
                8: open(player_name + "/datay8.csv", "w"),
                9: open(player_name + "/datay9.csv", "w"),
                10: open(player_name + "/datay10.csv", "w"),
                11: open(player_name + "/datay11.csv", "w"),
                12: open(player_name + "/datay12.csv", "w"),
                13: open(player_name + "/datay13.csv", "w"), }

        for line in f:
                split = line.split(",")

                season = int(split[2].strip())
                print(split)        
                x_map[season].write("\"" + split[0] + "\"" + ",")
                y_map[season].write(split[1] + ",")
