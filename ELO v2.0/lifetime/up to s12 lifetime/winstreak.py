f = open("results.csv", "r")
w = open("winstreak.csv", "w")

player_dict = {}
date = ""

for line in f:
    
    split_line = line.split(",")
    
    if(len(split_line) < 3):
        continue
    if(len(split_line) > 4):
        date = split_line[4]
    
    player_a = split_line[0]
    player_b = split_line[1]
    result = split_line[2]
    winner = ""
    loser = ""
    
    if(player_a not in player_dict):
        #longest_streak, current_streak, start_date, end_date
        player_dict[player_a] = [0, 0, date, date]

    if(player_b not in player_dict):
        player_dict[player_b] = [0, 0, date, date]

    if(str(result).strip() == "1"):
        winner = player_a
        loser = player_b
    else:
        winner = player_b
        loser = player_a

    winner_longest_streak = player_dict[winner][0]
    winner_current_streak = player_dict[winner][1]
    loser_longest_streak = player_dict[loser][0]
    loser_date_one = player_dict[loser][2]
    loser_date_two = player_dict[loser][3]

    player_dict[winner] = [
        winner_current_streak + 1 if(winner_longest_streak <= winner_current_streak) else winner_longest_streak,
        winner_current_streak + 1,
        date if(winner_current_streak == 0) else player_dict[winner][2],
        date]

    player_dict[loser] = [
        loser_longest_streak,
        0, 
        loser_date_one, 
        loser_date_two]


for player in player_dict:
    print(player + " longest win streak: " + str(player_dict[player][0]) + " from " + player_dict[player][2].strip() + " to " + player_dict[player][3])
    w.write(player + "," + str(player_dict[player][0]) + "," + player_dict[player][2].strip() + "," + player_dict[player][3])
    