import datetime

f = open("results.csv", "r")




players = ['adam.csv', 'alan.csv', 'alberto.csv', 'andrew d.csv', 'chris a.csv', 'clayton.csv', 'collin.csv', 'david o.csv', 'eric k.csv', 'evan s.csv', 'jacob.csv', 'john k.csv', 'juwan.csv', 'kevin s.csv', 'luca.csv', 'luis.csv', 'luke.csv', 'marco.csv', 'matt y.csv', 'nick d.csv', 'noah.csv', 'simon.csv', 'sonny.csv', 'stephen.csv', 'todd.csv', 'tony.csv', 'travis.csv', 'walski.csv', 'zane.csv', 'frank.csv', 'thana.csv']
default_date = datetime.datetime(2022, 1, 1)
s2_date = datetime.datetime(2023, 1, 1)
s3_date = datetime.datetime(2023, 4, 1)
s4_date = datetime.datetime(2023, 7, 1)
s5_date = datetime.datetime(2023, 10, 1)
s6_date = datetime.datetime(2024, 1, 1)
s7_date = datetime.datetime(2024, 4, 1)
s8_date = datetime.datetime(2024, 7, 1)
s9_date = datetime.datetime(2024, 10, 1)
s10_date = datetime.datetime(2025, 1, 1)
s11_date = datetime.datetime(2025, 3, 14)
s12_date = datetime.datetime(2025, 6, 27)
s13_date = datetime.datetime(2025, 9, 30)
s14_date = datetime.datetime(2025, 12, 19)
s15_date = datetime.datetime(2026, 4, 1)

for player in players:

    f.seek(0)
    f1 = open(player, "w")
    wins = 0
    losses = 0
    counter = 0

    for line in f:

        match = line.lower().split(',')
        season = 0

        if(len(match) > 3):
            print(match)
            month = match[4].split('-')[0]
            day = match[4].split('-')[1]
            year = match[4].split('-')[2].strip()
            date = datetime.datetime(int(year), int(month), int(day))

        if(player.split('.')[0] in match):

            print(player.split('.')[0])
            print(match[0])

            if(match[0] == player.split('.')[0]):
                if(match[2].strip() == "1"):
                    wins = wins + 1
                else:
                    losses = losses + 1
            elif(match[1] == player.split('.')[0]):
                if(match[2].strip() == "0"):
                    wins = wins + 1
                else:
                    losses = losses + 1

            if(date < s2_date):
                season = 1
            elif(date < s3_date):
                season = 2
            elif(date < s4_date):
                season = 3
            elif(date < s5_date):
                season = 4
            elif(date < s6_date):
                season = 5
            elif(date < s7_date):
                season = 6
            elif(date < s8_date):
                season = 7
            elif(date < s9_date):
                season = 8
            elif(date < s10_date):
                season = 9
            elif(date < s11_date):
                season = 10
            elif(date < s12_date):
                season = 11
            elif(date < s13_date):
                season = 12
            elif(date < s14_date):
                season = 13
            
            counter = counter + 1

            if(counter > 40):
                f1.write(str(date.strftime("%x")).strip() + "," + str(wins/(wins + losses)) + "," + str(season) + "\n")





