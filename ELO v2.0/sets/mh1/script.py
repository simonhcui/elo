import math
import glicko2

f = open("results.csv", "r")
d = open("data.csv", "w")

#Player: [Drafts, Wins-Losses]
overall_dict = {}

overall_dict ["Nick D"] = [8, "18-2"]
overall_dict ["Juwan"] = [6, "7-7"]
overall_dict ["Zane"] = [2, "1-4"]
overall_dict ["Sonny"] = [2, "2-3"]
overall_dict ["Chris A"] = [7, "8-11"]
overall_dict ["Matt"] = [6, "10-2"]
overall_dict ["Simon"] = [7, "7-9"]
overall_dict ["Adam"] = [3, "4-4"]
overall_dict ["Chris K"] = [2, "2-2"]
overall_dict ["Mike"] = [2, "2-3"]
overall_dict ["Todd"] = [3, "2-4"]
overall_dict ["Evan K"] = [2, "0-5"]
overall_dict ["Evan S"] = [2, "2-2"]
overall_dict ["Ian"] = [1, "1-1"]
overall_dict ["Jorgie"] = [1, "1-2"]
overall_dict ["Clayton"] = [2, "3-3"]
# overall_dict ["Julio"] = [1,2,1]
# overall_dict ["Alice"] = [1,3,1]
# overall_dict ["Andre"] = [0,2,1]
# overall_dict ["Vincent"] = [2,3,1]
# overall_dict ["Khang"] = [2,3,1]
# overall_dict ["David"] = [1,4,2]
# overall_dict ["Marco"] = [1,3,1]
# overall_dict ["Patrick"] = [1,3,1]
# overall_dict ["Travis"] = [0,2,1]
# overall_dict ["Ken"] = [2,2,1]


# Winrate functions
# increment_event()
# append_events()
# winrate()
def increment_event(d, players):
        for player in players:
                d[player][2] += 1

def append_events(player_one, player_two, event_players):
        if(player_one not in event_players):
                event_players.append(player_one)
        if(player_two not in event_players):
                event_players.append(player_two)

def winrate(file):
        dict = {}
        rank_dict = {}
        event_players = []

        for line in file:
                if(line == "\n"):
                        continue

                if(line.split(",")[0] == ""):
                        increment_event(dict, event_players)
                        continue
        
                if(len(line.split(',')) > 3):
                        increment_event(dict, event_players)
                        event_players = []

                match = line.split(",")
                player_one = match[0]
                player_two = match[1]
                result = match[2]

                if(player_one not in dict):
                        dict[player_one] = [0,0,0]
                if(player_two not in dict):
                        dict[player_two] = [0,0,0]

                if(result.strip() == "1"):
                        dict[player_one][0] += 1
                else:
                        dict[player_two][0] += 1
                dict[player_one][1] += 1
                dict[player_two][1] += 1

                append_events(player_one, player_two, event_players)            

                for key in dict:

                        wins = int(dict[key][0])
                        matches = int(dict[key][1])
                        events = int(dict[key][2])
                        
                        rank_dict[key] = (wins/matches, events, str(wins) + "-" + str(matches-wins))

                rank = 1

        #print("All players:")
        for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
                #print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts " + v[2])
        

                if(k not in overall_dict):
                        overall_dict[k] = [v[1], v[2]]
                else:
                        v_split = v[2].split("-")
                        print(k)
                        print(overall_dict[k])
                        print(overall_dict[k][1])
                        o_split = overall_dict[k][1].split("-")
                        overall_dict[k] = [overall_dict[k][0] + v[1], str(int(o_split[0]) + int(v_split[0])) + "-" + str(int(o_split[1]) + int(v_split[1]))]
                        print(overall_dict[k])
                
                
                rank += 1

        # print("\n")
        # rank = 1
        # print("Excluding players with less than 4 drafts:")
        # for k, v in sorted(rank_dict.items(), key=lambda p:p[1], reverse=True):
        #         if(v[1] > 3):
        #                 print(str(rank) + ") " + k + ": " + str(round(100*v[0], 2)) + "% winrate out of " + str(v[1]) + " drafts " + v[2])
        #                 rank += 1

        file.seek(0)

# ELO functions
# Probability()
# EloRating()
# elo()

# Function to calculate the Probability
def Probability(rating1, rating2):
 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))

# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):
   
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)
 
    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)
 
    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (int(d) == 1) :
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
     
 
    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else :
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
     
 
    #print("Updated Ratings:-")
    #print("Ra =", round(Ra, 6)," Rb =", round(Rb, 6))
    
    return (Ra, Rb)

