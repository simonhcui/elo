import csv
import os
import json
from collections import defaultdict
from datetime import datetime

# Helper function to normalize the date and parse it (handles both 2-digit and 4-digit year formats)
def parse_date(date_str):
    if not date_str:
        raise ValueError(f"Date string is empty or malformed: {date_str}")
    
    date_str = date_str.replace('/', '-')
    date_parts = date_str.split('-')
    
    if len(date_parts) != 3:
        raise ValueError(f"Invalid date format: {date_str}")
    
    if len(date_parts[0]) == 1:
        date_parts[0] = '0' + date_parts[0]
    
    if len(date_parts[1]) == 1:
        date_parts[1] = '0' + date_parts[1]
    
    normalized_date_str = '-'.join(date_parts)
    
    try:
        return datetime.strptime(normalized_date_str, "%m-%d-%Y")
    except ValueError:
        try:
            if len(date_parts[2]) == 2:
                normalized_date_str = '-'.join(date_parts[:2]) + '-20' + date_parts[2]
            return datetime.strptime(normalized_date_str, "%m-%d-%Y")
        except ValueError:
            raise ValueError(f"Date format error: {date_str} does not match expected formats.")

# Helper function to determine the season from a given date
def get_season(date):
    if date <= datetime(2022, 12, 31):
        return "Season 1"
    elif datetime(2023, 1, 1) <= date <= datetime(2023, 3, 31):
        return "Season 2"
    elif datetime(2023, 4, 1) <= date <= datetime(2023, 6, 30):
        return "Season 3"
    elif datetime(2023, 7, 1) <= date <= datetime(2023, 9, 30):
        return "Season 4"
    elif datetime(2023, 10, 1) <= date <= datetime(2023, 12, 31):
        return "Season 5"
    elif datetime(2024, 1, 1) <= date <= datetime(2024, 3, 31):
        return "Season 6"
    elif datetime(2024, 4, 1) <= date <= datetime(2024, 6, 30):
        return "Season 7"
    elif datetime(2024, 7, 1) <= date <= datetime(2024, 9, 30):
        return "Season 8"
    elif datetime(2024, 10, 1) <= date <= datetime(2024, 12, 31):
        return "Season 9"
    elif datetime(2025, 1, 1) <= date <= datetime(2025, 3, 31):
        return "Season 10"
    elif datetime(2025, 4, 1) <= date <= datetime(2025, 6, 30):
        return "Season 11"
    elif datetime(2025, 7, 1) <= date <= datetime(2025, 9, 30):
        return "Season 12"
    elif datetime(2025, 10, 1) <= date <= datetime(2025, 12, 31):
        return "Season 13"
    else:
        return "Season 14"

# Function to process the results.csv and generate winrate overtime
def generate_winrate_overtime_json():
    # Create output folder if it doesn't exist
    output_folder = "player_winrate_overtime"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Data structures to track player stats
    player_events = defaultdict(list)  # List of events each player participated in
    player_results = defaultdict(list)  # List of win/loss results for each player

    # Read the CSV file
    with open('results.csv', 'r') as file:
        reader = csv.reader(file)
        current_event_players = set()
        event_lines = []
        event_date = None
        
        # Parse the CSV file row by row
        for row in reader:
            if len(row) == 0 or not row[0]:  # Skip empty rows
                continue

            # First line of each event (contains event header info)
            if len(row) == 5:
                if event_lines:
                    # Process the event results after the event header
                    for event_line in event_lines:
                        player1, player2, result = event_line
                        if player1 != player2:
                            player_events[player1].append(event_date)
                            player_events[player2].append(event_date)
                            player_results[player1].append(result)
                            player_results[player2].append("0" if result == "1" else "1")

                # Reset for new event
                event_lines = []
                try:
                    event_date = parse_date(row[4].strip())  # The date is in the 5th column (index 4)
                except ValueError as e:
                    print(f"Skipping row due to date error: {row}")
                    continue  # Skip this row if the date is invalid
                continue

            # For each matchup result line in the event
            if len(row) == 3:
                player1 = row[0].strip()
                player2 = row[1].strip()
                result = row[2].strip()

                # Store match results for the current event
                event_lines.append((player1, player2, result))

        # Filter players with at least 40 events
        qualified_players = {player for player, events in player_events.items() if len(events) >= 40}

        # Generate winrate data for each player
        for player in qualified_players:
            player_dates = player_events[player]
            player_wins_losses = player_results[player]

            # Only start collecting data after the 20th event, but still include first 20 matches in win/loss record
            player_dates = player_dates[20:]
            player_wins_losses = player_wins_losses[20:]

            seasons_data = defaultdict(lambda: {"date": [], "win_percentage": []})

            total_wins = 0
            total_matches = 0
            date_to_results = {}

            # Calculate winrate for the 21st event onward
            for i in range(len(player_dates)):
                event_date = player_dates[i]
                result = player_wins_losses[i]

                # Determine the season for this event
                current_season = get_season(event_date)

                # Update total wins and matches
                total_matches += 1
                total_wins += int(result)

                # Store win percentage for that date
                win_percentage = total_wins / total_matches if total_matches > 0 else 0
                # Only record the final result of the day (no duplicates for the same day)
                date_str = event_date.strftime("%m/%d/%Y")
                date_to_results[date_str] = win_percentage

            # Prepare the data for the JSON output
            # Sort the dates and their corresponding win percentages by date
            sorted_dates = sorted(date_to_results.items())
            
            # Assign sorted dates and win percentages to the season
            season_name = "Season 1"
            season_dates = []
            season_win_percentages = []
            for date, win_percentage in sorted_dates:
                season_dates.append(date)
                season_win_percentages.append(win_percentage)
            
            # Ensure all seasons are correctly populated with their dates and win percentages
            seasons_data[season_name] = {
                "date": season_dates,
                "win_percentage": season_win_percentages
            }

            # Sort the seasons numerically
            sorted_seasons = sorted(seasons_data.items(), key=lambda x: int(x[0].split(' ')[-1]))

            # Store the sorted data
            player_data = []
            for season_name, data in sorted_seasons:
                player_data.append({"seasonName": season_name, **data})

            # Write each player's data to a JSON
            with open(os.path.join(output_folder, f"{player}.json"), 'w') as f:
                json.dump(player_data, f, indent=4)

            print(f"Processed data for player: {player}")

if __name__ == "__main__":
    generate_winrate_overtime_json()
