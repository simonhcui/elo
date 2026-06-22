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
    
    for level, threshold in reversed(level_thresholds.items()):
        if xp >= threshold:
            return level, xp - threshold
    return 'Beginner', xp

def experience(player):

    champ_xp = {
        'nick d': 425,
        'juwan': 175,
        'matt y': 400,
        'evan s': 225,
        'tony': 500,
        'clayton': 425,
        'chris a': 400,
        'alberto': 225,
        'alan': 350,
        'noah': 150,
        'eric k': 125,
        'john k': 100,
        'jacob': 275,
        'sonny': 100,
        'walski': 275,
        'stephen': 25,
        'kevin s': 175,
        'marco': 0,
        'adam': 75,
        'luis': 100
    }

    played = False
    events_played = 0
    wins = 0

    for line in i:
        if line.isspace() and played == True:
            played = False
            events_played = events_played + 1

        split = line.split(",")

        if len(split) > 1 and ((player in split[0].lower()) or (player in split[1].lower())):
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
    rank, progress = level(xp)

    w.write(player + "," + str(xp) + "," + rank + "," + str(progress) + "\n")


def main():
    players = ['adam', 'alan', 'alberto', 'andrew d', 'chris a', 'clayton', 'collin', 'david o', 'eric k', 'evan s', 'jacob', 'john k', 'juwan', 'kevin s', 'luca', 'luis', 'luke', 'marco', 'matt y', 'nick d', 'noah', 'simon', 'sonny', 'stephen', 'todd', 'tony', 'travis', 'walski', 'zane', 'frank', 'thana']
    for player in players:
        experience(player)

if __name__=="__main__":
    main()