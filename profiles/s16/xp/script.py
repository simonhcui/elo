i = open("results.csv", "r")
w = open("experience.csv", "w")

def level(xp):

    level_thresholds = {
        'Prodigy': 160,
        'Apprentice': 220,
        'Task Mage': 300,
        'Adept': 400,
        'Spellshaper': 540,
        'Guildmage': 720,
        'Invoker': 970,
        'Sorcerer': 1280,
        'Battlemage': 1720,
        'Archmage': 2300
    }
    
    last_threshold = 0

    for level, threshold in reversed(level_thresholds.items()):
        if xp >= threshold:
            return level, xp - threshold, str(xp - threshold) + "/" +  str(last_threshold - threshold)
        last_threshold = threshold
    return 'Beginner', xp, str(xp - threshold) + "/" +  str(last_threshold - threshold)

def experience(player):

    chris_s16 = 300
    eric_s16 = 125
    tony_s16 = 100
    nathan_s16 = 200
    collin_s16 = 100
    walski_s16 = 25
    marco_s16 = 75
    david_k_s16 = 25
    noah_s16 = 100
    thana_s16 = 75
    david_o_s16 = 50
    matt_s16 = 25
    jackson_s16 = 25
    clayton_s16 = 25
    nick_d_s16 = 25
    daniel_l_s16 = 25

    champ_xp = {
        'nick d': 575 + nick_d_s16,
        'juwan': 175,
        'matt y': 400 + matt_s16,
        'evan s': 225,
        'tony': 500 + tony_s16,
        'clayton': 900 + clayton_s16,
        'chris a': 425 + chris_s16,
        'alberto': 225,
        'alan': 350,
        'noah': 350 + noah_s16,
        'eric k': 375 + eric_s16,
        'john k': 100,
        'jacob': 300,
        'sonny': 100,
        'walski': 400 + walski_s16,
        'stephen': 25,
        'kevin s': 300,
        'marco': 250 + marco_s16,
        'adam s': 75,
        'luis': 275,
        'collin': 75 + collin_s16,
        'nathan': 100 + nathan_s16,
        'jim': 25,
        'david k': david_k_s16,
        'thana': thana_s16,
        'david o': david_o_s16,
        'jackson': jackson_s16,
        'daniel l': daniel_l_s16
    }

    played = False
    events_played = 0
    wins = 0

    for line in i:
        if line.isspace() and played == True:
            played = False
            events_played = events_played + 1

        split = line.split(",")

        if len(split) > 1 and ((player.lower() == split[0].lower()) or (player.lower() == split[1].lower())):
            played = True

            player_one = split[0]
            player_two = split[1]
            result = split[2]

            if(player_one.lower() == player):
                if(int(result) == 1):
                    wins = wins + 1
            elif(player_two.lower() == player):
                if(int(result) == 0):
                    wins = wins + 1

    i.seek(0)

    bonus = 0

    if(player in champ_xp):
        bonus = champ_xp[player]

    xp = events_played + wins * 3 + bonus
    rank, progress, remaining = level(xp)

    w.write(player + "," + str(xp) + "," + rank + "," + str(progress) + ',' + remaining + "\n")


def main():
    players = ['adam s', 'alan', 'alberto', 'andrew d', 'chris a', 'clayton', 'collin', 'david o', 'david k', 'daniel l', 'eric k', 'evan s', 'jackson', 'jacob', 'john k', 'juwan', 'kevin s', 'luca', 
               'luis', 'luke', 'marco', 'matt y', 'nick d', 'noah', 'simon', 'sonny', 'stephen', 'todd', 'tony', 'travis', 'walski', 'zane', 'frank', 'thana', 'aaron', 
               'mike', 'ana', 'david k', 'patrick h', 'nick c', 'nathan', 'grant', 'felix']
    for player in players:
        experience(player)

if __name__=="__main__":
    main()