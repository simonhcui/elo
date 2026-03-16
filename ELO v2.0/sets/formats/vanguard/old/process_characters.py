import csv
import json
import sys
from collections import defaultdict

# ============================================================
# Add inactive character names to this list (case-sensitive)
# ============================================================
INACTIVE_CHARACTERS = [
    "Takara",
    "Barrin",
    "Titania",
    "Oracle",
    "Xantcha",
    "Squee",
    "Lyna",
    "Gerrard",
    "Multani",
    "Orim",
    "Sidar Kondo",
    "Sliver Queen Brood Mother",
    "Teysa Orzhov Scion",
    "Sakashima the Imposter",
    "Greven il-Vec"
    # "Mishra",
    # "Urza",
]

def process_file(input_path):
    records = defaultdict(lambda: {"wins": 0, "losses": 0, "drafts": 0})

    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line_num, row in enumerate(reader, start=1):
            # Skip blank lines or comment lines
            if not row or row[0].strip().startswith("#"):
                continue

            if len(row) < 3:
                print(f"Warning: Line {line_num} has fewer than 3 fields, skipping: {row}")
                continue

            try:
                wins = int(row[0].strip())
                losses = int(row[1].strip())
                character = row[2].strip()
            except ValueError:
                print(f"Warning: Line {line_num} has invalid win/loss values, skipping: {row}")
                continue

            records[character]["wins"] += wins
            records[character]["losses"] += losses
            records[character]["drafts"] += 1

    return records


def build_table_data(records):
    """Convert records dict into a sorted list of table row dicts."""
    rows = []
    for name, data in records.items():
        total_games = data["wins"] + data["losses"]
        win_pct = (data["wins"] / total_games * 100) if total_games > 0 else 0.0
        rows.append({
            "name": name,
            "win_percentage_float": win_pct,
            "wins": data["wins"],
            "losses": data["losses"],
            "total_drafts": data["drafts"],
        })

    # Sort by win percentage descending, then total wins descending as tiebreaker
    rows.sort(key=lambda r: (r["win_percentage_float"], r["wins"]), reverse=True)

    table_data = []
    for rank, row in enumerate(rows, start=1):
        table_data.append({
            "rank": str(rank),
            "name": row["name"],
            "win_percentage": f"{row['win_percentage_float']:.2f}%",
            "wins_losses": f"{row['wins']}-{row['losses']}",
            "total_drafts": str(row["total_drafts"]),
        })

    return table_data


def main():
    if len(sys.argv) < 2:
        print("Usage: python process_characters.py <input_file.txt>")
        sys.exit(1)

    input_path = sys.argv[1]
    inactive_set = set(INACTIVE_CHARACTERS)

    print(f"Reading from: {input_path}")
    print(f"Inactive characters: {inactive_set if inactive_set else '(none)'}")

    all_records = process_file(input_path)

    active_records = {k: v for k, v in all_records.items() if k not in inactive_set}
    inactive_records = {k: v for k, v in all_records.items() if k in inactive_set}

    # Warn about inactive characters listed but not found in the data
    for name in inactive_set:
        if name not in all_records:
            print(f"Warning: Inactive character '{name}' was not found in the input data.")

    active_output = {"tableData": build_table_data(active_records)}
    inactive_output = {"tableData": build_table_data(inactive_records)}

    active_path = "active_characters.json"
    inactive_path = "inactive_characters.json"

    with open(active_path, "w", encoding="utf-8") as f:
        json.dump(active_output, f, indent=2)
    print(f"Active characters written to:   {active_path}  ({len(active_records)} characters)")

    with open(inactive_path, "w", encoding="utf-8") as f:
        json.dump(inactive_output, f, indent=2)
    print(f"Inactive characters written to: {inactive_path}  ({len(inactive_records)} characters)")


if __name__ == "__main__":
    main()
