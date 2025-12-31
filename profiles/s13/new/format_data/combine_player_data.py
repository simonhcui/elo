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
            with open(file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                # Get the base filename without the extension
                file_base_name = os.path.splitext(file_name)[0]

                # Process each entry for a player
                for entry in data:
                    player_name = entry["name"]
                    glicko = entry["glicko"]
                    
                    # If Glicko contains "Â" before the ± symbol, clean it up
                    if isinstance(glicko, str):
                        glicko = glicko.replace("Â", "").replace("\u00c2", "")
                    
                    player_entry = {
                        "Format": file_base_name,  # Remove .json and just use the base name
                        "Win %": entry["win_percentage"],
                        "Record": entry["wins_losses"],
                        "Drafts": entry["total_drafts"],
                        "Glicko": glicko
                    }
                    
                    # Add the player's entry to the player_data dictionary
                    if player_name not in player_data:
                        player_data[player_name] = []
                    player_data[player_name].append(player_entry)

    # Write the combined data for each player to a separate JSON file in the output folder
    for player_name, entries in player_data.items():
        player_file_path = os.path.join(output_folder, f"{player_name}")
        with open(player_file_path.lower() + "_format.json", "w", encoding="utf-8") as player_file:
            json.dump(entries, player_file, indent=4, ensure_ascii=False)
            print(f"Created file for player: {player_name}")

# Run the function
if __name__ == "__main__":
    combine_player_data()
