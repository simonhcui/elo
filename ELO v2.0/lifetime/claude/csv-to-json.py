import csv
import json

def read_csv_to_dict(csv_filepath):
    """Read CSV file and return list of dictionaries."""
    data = []
    with open(csv_filepath, 'r', encoding='cp1252') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def format_win_percentage(win_pct_str):
    """Format win percentage as XX.XX%"""
    try:
        win_pct = float(win_pct_str)
        return f"{win_pct * 100:.2f}%"
    except (ValueError, TypeError):
        return win_pct_str

def format_glicko(glicko_str):
    """Format glicko as 'rating ± deviation' rounded to nearest ones place"""
    try:
        # Split on ± symbol
        parts = glicko_str.replace('±', '±').split('±')
        if len(parts) == 2:
            rating = round(float(parts[0].strip()))
            deviation = round(float(parts[1].strip()))
            return f"{rating} ± {deviation}"
        return glicko_str
    except (ValueError, TypeError, AttributeError):
        return glicko_str

def format_gxe(gxe_str):
    """Format GXE as XX.XX%"""
    try:
        gxe = float(gxe_str)
        return f"{gxe:.2f}%"
    except (ValueError, TypeError):
        return gxe_str

def transform_to_json_format(data):
    """Transform CSV data to the specified JSON format."""
    # Filter players with more than 4 drafts
    filtered_data = []
    for row in data:
        try:
            num_drafts = int(row.get('Num Drafts', '0'))
            if num_drafts > 4:
                filtered_data.append(row)
        except (ValueError, TypeError):
            continue
    
    # Sort by win percentage descending
    filtered_data.sort(key=lambda x: float(x.get('Win %', '0')), reverse=True)
    
    result = []
    for rank, row in enumerate(filtered_data, start=1):
        player_entry = {
            "rank": str(rank),
            "name": row.get('Player', ''),
            "win_percentage": format_win_percentage(row.get('Win %', '')),
            "wins_losses": f"{row.get('Wins', '0')}-{row.get('Losses', '0')}",
            "total_drafts": row.get('Num Drafts', ''),
            "glicko": format_glicko(row.get('Glicko', '')),
            "gxe": format_gxe(row.get('GXE', '')),
            "last_set": row.get('Last Set Drafted', ''),
            "last_date": row.get('Last Date Drafted', '')
        }
        result.append(player_entry)
    
    return result

def write_json(data, json_filepath):
    """Write data to JSON file."""
    with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)

def main():
    csv_file = 'data.csv'
    json_file = 'output.json'
    
    print(f"Reading CSV from: {csv_file}")
    csv_data = read_csv_to_dict(csv_file)
    print(f"Read {len(csv_data)} rows")
    
    print("Transforming data...")
    transformed_data = transform_to_json_format(csv_data)
    
    print(f"Writing JSON to: {json_file}")
    write_json(transformed_data, json_file)
    print(f"Successfully created {json_file} with {len(transformed_data)} player entries!")

if __name__ == "__main__":
    main()