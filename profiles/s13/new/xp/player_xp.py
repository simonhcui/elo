import csv
from collections import defaultdict

# Define the XP thresholds for each level
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

# Define a function to determine the player's level and XP towards next level
def get_player_level_and_xp(xp):
    for level, threshold in reversed(level_thresholds.items()):
        if xp >= threshold:
            return level, xp - threshold
    return 'Beginner', xp  # For players with less than 160 XP

# Initialize a dictionary to store player data: XP, wins, and event counts
player_data = defaultdict(lambda: {'xp': 0, 'wins': 0, 'events': 0})

# Read the results CSV file
with open('results.csv', 'r') as infile:
    reader = csv.reader(infile)
    current_event_players = set()

    for row in reader:
        if len(row) == 5:  # This indicates a new event (first row of the event)
            # Process the previous event's matches before starting a new one
            for player in current_event_players:
                player_data[player]['events'] += 1  # Each player gets XP for participating in the event

            # Reset for the new event
            current_event_players.clear()

        elif len(row) == 3:  # A match between two players
            player1, player2, result = row[0], row[1], int(row[2])
            # Both players gain XP for participating
            player_data[player1]['xp'] += 1
            player_data[player2]['xp'] += 1
            current_event_players.add(player1)
            current_event_players.add(player2)

            # Winner gains 3 XP and counts the win
            if result == 1:
                player_data[player1]['xp'] += 3
                player_data[player1]['wins'] += 1
            else:
                player_data[player2]['xp'] += 3
                player_data[player2]['wins'] += 1

    # After the loop ends, handle the last event
    for player in current_event_players:
        player_data[player]['events'] += 1

# Prepare the output CSV file
with open('player_xp.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Player Name', 'Level', 'XP Towards Next Level', 'Total Wins', 'Total Events Played'])

    for player, data in player_data.items():
        # Only include players with at least 40 events
        if data['events'] >= 40:
            level, xp_to_next = get_player_level_and_xp(data['xp'])
            writer.writerow([player, level, xp_to_next, data['wins'], data['events']])

print("CSV file generated: player_xp.csv")
