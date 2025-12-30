import csv
import os
import json
from collections import defaultdict

# Function to process the results.csv and generate head-to-head matchups
def generate_matchup_json():
    # Create output folder if it doesn't exist
    output_folder = "player_matchups"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Track player participation and match results
    player_events = defaultdict(int)  # Tracks how many events each player participated in
    player_matchups = defaultdict(lambda: defaultdict(lambda: {"wins": 0, "losses": 0, "matches": 0}))  # Nested dict for player vs player results

    # Read the CSV file
    with open('results.csv', 'r') as file:
        reader = csv.reader(file)
        current_event_players = set()
        event_lines = []

        # Parse the CSV file row by row
        for row in reader:
            if len(row) == 0 or not row[0]:  # Skip empty rows
                continue

            # First line of each event (contains event header info)
            if len(row) == 5:
                if event_lines:
                    # Process event results after the event header is complete
                    for event_line in event_lines:
                        player1, player2, result = event_line
                        if player1 != player2:
                            # Update participation count
                            player_events[player1] += 1
                            player_events[player2] += 1

                            # Update head-to-head records
                            if result == "1":
                                player_matchups[player1][player2]["wins"] += 1
                                player_matchups[player2][player1]["losses"] += 1
                            else:
                                player_matchups[player2][player1]["wins"] += 1
                                player_matchups[player1][player2]["losses"] += 1

                # Reset for new event
                event_lines = []
                continue

            # For each matchup result line in the event
            if len(row) == 3:
                player1 = row[0].strip()
                player2 = row[1].strip()
                result = row[2].strip()

                # Store match results for the current event
                event_lines.append((player1, player2, result))

        # After parsing all events, filter players with at least 40 events
        qualified_players = {player for player, count in player_events.items() if count >= 40}

        # Now generate the matchup JSON for each player
        for player, matchups in player_matchups.items():
            if player in qualified_players:
                # List to store all matchups for the player
                player_results = []

                for opponent, stats in matchups.items():
                    if opponent != player and opponent in qualified_players:
                        total_matches = stats["wins"] + stats["losses"]
                        win_percent = (stats["wins"] / total_matches) * 100 if total_matches > 0 else 0

                        player_results.append({
                            "Player": opponent,
                            "Record": f"{stats['wins']}-{stats['losses']}",
                            "Win %": f"{win_percent:.2f}%",
                            "Total Matches": total_matches
                        })

                # Sort the results alphabetically by player name
                player_results.sort(key=lambda x: x["Player"])

                # Write to JSON file
                player_file_path = os.path.join(output_folder, f"{player}.json")
                with open(player_file_path, "w", encoding="utf-8") as player_file:
                    json.dump(player_results, player_file, indent=4, ensure_ascii=False)
                    print(f"Created file for player: {player}")

# Run the function
if __name__ == "__main__":
    generate_matchup_json()
