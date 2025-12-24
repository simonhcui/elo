import os
import json

# Define the function to process the JSON files
def combine_player_data():
    # Create a subfolder for the output files
    output_folder = "combined_player_data"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Dictionary to store combined data for players
    player_data = {}

    # Loop through all JSON files in the current directory
    for file_name in os.listdir():
        if file_name.endswith(".json"):  # Check if the file is a JSON file
            with open(file_name, "r") as f:
                data = json.load(f)
                
                # Process each entry for a player
                for entry in data:
                    player_name = entry["name"]
                    player_entry = {
                        "Format": file_name,  # Name of the file indicates the format
                        "Win %": entry["win_percentage"],
                        "Record": entry["wins_losses"],
                        "Drafts": entry["total_drafts"],
                        "Glicko": entry["glicko"]
                    }
                    
                    # Add the player's entry to the player_data dictionary
                    if player_name not in player_data:
                        player_data[player_name] = []
                    player_data[player_name].append(player_entry)

    # Write the combined data for each player to a separate JSON file in the output folder
    for player_name, entries in player_data.items():
        player_file_path = os.path.join(output_folder, f"{player_name}.json")
        with open(player_file_path, "w") as player_file:
            json.dump(entries, player_file, indent=4)
            print(f"Created file for player: {player_name}")

# Run the function
if __name__ == "__main__":
    combine_player_data()
