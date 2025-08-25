r = open("results.csv", "r")
w = open("pairings.csv", "w")

matchups = {}

for line in r:
    if(len(line) > 1):
        split = line.split(",")
        player_one = split[0]
        player_two = split[1]
        result = split[2].strip()

        player_one_first = player_one < player_two
        player_one_won = False
        player_two_won = False

        #print(player_one)
        #print(player_two)
        #print(player_one_first)

        if(player_one_first):

            #print(player_one)
            #print(player_two)
            #print(result)
            #print(result == '1')

            if(result == '1'):
                player_one_won = True
            else:
                player_two_won = True
        else:
            if(result == '1'):
                player_two_won = True
            else:
                player_one_won = True
                
            

        matchup = (player_one, player_two) if player_one < player_two else (player_two, player_one)

        if matchup not in matchups:
            #print(player_one)
            #print(player_two)
            #print(result)
            if(player_one_won):
                matchups[matchup] = (1,0)
            else:
                matchups[matchup] = (0,1)
        else:
            if(player_one_won):             
                matchups[matchup] = (matchups[matchup][0] + 1, matchups[matchup][1])
            else:
                matchups[matchup] = (matchups[matchup][0], matchups[matchup][1] + 1)

        print(str(matchup) + " " + str(matchups[matchup]))
        #print(player_one + " " + player_two + " " + str(matchups[matchup]))

#print(matchups)

for matchup in matchups:
     #print(str(matchup) + " " + str(matchups[matchup]))

     profile_players = [
         "Clayton", "Luis", "Alberto", "Alan", "Tony", "Nick D", "Eric K", "Matt Y", "Chris A", "Walski", "Evan S", "Noah", "Collin", "David O", "Adam", "Juwan", "Sonny", "Andrew D", "Kevin", "Todd", "Luca", "Simon",
         "Zane", "Stephen", "Luke", "John K", "Jacob", "Travis", "Marco"
     ]
 
     if(matchup[0] in profile_players and matchup[1] in profile_players):
        w.write(matchup[0] + "," + matchup[1] + "," + str(matchups[matchup][0]) + "," + str(matchups[matchup][1]) + "," + str(matchups[matchup][0]/(matchups[matchup][0] + matchups[matchup][1])) + "," + str(matchups[matchup][0] + matchups[matchup][1]) + "\n")
            