def elo(file):
        set = ""
        date = ""
        elo_dict = {}
  
        for line in file:

                if(line == '\n'):
                        set = ""
                        date = ""  
                        continue
    
                player1 = line.split(",")[0]
                player2 = line.split(",")[1]
                result = line.split(",")[2]

                if(len(line.split(",")) > 3):
                        set = line.split(",")[3]
                if(len(line.split(",")) > 4):
                        date = line.split(",")[4]
    
                if(player1 not in elo_dict):
                        elo_dict[player1] = (1000, set, date)
                if(player2 not in elo_dict):
                        elo_dict[player2] = (1000, set, date)
      
                gameResult = EloRating(elo_dict[player1][0], elo_dict[player2][0], 30, result.strip())
                elo_dict[player1] = (gameResult[0], set, date.strip())
                elo_dict[player2] = (gameResult[1], set, date.strip())
  
        position = 1
        for i in sorted(elo_dict,key=elo_dict.get,reverse=True):
                print(str(position) + ") " + str(i) + ":" + str(dict[i]))
                overall_dict[i].append(elo_dict[i])
                position+=1   

        file.seek(0)

# Glicko Functions
# populate_player_list()
# populate_player_dict()
# calculate_games()
# calculate_glixare()
# glicko()

def populate_player_list(file, player_list):
    for line in file:
        split = line.split(",")
        
        if(len(split) > 2):
            player_one = split[0]
            player_two = split[1]

            if(len(player_one) > 0 and player_one not in player_list):
                player_list.append(player_one)
            if(len(player_two) > 0 and player_two not in player_list):
                player_list.append(player_two)
    file.seek(0)

def populate_player_dict(player_list, player_dict):
    for player in player_list:
        player_dict[player] = glicko2.Player()

def calculate_games(file, player_dict):
    for line in file:
            split = line.split(",")

            if(len(split) > 2):
                player_one_name = split[0]
                player_two_name = split[1]
                result = split[2]

                player_one = player_dict[player_one_name]
                player_two = player_dict[player_two_name]
                player_one_outcome = float(result)
                player_two_outcome = float(abs(1 - int(result)))

                player_one.update_player([player_two.rating], [player_two.rd], [player_one_outcome])
                player_two.update_player([player_one.rating], [player_one.rd], [player_two_outcome])

def calculate_glixare(player, player_dict):
    pi = 3.14159265359

    return (10000/(1 + math.pow(10, (1500 - player_dict[player].rating)*pi/math.sqrt(3*math.pow(math.log(10), 2)*math.pow(player_dict[player].rd, 2) + 
                                                                                     2500*(64*math.pow(pi, 2) + 147 * math.pow(math.log(10), 2))))))/100

def glicko(file):
        player_list = []
        player_dict = {}
        populate_player_list(file, player_list)
        populate_player_dict(player_list, player_dict)
        calculate_games(file, player_dict)

        for player in player_dict:
                print(player + " " + str(player_dict[player].rating) + " ±" + str(player_dict[player].rd) + " " + str(player_dict[player].vol) + " " + str(calculate_glixare(player, player_dict)))
                overall_dict[player].append(player_dict[player].rating)
                overall_dict[player].append(player_dict[player].rd)
                overall_dict[player].append(player_dict[player].vol)
                overall_dict[player].append(calculate_glixare(player, player_dict))
        

def main():
    winrate(f)
    elo(f)
    glicko(f)
    print(overall_dict)

    d.write("Player,Num Drafts,Wins,Losses,Win %,ELO,Last Set Drafted,Last Date Drafted,Glicko,Volatility,GXE\n")    
    for player in overall_dict:
           
           num_drafts = overall_dict[player][0]
           num_wins = overall_dict[player][1].split("-")[0]
           num_losses = overall_dict[player][1].split("-")[1]
           win_percent = str(float(num_wins)/(float(num_wins)+float(num_losses)))
           print(player)
           print(overall_dict[player])
           
           if(len(overall_dict[player]) < 3):
                player_elo = "N/A"
                last_set = "N/A"
                last_date = "N/A"
                player_glicko_1 = "N/A"
                player_glicko_2 = "N/A"
                volatility = "N/A"
                gxe = "N/A"
           else:
                player_elo = overall_dict[player][2][0]
                last_set = overall_dict[player][2][1]
                last_date = overall_dict[player][2][2]
                player_glicko_1 = overall_dict[player][3]
                player_glicko_2 = overall_dict[player][4]
                volatility = overall_dict[player][5]
                gxe = overall_dict[player][6]
                
           d.write(player + "," + str(num_drafts) + "," + num_wins + "," + num_losses + "," + win_percent + "," + str(player_elo) + 
                   "," + last_set + "," + last_date + "," + str(player_glicko_1) + "±" + str(player_glicko_2) + 
                   "," + str(volatility) + "," + str(gxe) + "\n")     

if __name__ == "__main__":
    main()