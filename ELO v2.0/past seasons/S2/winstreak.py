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
        #longest_streak, current_streak, record_start_date, record_end_date, current_start, current_end
        player_dict[player_a] = [0, 0, date, date, date, date]

    if(player_b not in player_dict):
        player_dict[player_b] = [0, 0, date, date, date, date]

    if(str(result).strip() == "1"):
        winner = player_a
        loser = player_b
    else:
        winner = player_b
        loser = player_a

    winner_longest_streak = player_dict[winner][0]
    winner_current_streak = player_dict[winner][1]

    winner_current_start = player_dict[winner][4]
    winner_current_end = player_dict[winner][5]

    winner_record_start = player_dict[winner][2]
    winner_record_end = player_dict[winner][3]


    loser_longest_streak = player_dict[loser][0]

    loser_record_start = player_dict[loser][2]
    loser_record_end = player_dict[loser][3]

    loser_current_start = player_dict[loser][4]
    loser_current_end = player_dict[loser][5]

    player_dict[winner] = [
        winner_current_streak + 1 if(winner_longest_streak <= winner_current_streak) else winner_longest_streak,
        winner_current_streak + 1,
        date,
        winner_current_end if(winner_longest_streak <= winner_current_streak) else  winner_record_end,
        winner_current_start,
        date]

    player_dict[loser] = [
        loser_longest_streak,
        0, 
        loser_record_start,
        loser_record_end,
        date, 
        date]


for player in player_dict:
    print(player + " longest win streak: " + str(player_dict[player][0]) + " from " + player_dict[player][2].strip() + " to " + player_dict[player][3])
    w.write(player + "," + str(player_dict[player][0]) + "," + player_dict[player][2].strip() + "," + player_dict[player][3])
    